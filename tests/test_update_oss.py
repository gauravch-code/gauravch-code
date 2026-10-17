import unittest
from unittest.mock import patch

from scripts import update_oss


class BuildTests(unittest.TestCase):
    def test_only_merged_prs_are_listed_and_counted(self):
        def pr(number, repo, state, merged_at):
            return {
                "repository_url": f"https://api.github.com/repos/{repo}",
                "state": state,
                "pull_request": {"merged_at": merged_at},
                "title": f"fix: Contribution {number}",
                "html_url": f"https://github.com/{repo}/pull/{number}",
            }

        items = [
            pr(1, "team/first", "closed", "2026-10-01T12:00:00Z"),
            pr(2, "team/pending", "open", None),
            pr(3, "team/rejected", "closed", None),
            pr(4, "team/first", "closed", "2026-10-15T12:00:00Z"),
            pr(5, "team/second", "closed", "2026-10-16T12:00:00Z"),
        ]
        with patch.object(update_oss, "api") as api:
            api.side_effect = [
                {"items": items},
                {"stargazers_count": 100},
                {"stargazers_count": 200},
            ]
            section = update_oss.build()

        self.assertIn("is:merged", api.call_args_list[0].args[0])
        self.assertEqual(api.call_count, 3)
        self.assertIn("3 merged PRs across 2 projects", section)
        self.assertNotIn("pending", section)
        self.assertNotIn("rejected", section)
        self.assertNotIn("in review", section)
        self.assertLess(section.index("Contribution 5"), section.index("Contribution 4"))
        self.assertLess(section.index("Contribution 4"), section.index("Contribution 1"))

    def test_empty_history_has_no_pending_entries(self):
        with patch.object(update_oss, "api", return_value={"items": []}):
            section = update_oss.build()
        self.assertIn("0 merged PRs across 0 projects", section)
        self.assertNotIn("in review", section)


if __name__ == "__main__":
    unittest.main()
