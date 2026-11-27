---
title: "GDE-0003 WP3: Requirements and Architecture Design"
id: GDE-0003
type: guide
status: active
created: "2026-11-27"
tags: [plenergy-ai, wp3, requirements, architecture, kpi, kickoff]
related: [GDE-0001, GDE-0002, GDE-0004]
---

## Overview

This guide describes how WP3 *Requirements and Architecture Design* is implemented. KTH leads WP3, so the guide is written for the WP leader and is also the base for the kickoff presentation to all partners. The kickoff takes place at AIT in Vienna on 30 November and 1 December 2026; WP3 has the slot on day 1 at 16:45 (45 minutes), see [Kickoff Meeting Context](#kickoff-meeting-context). The deck is in `site/slides/wp3-kickoff.qmd`.

The guide separates two kinds of content:

- **From the proposal**: scope, tasks, partners, effort, deliverables, timing. These are commitments.
- **Proposed**: how the WP leader suggests carrying out the work (work plan by month, templates, decision rules). These are suggestions to discuss with the partners and are marked *Proposed*.

Read [GDE-0001](GDE-0001-plenergy-ai-overview.md) and [GDE-0002](GDE-0002-plenergy-ai-implementation.md) first for the project context. WP6, the other WP led by KTH, is in [GDE-0004](GDE-0004-wp6-use-case-validation-and-performance-assessment.md).

## WP3 at a Glance

| Item                    | Value                                                                                                                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lead                    | KTH                                                                                                                                                                                             |
| Duration                | M01–M09 (the Swedish project starts on 2026-11-01, so M09 is July 2027)                                                                                                                         |
| Effort                  | 37.6 person-months                                                                                                                                                                              |
| Target maturity         | TRL 3, as the starting point of the TRL 3 to 5 path                                                                                                                                             |
| Tasks                   | T3.1 Use Case Blueprints & Semantic Scoping (KTH lead), T3.2 Stakeholder Validation, KPIs & Impact Planning (KTH lead), T3.3 Modular System Architecture & Trust-by-Design Blueprint (AIT lead) |
| Deliverables            | D3.1 Use Case Blueprint Portfolio, D3.2 Validation & Impact Framework, D3.3 Trust-by-Design Architecture Specification, all at M09                                                              |
| Milestone               | M3 Architecture & Requirements Freeze (M09)                                                                                                                                                     |
| Workshop                | WS1 Co-Creation at M3                                                                                                                                                                           |
| Swedish funding for WP3 | 2 102 787 SEK across KTH, EIN and ProptechOS (Energimyndigheten proposal)                                                                                                                       |

Note: ProptechOS is the new name of IDUN, the same legal entity. The international proposal still says IDUN.

### Effort by partner

| Partner           | PMs  | Main contribution to WP3                                                                |
| ----------------- | ---- | --------------------------------------------------------------------------------------- |
| KTH               | 11.0 | WP leadership, T3.1 and T3.2 leads, KPI framework, Swedish pilot requirements           |
| EIN               | 7.0  | User and stakeholder requirements from the Hammarby Sjöstad pilot, Living Lab workshops |
| AIT               | 5.6  | T3.3 lead, architecture, semantic scoping, ECP and ESLA requirements for Austria        |
| IMT               | 5.0  | Explainability and trust requirements, semantic web standards                           |
| UNICA             | 3.0  | Semantic scoping (IEC CIM, PECO extensions), ECP requirements for Italy                 |
| IDUN / ProptechOS | 3.0  | Building data integration and platform interoperability requirements                    |
| FLOSS             | 2.0  | Implementation feasibility of the architecture, runtime and UI requirements             |
| TRI               | 1.0  | EU AI Act compliance and audit requirements                                             |

## Purpose and Position in the Project

WP3 is the first technical WP and sets the frame for all the others. It answers three questions before WP4 and WP5 start building:

1. What exactly must each use case (ECP, EDCR, ESLA) do, for whom, with which data?
2. How do we know it works? Which KPIs, which baselines, which evaluation method?
3. Which components exist, how do they talk to each other, and where are security, data sovereignty and human oversight enforced?

```text
Stakeholders (ECs, DSOs, regulators, tech providers)
        │ co-creation, MSAB
        ▼
   WP3  T3.1 blueprints ─┬─> WP4 (neuro-symbolic models, federation, XAI methods)
        T3.2 KPI framework ─┼─> WP6 (what gets measured and how)
        T3.3 architecture ──┴─> WP5 (what gets built, interfaces, security)
```

| Output                    | Used by       | How                                                                                                                         |
| ------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| D3.1 Blueprints           | WP4, WP5      | Workflows and data requirements guide the neuro-symbolic modelling (WP4) and the data layer and toolboxes (WP5)             |
| D3.2 Validation framework | WP6, WP2      | KPI scorecard and evaluation method for pilots and for reporting                                                            |
| D3.3 Architecture         | WP5, WP4, WP1 | Master technical blueprint for T5.1 and T5.2, human-intervention interfaces for T5.3 and T5.4, compliance evidence for T1.2 |

Once D3.1 to D3.3 are signed off at M09, the requirements and the architecture are frozen. Changes after M09 go through a controlled change process (see [Governance](#governance-and-decision-rules)).

## Work Plan

### Proposed schedule by month

The three tasks run in parallel, but they depend on each other. The proposed order is the following.

| Months  | T3.1 Blueprints                                                    | T3.2 KPIs & validation                    | T3.3 Architecture                                    | Gate                      |
| ------- | ------------------------------------------------------------------ | ----------------------------------------- | ---------------------------------------------------- | ------------------------- |
| M01     | Kickoff, WP3 plan, templates, stakeholder list                     | Draft KPI long list from the proposal     | Review of proposal architecture, tooling choices     | M1 Kickoff                |
| M02–M03 | Co-design workshop preparation, personas, user stories, interviews | Baseline definitions per KPI              | Architecture principles, component inventory         | **WS1** Co-Creation (M3)  |
| M03–M05 | Use case workflows, data inventory per pilot, semantic scoping     | Draft KPI scorecard, evaluation method    | Logical architecture v1, interface list              | Internal review           |
| M05–M07 | Blueprint drafts for ECP, EDCR, ESLA                               | MSAB review of requirements and KPI draft | Architecture v2 with security and oversight, ADR log | D1.1 / D1.2 / D1.3 at M06 |
| M07–M08 | Consolidation, cross-partner consistency check                     | Final scorecard, TRL 5 criteria           | Architecture v3, interface definitions               | Review round              |
| M09     | Sign-off                                                           | Sign-off                                  | Sign-off                                             | **M3 Freeze**, D3.1–D3.3  |

*Proposed.* The reason for this order is that the semantic scoping (T3.1) and the KPI baselines (T3.2) feed the architecture, and the architecture must be stable early enough for WP4 (starts M06) and WP5 (starts M12) to rely on it.

### Task T3.1 Use Case Blueprints & Semantic Scoping

**Partners (from the proposal):** KTH (lead), AIT, UNICA, EIN, IDUN, TRI, IMT.

**Goal.** Bridge the gap between the high-level objectives and technical execution by detailing the ECP, EDCR and ESLA use cases.

**Activities from the proposal:**

1. Iterative co-design workshops with pilot partners to map user journeys and functional requirements.
2. Identification of the data streams needed.
3. Semantic mapping for federated access, with extensions of the IEC CIM and PECO ontologies.
4. Regulatory constraints (AI auditability, human oversight, data sovereignty) integrated as design requirements.

**Proposed way of working:**

| Step | What                                                                                                                                                                    | Who                                                                                               | Result                                        |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 1    | Stakeholder map per pilot: energy community managers, DSO staff, building operators, technology providers, regulators                                                   | Pilot hosts (UNICA/FLOSS for IT, AIT for AT, EIN/ProptechOS for SE, TRI/IMT for FR), KTH collects | Stakeholder register                          |
| 2    | Interviews and co-creation workshops, including gender-responsive personas and user journeys so that the natural-language interface does not exclude non-expert members | KTH with EIN (Living Lab method), IMT on explainability needs                                     | Personas, journeys, user stories              |
| 3    | Data inventory per use case: source, owner, format, access conditions, update rate, privacy class, availability for the project                                         | Each pilot partner, ProptechOS for building data                                                  | Data requirements table                       |
| 4    | Semantic scoping: map each data item to IEC CIM or PECO concepts, list gaps that need ontology extensions                                                               | UNICA, AIT, with ProptechOS                                                                       | Semantic mapping tables, gap list             |
| 5    | Requirements consolidation: functional, data, interface, explainability, regulatory, non-functional (latency, availability)                                             | KTH                                                                                               | Requirements register with IDs and priorities |
| 6    | Review round with pilot partners, then with the MSAB                                                                                                                    | All                                                                                               | Updated blueprints                            |

The proposal says it assumes the existing ontologies are expressive enough, and de-risks this with targeted expert interviews in Phase 1. These interviews belong in step 4.

**Use case scope to be detailed** (from the proposal):

| Use case | Countries | What the blueprint must settle                                                                                                                                                                                             |
| -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ECP      | AT, IT    | Planning dialogue for non-experts: PV, storage and charging sizing, community scope, financial viability. Which public and community data feed it. Live pilot in Italy and high-fidelity simulation in Austria             |
| EDCR     | SE, FR    | Operator decision support under high renewable share: events (load peaks, EV charging surges), scenario simulations, DSO-informed grid constraints, shadow mode next to human operators. Swedish pilot in Hammarby Sjöstad |
| ESLA     | AT, FR    | Automated lifecycle for energy services: synthetic data generation, training, simulation, testing of a demand-response algorithm. Needs for developers and service operators                                               |

**Output D3.1 User-Centric Blueprint Portfolio.** *Proposed structure* for each use case:

1. Context and stakeholders, personas, user journeys
2. Operational workflow (what the agents do, where the human decides)
3. Functional and non-functional requirements with IDs and priority
4. Data requirements and semantic mapping (CIM/PECO), data access status
5. Regulatory and ethical constraints (AI Act, GDPR, national rules)
6. Pilot environment description and constraints
7. Open issues and assumptions

Plus a cross-use-case chapter on shared requirements, so that the platform is built once and instantiated three times.

**Done when:** every requirement is traceable to a stakeholder need or a regulation, every data item has an owner and an access status, and pilot partners have signed off their own blueprint.

### Task T3.2 Stakeholder Validation, KPIs & Impact Planning

**Partners (from the proposal):** KTH (lead), AIT, UNICA, EIN, IDUN.

**Goal.** Define the common validation framework for all pilots, so that WP6 evaluates the three use cases consistently at TRL 5.

**Activities from the proposal:**

1. Review of the T3.1 requirements and workflows with the Multi-Stakeholder Advisory Board (MSAB).
2. A balanced KPI scorecard covering technical performance, explainability, usability and societal impact.
3. A consistent TRL 5 evaluation method across pilots.

**Starting point: KPIs already committed in the proposal.** D3.2 must refine these into measurable definitions, not replace them.

| Objective | KPI in the proposal                                                              | Verification named in the proposal                          |
| --------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| O1        | 30–50% less manual engineering effort                                            | Manual vs agentic execution benchmark (WP6)                 |
| O1        | More than 90% task success without human intervention                            | Logs from stress tests                                      |
| O1        | 15–20% local peak load reduction via agentic BESS/EV negotiation                 | Functional tests of orchestration                           |
| O2        | Semantic mapping under 500 ms per new data point                                 | Benchmark of the Semantic API integration (T5.2)            |
| O2        | Cross-site queries under 2 s for 90% of requests                                 | Federated SPARQL tests                                      |
| O2        | At least 50% less data onboarding time                                           | Cross-site reuse in pilots                                  |
| O3        | 100% audit trail for high-risk decisions                                         | AI Act conformity self-assessment (T1.2), rule-based checks |
| O3        | 85% operator acceptance, transparency score of at least 4/5                      | Pilot surveys, XAI feedback loops                           |
| O3        | More than 80% of operators confirm the AI logic matches their own                | Pilot surveys                                               |
| O4        | Assessment time from about 3 months to under 21 days                             | KPI logging in pilots                                       |
| O4        | Automated DSO connection pre-assessment in under 4 hours (baseline 40 man-hours) | KPI logging in pilots                                       |
| O4        | 10–20% more hosting capacity, 25–40% fewer congestion hours                      | Independent verification, TRL assessment                    |

Use-case level targets in the proposal: ECP planning in 4–8 weeks instead of several months; ESLA development time reduced 30–50%; EDCR hosting capacity +10–20% and congestion mitigation 25–40%, evaluated as potential improvements through decision support in shadow mode.

**Proposed approach for the scorecard:**

| Dimension                         | Example indicators                                                                                                       | Typical data source                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| Technical performance             | Latency, query time, success rate, forecast error, hosting capacity, congestion hours                                    | Platform logs, simulations, pilot data            |
| Efficiency                        | Planning time, development time, manual effort, workflow errors                                                          | Time logs, baseline comparison, expert benchmarks |
| Explainability and trust          | Transparency score, operator acceptance, agreement with expert logic, share of recommendations with complete audit trail | Surveys, audit logger, interviews                 |
| Usability and inclusion           | Task completion by non-experts, error rate, accessibility, sex-disaggregated feedback                                    | Usability tests                                   |
| Safety and robustness             | Guardrail rejections, behaviour in degraded mode, low-confidence escalation                                              | Stress tests (T6.4)                               |
| Societal and environmental impact | Barrier reduction for energy communities, effects on vulnerable groups, estimated CO₂ effect                             | Surveys, simulations                              |

For each KPI the framework should fix: definition and formula, unit, baseline and how it is measured, target, data source, measurement point (which use case, which month), owner, and the tolerance for declaring success. The proposal's "Trust-Score" thresholds also need a definition here, because the shadow-mode validation uses them to calibrate the guardrails.

**Shadow-mode protocol (proposed content of D3.2).** The proposal commits to shadow-mode validation: AI recommendations run next to human decisions and never control physical assets. D3.2 should define:

- what is compared with what (AI recommendation vs documented human decision vs historical decision),
- which data are recorded, and how privacy is protected,
- how agreement and acceptance are computed,
- what happens when the AI and the operator disagree,
- the rules for "degraded mode" and low-confidence cases.

**TRL assessment method (proposed).** Define the TRL 3, 4 and 5 entry and exit criteria, the evidence expected at each of the workshops (WS1 at M3, WS2 at M18, WS3 at M32) and who signs off. The proposal states that TRL 5 means validation in a relevant, simulated or lab-scale operational environment, not live control of the grid (TRL 6).

**MSAB.** The Multi-Stakeholder Advisory Board is set up under T1.1. WP3 needs it from M03 on. Proposed: agree its membership (energy community representatives, DSO, regulator or municipality, technology provider) and its review calendar at the kickoff.

**Output D3.2 Validation & Impact Framework.** KPI scorecard with definitions and baselines, evaluation methodology, shadow-mode protocol, TRL criteria, data collection templates and the usability and ethics testing protocol (including participant consent and the gender and fairness checks promised in the proposal).

**Done when:** every proposal KPI has a measurable definition, a baseline and an owner, the MSAB has reviewed the framework, and the pilots can say how they will collect each indicator.

### Task T3.3 Modular System Architecture & Trust-by-Design Blueprint

**Partners (from the proposal):** AIT (lead), UNICA, FLOSS, KTH, IDUN, TRI, IMT.

**Goal.** Specify the modular architecture and how the orchestration engine, the federated knowledge layer and the explainability layer interact, with security, authentication, interoperability and human oversight built in.

KTH's role as WP leader is to make sure that the architecture meets the requirements from T3.1 and the KPIs from T3.2, and that the Swedish pilot requirements are reflected in it. AIT leads the writing.

**Building blocks already described in the proposal.** The architecture should start from these and not reinvent them.

| Block                               | Description in the proposal                                                                                                                                                                               | Implemented in |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Agent orchestration engine          | Multi-agent runtime with a central orchestrator, standard agent contracts, JSON/YAML workflows, message bus or direct calls, event handling, fallback strategies, Hierarchical Task Networks for planning | T4.1, T5.1     |
| Federated semantic layer            | Decentralised metadata registry, Semantic API, connectors (YAML-configured), SPARQL endpoints, JSON-LD/Turtle/RDF, federated knowledge graph on IEC CIM and PECO, no central data pool                    | T4.2, T5.2     |
| Physical guardrail ("Safety Layer") | Deterministic validation of control recommendations with power flow models (OpenDSS, Pandapower) against grid limits such as EN 50160, target latency under 100 ms                                        | T4.1, T5.1     |
| Explainability and trust module     | Explanation generators per agent, global explanation module, regulatory guardrails, human-in-the-loop feedback, transparency and audit logger                                                             | T4.3, T5.4     |
| Use case toolboxes                  | ECP web module with chat, EDCR operator dashboard, ESLA notebooks and configuration dashboard                                                                                                             | T5.3           |
| Cross-cutting services              | Observability (structured logs, tracing), RBAC/ABAC security hooks, differential privacy pipeline and synthetic data generation                                                                           | T5.1, T5.2     |

**Proposed design questions to close in T3.3** (each gets an architecture decision record):

| Topic                        | Questions                                                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Layers and boundaries        | What are the modules, what do they own, which interfaces are public?                                                                        |
| Agent contracts              | Registration, input and output schemas, error envelope, versioning                                                                          |
| Data access                  | Where do connectors run (at the data owner, at the edge, in the cloud)? How are schema changes handled? Which SPARQL features are required? |
| Security and identity        | Authentication between agents and external systems, RBAC/ABAC model, secrets, network zones for pilot sites                                 |
| Data sovereignty and privacy | What may leave a site? GDPR handling of building and consumption data, synthetic data release rules                                         |
| Human oversight              | Where recommendations pause for approval, override and kill-switch functions, how overrides are logged and fed back                         |
| Traceability                 | What the audit logger records (inputs, outputs, reasoning elements, approvals), retention, who can read it                                  |
| Deployment                   | Cloud-native target, containerisation, sizing for 10 communities and 100 concurrent agents, pilot-site edge devices                         |
| LLM strategy                 | Which models, hosting, small language models and federated inference to limit footprint, prompt and retrieval grounding                     |
| Licensing                    | Which components are open (Apache 2.0, Zenodo release of the Connector SDK and non-proprietary semantic models), which stay proprietary     |
| Interoperability             | Standards used (IEC CIM, SAREF, IEC 62559/SGAM for use cases), gateways to IoT and SCADA, external APIs                                     |

**Output D3.3 Modular Trust-by-Design Architecture Specification.** Architecture diagrams (logical, deployment, data flow), interface definitions, security requirements, the human oversight design, a traceability matrix from requirements (D3.1) to components, and the architecture decision log.

**Done when:** every requirement of D3.1 is allocated to a component, interfaces are defined well enough for the WP4 and WP5 teams to work in parallel, the security and oversight design has been reviewed by TRI and IMT, and AIT, FLOSS and the pilot hosts confirm it is feasible.

## Cross-WP Interfaces

| With | WP3 gives                                                                       | WP3 needs                                                                            |
| ---- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| WP1  | Input to risk register and AI Act self-assessment, data inventory for the DMP   | Handbook procedures (D1.1), MSAB set-up, DMP template (D1.2), data access agreements |
| WP2  | KPI framework and tracking tables for periodic reports                          | Reporting calendar                                                                   |
| WP4  | Use case workflows, semantic scoping, regulatory constraints as modelling input | Early feedback on what the methods can deliver by M22                                |
| WP5  | Architecture, interfaces, UI requirements                                       | Feasibility feedback from FLOSS and AIT, tool choices                                |
| WP6  | KPI scorecard, evaluation method, shadow-mode protocol, pilot blueprints        | Pilot readiness information (data access, site constraints)                          |

WP4 starts in M06, before WP3 ends. Proposed: WP4 leaders attend the WP3 reviews from M05 and work from draft versions of D3.1 and D3.3, so that the freeze at M09 does not come as a surprise.

## Governance and Decision Rules

*Proposed.*

- **Meetings:** a WP3 call every two weeks in M01–M09, plus working sessions per task and one WS1 workshop at M3.
- **Single source of truth:** a requirements register with unique IDs (for example `REQ-ECP-012`), status and owner, shared by all partners. The architecture decision log uses one record per decision.
- **Review cycle for each deliverable:** draft to task partners, internal review by two partners not involved in writing, MSAB review for D3.1 and D3.2, then sign-off by the pilot hosts and the General Assembly representative.
- **Freeze at M09:** after sign-off, changes need a change request that states the impact on WP4, WP5 and WP6, and are approved by the WP leaders concerned. Small clarifications are allowed without a request.
- **Escalation:** disagreements between partners go to the project coordinator (AIT) through the technical board set up under T1.1.

## Risks

| Risk                                                                                       | Source                      | Mitigation                                                                                            |
| ------------------------------------------------------------------------------------------ | --------------------------- | ----------------------------------------------------------------------------------------------------- |
| Semantic incompatibility between pilot sites (AT, IT, SE, FR)                              | Proposal, WP3 and WP4       | Use CIM and SAREF, start mapping early, expert interviews in Phase 1, automated alignment tools       |
| Data silos and unstable access to DSO or community data                                    | Proposal, WP3, WP5, WP6     | Data access agreements early, data inventory in T3.1 with access status, plan for synthetic data      |
| Explanations too technical for non-expert users                                            | Proposal, WP4 and WP6       | Co-creation workshops in T3.1 to define "understandable" metrics                                      |
| Late or unclear requirements delay WP4 and WP5                                             | Proposed                    | Early drafts shared from M05, freeze date at M09, traceability matrix                                 |
| KPI definitions are too vague to measure in WP6                                            | Proposed                    | Define baseline, formula and data source for every KPI in D3.2, dry run of the data collection in M26 |
| Pilot partners have little time in M01–M09 (low effort in WP3 for FLOSS, TRI, UNICA, IDUN) | Proposed, from effort table | Short, focused sessions, templates prepared by KTH, workshops grouped                                 |
| Overlap with the Swedish national timeline                                                 | Proposed                    | Align D3.x review dates with Energimyndigheten reporting once known                                   |

## Kickoff Meeting Context

The agenda is in `resources/kickoff_agenda.pdf` (issued by AIT). The meeting is on site at AIT, Vienna, with hybrid logistics for remote participants. WP3 is the last session of day 1, after a coffee break and a full afternoon. What comes before and after it shapes the WP3 slides.

| Time | Item (agenda) | What it means for the WP3 session |
| ---- | ------------- | --------------------------------- |
| 13:15 | Round table, about 5 minutes per partner | Partners have introduced their teams and roles. The WP3 deck does not repeat them |
| 13:55 | Project overview (AIT): pillars, use cases, objectives and KPIs, timeline and milestones | Do not repeat it. The KPI slide shows only what D3.2 adds, and the use case slide only what each blueprint adds |
| 14:40 | WP1 and WP2 (AIT): bodies and roles, decision making, meeting cadence, reporting, shared workspace, Knowledge Community | WP3 uses that governance and workspace. The "how we decide" slide covers only the WP3 rules |
| 15:30 | Consortium Agreement and funding contracts | Sets the data access and IPR conditions that the data inventory in T3.1 depends on |
| 16:00 | First six months (AIT, all): D1.1 to D1.3, advisory board nominations, website, logo, templates | The MSAB nominations are collected here, so WP3 only asks for the date of its first meeting. The project logo and templates may affect the slide template |
| 16:45 | **WP3 (KTH), 45 minutes** | About 25 minutes of slides, 15 minutes of discussion, 5 minutes of buffer |
| 17:30 | Open discussion, parking lot, wrap-up of day 1 (all) | Open WP3 questions can go to the parking lot, so the WP3 discussion stays focused on the asks |
| Day 2, 09:10 and 09:50 | WP4 (UNICA) and WP5 (FLOSSLAB) | They present after WP3. WP3 must tell them what to expect from D3.1 to D3.3, and when |
| Day 2, 11:25 | Cross-WP alignment (all): interfaces, dependencies, who needs what from whom and when, joint timeline towards MS3 | The hand-over table in the WP3 deck (what each WP gets from WP3, and when) is the input |
| Day 2, 11:45 | Next steps and action items (AIT) | The asks are written as action items with owner and date |

## Open Questions for the Kickoff

1. Who is the point of contact for each pilot and each task, and how much time can they give in M01 to M09? (Asked in the WP3 session.)
2. When does the MSAB first meet? The nominations are collected in the 16:00 session, so only the date is open.
3. Which tools hold the requirements register and the architecture decision log? The shared workspace (repository, mailing list, code) is presented under WP1 at 14:40; use it and confirm there.
4. What is the status of data access agreements for each pilot, and which data are available as proxy or synthetic data? Check what the Consortium Agreement session at 15:30 settles.
5. Which ontology versions (IEC CIM, PECO) are the baseline, and who owns the extensions?
6. Is the date for WS1 (M3) fixed, and where is it held? If M01 is November 2026, M3 is about January 2027; confirm the project start date with AIT.
7. What do the French pilot sites and the Austrian simulation need from the use case blueprints? The proposal describes EDCR in SE and FR and ESLA in AT and FR, but gives the Swedish pilot in the most detail.
8. Does the 16:00 session on project logo and templates change the template for the decks? Until then the decks use the KTH template.
9. What do WP4 and WP5 need from WP3, and by when? Collect it after their sessions and at the cross-WP alignment on day 2.

## Kickoff Presentation: Slot and Slide Structure

*Proposed.* The deck is a decision-driven core of 12 slides plus backup slides (see [BST-0001](../brainstorming/BST-0001-wp-presentation-structure-for-kickoff-meeting.md) for the reasoning). Titles stay within one line of the KTH template.

| # | Slide | Content | Time |
| - | ----- | ------- | ---- |
| 1 | WP3: Requirements and Architecture | Title, one-line scenario | 1 min |
| 2 | Why WP3 comes first | What WP4, WP5 and WP6 take from the M09 freeze | 2 min |
| 3 | Three tasks, one freeze at M09 | T3.1 to T3.3, D3.1 to D3.3, task leads | 2 min |
| 4 | Timeline and gates | Month plan, WS1 at M3, freeze at M09 | 2 min |
| 5 | T3.1: how we work | Six steps from stakeholders to review | 3 min |
| 6 | Three use cases, three blueprints | What each blueprint adds to the overview | 2 min |
| 7 | T3.2: from targets to baselines | Four KPIs and what D3.2 adds | 3 min |
| 8 | T3.3: the architecture | Building blocks and open design questions | 3 min |
| 9 | What WP4 to WP6 get, and when | Hand-over dates, input to the day 2 alignment | 3 min |
| 10 | How we decide | WP3 review cycle and freeze rule | 2 min |
| 11 | What we need from you | Five asks with owner and date | 3 min |
| 12 | Discussion | Four questions | 15 min |
| Backup | Effort, KPI list, architecture questions, risks, deliverable contents | For questions | n/a |

Supporting material to prepare in advance: a blank blueprint template, a blank data inventory sheet, a KPI definition sheet with the proposal KPIs prefilled, and a draft calendar for the first three months.

## References

- Kickoff meeting agenda: `resources/kickoff_agenda.pdf` (AIT, Vienna, 30 November and 1 December 2026)
- Slide deck: `site/slides/wp3-kickoff.qmd`
- International proposal: `resources/full_proposal_international.pdf`, sections 1.2, 1.3 and 3.1 (WP3 description, tables 3a, 3c, 3d, 3e, 3f)
- Swedish proposal to Energimyndigheten: `resources/full_proposal_swedish.pdf` (Swedish activities, budget per WP)
- [GDE-0001 Plenergy.AI: Overview](GDE-0001-plenergy-ai-overview.md)
- [GDE-0002 Plenergy.AI: Implementation](GDE-0002-plenergy-ai-implementation.md)
- [GDE-0004 WP6: Use Case Validation and Performance Assessment](GDE-0004-wp6-use-case-validation-and-performance-assessment.md)
