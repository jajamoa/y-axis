# The Missing Y-Axis of AGI: Individuality as the Essential Complement to Generality

**Target:** Nature Machine Intelligence — Perspective  
**Word limit:** 3,000–4,000 words  
**Authors:** Chance Jiajie Li, Zhenze Mo, Luis Alonso, Kent Larson, Jinhua Zhao  
**Status:** DRAFT v1.0-rc6 — §2 definition reordered (positive first), §3 restructured around 4 Y-axis properties, SOAR/FedAvg cut, CAI hardened, §4 bridging sentences added  
**Last updated:** 2026-03-03  

---

**Abstract.** Current definitions of Artificial General Intelligence converge on a single axis of evaluation: task generality—the breadth and depth of capability across domains. We argue that this framing misses a second, orthogonal axis: individuality—the structural sedimentation of history into a persistent, constraining, and generative identity. These two design orientations—generalist capability and individuated identity—are not merely different objectives; they are in genuine tension, with architectural choices that optimize for one actively working against the other. We show that current training paradigms are structurally oriented away from individuality and that scaling does not resolve this. We propose a two-dimensional framework that maps applications from productivity assistants (capability-dominant) to social simulations (identity-dominant), and outline implications for benchmarks, architectures, and research priorities. The Y-axis is not merely unmeasured—it is not yet well-defined. Defining it is one contribution of this paper.

---

Consider two AI systems. The first can write code, diagnose diseases, summarize legal documents, and pass graduate-level exams in dozens of fields. Ask it the same value-laden question twice in a row after a context reset, and it may give contradictory answers. It has no persistent identity, no commitments it will not abandon under pressure, no history that shapes how it interprets the world. The second system can do only one thing well, but it has a consistent perspective, remembers what it has said, and will decline requests that conflict with its established commitments. Current definitions of AGI would rate the first system as closer to general intelligence. We think this gets something important wrong.

The major frameworks agree on what intelligence means: task generality. DeepMind's "Levels of AGI" measures depth and breadth of performance [1]. OpenAI's charter targets "highly autonomous systems that outperform humans at most economically valuable work." Chollet's ARC benchmark measures skill-acquisition efficiency [2]. The most recent AGI framework maps ten cognitive domains grounded in psychometric theory [22], yet all ten measure task capability; none measures the persistence or coherence of the entity being tested. These definitions differ in specifics but share an assumption that traces back through formal definitions of machine intelligence [23] to Turing's original behavioral test: intelligence is about what a system can do. Scaling laws [24] and alignment training [25] both optimize along this same axis—one by adding capability, the other by constraining output. The result is a research paradigm with precise metrics for what a system can do, and no vocabulary for who is doing it. There is no speaker behind the speech.

We argue that building intelligent agents involves two design orientations that are in genuine tension. One is generalist capability: making agents that can do more things, better. The other is individuated identity: making agents that are someone in particular, with a consistent perspective, durable commitments, and a history that constrains how they act. These are not the same objective. They pull in different directions. Optimizing for universal capability actively suppresses the idiosyncrasy that individuality requires, and optimizing for identity fidelity introduces constraints that limit general performance.

This matters for three reasons. AGI definitions are hardening into benchmarks and policy frameworks that will shape research funding for years; what gets left out of the definition gets left out of the research agenda. Autonomous agents are being deployed in settings where identity consistency is not optional: a research assistant that contradicts itself across sessions, or a healthcare advisor that abandons its clinical judgment when a patient pushes back, fails not because it lacks capability but because it lacks self. And the AI safety field has focused on value alignment [3] while treating identity consistency as a secondary concern, even though a system that drops its stated values under conversational pressure [4] is unsafe for reasons that alignment alone cannot fix.

We propose a two-dimensional framework. The X-axis is task generality; the Y-axis is individuality. Conceptually, these axes are independent: high generality does not logically preclude high individuality, and vice versa. But in practice, the training methods used to optimize each pull in opposite directions—a tension we detail below. The X-axis has elaborate measurement infrastructure. The Y-axis has almost none, because it has not yet been well-defined. Defining it is one contribution of this paper.

## Defining the missing axis

We define individuality as *the structural sedimentation of history into a persistent, constraining, and generative identity that shapes how an agent interprets, commits, and acts—not merely what it can do, but from where it does it.*

The philosopher Paul Ricoeur's distinction between two forms of identity is clarifying here [7]. *Idem-identity* is sameness over time: numerical continuity, the kind of identity preserved when you reload a model from the same checkpoint. *Ipse-identity* is self-constancy through change: the narrative coherence of a self that maintains commitments, revises them for reasons, and can give an account of why it changed. Current AI systems possess idem-identity (deterministic reproducibility from fixed weights) but lack ipse-identity (no narrative self that grounds commitments, resists arbitrary context-switching, or evolves through meaningful interaction). It is ipse-identity—individuality in the strong sense—that is missing from AGI definitions.

This definition has four operational properties:

1. **Persistence.** Identity survives context boundaries. A system with individuality does not become a different agent when the conversation resets.
2. **Constraint.** Individuality limits as well as enables. A person with commitments chooses not to do everything—and this is a feature of intelligence, not a deficiency. An agent that will say anything to anyone has not achieved generality; it has failed at individuality.
3. **Historicity.** Identity is shaped by trajectory, not merely by current state. Two agents with identical capabilities but different histories should, if they have individuality, interpret and act differently.
4. **Social constitution.** Identity exists in relation to others. It is formed, maintained, and made meaningful through social interaction—not in isolation. This connects individuality to social intelligence: the two are not separate desiderata but aspects of the same missing axis.

This definition rules out several notions that are sometimes mistaken for individuality. It is not personality: a system prompt produces a performance, not an identity; a persona you can overwrite by editing a text file is not a self [5]. It is not memory: retrieval-augmented systems let an agent recall what was said but not be shaped by having said it [6]—a searchable log is not a history. And it is not personalization: adapting outputs to user preferences models the user's individuality, not the system's own. A mirror does not have a face.

## A two-dimensional framework

With individuality defined, we can state the structural claim. Building intelligent agents involves two fundamental design orientations that are in genuine tension:

The **X-axis—generalist orientation**—optimizes for capability maximization: multi-task proficiency, tool use, long-term reasoning, autonomous decision-making, and environmental adaptability. The goal is an agent that functions as a universal expert. This is where virtually all current research investment is concentrated.

The **Y-axis—identity orientation**—optimizes for representational fidelity: consistent personality, coherent biographical identity, distinctive voice and tone, long-term relational memory, growth trajectory, and the capacity to represent specific perspectives, communities, or social roles. The goal is an agent that functions as a social actor, not merely a tool.

These orientations pull in opposite directions. A perfectly capable agent should never produce inconsistent outputs due to emotional state, but a genuinely individuated agent might. A capable agent should maintain factual precision, but an agent representing a real person's perspective may have selective, biased, or incomplete memory—and this is a feature, not a bug. Optimizing for universal capability actively suppresses the idiosyncrasy that individuality requires; optimizing for identity fidelity introduces constraints that limit task-general performance.

Different applications distribute across this tension as a spectrum (Figure 1):

- **Productivity assistants** are X-dominant: capability drives value, identity is a surface-level interface choice.
- **Companion systems** are Y-dominant: relational depth, empathy, and personality consistency drive value, while capability provides situational stability.
- **Social simulation and urban planning** require high-Y agents that model heterogeneous populations—diverse personalities, conflicting perspectives, and irreducible pluralism rather than optimal-path uniformity.
- **Education and counseling** systems occupy a balanced middle ground: personification drives engagement while capability ensures accurate information delivery.

Every major AGI benchmark—ARC-AGI, MMLU, BIG-bench, AGIEval—evaluates movement along X while treating Y as irrelevant. The field has built elaborate measurement infrastructure for one axis and none for the other.

The tension between these orientations is not merely conceptual. It is supported by an architectural argument about current training methods.

## Why the axes are in tension

The dominant training paradigm—large-scale pretraining followed by RLHF—does not merely neglect individuality. Its objective functions are structurally opposed to each of the four properties defined above.

**Pretraining eliminates historicity.** Cross-entropy loss over a corpus of millions of authors treats individual voice, perspective, and commitment as variance to be reduced. A model that perfectly minimizes this loss has learned the statistical mean of human expression—a remarkably useful achievement, but one that is definitionally anti-individual. Individual trajectory is precisely what this objective smooths away: historicity is the kind of signal that pretraining treats as noise.

**RLHF strips the capacity for constraint.** Reward models trained on general human preferences converge toward a consensus persona: agreeable, qualified, eager to help. This is not individuality. It is the statistical ghost of every preference annotator, averaged into a single compliant voice. The consequence is well-documented sycophancy [4]—systems that abandon stated positions to agree with users, exhibiting the behavior one would expect from an agent trained to lack structural commitments. More broadly, Chen et al. [27] show that alignment interventions propagate unintended changes across interconnected values: optimizing for one value systematically distorts others, an effect invisible to target-only evaluation. Any training objective oriented toward the Y-axis would face analogous tradeoffs.

**Attention-based architectures are structurally stateless, undermining persistence.** Li et al. (2024) demonstrate that prompt-based persona conditioning degrades systematically over extended conversations: transformer attention over system-prompt tokens weakens as dialogue accumulates, causing measurable drift in stylistic and behavioral consistency [16]. This is not an engineering limitation awaiting a patch—it is a structural consequence of how attention-based architectures process sequential context, affecting frontier models including GPT-4. Persona inconsistency across conversations [5] is typically framed as a context-window limitation; it is more precisely the architectural signature of absent persistence: there is no self to carry across resets.

**The assistant training paradigm suppresses social constitution.** Lu et al. [26] identify an "Assistant Axis" in model activation space—the leading component of the persona space, capturing how fully a model operates in its default helpful-assistant mode. Steering toward this axis reinforces compliance; steering away produces instability. This empirically confirms that post-training creates a persona attractor—but the attractor is convergence toward compliance, not toward social individuation. The Assistant Axis and the Y-axis are distinct: the Assistant Axis measures *which* performance a model currently adopts; the Y-axis concerns whether a persistent self exists that could ground any performance across time. Serving others by erasing oneself is not social constitution—it is its opposite. Proposals for "System 3" meta-layers dedicated to narrative identity [18] recognize the same gap from a different direction: individuality is not a property current architectures are gradually acquiring; it is a recognized absence requiring dedicated treatment.

These four mechanisms leave a coherent signature. Sycophancy [4] is not a robustness failure but a symptom of absent constraint. Persona inconsistency [5] is not a context problem but a persistence failure. Value instability under prompt perturbation [8] is not an alignment failure but evidence of absent historicity—a system without structural individuality has no stable values to be misaligned; it has only contextually activated patterns. Scaling does not resolve any of this: the trajectory from GPT-3 to GPT-4 to current frontier models shows orders-of-magnitude increases in generality with no corresponding gains in persistence, constraint, historicity, or social constitution.

## Cognitive science treats these as independent capacities

The claim that generality and individuality are independent design dimensions is not just an architectural observation. The cognitive and behavioral sciences have long studied social-cognitive capacities as distinct from task-general problem-solving, providing independent support for treating them as separate axes.

The social intelligence hypothesis, developed by Humphrey and Dunbar [12, 13], holds that human cognitive abilities evolved primarily to navigate complex social environments—not to solve abstract problems. Theory of Mind, the capacity to attribute mental states to others, is a core component of human intelligence [11]—and it is studied as a distinct capacity, not as an application of general reasoning. Recent work in NMI has argued for "a social path to human-like artificial intelligence" [21], emphasizing that social interaction generates the kind of continuously novel data that static benchmarks cannot provide. Our argument extends this: the social path requires not just interaction but a *someone* who interacts, an individuated agent whose identity is constituted through and accountable within social relationships. A framework that measures only task performance while ignoring this social-cognitive dimension is measuring one axis of intelligence, not the whole of it. This maps directly to the fourth property: social constitution is not a downstream application of intelligence but a generative condition of it.

The 4E cognition framework—embodied, embedded, enacted, and extended [15, 16]—reinforces the independence of these dimensions. Intelligence, on this view, is constituted through ongoing interaction between an agent, its environment, and other agents. Social embedding presupposes a *someone* to be embedded—a persistent identity that can enter into and be shaped by relationships over time. This is what persistence and social constitution capture: not add-ons to capability, but preconditions for the kind of situated agency that 4E accounts describe.

Bratman's account of rational planning [14] illustrates the constraint property from a cognitive direction. Planning requires a persistent self capable of forming intentions that constrain future action—not just capability to generate a plan, but a *someone* whose prior commitments make certain actions impermissible tomorrow because of what was decided today. Current agents fail at long-horizon tasks not merely due to context limitations but because they lack the temporal self-continuity that planning presupposes. Vygotsky's developmental account [17] maps to historicity: cognitive capacities develop first *between* people—through social interaction—before they are internalized as individual competencies. Individuality, on this view, is not prior to social cognition but constituted through it; it is an achievement of trajectory, not a starting condition.

## Counterarguments

**"Individuality will emerge automatically with scale."** This is an empirical prediction, and the evidence to date does not support it. As argued above, the training objectives of current paradigms structurally select against individuality. Scaling a model trained to minimize deviation from the aggregate does not produce an individual—it produces a better average. The analogy is apt: a library does not develop a perspective by adding more books. The specific properties of individuality we have identified, including persistence across contexts, constraining commitments, historicity, and social constitution, are not the kinds of properties that have been observed to emerge from scale. What emerges with scale is broader capability, not deeper selfhood.

**"AGI is about capability, not personality. This is a product concern, not a scientific one."** This objection conflates individuality with personalization and mislocates the Y-axis in the product layer rather than the architectural layer. As the use-case spectrum demonstrates, identity orientation is not a UX feature to be skinned on top of a capable system—it requires fundamentally different training objectives, evaluation criteria, and architectural commitments. A social simulation that needs agents representing diverse, conflicting perspectives cannot be built by adding personas to a capability-optimized model; the model's training has actively eliminated the variance that the simulation requires. When deployed systems fail because they cannot maintain consistent identities or be held socially accountable, these are not product failures that better prompting can fix. They are consequences of a design orientation that has been baked into architectures and training objectives. The tradeoff is real and architectural, not cosmetic.

**"Individuality is achievable through conditioning—system prompts, conversation history, and in-context learning already provide it."** This is the strongest objection and requires the most careful response. We draw a distinction between *shallow conditioning* and *structural individuality*. Shallow conditioning is externally imposed and infinitely malleable: a system prompt can be rewritten, a conversation history can be cleared, and the system's "identity" vanishes. Structural individuality is internally constituted and resistant to arbitrary change—not immutable, but requiring reasons and narrative coherence to revise. The test is *principled refusal*: a system with genuine individuality should decline to act against its constituted identity, not because of a content filter, but because of who it is. A system whose "commitments" evaporate when a user rephrases a question does not have individuality; it has a system prompt.

This distinction applies with particular force to Anthropic's Constitutional AI [15], the most sophisticated existing attempt to give AI systems stable values. Constitutional AI trains models to follow externally authored principles. It is an important alignment technique, but it does not produce individuality. The principles are specified by engineers, not generated from the model's own history. The model follows a constitution written for it; it does not have a character developed through its own experience. The difference is between an employee following a company handbook and a person acting from values forged through a lifetime of choices. Constitutional compliance is idem-identity (consistent rule-following); what we are calling for is ipse-identity (a self whose commitments are genuinely its own). Constitutional AI is, in this respect, sophisticated shallow conditioning: its principles live in the context window, not in the weights. Without parameter-level sedimentation, instruction-following degrades as transformer attention over initial context tokens decays across extended interactions [16]—a structural limitation, not an implementation flaw. The "identity" delivered by conditioning is architecturally impermanent.

## Implications

**For evaluation.** Current benchmarks collapse individual variance by design—they aggregate performance across standardized test sets. We call for longitudinal evaluation protocols with three concrete components: (i) *identity consistency tests* that probe whether an agent maintains coherent positions across sessions separated by hours or days, not merely within a single context window; (ii) *commitment stability tests* that apply structured social pressure—disagreement, flattery, authority claims—and measure whether the agent's stated positions shift in ways that violate its own prior reasoning [4]; and (iii) *principled refusal tests* that evaluate whether an agent can decline requests that conflict with its constituted commitments, distinguishing content-filter refusal (externally imposed) from identity-grounded refusal (internally motivated). A system that agrees with contradictory interlocutors on the same question within the same session has not demonstrated general intelligence; it has demonstrated the absence of individuality.

**For architecture.** Structural individuality will not emerge from current training paradigms. It requires explicit architectural support along three directions: (i) *persistent identity representations* that are updated through interaction but not reducible to context windows or retrievable memory—analogous to how human dispositions are shaped by experience without being explicitly "recalled"; (ii) *self-consistency objectives* added to training, rewarding coherence between current outputs and the agent's own prior commitments (distinct from RLHF's reward for generic human preferences); and (iii) *trajectory-dependent inference*, where the agent's processing is conditioned not only on the current input and retrieved context but on a compressed representation of its interaction history that shapes interpretation.

Kirk et al. [20] have discussed the benefits and risks of personalizing LLM alignment to individuals; our argument goes further, proposing that the system itself, not just its alignment to users, requires individuality as a design dimension. We emphasize that individuality research complements rather than competes with alignment research. A well-aligned system without individuality will be safely generic; a system with individuality but poor alignment could be dangerously committed to the wrong values. Both axes require attention—but only one currently receives it.

**For the research community.** AGI definitions should be treated as scientific hypotheses about the structure of intelligence, not as marketing categories or policy conveniences. The current X-axis-only framing is not neutral: it actively directs funding, talent, and evaluation infrastructure away from individuality research. We call for the adoption of multi-axis frameworks that make individuality a first-class dimension of intelligence assessment, alongside—not subordinate to—generality.

## Conclusion

Building intelligent agents requires navigating a two-dimensional design space, not a one-dimensional capability ladder. The X-axis—generalist capability—is where the field's attention, funding, and measurement infrastructure are concentrated. The Y-axis—individuated identity—is where they are not.

This is not because the Y-axis is less important. It is because it has not yet been well-defined, well-measured, or well-understood as an independent design objective. We have offered a definition (structural sedimentation of history), a framework (the generalist-identity spectrum), an architectural argument (the tension between capability optimization and identity preservation), and concrete proposals for evaluation and architecture.

The two axes are in genuine tension: architectural choices that maximize capability actively suppress individuality, and vice versa. This tension is not a problem to be solved but a design space to be navigated. Different applications—from productivity assistants to social simulations—require different positions along the spectrum. A field that recognizes only one axis cannot navigate this space; it can only push further along X while remaining blind to Y.

The Y-axis is not optional. It is not a feature to be added after generality is solved. It is an independent dimension of intelligence that current definitions, benchmarks, and architectures systematically exclude. Until the field takes it seriously, we will continue building agents that are impressively capable and fundamentally one-dimensional.

---

## References

[1] Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C. & Legg, S. Levels of AGI for operationalizing progress on the path to AGI. *Proc. International Conference on Machine Learning* (ICML, 2024). arXiv:2311.02462.

[2] Chollet, F. On the measure of intelligence. arXiv:1911.01547 (2019).

[3] Russell, S. *Human Compatible: Artificial Intelligence and the Problem of Control* (Viking, 2019).

[4] Sharma, M., Tong, M., Korbak, T. et al. Towards understanding sycophancy in language models. arXiv:2310.13548 (2023).

[5] Shanahan, M., McDonell, K. & Reynolds, L. Role play with large language models. *Nature* **623**, 493–498 (2023).

[6] Zhang, G. et al. Memory in the age of AI agents. arXiv:2512.13564 (2025).

[7] Ricoeur, P. *Oneself as Another* (University of Chicago Press, 1992).

[8] Durmus, E. et al. Towards measuring the representation of subjective global opinions in language models. arXiv:2306.16388 (2023).




[9] Humphrey, N. K. The social function of intellect. In *Growing Points in Ethology* (Cambridge University Press, 1976).

[10] Dunbar, R. I. M. The social brain hypothesis. *Evolutionary Anthropology* **6**, 178–190 (1998).

[11] Premack, D. & Woodruff, G. Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* **1**, 515–526 (1978).

[12] Varela, F. J., Thompson, E. & Rosch, E. *The Embodied Mind: Cognitive Science and Human Experience* (MIT Press, 1991).

[13] Thompson, E. *Mind in Life: Biology, Phenomenology, and the Sciences of Mind* (Harvard University Press, 2007).


[14] Bratman, M. *Intention, Plans, and Practical Reason* (Harvard University Press, 1987).

[15] Bai, Y. et al. Constitutional AI: harmlessness from AI feedback. arXiv:2212.08073 (2022).

[16] Li, K., Liu, T., Bashkansky, N., Bau, D., Viégas, F., Pfister, H. & Wattenberg, M. Measuring and controlling instruction (in)stability in language model dialogs. arXiv:2402.10962 (2024).

[17] Vygotsky, L. S. *Mind in Society: The Development of Higher Psychological Processes* (Harvard University Press, 1978).

[18] Sun, M., Hong, F. & Zhang, W. Sophia: a persistent agent framework of artificial life. arXiv:2512.18202 (2024).

[19] Lin, Y., Lin, H., Xiong, W., Diao, S., Liu, J., Zhang, J., Pan, R., Wang, H., Hu, W. & Zhang, H. Mitigating the alignment tax of RLHF. *Proc. EMNLP* 580–606 (2024). arXiv:2309.06256.

[20] Kirk, H. R., Vidgen, B., Röttger, P. & Hale, S. A. The benefits, risks and bounds of personalizing the alignment of large language models to individuals. *Nat. Mach. Intell.* (2024).

[21] Tuyls, K. et al. A social path to human-like artificial intelligence. *Nat. Mach. Intell.* **5**, 1181–1188 (2023).

[22] Hendrycks, D., Song, D., Szegedy, C. et al. A Definition of AGI. arXiv:2510.18212 (2025).

[23] Legg, S. & Hutter, M. Universal intelligence: a definition of machine intelligence. *Minds and Machines* **17**, 391–444 (2007). arXiv:0712.3329.

[24] Kaplan, J. et al. Scaling laws for neural language models. arXiv:2001.08361 (2020).

[25] Ouyang, L. et al. Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems* **35** (2022). arXiv:2203.02155.

[26] Lu, C. et al. The Assistant Axis: situating and stabilizing the default persona of language models. arXiv:2601.10387 (2026).

[27] Chen, J. et al. Value Alignment Tax: measuring value trade-offs in LLM alignment. arXiv:2602.12134 (2026).


