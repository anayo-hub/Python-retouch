# Product Requirements Document
## [Working Name: "Briefly"] — Opportunity Intelligence for Nigerian Law Firms
**Version 1.0 | Prepared July 2026 | Status: Ready for Build**

---

## 1. Executive Summary

Nigerian corporate law firms win new mandates almost entirely through partner relationships and word of mouth. There is no systematic way for a firm to know, in real time, that a client or prospect just raised a funding round, got a CBN query, was named in a new suit, expanded into a new state, or had a regulator issue guidance that affects their sector — until a competitor firm calls the client first.

**Briefly** is a business-development intelligence platform that continuously reads Nigeria's public record — CAC filings, court dockets, SEC/CBN/NCC/NUPRC circulars, press, and company news — and turns it into partner-ready briefings: *what happened, why it matters to this firm's practice, and who should make the call.*

This is the Nigerian, sector-adapted version of the "opportunity intelligence for law firms" category (the reference model is Osmaura, a YC S26 company doing this for U.S./corporate firms). The Nigerian market has three things going for it that make this a stronger, faster build than the U.S. equivalent:

1. **A live regulatory tailwind** — the Nigerian judiciary is mid-rollout of the Nigeria Case Management System (NCMS): the Supreme Court and Federal High Court (Lagos) went digital in 2026, with e-filing and structured case records becoming mandatory. This is the first year structured, scrapable litigation data exists at scale in Nigeria.
2. **A thin competitive field** — existing Nigerian legal-tech players (LawPavilion, Modulaw AI, Case Radar, NextCounsel, JUDY) all serve *research* and *case management* inside firms. None serve *business development* — finding the next client before a competitor does. This is a clear, undefended niche.
3. **A CAC that is already API-reachable** — third parties (e.g., Mono) already offer CAC company-lookup APIs (registration, directors, shareholders, PSC, secretary), which removes a large chunk of the data-engineering risk of getting started.

**The ask:** build a lean, high-signal MVP in 12 weeks, pilot with 5–8 Lagos/Abuja commercial firms, and charge a monthly seat/firm license from day one.

---

## 2. Problem Statement

- Nigerian law firm business development is reactive: partners rely on their personal network, industry dinners, and inbound referrals to learn a client needs help.
- Junior associates or BD staff who *do* try to monitor the market do it manually — reading Nairametrics, TechCabal, BusinessDay, CAC gazette notices, court cause lists — and it doesn't scale past a handful of watched companies.
- By the time a public signal (a lawsuit, a funding round, a regulatory query) is visible enough for a firm to notice, it's often already visible to every competing firm too — there is no first-mover advantage without a monitoring system.
- Nigeria's public record is fragmented across CAC, individual court registries (now digitizing), sector regulators (CBN, SEC, NCC, NUPRC, NAICOM), and a very active business press — no single human can track all of it across even one practice group, let alone across a full-service firm's client base.

## 3. Why Now (Nigeria-specific timing)

- **NCMS rollout (2026):** the Supreme Court and the Federal High Court (Lagos Division) have moved to mandatory e-filing in 2026, with the rest of the superior courts being onboarded in phases under the Judicial Information Technology Policy Committee (JITPOCOM). This is the first moment structured Nigerian litigation data becomes systematically capturable rather than something you can only get by sending a clerk to a registry.
- **CAC digitization:** CAC's public search and the emerging third-party lookup APIs mean company registration, director, shareholder, and PSC data is queryable programmatically rather than by manual search.
- **A maturing regulatory cadence:** CBN, SEC Nigeria, NCC, and NUPRC each publish circulars, guidance, and enforcement actions on a predictable schedule, and these routinely create sudden compliance workloads for whole sectors at once (a strong, well-understood signal type).
- **No incumbent owns this niche yet** — the existing Nigerian legal-tech vendors are all "inside the firm" tools (research, drafting, case management, billing); none are "outside the firm, market-facing" tools. Being first here compounds, because the value of the underlying signal graph (which companies, which practices, which relationships) increases with time and data.

## 4. Goals & Success Metrics

| Goal | Metric | 6-month target |
|---|---|---|
| Prove partners will act on briefings | % of briefings marked "acted on" (partner logged an outreach) | ≥15% |
| Prove retention | Paying firm logo retention | ≥85% |
| Prove signal quality | Partner-rated relevance ("useful" vs "noise") on delivered briefings | ≥60% "useful" |
| Prove monetizable value | Paid pilots converted to annual contracts | ≥5 of first 8 pilots |
| Prove one attributable win | A new mandate a firm partner confirms originated from a Briefly briefing | ≥1 in pilot cohort |

## 5. Target Users & Buyer

- **Primary user:** Business-development / marketing lead at a mid-to-large Nigerian commercial law firm (10–150 lawyers) — curates and routes briefings to partners.
- **Primary beneficiary / real user:** Equity partners in Corporate/Commercial, Capital Markets, Employment & Immigration, Dispute Resolution, and TMT practice groups — they receive the final, partner-ready brief and decide whether to reach out.
- **Buyer / economic decision-maker:** Managing partner or Head of BD — signs off on the firm-wide license.
- **Not the target (v1):** solo practitioners, in-house counsel, individual consumers seeking legal help (that's the Lawpadi/PocketLawyers space — adjacent, not this product).

### Representative personas
1. **"Adaeze," Head of BD at a 60-lawyer Lagos full-service firm.** Manages a CRM of 400 corporate relationships by spreadsheet. Needs to know, every morning, which 3–5 of those relationships had something happen worth a partner call.
2. **"Chidi," Capital Markets partner.** Doesn't want a dashboard — wants a two-paragraph WhatsApp/email brief that tells him a client he already knows is doing something new, with enough context to open a conversation credibly.
3. **"Fatima," Dispute Resolution partner at a litigation-heavy firm.** Wants to see new filings and docket movement involving her firm's existing clients or known adversaries, now that court filings are digitized.

## 6. Product Scope — MVP (v1)

### 6.1 Signal sources (Nigeria-mapped)
| Signal type | Nigerian source(s) | Notes on access |
|---|---|---|
| Company registration & structure | CAC public search; CAC lookup APIs (via aggregators such as Mono) for registration status, directors, shareholders, PSC | Available now; strongest, cleanest data source to start with |
| Litigation activity | NCMS-connected court registries (Supreme Court, Federal High Court Lagos live in 2026; other divisions phasing in) | Live and expanding through 2026–2027 — build the ingestion pipeline now, coverage grows as courts onboard |
| Regulatory/compliance signals | CBN circulars, SEC Nigeria disclosures/enforcement notices, NCC directives, NUPRC/NMDPRA notices, NAICOM circulars, FIRS/tax notices | Publicly published; scrape + monitor for practice-relevant keywords |
| Market movement | Press (BusinessDay, TechCabal, Nairametrics, Proshare, The Cable), funding announcement trackers, hiring signals (LinkedIn public postings, job boards) | Press aggregation + NLP filtering |
| Company milestones | CAC filings (name/address/director changes, new incorporations), press releases, LinkedIn leadership changes | Combine CAC change-events with press |

### 6.2 Core pipeline (mirrors the reference model's 3-stage design, localized)
1. **Monitor** — continuously ingest the sources above; normalize into a single event stream keyed to Nigerian company identity (CAC RC number as canonical ID).
2. **Match** — connect each event to (a) the firm's actual client/prospect relationship graph, and (b) practice-group relevance rules (e.g., "CBN forex circular" → Banking & Finance + Capital Markets; "new FHC filing naming a listed company" → Dispute Resolution + Capital Markets).
3. **Brief** — generate a short, partner-legible brief: what happened, why it may create legal need, which practice fits, suggested opening line for outreach. Delivered by email/WhatsApp digest, not a login-required dashboard, for v1 (Nigerian partners are far more likely to read a WhatsApp/email digest than log into a portal).

### 6.3 v1 Feature list
- Firm onboarding: import client/prospect list (CSV or CRM export) and map to CAC RC numbers (assisted matching, human-in-the-loop for ambiguous matches).
- Practice-area configuration: firm selects which practice groups and signal types matter to them.
- Daily/weekly digest: ranked list of briefs per partner or practice group, delivered by email and WhatsApp.
- Lightweight web view: for partners who want to browse past briefs, see the underlying source document, and mark "useful / not useful" (feeds the ranking model).
- BD dashboard: firm-wide view of all briefs generated, action taken, and outcomes logged (did a partner reach out? did it become a matter?) — this closes the loop and is the core ROI-proof artifact for renewal conversations.
- Feedback loop: partner "useful/not useful" ratings retrain relevance ranking per firm.

### 6.4 Explicitly out of scope for v1
- Contract drafting, legal research, case management, billing (this is not a "practice tool" — leave that to LawPavilion/Modulaw AI/Case Radar).
- Consumer-facing legal help.
- Full-text legal research / case law database.
- States/courts not yet on NCMS — build the ingestion architecture to plug in as coverage expands, but don't promise national litigation coverage on day one; be explicit with pilot firms about current coverage.

## 7. Competitive Landscape (Nigeria)

| Player | What they do | Overlap with Briefly |
|---|---|---|
| LawPavilion | Case law research + case management SaaS | None — inside-firm tool |
| Modulaw AI | AI research, case management, client collaboration, billing (all-in-one) | None — inside-firm tool, though a natural future integration partner |
| Case Radar, NextCounsel | Research / case management point tools | None |
| JUDY | AI case-law database | None |
| Lawpadi, PocketLawyers, Legalstack-type players | Consumer/SME legal access | Different buyer (SME/consumer vs. commercial firm) |
| Osmaura (US, YC S26) | Direct reference model — opportunity intelligence for corporate firms | Same category, different geography/data sources; no Nigerian presence |

**Positioning:** "Business development intelligence" is an open lane in Nigeria. The risk isn't a legal-tech incumbent copying this — it's a firm's own BD team building a worse version in a spreadsheet, or a global player (Osmaura or a clone) entering Nigeria later. Speed and data-source lock-in (deep CAC/NCMS integration, a growing firm-specific relationship graph) are the moat.

## 8. Business Model

- **Pricing:** annual firm license, tiered by lawyer headcount (e.g., ₦-denominated tiers for 10–30, 31–75, 76–150+ lawyers), not per-seat — mirrors how Nigerian firms already buy LawPavilion/Modulaw-style tools, and avoids friction of metering individual partner usage.
- **Pilot motion:** 90-day paid pilot (discounted, not free — a free pilot signals low confidence and attracts non-committed firms) with 3–5 practice groups onboarded, success criteria agreed upfront (a defined number of "acted on" briefs and at least one attributable outreach).
- **Expansion revenue:** additional practice groups, additional offices (Lagos/Abuja/Port Harcourt), and later an added module for in-house counsel teams at the firm's own major clients (adjacent market, later phase).

## 9. Go-to-Market

- **Beachhead segment:** mid-size full-service commercial firms in Lagos (10–150 lawyers) with active Corporate/Commercial, Capital Markets, and Dispute Resolution practices — big enough to have a real BD function, small enough to decide fast (Tier-1 "magic circle style" Nigerian firms will be slower sales cycles; approach them in phase 2 once there are reference logos).
- **Wedge signal type:** lead with CAC + regulatory-circular monitoring (highest-confidence, cleanest data) rather than litigation coverage, since NCMS coverage is still expanding through 2026–2027 — be upfront that litigation coverage grows over time rather than overselling day-one court coverage.
- **Channel:** direct outreach to Heads of BD/Marketing at target firms (a small, known community in Lagos legal circles), warm intros through NBA Section on Business Law and legal-tech events, and a visible pilot with one recognizable firm as a reference case.
- **Proof asset:** the BD dashboard's "outcome log" (Section 6.3) — the single most important sales artifact once the first pilot firm has 60–90 days of data, since it turns the pitch from "trust us" into "here's what firm X saw."

## 10. Data, Privacy & Legal Considerations (do this properly, don't skip it)

- All source data must be from the **public record** (CAC public search, published court records/cause lists, published regulator notices, public press) — no scraping of paywalled or access-controlled registries.
- Build for compliance with the **Nigeria Data Protection Act (NDPA) 2023** and NDPR from day one: register with the Nigeria Data Protection Commission (NDPC) as applicable, maintain a data-processing register, and be able to explain the lawful basis for processing company/director personal data (legitimate interest, given the data is already public record, is the likely basis — get this confirmed by counsel before launch, not after).
- Company entity resolution should be anchored to **CAC RC number** as the canonical ID to avoid name-collision errors — Nigerian companies frequently share very similar names.
- Terms of service with pilot firms should be explicit that Briefly surfaces publicly available information and does not constitute legal advice, and that firms remain responsible for their own outreach and conflict checks.
- Build an internal conflict-of-interest safeguard early: since the same signal graph could tempt Briefly to sell to two competing firms in the same city, define (and eventually disclose) an exclusivity or non-compete policy per practice-area/city to protect firm trust — this becomes a major differentiator and sales point once you have more than one Lagos client.

## 11. Technical Approach (high level)

- **Ingestion layer:** scheduled scrapers/API pulls for CAC (via lookup API), regulator circular pages (CBN, SEC, NCC, NUPRC, NAICOM), court registries as NCMS access becomes available, and press/news APIs — normalized into a unified event schema.
- **Entity resolution:** CAC RC number as canonical company key; fuzzy-matching layer to reconcile press mentions and firm-provided client lists against RC numbers.
- **Relevance/ranking model:** start with a practice-area rules engine (keyword + entity-type mapping) for v1 explainability; layer in an LLM-based summarizer/briefing generator on top of matched events (this is where an LLM API is genuinely additive — turning a raw filing or circular into a two-paragraph, partner-legible brief with a suggested opening line).
- **Delivery:** email + WhatsApp Business API digest (native to how Nigerian professionals communicate) plus a lightweight web view; avoid requiring a habitual dashboard login for v1 adoption.
- **Feedback loop:** partner-level "useful/not useful" tagging feeds back into per-firm ranking weights.

## 12. Roadmap

| Phase | Timeframe | Focus |
|---|---|---|
| 0 — Discovery | Weeks 1–3 | Confirm signal-source access (CAC API terms, regulator scraping feasibility, NCMS access status); interview 10–15 BD leads/partners at target firms; finalize pilot firm list |
| 1 — MVP build | Weeks 4–12 | CAC + regulatory-circular ingestion, entity resolution, rules-based matching, LLM-assisted brief generation, email/WhatsApp delivery, basic web view |
| 2 — Paid pilot | Weeks 13–24 | 5–8 firm pilots, weekly feedback loop, outcome logging, iterate on relevance ranking |
| 3 — Litigation coverage expansion | Month 6–12 | Add NCMS-connected court data as coverage expands beyond Supreme Court/FHC Lagos; add more regulators; expand practice-area rule sets |
| 4 — Scale | Month 12+ | Move upmarket to larger firms, add Abuja/Port Harcourt firms, explore in-house counsel adjacent product, explore other African markets (Kenya, Ghana, South Africa) using the same playbook |

## 13. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Litigation data coverage is still rolling out (NCMS not yet national) | Lead GTM with CAC + regulatory signals, which are already strong; be transparent with pilots about current litigation coverage and price/roadmap accordingly |
| Partners don't act on digital BD tools (relationship-driven culture, low tech adoption habit) | Deliver via WhatsApp/email, not a portal; keep briefs to 2 paragraphs; make the "suggested opening line" do the cognitive work for the partner |
| Data privacy/compliance risk in scraping regulator and court sources | Public-record-only sourcing, NDPA/NDPC compliance built in from day one, legal review before launch |
| A firm's own BD team sees this as a threat to their job rather than a tool | Position and sell to Heads of BD as a force-multiplier for their own function, not a replacement — they become the internal champion, not the target of automation |
| Global competitor (e.g. Osmaura or similar) enters Nigeria later | Move fast on Nigerian data-source integration depth and firm relationship-graph accumulation — that compounding advantage is the moat, not the interface |
| Conflict-of-interest concerns (same signal serving two competing firms) | Define and communicate a per-practice/per-city exclusivity policy early, before it becomes a trust issue |

## 14. Open Questions for Founder Decision

- Confirm final legal basis for processing CAC director/shareholder data under NDPA before ingesting at scale — get NDPC-aware counsel to sign off.
- Decide initial city focus: Lagos-only pilot, or Lagos + Abuja from day one (Abuja has more regulatory/government-facing firms; Lagos has more capital markets/commercial firms).
- Decide whether WhatsApp Business API delivery is built in-house or via a provider (e.g., a WhatsApp BSP) — affects timeline and cost.
- Decide pricing tiers precisely once pilot conversations validate willingness to pay (don't set final pricing before at least 5–6 discovery calls with target BD leads).

---
*Prepared as a build-ready PRD. Next step: Phase 0 discovery calls and confirmation of CAC/regulator data-access terms before committing engineering resources to Phase 1.*
