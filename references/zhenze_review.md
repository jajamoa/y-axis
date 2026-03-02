# Zhenze's Paper Collection — Critical Review

## Paper Inventory (21 papers)

### BLOCK 1: Foundations of AI & Intelligence Definition
| # | ID | Title | Authors | Year |
|---|-----|-------|---------|------|
| 1 | turing.pdf | Computing Machinery and Intelligence | Turing | 1950 |
| 2 | cs/0605024 | A Formal Measure of Machine Intelligence | Legg & Hutter | 2006 |
| 3 | 0712.3329 | Universal Intelligence: A Definition of Machine Intelligence | Legg & Hutter | 2007 |
| 4 | 1510.04931 | Bad Universal Priors and Notions of Optimality | - | 2015 |
| 5 | 1911.01547 | On the Measure of Intelligence | Chollet | 2019 |

### BLOCK 2: Training Paradigm & Scaling
| # | ID | Title | Authors | Year |
|---|-----|-------|---------|------|
| 6 | 2001.08361 | Scaling Laws for Neural Language Models | Kaplan et al. | 2020 |
| 7 | 2203.15556 | Training Compute-Optimal LLMs (Chinchilla) | Hoffmann et al. | 2022 |
| 8 | 2206.07682 | Emergent Abilities of Large Language Models | Wei et al. | 2022 |
| 9 | 2203.02155 | Training LMs to Follow Instructions (InstructGPT/RLHF) | Ouyang et al. | 2022 |

### BLOCK 3: AGI Definitions & Abstraction
| # | ID | Title | Authors | Year |
|---|-----|-------|---------|------|
| 10 | 2311.02462 | Levels of AGI | Morris et al. (DeepMind) | 2023 |
| 11 | 2510.18212 | A Definition of AGI | Hendrycks et al. | 2025 |
| 12 | 2102.10717 | Abstraction and Analogy-Making in AI | Mitchell | 2021 |
| 13 | 2102.11107 | Towards Causal Representation Learning | Schölkopf et al. | 2021 |

### BLOCK 4: Alignment & Value Trade-offs
| # | ID | Title | Authors | Year |
|---|-----|-------|---------|------|
| 14 | 2112.00861 | A General Language Assistant as a Laboratory for Alignment | Askell et al. (Anthropic) | 2021 |
| 15 | 3442188.3445922 | On the Dangers of Stochastic Parrots | Bender et al. | 2021 |
| 16 | 2602.12134 | Value Alignment Tax | Chen et al. | 2026 |

### BLOCK 5: New Directions — Identity, Persona, Social
| # | ID | Title | Authors | Year |
|---|-----|-------|---------|------|
| 17 | 2601.10387 | The Assistant Axis | Lu et al. | 2026 |
| 18 | 2508.17407 | General Social Agents | - | 2025 |
| 19 | 2601.05171 | Inside Out: PersonaTree for Long-Term Dialogue | - | 2026 |

### BLOCK 6: Economics & Model-Based RL (supporting)
| # | ID | Title | Authors | Year |
|---|-----|-------|---------|------|
| 20 | 2602.20946 | Some Simple Economics of AGI | - | 2026 |
| 21 | 1907.02057 | Benchmarking Model-Based RL | - | 2019 |

---

## Zhenze's Narrative (reconstructed from his description)

**Story arc:** Turing → formal intelligence definitions (Legg/Hutter, Chollet) → mathematical optimization (scaling laws, RLHF) → current AGI definitions (Morris, Hendrycks) → problems with current paradigm (no memory, no identity, alignment tax, average voice) → emerging counter-movements (Assistant Axis, social agents) → need for new AGI definition → our Y-axis proposal.

This is a **historical narrative of how the field arrived at an X-axis-only conception of AGI, and why that's now breaking down.**

---

## Critical Analysis of Each Paper for Y-Axis Relevance

### ALREADY CITED in our draft:
- **2311.02462 (Morris et al.)** — [1] in current draft. Already well-used.
- **1911.01547 (Chollet)** — [2] in current draft. Already well-used.

### SHOULD CITE (high relevance, not currently cited):

**2601.10387 — "The Assistant Axis" (CRITICAL)**
- **Relevance:** ★★★★★
- **Why:** This is the closest existing work to our Y-axis concept — but fundamentally different. They find a "leading component of persona space" that captures how much a model is in "default Assistant mode." Steering away from the Assistant direction causes persona drift and bizarre behavior.
- **Key distinction from our paper:** Their "Assistant Axis" is about the *positioning* of a model within its pre-existing persona space (helpful assistant vs. other characters). Our Y-axis is about whether a model HAS a persistent, self-consistent identity at all. Their axis is within the space of possible performances; ours is about whether there's a someone performing.
- **Zhenze's framing:** He says it's "similar to our axis concept but different from our argument" — correct. The Assistant Axis is an empirical finding about model internals; our Y-axis is a design framework for what AGI should include.
- **MUST CITE.** Add to §3 or §5: "Recent work has identified an 'Assistant Axis' in model activation space [ref], capturing the degree to which a model operates in its default helpful persona. This empirical finding confirms that persona is a real, measurable dimension of model behavior — but the axis they identify is orthogonal to ours: it measures *which* persona a model currently performs, not whether the model has a persistent identity that constrains performance."
- **Citation:** Lu, C. et al. The Assistant Axis: Situating and stabilizing the default persona of language models. arXiv:2601.10387 (2026).

**2602.12134 — "Value Alignment Tax" (IMPORTANT)**
- **Relevance:** ★★★★☆
- **Why:** This paper introduces a "Value Alignment Tax (VAT)" framework — alignment interventions propagate unintended changes across the value system. This is DIRECT evidence for our X/Y tension: alignment (moving in the Y-axis direction) has systemic costs on the broader value structure.
- **Relation to our existing [23] (Lin et al. alignment tax):** This paper is NEWER and more sophisticated — it measures how alignment interventions ripple through interconnected values using Schwartz value theory.
- **Decision needed:** Should this REPLACE our current [23] (Lin et al.), or be cited alongside? The Chen et al. paper is more comprehensive (measures value propagation, not just capability degradation), but Lin et al. is published (EMNLP 2024) while Chen et al. is under review.
- **Citation:** Chen, J. et al. Value Alignment Tax: Measuring value trade-offs in LLM alignment. arXiv:2602.12134 (2026).

**2510.18212 — "A Definition of AGI" (Hendrycks et al.) (IMPORTANT)**
- **Relevance:** ★★★★☆
- **Why:** The most recent and mathematically sophisticated AGI definition — uses Cattell-Horn-Carroll cognitive theory, 10 cognitive domains, psychometric batteries. GPT-4 scores 27%, GPT-5 scores 57%.
- **Critical observation:** The 10 domains are ALL capability domains (reasoning, memory, perception, etc.). Zero mention of identity, individuality, or social constitution. Even their "long-term memory storage" domain (where current AI has the biggest deficit) is about *capability* (can you store and retrieve?), not *identity* (does what you store shape who you become?).
- **This paper is our strongest single example of the field's blind spot.** Hendrycks et al. 2025 is the most comprehensive, best-grounded AGI definition available — and it's entirely X-axis. We're not arguing they're wrong; we're arguing they're incomplete.
- **MUST CITE.** Best placement: §1, alongside Morris et al.: "The most recent AGI framework maps ten cognitive domains grounded in psychometric theory [ref], yet all ten measure task capability; none measures the persistence or coherence of the entity being tested."
- **Citation:** Hendrycks, D. et al. A Definition of AGI. arXiv:2510.18212 (2025).

**2508.17407 — "General Social Agents" (RELEVANT)**
- **Relevance:** ★★★☆☆
- **Why:** Demonstrates that AI agents can predict human behavior in novel game settings using theory-grounded natural language instructions + empirical data. 883,320 games, outperforms game-theoretic equilibria.
- **Connection to our paper:** Social agents need *individuated* humans to model. Their heterogeneous population of agents reflects individual differences. But this is about *modeling* human individuality, not *possessing* it.
- **Possible cite in §2 (social simulation use case):** Shows the practical value of modeling individual differences in agent populations.
- **Citation:** [Authors]. General social agents. arXiv:2508.17407 (2025).

### USEFUL CONTEXT (not necessarily for citation):

**Turing 1950 — "Computing Machinery and Intelligence"**
- The original question: "Can machines think?" The Turing Test is about behavioral indistinguishability — an X-axis measure. But Turing himself considered objections about consciousness, emotions, and self-awareness. We could note that even Turing's original paper acknowledged dimensions beyond capability, though he chose to set them aside.
- **Already covered by existing framing. Optional citation for opening.**

**Legg & Hutter 2006/2007 — "Formal Measure / Universal Intelligence"**
- Mathematical definition: intelligence = ability to achieve goals across a wide range of environments.
- Entirely X-axis. Influential in formalizing the "generality" concept.
- **Worth citing in §1 as a precursor to Morris/Hendrycks:** "Formal definitions of machine intelligence have converged on a single measure: the ability to achieve goals across diverse environments [Legg & Hutter 2007]."
- **RECOMMENDED.** Strengthens the historical argument.

**Kaplan et al. 2020 / Hoffmann et al. 2022 — Scaling Laws / Chinchilla**
- Established that capability scales predictably with compute, data, and parameters.
- Supports Zhenze's narrative: scaling laws led the field to believe more compute = more intelligence (X-axis optimization).
- **Useful for §3:** "Scaling laws established that task capability improves predictably with compute [ref], leading to the implicit assumption that all desirable properties — including identity-relevant ones — would emerge with scale. PERSIST [Tosato et al. 2026] shows this assumption is false for behavioral consistency."

**Wei et al. 2022 — "Emergent Abilities of LLMs"**
- Certain capabilities appear suddenly at scale thresholds.
- Supports the "emergence hypothesis" that our paper argues DOESN'T hold for individuality.
- **Possible cite:** "While certain capabilities emerge with scale [Wei et al. 2022], behavioral consistency does not [Tosato et al. 2026]."

**Ouyang et al. 2022 — InstructGPT/RLHF**
- The paper that introduced RLHF for instruction-following.
- Central to our argument: RLHF optimizes for human approval (X-axis), actively selects against individuality (Y-axis).
- **Already referenced via alignment tax. Could cite directly for RLHF as mechanism.**

**Askell et al. 2021 — "A General Language Assistant as a Laboratory for Alignment" (Anthropic)**
- Early Anthropic paper defining the assistant paradigm: helpful, harmless, honest.
- **Key for our paper:** This paper DEFINES the default orientation of modern LLMs — helpful assistants. Our Y-axis asks: what if you need something other than a helpful assistant? What if you need an *individual*?
- **RECOMMENDED.** Cite in §3: "The dominant paradigm explicitly optimizes for a 'helpful, harmless, honest' assistant [Askell et al. 2021], an orientation that by design produces a generic, undifferentiated service rather than an individuated agent."

**Bender et al. 2021 — "Stochastic Parrots"**
- LLMs as "stochastic parrots" — producing language without understanding.
- **Connection to our paper:** A stochastic parrot has no identity; it mimics patterns. Our Y-axis measures the distance from "parrot" to "person." But we should be careful: our paper doesn't argue LLMs should be persons. We argue the design space should be explicit.
- **Optional citation. Risk: associating our paper with the Bender et al. controversy.**

**Mitchell 2021 — "Abstraction and Analogy-Making in AI"**
- Argues abstraction is central to intelligence; current AI lacks it.
- X-axis argument (capability deficit), but the kind of capability she discusses (analogy-making) is closer to the cognitive flexibility that our Y-axis might enable.
- **Not directly relevant to our argument. Skip.**

**Schölkopf et al. 2021 — "Towards Causal Representation Learning"**
- Argues for learning causal rather than correlational representations.
- Tangentially relevant: causal understanding of self could be part of deep individuality. But this is too abstract for our paper.
- **Not directly relevant. Skip.**

**Inside Out (2601.05171) — PersonaTree**
- Memory architecture for long-term personalized dialogue.
- **Our analysis from previous lit review applies:** This is about USER modeling (remembering the user), not AGENT identity (the agent having its own identity). PersonaTree helps the agent remember who the USER is, not who IT is.
- **Optional cite in §5 (architectures):** "Emerging memory architectures like PersonaTree [ref] address user profiling but not agent identity; they solve the problem of remembering the interlocutor, not of being someone worth interacting with."

**Some Simple Economics of AGI (2602.20946)**
- Economic analysis: as AI automates execution, the bottleneck shifts to human verification.
- "Measurability Gap" between what agents can do and what humans can verify.
- **Interesting tangent:** If identity makes an agent more predictable (trustworthy), it reduces the "Cost to Verify" — an economic argument for the Y-axis.
- **Not essential. Skip for now.**

**Bad Universal Priors (1510.04931)**
- Technical philosophy of science paper about universal priors.
- **Not relevant to our paper. Skip.**

**Benchmarking Model-Based RL (1907.02057)**
- RL benchmark paper.
- **Not relevant to our paper. Skip.**

---

## Evaluation of Zhenze's Narrative

### Strengths:
1. **Historical arc is correct and compelling.** Turing → formal definitions → scaling → RLHF → current AGI race → blind spot. This is the right story.
2. **The "convergence" argument is strong.** Multiple independent lines of work (Legg/Hutter, Chollet, Morris, Hendrycks) all converge on X-axis-only definitions. This isn't one group's oversight; it's the field's consensus.
3. **The training paradigm critique is well-chosen.** Scaling laws + RLHF + emergence → the belief that scale will solve everything. Our paper says: not for individuality.
4. **The inclusion of Assistant Axis is excellent.** It shows the field is *starting* to notice the problem but framing it incorrectly (as a stability issue rather than a design axis).
5. **The Value Alignment Tax paper strengthens our existing argument** — a more comprehensive version of the alignment cost evidence.

### Weaknesses / Concerns:
1. **Some papers are tangential.** Mitchell (abstraction), Schölkopf (causal learning), Model-Based RL — these don't directly support the Y-axis argument. Including them risks diluting the narrative.
2. **The economics paper is interesting but off-topic for NMI.** The "measurability gap" argument is clever but would require too much setup to incorporate.
3. **Missing the companion/relationship angle entirely.** Zhenze's narrative is purely about the intellectual history of intelligence definitions. Our paper also makes the case through application domains (companions, education, therapy). De Freitas et al. (Replika), Park et al. (Generative Agents), therapeutic alliance — these are absent from his collection.
4. **"No speaker behind speech" is a great phrase** that should be in the paper if it isn't already. Need to check.

### Key Insight from Zhenze's Narrative:
**The narrative should flow:** intelligence was defined as capability → capability was operationalized through scaling → scaling became the dominant research paradigm → this paradigm has a structural blind spot → the blind spot is individuality → we need a new axis.

This is tighter and more historically grounded than our current draft's opening, which starts with a scenario. **Consider:** keeping the scenario opening (it's more engaging for NMI readers) but weaving Zhenze's historical narrative into §1 or §3.

---

## Recommendations for Draft Revision

### Must-add citations from Zhenze's collection:
1. **The Assistant Axis (2601.10387)** — directly comparable work; must distinguish from our Y-axis
2. **Hendrycks "A Definition of AGI" (2510.18212)** — strongest example of X-axis-only blind spot
3. **Value Alignment Tax (2602.12134)** — newer, stronger evidence for alignment costs

### Should-add (strengthens historical narrative):
4. **Legg & Hutter "Universal Intelligence" (0712.3329)** — foundational X-axis definition
5. **Askell et al. "A General Language Assistant" (2112.00861)** — defines the assistant paradigm
6. **Scaling Laws (2001.08361)** — supports "scale doesn't solve individuality" argument

### Optional:
7. General Social Agents (2508.17407) — social simulation relevance
8. Stochastic Parrots (3442188.3445922) — "no speaker behind speech" argument
9. Turing 1950 — historical opening

### Skip (not relevant enough for NMI Perspective):
- Mitchell (abstraction), Schölkopf (causal), Inside Out (user memory), Economics of AGI, Bad Universal Priors, Model-Based RL, Wei et al. (emergent abilities — useful one-liner but not essential), Chinchilla, InstructGPT (already covered via alignment tax)

### Total new citations to add: 3-6 (bringing total from 24 to 27-30, well within NMI 100 limit)
