# Zhenze Batch Review — 20 Papers from Google Drive
*Reviewed by Paul (PhD, LLM Reasoning) — 2026-03-02*

---

## Triage Summary

**Geology/Mining files (8 files) — SKIP:**
- 历史地质图纸、质量公报、历史地质资料、勘探计划书、Sayak Copper CPR、0746、Mineral prospectivity、1-s2.0-...
- Ended up in the Drive folder by mistake. No action needed.

**Already in draft (duplicates):**
- 2311.02462 = [1] Morris et al., "Levels of AGI"
- 1911.01547 = [2] Chollet, "On the Measure of Intelligence"

---

## TIER 1 — Add to draft (high priority)

### 2601.10387 — "The Assistant Axis"
Probes LLM persona space; finds a dominant "Assistant Axis" — a single activation direction governing how much a model operates in default helpfulness mode. Post-training collapses persona diversity onto one dimension.

**Verdict: ADD.** This is the paper Zhenze flagged as "similar but different." It's the productive foil we need. The Assistant Axis = convergence toward compliance. Our Y-axis = structural individuation. A system maximally on the assistant axis has minimal Y — empirically confirming the Y=0 attractor that current training creates.

*Use in §3 (RLHF creates persona attractor) + §5 (explicitly differentiate: "The assistant axis measures compliance direction; our Y-axis measures structural individuation — they are opposite ends of the same problem").*

### 2602.12134 — "Value Alignment Tax"
Formalizes alignment tax using Schwartz value theory. Alignment interventions (prompting, RLHF, fine-tuning) create off-target value losses — on-target gains (helpfulness) come with value profile narrowing.

**Verdict: ADD as primary alignment tax citation.** More directly relevant than current [23] Lin et al. (which shows capability degradation). This shows RLHF actively reshapes value expressions toward a consensus profile — i.e., the mechanism by which training creates the Y=0 attractor.

*Use in §3.1, replacing or supplementing current [23].*

### Turing (1950) — "Computing Machinery and Intelligence"
The original Turing Test paper. Intelligence = behavioral performance on tasks.

**Verdict: ADD. One-sentence genealogical citation.** The Turing Test is the foundational X-axis-only framework. "The question Turing posed was operationalized as behavioral performance — a framing dominant for 75 years that produced increasingly capable systems while leaving a different question unasked: not whether a machine can perform, but whether there is someone behind the performance."

*Use in §1 or §2 as the historical origin of the X-axis-only paradigm.*

### 2601.05171 — "Inside Out: PersonaTree"
Engineering solution for persona inconsistency in long-term dialogue. Dedicated hierarchical memory structure needed just to maintain coherent user-facing persona.

**Verdict: ADD.** Engineering existence proof that persona coherence requires explicit architectural support — it does not emerge from scale. Complements Li et al. [20] (drift evidence) with a parallel evidence stream.

*Use in §3.3: "The emergence of dedicated persona-management architectures [...] confirms that individuality is not a property that scale produces — it requires explicit structural support [REF]."*

---

## TIER 2 — Use selectively

### 2203.02155 — InstructGPT (Ouyang et al.)
The original RLHF paper. First demonstration of alignment/capability tradeoff.

**Verdict: Consider adding as founding citation for alignment tax genealogy.** Current draft cites the tax but not its origin. Brief.

### 2510.18212 — "A Definition of AGI" (CHC theory)
Operationalizes AGI as cognitive versatility across 10 domains (Cattell-Horn-Carroll framework). Stays entirely on X-axis.

**Verdict: Cite alongside [1] Morris et al.** Confirms that even recent formal AGI definitions are one-dimensional.

### 0712.3329 — "Universal Intelligence" (Legg & Hutter)
Mathematical definition of intelligence as expected reward across all computable environments. Foundational formal definition — purely X-axis.

**Verdict: Consider for §2** as the formal pole of existing definitions. Pairs with Turing (behavioral) and Morris et al. (operational) to show the full lineage of X-axis-only definitions.

### 2602.20946 — "Some Simple Economics of AGI"
Models AGI transition as execution costs → 0; human verification bandwidth becomes the binding constraint on growth.

**Verdict: Consider for §6 Implications.** Novel angle: if execution is free, accountability is scarce — and individuated agents are structurally better positioned for accountability than stateless ones. "As the cost of AI execution approaches zero, the binding constraint becomes human capacity to validate and underwrite responsibility [REF]. Individuated agents — with persistent commitments and traceable histories — are structurally suited to absorb some of this accountability load. Stateless systems, by definition, cannot be held responsible across time."

---

## TIER 3 — Skip

- **2203.15556** (Chinchilla): compute-optimal scaling. Not relevant.
- **2102.11107** (Causal Representation Learning): no link to individuality.
- **2206.07682** (Emergent Abilities): interesting contrast (abilities emerged, individuality didn't) but adding it requires a sentence that could distract.
- **2508.17407** (General Social Agents): about theory generalizability, not individuality.
- **2102.10717** (Abstraction/Analogy in AI): not our argument.
- **1907.02057** (Model-Based RL Benchmark): irrelevant.
- **1510.04931** (Bad Universal Priors): technical theory, not relevant.
- **2112.00861** (Anthropic 2021 alignment): superseded by Constitutional AI [19].
- **3442188.3445922** (Stochastic Parrots): peripheral to our specific claim.
- **2001.08361** (Scaling Laws): use only if adding explicit historical arc paragraph.

---

## Assessment of Zhenze's Narrative Arc

Zhenze's proposed structure:
1. AI definitions → mathematical/optimization framing
2. Training paradigm (scaling laws, emergent abilities, RLHF)
3. AGI = only increasing generality
4. Problems: memory resets, average voice, no speaker behind speech, alignment tax
5. Similar axis (assistant-axis) but different
6. Need Y-axis (individuality)

**What's strong:** More historically grounded than the current draft. The genealogy from Turing → scaling → RLHF → AGI definitions positions our paper as completing an intellectual arc, not just proposing a new idea. "No speaker behind the speech" is an excellent phrase — precise, concrete, quotable.

**Gaps in current draft:**

1. **Historical arc is implicit, not explicit.** The draft argues the framework but doesn't trace how the field systematically converged on X-axis-only. Adding 2-3 sentences in §1/§2 on the Turing→scaling→RLHF lineage would strengthen "why this gap exists."

2. **Assistant axis differentiation is missing.** 2601.10387 is the field's closest approximation to a Y-axis. Without engaging it explicitly, Reviewer 2 will ask "isn't this just the assistant axis rebranded?" The answer is clear and strong — but it needs to be in the paper.

3. **"No speaker behind the speech"** — Zhenze's phrase should appear in the paper. It's exactly the ipse-identity gap, formulated concisely. Consider integrating into §3 or the opening.

4. **Economics angle is untapped.** The verification bandwidth argument (2602.20946) motivates Y-axis from pure engineering economics without any philosophical commitment. One sentence in §6.

5. **Historical genealogy makes the critique structural.** If Turing, Legg/Hutter, Chollet, and Morris et al. all operationalize intelligence without individuality, this is not an oversight — it's a systematic exclusion baked into the field's origin. Naming the lineage sharpens the claim.

---

## Recommended Changes (summary for Professor)

**High priority (meaningfully change the argument):**
1. Add 2601.10387 — cite in §3, differentiate in §5
2. Add 2602.12134 — replace/supplement current [23] alignment tax
3. Add Turing 1950 — one sentence in §1/§2
4. Add 2601.05171 — one sentence in §3.3

**Medium priority:**
5. Add 2510.18212 (CHC AGI definition) alongside [1]
6. Add Legg & Hutter 0712.3329 in §2
7. Add Ouyang et al. InstructGPT as founding RLHF/alignment citation
8. Add 2602.20946 (Economics) in §6

**New ref count:** ~8 additions → 25 → ~33 refs. Within NMI Perspective norms (30-40 is common).
