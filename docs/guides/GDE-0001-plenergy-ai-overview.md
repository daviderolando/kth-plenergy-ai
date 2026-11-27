---
title: "GDE-0001 Plenergy.AI: Overview"
id: GDE-0001
type: guide
status: active
created: "2026-11-27"
tags: [plenergy-ai, overview, cetpartnership, consortium, work-packages]
related: [GDE-0002, GDE-0003, GDE-0004]
---

## Overview

This guide gives a short orientation to **Plenergy.AI**: what the project sets out to do, who is in the consortium, and how the work is organised into work packages (WPs). It is meant for new team members, collaborators and anyone who needs the big picture before reading the full proposals.

After reading it you should be able to name the project objectives, the three technical pillars, the three use cases, the eight partners and their roles, and the six work packages with their leads, timing and main tasks.

The content is summarised from the two proposals linked in `resources/`. If this guide and a proposal disagree, the proposal wins; please correct the guide.

| Item                     | Value                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Acronym                  | Plenergy.AI                                                                                                              |
| Title                    | A Federated, Explainable, and Semantic Aware Assistant for Planning and Operation of Distributed Digital Energy Services |
| Funding scheme           | CETPartnership Joint Call 2025, Call Module CM02 (proposal code CETP-2025-00540)                                         |
| Coordinator              | Marc Dünser, AIT Austrian Institute of Technology                                                                        |
| Duration                 | 36 months. The Swedish part runs 2026-11-01 to 2029-10-31                                                                |
| Maturity target          | TRL 3 to TRL 5                                                                                                           |
| Consortium               | 8 partners from 4 countries (AT, IT, FR, SE)                                                                             |
| Total project cost       | About 2.1 M EUR, as stated in the international proposal                                                                 |
| Swedish national funding | Energimyndigheten, with KTH as Swedish coordinator and project leader                                                    |

## Background and Motivation

European distribution grids are turning into cyber-physical systems with many distributed renewable assets and prosumers. Energy communities and aggregators now do work that large utilities used to do, but they often lack the IT capacity for it. Existing AI tools tend to be either too narrow (one task, no context) or too opaque (optimisation with no explanation). The EU AI Act classifies energy grid management as high-risk, which makes transparency, human oversight and auditability mandatory.

Plenergy.AI aims to close that gap with one assistant platform that is interoperable across domains and explainable by design.

## Technical Pillars

The platform rests on three pillars. A fourth objective, demonstration, ties them together.

1. **Agentic AI orchestration.** A modular multi-agent engine coordinates energy workflows such as community sizing, tariff optimisation, congestion analysis and flexibility dispatch. Planning uses Hierarchical Task Networks, so the engine can re-plan when an asset becomes unavailable.
2. **Federated knowledge integration.** Semantic connectors map distributed data to common ontologies (IEC CIM and PECO, the PARMENIDES Energy Community Ontology) in a federated knowledge graph. Data stays with its owner and the approach follows FAIR principles.
3. **Explainable AI recommendations.** Every recommendation comes with a human-readable justification covering assumptions, data sources and regulatory drivers. A deterministic neuro-symbolic safety layer checks control recommendations against grid constraints, and the AI runs in shadow mode next to human decisions during validation.

## Main Objectives

| ID  | Objective                                                                                                                       | Headline KPIs                                                                                                                     | Timing  |
| --- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------- |
| O1  | Develop an **Agentic AI Orchestration** engine that automates coordination of distributed flexibility and grid-support services | 30–50% less manual engineering effort; more than 90% task autonomy; 15–20% local peak load reduction                              | M30–M36 |
| O2  | Implement **Federated Knowledge Integration** with semantic interoperability, without centralising sensitive data               | Semantic mapping under 500 ms per data point; cross-site queries under 2 s for 90% of requests; at least 50% less onboarding time | M22–M36 |
| O3  | Provide **Explainable AI Recommendations** that are transparent and compliant with the EU AI Act and GDPR                       | 100% audit trail for high-risk decisions; 85% operator acceptance; transparency score of at least 4/5                             | M22–M36 |
| O4  | **Demonstrate** value across three use cases and raise solution maturity                                                        | Planning time cut from about 3 months to under 21 days; 10–20% more hosting capacity; 25–40% fewer congestion hours               | M36     |

## Use Cases

| Use case                                      | Countries | Primary pillar                  | What it validates                                                                                                                                                          |
| --------------------------------------------- | --------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ECP**, Energy Community Planning            | AT, IT    | Federated knowledge integration | Natural-language guidance for non-experts sizing PV and storage and assessing financial viability. Live pilot in Italy, high-fidelity simulation in Austria                |
| **EDCR**, Explainable Digital Control Room    | SE, FR    | Explainable recommendations     | Decision support for community and DSO operations under high renewable share, using real operational data in shadow mode. Swedish pilot in the Hammarby Sjöstad Living Lab |
| **ESLA**, Energy Service Lifecycle Automation | AT, FR    | Agentic orchestration           | Automated synthetic data generation, model training, simulation and testing for energy software developers                                                                 |

## Consortium

Eight partners from four countries cover the chain from ontology research to software industrialisation and real-world piloting.

| Partner                                   | Country | Type                    | Role                                                                                                |
| ----------------------------------------- | ------- | ----------------------- | --------------------------------------------------------------------------------------------------- |
| **AIT**, Austrian Institute of Technology | AT      | Research organisation   | Project coordinator. Leads agentic orchestration and physics-grounded agent workflows               |
| **UNICA**, University of Cagliari         | IT      | University              | Scientific lead. Federated semantics, ontology engineering, neuro-symbolic AI                       |
| **FLOSS**, Flosslab s.r.l.                | IT      | SME                     | Technical lead. Agent engine development, software architecture, SaaS UI                            |
| **KTH**, Royal Institute of Technology    | SE      | University              | Validation lead. Requirements, architecture, KPIs, pilot validation and impact assessment           |
| **EIN**, ElectriCITY Innovation           | SE      | Non-profit organisation | Engagement lead. Living Lab orchestration, citizen co-creation, host of the Swedish pilot           |
| **IDUN**, Idun Real Estate Solutions (now ProptechOS AB) | SE | SME                  | Building and IoT data integration, semantic connectors (ProptechOS platform)                        |
| **TRI**, Trialog                          | FR      | SME                     | Exploitation lead. EU AI Act compliance, trust framework, audit logging, interoperability standards |
| **IMT**, IMT Télécom SudParis             | FR      | University              | XAI frameworks, trust-by-design, semantic web standards                                             |

The Swedish proposal states that Idun Real Estate Solutions has changed its name to ProptechOS, with the same organisation number and legal entity. The international proposal still says IDUN, so both names appear in the project documents.

Prior collaborations reduce delivery risk. AIT, KTH and TRI worked together on PARMENIDES, which produced the PECO ontology this project extends. KTH and EIN have a long-term agreement on the Hammarby Sjöstad testbed.

### Effort by partner (person-months)

| Partner | WP1 | WP2 | WP3  | WP4  | WP5  | WP6  | Total |
| ------- | --- | --- | ---- | ---- | ---- | ---- | ----- |
| AIT     | 3.3 | 1.8 | 5.6  | 17.4 | 14.8 | 7.6  | 50.5  |
| UNICA   | 1.0 | 1.0 | 3.0  | 7.0  | 3.0  | 3.0  | 18.0  |
| FLOSS   | 1.0 | 1.0 | 2.0  | 3.0  | 8.0  | 3.0  | 18.0  |
| KTH     | 1.0 | 1.0 | 11.0 | 1.0  | 4.0  | 10.0 | 28.0  |
| EIN     | 1.5 | 1.5 | 7.0  | 0.0  | 2.0  | 12.0 | 24.0  |
| IDUN    | 0.5 | 0.5 | 3.0  | 0.0  | 5.5  | 2.5  | 12.0  |
| TRI     | 1.0 | 1.0 | 1.0  | 5.0  | 5.0  | 5.0  | 18.0  |
| IMT     | 1.0 | 1.5 | 5.0  | 20.5 | 16.0 | 10.0 | 54.0  |

## Work Package Structure

The work plan has six work packages. WP1 and WP2 run for the whole project. WP3 to WP6 are the technical chain, and each one moves the maturity level up a step.

| WP  | Title                                           | Lead  | PMs  | Start | End | Target TRL |
| --- | ----------------------------------------------- | ----- | ---- | ----- | --- | ---------- |
| WP1 | Project Management                              | AIT   | 10.3 | M01   | M36 | n/a        |
| WP2 | Reporting & Knowledge Community                 | AIT   | 9.3  | M01   | M36 | n/a        |
| WP3 | Requirements and Architecture Design            | KTH   | 37.6 | M01   | M09 | TRL 3      |
| WP4 | Theoretical and Methodological Foundations      | UNICA | 53.9 | M06   | M22 | TRL 4      |
| WP5 | Platform Development and Toolbox Implementation | FLOSS | 58.3 | M12   | M30 | TRL 4+     |
| WP6 | Use Case Validation and Performance Assessment  | KTH   | 53.1 | M16   | M36 | TRL 5      |

```text
Month   1         6           12          18          24          30          36
WP1     ████████████████████████████████████████████████████████████████████████
WP2     ████████████████████████████████████████████████████████████████████████
WP3     ██████████████████
WP4               ██████████████████████████████████
WP5                           ██████████████████████████████████████
WP6                                   ██████████████████████████████████████████
```

### WP1 Project Management (AIT)

Coordination, financial and administrative management, risk control and quality assurance. WP1 anchors the Trust-by-Design approach with human-in-the-loop governance, so that no automated decision is made without oversight, interpretability and the ability to intervene.

- T1.1 Project Coordination & Governance
- T1.2 Risk Management, Regulatory Compliance, and Trust-by-Design Auditing
- T1.3 Federated Data Governance & FAIR Transparency
- T1.4 Strategy for Communication, Dissemination, and Exploitation

Main outputs: Project Handbook (D1.1), Data Management Plan (D1.2), Plan for the Dissemination and Exploitation of Results (D1.3).

### WP2 Reporting & Knowledge Community (AIT)

Formal reporting at M12, M24 and M36, plus active contribution to the CETPartnership Knowledge Community and European platforms such as ETIP SNET, including policy briefs for regulators.

- T2.1 Periodic Reporting
- T2.2 Knowledge Community Engagement

Main outputs: periodic progress reports (D2.1 to D2.3) and the Policy & Knowledge Community Report (D2.4).

### WP3 Requirements and Architecture Design (KTH)

Co-design with DSOs, energy communities and building operators to turn the vision into requirements, data interfaces, a modular architecture and a common validation framework.

- T3.1 Use Case Blueprints & Semantic Scoping (KTH)
- T3.2 Stakeholder Validation, KPIs & Impact Planning (KTH)
- T3.3 Modular System Architecture & Trust-by-Design Blueprint (AIT)

Main outputs, all at M09: User-Centric Blueprint Portfolio (D3.1), Validation & Impact Framework with the KPI scorecard (D3.2), Trust-by-Design Architecture Specification (D3.3). Details are in [GDE-0003](GDE-0003-wp3-requirements-and-architecture-design.md).

### WP4 Theoretical and Methodological Foundations (UNICA)

Algorithmic foundation of the platform, taking the technology from TRL 3 to TRL 4. It develops neuro-symbolic methods that combine generative AI with structured energy domain knowledge.

- T4.1 Agentic AI Orchestration Models (AIT)
- T4.2 Federated Knowledge Integration Framework (UNICA)
- T4.3 Explainable AI Recommendations and Trust Framework (TRI)

Main outputs: Library of Agentic Orchestration Patterns (D4.1), plus the federated semantic and XAI frameworks.

### WP5 Platform Development and Toolbox Implementation (FLOSS)

Turns the WP4 models into a scalable, cloud-native platform with an alpha demo by M24 and a beta release by M30. It also provides interoperability with external systems and IoT gateways.

- T5.1 Agent Orchestration Runtime (FLOSS)
- T5.2 Federated Knowledge Integration Layer (UNICA)
- T5.3 Use Case Toolboxes & Human-Centric Interfaces (AIT)
- T5.4 Explainable AI Recommendation Framework (IMT)

### WP6 Use Case Validation and Performance Assessment (KTH)

Validation of the platform in relevant environments using the WP3 KPI framework, advancing the system to TRL 5 and measuring technical performance, usability and trust.

- T6.1 Validation of use case ECP (UNICA)
- T6.2 Validation of use case EDCR (KTH)
- T6.3 Validation of use case ESLA (AIT)
- T6.4 Robustness, Contingency & Scalability Validation (KTH)

Details are in [GDE-0004](GDE-0004-wp6-use-case-validation-and-performance-assessment.md).

Main outputs: validation reports for ECP (D6.1), EDCR (D6.2) and ESLA (D6.3), and the Robustness & Contingency Report (D6.4), all at M36.

### How the work packages connect

```text
WP3 requirements, architecture, KPI framework
   ├─> WP4 methods and logic ──> WP5 platform and toolboxes ──> WP6 validation
   └──────────────── KPI scorecard ─────────────────────────────────┘
WP1 management and WP2 reporting run alongside all of the above
```

Stakeholder workshops mark the maturity steps: WS1 co-creation at M3 (TRL 3), WS2 interim review at M18 (TRL 4) and WS3 impact evaluation at M32 (TRL 5).

## Key Exploitable Results

1. Agentic Orchestration Engine
2. Federated Semantic Middleware
3. Explainability & Trust Blueprint
4. ECP Toolbox
5. EDCR Toolbox
6. ESLA Toolbox

Non-proprietary semantic models and the Connector SDK are planned for open-source release (Apache 2.0) on Zenodo.

## The Swedish Part

KTH (Energy Technology) coordinates the Swedish participation, which Energimyndigheten funds nationally. It covers pilot validation, building data integration and user-centred evaluation in the Hammarby Sjöstad Living Lab, together with EIN and IDUN (ProptechOS). KTH leads WP3 and WP6, and therefore the requirements, the KPI framework and the validation of all three use cases.

Energimyndigheten funding requested for the Swedish partners is 6 284 299 SEK in total (rate 1 EUR = 11.001 SEK):

| Partner | Requested (SEK) | Support level |
| ------- | --------------- | ------------- |
| KTH | 3 138 013 | 100% |
| EIN | 2 002 182 | 100% |
| ProptechOS | 800 874 (plus 343 230 own funding) | 70% |

The largest Swedish shares go to WP3 (2 102 787 SEK) and WP6 (2 360 165 SEK), the two work packages KTH leads.

## References

- Kickoff meeting agenda: `resources/kickoff_agenda.pdf` (AIT, Vienna, 30 November and 1 December 2026)
- International proposal: `resources/full_proposal_international.pdf` (CETP-2025-00540, full proposal dated 2026-03-11)
- Swedish proposal to Energimyndigheten: `resources/full_proposal_swedish.pdf`
- [GDE-0002 Plenergy.AI: Implementation](GDE-0002-plenergy-ai-implementation.md), work package by work package
- [GDE-0003 WP3](GDE-0003-wp3-requirements-and-architecture-design.md) and [GDE-0004 WP6](GDE-0004-wp6-use-case-validation-and-performance-assessment.md), the two work packages led by KTH
- [resources/README.md](../../resources/README.md) for how the symbolic links to the shared proposal folder are set up
