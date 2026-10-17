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
**8 merged · 18 in review** across 25 projects. _Rebuilt daily from the GitHub API ([how](.github/workflows/update-readme.yml))._

| | Project | Pull request | Date |
|---|---|---|---|
| ✅ Merged | [**composio**](https://github.com/ComposioHQ/composio) ★ 30.6k | [Fix Pydantic field aliases in Python tool execution](https://github.com/ComposioHQ/composio/pull/4907) | Oct 2026 |
| ✅ Merged | [**baml**](https://github.com/BoundaryML/baml) ★ 9.4k | [Teach initialize_runtime to handle trailing slashes](https://github.com/BoundaryML/baml/pull/5223) | Oct 2026 |
| ✅ Merged | [**cli**](https://github.com/fosrl/cli) ★ 60 | [Select ARMv6 binary on armv6l](https://github.com/fosrl/cli/pull/158) | Oct 2026 |
| ✅ Merged | [**txtai**](https://github.com/neuml/txtai) ★ 13k | [Preserve ordered-list start values in HTMLToMarkdown](https://github.com/neuml/txtai/pull/1356) | Oct 2026 |
| ✅ Merged | [**sentence-transformers**](https://github.com/huggingface/sentence-transformers) ★ 19.2k | [Rescore with the CrossEncoder when only min_score is set in mine_hard_negatives](https://github.com/huggingface/sentence-transformers/pull/4073) | Oct 2026 |
| ✅ Merged | [**txtai**](https://github.com/neuml/txtai) ★ 13k | [Skip NULL aggregate values from shards with no matching rows](https://github.com/neuml/txtai/pull/1331) | Oct 2026 |
| ✅ Merged | [**haystack**](https://github.com/deepset-ai/haystack) ★ 26.8k | [Treat None meta values as missing in MetaFieldRanker](https://github.com/deepset-ai/haystack/pull/12863) | Sep 2026 |
| ✅ Merged | [**opensre**](https://github.com/Tracer-Cloud/opensre) ★ 12k | [Improve RCA prompt for evidence-grounded diagnosis](https://github.com/Tracer-Cloud/opensre/pull/716) | Apr 2026 |
| 🔄 In review | [**retell-client-js-sdk**](https://github.com/RetellAI/retell-client-js-sdk) ★ 22 | [Prevent call takeover after the monitor disconnects](https://github.com/RetellAI/retell-client-js-sdk/pull/35) | Oct 2026 |
| 🔄 In review | [**hud-python**](https://github.com/hud-evals/hud-python) ★ 313 | [Keep provider outages out of evaluation scores](https://github.com/hud-evals/hud-python/pull/722) | Oct 2026 |
| 🔄 In review | [**bland-plugins**](https://github.com/CINTELLILABS/bland-plugins) ★ 0 | [Use the active Claude profile when switching Bland servers](https://github.com/CINTELLILABS/bland-plugins/pull/28) | Oct 2026 |
| 🔄 In review | [**lemma**](https://github.com/uselemma/lemma) ★ 8 | [Fix missing errors for handled LangChain tool failures](https://github.com/uselemma/lemma/pull/121) | Oct 2026 |
| 🔄 In review | [**agentphone-mcp**](https://github.com/AgentPhone-AI/agentphone-mcp) ★ 125 | [Let MCP clients page through messages and agents](https://github.com/AgentPhone-AI/agentphone-mcp/pull/83) | Oct 2026 |
| 🔄 In review | [**openclaw-plugin**](https://github.com/agentmail-to/openclaw-plugin) ★ 3 | [Fix HTML extraction with newer OpenClaw SDK exports](https://github.com/agentmail-to/openclaw-plugin/pull/21) | Oct 2026 |
| 🔄 In review | [**posthog-js**](https://github.com/PostHog/posthog-js) ★ 633 | [Support Kotlin Gradle files in the Expo plugin](https://github.com/PostHog/posthog-js/pull/5283) | Oct 2026 |
| 🔄 In review | [**ssi**](https://github.com/spruceid/ssi) ★ 264 | [Preserve the original header when verifying detached JWS signatures](https://github.com/spruceid/ssi/pull/711) | Oct 2026 |
| 🔄 In review | [**magnitude**](https://github.com/magnitudedev/magnitude) ★ 7k | [Remove stale headers from local Codex WebSocket requests](https://github.com/magnitudedev/magnitude/pull/180) | Oct 2026 |
| 🔄 In review | [**MentraOS**](https://github.com/Mentra-Community/MentraOS) ★ 2.4k | [Fix Japanese voice-follow scrolling in the teleprompter](https://github.com/Mentra-Community/MentraOS/pull/4585) | Oct 2026 |
| 🔄 In review | [**ubicloud**](https://github.com/ubicloud/ubicloud) ★ 12.3k | [Ignore extra_float_digits in PgBouncer by default](https://github.com/ubicloud/ubicloud/pull/6630) | Oct 2026 |
| 🔄 In review | [**datasets**](https://github.com/huggingface/datasets) ★ 22.1k | [Support TensorFlow conversion of Dataset columns](https://github.com/huggingface/datasets/pull/8756) | Oct 2026 |
| 🔄 In review | [**typescript-sdk**](https://github.com/modelcontextprotocol/typescript-sdk) ★ 13.6k | [Fix URI template optional query matching](https://github.com/modelcontextprotocol/typescript-sdk/pull/2909) | Sep 2026 |
| 🔄 In review | [**zed**](https://github.com/zed-industries/zed) ★ 91.8k | [Fix thread switcher registration after enabling AI](https://github.com/zed-industries/zed/pull/63992) | Sep 2026 |
| 🔄 In review | [**agno**](https://github.com/agno-agi/agno) ★ 42.8k | [Restore direct answers for simple route-mode requests](https://github.com/agno-agi/agno/pull/10072) | Sep 2026 |
| 🔄 In review | [**browser-use**](https://github.com/browser-use/browser-use) ★ 118k | [Replace Enter substring matching with dispatched-key tracking in send_keys](https://github.com/browser-use/browser-use/pull/5690) | Sep 2026 |
| 🔄 In review | [**diffusers**](https://github.com/huggingface/diffusers) ★ 34.7k | [Preserve positional __init__ args through from_config round trips](https://github.com/huggingface/diffusers/pull/14708) | Sep 2026 |
| 🔄 In review | [**chroma**](https://github.com/chroma-core/chroma) ★ 29.5k | [Reject whitespace-padded names](https://github.com/chroma-core/chroma/pull/7610) | Aug 2026 |
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
