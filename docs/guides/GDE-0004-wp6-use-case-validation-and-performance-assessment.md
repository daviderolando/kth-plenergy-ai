---
title: "GDE-0004 WP6: Use Case Validation and Performance Assessment"
id: GDE-0004
type: guide
status: active
created: "2026-11-27"
tags: [plenergy-ai, wp6, validation, pilots, kpi, shadow-mode, kickoff]
related: [GDE-0001, GDE-0002, GDE-0003]
---

## Overview

This guide describes how WP6 *Use Case Validation and Performance Assessment* is implemented. KTH leads WP6, so the guide is written for the WP leader and is also the base for the kickoff presentation to all partners. The kickoff takes place at AIT in Vienna on 30 November and 1 December 2026; WP6 has the slot on day 2 at 10:45 (40 minutes), see [Kickoff Meeting Context](#kickoff-meeting-context). The deck is in `site/slides/wp6-kickoff.qmd`.

As in [GDE-0003](GDE-0003-wp3-requirements-and-architecture-design.md), content is split into:

- **From the proposal**: scope, tasks, partners, effort, deliverables, timing. These are commitments.
- **Proposed**: how the WP leader suggests carrying out the work. These are suggestions to discuss with the partners and are marked *Proposed*.

Read [GDE-0001](GDE-0001-plenergy-ai-overview.md) and [GDE-0002](GDE-0002-plenergy-ai-implementation.md) first for the project context.

## WP6 at a Glance

| Item                    | Value                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lead                    | KTH                                                                                                                                                       |
| Duration                | M16–M36 (M36 is October 2029 in the Swedish project calendar)                                                                                             |
| Effort                  | 53.1 person-months                                                                                                                                        |
| Target maturity         | TRL 5 (validation in a relevant environment)                                                                                                              |
| Tasks                   | T6.1 ECP validation (UNICA lead), T6.2 EDCR validation (KTH lead), T6.3 ESLA validation (AIT lead), T6.4 Robustness, Contingency & Scalability (KTH lead) |
| Deliverables            | D6.1 UC-ECP report, D6.2 UC-EDCR report, D6.3 UC-ESLA report, D6.4 Robustness & Contingency report, all at M36                                            |
| Milestones              | M7 Mid-term pilot readiness (M26), M9 Pilot completion & TRL 5 verification (M36), M10 Final impact & objective audit (M36, with WP1 and WP2)             |
| Workshops               | WS2 Interim review (M18), WS3 Impact evaluation in shadow mode (M32)                                                                                      |
| Swedish funding for WP6 | 2 360 165 SEK across KTH, EIN and ProptechOS (Energimyndigheten proposal)                                                                                 |

ProptechOS is the new name of IDUN, the same legal entity.

### Effort by partner

| Partner           | PMs  | Main contribution to WP6                                                       |
| ----------------- | ---- | ------------------------------------------------------------------------------ |
| EIN               | 12.0 | Swedish pilot host, Living Lab, stakeholders and operators in Hammarby Sjöstad |
| KTH               | 10.0 | WP leadership, T6.2 and T6.4 leads, KPI assessment, cross-case evaluation      |
| IMT               | 10.0 | Explainability and trust evaluation, EDCR (FR) and ESLA (FR) support           |
| AIT               | 7.6  | T6.3 lead, ECP in Austria, ESLA in Austria                                     |
| TRI               | 5.0  | AI Act compliance checks, guardrail testing, EDCR and ESLA (FR)                |
| UNICA             | 3.0  | T6.1 lead, ECP pilot in Italy, robustness testing                              |
| FLOSS             | 3.0  | Platform support during ECP validation, fixes and releases                     |
| IDUN / ProptechOS | 2.5  | Building data integration and platform support for the Swedish EDCR pilot      |

## Purpose and Position in the Project

WP6 produces the evidence that the project objectives were reached. It takes the three toolboxes and the platform from WP5 (beta at M30), the KPI framework from WP3 (D3.2), and shows, in relevant environments, whether the platform meets the targets set for O1 to O4.

```text
WP3  KPI framework (D3.2), pilot blueprints (D3.1)  ──┐
WP4  trust metrics, XAI and guardrail logic          ──┼─> WP6 ─> D6.1–D6.4 ─> M9 TRL 5, M10 objective audit
WP5  beta platform and 3 toolboxes (M30)             ──┘               │
                                                                        └─> WP2 (D2.3, D2.4), exploitation (WP1)
```

| WP6 task        | Objectives it evidences    | Main evidence                                                                                      |
| --------------- | -------------------------- | -------------------------------------------------------------------------------------------------- |
| T6.1 ECP        | O3, O4 (and O1, O2 by use) | Planning time, planning accuracy against experts, usability for non-experts                        |
| T6.2 EDCR       | O3, O4                     | Operator acceptance, explanation quality, hosting capacity and congestion analysis in shadow mode  |
| T6.3 ESLA       | O1, O4                     | Development time and manual effort reduction, workflow errors, robustness of federated integration |
| T6.4 Robustness | O1, O3                     | Stress, fault and scalability evidence, human-in-the-loop fallback                                 |

## Validation Principles

These come from the proposal and apply to all pilots.

1. **Relevant environment, TRL 5.** Validation uses real operational data where available, simulated grid constraints, and lab or simulated environments. Live grid demonstrations (TRL 6) are outside the project.
2. **Shadow mode.** AI recommendations run next to human decisions and never control physical assets.
3. **Common KPI framework.** All pilots use the scorecard of D3.2, so results can be compared across use cases and countries.
4. **Human-centred.** Technical performance is measured together with perceived transparency, trust and usability, with a diverse group of test participants and sex-disaggregated feedback where usability data are collected.
5. **Degraded mode.** Robustness is tested with data loss, communication failure and anomalous input.
6. **Data protection.** Federated access, no central data pool; real data only where agreements exist, otherwise high-fidelity proxies, open data or synthetic data.

## Work Plan

### Proposed schedule by month

| Months  | Activity                                                                                                                                 | Gate                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| M16–M18 | WP6 kickoff, evaluation plan per pilot based on D3.2, baseline measurements start, pilot site checks                                     | **WS2** Interim review (M18)    |
| M18–M22 | Pilot protocols, ethics and consent documents, data access confirmed per pilot, test data sets, measurement tooling                      | M6 Methodology prototype (M22)  |
| M20–M26 | Retrospective trials on historical data (ECP), baseline for EDCR and ESLA, first data pipelines tested with alpha components (M24)       | M5 Draft platform core (M20)    |
| M26     | **Dry run** of the ECP tool on test data, pre-validation report signed off by pilot partners                                             | **M7** Mid-term pilot readiness |
| M26–M30 | Preparation of beta deployment at all pilot sites, T6.4 test harness and load tests on the alpha                                         | M8 Beta release (M30)           |
| M30–M34 | Pilot operation with the beta toolboxes: ECP prospective trials, EDCR shadow mode, ESLA workflow comparison, T6.4 stress and fault tests | **WS3** Impact evaluation (M32) |
| M34–M36 | Data analysis, cross-case evaluation and replication analysis, reports D6.1–D6.4, TRL 5 assessment                                       | **M9** (M36), **M10** (M36)     |

*Proposed.* The key constraint is that the beta platform arrives at M30 and the reports are due at M36, leaving about four months of pilot operation. Everything that can be prepared earlier (protocols, baselines, test data, tooling, consent, dry runs with the alpha) must be done before M30. This is the main reason for the M26 dry run and for starting evaluation planning at M16.

### Task T6.1 Validation of use case ECP (Italy, Austria)

**Partners (from the proposal):** UNICA (lead), AIT, FLOSS, KTH.

**Goal.** Verify that the assistant supports citizen-led energy community planning and meets O3 and O4.

**From the proposal:**

- Retrospective trials on historical planning cases.
- Prospective planning activities with emerging communities.
- AI-generated recommendations compared with expert benchmarks, in shadow mode.
- Assessment of usability, planning efficiency and regulatory adaptability across national contexts.
- Live pilot in Italy (UNICA and FLOSS with Sardinian energy communities), high-fidelity simulation in Austria (AIT with its network of Austrian energy communities).
- Target impact: planning in 4–8 weeks instead of several months; assessment time from about 3 months to under 21 days.

**Proposed evaluation design:**

| Element    | Proposal                                                                                                                                                                                                                      |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cases      | A set of historical cases per country with known expert solutions (retrospective), plus two or three emerging communities in Italy and simulated communities in Austria (prospective)                                         |
| Baseline   | Time and cost of conventional planning (consultant or spreadsheet), recorded for the same case types                                                                                                                          |
| Comparison | AI recommendation vs expert plan: PV and storage sizing, financial indicators, community scope                                                                                                                                |
| Users      | Community managers and members, including non-experts, balanced by gender and background                                                                                                                                      |
| Indicators | Planning time, planning accuracy against expert benchmark, task completion and errors in the dialogue, perceived transparency (1 to 5), understanding of the explanation, regulatory correctness of national rules (AT vs IT) |
| Output     | Feasibility & Validation Report: planning accuracy, usability metrics, regulatory compliance                                                                                                                                  |

Open issues: which communities take part, whether live data come from smart meters or from public datasets, and how national incentives (Austrian and Italian) are encoded as rules.

### Task T6.2 Validation of use case EDCR (Sweden, France)

**Partners (from the proposal):** KTH (lead), EIN, IDUN, TRI, IMT.

**Goal.** Validate the explainable decision-support interface for coordinating distributed flexibility, addressing O3 and O4.

**From the proposal:**

- The Swedish pilot builds on the ElectriCITY innovation ecosystem in Hammarby Sjöstad, using real infrastructure data and simulated grid constraints (DSO-informed).
- Recommendations for events such as load peaks, EV charging surges and flexibility activation, with traceable explanations.
- Shadow mode next to human operators, no control of physical assets.
- Evaluation of operator interaction, situational awareness and usefulness of the decision support.
- Targets: 10–20% more hosting capacity and 25–40% fewer congestion hours (evaluated as potential improvements), more than 85% operator acceptance, transparency score of at least 4/5, more than 80% agreement of operators with the AI logic, automated DSO connection pre-assessment in under 4 hours (baseline 40 man-hours).
- Swedish partners: KTH validation lead and coordination, EIN stakeholder and operational context, ProptechOS operational building data and platform support (Energimyndigheten proposal).

**Proposed evaluation design:**

| Element    | Proposal                                                                                                                                                                                                             |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data       | Building and community data through the ProptechOS connectors and semantic API, grid constraints from a model informed by the DSO, historical events for replay                                                      |
| Scenarios  | A catalogue of events: peak load, EV charging surge, PV surplus, loss of a flexible asset, combinations with extreme weather (using synthetic stress scenarios)                                                      |
| Modes      | (1) Replay of historical events with known operator decisions, (2) live shadow mode with operators, (3) tabletop or workshop sessions where operators review recommendations                                         |
| Comparison | AI recommendation vs operator decision, with the physical guardrail result recorded for every recommendation                                                                                                         |
| Indicators | Acceptance rate, agreement with operator logic, transparency and trust scores, time to decision, situational awareness, number of guardrail interventions, hosting capacity and congestion estimates from simulation |
| Audit      | Completeness of the audit trail for every high-risk recommendation (target 100%)                                                                                                                                     |
| Output     | UC-EDCR Validation Report: operator evaluation, explainability metrics, flexibility scenario analysis                                                                                                                |

The proposal also assigns EDCR validation to France (TRI, IMT) but describes only the Swedish setup in detail. The French contribution (which data, which environment, which operators) must be clarified with TRI and IMT early.

Open issues: operator availability and time, access to DSO-informed constraints, data sharing between ProptechOS, EIN and KTH (agreements, privacy), the site equipment (edge devices, gateways) funded by the Swedish budget.

### Task T6.3 Validation of use case ESLA (Austria, France)

**Partners (from the proposal):** AIT (lead), KTH, TRI, IMT.

**Goal.** Validate that agentic orchestration automates the energy service development lifecycle, supporting O1 and O4.

**From the proposal:**

- Automation of data ingestion from distributed sources, simulation dataset preparation and model validation workflows, without centralising sensitive data.
- Comparison of automated workflows with conventional engineering pipelines for services such as demand forecasting, flexibility assessment and building performance modelling.
- Indicators: reduction in manual data preparation effort, development time and workflow errors, robustness of federated data integration across several data providers.
- Impact target: 30–50% shorter development timelines.
- The task description names Austria as the validation environment while the use case is labelled AT/FR; the French role needs to be confirmed.

**Proposed evaluation design:**

| Element            | Proposal                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reference workflow | Fix one or two services (for example a demand forecast and a demand-response algorithm) and measure the conventional development process first                                                                     |
| Automated workflow | Same services built with the ESLA toolbox: synthetic scenario generation, power flow simulation (Pandapower, OpenDSS), model training, analysis                                                                    |
| Measures           | Person-hours for data preparation and development, elapsed time, number of workflow errors and reruns, autonomy rate (steps completed without human intervention, target above 90%), compliance trail completeness |
| Users              | Developers and service operators at AIT and partner organisations                                                                                                                                                  |
| Output             | UC-ESLA Validation Report: efficiency gains and performance of the orchestration framework                                                                                                                         |

### Task T6.4 Robustness, Contingency & Scalability Validation

**Partners (from the proposal):** KTH (lead), UNICA, IMT. The proposal lists KTH twice in the partner list.

**Goal.** Evaluate the safe, robust and scalable operation of the framework under non-nominal conditions, in parallel with T6.1 to T6.3.

**From the proposal:**

- Stress tests with high data loads and many concurrent users.
- Simulated failures such as temporary loss of data sources or communication links, to verify degraded-mode behaviour.
- Detection of anomalous or inconsistent input data and flagging in the trust layer.
- Scalability by simulating multiple virtual communities and bigger data flows (risk table: performance when going above 10 communities or 100 concurrent agents).
- Validation of human-in-the-loop fallback: low-confidence recommendations lead to operator intervention and not to automatic action.
- Evidence of "Safety-by-Design" for O1 and O3, and for commercial exploitation.

**Proposed test catalogue:**

| Test family             | Examples                                                                                                    | Metric                                                                                                |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Load                    | 10, 50 and 100 virtual communities, 100+ concurrent agents, bursts of IoT messages                          | Response time, throughput, error rate, resource use                                                   |
| Federation latency      | Cross-site SPARQL queries over several nodes, with and without edge caching                                 | Share of queries under 2 s (target 90%), semantic mapping time under 500 ms                           |
| Fault injection         | Data source down, delayed or stale data, link loss, agent crash, convergence failure of the grid simulation | Recovery time, fallback behaviour, share of agent recoveries without failure                          |
| Data quality            | Missing values, outliers, inconsistent units, conflicting sources                                           | Detection rate, false alarms, flags in the audit log                                                  |
| Guardrail and oversight | Recommendations that violate voltage or capacity limits, low-confidence cases, manual override              | Rejection by guardrail (100% of violations), operator escalation rate, guardrail latency under 100 ms |
| Security                | Role-based access checks, unauthorised tool use                                                             | Policy violations blocked                                                                             |

Output: Robustness & Contingency Evaluation Report with resilience metrics, fault-tolerance behaviour and operational limits.

Proposed: start building the test harness at M26 so that the first load and fault tests run on the alpha and the beta tests only repeat them.

## Evaluation Framework

The framework itself is defined in WP3 (T3.2, D3.2). WP6 applies it. See [GDE-0003](GDE-0003-wp3-requirements-and-architecture-design.md) for the KPI list per objective.

### What WP6 must show for each objective

| Objective | KPI (proposal)                                                                                                 | Main WP6 task    | Timing in proposal |
| --------- | -------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| O1        | 30–50% less manual engineering effort, above 90% task autonomy, 15–20% local peak load reduction               | T6.3, T6.4       | M30–M36            |
| O2        | Under 500 ms semantic mapping, under 2 s for 90% of queries, 50% less onboarding time                          | T6.4, all pilots | M22–M36            |
| O3        | 100% audit trail, 85% acceptance, transparency at least 4/5, over 80% expert agreement                         | T6.2, T6.1, T6.4 | M22–M36            |
| O4        | Assessment under 21 days, DSO pre-assessment under 4 hours, +10–20% hosting capacity, −25–40% congestion hours | T6.1, T6.2       | M36                |

### Data collection and analysis (proposed)

- One **KPI data sheet** per pilot, prefilled from D3.2, with measurement date, value, method and evidence link.
- Automatic logging wherever possible (platform logs, audit logger, workflow timers) to avoid manual reporting.
- Surveys and interviews with a common questionnaire for transparency, trust and usability, run in the local language, with consent and anonymisation.
- A common data format and a shared repository for results, compatible with the project data management plan (D1.2).
- **Cross-case evaluation** after the pilots: compare results across ECP, EDCR and ESLA and across countries, discuss what depends on national regulation, and write the replication analysis that the proposal promises.
- **Independent verification.** The proposal names independent verification by partners, stakeholders and community managers as evidence for O4. Proposed: each pilot's results are reviewed by a partner who did not run that pilot.

### TRL 5 assessment

At M36 the task is to show that the integrated system works in a relevant environment. Proposed evidence pack: the integrated platform description (D3.3), proof that all three toolboxes ran on the beta in the pilot environments, KPI results against targets, the T6.4 evidence, and a short TRL checklist signed off by the pilot partners and discussed at WS3.

## Pilot Environments and Responsibilities

| Pilot   | Use case   | Host and participants                             | Environment                                               | Data                                                                 |
| ------- | ---------- | ------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------- |
| Italy   | ECP        | UNICA, FLOSS, Sardinian energy communities        | Live planning pilot                                       | Community and public data, regulation rules                          |
| Austria | ECP, ESLA  | AIT, Austrian energy communities                  | High-fidelity simulation, service development environment | Utility-grade datasets and models from partners                      |
| Sweden  | EDCR       | KTH, EIN, ProptechOS, Hammarby Sjöstad Living Lab | Relevant operational environment, shadow mode             | Real community and building data, DSO-informed simulated constraints |
| France  | EDCR, ESLA | TRI, IMT                                          | To be specified                                           | To be specified                                                      |

For the Swedish pilot, KTH and EIN have a long-term agreement on the Hammarby Sjöstad testbed (proposal, section 3.2). The Swedish budget also covers pilot equipment at ProptechOS (edge devices, IoT gateways), computing equipment and purchased cloud services at KTH, and travel for pilot work.

## Governance and Roles

*Proposed.*

| Role               | Who                                        | Responsibility                                                   |
| ------------------ | ------------------------------------------ | ---------------------------------------------------------------- |
| WP leader          | KTH                                        | Plan, coordination, consistency of the evaluation, final reports |
| Task leaders       | UNICA (T6.1), KTH (T6.2, T6.4), AIT (T6.3) | Protocols, execution, task reports                               |
| Pilot coordinators | One named person per pilot                 | Site access, participants, local logistics, data agreements      |
| Evaluation lead    | One named person in KTH                    | KPI data sheets, analysis, cross-case evaluation                 |
| Reviewers          | A partner who did not run the pilot        | Independent verification                                         |

- **Meetings:** monthly WP6 call from M16, fortnightly from M26, plus a pilot readiness review before M30.
- **Evaluation protocol per pilot** approved before data collection starts, including ethics, consent and privacy handling.
- **Reporting rhythm:** short monthly KPI status from each pilot, WP6 summary for the periodic reports (D2.2 at M24, D2.3 at M36).
- **Issue handling:** problems found in the platform are logged and passed to WP5 with severity, so that the beta can be fixed during the pilot period. A fix freeze date before the final measurements is needed.

## Risks

| Risk                                                   | Source                  | Mitigation                                                                                                            |
| ------------------------------------------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Data silos and unstable data access                    | Proposal, WP3, WP5, WP6 | Data access agreements early, M7 readiness check, synthetic data generators                                           |
| Pilot user disengagement                               | Proposal, WP6 and WP2   | Community managers at each site, communicate benefits, gamified feedback in the toolboxes                             |
| Platform scalability limits                            | Proposal, WP5 and WP6   | Simulated load tests in T6.4, modular microservices                                                                   |
| Divergent or changing regulation                       | Proposal, WP6 and WP2   | Monitoring in T2.2, reconfigurable regulatory guardrails                                                              |
| Explanations too technical                             | Proposal, WP4 and WP6   | Trust score tracking in WP6, iterative UI testing in WP5                                                              |
| Beta arrives late (M30) and shortens the pilot period  | Proposed                | Alpha demos at M24, dry run at M26, evaluation tooling and protocols ready before M30, earlier access for pilot hosts |
| Operators have little time for shadow-mode sessions    | Proposed                | Agree schedule with EIN and DSO early, use replay of historical events, short sessions                                |
| KPI baselines missing, so improvements cannot be shown | Proposed                | Measure baselines from M16 (before the AI is used)                                                                    |
| French and Austrian pilot setups unclear               | Proposed                | Clarify scope with TRI, IMT and AIT before WS2                                                                        |
| Ethics and privacy approvals take long                 | Proposed                | Prepare protocols at M18–M22, check national requirements per country                                                 |

## Kickoff Meeting Context

The agenda is in `resources/kickoff_agenda.pdf` (issued by AIT). WP6 is the third work package session on day 2, after WP4 and WP5, and it leads straight into the cross-WP alignment. What comes before and after it shapes the WP6 slides.

| Time | Item (agenda) | What it means for the WP6 session |
| ---- | ------------- | --------------------------------- |
| Day 1, 13:55 | Project overview (AIT): use cases, objectives and KPIs, timeline and milestones | The KPIs and use cases are known. WP6 shows only the evidence each KPI needs |
| Day 1, 16:45 | WP3 (KTH): blueprints, validation framework, architecture | The KPI framework, baselines and shadow-mode protocol were introduced the day before. WP6 refers to them |
| 09:00 | Welcome back, recap of day 1 (AIT) | Update the opening of the WP6 deck with the day 1 outcomes (pilot contacts, data inventory dates) |
| 09:10 | WP4 (UNICA): methods, D4.1 to D4.3, MS6 (TRL 4) | WP6 builds on TRL 4 and the trust metrics. Do not re-explain the methods |
| 09:50 | WP5 (FLOSSLAB): runtime, data backbone, toolboxes, explainability module, D5.1 to D5.4, MS5 and MS8 | The alpha and beta dates come from WP5. The WP6 timeline must match what WP5 presents, and the pilot hosts need early access |
| 10:30 | Coffee break | |
| 10:45 | **WP6 (KTH), 40 minutes** | About 22 minutes of slides, 10 minutes of discussion, 8 minutes of buffer |
| 11:25 | Cross-WP alignment (all, 20 minutes): interfaces, dependencies, who needs what from whom and when, joint timeline | Direct continuation. The "what WP6 needs from other WPs" table in the deck is the input |
| 11:45 | Next steps, action items, next plenary and online meetings (AIT) | The asks are written as action items with owner and date |
| 12:00 | End of meeting, lunch | Hard stop, so the WP6 session must not run over |

## Open Questions for the Kickoff

1. Who is the named pilot coordinator in each country? (Partly covered by the WP3 asks on day 1.)
2. What is the French EDCR and ESLA pilot concretely (environment, data, participants)?
3. Which Austrian communities and datasets are used for ECP and ESLA?
4. What is the date for beta access for pilot hosts, and can an earlier preview be agreed? Compare with the dates WP5 presents at 09:50.
5. What are the baselines available today for planning time, DSO connection studies and service development time?
6. Which ethics or data protection approvals are needed in each country, and who prepares them?
7. Who acts as independent reviewer for each pilot?
8. How will results be stored and shared (repository, format), and what can be published openly? The shared workspace is presented under WP1 on day 1.
9. What do WP3, WP4 and WP5 give WP6, and when? Settle it at the alignment session at 11:25.

## Kickoff Presentation: Slot and Slide Structure

*Proposed.* WP6 starts at M16, so the focus is on a shared picture of TRL 5 and on what must be prepared early. The deck is a decision-driven core of 11 slides plus backup slides (see [BST-0001](../brainstorming/BST-0001-wp-presentation-structure-for-kickoff-meeting.md) for the reasoning).

| # | Slide | Content | Time |
| - | ----- | ------- | ---- |
| 1 | WP6: Use Case Validation | Title, one-line goal | 1 min |
| 2 | What we must prove | Evidence each objective needs | 2 min |
| 3 | What TRL 5 means here | Relevant environment, shadow mode, one KPI framework, degraded mode | 2 min |
| 4 | Four pilots, four countries | Hosts, environments, the open French pilot | 3 min |
| 5 | Timeline and the tight window | M16 to M36 with WP5 dates, about four months of pilots | 3 min |
| 6 | How each use case is evaluated | What is compared with what, plus T6.4 | 3 min |
| 7 | From KPI to evidence | KPI, source, measurement, owner, report | 2 min |
| 8 | Ready before M30 | Baselines, data access, ethics, coordinators, test harness | 2 min |
| 9 | What WP6 needs from other WPs | Input to the 11:25 alignment | 2 min |
| 10 | What we need from you now | Five asks as action items | 2 min |
| 11 | Discussion | Four questions | 10 min |
| Backup | Effort, evaluation design, test catalogue, roles, risks | For questions | n/a |

Supporting material to prepare in advance: a one-page timeline from M16 to M36 with the dependencies on WP3 and WP5, a pilot fact sheet template, and a table of baseline data still to be collected.

## References

- Kickoff meeting agenda: `resources/kickoff_agenda.pdf` (AIT, Vienna, 30 November and 1 December 2026)
- Slide deck: `site/slides/wp6-kickoff.qmd`
- International proposal: `resources/full_proposal_international.pdf`, sections 1.2, 1.3, 2.1 and 3.1 (WP6 description, tables 3a, 3c, 3d, 3e, 3f)
- Swedish proposal to Energimyndigheten: `resources/full_proposal_swedish.pdf` (Swedish activities, budget per WP and per partner)
- [GDE-0001 Plenergy.AI: Overview](GDE-0001-plenergy-ai-overview.md)
- [GDE-0002 Plenergy.AI: Implementation](GDE-0002-plenergy-ai-implementation.md)
- [GDE-0003 WP3: Requirements and Architecture Design](GDE-0003-wp3-requirements-and-architecture-design.md)
