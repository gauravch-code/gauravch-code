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

I find real bugs in AI tools, reproduce them, and ship the fix with a regression test.

<!-- oss:start -->
**2 merged · 6 in review** across 8 projects. _Rebuilt daily from the GitHub API ([how](.github/workflows/update-readme.yml))._

| | Project | Pull request | Date |
|---|---|---|---|
| ✅ Merged | [**haystack**](https://github.com/deepset-ai/haystack) ★ 26.6k | [Treat None meta values as missing in MetaFieldRanker](https://github.com/deepset-ai/haystack/pull/12863) | Sep 2026 |
| ✅ Merged | [**opensre**](https://github.com/Tracer-Cloud/opensre) ★ 11.2k | [Improve RCA prompt for evidence-grounded diagnosis](https://github.com/Tracer-Cloud/opensre/pull/716) | Apr 2026 |
| 🔄 In review | [**sentence-transformers**](https://github.com/huggingface/sentence-transformers) ★ 19.1k | [Rescore with the CrossEncoder when only min_score is set in mine_hard_negatives](https://github.com/huggingface/sentence-transformers/pull/4073) | Sep 2026 |
| 🔄 In review | [**zed**](https://github.com/zed-industries/zed) ★ 90.9k | [Fix thread switcher registration after enabling AI](https://github.com/zed-industries/zed/pull/63992) | Sep 2026 |
| 🔄 In review | [**agno**](https://github.com/agno-agi/agno) ★ 42.3k | [Restore direct answers for simple route-mode requests](https://github.com/agno-agi/agno/pull/10072) | Sep 2026 |
| 🔄 In review | [**browser-use**](https://github.com/browser-use/browser-use) ★ 116k | [Replace Enter substring matching with dispatched-key tracking in send_keys](https://github.com/browser-use/browser-use/pull/5690) | Sep 2026 |
| 🔄 In review | [**diffusers**](https://github.com/huggingface/diffusers) ★ 34.6k | [Preserve positional __init__ args through from_config round trips](https://github.com/huggingface/diffusers/pull/14708) | Sep 2026 |
| 🔄 In review | [**chroma**](https://github.com/chroma-core/chroma) ★ 29.4k | [Reject whitespace-padded names](https://github.com/chroma-core/chroma/pull/7610) | Aug 2026 |
<!-- oss:end -->

---

## Engineering toolbox

**Languages:** Python, Go, TypeScript, JavaScript, SQL, Scala, C

**AI and agents:** PyTorch, Transformers, PydanticAI, CrewAI, LangGraph, LangChain, MCP, DSPy, RAG, Sentence Transformers, scikit-learn

**Backend and data:** FastAPI, Flask, Next.js, Postgres, SQLAlchemy, Drizzle, Pinecone, Pandas, NumPy, Spark

**Infrastructure:** Kubernetes, Docker, Prometheus, Cloudflare Workers, AWS, Azure, GitHub Actions, Linux

---

## Let's connect

I'm interested in teams building AI agents, evaluation and observability infrastructure, developer tools and full-stack ML products. Reach me at [gaurav.pvt25@gmail.com](mailto:gaurav.pvt25@gmail.com), on [LinkedIn](https://www.linkedin.com/in/gauravchintak/), or through my [portfolio](https://gauravch-code.github.io/Portfolio/).
