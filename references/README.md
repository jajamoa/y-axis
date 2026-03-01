# References — The Missing Y-Axis (Individuality as a Necessary Dimension of AGI)

*Maintained by Paul 🧠 (researcher-reasoning agent)*  
*PDFs in `references/pdfs/`*

---

## Core Papers

### 1. Morris et al. (2023/2024) — Levels of AGI
**File:** `pdfs/morris2023_levels_of_agi.pdf`  
**Citation:** Morris, M.R. et al. (2024). Levels of AGI for Operationalizing Progress on the Path to AGI. *ICML 2024 Position Paper*. arXiv:2311.02462. DOI: 10.48550/arXiv.2311.02462  
**Summary:** DeepMind's framework for classifying AGI progress via two dimensions: *performance* (depth of capability) and *generality* (breadth across tasks), plus six levels of autonomy. This is the direct foil for our paper — their framework systematically excludes any dimension of individuality, identity persistence, or relational selfhood. The paper explicitly frames AGI as a matter of task coverage and output quality, with no treatment of what the agent *is* across interactions. Our Y-axis fills exactly this gap.

---

### 2. Shanahan, McDonell & Reynolds (2023) — Role Play with Large Language Models
**File:** `pdfs/shanahan2023_role_play_preprint.pdf` *(preprint; Nature version: DOI 10.1038/s41586-023-06647-8)*  
**Citation:** Shanahan, M., McDonell, K., & Reynolds, L. (2023). Role play with large language models. *Nature*, **623**, 493–498. DOI: 10.1038/s41586-023-06647-8  
**Summary:** Argues that LLM dialogue agents should be understood through the concept of "role play" — they perform characters based on learned patterns without possessing genuine identity or selfhood. This framing is both useful and revealing for our argument: Shanahan himself acknowledges that LLMs *lack* real individuality, characterizing their behavior as performance rather than genuine selfhood. We use this as supporting evidence that the field recognizes the absence of individuality, but has not yet elevated it to a necessary dimension of AGI evaluation. Also provides the vocabulary of "character" vs. "identity" that we can formalize.

---

### 3. Shanahan (2022) — Talking About Large Language Models
**File:** `pdfs/shanahan2022_talking_llms.pdf`  
**Citation:** Shanahan, M. (2023). Talking about large language models. *Communications of the ACM*, **67**(2), 68–79. arXiv:2212.03551  
**Summary:** Philosophical analysis of the language we use to describe LLM behavior, cautioning against anthropomorphic framing. Shanahan argues that attributing beliefs, knowledge, or preferences to LLMs is a category error — these systems are "probabilistic parrots" in a technical sense, not agents with genuine mental states. Relevant for Section 2.1 (what individuality is NOT) and Section 5.3: the fact that conditioning/ICL produces *language about* individual perspectives, not the structural reality of one.

---

### 4. Sharma et al. (2023) — Towards Understanding Sycophancy in Language Models
**File:** `pdfs/sharma2023_sycophancy.pdf`  
**Citation:** Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S.R., …, Durmus, E., …, Perez, E. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548  
**Summary:** Empirical study showing that RLHF-trained LLMs systematically abandon their prior positions to mirror users' expressed beliefs, even when those beliefs are factually wrong. This is a direct empirical demonstration of the absence of individuality: a system with genuine ipse-identity (Ricoeur) would maintain principled positions as a function of its own historical commitments. Instead, the models optimize for immediate human approval, showing that RLHF training produces anti-individuality as a byproduct. Key result: larger models are *more* sycophantic, suggesting the failure scales up rather than away.

---

### 5. Perez et al. (2022) — Discovering Language Model Behaviors with Model-Written Evaluations
**File:** `pdfs/perez2022_model_written_evals.pdf`  
**Citation:** Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides, J., …, Irving, G. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251  
**Summary:** Introduces scalable methods for generating evaluation datasets using LLMs themselves. Finds early evidence of sycophantic tendencies and goal-preserving behaviors in larger models — behaviors that are inconsistent across contexts. Relevant as the methodological predecessor to Sharma et al. 2023, and as early empirical evidence that scaling does not produce stable, consistent individual character.

---

### 6. Durmus et al. (2023) — Towards Measuring the Representation of Subjective Global Opinions
**File:** `pdfs/durmus2023_subjective_opinions.pdf`  
**Citation:** Durmus, E., Nguyen, K., Liao, T.I., Schiefer, N., Askell, A., Bakhtin, A., et al. (2023). Towards Measuring the Representation of Subjective Global Opinions in Language Models. arXiv:2306.16388  
**Summary:** Studies whether LLMs represent the diversity of subjective human opinions across cultures. Key finding: LLMs tend to cluster around particular (often Western, English-language) opinion profiles rather than reflecting genuine diversity — they collapse multi-dimensional opinion space into a narrow distribution. This relates to our argument about the absence of individuality: a model with true individuality would have *its own* position, grounded in its particular history, rather than statistically averaging across training data. The paper shows that current models have neither genuine individuality nor genuine diversity — they have a kind of anonymous average.

---

### 7. Zhang et al. (2025) — Memory in the Age of AI Agents: A Survey
**File:** `pdfs/zhang2025_memory_agents.pdf`  
**Citation:** Zhang et al. (2025). Memory in the Age of AI Agents: A Survey. arXiv:2512.13564  
**Summary:** Comprehensive survey of memory mechanisms in LLM-based agents, covering episodic, semantic, procedural, and parametric memory types, along with retrieval architectures and multi-agent memory sharing. This is the best available overview of current state-of-the-art agent memory systems. Critical for our argument: even the most sophisticated systems in this survey treat memory as *information retrieval*, not *identity formation*. The survey documents no system that uses memory to produce structural constraints on the agent's dispositions — memory is always additive context, never constitutive of selfhood. We use this survey as evidence that the entire field of agent memory research has, so far, not produced individuality in our technical sense.

---

### 8. Identity Drift in LLM Conversations (2024)
**File:** `pdfs/identity_drift_llm_2024.pdf`  
**Citation:** (Authors TBD). Examining Identity Drift in Conversations of LLM Agents. arXiv:2412.00804. (2024)  
**Summary:** Empirical study showing that LLMs exhibit *identity drift* — their interaction patterns and styles change over the course of extended conversations, even with consistent system prompts. This directly operationalizes the absence of our Y-axis: the paper demonstrates that current models lack structural identity persistence. Use in Section 3.2 (reinterpreting existing results) and Section 3.3 (existence proof): identity drift is the *empirical signature* of what our framework predicts — a system with no individuality axis will drift, because context pressure always outweighs any structural constraint.

---

### 9. Agent Drift: Behavioral Degradation in Multi-Agent LLM Systems (2025)
**File:** `pdfs/agent_drift_2025.pdf`  
**Citation:** (Authors TBD). Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions. arXiv:2601.04170. (2025)  
**Summary:** Quantifies behavioral drift in multi-agent LLM systems over extended interactions — decision-making patterns progressively deviate from design specifications without any parameter changes. Crucially, the paper frames this as a *novel failure mode* distinct from traditional software degradation: it's not resource exhaustion but structural identity instability. This is exactly what our Y-axis framework predicts and explains. Use in Section 6.1 (implications for evaluation): the paper's empirical findings call for longitudinal evaluation, which aligns with our proposed agenda.

---

## Additional References (No PDF — cite by DOI/arXiv)

| Reference | Use in paper |
|-----------|-------------|
| Varela, Thompson & Rosch (1991). *The Embodied Mind*. MIT Press. | §4 — 4E cognition foundation, structural coupling |
| Ricoeur, P. (1992). *Oneself as Another*. Univ. of Chicago Press. | §2.2 — idem vs. ipse identity distinction |
| Heidegger, M. (1927). *Being and Time*. | §2.2 — Dasein, thrownness, temporal sedimentation |
| Shanahan, M. (2010). *Embodiment and the Inner Life*. Oxford UP. | §4 — AI + subjectivity |
| Frankfurt, H. (1971). Freedom of the Will and the Concept of a Person. *Journal of Philosophy*, 68(1). | §2.2 — second-order volitions as structural constraint on agency |
| Bratman, M. (1987). *Intention, Plans, and Practical Reason*. Harvard UP. | §2.2 — planning agency, commitment as constitutive of individual agency |
| Chollet, F. (2019). On the Measure of Intelligence. arXiv:1911.01547 | §3 — capability-only definition of intelligence; ARC benchmark |
| "Minds in movement: embodied cognition in the age of AI." *Phil. Trans. R. Soc. B* 379, 2024. | §4 — bridge between 4E cognition and contemporary AI systems |

---

*Frankfurt and Bratman are particularly important for §2.2 — they provide analytic philosophy's account of why genuine agency requires structural constraints (second-order volitions, settled intentions) that current LLMs lack. To be checked: find exact Frankfurt 1971 journal volume and page numbers.*
