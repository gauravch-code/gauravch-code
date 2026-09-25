"""Rebuild the open-source section of the profile README from live GitHub data.

Lists every pull request I've opened against someone else's repository, merged ones first.
Closed-without-merge PRs are left out. Runs daily from .github/workflows/update-readme.yml.
"""

import json
import os
import re
import urllib.request
from datetime import datetime

USER = "gauravch-code"
README = "README.md"
START, END = "<!-- oss:start -->", "<!-- oss:end -->"
# Leading "[fix]" / "[BUG](types):" tags and conventional-commit prefixes like "fix(scope):"
PREFIX = re.compile(r"^\s*(?:\[[^\]]+\]\s*)?(?:\([^)]*\)\s*:?\s*)?(?:[a-z]+(?:\([^)]*\))?!?:\s*)?", re.IGNORECASE)
ISSUE_REF = re.compile(r"\s*\((?:fixes|closes|resolves)\s+#\d+\)\s*$", re.IGNORECASE)


def api(path: str) -> dict:
    req = urllib.request.Request(f"https://api.github.com/{path}", headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def stars(n: int) -> str:
    if n >= 100_000:
        return f"{n // 1000}k"
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def title(raw: str) -> str:
    text = ISSUE_REF.sub("", PREFIX.sub("", raw)).strip()
    return text[:1].upper() + text[1:]


def build() -> str:
    items = api(f"search/issues?q=author:{USER}+is:pr+-user:{USER}&sort=created&order=desc&per_page=100")["items"]
    rows, repo_stars = [], {}
    for pr in items:
        repo = pr["repository_url"].split("/repos/")[1]
        merged_at = pr["pull_request"].get("merged_at")
        if pr["state"] == "closed" and not merged_at:
            continue
        if repo not in repo_stars:
            repo_stars[repo] = api(f"repos/{repo}")["stargazers_count"]
        date = (merged_at or pr["created_at"])[:10]
        rows.append({"repo": repo, "merged": bool(merged_at), "date": date, "title": title(pr["title"]), "url": pr["html_url"]})
    # Merged first, then newest first within each group
    rows.sort(key=lambda r: (not r["merged"], -int(r["date"].replace("-", ""))))

    merged = sum(r["merged"] for r in rows)
    lines = [
        f"**{merged} merged · {len(rows) - merged} in review** across {len(repo_stars)} projects. "
        f"_Rebuilt daily from the GitHub API ([how](.github/workflows/update-readme.yml))._",
        "",
        "| | Project | Pull request | Date |",
        "|---|---|---|---|",
    ]
    for r in rows:
        status = "✅ Merged" if r["merged"] else "🔄 In review"
        name = r["repo"].split("/")[1]
        lines.append(
            f"| {status} | [**{name}**](https://github.com/{r['repo']}) ★ {stars(repo_stars[r['repo']])} "
            f"| [{r['title']}]({r['url']}) | {datetime.fromisoformat(r['date']).strftime('%b %Y')} |"
        )
    return "\n".join(lines)


def main() -> None:
    with open(README, encoding="utf-8") as f:
        readme = f.read()
    section = f"{START}\n{build()}\n{END}"
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: section, readme, flags=re.DOTALL)
    if updated != readme:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated)
        print("README updated")
    else:
        print("No changes")


if __name__ == "__main__":
    main()
