---
title: "BST-0001 WP presentation structure for kickoff meeting"
id: BST-0001
type: brainstorming
status: draft
created: "2026-11-27"
tags: [plenergy-ai, kickoff, wp3, wp6, slides, presentation, kth-template]
related: [GDE-0003, GDE-0004]
---

## Context

KTH leads two work packages, WP3 (Requirements and Architecture Design) and WP6 (Use Case Validation and Performance Assessment). At the project kickoff meeting, with all eight partners in the room, the WP leader presents each of them in a separate slide deck and discusses the implementation with the partners.

The two work packages are very different in timing:

- **WP3 starts at M01.** Partners must act within weeks: name contacts, provide data inventories, join workshops, review drafts. The deck has to produce commitments.
- **WP6 starts at M16**, more than a year after the kickoff. Nobody will run a pilot soon. The deck has to give a shared picture of the end goal and list what must be prepared early, without asking for details that cannot be known yet.

A deck that is too long, too dense, or that lists tasks the partners already know from the proposal wastes the one moment when everyone is present. The goal is to use the slot to align and to collect decisions.

The kickoff agenda (`resources/kickoff_agenda.pdf`, issued by AIT) fixes the slots: WP3 on day 1 (30 November 2026) at 16:45 for 45 minutes, and WP6 on day 2 (1 December 2026) at 10:45 for 40 minutes. The meeting is on site at AIT in Vienna with hybrid logistics. What is discussed before and after each slot shapes the content (see [Kickoff agenda and its consequences](#kickoff-agenda-and-its-consequences)).

Both decks are built on the official KTH PowerPoint template (`resources/kth_template_presentation.pdf` is a preview of it) and use the KTH logo (`resources/kth_logo.png`). The template sets hard limits on what a slide can hold, so it shapes the structure as much as the content does (see [Template constraints](#template-constraints)).

The detailed content is in [GDE-0003](../guides/GDE-0003-wp3-requirements-and-architecture-design.md) and [GDE-0004](../guides/GDE-0004-wp6-use-case-validation-and-performance-assessment.md), each with a first slide list. This note takes a step back: what shape should the two decks have, and what should each slide do?

## Objectives

What we want the partners to leave the room with:

**WP3**

- A shared understanding of what is frozen at M09 and why it matters for WP4, WP5 and WP6.
- A named contact and a time commitment from every partner for M01–M09.
- Agreement on the way of working: requirements register, review cycle, workshop WS1 at M3.
- First inputs started: data inventory, stakeholder lists, MSAB candidates.

**WP6**

- A shared picture of what "validated at TRL 5" means and how it will be measured.
- Awareness that the pilot window is short (beta at M30, reports at M36) and of what must therefore be prepared before M30.
- The open scoping issues named, especially the French pilots and the Austrian setup.
- A list of early preparation items with owners (baselines, data access, ethics, pilot coordinators).

**Both decks**

- Fit the slot, leave real time for discussion.
- Follow the KTH template without changes to the master slides, so that the decks are correct on brand and easy to edit by others.
- Be reusable later: the same slides serve the General Assembly, the WS1 and WS2 workshops and the periodic reports.

## Current Situation

- The two guides each propose a slide list of 15 slides, a 30 to 40 minute slot and the content per slide. This is a good starting point, but it is a plain sequence of topics and it ignores the template.
- The kickoff agenda is known (see below). The WP3 and WP6 slots are 45 and 40 minutes, and both are followed by a joint discussion slot.
- The audience is mixed: university researchers (AIT, UNICA, IMT, KTH), SMEs (FLOSS, TRI, ProptechOS), and a living lab (EIN). The SMEs and EIN care mainly about effort, data requests and what they have to build or host.
- Many partners wrote parts of the proposal, so they know the task list. They do not know the working method, the dates, or what is expected of them in the next three months.
- Language is English. Slides will be shown in a room and probably also online, so they must be readable at a distance and without the speaker.
- The proposal has unresolved items that should surface openly at the kickoff and not later: the French EDCR and ESLA pilot setup, the exact Austrian setup, the pilot baselines, the date of the first workshop.
- The template I have is a 4-page PDF preview. The editable `.pptx` is the KTH file `KTH-PPT-template-251203` in the KTH templates folder (according to the file name, the version of 2025-12-03). Fonts, placeholders and slide numbering must be checked in that file and not in the PDF.

### Kickoff agenda and its consequences

Source: `resources/kickoff_agenda.pdf`. Relevant items around the two slots:

| When | Item | Who | Consequence |
| ---- | ---- | --- | ----------- |
| Day 1, 13:15 | Round table, about 5 minutes per partner on team and role | All | Partners are introduced. No roles slide in the WP decks |
| Day 1, 13:55 | Project overview: pillars, use cases, objectives and KPIs, timeline and milestones | AIT | Already shown. The WP3 and WP6 decks only add detail and do not repeat it |
| Day 1, 14:40 | WP1 and WP2: bodies and roles, decision making, meeting cadence, reporting, shared workspace | AIT | Governance and workspace are set there. The "how we decide" slide covers only WP3 rules |
| Day 1, 15:30 | Consortium Agreement and funding contracts | AIT, all | Data access and IPR conditions, relevant for the WP3 data inventory |
| Day 1, 16:00 | First six months: D1.1 to D1.3, advisory board nominations, website, logo, templates | AIT, all | MSAB nominations are collected before WP3. WP3 asks only for its first meeting. Logo and templates may affect the deck template |
| **Day 1, 16:45** | **WP3, 45 minutes** | **KTH** | Last session of the day, after a coffee break. About 25 minutes of slides, 15 of discussion, 5 of buffer |
| Day 1, 17:30 | Open discussion, parking lot, wrap-up of day 1 | All | Open WP3 questions can move to the parking lot |
| Day 2, 09:10 | WP4, 40 minutes | UNICA | Presents after WP3. WP3 must say what WP4 can expect and when |
| Day 2, 09:50 | WP5, 40 minutes | FLOSSLAB | Sets the alpha and beta dates that the WP6 timeline relies on |
| **Day 2, 10:45** | **WP6, 40 minutes** | **KTH** | About 22 minutes of slides, 10 of discussion, 8 of buffer |
| Day 2, 11:25 | Cross-WP alignment: interfaces, dependencies, who needs what from whom and when, joint timeline towards MS3 | All | Direct continuation of both decks. Each deck contains a hand-over table that feeds this session |
| Day 2, 11:45 | Next steps, action items, next plenary | AIT | Asks are written as action items with owner and date |
| Day 2, 12:00 | End of meeting | | Hard stop |

What this changes compared with the first version of this note:

- **No repeated content.** AIT presents the vision, pillars, use cases, KPIs and milestones on day 1, and the partners introduce themselves. The WP3 deck no longer introduces the use cases and KPIs as new. The WP6 deck shows the evidence each KPI needs and leaves the KPIs themselves out.
- **Governance and workspace come from WP1.** The requirements register and the decision log go into the shared workspace presented at 14:40, so the "which tool" question is closed.
- **MSAB nominations come before WP3.** The WP3 asks no longer collect candidates.
- **Hand-over tables for the alignment session.** WP3 adds "What WP4 to WP6 get, and when" and WP6 adds "What WP6 needs from other WPs". Both are built to be used again at 11:25.
- **WP4 and WP5 present between the two decks.** The WP6 deck must match the dates and scope they present, and WP3 must give WP4 and WP5 something to plan with the evening before.
- **Energy and time of day.** WP3 closes day 1 after a long afternoon, so it stays short and ends in an interactive asks table. WP6 has a hard stop at 12:00 and the alignment session after it, so it runs to time and hands over.
- **Hybrid meeting.** Slide numbers are on and fonts follow the template, so remote participants can follow and refer to slides.

### Template constraints

What the PDF preview shows (16:9, 960 × 540 pt):

| Layout | What it looks like | Use for |
| ------ | ------------------ | ------- |
| 1. Title | Dark navy background, white KTH logo centred at the top, thin blue outline curves in two corners, large empty area below the logo | Opening slide of each deck. Can also work as a divider before the discussion |
| 2. Title and content | White, small navy KTH logo top left, bold navy title, bullets with a blue bullet sign | Most core slides |
| 3. Title, content and one image | As layout 2, with one landscape image on the lower right (about 420 × 280 pt) | A slide with a short list plus a photo or a diagram |
| 4. Title and four images | Four portrait images in a row (about 190 × 350 pt each) below the title | A slide with four items that can be shown by photo |

Measured values in the preview: title 36 pt bold in navy (#000061), body 20 pt black with blue (#004791) bullets, left margin 54 pt, content area from about y = 143 pt to y = 500 pt (about 858 × 350 pt). The layouts do not have a section divider, a two-column layout, a table layout or a footer.

What follows from this:

| Constraint | Consequence for the decks |
| ---------- | ------------------------- |
| Title at 36 pt bold in one line, about 40 characters at most (a longer title wraps and collides with the content) | Titles are short labels or short claims, not full message sentences. The message goes in the first line of the body or in the speaker notes |
| Body at 20 pt, about 10 lines of text fit | At most 5 to 6 bullets of about 8 words. Anything denser goes to the backup |
| Tables do not fit at 20 pt | A table in the core has at most 4 or 5 rows and 3 columns, at 16 pt or more. Longer tables go to the backup and to the handout, where 12 pt is acceptable |
| Only four layouts, no diagram layout | Diagrams are built with native PowerPoint shapes on layout 2 (title only, empty body). Native shapes stay editable and keep the KTH colours. Pasted images of tables from the proposal are not used |
| The logo is already in the layouts | Do not add the logo by hand on the slides. Any extra logo (project or partners) is placed on the title slide only, in its large empty area |
| No slide number or footer | Check in the `.pptx` whether slide numbers can be turned on. In a discussion with online participants, "go back to slide 7" is needed |
| Two colours only: navy and a blue accent | Use-case distinction (ECP, EDCR, ESLA) cannot rely on three new colours. Use tints of the KTH palette from the KTH graphic profile, plus a label or symbol so that the slide is readable in black and white |
| Image layouts come with stock photos | The sample photos in layouts 3 and 4 are placeholders. Replace them with own photos or KTH image bank photos with a clear right to use. Do not keep them just to fill the layout |

### The KTH logo

`resources/kth_logo.png` is the navy version of the logo (1867 × 2092 pixels, with transparent background, portrait shape). Rules to follow:

- Use it on white or light backgrounds only. On the dark title slide the layout already carries a white version of the logo; if another white file is needed, it is in the same KTH templates folder (check the name there).
- Keep the proportions, no stretching, no recolouring, no effects, and leave free space around it.
- In the decks, the logo comes from the template. This file is for the handouts, the shared asks document, the front page of the guides when exported, and e-mails.
- The resolution is enough for print at a small size and for A4 handouts.

## Ideas and Alternatives

### Option A: One topic-by-topic deck per WP (current guide proposal)

Each deck follows the structure of the work package: scope, partners, timeline, each task in turn, governance, risks, open questions.

**Advantages**:

- Easy to prepare, because it follows the proposal and the guides.
- Complete reference: anyone can look up a task afterwards.
- Neutral tone, nothing for the partners to object to.

**Disadvantages**:

- Repeats what the proposal already says.
- Little structure for discussion; decisions get lost between the slides.
- Task-by-task walk-through takes most of the slot and leaves 5 minutes for questions.
- Task descriptions are dense text and tables, which do not fit the 20 pt layout of the template; the slides would be crowded or full of small print.
- Treats WP3 and WP6 the same way, although they need different outcomes from the room.

### Option B: Decision-driven deck, with the content in an appendix

The main part is short (about 10 slides) and built around what the partners must decide or provide. Each section ends with an explicit "we need from you" slide. Detailed task descriptions, KPI tables and risk tables sit in an appendix that is not presented.

**Advantages**:

- Uses the time for alignment and decisions.
- Short slides with few words fit the KTH layouts naturally.
- Makes the asks visible; easier to follow up with a list of actions.
- The appendix keeps the complete reference without taking presentation time.

**Disadvantages**:

- Requires some preparation of the asks and of the discussion, since the slides are not self-explanatory.
- Partners who want the full detail must read the appendix or the guides.
- Risk of pushing for decisions the partners are not ready to make on the first day.

### Option C: Storyline deck built around the use cases and a scenario

Both decks follow one example story, for instance a community manager planning a PV and storage investment (ECP) or an operator facing a load peak (EDCR), and show where WP3 and WP6 touch it: requirements first, then architecture, then evidence.

**Advantages**:

- Concrete and engaging, helps non-experts and SMEs see the point.
- Shows the link between WP3 and WP6 naturally.
- Works well with the photo layouts of the template.

**Disadvantages**:

- Takes time to design and risks being seen as too informal.
- Does not cover governance, risks and dates by itself, so it still needs Option A or B content.
- Harder to reuse as a general reference.

### Option D: One combined deck for both work packages

A single presentation of the KTH-led work, with WP3 now and WP6 as a look ahead.

**Advantages**:

- Short, shows the relation between the two WPs directly.
- Saves partners' time.

**Disadvantages**:

- Two separate decks were asked for, and each is discussed in its own agenda slot, likely with different time.
- The detail needed for WP3 would crowd out WP6.

## Technical Considerations

### Recommended shape: Option B, with a small piece of Option C

Build each deck in three layers:

1. **Core (presented):** about 10 slides, decision-driven, with a clear storyline.
2. **Backup (available for questions):** the task detail, the KPI tables, the risk tables, the pilot fact sheets. Same template, titles start with "Backup:".
3. **Reference:** the guides GDE-0003 and GDE-0004 and the proposal.

Use one short scenario (one line on the title slide, not a story) to open each deck so that the audience has a picture. The template is the same for both decks, so they look like one WP leader's work.

### Common building blocks for both decks

| Block | Purpose | Template layout |
| ----- | ------- | --------------- |
| Title slide with the WP in one sentence | Frame the purpose | 1 (dark title) |
| "Where this fits" slide | Show inputs and outputs to the other WPs | 2, with a diagram of native shapes |
| Timeline slide | Dates, gates, workshops | 2, with a diagram |
| Roles slide | Who does what | 2, with a small table or bars |
| "What we need from you" slide | Collect commitments | 2, with a table of at most 5 rows |
| Discussion slide | Make questions concrete | 1 (dark) as a visual break, with 3 to 4 questions in white text |
| Closing slide | Next steps | 2, first three dates and actions |

### Core structure of the two decks

The decks are built in `site/slides/wp3-kickoff.qmd` and `site/slides/wp6-kickoff.qmd`. The slide tables with timing are in [GDE-0003](../guides/GDE-0003-wp3-requirements-and-architecture-design.md) and [GDE-0004](../guides/GDE-0004-wp6-use-case-validation-and-performance-assessment.md). Titles respect the limit of about 40 characters; the message is the first line on the slide or in the speaker notes.

**WP3, day 1, 16:45 to 17:30 (45 minutes)**

| # | Slide | Role in the session | Time |
| - | ----- | ------------------- | ---- |
| 1 | WP3: Requirements and Architecture | Title and one-line scenario | 1 min |
| 2 to 4 | Why WP3 comes first, three tasks, timeline | Frame: what is frozen at M09 and why | 6 min |
| 5 to 6 | T3.1 how we work, use cases and blueprints | Method, building on the overview | 5 min |
| 7 to 8 | T3.2 from targets to baselines, T3.3 architecture | The two other tasks | 6 min |
| 9 | What WP4 to WP6 get, and when | Prepares day 2 (WP4, WP5, alignment) | 3 min |
| 10 | How we decide | Only the WP3 rules | 2 min |
| 11 | What we need from you | Asks as action items | 3 min |
| 12 | Discussion | Four questions, then the parking lot | 15 min |

**WP6, day 2, 10:45 to 11:25 (40 minutes)**

| # | Slide | Role in the session | Time |
| - | ----- | ------------------- | ---- |
| 1 | WP6: Use Case Validation | Title and goal. Open with the day 1 outcomes | 1 min |
| 2 to 3 | What we must prove, what TRL 5 means here | Evidence and scope | 4 min |
| 4 to 5 | Four pilots, timeline and the tight window | Where and when, matching the WP5 dates | 6 min |
| 6 to 7 | How each use case is evaluated, from KPI to evidence | Method | 5 min |
| 8 | Ready before M30 | Early preparation | 2 min |
| 9 | What WP6 needs from other WPs | Input to the 11:25 alignment | 2 min |
| 10 | What we need from you now | Asks as action items | 2 min |
| 11 | Discussion | Four questions, then the alignment session | 10 min |

Both decks keep backup slides (effort, detailed tables, risks) for questions and are not presented.

### Storyline across the two decks

The two decks should tell one story: WP3 defines what is built and how it is measured, WP6 shows that it works. Concretely:

- WP3 slide 7 (targets and baselines) and WP6 slide 2 (evidence) use the same four objectives in the same order. AIT shows the KPIs on day 1; WP3 adds the baseline, WP6 adds the evidence.
- WP3 slide 4 and WP6 slide 5 use the same timeline graphic, with the WP highlighted.
- The use cases keep the same label and symbol in both decks, with colours taken from the KTH palette.
- WP6 slide 8 (ready before M30) points back to the WP3 asks, so partners see that early work (data inventory, baselines) pays off later.

### Design and delivery

- One idea per slide, at most about 40 words. Tables in the core have at most five rows.
- Colours: navy for titles and main shapes, the blue accent for highlights and for what the partners must act on. Do not add colours outside the KTH graphic profile.
- Redraw tables and figures from the proposal natively, in the template colours, instead of using screenshots.
- Photos: layouts 3 and 4 want photos. Candidates are the Hammarby Sjöstad area (check rights with EIN and KTH), the pilot sites, or the KTH image bank. Portrait crops are needed for layout 4 (about 190 × 350 pt). If no suitable photo exists, use layout 2 and leave the photo layouts out.
- Prepare speaker notes per slide with the key sentence, the number to remember and the likely question.
- Prepare a one-page handout per WP with dates, deliverables, contacts and the asks. It can carry the navy KTH logo from `resources/kth_logo.png`.
- Put the "asks" as a live table in a shared document during the meeting and record the answers during the discussion.
- Test the decks for online participants: font sizes as in the template, no animation that carries information, diagrams readable at small size, slide numbers on.
- Export a PDF of each deck after the meeting for the partners, and keep the `.pptx` as the master.

### Preparation work needed before the kickoff

| Item | For | Source |
| ---- | --- | ------ |
| Open the real KTH `.pptx` template, check fonts, placeholders, slide numbering and the availability of a white logo | Both decks | KTH templates folder |
| Dependency diagram (WP3 to WP4, WP5, WP6), as native shapes | Both decks | GDE-0003, GDE-0004 |
| Timeline graphic M1 to M36 with gates and workshops | Both decks | Milestones table in GDE-0002 |
| Objective to KPI table, simplified to 4 rows | Both decks | GDE-0003 |
| Photos for layouts 3 and 4, with clear usage rights | Both decks | KTH image bank, EIN, partners |
| Blank templates: blueprint, data inventory sheet, KPI definition sheet | WP3 | To be created |
| Pilot fact sheet template | WP6 | To be created |
| List of the asks with owner and due date | Both decks | Open questions in GDE-0003 and GDE-0004 |
| Draft contacts list per partner and task | WP3 | Ask the coordinator for the project contact list |
| Rehearsal with one or two partners (for example the coordinator and EIN) | Both decks | Colleagues |

## Open Questions

Answered by the agenda:

- [x] Time per WP: 45 minutes for WP3 (day 1, 16:45) and 40 minutes for WP6 (day 2, 10:45), each in the plenary and followed by shared discussion slots.
- [x] Format: on site at AIT in Vienna, with hybrid logistics.
- [x] Whether the requirements register needs a tool: the shared workspace is presented under WP1 at 14:40.
- [x] Whether WP3 collects MSAB candidates: the nominations are collected at 16:00.

Still open:

- [ ] Does the 16:00 session (website, logo, templates) produce a common project template or logo? If so, the KTH template may not be allowed for the whole meeting, and the structure moves to that template with the same limits (short titles, few words).
- [ ] If the KTH template is used, does a Plenergy.AI project logo exist, and where does it go (title slide only)?
- [ ] Does the real `.pptx` template allow slide numbers, and which font does it use? (The decks are built in Quarto and mimic the template.)
- [ ] Is there a white KTH logo file for dark backgrounds in the KTH templates folder? (The file in `resources/` is the navy one; the decks invert it with CSS.)
- [ ] Which photos can be used, and who owns the rights (KTH image bank, EIN, pilot hosts)?
- [ ] What happens in the 17:30 parking lot: who records the WP3 items, and who follows them up?
- [ ] Which dates will WP4 and WP5 present for alpha and beta? The WP6 timeline must match them.
- [ ] Do task leads (AIT for T3.3, UNICA for T6.1, AIT for T6.3) present their own slide? Their slides must be set in the same template.
- [ ] Will the slides be shared before the meeting, so partners can prepare, or after?
- [ ] Are there partner-specific points to cover (for example the Swedish national funding conditions) that are not appropriate for the plenary?
- [ ] Who reviews the decks before the kickoff, to catch gaps and tone?

## Preliminary Conclusions

- Option B (decision-driven core with an appendix) fits the purpose best. It uses the time with all partners present for alignment and commitments, and it also fits the KTH template, which is made for short titles and about six bullets per slide.
- The WP3 deck should be built to produce commitments (contacts, data inventory, workshop dates). The WP6 deck should be built to create a shared picture and to start a short list of early preparation items.
- Core decks of 12 slides (WP3, 45 minutes) and 11 slides (WP6, 40 minutes), plus backup, fit the slots from the agenda with 5 to 8 minutes of buffer.
- The agenda removes content that others present: pillars, use cases, KPIs, milestones, roles and governance. The WP decks reuse them and add only what is new.
- Each deck ends with a hand-over table that feeds the cross-WP alignment on day 2 (11:25), and with asks written as action items for the 11:45 wrap-up.
- The template changes the slide wording: titles must stay within one line of 36 pt (about 40 characters), so the "message" goes in the body or the notes. Dense tables move to the backup and the handout.
- The two decks share the KTH template, one timeline graphic and one KPI table, so that they tell a single story. The logo comes from the template and is not placed by hand; the PNG in `resources/` serves handouts and documents.
- Layout 4 (four photos) suits the "four pilots" slide of WP6, if suitable portrait photos with clear rights exist. Otherwise layout 2 is used.
- The French pilot setup and the Austrian setup are the main uncertainties in WP6. It is better to name them openly as questions at the kickoff than to present a fuller picture than the proposal supports.

These conclusions are exploratory and depend on what the 16:00 session decides about the project template and on the dates WP4 and WP5 present. The template measurements come from a PDF preview and must be checked in the `.pptx`.

## Next Steps

1. Done: the agenda is known and the decks reflect the slots and the sessions around them.
2. Before day 1: check at the 16:00 session whether a project template or logo is set, and adapt the title slide if needed.
3. Open the KTH `.pptx` template and settle the template questions above (fonts, slide numbers, white logo), or keep the Quarto decks if the look is acceptable.
4. Send a question to TRI, IMT and AIT about the French and Austrian pilots before day 2, so that the WP6 slide can show their answers.
5. After WP4 and WP5 on day 2, check the alpha and beta dates on the WP6 timeline and update the slide if they changed.
6. Prepare the handouts and the template files (blueprint, data inventory, KPI definition sheet, pilot fact sheet), and collect photos with clear rights.
7. Rehearse both decks against the time budgets with one or two colleagues.
8. Keep GDE-0003, GDE-0004 and the decks in step: the slide tables in the guides follow the decks.
