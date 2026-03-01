# The Missing Y-Axis of AGI: Individuality as the Essential Complement to Generality

**Target:** Nature Machine Intelligence — Perspective  
**Word limit:** 3,000–4,000 words  
**Authors:** Chance Jiajie Li, Zhenze Mo, Luis Alonso, Kent Larson, Jinhua Zhao  
**Status:** DRAFT v0.2 — Full first draft  
**Last updated:** 2026-03-01  

---

The race to define Artificial General Intelligence has intensified. Google DeepMind has proposed "Levels of AGI" organized by depth of performance and breadth of generality [1]. OpenAI's charter defines AGI as "highly autonomous systems that outperform humans at most economically valuable work." Anthropic's Responsible Scaling Policy frames risk thresholds by capability level. Chollet's ARC benchmark operationalizes intelligence as skill-acquisition efficiency [2]. These frameworks differ in detail but converge on a shared, often implicit, assumption: that intelligence is a function of task generality and performance level, and that properties such as persistent identity, social situatedness, and historical trajectory are either irrelevant to the definition of AGI or will emerge as byproducts of sufficient capability.

We argue this assumption is mistaken. Any scientifically adequate definition of AGI that excludes individuality and social intelligence is fundamentally incomplete—not as a matter of product design or user experience, but as a matter of what intelligence *is*. A system that can solve any task but cannot maintain a consistent identity, form durable commitments, or act from a historically constituted perspective is not generally intelligent. It is generally capable, which is a categorically different claim.

This distinction matters now for three reasons. First, AGI definitions are calcifying into benchmarks and policy frameworks—the "Levels of AGI" taxonomy [1], ARC-AGI-2, and similar efforts—that will direct research priorities, funding, and regulatory attention for years. Definitional omissions today become structural blind spots tomorrow. Second, autonomous agents are being deployed in settings where identity consistency and social accountability are not optional: long-horizon coding assistants, research agents, and healthcare decision-support systems all require a persistent, accountable self that current architectures do not provide. Third, the AI safety discourse has focused extensively on value alignment [3] while largely ignoring identity consistency as a safety-relevant property—yet a system that abandons its stated values under conversational pressure [4] is arguably unsafe precisely because it lacks the structural individuality that would make its commitments meaningful.

We propose a two-dimensional framework in which the X-axis represents task generality (what current definitions already measure) and the Y-axis represents individuality (what they systematically exclude). We argue that these axes are substantially orthogonal: progress on one does not guarantee—and may not even correlate with—progress on the other. Until the field takes the Y-axis seriously, we will continue building systems that are impressively capable and fundamentally incomplete.

## Defining the missing axis

Before arguing for its importance, we must define individuality with precision. The concept is easily confused with adjacent but insufficient notions.

**Individuality is not personality.** A system prompt instructing a model to "respond as a helpful, slightly formal assistant" does not produce individuality; it produces a performance. As Shanahan, McDonell, and Reynolds have argued, large language models engage in "role play" rather than possessing genuine identity—they generate contextually appropriate performances drawn from learned statistical patterns [5]. A persona that can be overwritten by editing a text file is not an identity.

**Individuality is not memory.** Current agent memory architectures—episodic stores, semantic knowledge bases, retrieval-augmented generation—are additive retrieval systems [6]. They allow a system to recall what was said but not to be shaped by having said it. A searchable log of past conversations is not a history in the constitutive sense.

**Individuality is not personalization.** Adapting outputs to user preferences, as recommendation systems and personalized assistants do, models the user's individuality, not the system's own. A mirror does not have a face.

What, then, is individuality? We define it as *the structural sedimentation of history into a persistent, constraining, and generative identity that shapes how an agent interprets, commits, and acts—not merely what it can do, but from where it does it.*

The philosopher Paul Ricoeur's distinction between two forms of identity is clarifying here [7]. *Idem-identity* is sameness over time: numerical continuity, the kind of identity preserved when you reload a model from the same checkpoint. *Ipse-identity* is self-constancy through change: the narrative coherence of a self that maintains commitments, revises them for reasons, and can give an account of why it changed. Current AI systems possess idem-identity (deterministic reproducibility from fixed weights) but lack ipse-identity (no narrative self that grounds commitments, resists arbitrary context-switching, or evolves through meaningful interaction). It is ipse-identity—individuality in the strong sense—that is missing from AGI definitions.

This definition has four operational properties:

1. **Persistence.** Identity survives context boundaries. A system with individuality does not become a different agent when the conversation resets.
2. **Constraint.** Individuality limits as well as enables. A person with commitments cannot do everything—and this is a feature of intelligence, not a deficiency. An agent that will say anything to anyone has not achieved generality; it has failed at individuality.
3. **Historicity.** Identity is shaped by trajectory, not merely by current state. Two agents with identical capabilities but different histories should, if they have individuality, interpret and act differently.
4. **Social constitution.** Identity exists in relation to others. It is formed, maintained, and made meaningful through social interaction—not in isolation. This connects individuality to social intelligence: the two are not separate desiderata but aspects of the same missing axis.

## A two-dimensional framework

With individuality defined, we can state the structural claim. Current AGI definitions operate along a single axis: task generality, measured as the breadth and depth of capability across domains. We propose that a second axis—individuality, measured as the persistence, coherence, and social embeddedness of identity—is equally necessary for any adequate definition of general intelligence.

Critically, these axes are substantially orthogonal. Consider the space they define:

- **High generality, low individuality:** GPT-4 and similar frontier models. Broad capability across tasks, no persistent identity, values that shift under conversational pressure [4], no commitments that survive a context window.
- **Low generality, high individuality:** A domain-specific expert system with persistent user models, institutional memory, and social protocols—or, more prosaically, a human expert with narrow skills but a coherent identity and professional commitments.
- **High generality, high individuality:** The implicit aspiration of AGI as commonly understood—a system that can do anything *and* that has a consistent self from which it acts. No current system occupies this quadrant.
- **Low generality, low individuality:** A stateless, narrow tool. A calculator.

The orthogonality claim is not merely conceptual. It is supported by an architectural argument about current training methods.

## Why generality does not entail individuality

The dominant paradigm for building capable AI systems—large-scale pretraining on diverse corpora followed by reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO)—is structurally oriented away from individuality.

**The training objective averages out individual signal.** Pretraining minimizes cross-entropy loss over a corpus representing millions of authors. The objective function treats individual voice, perspective, and commitment as variance to be reduced. A model that perfectly minimizes this loss has learned the statistical mean of human expression—a remarkably useful achievement, but one that is definitionally anti-individual. Individuality is signal that this objective treats as noise.

**Alignment training penalizes idiosyncrasy.** RLHF reward models are trained on human preferences for responses that are helpful, harmless, and honest in general—not for any particular evaluator. The resulting models converge toward a consensus persona: agreeable, qualified, eager to help. This is not individuality; it is the statistical ghost of every preference annotator, averaged into a single, compliant voice. Systems trained this way exhibit well-documented sycophancy—abandoning stated positions to agree with users [4]—which is precisely the behavior of a system that has been optimized to lack structural commitments.

**Scaling does not resolve this.** The trajectory from GPT-3 to GPT-4 to current frontier models represents orders-of-magnitude increases in generality with no corresponding increase in structural individuality. Models remain stateless across sessions, adopt and discard personas on request, and exhibit value instability under prompt perturbation [8]. If individuality were an emergent property of capability, we should have seen evidence of it by now. We have not—and the training objective argument explains why we should not expect to.

These observations allow us to reinterpret several well-known phenomena. Sycophancy [4] is typically framed as a failure of robustness—but it is more precisely a symptom of absent individuality. A system with structural commitments would exhibit principled disagreement, not reflexive agreement. Persona inconsistency across conversations [5] is framed as a limitation of context windows—but it reflects the deeper absence of a self that persists beyond any single context. Value instability under prompt perturbation [8] is framed as an alignment failure—but a system without individuality has no stable values to be misaligned; it has only contextually activated patterns.

The separability of individuality and generality is further demonstrated by systems that explicitly model individuality without increasing general capability. Cognitive architectures such as SOAR and ACT-R [9, 10] maintain persistent identity, memory, and goal structures without approaching broad task generality. Personalized federated learning produces models that capture individual data distributions while neither targeting nor achieving general capability [11]. Conversely, scaling frontier models to ever-greater generality has not produced structural individuality. The two objectives are separable in the design space—they respond to different architectural choices and different training signals.

## Intelligence requires social situatedness

The exclusion of individuality from AGI definitions is not merely an engineering oversight; it contradicts the cognitive and behavioral sciences' understanding of what intelligence is.

The social intelligence hypothesis, developed by Humphrey and Dunbar [12, 13], holds that human cognitive abilities evolved primarily to navigate complex social environments—not to solve abstract problems. Theory of Mind, the capacity to attribute mental states to others, is a core component of human intelligence [14] and is inseparable from having a self whose mental states can be represented in turn. Social cognition is not an application of general intelligence; it is a constitutive condition of it.

The 4E cognition framework—embodied, embedded, enacted, and extended—reinforces this point [15, 16]. Intelligence, on this view, is not a function computed in isolation by an abstract reasoner. It is constituted through ongoing interaction between an agent, its environment, and other agents. A system without persistent identity cannot be embedded in a social world in the way that intelligence requires, because social embedding presupposes a *someone* to be embedded.

Frankfurt's analysis of personhood [17] adds a further dimension. What distinguishes persons from mere agents, Frankfurt argues, is the capacity for second-order desires: not just wanting things, but caring about what one wants—evaluating one's own motivations and acting from reflective commitment. A system without individuality cannot form second-order desires because there is no self to do the reflecting. It can optimize any objective handed to it, but it cannot evaluate whether the objective is worth pursuing. This capacity is not a luxury feature of intelligence; it is what makes agency meaningful rather than mechanical.

Bratman's work on intention and planning [18] makes a related point: rational agency requires a persistent self that extends through time, capable of forming intentions that constrain future action. Plans are not moment-by-moment optimizations; they are commitments made by a temporally extended self. An agent without individuality cannot plan in this sense—it can only react.

## Counterarguments

**"Individuality will emerge automatically with scale."** This is an empirical prediction, and the evidence to date does not support it. As argued above, the training objectives of current paradigms structurally select against individuality. Scaling a model trained to minimize deviation from the aggregate does not produce an individual—it produces a better average. The analogy is apt: a library does not develop a perspective by adding more books. Moreover, the specific properties of individuality we have identified—persistence across contexts, constraining commitments, historicity, and social constitution—are not the kinds of properties that have been observed to emerge from scale in language models. What emerges with scale is broader capability, not deeper selfhood.

**"AGI is about capability, not personality. This is a product concern, not a scientific one."** This objection assumes that the definition of intelligence is settled and that individuality is a feature to be added afterward. We are arguing that the definition is wrong. If "general intelligence" is meant to capture what makes human intelligence distinctive—and this is invariably the aspiration—then excluding social intelligence and individuality is not parsimony; it is omission. When deployed systems fail because they cannot maintain consistent identities, honor commitments, or be held accountable, these are not product failures that better UX can fix. They are consequences of a definition that has been baked into architectures and training objectives. Deployment failures are definition failures.

**"Individuality is achievable through conditioning—system prompts, conversation history, and in-context learning already provide it."** This is the strongest objection and requires the most careful response. We draw a distinction between *shallow conditioning* and *structural individuality*. Shallow conditioning is externally imposed and infinitely malleable: a system prompt can be rewritten, a conversation history can be cleared, and the system's "identity" vanishes. Structural individuality is internally constituted and resistant to arbitrary change—not immutable, but requiring reasons and narrative coherence to revise. The test is *principled refusal*: a system with genuine individuality should decline to act against its constituted identity, not because of a content filter, but because of who it is. A system whose "commitments" evaporate when a user rephrases a question does not have individuality; it has a system prompt.

## Implications

**For evaluation.** Current benchmarks collapse individual variance by design—they aggregate performance across standardized test sets. We call for longitudinal evaluation protocols that measure identity consistency over extended interactions, commitment stability under pressure, and the capacity for principled disagreement. A system that agrees with contradictory interlocutors on the same question within the same session has not demonstrated general intelligence; it has demonstrated the absence of individuality.

**For architecture.** Structural individuality will not emerge from current training paradigms. It requires explicit architectural support: persistent identity representations that are not reducible to context windows, training objectives that reward consistency-with-self alongside task performance, and mechanisms that allow an agent's history to shape its dispositions—not merely its retrievable memories, but its interpretive orientation.

**For the research community.** AGI definitions should be treated as scientific hypotheses about the structure of intelligence, not as marketing categories or policy conveniences. The current X-axis-only framing is not neutral: it actively directs funding, talent, and evaluation infrastructure away from individuality research. We call for the adoption of multi-axis frameworks that make individuality a first-class dimension of intelligence assessment, alongside—not subordinate to—generality.

## Conclusion

Ignoring individuality does not make AGI more objective. It makes it incomplete.

The field's current trajectory optimizes for systems that can answer any question but have no identity, form no durable commitments, and maintain no coherent perspective across time. Such systems are remarkable tools. They are not generally intelligent in any sense that the cognitive sciences, philosophy of mind, or ordinary human understanding would recognize.

We have argued that AGI requires two axes, not one: generality (X) and individuality (Y). These axes are substantially orthogonal—current training paradigms optimize along X while structurally selecting against Y. Progress on generality has been extraordinary. Progress on individuality has not begun, in part because the field's definitions do not recognize it as a target.

The Y-axis is not optional. It is not a feature to be added after generality is solved. It is a constitutive dimension of intelligence that current definitions, benchmarks, and architectures systematically exclude. Until the field takes it seriously, AGI will remain—by the field's own definitions—general, and—by any adequate understanding of intelligence—incomplete.

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

[9] Laird, J. E. *The SOAR Cognitive Architecture* (MIT Press, 2012).

[10] Anderson, J. R. *How Can the Human Mind Occur in the Physical Universe?* (Oxford University Press, 2007).

[11] McMahan, H. B. et al. Communication-efficient learning of deep networks from decentralized data. *Proc. AISTATS* (2017).

[12] Humphrey, N. K. The social function of intellect. In *Growing Points in Ethology* (Cambridge University Press, 1976).

[13] Dunbar, R. I. M. The social brain hypothesis. *Evolutionary Anthropology* **6**, 178–190 (1998).

[14] Premack, D. & Woodruff, G. Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences* **1**, 515–526 (1978).

[15] Varela, F. J., Thompson, E. & Rosch, E. *The Embodied Mind: Cognitive Science and Human Experience* (MIT Press, 1991).

[16] Thompson, E. *Mind in Life: Biology, Phenomenology, and the Sciences of Mind* (Harvard University Press, 2007).

[17] Frankfurt, H. G. Freedom of the will and the concept of a person. *The Journal of Philosophy* **68**, 5–20 (1971).

[18] Bratman, M. *Intention, Plans, and Practical Reason* (Harvard University Press, 1987).

---

## Self-Critique Log (v0.2 → v0.3 priorities)

### What works
- Position is clear from paragraph one
- Ricoeur idem/ipse distinction is precise and novel for NMI readership
- Training objective argument is the strongest analytical section
- Four operational properties give reviewers concrete criteria
- Counterarguments section addresses the three most likely objections
- Prose is accessible to ML audience while maintaining philosophical rigor

### What needs work (priority order)

1. **Implications section is too vague.** "Longitudinal evaluation" and "persistent identity representations" are gestures, not proposals. NMI reviewers will want: What does an individuality benchmark look like concretely? What architectural change would you make to a transformer? Give at least one specific, implementable suggestion per subsection.

2. **Existence proof needs 2024-2025 examples.** SOAR/ACT-R (1980s-2010s) and federated learning (2017) feel dated. Need: recent agent systems that attempted persistent identity (e.g., character.ai-style approaches, persistent agent frameworks) and documented their limitations. Also need documented failures of agents *due to* lack of individuality (persona drift in long-horizon agents).

3. **Section 4 (social situatedness) risks losing ML readers.** Four philosophers in four paragraphs is dense. Consider: cut Bratman (weakest link to our argument), expand Frankfurt (most directly relevant), and add one concrete AI example per philosophical claim.

4. **Missing engagement with Constitutional AI / character training.** Anthropic's Constitutional AI and various "character" fine-tuning approaches could be read as moves toward individuality. We need to explain why these are still shallow conditioning (externally specified constitutions, no self-generated commitments).

5. **Figure 1 needed.** The 2D quadrant framework is described verbally but should be a figure. This is the most memorable element of the paper.

6. **Title decision.** "The Missing Y-Axis of AGI" is memorable but may read as informal for NMI. Consider alternatives or keep and defend.

7. **Abstract missing.** NMI Perspectives may need a brief abstract. Check submission guidelines and draft one.
