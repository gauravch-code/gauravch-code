# Gaurav Chintak

**AI engineer building agentic systems that are useful, observable, and grounded in real workflows.**

I am an MS Computer Science graduate from the University of Illinois Chicago (May 2026, GPA 3.89). My work spans local-first AI, agent evaluation and observability, RAG, synthetic data generation, and full-stack products in Python, Go, and TypeScript.

Based in New Jersey | Open to full-time AI Engineer, ML Engineer, and Software Engineer roles | OPT work authorization

[Email](mailto:gaurav.pvt25@gmail.com) | [LinkedIn](https://www.linkedin.com/in/gauravchintak/) | [Portfolio](https://gauravch-code.github.io/Portfolio/)

---

## Featured Work

### [Winnow](https://github.com/gauravch-code/winnow) - Local-first AI inbox triage

[Live demo](https://gauravch-code.github.io/winnow/) | [Source code](https://github.com/gauravch-code/winnow)

Winnow classifies email locally before deciding whether an LLM is needed. A scikit-learn model with MiniLM embeddings handles confident messages in roughly 5 ms on CPU; uncertain cases can opt into a PydanticAI fallback. User corrections become training data for a guarded retraining loop, and every decision remains explainable.

`Python` `FastAPI` `PydanticAI` `scikit-learn` `Sentence Transformers` `Postgres` `Next.js` `TypeScript`

### [TraceGuard](https://github.com/gauravch-code/TraceGuard) - AI agent run tracing and review

[Live demo](https://gauravch-code.github.io/TraceGuard/) | [Source code](https://github.com/gauravch-code/TraceGuard)

TraceGuard records AI-agent runs, exposes each step and tool call, and places generated support drafts into a human review queue. It includes a working support-agent example plus an ingestion API that lets external agents submit their own traces.

`TypeScript` `Next.js` `OpenAI` `Cloudflare Workers` `D1` `Drizzle`

### [Agentic SRE Pipeline](https://github.com/gauravch-code/Agentic-SRE-Pipeline) - Autonomous Kubernetes remediation

[Live demo](https://gauravch-code.github.io/Agentic-SRE-Pipeline/) | [Source code](https://github.com/gauravch-code/Agentic-SRE-Pipeline)

A Go watchdog polls Prometheus for memory pressure and sends incidents to a CrewAI orchestrator. Four allowlisted MCP tools collect evidence and perform bounded remediation: restart on the first alert, then double the memory limit only when the problem recurs inside the escalation window.

`Go` `Python` `CrewAI` `MCP` `Kubernetes` `Prometheus` `Flask`

### [Toolgen](https://github.com/gauravch-code/toolgen) - Tool-use training data generator

[Live demo](https://gauravch-code.github.io/toolgen/) | [Source code](https://github.com/gauravch-code/toolgen)

Toolgen turns ToolBench schemas into grounded, multi-turn training conversations. It builds an endpoint graph, samples connected tool chains, executes schema-valid mock responses with session state, and uses an LLM judge plus repair loop to protect dataset quality and diversity.

`Python` `Pydantic` `NetworkX` `OpenAI` `Faker` `Multi-agent systems` `LLM-as-judge`

---

## Open Source

### [OpenSRE](https://github.com/Tracer-Cloud/opensre/pull/716)

Contributed a structured root-cause analysis prompt, alternative-hypothesis output, and a backward-compatible response parser for mixed-signal incidents.

---

## Engineering Toolbox

**Languages:** Python, Go, TypeScript, JavaScript, SQL, Scala, C

**AI and ML:** PyTorch, TensorFlow, PydanticAI, CrewAI, LangGraph, LangChain, MCP, DSPy, Transformers, RAG, Sentence Transformers, scikit-learn

**Backend and data:** FastAPI, Flask, Next.js, Postgres, SQLAlchemy, Drizzle, Pinecone, Pandas, NumPy, Spark

**Infrastructure:** Kubernetes, Docker, Prometheus, Cloudflare Workers, AWS, Azure, GitHub Actions, Linux

---

## Let's Connect

I am interested in teams building AI agents, evaluation infrastructure, developer tools, and full-stack ML products. Reach me at [gaurav.pvt25@gmail.com](mailto:gaurav.pvt25@gmail.com) or on [LinkedIn](https://www.linkedin.com/in/gauravchintak/).
