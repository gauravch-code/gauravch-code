# Gaurav Chintakunta

**AI engineer building agents that are observable, bounded, and grounded in real workflows.**

MS Computer Science, University of Illinois Chicago (May 2026, GPA 3.89). I work on local-first AI, agent evaluation and observability, RAG, synthetic training data, and full-stack products in Python, Go and TypeScript. My fixes are merged into open-source AI tools like **Haystack** and **OpenSRE**.

Based in New Jersey · Open to full-time AI Engineer, ML Engineer and Software Engineer roles · OPT work authorization

[**Portfolio**](https://gauravch-code.github.io/Portfolio/) · [Email](mailto:gaurav.pvt25@gmail.com) · [LinkedIn](https://www.linkedin.com/in/gauravchintak/) · [Resume](https://gauravch-code.github.io/Portfolio/Gaurav_Resume.pdf)

---

## Featured work

Every project has a live, in-browser demo. No sign-up and no API key needed.

<table>
<tr>
<td width="50%" valign="top">

<a href="https://gauravch-code.github.io/winnow/"><img src="https://gauravch-code.github.io/Portfolio/assets/winnow.webp" alt="Winnow live demo" /></a>

### [Winnow](https://github.com/gauravch-code/winnow)
**Local-first AI inbox triage.** A scikit-learn + MiniLM classifier sorts mail in about 5 ms on CPU and calls a PydanticAI fallback only when it isn't confident. Corrections feed a guarded retraining loop, and every route comes with an explanation.

[**Live demo →**](https://gauravch-code.github.io/winnow/) · [Source](https://github.com/gauravch-code/winnow)

`Python` `FastAPI` `PydanticAI` `scikit-learn` `Sentence Transformers` `Postgres` `Next.js`

</td>
<td width="50%" valign="top">

<a href="https://gauravch-code.github.io/TraceGuard/"><img src="https://gauravch-code.github.io/Portfolio/assets/traceguard.webp" alt="TraceGuard live demo" /></a>

### [TraceGuard](https://github.com/gauravch-code/TraceGuard)
**An operations console for AI agents.** It records every run, exposes each step and tool call, and puts generated support drafts into a human review queue. External agents can send their own traces through an ingestion API.

[**Live demo →**](https://gauravch-code.github.io/TraceGuard/) · [Source](https://github.com/gauravch-code/TraceGuard)

`TypeScript` `Next.js` `OpenAI` `Cloudflare Workers` `D1` `Drizzle`

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://gauravch-code.github.io/Agentic-SRE-Pipeline/"><img src="https://gauravch-code.github.io/Portfolio/assets/sre.webp" alt="Agentic SRE Pipeline live demo" /></a>

### [Agentic SRE Pipeline](https://github.com/gauravch-code/Agentic-SRE-Pipeline)
**Autonomous Kubernetes remediation with guardrails.** A Go watchdog polls Prometheus, and a CrewAI orchestrator gathers evidence through four allowlisted MCP tools. It restarts on the first alert and doubles the memory limit only if the problem recurs.

[**Live demo →**](https://gauravch-code.github.io/Agentic-SRE-Pipeline/) · [Source](https://github.com/gauravch-code/Agentic-SRE-Pipeline)

`Go` `Python` `CrewAI` `MCP` `Kubernetes` `Prometheus`

</td>
<td width="50%" valign="top">

<a href="https://gauravch-code.github.io/toolgen/"><img src="https://gauravch-code.github.io/Portfolio/assets/toolgen.webp" alt="Toolgen live demo" /></a>

### [Toolgen](https://github.com/gauravch-code/toolgen)
**Training data for tool-using agents.** It turns ToolBench schemas into grounded multi-turn conversations: an endpoint graph, connected tool chains, schema-valid mock execution with session state, and an LLM judge with a repair loop.

[**Live demo →**](https://gauravch-code.github.io/toolgen/) · [Source](https://github.com/gauravch-code/toolgen)

`Python` `Pydantic` `NetworkX` `OpenAI` `LLM-as-judge`

</td>
</tr>
</table>

---

## Open source

Each fix is a real bug I found, reproduced, fixed and covered with a regression test. The status badges update live.

| Project | What I fixed | Status |
|---|---|---|
| [**OpenSRE**](https://github.com/Tracer-Cloud/opensre) ![stars](https://img.shields.io/github/stars/Tracer-Cloud/opensre?style=flat&label=%E2%98%85&color=555) | [Evidence-grounded root-cause analysis](https://github.com/Tracer-Cloud/opensre/pull/716): a structured RCA prompt with an alternative-hypothesis output, which cut false-positive classifications by 30% | ![state](https://img.shields.io/github/pulls/detail/state/Tracer-Cloud/opensre/716) |
| [**Haystack**](https://github.com/deepset-ai/haystack) ![stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=flat&label=%E2%98%85&color=555) | [MetaFieldRanker ignored its missing-meta policy](https://github.com/deepset-ai/haystack/pull/12863): one `None` metadata value silently turned off ranking for the whole batch | ![state](https://img.shields.io/github/pulls/detail/state/deepset-ai/haystack/12863) |
| [**Sentence Transformers**](https://github.com/huggingface/sentence-transformers) ![stars](https://img.shields.io/github/stars/huggingface/sentence-transformers?style=flat&label=%E2%98%85&color=555) | [Hard-negative mining skipped the CrossEncoder](https://github.com/huggingface/sentence-transformers/pull/4073) when `min_score` was the only filter | ![state](https://img.shields.io/github/pulls/detail/state/huggingface/sentence-transformers/4073) |
| [**browser-use**](https://github.com/browser-use/browser-use) ![stars](https://img.shields.io/github/stars/browser-use/browser-use?style=flat&label=%E2%98%85&color=555) | [`send_keys` treated "center" as an Enter key](https://github.com/browser-use/browser-use/pull/5690) and added a navigation wait to ordinary typing | ![state](https://img.shields.io/github/pulls/detail/state/browser-use/browser-use/5690) |
| [**Diffusers**](https://github.com/huggingface/diffusers) ![stars](https://img.shields.io/github/stars/huggingface/diffusers?style=flat&label=%E2%98%85&color=555) | [Positional config arguments were lost](https://github.com/huggingface/diffusers/pull/14708) on a `from_config` round-trip | ![state](https://img.shields.io/github/pulls/detail/state/huggingface/diffusers/14708) |
| [**Chroma**](https://github.com/chroma-core/chroma) ![stars](https://img.shields.io/github/stars/chroma-core/chroma?style=flat&label=%E2%98%85&color=555) | [Collection names with invisible whitespace](https://github.com/chroma-core/chroma/pull/7610) are now rejected with a clear error | ![state](https://img.shields.io/github/pulls/detail/state/chroma-core/chroma/7610) |

---

## Contribution activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/gauravch-code/gauravch-code/output/github-snake-dark.svg" />
    <img alt="Gaurav's GitHub contribution grid, animated as a snake eating each day's contributions. Regenerated daily." src="https://raw.githubusercontent.com/gauravch-code/gauravch-code/output/github-snake.svg" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=gauravch-code&theme=github_dark" />
    <img alt="Gaurav's GitHub contributions over the last year" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=gauravch-code&theme=default" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=gauravch-code&theme=dark&background=0D1117&ring=2DD4BF&fire=2DD4BF&currStreakLabel=2DD4BF&hide_border=true" />
    <img alt="Gaurav's GitHub contribution streak" src="https://streak-stats.demolab.com?user=gauravch-code&ring=0D9488&fire=0D9488&currStreakLabel=0D9488&hide_border=true" />
  </picture>
</p>

---

## Engineering toolbox

**Languages:** Python, Go, TypeScript, JavaScript, SQL, Scala, C

**AI and agents:** PyTorch, Transformers, PydanticAI, CrewAI, LangGraph, LangChain, MCP, DSPy, RAG, Sentence Transformers, scikit-learn

**Backend and data:** FastAPI, Flask, Next.js, Postgres, SQLAlchemy, Drizzle, Pinecone, Pandas, NumPy, Spark

**Infrastructure:** Kubernetes, Docker, Prometheus, Cloudflare Workers, AWS, Azure, GitHub Actions, Linux

---

## Let's connect

I'm interested in teams building AI agents, evaluation and observability infrastructure, developer tools and full-stack ML products. Reach me at [gaurav.pvt25@gmail.com](mailto:gaurav.pvt25@gmail.com), on [LinkedIn](https://www.linkedin.com/in/gauravchintak/), or through my [portfolio](https://gauravch-code.github.io/Portfolio/).
