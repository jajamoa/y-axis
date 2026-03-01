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

*Last updated: 2026-03-01 03:22 EST*
