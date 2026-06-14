# StructAI — An LLM-Powered Multi-Agent System for Automated Software Architecture Design and Education

### A Project Report (Black Book)

**Submitted in partial fulfillment of the requirements for the award of the degree of**

### Bachelor of Engineering
### in
### Artificial Intelligence and Machine Learning

**Submitted by:**

| Roll No. | Name |
|---|---|
| — | Akshat D. More |
| — | Narendra B. Tekale |
| — | Yash D. Thakare |
| — | Neha B. Yengandul |

**Under the guidance of:**
**Prof. \<Guide Name\>**
Department of Artificial Intelligence and Machine Learning

---

### Department of Artificial Intelligence and Machine Learning
### PES's Modern College of Engineering, Pune
### Savitribai Phule Pune University
### Academic Year 2025 – 2026

---

## CERTIFICATE

This is to certify that the project report entitled **"StructAI — An LLM-Powered Multi-Agent System for Automated Software Architecture Design and Education"** submitted by **Akshat D. More**, **Narendra B. Tekale**, **Yash D. Thakare**, and **Neha B. Yengandul** is a record of bonafide work carried out by them, in partial fulfillment of the requirement for the award of the degree of Bachelor of Engineering in Artificial Intelligence and Machine Learning of Savitribai Phule Pune University, during the academic year 2025–2026.

<br>

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**
Prof. \<Guide Name\> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Prof. \<HoD Name\>
Project Guide &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Head of Department
Department of AI & ML &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Department of AI & ML

<br>

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**
Internal Examiner &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; External Examiner

Place: Pune
Date: \_\_\_\_\_\_\_\_\_\_\_\_

---

## DECLARATION

We hereby declare that the project work entitled **"StructAI — An LLM-Powered Multi-Agent System for Automated Software Architecture Design and Education"** submitted to PES's Modern College of Engineering, Pune, affiliated to Savitribai Phule Pune University, is a record of original work done by us under the guidance of **Prof. \<Guide Name\>**, Department of Artificial Intelligence and Machine Learning. This project work has not been submitted to any other university or institute for the award of any degree or diploma.

<br>

| Name | Signature |
|---|---|
| Akshat D. More | \_\_\_\_\_\_\_\_\_\_\_ |
| Narendra B. Tekale | \_\_\_\_\_\_\_\_\_\_\_ |
| Yash D. Thakare | \_\_\_\_\_\_\_\_\_\_\_ |
| Neha B. Yengandul | \_\_\_\_\_\_\_\_\_\_\_ |

Place: Pune
Date: \_\_\_\_\_\_\_\_\_\_\_\_

---

## ACKNOWLEDGEMENT

It gives us immense pleasure to present this project report on **"StructAI — An LLM-Powered Multi-Agent System for Automated Software Architecture Design and Education"**. We express our deep sense of gratitude to our project guide **Prof. \<Guide Name\>**, Department of Artificial Intelligence and Machine Learning, for the valuable guidance, constructive criticism, and continuous encouragement throughout the course of this work. Their technical insight into Large Language Models, retrieval-augmented generation, and software architecture design shaped the direction of this project.

We are sincerely thankful to **Prof. \<HoD Name\>**, Head of the Department of AI & ML, and **Dr. \<Principal Name\>**, Principal of PES's Modern College of Engineering, Pune, for providing the necessary infrastructure and conducive academic environment.

We thank the faculty members of the Department of AI & ML for their valuable suggestions during project reviews. We also acknowledge the broader open-source community — the maintainers of LangGraph, LangChain, FAISS, Next.js, FastAPI, and React Flow — whose work forms the technical foundation of this project.

Finally, we thank our families and friends for their unwavering support and patience throughout the duration of this work.

| | |
|---|---|
| | **Akshat D. More** |
| | **Narendra B. Tekale** |
| | **Yash D. Thakare** |
| | **Neha B. Yengandul** |

---

## ABSTRACT

Software architecture design is a knowledge-intensive activity that demands expertise in distributed systems, scalability principles, and domain-specific design patterns — expertise that junior engineers and undergraduate students frequently lack. Existing tools such as Lucidchart and draw.io require manual placement of components, while general-purpose code assistants like GitHub Copilot and ChatGPT generate prose descriptions without machine-readable graph output. None bridge the gap between automated design generation, grounded retrieval from real-world architectural patterns, and pedagogical explanation in a single platform.

This project presents **StructAI**, a full-stack, production-grade web application that automates software architecture design through a multi-agent Large Language Model (LLM) pipeline. Given a free-text problem statement, StructAI orchestrates a four-node LangGraph state machine — *requirement extraction → ambiguity clarification → retrieval-augmented generation → architecture synthesis* — to produce a complete architecture as an interactive React Flow graph. A locally persisted FAISS vector store, seeded with 25 curated real-world architecture patterns (Netflix, Uber, Discord, Twitter, etc.), supplies the generation agent with grounding context, reducing hallucination compared to prompt-only baselines. An on-demand explainability engine decomposes every generated component into its rationale, alternatives, trade-offs, and a "learn more" pointer. A learn module presents ten curated system design topics with GPT-4o-generated adaptive quizzes for in-platform skill development.

The platform is implemented using a three-tier architecture: a **Next.js 14** frontend with the App Router and React Flow visualization, a **FastAPI** backend orchestrating GPT-4o calls through LangGraph, and a **MongoDB Atlas** document store combined with a disk-persisted **FAISS** index. Authentication uses **Google OAuth 2.0** via NextAuth.js with a custom HS256 JWT bridge that makes the same token verifiable in both the Next.js Edge Runtime middleware and the Python backend.

Evaluation across thirty diverse problem statements demonstrates that RAG augmentation improves architectural completeness by **34%** over a non-RAG baseline, and a user study with twenty participants shows a mean task completion time of **4.2 minutes** for StructAI compared to **46.8 minutes** for manual design — an **11× speedup** — with explanation quality rated **4.1 / 5.0** on a Likert scale.

**Keywords:** Large Language Models, Software Architecture Design, Multi-Agent Systems, Retrieval-Augmented Generation, LangGraph, FAISS, Explainable AI, Software Engineering Education.

---

## TABLE OF CONTENTS

| Sr. No. | Title | Page No. |
|---|---|---|
| | Certificate | i |
| | Declaration | ii |
| | Acknowledgement | iii |
| | Abstract | iv |
| | List of Figures | vii |
| | List of Tables | viii |
| | List of Abbreviations | ix |
| **1** | **Introduction** | 1 |
| 1.1 | Background and Motivation | 1 |
| 1.2 | Problem Statement | 2 |
| 1.3 | Objectives | 2 |
| 1.4 | Scope of the Project | 3 |
| 1.5 | Organization of the Report | 3 |
| **2** | **Literature Survey** | 4 |
| 2.1 | Large Language Models for Software Engineering | 4 |
| 2.2 | Automated Domain and Architecture Modeling | 5 |
| 2.3 | Retrieval-Augmented Generation Systems | 5 |
| 2.4 | Graph-Augmented RAG and Knowledge Graphs | 6 |
| 2.5 | Multi-Agent LLM Systems | 6 |
| 2.6 | Explainability in AI-Assisted Software Engineering | 7 |
| 2.7 | Comparative Analysis of Surveyed Work | 7 |
| 2.8 | Research Gap | 8 |
| **3** | **System Analysis** | 9 |
| 3.1 | Existing Systems | 9 |
| 3.2 | Limitations of Existing Systems | 10 |
| 3.3 | Proposed System | 10 |
| 3.4 | Feasibility Study | 11 |
| **4** | **System Requirements** | 13 |
| 4.1 | Functional Requirements | 13 |
| 4.2 | Non-Functional Requirements | 14 |
| 4.3 | Hardware Requirements | 14 |
| 4.4 | Software Requirements | 15 |
| 4.5 | External Service Dependencies | 15 |
| **5** | **System Design** | 16 |
| 5.1 | High-Level System Architecture | 16 |
| 5.2 | Multi-Agent LangGraph Pipeline | 17 |
| 5.3 | Retrieval-Augmented Generation Subsystem | 19 |
| 5.4 | Authentication and Authorization Design | 20 |
| 5.5 | Data Model and Database Schema | 21 |
| 5.6 | Use Case Diagram | 22 |
| 5.7 | Data Flow Diagram | 23 |
| **6** | **Implementation** | 24 |
| 6.1 | Technology Stack | 24 |
| 6.2 | Backend Implementation | 25 |
| 6.3 | LangGraph Node Implementation | 26 |
| 6.4 | FAISS Vector Store Implementation | 28 |
| 6.5 | Explainability Engine | 29 |
| 6.6 | Learn Mode and Quiz Engine | 29 |
| 6.7 | Export Subsystem | 30 |
| 6.8 | Frontend Implementation | 30 |
| 6.9 | Prompt Engineering | 32 |
| **7** | **Testing** | 33 |
| 7.1 | Testing Strategy | 33 |
| 7.2 | Unit Testing | 33 |
| 7.3 | Integration Testing | 34 |
| 7.4 | End-to-End Testing | 34 |
| 7.5 | Test Cases and Results | 34 |
| **8** | **Results and Discussion** | 36 |
| 8.1 | Evaluation Setup | 36 |
| 8.2 | RAG vs. Non-RAG Performance | 36 |
| 8.3 | User Study Results | 37 |
| 8.4 | Ablation Study | 38 |
| 8.5 | Discussion | 38 |
| 8.6 | Limitations and Threats to Validity | 39 |
| **9** | **Conclusion and Future Scope** | 40 |
| 9.1 | Conclusion | 40 |
| 9.2 | Future Scope | 40 |
| | **References** | 42 |
| | **Appendix A — System Prompts** | 44 |
| | **Appendix B — API Reference** | 46 |
| | **Appendix C — Sample Output** | 47 |

---

## LIST OF FIGURES

| Fig. No. | Caption | Page |
|---|---|---|
| 5.1 | Three-tier system architecture of StructAI | 16 |
| 5.2 | LangGraph multi-agent pipeline DAG | 18 |
| 5.3 | RAG retrieval and generation pipeline | 19 |
| 5.4 | Authentication sequence diagram (OAuth + HS256 JWT) | 20 |
| 5.5 | MongoDB entity-relationship data model | 21 |
| 5.6 | Use case diagram | 22 |
| 5.7 | Level-1 data flow diagram | 23 |
| 6.1 | Component-level module breakdown | 25 |
| 8.1 | RAG vs. non-RAG completeness comparison | 37 |
| 8.2 | Task completion time distribution (user study) | 37 |

---

## LIST OF TABLES

| Table No. | Caption | Page |
|---|---|---|
| 2.1 | Comparative analysis of surveyed literature | 8 |
| 4.1 | Hardware requirements | 14 |
| 4.2 | Software requirements | 15 |
| 5.1 | Pipeline state schema (TypedDict) | 17 |
| 5.2 | Thirteen architectural node types | 19 |
| 6.1 | Technology stack summary | 24 |
| 6.2 | LLM temperature configuration per agent | 32 |
| 7.1 | Representative test cases | 35 |
| 8.1 | Architecture completeness: RAG vs. non-RAG | 36 |
| 8.2 | User study results (n = 20) | 38 |
| 8.3 | Ablation study results | 38 |

---

## LIST OF ABBREVIATIONS

| Abbreviation | Expansion |
|---|---|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CDN | Content Delivery Network |
| DAG | Directed Acyclic Graph |
| FAISS | Facebook AI Similarity Search |
| HS256 | HMAC with SHA-256 |
| JWE | JSON Web Encryption |
| JWT | JSON Web Token |
| KG | Knowledge Graph |
| LLM | Large Language Model |
| ML | Machine Learning |
| MVP | Minimum Viable Product |
| NoSQL | Not Only SQL |
| OAuth | Open Authorization |
| REST | Representational State Transfer |
| RAG | Retrieval-Augmented Generation |
| SDLC | Software Development Life Cycle |
| TLS | Transport Layer Security |
| UML | Unified Modeling Language |
| XAI | Explainable Artificial Intelligence |

---

---

# CHAPTER 1
# INTRODUCTION

## 1.1 Background and Motivation

Software architecture design is among the most consequential and least automated phases of the software development lifecycle. Architectural decisions — which databases to use, how services communicate, how to handle load and failure — shape the entire trajectory of a system's scalability, maintainability, and operational cost. Yet these decisions are routinely made under time pressure, often by engineers who lack deep architectural expertise.

In industry, senior architects spend significant time on repetitive documentation of well-understood patterns. In academia, students preparing for system design interviews and distributed-systems coursework must develop architectural intuition largely through self-study, with limited interactive tooling for feedback. Commercial diagramming suites such as Lucidchart and draw.io require fully manual placement of components and offer no AI-driven generation. General-purpose code assistants such as GitHub Copilot and ChatGPT produce prose descriptions, but generate neither machine-readable graph JSON nor interactive diagrams.

The recent emergence of Large Language Models (LLMs) capable of complex multi-step reasoning and structured JSON generation [1], [10], [11] presents a transformative opportunity for this domain. Surveys by Fan et al. [10] and Raiaan et al. [1] demonstrate that GPT-4-class models consistently outperform smaller alternatives on structured generation tasks. Recent work on retrieval-augmented generation [3], [12] establishes that grounding LLMs in curated domain corpora substantially reduces hallucination on knowledge-intensive tasks. Multi-agent frameworks [8], [9] show that decomposing complex problems across specialized agents outperforms monolithic single-agent prompting. However, no prior system unifies these advances into a single, deployable platform for software architecture design with integrated pedagogical scaffolding.

## 1.2 Problem Statement

To design and implement a full-stack, AI-powered platform that, given a natural-language problem statement, automatically generates a complete, production-grade software architecture as an interactive, machine-readable graph; explains the rationale for every component on demand; teaches the underlying system design concepts through an adaptive quiz module; and is deployable as a secure, multi-user web application.

Three concrete deficiencies in existing tooling motivate this work:

1. **Unstructured output:** General-purpose LLMs produce free-form prose or code snippets rather than machine-readable architecture graphs suitable for interactive visualization.
2. **Ungrounded generation:** LLMs operating from parametric memory alone hallucinate architectural patterns, citing technologies or topologies that are inconsistent with real-world production designs.
3. **Absent pedagogy:** A user who receives a generated architecture has no in-platform mechanism to understand *why* each component was chosen, what alternatives exist, or how to deepen their conceptual knowledge through structured assessment.

## 1.3 Objectives

The principal objectives of this project are as follows:

1. **Design a multi-agent LLM pipeline** that decomposes the architecture generation task into specialized agents — requirement extraction, ambiguity clarification, pattern retrieval, and architecture synthesis — coordinated via an explicit state machine.
2. **Implement retrieval-augmented generation** over a curated corpus of real-world architectural patterns to ground LLM output in established designs and reduce hallucination.
3. **Build an interactive diagram interface** that renders generated architectures as pannable, zoomable React Flow graphs with thirteen distinct node types for components such as load balancers, databases, caches, message queues, and CDNs.
4. **Engineer an explainability engine** that produces structured, decision-level explanations (what, why, alternatives, trade-offs, learn-more) for any clicked component.
5. **Develop a learn module** with ten curated system design topics and an adaptive quiz generator that produces scenario-based questions at three difficulty levels.
6. **Deliver a secure, deployable web application** with Google OAuth authentication, role-based authorization, MongoDB persistence, and PDF/Markdown export capabilities.
7. **Empirically evaluate the system** against non-RAG baselines and manual design workflows, measuring completeness, correctness, time-to-design, and explanation quality.

## 1.4 Scope of the Project

**In scope:**

- Generation of cloud-native, web-scale software architectures (web applications, mobile back-ends, real-time messaging, content delivery, search-and-recommendation systems).
- Component-level explanation, decision rationale, and pedagogical content for the thirteen supported node types.
- Single-user authenticated sessions with persisted designs and quiz history.
- PDF and Markdown export of completed designs.
- Local-development and self-hosted deployment.

**Out of scope:**

- Generation of architectures for embedded systems, real-time control systems, scientific HPC, or specialized hardware domains (the FAISS corpus does not cover these).
- Automatic generation of executable code, Infrastructure-as-Code, or Kubernetes manifests (planned for future work).
- Real-time multi-user collaborative editing.
- Fine-tuning of LLMs on the architecture-generation task — the project uses the hosted OpenAI GPT-4o model exclusively.

## 1.5 Organization of the Report

The remainder of this report is organized as follows. **Chapter 2** surveys related literature across six thematic areas and identifies the research gap. **Chapter 3** analyzes existing systems and presents the proposed solution along with feasibility considerations. **Chapter 4** lists functional, non-functional, hardware, and software requirements. **Chapter 5** details the system design, including the high-level architecture, the LangGraph pipeline, the RAG subsystem, the authentication design, and the data model. **Chapter 6** describes the implementation across the backend, frontend, and supporting subsystems. **Chapter 7** presents the testing strategy and results. **Chapter 8** reports the empirical evaluation. **Chapter 9** concludes and outlines future work.

---

---

# CHAPTER 2
# LITERATURE SURVEY

The literature review is organized around six thematic areas that together establish the technical foundation of this work: (i) Large Language Models for software engineering; (ii) automated domain and architecture modeling; (iii) retrieval-augmented generation; (iv) graph-augmented RAG and knowledge graphs; (v) multi-agent LLM systems; and (vi) explainability in AI-assisted software engineering. Thirteen papers were reviewed in depth; each is referenced according to IEEE style.

## 2.1 Large Language Models for Software Engineering

Fan, Gokkaya, Harman, Lyubarskiy, Sengupta, Yoo, and Zhang [10] provide a comprehensive survey of LLM applications across the software engineering lifecycle, identifying code generation, test synthesis, bug detection, and documentation as primary application areas. They observe that while LLMs excel at token-level code completion, their effectiveness for higher-level *architectural* reasoning remains underexplored — a gap StructAI directly addresses.

Raiaan, Mukta, Fatema, Fahad, Sakib, Mim, Ahmad, Ali, and Azam [1] survey the evolution of LLM architectures from early statistical language models through transformer-based variants such as BERT, GPT, T5, and PaLM. They document the scaling laws that enable emergent capabilities relevant to complex reasoning tasks and identify structured output generation as a frontier capability.

Shao, Basit, Karri, and Shafique [11] survey current LLM architectures with emphasis on multimodal capabilities and benchmark performance, concluding that GPT-4-class models consistently outperform smaller alternatives on structured-generation benchmarks. This finding directly motivates StructAI's adoption of GPT-4o as its generation backbone.

**Relevance to StructAI:** This body of work establishes the technical viability of using GPT-4o for the structured JSON output that StructAI's pipeline requires.

## 2.2 Automated Domain and Architecture Modeling

Chen, Yang, Chen, López, Mussbacher, and Varró [2] present a comparative study of LLM-based automated domain modeling, evaluating GPT-3.5, GPT-4, and open-source models on extraction of UML class diagrams from natural-language requirements. GPT-4 achieves 78% recall on entity identification but struggles with relationship cardinality without explicit prompt engineering — a finding that informs StructAI's use of strict JSON schemas and explicit relationship rules in the generation prompt.

Arulmohan, Meurs, and Mosser [6] present a pipeline for extracting domain models from textual requirements in the LLM era, demonstrating that chain-of-thought prompting improves structural completeness in generated models.

Both works operate at the **conceptual model layer** (entities, relationships, attributes) and do not address infrastructure-level architecture generation, leaving the higher-abstraction problem that StructAI tackles open.

**Relevance to StructAI:** StructAI extends the work of [2] and [6] from conceptual modeling to infrastructure-level architecture generation, with the additional contribution of RAG-grounded retrieval that neither prior work employs.

## 2.3 Retrieval-Augmented Generation Systems

Tekgöz, Şahin, and Aydın [3] empirically evaluate combinations of vector databases (FAISS, Chroma, Pinecone, Weaviate) and LLMs (GPT-4o, GPT-3.5, Llama 3) for RAG system performance, measuring retrieval latency, relevance, and downstream generation quality. Their results show that FAISS achieves the lowest retrieval latency for corpora under 100K documents while maintaining competitive relevance scores — directly informing StructAI's choice of FAISS over hosted alternatives.

Fan, Wu, Ding, Ning, Wang, and Li [12] present a comprehensive treatment of RAG data management and system design, identifying corpus quality, chunking strategy, and embedding model selection as the primary levers for RAG performance. They recommend OpenAI's `text-embedding-ada-002` as a strong general-purpose embedding model — consistent with StructAI's implementation.

**Relevance to StructAI:** StructAI applies the RAG principles of [3] and [12] to a specialized corpus of 25 curated real-world architecture patterns, achieving grounded generation that reduces hallucination compared to prompt-only baselines.

## 2.4 Graph-Augmented RAG and Knowledge Graphs

Procko and Ochoa [7] survey the emerging area of **Graph RAG**, in which knowledge graphs replace or supplement vector-retrieved documents as the retrieval substrate. They argue that KGs provide noise-free, semantically structured context, reducing irrelevant content injection into LLM prompts — a known limitation of flat vector retrieval.

Pan, Luo, Wang, Chen, Wang, and Wu [13] present a roadmap for unifying LLMs and knowledge graphs, identifying three paradigms: *KG-enhanced LLMs*, *LLM-augmented KGs*, and *synergized LLM+KG* systems. They demonstrate that KG-enhanced approaches improve factual accuracy on knowledge-intensive benchmarks.

**Relevance to StructAI:** StructAI currently uses flat FAISS-based vector retrieval. The findings of [7] and [13] motivate a planned Graph RAG extension (discussed in Chapter 9) that would represent architectural relationships (e.g., *"load balancer precedes API gateway"*) as a structured KG.

## 2.5 Multi-Agent LLM Systems

Mushtaq, Naeem, Ghaznavi, Taj, Hashmi, and Qadir [8] propose a multi-agent LLM framework for complex engineering problem-solving in educational contexts. Specialized agents assuming distinct expert personas achieve 89% alignment with faculty scores, versus 71% for single-agent systems. This establishes that task decomposition across specialized agents improves output quality on problems requiring multiple competencies.

Gogineni [9] presents a technical framework for multi-agent LLM systems with optimized knowledge retrieval and inter-agent communication, reporting 42% higher accuracy on complex knowledge tasks, 37% reduction in hallucinations, and 29% faster convergence compared to single-agent baselines.

**Relevance to StructAI:** StructAI realizes multi-agent coordination through **LangGraph**'s explicit state-machine formulation, decomposing the design task into four specialized agents (extraction, clarification, retrieval, generation) with typed state propagation. This is a more structured approach than the conversation-based coordination in [8] and [9], offering deterministic debuggability and conditional branching.

## 2.6 Explainability in AI-Assisted Software Engineering

Tantithamthavorn and Jiarpakdee [4] deliver a tutorial on explainable AI for software engineering, arguing that AI-generated recommendations without interpretable rationale are systematically distrusted by practitioners. They demonstrate that adding feature-importance explanations to defect prediction models increases practitioner adoption by 2.3×.

Arora, Easwaran, and Chaudhary [5] survey XAI techniques across the SDLC and find that the **architecture and design phase** is the least served by existing explainability approaches — precisely the gap StructAI targets. They recommend that SE tools provide *decision-level* explanations (why was this component chosen?) rather than *model-level* explanations (which features activated?).

**Relevance to StructAI:** StructAI's explainability engine directly implements the recommendation of [5] by generating decision-level explanations: *what* the component is, *why* it was selected for this specific system, what *alternatives* exist, and what *trade-offs* the choice entails.

## 2.7 Comparative Analysis of Surveyed Work

**TABLE 2.1 — Comparative Analysis of Surveyed Literature**

| Ref. | Authors (Year) | Domain | Key Contribution | Limitation Addressed by StructAI |
|---|---|---|---|---|
| [1] | Raiaan et al. (2024) | LLM survey | Architectures, scaling laws | Generic — no SE focus |
| [2] | Chen et al. (2023) | Domain modeling | LLM extraction of UML | Limited to class diagrams |
| [3] | Tekgöz et al. (2025) | RAG benchmarking | FAISS optimal for < 100K docs | No SE-specific corpus |
| [4] | Tantithamthavorn et al. (2021) | XAI for SE | Practitioner adoption metrics | Tutorial — no system |
| [5] | Arora et al. (2025) | XAI SDLC survey | Phase-specific gap analysis | No design-phase tool |
| [6] | Arulmohan et al. (2023) | Domain modeling | CoT prompting for models | Conceptual layer only |
| [7] | Procko & Ochoa (2024) | Graph RAG survey | KG vs. vector retrieval | Survey only |
| [8] | Mushtaq et al. (2025) | Multi-agent LLM | Engineering education | Conversation-based |
| [9] | Gogineni (2025) | Multi-agent LLM | 42% accuracy gain | No SE focus |
| [10] | Fan et al. (2023) | LLM-for-SE survey | Lifecycle taxonomy | No architecture tool |
| [11] | Shao et al. (2024) | LLM architectures | GPT-4 SOTA | No domain application |
| [12] | Fan et al. (2025) | RAG systems | Corpus-quality dominance | No SE corpus |
| [13] | Pan et al. (2024) | LLM + KG | Three integration paradigms | Roadmap only |

## 2.8 Research Gap

Synthesizing the surveyed literature reveals a clear and previously unfilled research gap:

> **No existing system simultaneously provides (a) automated multi-agent generation of structured infrastructure-level software architectures, (b) retrieval-augmented grounding in a curated real-world pattern corpus, (c) decision-level explainability at the component granularity, and (d) integrated pedagogical scaffolding through adaptive quizzes — within a single, deployable platform.**

StructAI is designed specifically to close this gap.

---

---

# CHAPTER 3
# SYSTEM ANALYSIS

## 3.1 Existing Systems

The existing landscape for architecture design tooling falls into three categories:

**1. Manual Diagramming Tools** — Lucidchart, draw.io, Microsoft Visio, and Miro. These tools provide canvas, shapes, and connectors for manual diagram construction. They are widely adopted in industry but require the user to already know the architecture they want to draw.

**2. General-Purpose AI Assistants** — ChatGPT, GitHub Copilot, Claude, and Gemini. These conversational LLM interfaces can describe architectures in prose when prompted, but they produce neither machine-readable graph JSON nor interactive visualizations, and they have no domain-specific grounding.

**3. Specialized Modeling Research Prototypes** — academic prototypes from Chen et al. [2] and Arulmohan et al. [6] that extract UML class models from text. These operate at the conceptual model layer and have no infrastructure-level abstraction or interactive component explanation.

## 3.2 Limitations of Existing Systems

| Limitation | Manual Tools | General AI | Research Prototypes |
|---|---|---|---|
| Requires architectural expertise from the user | ✗ | ✗ | ✓ |
| Produces machine-readable graph JSON | ✗ | ✗ | Partial |
| Interactive component-level explanation | ✗ | ✗ | ✗ |
| Grounded in real-world architecture patterns | ✗ | ✗ | ✗ |
| Integrated pedagogical scaffolding | ✗ | ✗ | ✗ |
| Deployable end-to-end production system | ✓ | ✓ | ✗ |
| Authentication and multi-user persistence | ✓ | Partial | ✗ |

The composite limitation is clear: **no existing tool combines automation, grounding, explainability, and education in a deployable platform**.

## 3.3 Proposed System

StructAI proposes a multi-agent, RAG-grounded, explainability-rich platform for automated software architecture design. The user provides a single natural-language problem statement, and the system:

1. **Extracts** structured functional, non-functional, scale, and ambiguity requirements via GPT-4o.
2. **Detects** ambiguities and (when present) asks 2–4 targeted clarifying questions in a two-pass interaction.
3. **Retrieves** the top-3 most similar real-world architecture patterns from a FAISS vector store seeded with 25 curated patterns.
4. **Generates** a complete architecture as a structured JSON graph with 13 distinct component types, communication edges, a tech stack, and a 2–3 sentence summary.
5. **Renders** the graph interactively via React Flow with `dagre` left-to-right layout.
6. **Explains** any clicked component with a structured five-field decision rationale (*what*, *why*, *alternatives*, *trade-offs*, *learn-more*).
7. **Teaches** ten curated system design topics with GPT-4o-generated adaptive quizzes and a 70%-passing-threshold grading engine.
8. **Exports** completed designs as styled PDF or Markdown reports.
9. **Tracks** per-user analytics: design count, quiz score history, and recent activity.

The system is deployed as a three-tier web application with Google OAuth authentication.

## 3.4 Feasibility Study

### 3.4.1 Technical Feasibility

All required technologies are mature and openly available:

- **GPT-4o** is generally available through OpenAI's API with stable pricing.
- **LangGraph** and **LangChain** are open-source Python libraries with active maintenance.
- **FAISS** is a battle-tested vector search library from Meta, suitable for corpora of the size StructAI uses.
- **Next.js 14**, **FastAPI**, **MongoDB Atlas**, and **React Flow** are production-grade frameworks widely deployed in industry.

Prototype implementation confirmed that an end-to-end design generation completes in 5–7 seconds (no clarification) or 10–12 seconds (with clarification), well within acceptable interactive latency.

### 3.4.2 Economic Feasibility

The operating-cost model is dominated by OpenAI API charges:

| Cost Component | Estimate |
|---|---|
| GPT-4o per design generation | ≈ $0.04–0.08 |
| `text-embedding-ada-002` index (one-time, 25 patterns) | ≈ $0.001 |
| Component explanation (cached after first call) | ≈ $0.01 first call, $0 thereafter |
| MongoDB Atlas free tier | $0 / month |
| Self-hosted FastAPI + Next.js | $0 (local) / ≈ $20/month (small VPS) |

At a unit cost of approximately ten cents per complete design including explanations, the system is economically viable for free-tier educational deployment with modest sponsorship, or freemium / paid SaaS pricing.

### 3.4.3 Operational Feasibility

The user interface is a standard browser application with a familiar SaaS layout (left sidebar navigation, light-themed content area). No client-side installation is required. Sign-in is via Google OAuth — the most widely used identity provider in the target audience (engineering students and developers). Generated designs are persisted server-side and accessible across devices on subsequent login.

### 3.4.4 Schedule Feasibility

The project was executed across two academic semesters in distinct phases: requirement analysis and literature survey (4 weeks), system design and prototype (6 weeks), full implementation across backend and frontend (12 weeks), and evaluation and documentation (6 weeks), totaling 28 weeks — within the available final-year project window.

---

---

# CHAPTER 4
# SYSTEM REQUIREMENTS

## 4.1 Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | The system shall authenticate users via Google OAuth 2.0. | High |
| FR-2 | The system shall accept a free-text problem statement from authenticated users. | High |
| FR-3 | The system shall extract structured requirements (functional, non-functional, scale, ambiguities) using a GPT-4o agent with `temperature=0`. | High |
| FR-4 | The system shall detect ambiguities and, when present, generate 2–4 clarifying questions and pause for user input. | High |
| FR-5 | The system shall retrieve the top-3 most similar architecture patterns from a FAISS vector store using `text-embedding-ada-002` embeddings. | High |
| FR-6 | The system shall generate a complete architecture as a JSON graph containing nodes (13 supported types), edges, tech stack, and summary. | High |
| FR-7 | The system shall render the generated architecture as an interactive React Flow diagram with automatic `dagre` layout. | High |
| FR-8 | The system shall produce a five-field structured explanation (*what*, *why*, *alternatives*, *trade-offs*, *learn-more*) on click of any architecture node, with explanations cached per design. | High |
| FR-9 | The system shall provide a catalog of ten curated system design topics with adaptive quizzes generated by GPT-4o. | Medium |
| FR-10 | The system shall grade quiz submissions, persist attempts, and report a 70%-threshold pass/fail outcome with per-question explanations. | Medium |
| FR-11 | The system shall export completed designs as PDF and Markdown documents on demand. | Medium |
| FR-12 | The system shall display per-user analytics: total designs, total quizzes, average quiz score, recent activity. | Medium |
| FR-13 | The system shall provide an admin role with platform-wide statistics, user list, role promotion, and FAISS index rebuild capability. | Low |

## 4.2 Non-Functional Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-1 | **Performance** — end-to-end design generation latency | ≤ 7 s without clarification; ≤ 12 s with clarification |
| NFR-2 | **Performance** — FAISS retrieval latency | ≤ 100 ms per query |
| NFR-3 | **Security** — all API endpoints (except OAuth callbacks and topic listing) require valid HS256 JWT | 100% coverage |
| NFR-4 | **Security** — design ownership enforced via `user_id` filter on every MongoDB query | 100% coverage |
| NFR-5 | **Security** — role information read from MongoDB on every request, never from JWT claims | Mandatory |
| NFR-6 | **Scalability** — backend supports concurrent design generation via async I/O and a `ThreadPoolExecutor(max_workers=2)` for FAISS | ≥ 50 concurrent users on a single 8-vCPU host |
| NFR-7 | **Maintainability** — backend and frontend codebases use strict type checking (Pydantic v2 and TypeScript strict mode) | 100% type coverage |
| NFR-8 | **Usability** — first-time users complete an end-to-end design within 5 minutes of first sign-in | Measured in user study |
| NFR-9 | **Reliability** — invalid GPT-4o JSON output is caught and surfaced as HTTP 500 with diagnostic information | Mandatory |
| NFR-10 | **Portability** — backend runs on Linux, macOS, and Windows with Python 3.11+; frontend runs on any modern browser supporting ES2022 | Mandatory |

## 4.3 Hardware Requirements

**TABLE 4.1 — Hardware Requirements**

| Component | Development | Production (Single Node) |
|---|---|---|
| CPU | Modern x86-64 / Apple Silicon | 8 vCPU |
| RAM | 8 GB minimum (4 GB usable) | 16 GB |
| Disk | 2 GB for venv, node_modules, FAISS index | 20 GB SSD |
| Network | Stable internet for OpenAI and MongoDB Atlas | 100 Mbps symmetric |
| GPU | Not required (inference is API-based) | Not required |

## 4.4 Software Requirements

**TABLE 4.2 — Software Requirements**

| Layer | Software | Version |
|---|---|---|
| OS (dev) | macOS / Linux / Windows | macOS 13+, Ubuntu 22.04+, Windows 11 |
| Backend runtime | Python | 3.11+ |
| Backend framework | FastAPI, Uvicorn | Latest |
| LLM orchestration | LangGraph, LangChain | Latest |
| Vector store | FAISS (faiss-cpu) | 1.7+ |
| Database driver | Motor (async MongoDB driver) | Latest |
| Auth library | python-jose | Latest |
| Frontend runtime | Node.js | 20+ |
| Frontend framework | Next.js (App Router) | 14.x |
| UI library | React, Tailwind CSS | 18.x, 3.x |
| Diagram | React Flow (`@xyflow/react`), `@dagrejs/dagre` | Latest |
| Auth (FE) | NextAuth.js, `jose` | 4.x |
| Browser | Chrome, Edge, Firefox, Safari | Latest two majors |

## 4.5 External Service Dependencies

| Service | Purpose | Tier Used |
|---|---|---|
| **OpenAI API** | GPT-4o inference + `text-embedding-ada-002` embeddings | Paid (pay-as-you-go) |
| **MongoDB Atlas** | Persistent document storage | Free tier (M0, 512 MB) |
| **Google OAuth 2.0** | Identity provider | Free |
| **Google Fonts** | Space Grotesk, Inter typefaces | Free CDN |

---

---

# CHAPTER 5
# SYSTEM DESIGN

## 5.1 High-Level System Architecture

StructAI follows a classic three-tier web application architecture comprising a presentation layer, an application layer, and a data layer. The three tiers communicate over HTTP/REST with mutual TLS where applicable. Figure 5.1 illustrates the complete system.

```
+-----------------------------------------------------------------+
|                       PRESENTATION LAYER                        |
|             Next.js 14 (App Router) — Port 3000                 |
|   +----------+ +----------+ +---------+ +---------+ +--------+  |
|   | Landing  | |Dashboard | | Builder | |  Learn  | |Analytic|  |
|   +----------+ +----------+ +---------+ +---------+ +--------+  |
|              Axios — Authorization: Bearer <HS256 JWT>          |
+-----------------------------------------------------------------+
                              | HTTPS REST
                              v
+-----------------------------------------------------------------+
|                       APPLICATION LAYER                         |
|                  FastAPI (Python 3.11) — Port 8000              |
|   +-------------+ +------------+ +-----------+ +-------------+  |
|   |  Auth API   | |Designs API | |Learn API  | |Analytics API|  |
|   +-------------+ +------------+ +-----------+ +-------------+  |
|   Security: decode_token() -> get_current_user() (HS256, JWT)   |
|                                                                 |
|   +--------------------------------------------------------+    |
|   |  LangGraph StateGraph                                  |    |
|   |  extract -> [clarify?] -> retrieve -> generate         |    |
|   +--------------------------------------------------------+    |
+-----------------------------------------------------------------+
            |                    |                    |
            v                    v                    v
   +----------------+   +----------------+   +----------------+
   | OpenAI GPT-4o  |   |  FAISS Index   |   | MongoDB Atlas  |
   |  + Embeddings  |   | 25 patterns    |   | users, designs |
   +----------------+   +----------------+   +----------------+
```

*Fig. 5.1 — Three-tier system architecture of StructAI.*

**Request lifecycle (design generation):**

1. User submits a problem statement; the frontend issues `POST /api/v1/designs/generate` with a Bearer token.
2. FastAPI's `get_current_user()` dependency decodes the HS256 JWT and fetches the user document from MongoDB.
3. `run_initial(problem_statement)` invokes the LangGraph pipeline: `extract → (clarify | retrieve) → generate`.
4. If clarification is required, the API returns `status: "awaiting_clarification"` with the generated questions; otherwise it returns the complete architecture JSON.
5. On clarification, the user's answers trigger `POST /api/v1/designs/{id}/clarify`, which calls `run_with_clarifications()` to bypass the graph and invoke retrieval + generation directly.
6. The completed architecture is persisted in MongoDB; the user's `design_count` is incremented atomically.

## 5.2 Multi-Agent LangGraph Pipeline

The core of StructAI is a four-node LangGraph `StateGraph`. Each node is an `async` Python function that receives a typed shared state and returns a partial update.

**TABLE 5.1 — Pipeline State Schema (TypedDict)**

| Field | Type | Set By | Description |
|---|---|---|---|
| `problem_statement` | `str` | API caller | Raw user input |
| `requirements` | `dict` | extract | Structured output of the extraction agent |
| `clarifying_questions` | `list[str]` | clarify | Questions for the user (first pass) |
| `clarifications` | `Optional[dict]` | API (pass 2) | User-supplied answers |
| `rag_context` | `str` | retrieve | Concatenated top-3 pattern texts |
| `architecture` | `Optional[dict]` | generate | Final JSON graph |
| `error` | `Optional[str]` | any node | Propagated exception message |

```
       ( Problem Statement )
                 |
                 v
        +-----------------+
        |  node_extract   |   GPT-4o, T=0
        +-----------------+
                 |
       +---------+---------+
       | should_clarify?   |
       +---+-----------+---+
           | YES       | NO
           v           v
   +--------------+   +--------------+
   | node_clarify |   | node_retrieve|
   |  GPT-4o, T=0 |   | FAISS top-k=3|
   +--------------+   +--------------+
           |                 |
           v                 v
     ( Await Input )   +--------------+
           |           | node_generate|
           +---------->|  GPT-4o,T=0.2|
                       +--------------+
                              |
                              v
                  ( Architecture JSON )
```

*Fig. 5.2 — LangGraph multi-agent pipeline DAG. Conditional edge routes ambiguous inputs through the clarification node; both paths converge at generation.*

**Conditional edge function:**

```python
def should_clarify(state: DesignState) -> str:
    has_ambiguities = bool(state["requirements"].get("ambiguities"))
    already_clarified = bool(state.get("clarifications"))
    return "clarify" if (has_ambiguities and not already_clarified) else "retrieve"
```

This dual condition allows the second pass (after clarifications) to skip the clarification node cleanly, without requiring a separate graph topology.

**Pass-1 lifecycle:** `problem_statement → extract → [ambiguities?] → clarify | (retrieve → generate)`.
**Pass-2 lifecycle:** bypasses LangGraph and invokes `retrieve_similar_patterns` and `generate_architecture` directly, reading the persisted requirements from MongoDB.

## 5.3 Retrieval-Augmented Generation Subsystem

The RAG subsystem grounds the generation agent in 25 curated architecture pattern documents (Netflix, Uber, Discord, Twitter, Airbnb, Dropbox, etc.). Each document is a 300-word prose description covering use case, key components, communication patterns, scaling strategy, and tech stack.

**TABLE 5.2 — Thirteen Architectural Node Types**

| # | Type | Example Tech |
|---|---|---|
| 1 | `client` | React Native, Flutter |
| 2 | `api_gateway` | Kong, AWS API Gateway |
| 3 | `load_balancer` | Nginx, HAProxy, AWS ALB |
| 4 | `web_server` | Node.js, Spring, FastAPI |
| 5 | `database` | PostgreSQL, MySQL |
| 6 | `nosql_database` | MongoDB, Cassandra |
| 7 | `cache` | Redis, Memcached |
| 8 | `message_queue` | Kafka, RabbitMQ, SQS |
| 9 | `cdn` | CloudFront, Cloudflare |
| 10 | `object_storage` | S3, GCS |
| 11 | `auth_service` | OAuth, Auth0, Keycloak |
| 12 | `monitoring` | Prometheus, Grafana, Datadog |
| 13 | `ml_service` | TensorFlow Serving, SageMaker |

```
   ( Problem Statement )
            |
            v
   +------------------+
   |  Embed query     |  text-embedding-ada-002 -> 1536-dim
   +------------------+
            |
            v
   +------------------+
   | FAISS sim search |  IndexFlatL2, ThreadPoolExecutor
   |   top-k = 3      |
   +------------------+
        / |  \
       v  v   v
   +----+ +----+ +----+
   | P1 | | P2 | | P3 |  ~300 words each
   +----+ +----+ +----+
        \  |  /
         v v v
   +------------------+
   | Concatenated     |  joined by --- separators
   | RAG context      |  ~1200 tokens total
   +------------------+
            |
            v
   +------------------+
   | GPT-4o generate  |  T=0.2, strict JSON schema
   +------------------+
            |
            v
   ( Architecture JSON )
```

*Fig. 5.3 — RAG retrieval and generation pipeline.*

## 5.4 Authentication and Authorization Design

StructAI uses **Google OAuth 2.0** with a custom HS256 JWT bridge. The standard NextAuth.js token uses JWE (JSON Web Encryption with RSA), which is incompatible with `python-jose`'s HS256 verification. The `encode` and `decode` callbacks are overridden using the `jose` library (Edge-Runtime compatible) so that the same HS256-signed JWT is verifiable in both the Next.js middleware (Edge Runtime) and the FastAPI backend with a shared `NEXTAUTH_SECRET`.

```
Browser            NextAuth           Google             FastAPI            MongoDB
  |                   |                  |                   |                  |
  | signIn("google") |                  |                   |                  |
  |------------------>|                  |                   |                  |
  |                   |---- redirect --->|                   |                  |
  |                   |                  |--- consent UI --->|                  |
  |                   |<-- auth code ----|                   |                  |
  |                   |--- POST /token ->|                   |                  |
  |                   |<-- profile ------|                   |                  |
  |                   | SignJWT(HS256)   |                   |                  |
  |<- Set-Cookie -----|                  |                   |                  |
  |                   |                  |                   |                  |
  | POST /upsert-user (no auth required) |                   |                  |
  |------------------------------------------>             |                  |
  |                                                          |---- findOne --->|
  |                                                          |<-- user doc ----|
  |<------------------ 200 user profile -----------------------                 |
  |                                                          |                  |
  | Authenticated request + Bearer <JWT>                     |                  |
  |------------------------------------------>             |                  |
  |                                          decode_token() |                  |
  |                                          findOne(uid)   |---- query ----->|
  |                                          authorized op  |<-- doc ---------|
  |<------------------ 200 response --------------------------                  |
```

*Fig. 5.4 — Authentication sequence. The custom HS256 JWT bridges Edge Runtime middleware and Python backend through a single shared secret.*

**Authorization model (two levels):**

- **User-level:** every query touching `designs` or `quiz_attempts` includes `user_id` in the MongoDB filter, enforcing ownership.
- **Admin-level:** admin routes use `get_admin_user()` which calls `get_current_user()` and then checks `user["role"] == "admin"`. Role is *never* read from the JWT — only from MongoDB — preventing privilege escalation via token manipulation.

## 5.5 Data Model and Database Schema

MongoDB stores three collections: `users`, `designs`, and `quiz_attempts`. The `designs` collection embeds the full architecture JSON to avoid joins.

```
+----------------+         +------------------+         +--------------------+
|     users      |  1 : N  |     designs      |  1 : N  |  quiz_attempts     |
|----------------|<--------|------------------|         |--------------------|
| _id (PK)       |         | _id (PK)         |         | _id (PK)           |
| name           |         | user_id (FK)     |         | user_id (FK) ----+ |
| email (unique) |         | problem_stmt     |         | quiz_id           |
| image          |         | requirements{}   |         | topic             |
| role           |         | clarifying_qs[]  |         | score (float)     |
| created_at     |         | clarifications{} |         | passed (bool)     |
| design_count   |         | architecture{}   |         | completed_at      |
| quiz_count     |         |   nodes[], edges[]         +--------------------+
+----------------+         |   tech_stack[], summary |
                           | explanations{}    |
                           | status            |
                           | created_at        |
                           | updated_at        |
                           +-------------------+
```

*Fig. 5.5 — MongoDB entity-relationship data model. Ownership is enforced via `user_id` foreign key on every read/write. Role is stored only in `users`, never in JWT claims.*

## 5.6 Use Case Diagram

```
                +-----------------------------------+
                |          StructAI Platform        |
                |                                   |
   +--------+   |  ( Sign in with Google )          |
   |        |---|->                                 |
   | Student|   |  ( Submit problem statement )     |
   |/Engineer---|->                                 |
   |        |   |  ( Answer clarifying questions )  |
   |        |---|->                                 |
   |        |   |  ( View generated architecture )  |
   |        |---|->                                 |
   |        |   |  ( Click node -> explanation )    |
   |        |---|->                                 |
   |        |   |  ( Take quiz on topic )           |
   |        |---|->                                 |
   |        |   |  ( Export design as PDF / MD )    |
   |        |---|->                                 |
   |        |   |  ( View personal analytics )      |
   |        |---|->                                 |
   +--------+   |                                   |
                |                                   |
   +--------+   |  ( View platform-wide stats )     |
   | Admin  |---|->                                 |
   |        |   |  ( Promote user role )            |
   |        |---|->                                 |
   |        |   |  ( Rebuild FAISS index )          |
   |        |---|->                                 |
   +--------+   +-----------------------------------+
```

*Fig. 5.6 — Use case diagram. Two actor roles: Student/Engineer and Admin.*

## 5.7 Data Flow Diagram

**Level-1 DFD:**

```
                +-----------+
   User input ->|  Process  |
   (problem)    | 1. Extract|
                |Reqs (GPT) |
                +-----+-----+
                      |
                      v
                +-----------+         +--------------+
                |  Process  |         |  D1: FAISS   |
                | 2. Retrieve <-----> |  Index       |
                |  Patterns |         +--------------+
                +-----+-----+
                      |
                      v
                +-----------+         +--------------+
                |  Process  |         | D2: MongoDB  |
                | 3. Generate <-----> |  designs     |
                | Arch (GPT)|         +--------------+
                +-----+-----+
                      |
                      v
                +-----------+
                |  Process  |
                | 4. Render |---> Architecture diagram (User)
                | React Flow|
                +-----+-----+
                      |
                      v (on click)
                +-----------+
                |  Process  |
                | 5. Explain|---> Component rationale (User)
                | (GPT, T=0.3)
                +-----------+
```

*Fig. 5.7 — Level-1 data flow diagram.*

---

---

# CHAPTER 6
# IMPLEMENTATION

## 6.1 Technology Stack

**TABLE 6.1 — Technology Stack Summary**

| Layer | Technology | Version / Notes |
|---|---|---|
| Frontend framework | Next.js (App Router) | 14 |
| Frontend language | TypeScript | strict mode |
| Styling | Tailwind CSS | 3.x with custom `brand` and `navy` tokens |
| Diagram | React Flow (`@xyflow/react`) | with custom node renderers |
| Layout | `@dagrejs/dagre` | left-to-right hierarchical |
| Auth (FE) | NextAuth.js + `jose` | HS256 JWT, Edge Runtime |
| HTTP client | Axios | request interceptor for Bearer token |
| Backend framework | FastAPI | Python 3.11+, async-native |
| Orchestration | LangGraph + LangChain | StateGraph, typed async nodes |
| LLM | OpenAI GPT-4o (`gpt-4o-2024-08-06`) | T=0 / 0.2 / 0.3 / 0.7 |
| Embeddings | `text-embedding-ada-002` | 1536 dims |
| Vector store | FAISS (`IndexFlatL2`) | persisted at `vector_store/faiss_index/` |
| Database | MongoDB Atlas | Motor async driver |
| Auth (BE) | python-jose | HS256 with `NEXTAUTH_SECRET` |
| Validation | Pydantic v2 | request body validation |
| PDF | `reportlab` / `fpdf` | server-side generation |

## 6.2 Backend Implementation

The backend follows a layered architecture under `backend/app/`:

```
app/
├── main.py                 FastAPI app, CORS, router registration, lifespan
├── api/routes/             auth, designs, explain, learn, export, analytics, admin
├── core/                   config (pydantic-settings), database, security
├── models/                 Pydantic request/response models
└── services/
    ├── design_builder/     pipeline (LangGraph), extractor, generator, rag
    ├── explainability/     explainer
    ├── learn_mode/         topics catalog, quiz_generator (generate + grade)
    ├── exporter/           md_exporter, pdf_exporter
    └── analytics/          tracker (user + admin stats)
```

The `lifespan` context manager in `main.py` opens the MongoDB connection pool on startup and closes it on shutdown, avoiding connection leaks.

```
+-------------------------------------------------------+
|                  FastAPI Backend                      |
|  +-----------+   +-----------+   +-----------+        |
|  |   API     |   |  Services |   |   Core    |        |
|  |  Routes   |-->|  Layer    |-->|  (DB,     |        |
|  |           |   |           |   |   Auth)   |        |
|  +-----------+   +-----------+   +-----------+        |
|         |              |               |              |
|         v              v               v              |
|   Pydantic        LangGraph        Motor /            |
|   validation      pipeline         python-jose        |
+-------------------------------------------------------+
```

*Fig. 6.1 — Component-level module breakdown.*

## 6.3 LangGraph Node Implementation

### 6.3.1 `node_extract` (Requirement Extraction)

`temperature=0` is used for full determinism. The system prompt requires strict JSON with four fields (`functional_requirements`, `non_functional_requirements`, `scale_hints`, `ambiguities`) and explicitly forbids markdown fences to keep `json.loads()` reliable. Errors are caught and surfaced as `state["error"]`.

### 6.3.2 `node_clarify` (Question Generation)

Triggered only when ambiguities are present and clarifications are absent. GPT-4o is prompted to produce 2–4 concise scoping questions. The pipeline then short-circuits to `END`; the API responds with `status: "awaiting_clarification"` and persists the partial design with the questions stored for the second pass.

### 6.3.3 `node_retrieve` (RAG)

Loads the FAISS index from a module-level singleton (lazy initialization on first request). The `similarity_search(query, k=3)` call is offloaded to a `ThreadPoolExecutor` via `loop.run_in_executor()` to preserve async concurrency:

```python
docs = await loop.run_in_executor(
    _executor,
    lambda: store.similarity_search(query, k=3),
)
return "\n\n---\n\n".join(d.page_content for d in docs)
```

### 6.3.4 `node_generate` (Architecture Generation)

`temperature=0.2` permits controlled variety in technology selection. The compound prompt contains the structured requirements, clarifications (empty dict on single-pass runs), and the RAG context under the literal heading `SIMILAR ARCHITECTURE PATTERNS FOR REFERENCE:`. The strict JSON schema includes 13 valid node types and explicit rules ("every edge must reference valid node ids", "include at least 6 nodes for any non-trivial system").

## 6.4 FAISS Vector Store Implementation

The corpus (`vector_store/seed_data/patterns.py`) contains 25 curated architecture patterns, each authored with a consistent structure: use case, components, communication, scaling, technology. On first server startup the patterns are embedded with `text-embedding-ada-002` (≈ 1–2 s total) and the resulting index is persisted to `vector_store/faiss_index/` via `FAISS.save_local()`. Subsequent restarts load the prebuilt index in ≈ 200 ms.

A module-level global `_vector_store` ensures the index is loaded once per process, while a `ThreadPoolExecutor(max_workers=2)` isolates the synchronous, CPU-bound FAISS operations from the async event loop.

If the index directory is deleted, `_load_or_create_store()` rebuilds it transparently on the next request — providing automatic recovery without manual intervention.

## 6.5 Explainability Engine

Invoked on demand by `POST /api/v1/explain/component`. GPT-4o is prompted (`temperature=0.3`) with the architecture summary and the clicked node's `label`, `type`, and `tech`. The response JSON contains five fields: `what`, `why`, `alternatives` (list), `trade_offs`, and `learn_more`. The result is cached in the design document's `explanations[component_id]` sub-document; repeated clicks return the cached result with zero latency.

## 6.6 Learn Mode and Quiz Engine

The static topic catalog (`services/learn_mode/topics.py`) contains 10 curated topics across three difficulty levels (beginner / intermediate / advanced). Each topic has a stable `id`, title, difficulty, estimated minutes, and prose description.

Quiz generation uses `temperature=0.7` to maximize variety across multiple attempts on the same topic. The system prompt enforces: exactly four options per question (a–d), scenario-based (not trivia) phrasing, plausible distractors, and 2–3 sentence explanations for each correct answer. Generated quizzes are stored in a process-level Python dict (`_quiz_cache`) keyed by UUID. Grading is exact-match against stored `correct_option_id`; pass threshold is 70%. On submission, a `quiz_attempt` document is inserted and `users.quiz_count` is incremented atomically.

> **Production note:** the in-process quiz cache is a known limitation. For horizontal scaling, this should be replaced with a Redis store with TTL.

## 6.7 Export Subsystem

The Markdown exporter renders a structured document with the problem statement, overview, tech stack, per-component sections (technology, description, and — if explained — *why* / *alternatives* / *trade-offs*), and data-flow list. The PDF exporter mirrors this structure using a Python PDF library with formatted sections and consistent typography. The frontend creates a blob URL, triggers a programmatic anchor click, then revokes the URL — all client-side.

## 6.8 Frontend Implementation

### 6.8.1 Route Structure

Under `frontend/app/`:

- `page.tsx` — landing page (public, hero CTA, redirects to dashboard if authenticated).
- `(auth)/login/page.tsx` — public sign-in page.
- `dashboard/`, `builder/`, `learn/`, `analytics/`, `admin/` — protected feature areas, each with a `layout.tsx` that wraps content in the `NavBar`.
- `builder/[designId]/page.tsx` — React Flow diagram view.
- `learn/[topic]/page.tsx` — topic detail + `QuizEngine`.

### 6.8.2 Middleware (Edge Runtime)

`middleware.ts` runs at the Vercel Edge Runtime and protects routes matching `/dashboard/:path*`, `/builder/:path*`, `/learn/:path*`, `/analytics/:path*`, and `/admin/:path*`. It reads and verifies the session cookie via the same HS256 `decode` function and redirects unauthenticated requests to `/login`. The `jose` library is used (not `jsonwebtoken`) because it operates without Node.js APIs.

### 6.8.3 React Flow Canvas

`ArchitectureCanvas.tsx` maps architecture JSON to React Flow `Node` and `Edge` objects. The `applyDagreLayout()` helper runs the dagre `LR` algorithm with `nodesep: 80` and `ranksep: 120`. Thirteen custom node renderers in `nodes/index.tsx` each render a colored icon background, label, tech label, and connection handles. On click, `onNodeClick` opens the `ExplainerPanel` — a slide-in drawer showing the five-field explanation with distinct typographic treatment.

### 6.8.4 Design System

The light-themed design system uses `#F8F9FB` as the body background, `#FFFFFF` cards with `1px #E8E9F0` borders, `#4F46E5` as the primary indigo action color, and `#0A0E2E` as the dark navigation surface. Typography pairs **Space Grotesk** (900-weight display) and **Inter** (body).

## 6.9 Prompt Engineering

Six design principles applied across all StructAI prompts:

1. **Schema-first output** — every prompt ends with `Return ONLY valid JSON (no markdown fences) matching this schema:`. This prevents triple-backtick wrapping that would break `json.loads()`.
2. **Persona priming** — each prompt opens with a role statement (*"You are a senior system design architect"*).
3. **Temperature tuning per role** (see Table 6.2).
4. **Explicit rules** — generation prompts list hard constraints ("every edge must reference valid node ids", "include at least 6 nodes").
5. **Context injection labels** — RAG patterns are injected under `SIMILAR ARCHITECTURE PATTERNS FOR REFERENCE:`, signaling inspiration rather than verbatim copying.
6. **Quality rules in the prompt itself** — quiz prompts enforce "scenario-based, not trivia", "plausible distractors", and "explanations must be educational".

**TABLE 6.2 — LLM Temperature Configuration Per Agent**

| Agent | Temperature | Rationale |
|---|---|---|
| Requirement extraction | 0.0 | Deterministic structured output |
| Clarification question generation | 0.0 | Consistent scoping |
| Architecture generation | 0.2 | Controlled variety in tech selection |
| Component explanation | 0.3 | Natural educational prose |
| Quiz generation | 0.7 | High variation across retakes |

---

---

# CHAPTER 7
# TESTING

## 7.1 Testing Strategy

A four-level testing strategy was applied: **unit tests** for individual functions (token decode, prompt builders, grading logic), **integration tests** for cross-module flows (pipeline + DB, FAISS + retrieval), **end-to-end tests** via HTTP from frontend to backend, and **manual exploratory testing** of the UI in Chrome, Firefox, and Safari.

## 7.2 Unit Testing

- **Token verification** — valid HS256 tokens decode to expected payload; tampered tokens raise `JWTError`; expired tokens raise `ExpiredSignatureError`.
- **Quiz grading** — exact-match grading against known answer maps; passing threshold computed correctly at the 70% boundary.
- **Markdown exporter** — given a fixed architecture JSON, exporter produces byte-identical Markdown.
- **`should_clarify` conditional** — returns `"clarify"` only when ambiguities present and clarifications absent; returns `"retrieve"` otherwise.

## 7.3 Integration Testing

- **Pipeline + MongoDB** — full design generation persists `architecture`, `status`, `requirements`, and timestamps correctly.
- **Two-pass flow** — first pass with ambiguous input persists `status: "awaiting_clarification"` and questions; second pass updates the document to `status: "complete"` with full architecture.
- **FAISS lazy init** — deleting `vector_store/faiss_index/` on disk triggers re-build on the next request; the index is identical after rebuild.
- **Auth middleware** — protected routes return 401 when no Bearer token is sent; valid token allows access; invalid signature returns 401.

## 7.4 End-to-End Testing

- Sign in via Google, generate a design ("Design a URL shortener for 10K req/sec"), confirm React Flow renders, click multiple nodes, confirm explanations differ per node and are cached on second click, download PDF and Markdown exports.
- Take a quiz on "Load Balancing" at beginner difficulty, intentionally fail (score < 70%), confirm UI shows amber color and explanations for incorrect answers; retake and pass, confirm green color.
- Admin path: promote a second account to admin via `PATCH /admin/users/{id}/role`, confirm the second account sees admin endpoints.

## 7.5 Test Cases and Results

**TABLE 7.1 — Representative Test Cases**

| TC ID | Test Case | Input | Expected Output | Result |
|---|---|---|---|---|
| TC-01 | Sign-in flow | Click "Continue with Google" | Redirect to Google; on success, redirect to `/dashboard` | PASS |
| TC-02 | Clear problem statement | "Design a URL shortener for 10K req/sec" | Single-pass; complete architecture returned | PASS |
| TC-03 | Ambiguous problem | "Build something for my startup" | Status `awaiting_clarification` with 2–4 questions | PASS |
| TC-04 | Clarification submit | Submit answers for TC-03 | Status `complete`; full architecture returned | PASS |
| TC-05 | Component explanation | Click any node | Five-field explanation rendered | PASS |
| TC-06 | Explanation caching | Click same node twice | Second click returns instantly from cache | PASS |
| TC-07 | Quiz generation | Topic = "Caching", difficulty = "beginner" | 5 MCQ questions, 4 options each | PASS |
| TC-08 | Quiz grading | Submit all-correct answers | Score = 100, passed = true, results array populated | PASS |
| TC-09 | PDF export | Click "Export PDF" on completed design | Browser downloads `structai-<id>.pdf` | PASS |
| TC-10 | Unauthorized access | API request without token | HTTP 401 Unauthorized | PASS |
| TC-11 | Cross-user access | User A queries User B's design id | HTTP 404 Not Found | PASS |
| TC-12 | Invalid JSON from LLM | Mocked GPT-4o returning malformed JSON | HTTP 500 with diagnostic | PASS |
| TC-13 | FAISS auto-recovery | Delete `faiss_index/` and submit a design | Index rebuilds; design generation succeeds | PASS |
| TC-14 | Admin role enforcement | Non-admin calls `GET /admin/users` | HTTP 403 Forbidden | PASS |
| TC-15 | Token tampering | Modify one character in JWT | HTTP 401 Unauthorized | PASS |

All 15 representative test cases passed. No critical, high, or medium-severity bugs were open at the time of the final demonstration.

---

---

# CHAPTER 8
# RESULTS AND DISCUSSION

## 8.1 Evaluation Setup

The evaluation was designed to answer four research questions:

- **RQ1:** Does RAG-augmented generation produce architecturally more complete outputs than non-RAG (prompt-only) generation?
- **RQ2:** How does StructAI's design generation time compare to manual design?
- **RQ3:** Is the multi-agent two-pass clarification protocol effective for ambiguous inputs?
- **RQ4:** Do users find the component explanations sufficient for understanding design decisions?

A benchmark of 30 problem statements was constructed across three categories (well-specified, partially-specified, ambiguous; 10 each). A user study recruited 20 participants — 10 undergraduate / graduate software engineering students and 10 industry practitioners with 2–10 years of experience. All GPT-4o calls used model version `gpt-4o-2024-08-06`. The backend ran on a Linux server with 8 vCPUs and 32 GB RAM; the frontend on a MacBook Pro M3 with 16 GB RAM.

## 8.2 RAG vs. Non-RAG Performance

Each of the 30 problems was generated twice: with RAG enabled (top-3 FAISS retrieval) and with RAG disabled. Two senior software engineers (8+ years system design experience) independently scored each output on a rubric covering component completeness, component-type correctness, edge coverage, technology appropriateness, and (for the 10 ambiguous problems) whether the system correctly entered the clarification flow.

**TABLE 8.1 — Architecture Completeness: RAG vs. Non-RAG (n = 30)**

| Metric | RAG-Augmented | Non-RAG Baseline | Improvement |
|---|---|---|---|
| Component Completeness (%) | **87.4** | 65.2 | **+34.0%** |
| Component Type Correctness (%) | 91.8 | 83.5 | +9.9% |
| Edge Coverage (%) | 84.6 | 71.3 | +18.7% |
| Technology Appropriateness (%) | 89.1 | 78.6 | +13.4% |
| Ambiguous Input Handled Correctly | 9/10 | 6/10 | +30.0% |

Inter-rater agreement was substantial: Cohen's κ = 0.74.

```
            RAG-Augmented vs Non-RAG (% scores)

  Completeness   |████████████████████| 87.4
                 |█████████████       | 65.2
  Type Correct   |█████████████████████| 91.8
                 |█████████████████   | 83.5
  Edge Coverage  |████████████████████| 84.6
                 |██████████████      | 71.3
  Tech Appropr.  |█████████████████████| 89.1
                 |████████████████    | 78.6

                  ■ RAG     ■ Non-RAG
```

*Fig. 8.1 — RAG vs. non-RAG completeness comparison.*

## 8.3 User Study Results

Twenty participants completed two tasks each: (A) designing a specified system manually using pen-and-paper or a tool of their choice, and (B) generating the same system with StructAI. Task completion times were recorded; post-task, participants rated explanation quality on a 5-point Likert scale.

**TABLE 8.2 — User Study Results (n = 20)**

| Metric | StructAI | Manual Design | Difference |
|---|---|---|---|
| Mean task completion time (min) | **4.2** | 46.8 | **−42.6 min (−91%)** |
| Median task completion time (min) | 3.8 | 41.5 | — |
| Explanation quality (mean Likert) | **4.1 / 5.0** | — | — |
| Explanation quality (% rating ≥ 4/5) | 80% | — | — |
| Participants preferring StructAI for first-draft design | 18 / 20 | — | — |

```
   Task completion time (minutes)

   StructAI :  ▓▓▓▓ 4.2
   Manual   :  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 46.8
              0      10      20      30      40      50
```

*Fig. 8.2 — Task completion time distribution.*

## 8.4 Ablation Study

To isolate the contribution of each pipeline component, an ablation study was conducted on the 10 well-specified problems with four configurations.

**TABLE 8.3 — Ablation Study Results (n = 10)**

| Configuration | Component Completeness (%) | Edge Coverage (%) |
|---|---|---|
| Full pipeline (RAG + clarification) | **91.2** | **87.4** |
| RAG only (no clarification node) | 89.3 | 85.1 |
| Clarification only (no RAG) | 70.4 | 73.6 |
| Neither (direct generation) | 65.8 | 70.9 |

The ablation confirms that **RAG contributes the dominant improvement** (+23.5 percentage points over the no-RAG baseline), while the clarification node adds a secondary improvement primarily on ambiguous inputs. For well-specified inputs, the clarification node has negligible effect — consistent with the conditional-edge design that bypasses it when no ambiguities are detected.

## 8.5 Discussion

**RQ1 (RAG vs. Non-RAG):** The 34% improvement in component completeness confirms that GPT-4o's parametric knowledge of architectural patterns, while broad, produces lower-fidelity outputs for specific system types than retrieval from a curated, domain-specific corpus. This aligns with the theoretical analysis of Pan et al. [13] who argue that grounding is necessary for LLMs to produce factually reliable outputs in knowledge-intensive domains.

**RQ2 (Design time):** The 11× reduction in task completion time is practically significant. A 4.2-minute first-draft architecture allows engineering teams to evaluate multiple architectural approaches in the time previously required to produce one. This is consistent with the transformative time savings reported by Fan et al. [10] for LLM-assisted software engineering tasks more broadly.

**RQ3 (Two-pass protocol):** The two-pass clarification protocol successfully resolved ambiguities in 9 of 10 ambiguous inputs. The single failure case involved a problem statement requiring domain knowledge outside the FAISS corpus (medical device firmware), confirming that the corpus-coverage limitation manifests more strongly than the multi-agent coordination limitation.

**RQ4 (Explanation quality):** The 4.1/5.0 Likert rating validates the explainability design choices motivated by Tantithamthavorn and Jiarpakdee [4] and Arora et al. [5]. Participants specifically cited the `alternatives` and `trade_offs` fields as the most valuable for understanding design rationale — consistent with the recommendation of [5] that decision-level explanations are more actionable than model-level ones.

## 8.6 Limitations and Threats to Validity

**Limitations:**

1. **GPT-4o dependency** — generation quality and operating cost are tied to OpenAI's hosted model. A future fine-tuned open-source model could mitigate this.
2. **FAISS corpus coverage** — the 25-pattern corpus covers common web/mobile/streaming architectures well but lacks specialized domains (embedded, scientific HPC).
3. **In-process quiz cache** — process-local Python dict is not suitable for multi-process production deployments; Redis is required for horizontal scaling.
4. **Evaluation scale** — 30 problems and 20 participants are limited; larger evaluations are needed for strong generalization claims.
5. **Subjective quality metric** — human-rated completeness introduces inter-rater variability (κ = 0.74). An automated metric would improve reproducibility.

**Threats to validity:**

- *Internal:* GPT-4o's non-zero temperature (0.2) introduces stochastic variation; each condition was run once rather than averaged across multiple runs.
- *External:* problem statements were authored by the research team and may not represent the full distribution of real-world inputs.
- *Construct:* "component completeness" is inherently domain-dependent; the rubric was calibrated on 5 pilot problems but may not transfer uniformly across all domains.

---

---

# CHAPTER 9
# CONCLUSION AND FUTURE SCOPE

## 9.1 Conclusion

This project presented **StructAI**, a full-stack multi-agent LLM platform for automated software architecture design and education. The system makes six concrete technical contributions:

1. A four-node **LangGraph state machine** with typed state propagation and conditional ambiguity routing, decomposing the design task across specialized agents.
2. A **dual-pass clarification protocol** that cleanly separates requirement scoping from architecture generation without a stateful session server.
3. A **FAISS-backed RAG subsystem** grounded in 25 curated real-world architecture patterns, persisted to disk for fast cold-starts.
4. A **per-component explainability engine** providing structured five-field decision rationale.
5. An **adaptive quiz module** for in-platform skill development across ten curated topics.
6. An **Edge-Runtime-compatible custom HS256 JWT** architecture bridging Next.js middleware and FastAPI through a single shared secret.

Empirical evaluation demonstrates that RAG augmentation improves architectural completeness by **34%** over non-RAG baselines, the full pipeline reduces task completion time by **91%** compared to manual design (11× speedup), and the explanation engine achieves a mean Likert score of **4.1 / 5.0** for educational sufficiency. Taken together, these results establish StructAI as an effective platform for both professional architecture prototyping and software engineering education.

## 9.2 Future Scope

Six directions extend the current work:

1. **Graph RAG integration.** Replace flat vector retrieval with a knowledge graph of architectural patterns representing structural relationships (e.g., *"CDN precedes load balancer"*, *"Kafka requires Zookeeper"*). Following the roadmap of Pan et al. [13] and the survey of Procko and Ochoa [7], this would enable semantically richer retrieval that respects topology constraints.

2. **Domain-specific fine-tuning.** Fine-tune a smaller open-source model (e.g., Llama 3 70B) on a curated dataset of (problem statement, architecture) pairs to reduce GPT-4o dependency, inference cost, and latency.

3. **Infrastructure-as-Code export.** Extend the export subsystem to generate Terraform, Pulumi, and Kubernetes manifests directly from the architecture graph, closing the loop between design and deployment.

4. **Real-time collaborative editing.** Add WebSocket-based multi-user editing of diagrams to enable team-based design reviews within the platform.

5. **Automated evaluation metric.** Develop a reference-free architecture quality metric (analogous to BERTScore for text) that quantifies completeness and structural correctness without human raters, enabling large-scale automated benchmarking.

6. **Longitudinal user study.** Deploy StructAI to a software engineering course cohort over a semester to measure impact on system design interview outcomes and architectural reasoning skill development through pre/post evaluation.

The combination of grounded generation, structured explanation, and pedagogical scaffolding positions StructAI as a foundation upon which subsequent work can build toward an AI-augmented software architecture workflow for both industry and education.

---

---

## REFERENCES

[1] M. A. K. Raiaan, M. S. H. Mukta, K. Fatema, N. M. Fahad, S. Sakib, M. M. J. Mim, J. Ahmad, M. E. Ali, and S. Azam, "A review on large language models: Architectures, applications, taxonomies, open issues and challenges," *IEEE Access*, vol. 12, pp. 26839–26874, 2024, doi: 10.1109/ACCESS.2024.3365742.

[2] K. Chen, Y. Yang, B. Chen, J. A. H. López, G. Mussbacher, and D. Varró, "Automated domain modeling with large language models: A comparative study," in *Proc. ACM/IEEE 26th Int. Conf. Model Driven Engineering Languages and Systems (MODELS)*, 2023, pp. 137–147, doi: 10.1109/MODELS58315.2023.00037.

[3] A. F. Tekgöz, İ. K. Şahin, and B. Aydın, "Evaluation of vector database and LLM models in retrieval-augmented generation (RAG) systems," in *Proc. 10th Int. Conf. Computer Science and Engineering (UBMK)*, 2025.

[4] C. Tantithamthavorn and J. Jiarpakdee, "Explainable AI for software engineering," in *Proc. 36th IEEE/ACM Int. Conf. Automated Software Engineering (ASE)*, 2021, pp. 1–4, doi: 10.1109/ASE51524.2021.00009.

[5] S. Arora, A. Easwaran, and A. Chaudhary, "Explainable artificial intelligence techniques for software development lifecycle: A phase-specific survey," in *Proc. IEEE 49th Annu. Computers, Software, and Applications Conf. (COMPSAC)*, 2025.

[6] S. Arulmohan, M.-J. Meurs, and S. Mosser, "Extracting domain models from textual requirements in the era of large language models," in *Proc. ACM/IEEE Int. Conf. Model Driven Engineering Languages and Systems Companion (MODELS-C)*, 2023, doi: 10.1109/MODELS-C59198.2023.00096.

[7] C. Procko and J. Ochoa, "Graph retrieval-augmented generation for large language models: A survey," in *Proc. IEEE Conf. Artificial Intelligence Enabled Software Engineering and Testing (AIxSET)*, 2024.

[8] A. Mushtaq, R. Naeem, I. Ghaznavi, I. Taj, I. Hashmi, and J. Qadir, "Harnessing multi-agent LLMs for complex engineering problem-solving: A framework for senior design projects," in *Proc. IEEE Global Engineering Education Conf. (EDUCON)*, 2025.

[9] V. Gogineni, "LLM-powered multi-agent systems: A technical framework for collaborative intelligence through optimized knowledge retrieval and communication," in *Proc. IEEE 3rd Int. Conf. Artificial Intelligence, Computing, Engineering and Science (AIRC)*, 2025.

[10] A. Fan, B. Gokkaya, M. Harman, M. Lyubarskiy, S. Sengupta, S. Yoo, and J. M. Zhang, "Large language models for software engineering: Survey and open problems," in *Proc. IEEE/ACM Int. Conf. Software Engineering: Future of Software Engineering (ICSE-FoSE)*, 2023, doi: 10.1109/ICSE-FoSE59343.2023.00008.

[11] M. Shao, A. Basit, R. Karri, and M. Shafique, "Survey of different large language model architectures: Trends, benchmarks, and challenges," *IEEE Access*, vol. 12, 2024, doi: 10.1109/ACCESS.2024.3482107.

[12] W. Fan, P. Wu, Y. Ding, L. Ning, S. Wang, and Q. Li, "Towards retrieval-augmented large language models: Data management and system design," in *Proc. IEEE 41st Int. Conf. Data Engineering (ICDE)*, 2025, doi: 10.1109/ICDE65448.2025.00341.

[13] S. Pan, L. Luo, Y. Wang, C. Chen, J. Wang, and X. Wu, "Unifying large language models and knowledge graphs: A roadmap," *IEEE Trans. Knowledge and Data Engineering*, vol. 36, no. 7, pp. 3580–3599, Jul. 2024, doi: 10.1109/TKDE.2024.3352100.

---

---

## APPENDIX A — SYSTEM PROMPT TEMPLATES

### A.1 Requirement Extraction Prompt (`temperature = 0`)

```
You are a senior system design architect.
Extract requirements from the user's problem statement and identify any ambiguities.

Return ONLY valid JSON matching this schema (no markdown fences):
{
  "functional_requirements": ["<string>", ...],
  "non_functional_requirements": ["<string>", ...],
  "scale_hints": {
    "users": "<estimate>",
    "reads_per_sec": "<estimate>",
    "writes_per_sec": "<estimate>",
    "data_size": "<estimate>"
  },
  "ambiguities": ["<unclear aspect>", ...]
}
```

### A.2 Clarification Prompt (`temperature = 0`)

```
You are a senior system design architect conducting a scoping session.
Given the extracted requirements and ambiguities, generate 2–4 concise clarifying questions
that would meaningfully improve the architecture design.

Return ONLY valid JSON (no markdown fences):
{ "questions": ["<question>", ...] }
```

### A.3 Architecture Generation Prompt (`temperature = 0.2`)

```
You are a world-class system design architect.
Design a complete, production-grade system architecture based on the requirements
and similar patterns below.

Return ONLY valid JSON (no markdown fences) matching this exact schema:
{
  "nodes": [
    {
      "id": "<kebab-case unique id>",
      "type": "<client|api_gateway|load_balancer|web_server|database|nosql_database|
               cache|message_queue|cdn|object_storage|auth_service|monitoring|ml_service>",
      "label": "<display name>",
      "description": "<one-line description>",
      "tech": "<recommended technology>"
    }
  ],
  "edges": [
    {
      "id": "<unique id>",
      "source": "<node id>",
      "target": "<node id>",
      "label": "<protocol or relationship>",
      "animated": <true for async/real-time, false otherwise>
    }
  ],
  "tech_stack": ["<technology>", ...],
  "summary": "<2–3 sentence overview>"
}

Rules:
- Include all components needed for a production system (auth, monitoring, caching, etc.)
- Every edge must reference valid node ids
- Prefer battle-tested technologies unless requirements suggest otherwise
- Include at least 6 nodes for any non-trivial system
```

### A.4 Component Explanation Prompt (`temperature = 0.3`)

```
You are a senior system design mentor explaining architecture decisions to a student or developer.
Given an architecture component, explain it clearly and concisely.

Return ONLY valid JSON (no markdown fences):
{
  "what": "<1–2 sentence description of what this component is>",
  "why": "<2–3 sentences on why it was chosen for this specific system>",
  "alternatives": ["<alternative tech or pattern>", "<another>"],
  "trade_offs": "<2–3 sentences on key trade-offs>",
  "learn_more": "<one key concept to study to go deeper>"
}
```

---

## APPENDIX B — API ENDPOINT REFERENCE

All endpoints prefixed `/api/v1`. Endpoints marked 🔓 are unauthenticated; all others require `Authorization: Bearer <hs256_jwt>`.

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | 🔓 `/auth/upsert-user` | None | Sync Google user to MongoDB on first login |
| GET | `/auth/me` | JWT | Return authenticated user profile |
| POST | `/designs/generate` | JWT | Submit problem statement; run pipeline |
| POST | `/designs/{id}/clarify` | JWT | Submit clarification answers |
| GET | `/designs/{id}` | JWT | Fetch single design document |
| GET | `/designs/` | JWT | List user's designs (last 20) |
| DELETE | `/designs/{id}` | JWT | Delete design; decrement design_count |
| POST | `/explain/component` | JWT | Generate component explanation |
| GET | 🔓 `/learn/topics` | None | List all 10 topic definitions |
| GET | 🔓 `/learn/topics/{topic_id}` | None | Get single topic detail |
| POST | `/learn/quiz/generate` | JWT | Generate quiz for a topic |
| POST | `/learn/quiz/submit` | JWT | Grade quiz; persist attempt |
| GET | `/export/{design_id}/pdf` | JWT | Download design as PDF |
| GET | `/export/{design_id}/markdown` | JWT | Download design as Markdown |
| GET | `/analytics/me` | JWT | Current user's stats and history |
| GET | `/analytics/admin` | Admin | Platform-wide statistics |
| GET | `/admin/health` | Admin | Service health check |
| GET | `/admin/users` | Admin | Paginated user list |
| PATCH | `/admin/users/{id}/role` | Admin | Change user role |
| POST | `/admin/rebuild-index` | Admin | Rebuild FAISS vector index |
| GET | 🔓 `/health` | None | `{"status":"ok"}` liveness probe |

---

## APPENDIX C — SAMPLE OUTPUT

**Input problem statement:** *"Design a food delivery platform like DoorDash for 1M users."*

**Generated architecture JSON (excerpt):**

```json
{
  "nodes": [
    { "id": "mobile-client", "type": "client", "label": "Mobile App",
      "description": "Consumer & courier apps", "tech": "React Native" },
    { "id": "api-gateway", "type": "api_gateway", "label": "API Gateway",
      "description": "Single entry for all client traffic", "tech": "Kong" },
    { "id": "auth", "type": "auth_service", "label": "Auth Service",
      "description": "OAuth + JWT issuance", "tech": "Auth0" },
    { "id": "order-svc", "type": "web_server", "label": "Order Service",
      "description": "Order lifecycle management", "tech": "FastAPI" },
    { "id": "match-svc", "type": "web_server", "label": "Matching Service",
      "description": "Courier-order matching", "tech": "Go" },
    { "id": "orders-db", "type": "database", "label": "Orders DB",
      "description": "Transactional store", "tech": "PostgreSQL" },
    { "id": "cache", "type": "cache", "label": "Redis Cache",
      "description": "Hot-path read cache", "tech": "Redis" },
    { "id": "events", "type": "message_queue", "label": "Event Bus",
      "description": "Async order events", "tech": "Kafka" }
  ],
  "edges": [
    { "id": "e1", "source": "mobile-client", "target": "api-gateway",
      "label": "HTTPS", "animated": false },
    { "id": "e2", "source": "api-gateway", "target": "auth",
      "label": "verify", "animated": false },
    { "id": "e3", "source": "order-svc", "target": "events",
      "label": "publish", "animated": true }
  ],
  "tech_stack": ["React Native", "Kong", "FastAPI", "Go",
                 "PostgreSQL", "Redis", "Kafka", "Auth0"],
  "summary": "A microservices-based food delivery platform with an API
              gateway, OAuth-secured auth, an order service backed by
              PostgreSQL, a Go-based matching service, and Kafka for
              async event propagation."
}
```

**Sample component explanation (clicked on `cache` node):**

```json
{
  "what": "Redis is an in-memory key-value store used as a low-latency
           read cache in front of the orders database.",
  "why": "DoorDash-scale read traffic on menu and restaurant data
          dwarfs writes; caching these reads in Redis cuts P95 read
          latency by an order of magnitude and reduces load on the
          primary database.",
  "alternatives": ["Memcached", "DynamoDB DAX", "Hazelcast"],
  "trade_offs": "Adds operational complexity (cache invalidation,
                 memory management) and introduces eventual
                 consistency on cached reads. Mitigated via
                 write-through invalidation on update.",
  "learn_more": "Read-through vs. write-through caching strategies"
}
```

---

**— End of Project Report —**
