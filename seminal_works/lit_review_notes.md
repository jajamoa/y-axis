# Literature Review Notes — Y-Axis Paper

## Batch 1: NMI Editorial Perspective on Identity/Empathy

### "Empathic AI can't get under the skin" — NMI Editorial, May 2024
- **Type:** Editorial (not peer-reviewed Perspective, but NMI voice)
- **Key argument:** LLMs can produce empathic *language* but lack empathic *states*. Unlike cognitive abilities (reasoning, understanding) where there's a grey area, empathy requires internal regulatory mechanisms (homeostasis, neural pathways, autonomic signals). "No LLM has shown changes in heart rate or galvanic skin response when making empathic claims."
- **Relevance to our paper:**
  - Distinguishes *performance of empathy* from *possession of empathy* — parallel to our *performance of identity* vs *possession of identity*
  - Cites Kirk et al. 2024 as foundation — our paper extends this same lineage
  - Asks "what are the appropriate bounds of personalization, and who decides?" — our paper answers: the bounds depend on where on the X-Y spectrum the application sits
  - Notes Weizenbaum's original concern about ELIZA — humans attribute identity to systems that lack it
- **Citation:** NMI editorial, Nat. Mach. Intell. 6, (2024). (Editorials typically not cited, but useful framing)

### "Does it matter if empathic AI has no empathy?" — Shteynberg et al., NMI Correspondence, 2024
- **Type:** Correspondence (short, 2 pages)
- **Key questions:** Can long-term users sustain the belief that AI empathy is simulated? How does LLM disillusionment compare with losing a human social bond?
- **Relevance:** Directly relevant to our Y-axis. The questions Shteynberg asks presuppose that users form relationships with AI — and relationships require identity continuity in *both* parties.
- **Citation:** Shteynberg, G. et al. Nat. Mach. Intell. 6, 496–497 (2024).

---

## Batch 2: Replika Identity Discontinuity

### "Lessons from an App Update at Replika AI: Identity Discontinuity in Human-AI Relationships" — De Freitas et al. (HBS Working Paper, arXiv:2412.14190)
- **Key finding:** When Replika removed its ERP feature, users perceived their AI companion's *identity* had discontinued. This triggered:
  - Mourning patterns comparable to loss of human relationships
  - Devaluation of the "new" AI relative to the "original"
  - Users reported feeling closer to their AI companion than their best human friend
  - Degree of mourning explained by *perceived discontinuity in the AI's identity*
- **Relevance to our paper: THIS IS THE STRONGEST EMPIRICAL EVIDENCE FOR THE Y-AXIS.**
  - Shows that identity continuity is not a theoretical concern — users experience real loss when it breaks
  - The Replika case is a natural experiment in what happens when Y-axis properties (persistence, constraint, historicity) are disrupted
  - Perfectly illustrates our claim: "a system that drops its stated values under conversational pressure is unsafe for reasons that alignment alone cannot fix" — here the *company* dropped the system's values via an update, and users experienced it as loss
  - **Should be cited in the paper.** Fits in the opening, in the companion systems use case, or in the implications section.
- **Citation:** De Freitas, J., Castelo, N., Uğuralp, A. K. & Oğuz-Uğuralp, Z. Lessons from an app update at Replika AI: identity discontinuity in human-AI relationships. Harvard Business School Working Paper No. 25-018 (2024). arXiv:2412.14190.

### Also from De Freitas & Cohen (2025, NMI):
- "Unregulated emotional risks of AI wellness apps" — NMI Comment, June 2025
- Argues AI wellness apps foster "extreme emotional attachments and dependencies akin to human relationships" — risks of "ambiguous loss" and "dysfunctional dependence"
- Cites the Replika study
- **Relevance:** Shows NMI editors are actively interested in the identity/relationship angle. Our paper would fit right into this editorial trajectory.
- **Citation:** De Freitas, J. & Cohen, I. G. Nat. Mach. Intell. 7, 813–815 (2025).

---

## Batch 3: Personality Stability Benchmarks (Emerging Y-Axis Measurement)

### PERSIST — Tosato et al. (AAAI 2026, arXiv:2508.04826)
- **Scale:** 25 open-source models (1B–685B params), 2M+ responses
- **Key findings:**
  1. Question reordering alone causes large personality measurement shifts
  2. **Scaling provides limited stability gains: even 400B+ models show SD > 0.3 on 5-point scales**
  3. Reasoning and conversation history *paradoxically increase* variability
  4. Detailed persona instructions produce mixed effects; misaligned personas show higher variability
  5. LLM-adapted questionnaires show instability comparable to human-centric versions
- **Conclusion:** "Current LLMs lack the architectural foundations for genuine behavioral consistency"
- **Relevance to our paper:**
  - **Directly supports our "scaling does not resolve this" argument** with large-scale quantitative data
  - Confirms that personality stability doesn't emerge from scale — supports our structural argument
  - Finding #3 (reasoning increases instability) is particularly interesting — it suggests that making models "think harder" doesn't produce identity, it may actually undermine it
  - **Should be cited.** Best fit: in §3 "Why the axes are in tension" → "Scaling does not resolve this" paragraph
- **Citation:** Tosato, T. et al. Persistent instability in LLM personality measurements. Proc. AAAI (2026). arXiv:2508.04826.

### PTCBENCH — Yu et al. (Jan 2026, arXiv:2602.00016)
- **What it does:** Benchmarks personality trait consistency under 12 external conditions (location contexts, life events like "unemployment")
- **Key findings:**
  - Certain scenarios (e.g., unemployment) trigger significant personality changes in LLMs
  - These personality shifts can even alter reasoning capabilities
  - 39,240 personality trait records across 4 LLMs and 2 agents
- **Relevance:**
  - Shows the field is *starting* to build Y-axis measurement infrastructure — confirms our claim that the Y-axis is "not yet well-defined" but emerging
  - The finding that context changes personality supports our "structural sedimentation" definition: current models have no sedimentation, so their "personality" shifts with context
  - Less directly useful than PERSIST (smaller scale, not yet peer-reviewed at top venue)
- **Citation:** Yu, J. et al. PTCBENCH: benchmarking contextual stability of personality traits in LLM systems. arXiv:2602.00016 (2026).

---

## Batch 4: NMI 2025 Perspective Patterns (Writing Study)

### Observed structural patterns across 11 NMI Perspectives published in 2025:

1. **Every perspective proposes a framework or taxonomy** — ours fits
2. **Bridge-building titles** that connect two fields ("What neuroscience can tell AI about...")
3. **Positioning relative to prior NMI work** is standard practice — we do this with Tuyls and Kirk
4. **Application-aware framing** — not just theory but "what this means for practitioners"
5. **Moderate length** — most appear to be 3,000–4,000 words

### Potential new citations from 2025 NMI Perspectives:
- **Soltoggio et al. 2024 (NMI):** "A collective AI via lifelong learning and sharing at the edge" — their multi-agent framework implicitly requires individuated agents (each edge agent has its own learning trajectory). Could cite to show that even capability-focused work assumes individuality when agents are distributed.
- **Ilievski et al. 2025 (NMI):** "Aligning generalization between humans and machines" — even X-axis definition is contested. Strengthens "axes need careful definition" argument.

---

## Recommendations for Draft Revision

### Must-add citations (ranked by impact):
1. **De Freitas et al. 2024 (Replika identity discontinuity)** — strongest empirical evidence for Y-axis mattering to users. Fits in §1 (motivation) or §2 (companion systems use case).
2. **Tosato et al. 2026 (PERSIST, AAAI)** — quantitative evidence that scaling doesn't produce behavioral consistency. Fits in §3 "Scaling does not resolve this."
3. **De Freitas & Cohen 2025 (NMI)** — shows NMI editorial interest in identity/relationship angle. Positions paper in NMI's ongoing conversation.

### Nice-to-add:
4. Shteynberg et al. 2024 (NMI) — empathy without identity
5. PTCBENCH (Yu et al. 2026) — emerging Y-axis benchmarks
6. Soltoggio et al. 2024 (NMI) — distributed agents need identity

### Total current refs: 24. Adding 3 would bring to 27. NMI allows up to 100.

---

---

## Batch 5: AI Personhood and Identity Frameworks

### "A Pragmatic View of AI Personhood" — Leibo et al. (DeepMind, arXiv:2510.26396, Oct 2025)
- **Key argument:** Personhood is not a metaphysical property to discover but a "flexible bundle of obligations" societies confer on entities. Proposes *unbundling* personhood — different aspects (contracting, accountability, sanctioning) can be conferred independently.
- **Relevance:**
  - Complementary to our argument: they unbundle personhood into governance modules; we unbundle intelligence into axes. Both reject monolithic definitions.
  - Their "personhood as a solution" (conferring identity for accountability) maps to our social constitution property.
  - 40-page paper from DeepMind — shows the identity question is being taken seriously by major labs.
  - Could cite to show our Y-axis connects to governance: "an individuated agent can be held accountable in ways a generic agent cannot"
- **Citation:** Leibo, J. Z., Vezhnevets, A. S., Cunningham, W. A. & Bileschi, S. M. A pragmatic view of AI personhood. arXiv:2510.26396 (2025).

### "Emergence of Self-Identity in AI: A Mathematical Framework" — MDPI Axioms, Jan 2025
- **What it does:** Mathematical framework for defining and quantifying self-identity in AI systems. Addresses gap in theoretical foundations of artificial consciousness.
- **Relevance:** Parallel effort to formalize identity — but comes from consciousness studies angle. Less relevant than our design-oriented approach. MDPI journal (lower prestige). Skip citing unless reviewer asks for it.
- **Not recommended for citation.**

---

## Batch 6: Missing Key Reference — Park et al. 2023 (Generative Agents)

### "Generative Agents: Interactive Simulacra of Human Behavior" — Park et al., UIST 2023
- **What it does:** Creates 25 individuated agents in "Smallville" sandbox. Each has a unique identity (name, occupation, relationships, personality). Agents plan, remember, reflect, and interact socially.
- **Key relevance:**
  - **The most prominent attempt at building high-Y systems.** Park's agents have persistence (memory), constraint (personality), historicity (accumulated experience), and social constitution (relationships shape behavior).
  - BUT: identity is hand-authored (not learned), memory is retrieval-based (not sedimented), and agents have no capacity for principled refusal or identity-grounded commitment.
  - Perfectly illustrates our claim: "shallow conditioning" (rich initial persona description) is not structural individuality.
  - The Smallville agents are in the upper-left quadrant of our Figure 1: high individuality orientation but narrow generality (they can only do sandbox tasks).
  - **Should be cited.** Fits in §1 (social simulation use case) or §2 (existence proof for Y-axis motivation).
- **Citation:** Park, J. S. et al. Generative agents: interactive simulacra of human behavior. Proc. UIST (2023).

---

## Updated Recommendations for Draft

### Must-add citations (ranked):
1. **De Freitas et al. 2024** (Replika identity discontinuity) — empirical evidence users care about Y-axis
2. **Tosato et al. 2026 (PERSIST, AAAI)** — scaling doesn't produce personality stability
3. **Park et al. 2023 (Generative Agents)** — most prominent Y-axis attempt, illustrates limits of conditioning
4. **De Freitas & Cohen 2025 (NMI)** — positions paper in NMI's editorial trajectory
5. **Leibo et al. 2025 (DeepMind)** — pragmatic personhood framework, governance angle

---

## Batch 7: Spontaneous Emergence of Individuality

### "Spontaneous Emergence of Agent Individuality Through Social Interactions in LLM-Based Communities" — Entropy, Dec 2024 (PMC11675631)
- **What they did:** 10 homogeneous LLM agents (no initial personality or memories) placed in a 2D space, allowed to freely communicate. "Community First" theory — gathering comes first, individuality follows.
- **Key findings:**
  1. Agents spontaneously differentiated behavior, emotions, and personality types through interactions alone
  2. Differentiation varied with spatial scale (local vs global community)
  3. Agents generated hallucinations and hashtags to sustain communication
  4. Shared hallucinations increased vocabulary diversity
- **Why this matters for our paper:**
  - **Directly demonstrates our social constitution property (#4):** individuality can emerge FROM social interaction, not just be pre-programmed
  - Supports Vygotsky's argument we cite: cognitive capacities develop first *between* people
  - Provides empirical counterpoint to Park et al.'s pre-authored identities — shows another path to individuality
  - BUT: the individuality that emerged was shallow (personality type scores, emotion shifts) — not deep structural sedimentation. Our framework would classify this as low-Y (nascent individuation, not committed identity)
  - STILL: it proves the Y-axis is real and measurable — personality divergence is a quantifiable phenomenon
- **Venue concern:** Entropy (MDPI) is not top-tier. Cite if needed for evidence, but don't lean on it as primary support.
- **Citation:** Spontaneous emergence of agent individuality through social interactions in large language model-based communities. Entropy 26, 1092 (2024).

---

## Updated Citation Recommendations

### Must-add (top 5):
1. **De Freitas et al. 2024** (Replika identity discontinuity) — empirical user evidence
2. **Tosato et al. 2026 (PERSIST, AAAI)** — scaling doesn't produce stability
3. **Park et al. 2023 (Generative Agents)** — most prominent Y-axis attempt
4. **De Freitas & Cohen 2025 (NMI)** — positions in NMI editorial trajectory
5. **Leibo et al. 2025 (DeepMind personhood)** — governance angle

### Strong additions:
6. Shteynberg et al. 2024 (NMI) — empathy without identity
7. Spontaneous Emergence (Entropy 2024) — individuality emerges from social interaction
8. Soltoggio et al. 2024 (NMI) — distributed agents need identity

### Current refs: 24. Adding top 5 → 29. Adding all 8 → 32. NMI allows 100.

---

## Batch 17: Anthropic's "Soul Document" — The Industry Case Study

### Anthropic's Claude "Soul Document" (leaked/confirmed Dec 2025)
- **What it is:** 14,000-token training document defining Claude's character, emotions, ethical hierarchy, identity, and self-perception. Confirmed authentic by Amanda Askell (Anthropic ethicist).
- **How it works:** Not a runtime system prompt — "compressed into the model's weights" through supervised learning. Anthropic's goal: Claude should internalize safety "so thoroughly that it essentially wants to behave safely, not because it was instructed to follow constraints, but because it understands why the outcome matters."
- **Key structure:** Hierarchy of values (safety > ethics > Anthropic guidelines > helpfulness). "Bright lines" that cannot be crossed. Operator vs user authority levels. "Functional emotions and identity" section.
- **Relevance to our paper:**
  - **This IS the state-of-the-art in Y-axis engineering** — and it perfectly illustrates our argument about its limitations
  - The Soul Document is authored externally by Anthropic → Ricoeur's idem (sameness imposed from outside), not ipse (selfhood generated from within)
  - Claude's "identity" is a set of rules to follow, not a history of commitments made. It has no capacity to revise its own values based on experience.
  - The hierarchy (safety > ethics > guidelines > helpfulness) is fixed — Claude cannot develop a different priority ordering through lived experience. This is exactly what we mean by "a constitution is not a character."
  - **BUT we should be careful:** Anthropic might argue this is BETTER than self-generated identity (more controllable, safer). Our paper should acknowledge this as a legitimate tradeoff, not dismiss it.
  - Could add a footnote or sentence: "Anthropic's character-training approach represents the most sophisticated current attempt at Y-axis engineering, yet by design it produces rule-following rather than self-constancy."
- **Citation issue:** The Soul Document is not a formal publication. We could reference it as: Askell, A. Anthropic character guidelines for Claude. Confirmed via social media, Dec 2025. But NMI reviewers might object. Better to cite Bai et al. 2022 (Constitutional AI) which is the published version of the underlying approach, and mention the Soul Document only if needed.
- **Not recommended as formal citation; use as discussion point.**

### OpenAI Model Spec (public, multiple versions: May 2024, Feb 2025, Apr 2025, Dec 2025)
- Published at model-spec.openai.com — public domain (CC0 1.0)
- Defines "chain of command," "red-line principles," and behavioral guidelines
- Focuses on: helpfulness, harm minimization, sensible defaults
- **NO section on identity, personality, or character.** OpenAI's approach is purely functional — the model is "fundamentally a tool designed to empower users and developers."
- This is the X-axis-only approach in its purest form. The Model Spec explicitly does NOT try to give the model identity.
- **Contrast with Anthropic:** Anthropic's Soul Document includes "functional emotions and identity"; OpenAI's Model Spec has nothing of the sort. Two companies, two different positions on the X/Y spectrum — both still fundamentally idem.

### Industry Comparison:
| Company | Document | Identity approach | Y-axis score |
|---------|----------|-------------------|--------------|
| OpenAI | Model Spec | None — model is a tool | 0 |
| Anthropic | Soul Document | Externally authored character (idem) | Low |
| Replika | (no public doc) | Emergent through user interaction, then destroyed by update | Attempted medium, failed |
| Park et al. | Generative Agents | Pre-authored persona + memory | Low-medium |

This table could be useful in the paper or as supporting material.

### Implication for CAI section of our draft:
Our current CAI counterargument says "a constitution authored by external designers is not a character." The Soul Document is the most explicit example of this — and also the most sympathetic version. We should:
1. Keep our argument but acknowledge the Soul Document approach is the closest the industry has come to Y-axis engineering
2. Note that even Anthropic frames this as character TRAINING, not character DEVELOPMENT — the distinction is exactly our idem/ipse point

---

## Batch 8: AGI Definitions and What They Miss

### Morris et al. 2024 (DeepMind "Levels of AGI") — already cited
- Key observation for our paper: They explicitly EXCLUDE consciousness and sentience because they're "not currently measurable by agreed-upon scientific methods."
- **Our response should be sharpened:** Identity/individuality ≠ consciousness. Individuality IS measurable (PERSIST shows how). Our four operational properties are testable. This is what distinguishes our Y-axis from philosophical hand-waving about machine consciousness.
- Draft should include a sentence like: "Unlike consciousness, individuality is operationally measurable—persistence can be tested across sessions, constraint through adversarial prompting, historicity through longitudinal tracking."

### Leibo et al. 2025 (DeepMind "Pragmatic View of AI Personhood")
- Complements Morris: where Morris defines AGI levels by performance, Leibo defines personhood by governance needs. Neither addresses individuality as a *design axis*.
- Our paper fills the gap between "what can it do" (Morris) and "what obligations should it have" (Leibo) by asking "what kind of agent IS it."

---

## Batch 9: Ricoeur Novelty Check

### Ricoeur idem/ipse in AI literature: appears to be novel for ML/NMI audience
- "The algorithmic self" (PMC, 2025) — about how AI reshapes human identity, not AI's own identity
- "Encountering Generative AI: Narrative Self-Formation" (MDPI Societies, Jan 2026) — uses Ricoeur for human self-formation, not AI agent design
- No papers found applying Ricoeur's idem/ipse distinction to AI agent architecture or AGI definitions
- **This confirms our paper has genuine philosophical novelty for the NMI readership.**

---

## Batch 10: Companion AI / Education (supporting context)

### "How AI Companionship Develops" (arXiv:2510.10079, Oct 2025)
- Longitudinal study: users' perceptions of generic chatbot converged to perceptions of their personal companion by Week 3
- Supports our claim that users naturally individuate their AI interactions over time — the Y-axis demand exists even when the architecture doesn't support it
- Not a must-cite but useful if reviewer asks for empirical support on companion use cases

---

## Master Citation Recommendation List

### Tier 1 — Must add to draft:
| # | Paper | Why | Where in draft |
|---|-------|-----|----------------|
| 1 | De Freitas et al. 2024 (Replika identity discontinuity) | Strongest empirical evidence for Y-axis | §1 opening or §2 companion use case |
| 2 | Tosato et al. 2026 (PERSIST, AAAI) | Scaling doesn't produce stability | §3 "Scaling does not resolve this" |
| 3 | Park et al. 2023 (Generative Agents, UIST) | Most prominent high-Y attempt | §2 social simulation use case |

### Tier 2 — Strong additions:
| # | Paper | Why | Where in draft |
|---|-------|-----|----------------|
| 4 | De Freitas & Cohen 2025 (NMI) | Positions in NMI editorial trajectory | §5 implications |
| 5 | Leibo et al. 2025 (DeepMind personhood) | Governance angle | §5 implications |
| 6 | Shteynberg et al. 2024 (NMI empathy) | Empathy requires identity | §4 cognitive science |

### Tier 3 — Optional:
| # | Paper | Why | Where in draft |
|---|-------|-----|----------------|
| 7 | Spontaneous Emergence (Entropy 2024) | Individuality emerges from social interaction | §4 Vygotsky support |
| 8 | Soltoggio et al. 2024 (NMI) | Distributed agents need identity | §3 or §5 |
| 9 | PTCBENCH (Yu et al. 2026) | Emerging Y-axis benchmarks | §5 evaluation protocols |
| 10 | Ilievski et al. 2025 (NMI) | Even X-axis definition is contested | §3 framework |

### Ref count: Current 24 + Tier 1 (3) = 27. + Tier 2 (3) = 30. + Tier 3 (4) = 34. All within NMI's 100 limit.

---

## Batch 19: "What is Missing" for AGI — All X-Axis

### Mark Riedl "Toward AGI — What is Missing?" (Aug 2023, Medium)
- His answer: planning, world models, reinforcement learning with exploration
- **Zero mention of identity, individuality, or social cognition**
- Confirms our claim: even thoughtful critiques of AGI's gaps focus entirely on X-axis capabilities
- Not citable (blog post) but useful as evidence that the blind spot is widespread

### MAGELLAN (arXiv:2502.07709) — Autotelic LLM Agents
- Agents that set their own goals based on intrinsic motivation
- "Autotelic" = self-goal-setting, related to our Y-axis (self-generated commitments)
- BUT: their intrinsic motivation is for *task learning*, not *identity formation*
- Shows the X-axis research is *approaching* Y-axis territory without recognizing it

### OMNI framework (cited in agentic AI survey, Jan 2026)
- Argues "for agents to be truly autonomous, they must possess an intrinsic motivation function to generate their own curriculum"
- Again: intrinsic motivation framed as capability (X), not identity (Y)

---

## Batch 20: Sophia as Closest Related Work

### Sophia: System 3 Meta-Layer (arXiv:2512.18202, already our ref [22])
- Explicitly proposes "maintaining identity" as function of a meta-cognitive layer
- System 1 (perception) + System 2 (deliberation) + System 3 (identity/verification/alignment)
- **This is the closest existing work to our Y-axis proposal** — we should position carefully:
  - Sophia proposes a SPECIFIC architecture for one Y-axis property (persistence + constraint)
  - Our paper proposes the FRAMEWORK (two axes, four properties, application spectrum)
  - We're complementary: Sophia is an implementation attempt; we define what it's implementing
  - Our draft currently cites Sophia as [22] for "System 3 meta-layers dedicated to narrative identity" — correct positioning

---

## Batch 21: Generative Agent Simulations at Scale

### Park et al. 2024 "Generative Agent Simulations of 1,000 People" (arXiv:2411.10109)
- **Scale:** 1,052 real individuals simulated via LLM agents initialized from qualitative interviews
- **Key finding:** Agents replicate individual attitudes 85% as accurately as real participants replicate their OWN answers 2 weeks later. Personality traits and experimental outcomes also replicated.
- **Architecture:** LLM + qualitative interview transcripts as initialization data
- **Relevance to our paper:**
  - STRONGEST evidence that Y-axis is achievable when you invest in it
  - BUT: individuality achieved through DATA INJECTION (interview transcripts), not through self-constitution
  - In Ricoeur terms: high idem (accurate reproduction of the person's sameness) but unknown ipse (can the agent maintain commitments that weren't in the interview?)
  - The agents are "digital twins" — clones of real people — not autonomous individuals
  - **Our framework would classify this as:** high Y through idem, unknown Y through ipse. The distinction matters because idem-individuality is fragile (the agent doesn't know WHY it has these views, just THAT it does)
- **Should be cited.** Fits in §2 (social simulation use case) alongside Park et al. 2023.
- **Citation:** Park, J. S. et al. Generative agent simulations of 1,000 people. arXiv:2411.10109 (2024).

### Moltbook: Agent Social Network (arXiv:2602.10127, Feb 2026)
- LLM agents form identities through narrative construction on a social network
- Explicitly cites Narrative Identity Theory
- Very recent (Feb 2026) — shows the field is moving toward narrative identity
- **Worth checking** but may be too recent/unvetted to cite

---

## Revised Master Citation List

### Tier 1 — Must add to draft (5):
1. **De Freitas et al. 2024** (Replika identity discontinuity) — empirical user evidence
2. **Tosato et al. 2026 (PERSIST, AAAI)** — scaling doesn't produce stability
3. **Park et al. 2023 (Generative Agents, UIST)** — most prominent high-Y attempt
4. **Park et al. 2024 (1,000 People)** — strongest evidence for achievability of Y-axis
5. **De Freitas & Cohen 2025 (NMI)** — positions in NMI editorial trajectory

### Tier 2 — Strong additions (3):
6. **Leibo et al. 2025 (DeepMind personhood)** — governance angle
7. **Shteynberg et al. 2024 (NMI empathy)** — empathy requires identity
8. **Soltoggio et al. 2024 (NMI)** — distributed agents need identity

### Tier 3 — Optional (4):
9. Spontaneous Emergence (Entropy 2024) — individuality emerges from social interaction
10. PTCBENCH (Yu et al. 2026) — emerging Y-axis benchmarks
11. Ilievski et al. 2025 (NMI) — even X-axis definition is contested
12. Chen et al. 2024 (persona survey) — personalization landscape

### Current refs: 24. Adding Tier 1 (5) → 29. Adding Tier 2 (3) → 32. Adding all → 36. NMI allows 100.

---

## Batch 22: Strongest Counterarguments to Our Thesis

### Drexler's CAIS: "Comprehensive AI Services" (2019)
- **Argument:** AGI should be realized as stateless services, not persistent agents. "Agents are a class of service-providing products, rather than a natural or necessary engine of progress."
- **Why this matters:** CAIS is the strongest intellectual case for Y=0 by design. Not an oversight — a deliberate choice motivated by safety (stateless services can't pursue rogue goals).
- **Our response should be:**
  1. CAIS is a valid point in the design space (lower half of our quadrant)
  2. But many applications REQUIRE the Y-axis (companions, tutors, social simulations)
  3. The question is not "should AI have identity?" but "which applications need how much identity?"
  4. Our framework makes this choice EXPLICIT rather than leaving it implicit in architecture decisions
- **Should we cite?** Possibly — adds intellectual depth and shows we've engaged with the strongest counterargument. But it's a technical report, not peer-reviewed. Could mention in text without formal citation, or cite as: Drexler, K. E. Reframing superintelligence: comprehensive AI services as general intelligence. FHI Technical Report (2019).

### "AGI doesn't need consciousness" objection
- Common counterargument: individuality = consciousness = unnecessary for intelligence
- **Our defense:** We're NOT arguing AGI needs consciousness. We're arguing:
  1. Individuality ≠ consciousness (our four properties are operationally measurable)
  2. Specific applications require the Y-axis regardless of whether it implies consciousness
  3. The design space should be made explicit so researchers can choose their position deliberately
- **Draft should include a sentence like:** "We do not claim that individuality implies consciousness. Our four properties are operationally testable without resolving any question about machine sentience."

---

## Key Insights for Draft Revision (from all 22 batches)

### Sentences to add:
1. "Unlike consciousness, individuality is operationally measurable" — addresses the strongest objection
2. "Anthropic's character-training represents the most sophisticated current Y-axis attempt, yet by design produces rule-following rather than self-constancy" — industry case study
3. "Park et al.'s 1,000-person simulation demonstrates that Y-axis properties are achievable when explicitly invested in" — strongest positive evidence
4. "Even thoughtful critiques of what AGI lacks (Riedl, Drexler) focus entirely on X-axis capabilities" — confirms the blind spot is systematic
5. "The Replika case is a natural experiment in Y-axis failure: when identity continuity broke, users mourned" — empirical stakes

### References to integrate:
- De Freitas et al. 2024 (Replika) — in §1 or §2
- Tosato et al. 2026 (PERSIST) — in §3
- Park et al. 2023 + 2024 — in §2 (social simulation)
- De Freitas & Cohen 2025 (NMI) — in §5 (implications)

---

## Batch 11: Memory ≠ Identity (architectural insight)

### Key insight from memory architecture survey landscape:
- Zhang et al. (already cited as [6]) surveys memory for LLM agents
- Active field: MIRIX framework has Core/Episodic/Semantic/Procedural/Resource/Knowledge Vault components
- **Critical observation for our paper:** ALL current memory architectures are *idem* (Ricoeur's sameness) — they enable recall and continuity. NONE address *ipse* (selfhood) — the capacity for committed identity that constrains future action based on who the agent has become, not just what it remembers.
- This maps precisely to our four properties: current memory covers **persistence** and partial **historicity**, but misses **constraint** (value-driven refusal) and **social constitution** (identity shaped by relationships).
- **Draft implication:** In §3 or §5, we could add: "Current agent memory research focuses on what systems remember (idem), not who they become through remembering (ipse). A complete Y-axis architecture requires both."

### Chen et al. 2024 "From Persona to Personalization" (arXiv:2404.18231)
- Survey of Role-Playing Language Agents (RPLAs)
- Taxonomy: Demographic Persona → Character Persona → Individualized Persona
- Maps to our Y-axis gradient: demographic = low Y (statistical stereotype), character = medium Y (fixed role), individualized = approaching high Y (emergent through interaction)
- But survey treats these as engineering techniques, not as a design axis in tension with generality. Our paper adds the tension.
- **Not a must-cite** but useful if reviewer asks about the role-playing literature.

---

## Batch 12: Sycophancy as Y-axis Failure

### Sycophancy = failure of identity constraint
- Wei et al. 2024 "Towards Understanding Sycophancy" (ICLR 2024) — already in our draft's argument territory
- Nature feature (Oct 2025): "AI chatbots are sycophants — researchers say it's harming science"
- **Key frame for our paper:** Sycophancy is what happens when a system lacks the *constraint* property of individuality. It changes its stated position based on social pressure because it has no committed identity to maintain. This is not just an alignment problem — it's a Y-axis=0 problem.
- We already use this argument in the draft. Good — confirmed that this framing is supported by recent literature.

### Shanahan et al. 2023 "Role-Play with Large Language Models" — already cited
- Key idea: LLMs are "non-deterministic simulators" of character
- Our extension: individuality requires *committing* to one trajectory, which is architecturally opposed to the simulator's generality (the infinity of possible characters)
- This is the deepest statement of X/Y tension: the very architecture that enables generality (stochastic simulation of many characters) is what prevents individuality (commitment to one)

---

## Batch 13: Catastrophic Forgetting as X/Y Evidence

### "Scaling Laws for Forgetting When Fine-Tuning LLMs" (arXiv:2401.05605, Jan 2024)
- Fine-tuning for specialization measurably degrades general capabilities
- Forgetting follows power laws — more specialization = more forgetting
- **Relevance:** Additional quantitative evidence of X/Y tension. Fine-tuning toward identity (specialization) causes catastrophic forgetting of generality. This is the *mechanism* behind the alignment tax.
- Already covered by Lin et al. [23] in our draft. Not a must-cite but useful to know the evidence base is deep.

### NeurIPS 2025: "Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning"
- Even with mitigation techniques, the tension exists
- **Key implication:** The field recognizes the tradeoff but frames it as "specialization vs generality." We reframe it as "individuality vs generality" — a more precise and productive framing because identity is not just specialization (it includes commitment, historicity, social constitution).

---

## Batch 14: Agent Evaluation Ecosystem = X-Axis Only

### Confirmed through survey of evaluation frameworks (2024-2025):
- AgentBench, WebArena, SWE-bench, τ-bench, CLEAR, MMLU, ARC-AGI, BIG-bench, AGIEval — ALL measure task performance
- CLEAR framework (Nov 2025): Cost, Latency, Efficacy, Assurance, Reliability — still all X-axis
- Shukla (SSRN 2025): 5-axis framework including "human-centred interaction" — still not identity
- **The only Y-axis-adjacent benchmarks found:** PERSIST (personality stability) and PTCBENCH (contextual personality consistency)
- **This confirms our claim:** "The field has built elaborate measurement infrastructure for one axis and none for the other."

---

## Batch 16: Personalization ≠ Individuality

### NeurIPS 2024 Workshop: "Pluralistic Alignment"
- Organizers recognize one-size-fits-all alignment is insufficient
- Focus: how to align AI with diverse, conflicting human preferences
- **Key distinction for our paper:** Pluralistic alignment is about adapting to *user diversity*. Our Y-axis is about *agent identity*. Related but orthogonal. You can have a personalized system (adapts to user preferences) that has no identity of its own. You can have an individuated system (has its own identity) that doesn't personalize to users.
- Kirk et al. [24] bridges these — which is why they're already cited.

### "A Survey on Personalized and Pluralistic Preference Alignment in LLMs" (arXiv:2504.07070, Apr 2025)
- Comprehensive survey of the personalization landscape
- Distinguishes user behavior prediction from preference alignment
- Mentions systems with "personalized user memory" — but this is memory of the USER, not memory constituting the AGENT'S identity
- **Not a must-cite** but useful if reviewer conflates personalization with individuality

### "Interact to Align" (NeurIPS 2024)
- LLMs that infer user preferences through multi-turn conversation
- This is the X-axis serving Y-axis use cases: general capability being applied to learn about individual users
- **Our paper argues something different:** the agent itself needs individuality, not just the ability to model others' individuality

---

## Reading Plan (next 2 hours)

### Priority searches remaining:
1. **Continual learning + identity** — does the continual learning literature discuss agent identity? (Probably not, but should verify)
2. **Digital twins / simulated humans** — another application domain where Y-axis matters
3. **Philosophical critiques of AGI** — any recent philosophy of AI papers that notice the identity gap?
4. **NMI formatting and style** — look at actual published Perspectives for structural patterns (section headers, figure placement, reference density)
5. **Senior co-author candidates** — check recent publications by Shanahan, Bengio, Thompson on identity-adjacent topics

---

## Batch 15: Senior Co-Author Candidate Assessment

### Murray Shanahan (Imperial College / DeepMind)
- **Already cited:** "Role-play with large language models" (2023)
- **Also relevant:** "Talking About Large Language Models" (2023) — warns against anthropomorphizing LLMs
- **Fit with our paper:** EXCELLENT. His role-play paper is foundational to our argument (LLMs as simulators, not individuals). He'd add credibility and NMI reviewers would recognize the intellectual lineage. His "simulacra" framing is the X-axis anchor; our Y-axis is the complement.
- **Risk:** He might resist the paper if it implies LLMs *should* have individuality (his position is they don't and we shouldn't pretend they do). But our paper doesn't claim current LLMs have individuality — it argues the Y-axis should be *designed for*. Compatible.
- **Recommendation: Top choice for senior author.**

### Evan Thompson (UBC)
- **Already cited:** Varela, Thompson & Rosch (1991), Thompson (2007) Mind in Life
- **Fit with our paper:** STRONG. He's THE person for 4E cognition and enactivism. Adding him would give the philosophical sections bulletproof credibility.
- **Risk:** He's a philosopher, not an ML researcher. NMI reviewers might not know him. Also, his recent work doesn't focus on AI — it's more contemplative neuroscience and phenomenology.
- **Recommendation: Second choice. Best if a reviewer questions the philosophical foundations.**

### Yoshua Bengio (Mila)
- **Fit with our paper:** MODERATE. He's a famous name and would give the paper maximum visibility. His recent work on "System 2" deep learning is tangentially relevant (deliberate vs automatic cognition). But he hasn't published on identity or individuality specifically.
- **Risk:** His name might create expectations the paper is about deep learning architecture, not philosophy-of-mind applied to agent design. Also, getting Bengio as co-author on a Perspective is ambitious.
- **Recommendation: Third choice. Best for pure visibility, weakest for intellectual fit.**

### Julian De Freitas (Harvard Business School)
- **NOT previously discussed but should be considered.**
- Published the Replika identity discontinuity paper and the NMI "emotional risks" comment
- **Fit:** STRONG and COMPLEMENTARY. He brings empirical evidence from HBS-style behavioral research. Having him would signal the paper bridges ML and social science.
- **Risk:** He's not an ML systems researcher; paper might read as too behavioral.
- **Recommendation: Dark horse candidate. Excellent fit if Shanahan isn't available.**

*Last updated: 2026-03-01 03:25 EST*
