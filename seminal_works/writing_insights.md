# Writing Insights from NMI Seminal Perspectives

## Papers Studied

1. **Rudin (2019)** — "Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead" — NMI's most-cited paper ever (~7000+ citations)
2. **Kirk et al. (2024)** — "The benefits, risks and bounds of personalizing the alignment of large language models to individuals" — directly relevant to our Y-axis topic
3. **Ilievski et al. (2025)** — "Aligning generalization between humans and machines"
4. **Durstewitz et al. (2025)** — "What neuroscience can tell AI about learning in continuously changing environments"

## What Makes These Work (Patterns)

### 1. Title is a thesis, not a topic
- Rudin: "Stop explaining black box models... and use interpretable models instead" — the title IS the argument
- Kirk: "benefits, risks and bounds" — the title IS the structure
- Our title "The Missing Y-Axis of AGI" is good — memorable, contains the metaphor — but doesn't state the argument. Consider subtitle that states it.

### 2. First paragraph stakes a claim, not surveys a landscape
- Rudin opens with a *problem* (black boxes are being used for high-stakes decisions), not a survey of the field
- Good NMI perspectives don't begin with "Recent advances in X have led to..." 
- They begin with "X is wrong" or "X is happening and it's a problem"
- **Our intro currently starts with landscape survey ("The race to define AGI has intensified..."). Consider opening with the tension itself.**

### 3. Concrete examples carry the argument
- Rudin uses COMPAS recidivism, criminal justice, healthcare — specific cases, not abstract claims
- Kirk uses ChatGPT memory, OpenAI GPTs, specific product decisions
- **Our draft is too abstract.** We need at least 2-3 concrete examples of:
  - An agent failing because it lacks individuality
  - A use case where identity orientation matters more than capability
  - A real product/system that illustrates the X-Y tradeoff

### 4. Simple sentences, direct claims
- Rudin: "There is a widespread belief that we must trade off accuracy for interpretability. This is fundamentally wrong."
- No hedging. No "it could be argued that perhaps..."
- Sentences are short. Claims are direct. Philosophy is smuggled in through clarity, not jargon.
- **Our draft uses too many em dashes, too many multi-clause sentences, too many philosophical terms without concrete payoff.**

### 5. Figures are frameworks, not decorations
- Every cited NMI perspective that works well has 1-2 framework figures
- Kirk has a taxonomy figure
- **We need Figure 1 (the 2D quadrant) and possibly Figure 2 (the use-case spectrum)**

### 6. The tone is confident but not combative
- Rudin is passionate but precise. She attacks the *practice*, not the people.
- Kirk acknowledges the value of what exists before arguing for what's missing.
- **Our draft sometimes sounds like we're attacking AGI researchers ("the field has built elaborate infrastructure for one axis and none for the other"). Soften to "the field has not yet recognized..."**

### 7. No AI-writing tells
- No "Additionally", no "It is important to note", no "delve", no "landscape" as metaphor, no rule-of-three lists, no em dash overuse
- Straight prose. Reads like a person wrote it, not a system generated it.

## Specific Language Fixes for Our Draft

### Em dash overuse
Our draft has 10+ em dashes. NMI style prefers commas, semicolons, or separate sentences.

### "Substantially orthogonal" appears 3+ times
Vary: "largely independent", "respond to different architectural choices", "the axes don't move together"

### Philosophical jargon density
- "structural sedimentation of history" — keep, it's our key term
- "ipse-identity" / "idem-identity" — keep, but explain once and then use English
- "socially constituted before individually possessed" — good
- "constitutive condition" — replace with "necessary condition" or "requirement"
- "wantons" (Frankfurt) — risky for ML audience; keep but ensure analog is crystal clear

### Sentences that are too long
Multiple sentences in our draft exceed 40 words. NMI readers are busy ML researchers. Break them up.

## Recommended Structure Changes

1. Open with a concrete scenario, not a field survey
2. Reduce Section 4 (philosophy) by 30% — every philosophical claim should have its AI analog in the same paragraph, not in a separate section
3. Add a Box or Figure for the use-case spectrum
4. Make the conclusion shorter and punchier — Rudin's conclusion is ~100 words

## Key Reference to Add

- **Kirk et al. (2024)** should be cited in our paper — they discuss personalization of alignment, which is adjacent to our Y-axis. We should position our work as going further: they discuss adapting alignment to individuals; we argue that the system itself needs individuality.
