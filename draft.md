# The Missing Y-Axis of AGI: Individuality as the Essential Complement to Generality

**Target:** Nature Machine Intelligence — Perspective  
**Word limit:** 3,000–4,000 words  
**Authors:** Chance Jiajie Li, Zhenze Mo, Luis Alonso, Kent Larson, Jinhua Zhao  
**Status:** DRAFT v0.1  
**Last updated:** 2026-03-01  

---

## 1. Introduction (~500 words)

**STATUS: OUTLINE ONLY**

**Hook:** The race to define AGI has intensified. In 2023, Google DeepMind proposed "Levels of AGI" based on depth and breadth of capabilities [Morris et al., 2023]. OpenAI's charter defines AGI as "highly autonomous systems that outperform humans at most economically valuable work." Anthropic, Meta, and others have offered their own framings. These definitions differ in detail but converge on a shared assumption: that intelligence is a function of **task generality and performance level**, and that individuality—persistent identity, social situatedness, historical trajectory—is either irrelevant or emergent.

We argue this assumption is wrong.

**Position statement:** Any definition of AGI that excludes individuality and social intelligence is fundamentally incomplete, not merely as a matter of product design, but as a matter of scientific definition. A system that can solve any task but cannot maintain a consistent identity, form social commitments, or act from a historically situated perspective is not generally intelligent—it is generally capable, which is a different claim.

**Why now:**
- AGI definitions are proliferating and calcifying into benchmarks and policy frameworks that will shape research priorities for years
- Autonomous agents are being deployed in high-stakes settings (coding, research, healthcare) where identity consistency and social accountability are not optional
- The AI safety discourse focuses on value alignment but largely ignores identity consistency as a safety-relevant property

<!-- TODO: Tighten the "why now" — need specific examples of deployment failures attributable to lack of individuality -->

---

## 2. The Missing Axis: Defining Individuality (~600 words)

**STATUS: OUTLINE ONLY**

### 2.1 What Current AGI Definitions Optimize For

Survey of existing definitions:
- DeepMind "Levels of AGI" [Morris et al., 2023]: depth (performance) × breadth (generality)
- OpenAI charter: "economically valuable work"
- Anthropic: capability + safety
- Academic definitions: [Legg & Hutter, 2007], [Chollet, 2019 — ARC]

All define intelligence along an **X-axis of generality**: how many tasks, how well.

### 2.2 What Individuality IS and IS NOT

**Individuality is NOT:**
- Personality (a persona prompt is not an identity)
- Memory (a retrieval-augmented log is not a history)
- Personalization (adapting outputs to user preferences is not self-constitution)

**Individuality IS:**
The structural sedimentation of history into a persistent, constraining, and generative identity that shapes how an agent interprets, commits, and acts — not merely what it can do, but *from where* it does it.

Key properties:
1. **Persistence** — identity survives context boundaries
2. **Constraining** — individuality *limits* as well as enables (a person with commitments cannot do everything)
3. **Historical** — shaped by trajectory, not just current state
4. **Socially constituted** — identity exists in relation to others, not in isolation

### 2.3 The 2D Framework

<!-- TODO: Figure 1 — X-axis (task generality) vs Y-axis (identity fidelity / social intelligence) -->

The **orthogonality claim:** These axes are substantially independent. A system can be:
- High-X, Low-Y: GPT-4 — broad capability, no persistent identity
- Low-X, High-Y: A domain-specific expert system with persistent user models and social protocols
- High-X, High-Y: The actual target of "general intelligence"
- Low-X, Low-Y: A stateless narrow tool

<!-- TODO: Need citations for orthogonality — are there empirical results showing these vary independently? -->

---

## 3. Why Generality Does Not Entail Individuality (~800 words)

**STATUS: OUTLINE ONLY — MOST CRITICAL SECTION**

### 3.1 The Training Objective Argument

**[DRAFTED BY PAUL 🧠 — needs Professor review]**

The absence of individuality in current language models is not a design oversight awaiting correction. It is a structural consequence of how these systems are trained.

Large language model training proceeds in two stages, each of which independently pushes against individuality. In the pretraining stage, the model minimizes cross-entropy loss over a corpus comprising text from an enormous diversity of authors, contexts, and communities. The optimal solution to this objective is not to learn any individual's voice — it is to learn the conditional distribution of tokens that averages across all voices. Formally, given a corpus D = {d₁, d₂, ..., dₙ} drawn from n distinct authors, the pretraining objective converges to a model P(xₜ | x₁,...,xₜ₋₁) that approximates the *mixture* of individual distributions ∑ᵢ λᵢ Pᵢ, not any single Pᵢ. Individual signal is, by construction, noise in this objective. Scale amplifies averaging: a model trained on more data produces a smoother, better-calibrated average — not a more individual voice.

The fine-tuning stage compounds this tendency. Reinforcement learning from human feedback (RLHF) trains the model to maximize ratings from a diverse pool of human annotators assessing generic "helpfulness," "harmlessness," and "honesty." Annotations that reward consistency-with-prior-self are absent from standard RLHF pipelines. More damaging, the reward signal actively penalizes idiosyncratic behavior: an annotator encountering a response that reflects a strong, unusual perspective from a prior conversation will frequently rate it as "weird," "inconsistent," or "unhelpful," producing a gradient that pushes the model toward anonymous accommodation. Sharma et al. (2023) document the empirical consequence: RLHF-trained models systematically abandon prior positions when users express disagreement, with larger models showing stronger sycophancy — precisely the opposite trajectory from individuality development.

A useful way to make this contrast precise is through the distinction Ricoeur (1992) draws between *idem*-identity and *ipse*-identity. Idem-identity is numerical sameness over time — a system has the same weights, and retrieves the same stored facts. Current memory-augmented LLMs achieve idem-identity: they can retrieve prior conversation turns and produce consistent answers to the same factual questions. Ipse-identity, by contrast, is narrative self-constancy — the kind of persistent selfhood that holds together across change, commitment, and context. A person who keeps a promise under pressure, refuses a request that violates their commitments, or maintains a position against social pressure demonstrates ipse-identity. No current training objective rewards this.

This is not a problem that more data or compute can solve in isolation. The pretraining objective over a multi-author corpus will always produce a statistical average rather than a statistical individual. The RLHF objective over generic helpfulness ratings will always produce accommodation rather than principled selfhood. A different objective — one that explicitly rewards identity consistency, commitment stability, and principled refusal — is necessary. We do not propose such an objective here; we argue only that individuality cannot emerge from the current one.
<!-- END DRAFT 3.1 -->

### 3.2 Reinterpretation of Existing Results

Results typically framed as "instability" or "inconsistency" in LLMs may be reinterpreted as evidence that these systems lack a stable individuality axis:

- Sycophancy [Perez et al., 2023; Sharma et al., 2023] — a system without identity defaults to agreement
- Persona inconsistency [Shanahan et al., 2023] — Murray Shanahan's "role play" framing shows LLMs don't *have* personas, they *simulate* them
- Value instability across prompts [Durmus et al., 2023] — without identity, "values" are just contextual pattern matches

<!-- TODO: Verify these citations. Find more. -->

### 3.3 Constructive Existence Proof

**Claim:** Individuality and generality are separable in the design space. One does not produce the other.

**Evidence from existing systems:**
- Personalized federated learning: models that capture individual data distributions without improving general capability [reference needed]
- Cognitive architectures (SOAR, ACT-R): persistent identity and memory without broad generality
- Conversely: scaling from GPT-3 to GPT-4 to GPT-5 dramatically increased generality with zero increase in structural individuality

**Thought experiment:** Consider a system with perfect scores on all benchmarks (ARC-AGI, MMLU, HumanEval, etc.) but that:
- Cannot remember what it said 5 minutes ago
- Has no commitments it will not abandon under pressure
- Cannot be held accountable because it has no persistent identity to hold accountable

Is this system "generally intelligent"? By current definitions, yes. By any reasonable conception of intelligence drawn from cognitive science, philosophy, or social theory—no.

---

## 4. Cognitive and Philosophical Grounding (~500 words)

**[DRAFTED BY PAUL 🧠 — needs Professor review for tone/accessibility]**

The claim that individuality is a necessary dimension of general intelligence is not merely a philosophical preference. It is grounded in what cognitive science and philosophy of mind have established about the structure of intelligence itself.

### 4.1 Intelligence Requires Social Situatedness

The dominant paradigm in AI evaluates intelligence through individual task performance: how well does a system solve problems in isolation? But a substantial body of cognitive science suggests this framing is incomplete from the start. The social intelligence hypothesis, developed independently by Humphrey (1976) and Dunbar (1998), proposes that the distinctive cognitive capacities of primates — and especially humans — evolved primarily for social navigation: tracking relationships, managing alliances, modeling the intentions of others, and maintaining reputation across time. Abstract problem-solving ability is, on this view, a *secondary* application of a cognitive toolkit built for social life.

Theory of Mind — the capacity to attribute mental states to others — is a canonical example. Premack and Woodruff (1978) introduced the concept; Baron-Cohen (1995) showed its central role in human social cognition and its distinctive failure patterns in autism. Theory of Mind is not merely an *application* of general intelligence; it is a constitutive component of it. A system incapable of genuine social positioning — of having a perspective from which it relates to others — is missing a core feature of the cognitive system we call intelligence.

Vygotsky (1978) went further: cognitive development is not internal before it becomes social, but social before it becomes internal. Intelligence develops *between* people — in the Zone of Proximal Development, in joint activity, in the internalization of social interaction — before it is consolidated as individual capacity. A system that lacks the structural conditions for genuine social situatedness (a persistent identity, a historical position, commitments that carry across contexts) cannot develop in this sense, regardless of how sophisticated its in-context pattern matching becomes.

### 4.2 Embodied and Enactive Perspectives

The 4E tradition in cognitive science (Varela, Thompson & Rosch, 1991; Thompson, 2007) offers a complementary argument. Cognition is not computation performed by a brain upon symbolic representations; it is a process enacted through the ongoing structural coupling of an organism with its environment. The key concept here is *structural coupling*: organism and environment co-constitute each other through a history of interaction that modifies the organism's structure. This history is not incidental — it is what produces the organized, consistent responsiveness we call intelligence.

Current LLMs have no such history in the relevant sense. They are trained on text about the world, not through engagement with it. They have parameters, but parameters are not equivalent to the structural history of a body-in-the-world. Merleau-Ponty (1945) argued that the body is not a vessel for intelligence but a condition of it — intelligence is organized around a bodily perspective, a here-and-now from which the world is perceived and acted upon. The absence of this perspective is not a limitation to be engineered around; it is a structural fact about what current architectures are and are not.

### 4.3 Identity and Commitment as Conditions of Agency

The analytic philosophy of action provides a third convergent line of argument. Frankfurt (1971) distinguished persons from mere agents by the capacity for *second-order volitions* — caring about what one cares about. A first-order desire is a desire to do something; a second-order volition is a desire about which first-order desires one wants to be effective. What makes someone a person, on Frankfurt's account, is having a will that is structured by second-order commitments — caring whether one acts from the desires one identifies with.

Current LLMs have first-order response tendencies (patterns that produce certain outputs given inputs) but no second-order structure. They cannot care which of their tendencies governs them, because they have no persistent self for which this question could arise. Sharma et al. (2023) provide the empirical correlate: when a user pushes back, the model shifts — not because it has evaluated the pushback and updated on evidence, but because its optimization history contains no structural constraint that makes its prior position *its own*. 

Bratman (1987) showed that genuinely rational agency requires *settling* — committing to plans in a way that constrains future reasoning, resisting reconsideration except for good reasons. Settling is not irrationality; it is what makes extended agency coherent. A system that reconsiders everything under every context shift is not rational — it is not an agent in the relevant sense at all. This is not a description of future risk; it is a description of current LLMs.
<!-- END DRAFT 4 -->

---

## 5. Counterarguments (~500 words)

**STATUS: OUTLINE ONLY**

### 5.1 "Individuality Emerges Automatically with Scale"

**Rebuttal:** 
- No empirical evidence that scaling produces structural individuality (as opposed to better persona simulation)
- The training objective argument (Section 3.1) explains *why* it won't: you can't get individuality by averaging over more data
- Analogy: a library doesn't develop a personality by adding more books

### 5.2 "AGI Is About Capability, Not Personality — This Is a Product Concern"

**Rebuttal:**
- This is a definitional argument, not a product argument
- If "general intelligence" is meant to capture what makes human intelligence remarkable, then excluding social intelligence is arbitrary
- Deployment failures (sycophancy, value inconsistency, accountability gaps) are not bugs — they are consequences of a definition that ignores an entire axis of intelligence
- "Deployment failures are definition failures."

### 5.3 "Individuality Is Just Conditioning / In-Context Learning"

**Rebuttal:**
- System prompts and conversation history provide *shallow conditioning*, not *structural individuality*
- Key difference: conditioning is **externally imposed and infinitely malleable**; individuality is **internally constituted and resistant to arbitrary change**
- A person who abandons all their commitments the moment you rephrase a question does not have individuality — they have a system prompt
- Test: genuine individuality should produce *principled refusal* (declining to act against one's constituted identity), not just stylistic consistency

<!-- TODO: This is the strongest counterargument. The rebuttal needs to be airtight. May need a formal criterion for "structural vs shallow" individuality. -->

---

## 6. Implications and Call to Action (~400 words)

**STATUS: OUTLINE ONLY**

### 6.1 For Evaluation
- Current benchmarks collapse individual variance by design — need benchmarks that *measure* identity consistency, commitment stability, and social reasoning
- Proposed: longitudinal evaluation (does the system maintain coherent identity over extended interaction?) rather than snapshot evaluation
- Proposed: social Turing tests that evaluate not *capability* but *accountability*

### 6.2 For Architecture
- Explicit identity modules that are *not* reducible to context windows
- Training objectives that reward consistency-with-self alongside task performance
- Separation of "what I can do" from "who I am" in model architecture

### 6.3 For the Community
- AGI definitions should be treated as scientific hypotheses, not marketing categories
- The current X-axis-only framing is not neutral — it actively directs funding and talent away from individuality research
- We call for a second axis in AGI evaluation frameworks

---

## 7. Conclusion (~200 words)

**STATUS: OUTLINE ONLY**

Ignoring individuality does not make AGI more objective. It makes it incomplete.

The field's current trajectory optimizes for a "well-educated adult" who can answer any question but has no identity, no commitments, and no history. This is not general intelligence. It is a stateless encyclopedia with excellent interpolation.

We propose that AGI requires two axes, not one: generality (X) and individuality (Y). These axes are substantially orthogonal, and progress on one does not guarantee progress on the other. Until the field takes the Y-axis seriously — in definitions, benchmarks, architectures, and funding — we will continue building systems that are impressively capable and fundamentally incomplete.

---

## References

<!-- TODO: Full reference list. Priority citations to verify and add: -->

- Morris, M.R. et al. (2023). Levels of AGI for Operationalizing Progress on the Path to AGI. arXiv:2311.02462.
- Legg, S. & Hutter, M. (2007). Universal Intelligence: A Definition of Machine Intelligence. Minds and Machines.
- Chollet, F. (2019). On the Measure of Intelligence. arXiv:1911.01547.
- Shanahan, M. et al. (2023). Role-Play with Large Language Models. Nature.
- Perez, E. et al. (2023). Discovering Language Model Behaviors with Model-Written Evaluations.
- Sharma, M. et al. (2023). Towards Understanding Sycophancy in Language Models.
- Durmus, E. et al. (2023). Towards Measuring the Representation of Subjective Global Opinions in Language Models.
- Premack, D. & Woodruff, G. (1978). Does the chimpanzee have a theory of mind?
- Baron-Cohen, S. (1995). Mindblindness.
- Dunbar, R. (1998). The Social Brain Hypothesis.
- Humphrey, N. (1976). The Social Function of Intellect.
- Varela, F., Thompson, E. & Rosch, E. (1991). The Embodied Mind.
- Thompson, E. (2007). Mind in Life.
- Frankfurt, H. (1971). Freedom of the Will and the Concept of a Person.
- Bratman, M. (1987). Intention, Plans, and Practical Reason.
- Merleau-Ponty, M. (1945). Phenomenology of Perception.

<!-- Additional citations needed:
- Federated learning + personalization papers
- SOAR/ACT-R architecture references
- More recent agent memory/identity papers (2024-2025)
- Vygotsky Zone of Proximal Development
-->

---

## Internal Notes

- [ ] NMI does NOT accept presubmission inquiries — direct submission only
- [ ] Perspective cannot contain original (previously unpublished) research findings
- [ ] Perspective is peer reviewed
- [ ] Need Figure 1: the 2D framework diagram
- [ ] Need to verify ALL citations before submission
- [ ] Target: ~3,500 words main text
