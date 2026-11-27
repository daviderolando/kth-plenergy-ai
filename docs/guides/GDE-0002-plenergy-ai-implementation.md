---
title: "GDE-0002 Plenergy.AI: Implementation"
id: GDE-0002
type: guide
status: active
created: "2026-11-27"
tags: [plenergy-ai, implementation, work-packages, deliverables, milestones]
related: [GDE-0001, GDE-0003, GDE-0004]
---

## Overview

This guide describes how the Plenergy.AI work is implemented, one work package (WP) at a time. For each WP it gives the goal, the task breakdown with the partners involved, the technical approach, the deliverables, and the links to the other WPs. It also lists the project milestones, the maturity (TRL) path and the main implementation risks.

It is written for project members who have to plan or carry out a task. For the project background, objectives and consortium, read [GDE-0001](GDE-0001-plenergy-ai-overview.md) first.

The source is the international full proposal in `resources/full_proposal_international.pdf`, section 3 (tables 3a to 3f). Partner short names are AIT, UNICA, FLOSS, KTH, EIN, IDUN, TRI and IMT, as in GDE-0001. IDUN is now named ProptechOS (same legal entity); the international proposal still uses IDUN. The first partner listed for a task is its lead.

The two work packages led by KTH have their own, more detailed guides: [GDE-0003](GDE-0003-wp3-requirements-and-architecture-design.md) for WP3 and [GDE-0004](GDE-0004-wp6-use-case-validation-and-performance-assessment.md) for WP6. Month numbers (M01 to M36) count from project start; the Swedish part starts on 2026-11-01.

## Implementation Logic

The work is organised in four phases that raise the maturity of the platform step by step. The two cross-cutting WPs (WP1, WP2) run for the whole project.

| Phase                           | WP  | Months  | Target TRL | What happens                                                                              |
| ------------------------------- | --- | ------- | ---------- | ----------------------------------------------------------------------------------------- |
| 1. Requirements & architecture  | WP3 | M01–M09 | TRL 3      | Co-design with stakeholders, KPI framework, architecture blueprint                        |
| 2. Core technology development  | WP4 | M06–M22 | TRL 4      | Methods for orchestration, federation and explainability, tested separately in simulation |
| 3. Integration & implementation | WP5 | M12–M30 | TRL 4+     | Cloud-native platform with alpha demos by M24 and beta release by M30                     |
| 4. Validation & impact          | WP6 | M16–M36 | TRL 5      | Shadow-mode pilots in AT, IT, SE, FR and cross-case evaluation                            |

Three stakeholder workshops gate the progress: WS1 co-creation (M3), WS2 interim review with the mid-term prototype (M18), WS3 impact evaluation with pilot data in shadow mode (M32).

Design rules that apply to every WP:

- **Shadow mode.** AI recommendations run in parallel with human decisions and never control physical assets during the project.
- **Neuro-symbolic guardrails.** LLM agents handle language and planning; a deterministic safety layer based on power flow models validates every control recommendation (target latency under 100 ms).
- **Data at source.** Federated access, no central data pool. Synthetic data fills the gap when real data is delayed.
- **Human in the loop.** Manual override and audit logs are built into every interface.
- **Open outputs.** Non-proprietary semantic models and the Connector SDK are released under Apache 2.0.

## WP1 Project Management

|          |                   |
| -------- | ----------------- |
| Lead     | AIT               |
| Duration | M01–M36           |
| Effort   | 10.3 PMs in total |

**Goal.** Coordination, financial and administrative management, risk control and quality assurance, with the Trust-by-Design framework as the governance backbone.

| Task                                                                                 | Content                                                                                                                                                                                                                                          | Output                                                       |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| T1.1 Project Coordination & Governance (AIT, all)                                    | General Assembly and technical board meetings, a Multi-Stakeholder Advisory Board (MSAB) that gives energy community representatives a formal voice, a Human-in-the-Loop Oversight Protocol, synchronisation between WP4 theory and WP5 software | Project Handbook (D1.1)                                      |
| T1.2 Risk Management, Regulatory Compliance, and Trust-by-Design Auditing (AIT, all) | Dynamic risk register, "Regulatory Drift" assessments in AT, IT, SE and FR, EU AI Act conformity self-assessments for the agentic orchestration, documented kill-switch and manual override protocols                                            | Risk register and conformity self-assessments (part of D1.1) |
| T1.3 Federated Data Governance & FAIR Transparency (AIT, all)                        | Data Management Plan, differential privacy pipeline so that released synthetic datasets keep k-anonymity, provenance logs for all data used by agents                                                                                            | Data Management Plan (D1.2), data provenance logs            |
| T1.4 Strategy for Communication, Dissemination, and Exploitation (AIT, all)          | Visual identity, website, social media, open-access publications, central IPR registry, licensing and SaaS models, standardisation roadmap towards CEN/CENELEC and ETSI                                                                          | Dissemination, exploitation and open science plan (D1.3)     |

**Deliverables.** D1.1, D1.2, D1.3, all due at M06 and then updated.

**Links.** WP1 supports O3 and O4 through its compliance and oversight work. The IPR conflict and partner attrition risks sit here.

## WP2 Reporting & Knowledge Community

|          |                  |
| -------- | ---------------- |
| Lead     | AIT              |
| Duration | M01–M36          |
| Effort   | 9.3 PMs in total |

**Goal.** Formal reporting to the funders and transfer of results to the CETPartnership Knowledge Community and European platforms such as ETIP SNET.

| Task                                           | Content                                                                                                                                                                 | Output                                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| T2.1 Periodic Reporting (AIT, all)             | Reporting at M12, M24 and M36 with a quality assurance loop that compares partner inputs and KPIs with the baseline objectives                                          | Progress reports D2.1, D2.2, D2.3, with KPI tracking tables, resource audits and risk logs |
| T2.2 Knowledge Community Engagement (AIT, all) | Cross-project exchange on semantic standards and AI ethics, policy briefs for regulators, representation in thematic working groups, monitoring of EU energy directives | Policy & Knowledge Community Report (D2.4)                                                 |

**Deliverables.** D2.1 (M12), D2.2 (M24), D2.3 (M36), D2.4 (M36).

**Links.** Takes trust-by-design evidence from WP1 and WP4 and validation results from WP6. T2.2 also watches the regulatory changes that could affect the use cases.

## WP3 Requirements and Architecture Design

|                 |                                                |
| --------------- | ---------------------------------------------- |
| Lead            | KTH                                            |
| Duration        | M01–M09                                        |
| Effort          | 37.6 PMs (KTH 11.0, EIN 7.0, AIT 5.6, IMT 5.0) |
| Target maturity | TRL 3                                          |

**Goal.** Turn the project vision into requirements, data interfaces, a modular architecture and a shared validation framework, together with DSOs, energy communities and building operators.

| Task                                                                                                  | Content                                                                                                                                                                                                                                                                                                               | Output                                            |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| T3.1 Use Case Blueprints & Semantic Scoping (KTH, AIT, UNICA, EIN, IDUN, TRI, IMT)                    | Iterative co-design workshops with pilot partners, user journeys and functional requirements for ECP, EDCR and ESLA, identification of data streams, semantic mapping with extensions of IEC CIM and PECO, regulatory constraints (auditability, human oversight, data sovereignty) written in as design requirements | Use Case Blueprint Portfolio (D3.1)               |
| T3.2 Stakeholder Validation, KPIs & Impact Planning (KTH, AIT, UNICA, EIN, IDUN)                      | Review of the T3.1 results with the MSAB, balanced KPI scorecard (technical performance, explainability, usability, societal impact), common TRL 5 evaluation method for all pilots                                                                                                                                   | Validation & Impact Framework (D3.2)              |
| T3.3 Modular System Architecture & Trust-by-Design Blueprint (AIT, UNICA, FLOSS, KTH, IDUN, TRI, IMT) | Architecture linking the orchestration engine, the federated knowledge layer and the explainability layer, security, authentication and interoperability mechanisms, human oversight (audit logs, traceability, override)                                                                                             | Trust-by-Design Architecture Specification (D3.3) |

**Deliverables.** D3.1, D3.2, D3.3, all due at M09 (milestone M3, Architecture & Requirements Freeze).

**Links.** D3.1 guides the modelling in WP4 and the data layer and toolboxes in WP5. D3.2 provides the KPIs that WP6 measures. D3.3 is the master blueprint for T5.1 and T5.2 and fixes the human-intervention interfaces for T5.3 and T5.4. Co-creation also defines what counts as an "understandable" explanation, which addresses the XAI complexity risk.

## WP4 Theoretical and Methodological Foundations

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Lead            | UNICA                                                        |
| Duration        | M06–M22                                                      |
| Effort          | 53.9 PMs (IMT 20.5, AIT 17.4, UNICA 7.0, TRI 5.0, FLOSS 3.0) |
| Target maturity | TRL 3 to TRL 4                                               |

**Goal.** Establish the algorithmic foundation: neuro-symbolic methods that combine generative AI with structured energy domain knowledge so that recommendations stay physically consistent and transparent.

| Task                                                                             | Content                                                                                                                                                                                                                                                                                                                 | Output                                                                                                          |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| T4.1 Agentic AI Orchestration Models (AIT, IMT)                                  | LLMs combined with symbolic reasoning, a deterministic Physical Guardrail layer for control commands, retrieval-augmented generation grounded in the real-time grid topology, Hierarchical Task Networks to break goals into verifiable sub-tasks, reusable patterns such as parallel "what-if" simulation agents       | Library of Agentic Orchestration Patterns (D4.1): templates, pseudo-code, early prototypes                      |
| T4.2 Federated Knowledge Integration Framework (UNICA, AIT)                      | Alignment of IEC 61970 (CIM) with PECO, federated RDF graph architecture, semantic APIs and SPARQL endpoints that wrap local silos such as DSO SCADA and smart meter hubs, on-the-fly translation between relational and graph data, decentralised metadata registry                                                    | Federated Semantic Mapping Methodology (D4.2): ontology alignment, SPARQL endpoint security, metadata discovery |
| T4.3 Explainable AI Recommendations and Trust Framework (TRI, UNICA, FLOSS, IMT) | Explanation methods adapted to energy time series (such as SHAP or LIME), AI trustworthiness analysis against the EU AI Act, regulatory guardrails as automated verification layers, human-in-the-loop feedback, specification of the transparency and audit logger, security-by-design and ethics-by-design mechanisms | Integrated Trust & Explainability Blueprint (D4.3)                                                              |

**Deliverables.** D4.1, D4.2, D4.3, all due at M22 (milestone M6, Methodology & Logic Prototype, TRL 4).

**Example of the intended behaviour.** If the system recommends an unusual grid reconfiguration, the XAI module justifies it symbolically ("Action prioritised to prevent predicted voltage drop at Node Y"). The operator can reject it with a manual override, and the rejection is recorded as a learning event.

**Links.** Takes requirements from WP3. Supplies the algorithm library, the communication protocols and the UI and trust specifications that WP5 implements and WP6 evaluates. Hosts the orchestration hallucination risk, which the guardrail layer addresses.

## WP5 Platform Development and Toolbox Implementation

|                 |                                                             |
| --------------- | ----------------------------------------------------------- |
| Lead            | FLOSS                                                       |
| Duration        | M12–M30                                                     |
| Effort          | 58.3 PMs (IMT 16.0, AIT 14.8, FLOSS 8.0, IDUN 5.5, TRI 5.0) |
| Target maturity | TRL 4+ (system prototype)                                   |

**Goal.** Turn the WP4 models into a scalable, cloud-native platform with the three use-case toolboxes, and provide interoperability with external systems and IoT gateways. Integration is incremental: alpha demos by M24, beta release by M30, with each agent tested in isolation before it joins the multi-agent environment.

| Task                                                                      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Output                                                          |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| T5.1 Agent Orchestration Runtime (FLOSS, AIT, UNICA)                      | Agent management on an existing multi-agent framework (such as JADE) or a Python runtime, standard agent contracts (registration, input and output schemas, error envelopes), JSON/YAML workflow specifications, discovery and messaging APIs, a central Orchestrator agent, event handling, parallel execution and fallback strategies, integration of low-code tools such as n8n or Node-RED, observability (structured logging, distributed tracing), RBAC/ABAC security hooks | Agent Runtime Environment (D5.1)                                |
| T5.2 Federated Knowledge Integration Layer (UNICA, AIT, FLOSS)            | Decentralised metadata registry, Semantic API as ontology-aware gateway, Python connectors that turn raw telemetry into JSON-LD, Turtle or RDF, YAML-configured connectors for quick deployment at pilot sites, real-time cross-silo SPARQL queries, automatic mapping of schema changes, differential privacy pipeline producing physics-informed synthetic data when real data access is delayed                                                                                | Data Backbone (D5.2)                                            |
| T5.3 Use Case Toolboxes & Human-Centric Interfaces (AIT, FLOSS, KTH, IMT) | ECP: web module with chat interface and scenario dashboard (financial metrics, PV and storage charts). EDCR: operator dashboard with live community-grid metrics from IoT streams (Idun and ElectriCITY infrastructures) and an alert and advice panel with explanations. ESLA: configuration dashboard and Jupyter notebooks for queuing synthetic data and model-training workflows. English with Italian and German fragments, predefined scenario templates                   | Use Case Toolboxes (D5.3), three deployable assistant instances |
| T5.4 Explainable AI Recommendation Framework (IMT, KTH, TRI)              | XAI backend coupled to the agent runtime, extraction of decision logic from agent reasoning paths, explainability plugins per toolbox, feedback from human-in-the-loop use to calibrate explanation confidence, behavioural and policy testing of agents with Trialog's ODC tester, centralised transparency and audit trail logger                                                                                                                                               | Explainability & Trust Module (D5.4)                            |

**Deliverables.** D5.1 to D5.4, all due at M30 (milestone M8, Integrated Platform Beta Release). Milestone M5 (M20) is an internal demo of the core orchestrator and the first data plugins.

**Links.** Implements WP3 blueprints and WP4 methods. The three toolbox instances are what WP6 tests in the field. T5.1 is the base for T5.2 to T5.4. Hosts the federated-query latency and scalability risks, handled with edge caching, optimised SPARQL queries and a microservice architecture.

## WP6 Use Case Validation and Performance Assessment

|                 |                                                           |
| --------------- | --------------------------------------------------------- |
| Lead            | KTH                                                       |
| Duration        | M16–M36                                                   |
| Effort          | 53.1 PMs (EIN 12.0, KTH 10.0, IMT 10.0, AIT 7.6, TRI 5.0) |
| Target maturity | TRL 5                                                     |

**Goal.** Validate the platform in relevant environments, using the WP3 KPI framework, and measure performance, usability and trust. Each pilot follows a structured evaluation protocol, with user-centred outcomes such as perceived transparency next to technical ones such as hosting capacity and decision time.

| Task                                                                    | Content                                                                                                                                                                                                                                                                                                                | Output                                 |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| T6.1 Validation of use case ECP, IT and AT (UNICA, AIT, FLOSS, KTH)     | Retrospective trials on historical planning cases, then prospective planning with emerging communities. AI recommendations are compared with expert benchmarks in shadow mode. Assessment of usability, planning efficiency and regulatory adaptability across countries                                               | UC-ECP Validation Report (D6.1)        |
| T6.2 Validation of use case EDCR, SE and FR (KTH, EIN, IDUN, TRI, IMT)  | Swedish pilot in the ElectriCITY ecosystem in Hammarby Sjöstad with real infrastructure data and simulated grid constraints. Explainable recommendations for load peaks and flexibility activation, in shadow mode next to human operators. Evaluation of operator interaction, situational awareness and usefulness   | UC-EDCR Validation Report (D6.2)       |
| T6.3 Validation of use case ESLA, AT and FR (AIT, KTH, TRI, IMT)        | Comparison of automated workflows with conventional engineering pipelines for services such as demand forecasting, flexibility assessment and building performance modelling. Indicators: manual data preparation effort, development time, workflow errors, robustness of federated integration across data providers | UC-ESLA Validation Report (D6.3)       |
| T6.4 Robustness, Contingency & Scalability Validation (KTH, UNICA, IMT) | Runs in parallel with T6.1 to T6.3. Stress tests with high data loads and concurrent users, simulated loss of data sources or links (degraded mode), detection of anomalous input data, scaling to multiple virtual communities, checks that low-confidence recommendations trigger operator intervention              | Robustness & Contingency Report (D6.4) |

**Deliverables.** D6.1 to D6.4, all due at M36. Milestone M7 (M26) is a successful dry run of the ECP tool on test data, signed off by the pilot partners, which also verifies data access stubs.

**Links.** Consumes the three toolboxes from WP5 and the KPIs from WP3. Produces the evidence for O1 (task autonomy, peak load reduction), O3 (auditability, operator trust) and O4 (planning time, hosting capacity, congestion hours). Hosts the pilot disengagement risk, mitigated by dedicated community managers at each pilot site.

## Milestones

| No. | Milestone                             | WP      | Month | Means of verification                                                  |
| --- | ------------------------------------- | ------- | ----- | ---------------------------------------------------------------------- |
| M1  | Project kick-off & quality plan       | 1       | M01   | Kick-off meeting held, management procedures set up                    |
| M2  | Project foundation & strategy         | 1       | M06   | D1.1, D1.2, D1.3 submitted                                             |
| M3  | Architecture & requirements freeze    | 3       | M09   | D3.1, D3.2, D3.3 submitted, specifications and KPIs signed off         |
| M4  | First period governance review        | 2       | M12   | D2.1 submitted, first-year KPIs and resources verified                 |
| M5  | Draft platform core & plugin library  | 5       | M20   | Internal release and demo of core orchestrator and first data plugins  |
| M6  | Methodology & logic prototype (TRL 4) | 4       | M22   | D4.1, D4.2, D4.3 submitted, logic verified in lab settings             |
| M7  | Mid-term pilot readiness              | 6       | M26   | Dry run of the ECP tool on test data, pre-validation report signed off |
| M8  | Integrated platform beta release      | 5       | M30   | D5.1 to D5.4 submitted, beta toolboxes deployed to all pilot sites     |
| M9  | Pilot completion & TRL 5 verification | 6       | M36   | D6.1 to D6.4 submitted, field validation data collection finished      |
| M10 | Final impact & objective audit        | 1, 2, 6 | M36   | D6.4, D2.3, D2.4 submitted, consensus on achieving O1 to O4            |

## Deliverables at a Glance

| Month | Deliverables                                                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------- |
| M06   | D1.1 Project Handbook, D1.2 Data Management Plan, D1.3 Dissemination, Exploitation & Open Science Plan                             |
| M09   | D3.1 Use Case Blueprint Portfolio, D3.2 Validation & Impact Framework, D3.3 Trust-by-Design Architecture Specification             |
| M12   | D2.1 Periodic Progress Report 1                                                                                                    |
| M22   | D4.1 Agentic Orchestration Patterns, D4.2 Federated Semantic Mapping Methodology, D4.3 Integrated Trust & Explainability Blueprint |
| M24   | D2.2 Periodic Progress Report 2                                                                                                    |
| M30   | D5.1 Agent Runtime Environment, D5.2 Data Backbone, D5.3 Use Case Toolboxes, D5.4 Explainability & Trust Module                    |
| M36   | D2.3 Progress Report 3, D2.4 Policy & Knowledge Community Report, D6.1 to D6.4 validation and robustness reports                   |

## Implementation Risks

| Risk                                                                                | Likelihood | Severity | WP      | Mitigation                                                                           |
| ----------------------------------------------------------------------------------- | ---------- | -------- | ------- | ------------------------------------------------------------------------------------ |
| Data silos and connectivity: DSOs or communities fail to provide stable data access | Medium     | High     | 3, 5, 6 | Early data access agreements, M7 readiness checkpoint, synthetic data generators     |
| Semantic incompatibility between national pilot sites                               | Medium     | Medium   | 3, 4    | Use CIM and SAREF, build automated alignment tools early                             |
| Orchestration hallucination: unsound grid recommendations                           | Low        | High     | 4       | Neuro-symbolic guardrail layer, mandatory human oversight for critical operations    |
| XAI complexity: explanations too technical for non-experts                          | Medium     | Medium   | 4, 6    | Co-creation workshops, iterative UI/UX testing, trust-score tracking                 |
| Integration latency of federated queries                                            | Medium     | Medium   | 5       | Edge caching, optimised SPARQL, robustness testing before pilots                     |
| Platform scalability beyond 10 communities or 100 concurrent agents                 | Low        | Medium   | 5, 6    | Simulated load tests in T6.4, modular microservices                                  |
| Pilot user disengagement                                                            | Medium     | Medium   | 6, 2    | Community managers at each site, clear communication of benefits, gamified feedback  |
| Divergent or changing regulatory frameworks                                         | Low        | High     | 6, 2    | Monitoring in T2.2, reconfigurable regulatory guardrails                             |
| Partner attrition or resource gap                                                   | Low        | Medium   | 1       | Shared documentation and repository, task reallocation through T1.1                  |
| IPR conflicts over foreground knowledge                                             | Low        | High     | 1       | Background and foreground IPR defined in the Consortium Agreement, live IPR registry |

## Notes

- The proposal lists the task partners with some repetition (for example KTH appears twice in the T3.2 and T6.4 lists). This guide shows each partner once.
- The proposal text writes the third use case both as ESLA and ELSA. This guide uses ESLA.
- The risk table cites "M6 Robustness testing" and the "M7 Pilot Readiness checkpoint" as mitigations. These most likely refer to milestones M6 (M22) and M7 (M26), not to months. Milestone M6 only verifies the logic in lab settings, while the robustness work (T6.4) starts at M16, so it is worth agreeing with the WP5 and WP6 leads what exactly is tested before M22.
- Month references follow the international proposal. Check the Swedish proposal and the grant decision for national reporting dates.

## References

- Kickoff meeting agenda: `resources/kickoff_agenda.pdf` (AIT, Vienna, 30 November and 1 December 2026)
- International proposal: `resources/full_proposal_international.pdf` (section 3, tables 3a to 3f)
- Swedish proposal to Energimyndigheten: `resources/full_proposal_swedish.pdf`
- [GDE-0001 Plenergy.AI: Overview](GDE-0001-plenergy-ai-overview.md)
