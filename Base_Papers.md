# Base Papers Index

> **Research Paper Repository — StructAI Project**
>
> All content is reproduced verbatim from the respective publications.
> For academic reference and research paper drafting purposes only.

---

## Table of Contents

- [P-01 — A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges](#p01-----a-review-on-large-language-models-architectures-applications-taxonomies-open-issues-and-challenges)
- [P-02 — Automated Domain Modeling with Large Language Models: A Comparative Study](#p02-----automated-domain-modeling-with-large-language-models-a-comparative-study)
- [P-03 — Evaluation of Vector Database and LLM Models in Retrieval-Augmented Generation (RAG) Systems](#p03-----evaluation-of-vector-database-and-llm-models-in-retrieval-augmented-generation-rag-systems)
- [P-04 — Explainable AI for Software Engineering](#p04-----explainable-ai-for-software-engineering)
- [P-05 — Explainable Artificial Intelligence Techniques for Software Development Lifecycle: A Phase-Specific Survey](#p05-----explainable-artificial-intelligence-techniques-for-software-development-lifecycle-a-phase-specific-survey)
- [P-06 — Extracting Domain Models from Textual Requirements in the Era of Large Language Models](#p06-----extracting-domain-models-from-textual-requirements-in-the-era-of-large-language-models)
- [P-07 — Graph Retrieval-Augmented Generation for Large Language Models: A Survey](#p07-----graph-retrieval-augmented-generation-for-large-language-models-a-survey)
- [P-08 — Harnessing Multi-Agent LLMs for Complex Engineering Problem-Solving: A Framework for Senior Design Projects](#p08-----harnessing-multi-agent-llms-for-complex-engineering-problem-solving-a-framework-for-senior-design-projects)
- [P-09 — LLM-Powered Multi-Agent Systems: A Technical Framework for Collaborative Intelligence Through Optimized Knowledge Retrieval and Communication](#p09-----llm-powered-multi-agent-systems-a-technical-framework-for-collaborative-intelligence-through-optimized-knowledge-retrieval-and-communication)
- [P-10 — Large Language Models for Software Engineering: Survey and Open Problems](#p10-----large-language-models-for-software-engineering-survey-and-open-problems)
- [P-11 — Survey of Different Large Language Model Architectures: Trends, Benchmarks, and Challenges](#p11-----survey-of-different-large-language-model-architectures-trends-benchmarks-and-challenges)
- [P-12 — Towards Retrieval-Augmented Large Language Models: Data Management and System Design](#p12-----towards-retrieval-augmented-large-language-models-data-management-and-system-design)
- [P-13 — Unifying Large Language Models and Knowledge Graphs: A Roadmap](#p13-----unifying-large-language-models-and-knowledge-graphs-a-roadmap)

---

<br>

<a id="p01-----a-review-on-large-language-models-architectures-applications-taxonomies-open-issues-and-challenges"></a>

## P-01 — A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges

| Field | Details |
|-------|---------|
| **Paper ID** | `P-01` |
| **Title** | A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges |
| **Authors** | Mohaimenul Azam Khan Raiaan, Md. Saddam Hossain Mukta, Kaniz Fatema, Nur Mohammad Fahad, Sadman Sakib, Most Marufatul Jannat Mim, Jubaer Ahmad, Mohammed Eunus Ali, and Sami Azam |
| **Affiliation(s)** | (1) Department of Computer Science and Engineering, United International University, Dhaka, Bangladesh<br>(2) LUT School of Engineering Sciences, Lappeenranta-Lahti University of Technology, Finland<br>(3) Faculty of Science and Technology, Charles Darwin University, Australia<br>(4) Department of CSE, BUET, Bangladesh |
| **Venue** | IEEE Access |
| **Volume / Year** | Vol. 12, 2024 |
| **DOI** | [10.1109/ACCESS.2024.3365742](https://doi.org/10.1109/ACCESS.2024.3365742) |
| **Dates** | Received: 14 January 2024 | Accepted: 5 February 2024 | Published: 13 February 2024 | Current Version: 23 February 2024 |

---

Received 14 January 2024, accepted 5 February 2024, date of publication 13 February 2024, date of current version 23 February 2024.

Digital Object Identifier 10.1109/ACCESS.2024.3365742

A Review on Large Language Models:
Architectures, Applications,
Taxonomies, Open Issues
and Challenges

MOHAIMENUL AZAM KHAN RAIAAN 1, MD. SADDAM HOSSAIN MUKTA 2,
KANIZ FATEMA 3, NUR MOHAMMAD FAHAD1, SADMAN SAKIB 1,
MOST MARUFATUL JANNAT MIM 1, JUBAER AHMAD1, MOHAMMED EUNUS ALI 4,
AND SAMI AZAM 3
1Department of Computer Science and Engineering, United International University, Dhaka 1212, Bangladesh
2LUT School of Engineering Sciences, Lappeenranta-Lahti University of Technology, 53850 Lappeenranta, Finland
3Faculty of Science and Technology, Charles Darwin University, Casuarina, NT 0909, Australia
4Department of CSE, Bangladesh University of Engineering and Technology (BUET), Dhaka 1000, Bangladesh

Corresponding author: Md. Saddam Hossain Mukta (Saddam.Mukta@lut.fi)


### Abstract

Large Language Models (LLMs) recently demonstrated extraordinary capability in various
natural language processing (NLP) tasks including language translation, text generation, question answering,
etc. Moreover, LLMs are new and essential part of computerized language processing, having the ability to
understand complex verbal patterns and generate coherent and appropriate replies in a given context. Though
this success of LLMs has prompted a substantial increase in research contributions, rapid growth has made it
difficult to understand the overall impact of these improvements. Since a plethora of research on LLMs have
been appeared within a short time, it is quite impossible to track all of these and get an overview of the current
state of research in this area. Consequently, the research community would benefit from a short but thorough
review of the recent changes in this area. This article thoroughly overviews LLMs, including their history,
architectures, transformers, resources, training methods, applications, impacts, challenges, etc. This paper
begins by discussing the fundamental concepts of LLMs with its traditional pipeline of the LLMs training
phase. Then the paper provides an overview of the existing works, the history of LLMs, their evolution
over time, the architecture of transformers in LLMs, the different resources of LLMs, and the different
training methods that have been used to train them. The paper also demonstrates the datasets utilized in the
studies. After that, the paper discusses the wide range of applications of LLMs, including biomedical and
healthcare, education, social, business, and agriculture. The study also illustrates how LLMs create an impact
on society and shape the future of AI and how they can be used to solve real-world problems. Finally, the
paper also explores open issues and challenges to deploy LLMs in real-world scenario. Our review paper
aims to help practitioners, researchers, and experts thoroughly understand the evolution of LLMs, pre-trained
architectures, applications, challenges, and future goals.


### Index Terms / Keywords

Large language models (LLM), natural language processing (NLP), artificial intelligence,
transformer, pre-trained models, taxonomy, application.


### I. Introduction
Language is a vital tool for human expression and com-
munication which we begin to learn after our birth and

The associate editor coordinating the review of this manuscript and

approving it for publication was Bo Pu

.

make diverse use of it throughout our lifetime [1], [2].
Nevertheless, machines are unable to possess the innate
ability to understand and speak in human language without
the help of sophisticated artificial
intelligence (AI) [3].
Therefore, a long-standing scientific challenge and aim
has been to achieve human-like reading, writing, and

VOLUME 12, 2024


2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

26839


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 1. Pipeline of the LLMs training phase.

communication skills in machines [4]. Advances in deep
learning approaches, the availability of immense computer
resources, and the availability of vast quantities of training
data all contributed to the emergence of large language
models (LLMs). LLMs are category of language models that
utilizes neural networks containing billions of parameters,
trained on enormous quantities of unlabeled text data using
a self-supervised learning approach [5]. Frequently pre-
training on large corpora from the web,
these models
may learn complicated patterns, language subtleties, and
semantic linkages. However, LLMs have proved their ability
in various language-related tasks, including text synthesis,
translation, summarization, question-answering, and senti-
ment analysis, by leveraging deep learning techniques and
large datasets. Moreover, fine-tuning these models on specific
downstream tasks has been quite promising, with state-
of-the-art performance in several benchmarks [6]. LLMs
have their roots in the early development of language
models and neural networks. Statistical approaches and
n-gram models were used in earlier attempts to develop
language models [7]; but these models have shortcomings
in
in expressing long-term interdependence and context
language. After that, researchers began to explore more
complex ways with the development of neural networks
and the availability of larger datasets. The creation of
the Recurrent Neural Network (RNN) [8], which allowed
for the modeling of sequential data, including language,
was a crucial milestone. However, RNNs were limited in
their efficacy due to vanishing gradients and long-term
dependencies. The significant advancement in LLMs systems
occurred when the transformer architecture was introduced in
the seminal work [9]. The transformer model is built around
the self-attention mechanism, enabling parallelization and
efficient handling of long-range dependencies. Furthermore,
LLM architectures served as the basis for models such
as Google’s Bidirectional Encoder Representations from
Transformers (BERT) [10] and open AI’s Generative Pre-
trained Transformer (GPT) series, which excelled at various
language tasks.

The pipeline of the basic LLMs architecture is shown
in Figure 1. LLMs architecture receives text data from
multiple sources and then the architecture forwards text to
the subsequent stage for preprocessing. It then completes its
training process by executing a series of stages, including
random parameter initialization, numerical data input, loss
function calculation, parameter optimization, and iterative
training. They offer text translation, text summarization,
sentiment analysis, and other services following the training
phase. Prior research has shown the potential of LLMs
in many NLP tasks, including specialized applications in
domains such as the medical and health sciences [11] and
politics [12]. Moreover, after inventing the most sophisticated
GPT model [13], developing the state-of-the-art models
(LLaMa and Bard [14]), and exploring their capabilities, such
as Alpaca and GPTHuggingface [15], LLM has become a
crucial and effective domain. As a result, a trustworthy assess-
ment of current LLMs research is becoming increasingly
important, and prior research has shown the potential and
superiority of LLMs in NLP tasks. Despite this, only a few
studies [3], [16], [17] have thoroughly reviewed latest LLMs
developments, possibilities, and limitations in their research.
Besides, researchers have presented various aspects of
the LLMs domain in several studies [3], [16], [17], [18];
but their work still has several limitations. These studies
miss many aspects of LLM including high-level architecture
and configurations, taxonomies, API and domain-specific
applications, and datasets of LLMs. For example,
there
is a lack of introduction to the core architecture and
configurations of the LLMs model, a lack of adequate
explanation of the taxonomy of LLMs, differentiation based
on ML, domain-specific applications, API applications, and
descriptions of LLMs datasets. Furthermore, the vast majority
of LLMs review papers are not peer-reviewed works. The
absence of these key points in a review indicates that a
thorough investigation is missing in the current literature.
Due to the significant extent of the constraints, it is possible
to mitigate these research gaps by thoroughly analyzing and
addressing these missing points. Thus, the motivation of

26840

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 2. Section organization of the review.

this paper is to comprehensively explore the current review
papers, identify their limitations, and outline the current
state-of-the-art methods to address these vital challenges.
Therefore, our primary objective is to explore, comprehend,
and evaluate LLMs that encompass domains, evolution,
classification, the structure of pre-trained models, resources,
and real-time applications. Additionally, our comprehensive
review discusses open issues and challenges associated with
LLMs, including security, ethical, privacy, economic, and
environmental considerations. In addition, we present a set
of guidelines to explore future research and development
in the effective use of LLMs. We hope that this study will
contribute to a better understanding and use of LLMs. The
list of contributions to this paper is as follows:

- Providing a complete overview of LLMs, including their
evolution, classification, and transformer architecture.
The history of LLMs provides a brief account of the
evaluation from its origins (1940) to the present (2023),
as well as a taxonomy of LLMs based on pre-trained and
API-based models and major LLMs structures.

- Describing the comparison of different pre-trained
model designs in LLMs, along with their own systems
that show how the model architectures are different.
- Explaining the influence of ML models on LLMs,
demonstrating the significance of ML in various LLMs
domains.

- Providing a brief overview of the datasets used in the
training phase to differentiate between the models in
existing works.

- Presenting a thorough explanation of the hardware
implementation in training and testing models in terms
of LLMs.

- Defining insights into the potential of LLMs and their
impact on society and demonstrating bio-medical appli-
cations in five practical domains, including bio-medical
and healthcare, education, social media, business, and
agriculture.

- Investigating LLMs’s diverse set of open issues, chal-
lenges, and future opportunities. This section focuses on
identifying key challenges and future opportunities that
can aid in advancing knowledge in this area.

The remaining sections of the paper are organized as
depicted in Figure 2. In Section II, the literature review is dis-
cussed. Section III illustrates the history of LLMs; Section IV
demonstrates the Methodology; Section V explains the clear
concept of large language models; Section VI describes the
resources of LLMs; Section VII demonstrates the domain-
specific applications of LLMs; and Section VIII explains
the societal
impact of LLMs, Indusrial significance of
LLMs is highlighted in Section IX, Section X discuss the
open issues and challenges regarding LLMs, Section XI
discusses about the future research directions of LLMs,
Section XII acknowledges the limitation and Section XIII
finally concludes the paper.


### II. Literature Review
The growing number of LLMs is an extraordinary develop-
ment in the field of AI. In recent years, numerous studies [3],
[16], [17], [18] have been conducted to investigate and
evaluate their capabilities. Researchers from various fields
have contributed on the rise of LLMs, shedding light on
their remarkable advancements, diverse applications, and
potential to revolutionize tasks from text generation and com-
prehension to demonstrating reasoning skills. Collectively,

VOLUME 12, 2024

26841

TABLE 1. Comparison between state-of-the-art research.


#### M. A. K. Raiaan et al.: Review on Large Language Models

these studies contribute to our comprehension of LLMs’
significant role in shaping the landscape of AI-driven
language processing and problem-solving.

Huang et al., [18] presented a study on reasoning in
LLMs that comprehensively summarizes the current state of
LLMs’ reasoning capabilities. It examines various aspects of
reasoning in LLMs, such as techniques to enhance and extract
reasoning abilities, methodologies and criteria for assessing
these abilities, insights from prior research, and suggestions
for future directions. The primary concern is the extent to
which LLMs can demonstrate reasoning skills. This paper
aims to provide an in-depth and up-to-date examination of
this topic, fostering fruitful discussions and guiding future
research in LLMs-based reasoning. In another study, Zhao
et al., [3] survey on LLMs illustrates a comprehensive
examination of the evolution and impact of LLMs in the field
of artificial intelligence and natural language processing.
It traces the historical journey from early language models
to the recent emergence of pre-trained language models
(PLMs) with billions of parameters. Notably,
the paper
discusses LLMs’ unique capabilities as they scale in size,
including in-context
the
significant contributions of LLMs to the AI community and
the launch of ChatGPT, a prominent AI chatbot powered
by LLMs. The survey is structured around four key aspects
of LLMs: pre-training, adaptation tuning, utilization, and
capacity evaluation. Additionally, the paper provides insights
into available resources for LLMs development and identifies
further research and development areas.

learning. The authors highlight

A recent study by Fan et al. [16] conducted a bibliometric
review of LLMs research from 2017 to 2023, encompass-
ing over 5,000 publications. The study aims to provide
researchers, practitioners, and policymakers with an overview
of the evolving landscape of LLMs research. The study
also tracks research trends during the specified time period,
including advancements in fundamental algorithms, major

NLP tasks, and applications in disciplines such as medicine,
engineering, social sciences, and the humanities. In addition
to highlighting the dynamic and rapidly changing nature of
LLMs research, the study offers insights into their current
status, impact, and potential in the context of scientific
and technological advancements. Chang et al. [17] focuses
on the assessment of LMMs. Their research examines the
increasing prevalence of LLMs in academia and industry
due to their exceptional performance in various applica-
tions. The study highlights the growing significance of
evaluating LLMs at both the task and societal levels in
order to comprehend potential risks. The paper thoroughly
analyzes LLMs evaluation methods, focusing on three critical
dimensions: what to evaluate, where to evaluate, and how
to evaluate. The research also includes tasks such as natural
language processing, reasoning, medical applications, ethics,
and education. The article examines evaluation methods and
benchmarks for assessing LLMs performance, emphasizing
successful and unsuccessful cases. The paper also underlines
future challenges in LLMs evaluation and emphasizes the
importance of evaluating LLMs as a fundamental discipline
to support the development of more competent LLMs.

Table 1 illustrates the comparison between different review
papers based on some fundamental properties such as LLMs
models, APIs, datasets, domain specific LLMs, ml-based
comparison of LLMs, taxonomy, architectures, performance,
hardware specifications for testing and training, and config-
urations. Huang et al. [18] lack information on LLMs’ API,
dataset, domain-specific LLMs, taxonomy, architectures, and
LLMs Configurations. In contrast, Zhao et al., [3] has missing
aspects on LLMs’ API, domain-specific LLMs, taxonomy,
architecture, and configurations. Moreover, Fan et al. [16] and
Chang et al., [17] lack information on LLMs’ API, domain-
specific LLMs, taxonomy, architecture, and configurations.
On the contrary, our paper offers a considerably broader
aspects on the LLMs context. In addition to incorporating

26842

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

every aspect specified in the table, we provide a detailed
demonstration on the account of the hardware implemen-
tation and LLMs datasets. Previous research frequently
focuses on limited aspects of LLMs, including historical
development, bibliometric patterns, and assessment tech-
niques. However, our study recovers previous shortcomings.
A thorough examination is conducted on each of these
aspects, resulting in a comprehensive representation of
the strengths and weaknesses of LLMs. Furthermore, our
research is focused on the crucial element of reasoning
capabilities in LLMs, thereby providing a significant addition
to the body of knowledge in the field. By giving thorough
information, such as descriptions of datasets and hardware
implementations required, our paper stands out as a primary
resource for LLMs practitioners and researchers. Further-
more, we briefly discuss open issues in LLMs research,
such as ethical and responsible AI, multimodal integration,
energy efficiency, privacy and data protection, generalization
and few-shot learning, and cross-lingual and low-resource
settings. We also highlight key challenges, including data
complexity and scaling, tokenization sensitivity, computa-
tional resource demands, fine-tuning complexity, real-time
responsiveness, contextual constraints, bias and undesirable
output, knowledge temporality, and evaluation complexity.
Our review suggests future research directions to tackle
open issues and important resource for LLMs researchers
and practitioners. Our extensive systematic review presents
a detailed discussion on LLMs which makes a substantial
contribution to the field of LLMs research.


### III. History Of Large Language Models
LLMs refer to a category of AI models developed specifically
to comprehend and produce human language [19]. LLMs
have significantly contributed to the field of AI and
have been applied in diverse areas, including education,
communication, content generation, article composition,
healthcare, research, entertainment, and information dissem-
ination, among others [19], [20]. The origins of LLMs can
be attributed to the emergence and advancement of neural
network-based methodologies in the field of NLP [20].
In order to process language, early NLP systems utilized
rule-based techniques and statistical models. However, those
methods frequently encountered difficulties in comprehend-
ing the textual context in a specific discourse [21]. This
section provides a high-level overview of LLMs, including
their background, development,
training, and operation.
Figure 3 depicts the history of language models.

In the 1940s, Warren McCulloch and Walter Pitts intro-
duced the idea of artificial neural networks (ANNs) [22].
Afterwards, the 1950s and 1960s saw the development of
the first language models [23]. These models included early
neural networks as well as rule-based models. The processing
of language was facilitated by their utilization of precisely
established linguistic rules and features [24]. These models
experienced limitations in their abilities and encountered
difficulties in managing the complexities of complicated

language assignments. The models were predominantly
employed for tasks involving binary classification. However,
their efficacy in dealing with the complex situation in NLP
tasks was limited [24].

Statistics-based models of language were created in the
’80s and ’90s. These models belong to a category of
models utilized in the field of NLP and machine learning
(ML) with the purpose of capturing and quantifying the
statistical patterns and correlations within language data [21].
language models have significance in several
Statistical
applications, such as predictive text input, text generation,
speech recognition, spam detection, etc. These models were
superior in terms of accuracy to early neural networks and
rule-based models, as they were able to process large amounts
of data with ease [21]. Although statistical language models
have been successful in many applications of NLP, they
still have limitation when these models come to predict the
semantic relationship between concepts and context of the
language. These techniques have difficulty dealing with long-
range dependencies [25].

During the mid-2000s, the field of NLP witnessed the
introduction of word embeddings, which were recognized as
a notable breakthrough and subsequently acquired consider-
able attention [26]. Word embedding refers to the process
of representing words in a continuous vector space. The
approach captures the semantic relationships among words
by representing them in a vector space. The representation
reduces the computational cost by mapping the words to a
lower-dimensional space. Word2Vec and GloVe are widely
recognized word embedding models in the domain [27].
These models are mostly utilized for assessing word sim-
ilarity and assisting in the clustering and representation of
words within semantic domains. Although not classified as
LLMs, these embeddings have significantly contributed to
the progress of natural language comprehension and have set
the path for the development of more complex models. Nev-
ertheless, these models have several limitations, such as their
difficulty in effectively dealing with words that have multiple
meanings (i.e., homonyms) or words that sound the same
(i.e., homophones), as well as their inability to comprehend
contextual information in an accepted manner [26].

The introduction of neural language models in the mid-
2010s marked a significant advancement in LLMs [28].
These models employed deep learning approaches to acquire
knowledge of language patterns from extensive textual
data and additionally utilized artificial neural networks to
comprehend, produce, or forecast human language. Fur-
thermore, they have demonstrated exceptional outcomes in
a wide range of language-related tasks. The initial neural
language model to be introduced was the recurrent neural
network language model (RNNLM) in 2010 [29]. The
purpose of its development was to capture the sequential
dependencies present in textual data. The utilization of a
hidden state allows for the retention and propagation of
information from preceding words in a particular sequence.
RNNLM has been employed in several applications such

VOLUME 12, 2024

26843


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 3. Brief history of language models.

as text production, speech recognition, machine translation,
and language modeling. The RNNLM demonstrated the
capability to effectively capture the contextual information of
words, resulting in the generation of text that exhibits a higher
degree of naturalness compared to earlier models. Although
the RNNLM offers certain advantages, it is not without its
drawbacks. Some of these limitations include a limited short-
term memory capacity, extended training time requirements,
and prone to suffer in overfitting [30].

In the year 2015, Google unveiled the initial large neural
language model that employed deep learning methodologies.
The technology was referred to as the Google Neural Machine
Translation (GNMT) model [31]. The model underwent
training using huge quantities of multilingual textual data.
This development signifies a notable progression in the field
of machine translation [32]. The model demonstrated excep-
tional performance on machine translation tasks, departing
from traditional rule-based and statistical techniques in favor
of neural network-based methodologies. When compared
to earlier language models, it was able to tackle complex
natural language tasks with ease. The utilization of this
model resulted in enhanced translation accuracy and the
generation of meaningful translations, while also mitigating
errors associated with intricate linguistic constructions [31].
The advancement of Language models persisted with the
emergence of the Transformer model in the year 2017 [33].
The transformer model has had a significant impact on
the field of NLP and has played a crucial role in the
development of language models such as Bidirectional
Encoder Representations from Transformers (BERT) and
Generative Pre-trained Transformers (GPT) [34]. These

models employ a self-attention mechanism that enables them
to assess the relative significance of individual words in a
sentence, thereby encoding complex relationships within the
text [34]. The primary objective behind the development
of the Transformer model was to overcome the inherent
constraints observed in earlier models such as RNNs and
Long Short-Term Memory (LSTM) networks. The Trans-
former models possess notable advantages in comparison
to other models due to their ability to capture longer-term
dependencies in language and facilitate concurrent training
on many Graphical Processing Units (GPUs) with a vast
number of parameters, enabling the construction of much
larger models [35]. Parallelization capabilities and scalability
are further benefits that have resulted in notable progress
across many NLP activities [33].

The introduction of BERT in 2018 by Google AI represents
a noteworthy advancement in the domain of NLP [16].
The underlying framework utilized in this study was the
transformer architecture. Before the introduction of BERT,
the preceding language model rooted in NLP had constraints
in understanding contextual information due to its reliance on
unidirectional language modeling. BERT was introduced by
Google as a solution to address this particular constraint [36].
The employed methodology involved the utilization of deep
bidirectional representations, which were conditioned on
both the left and right contexts across all layers [37]. The
pre-trained BERT model was able to undergo fine-tuning by
incorporating an additional output layer, hence enabling its
applicability to diverse tasks such as question answering and
language inference. Due to the widespread adoption of BERT,
several versions and subsequent models, such as RoBERTa,

26844

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

T5, and DistilBERT, have been developed to effectively
address diverse tasks across multiple domains [37].

Following the advent of transformers, subsequent years
saw the development of scaling-up LLMs models through the
expansion of training data and parameter counts [20]. OpenAI
significantly contributed to the development of LLMs in
2018. During the same year, GPT, an additional transformer-
based architecture, was developed. Multiple iterations of
the GPT models, developed by OpenAI, underwent pre-
training using extensive datasets comprising excerpts from
the Internet, novels, and various other textual sources [38].
The first version of the GPT model was referred to as GPT-
1 [39]. The introduction of GPT-1 was a notable progression
in the field of NLP. GPT-1 effectively produces words that
are contextually appropriate, showcasing the transformative
capabilities of transformers in significantly advancing natural
language processing tasks. This proficiency is attributed
to its extensive training on a vast number of parameters,
specifically 117 million. The model underwent a two-step
procedure consisting of unsupervised pre-training followed
by supervised fine-tuning [20]. The initial iteration of GPT
did not attain the same level of popularity as BERT due to
several inherent limitations [40]. These drawbacks include a
restricted context window, absence of bi-directionality, and
occasional generation of biased content. Despite the inherent
limits of GPT-1, this model played a crucial role in paving
the way for later, more advanced models. As a result, it has
sparked a new era of AI research and intensified competition
in the development of LLMs.

The subsequent version of the GPT series, known as
GPT-2, was designed with the purpose of addressing the
limitations observed in its predecessor, GPT-1 [40]. Similar
to GPT-1, GPT-2 was developed utilizing the transformer
architecture. In the year 2019, Alec Radford introduced
GPT-2, a language model that was developed on a deep
neural network consisting of 1.5 billion parameters [41].
The GPT-2 model includes a transformer design, which
incorporates self-attention processes to extract information
from different positions within the input sequence. Despite
the high computing cost associated with training and
executing the model, its substantial magnitude facilitates the
comprehension and generation of a wide range of linguistic
subtleties and diversified outputs [40]. The GPT-2 model has
played a pivotal function in the advancement of LLMs and
the execution of NLP activities. The influence of GPT-2 has
had a significant impact on successor models like GPT-3 and
GPT-4, leading to additional advancements in the field of
language processing and creation [42].

In 2019, NVIDIA produced Megatron-LM, which is an
LLMs [43]. Similar to GPT, this model is built on the
transformer architecture. The model possesses a total of
8.3 billion parameters, a notably bigger quantity compared to
the parameter count of GPT-1 and GPT-2 [16]. The magnitude
of this dimension facilitates the model’s capacity to acquire
and produce intricate linguistic structures. Nevertheless,

Megatron-LM has certain limitations, primarily due to
its substantial dimensions, which necessitate substantial
computational resources for both the training and inference
processes [43].

In the year 2020, OpenAI introduced GPT-3 as the
successor to GPT-2 [40]. GPT-3 was trained on an extensive
collection of textual data and demonstrated the ability to
generate text that exhibited a high degree of coherence
and naturalness. Similar to GPT-1 and GPT-2, this model
also utilizes the Transformer architecture [20]. The potential
of LLMs for various NLP applications was exemplified
by GPT-3. This particular LLMs was trained on a deep
neural network with an enormous 175 billion parameters,
surpassing the size of any other LLMs available at that
particular time [16]. The ability to produce natural language
text of superior quality with less fine-tuning is facilitated
by sophisticated methodologies, including a more significant
number of layers and a wider range of training data. One of
the most essential characteristics of GPT-3 is its capacity to
engage in few-shot and zero-shot learning, hence mitigating
the necessity for extensive data in order to generate natural
language text of superior quality. The advent of GPT-3 has
catapulted the domain of natural language processing to new
heights [40]

In the year 2020, OpenAI introduced GPT-4, the sub-
sequent version of their language model, following the
achievements of GPT-3 [20]. Similar to its predecessor,
GPT-4 is a transformer-based model. The system has the
capability to analyze both textual and visual data to produce
textual outputs [16]. The performance of the system was
assessed using a range of standardized professional and
academic examinations specifically intended for human test-
takers. GPT-4 exhibited a level of performance comparable to
that of humans on the majority of examinations. Significantly,
it achieved a ranking inside the highest decile of participants
on a simulated iteration of the Uniform Bar Examination [44].
GPT-4 has greater dimension and efficacy compared to
its predecessor, GPT-3, as it possesses the capacity to
generate text that is even more comprehensive and exhibits
a heightened level of naturalness [20].

The development of large language models presents addi-
tional prospects for innovation, knowledge acquisition, and
experimentation across diverse domains such as healthcare,
education, research, etc. The utilization of AI and NLP in
these models has significantly transformed how we engage
people with machines.


### IV. Methodology
Preferred Reporting Items for Systematic Reviews and
Meta-Analyses (PRISMA) guide is crucial for drafting
review papers as it assists systematic reviews in conducting
transparent meta-analyses, accurately reporting aims and
concluding the study, and ensuring the adequate reliability
and relevance with the findings of the study [45]. Therefore,
this review work focuses on the adoption of PRISMA

VOLUME 12, 2024

26845


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 2. Electronic database search.

TABLE 3. Search queries used for the review paper.

FIGURE 4. PRISMA flow diagram of the review.

technique in analyzing the design, configurations, applica-
tions, and challenges of LLMs.


#### A. INITIAL SEARCHING
The research materials employed in this study have been
acquired from recognized scientific journals and conferences
from January 2020 to August 2023, conducted through the
Google Scholar platform. A comprehensive selection of
scholarly research articles has been specified, encompassing
various reputable academic sources such as IEEE Xplore,
ScienceDirect, ACM Digital Library, Wiley Online Library,
Springer Link, MDPI, and patents. Initially, 355 papers were
selected based on their relevance to the topic and keyword.
Table 2 describes the identification technique of the materials
from various electronic sources.


#### B. SEARCHING QUERY AND KEYWORDS
Using the combination of the appropriate search queries
and keywords enlisted in Table 3 helps to perform a proper
literature search. To conduct a thorough search of the
articles for our LLMs-based review work, we encompass the
following terms: ‘‘LLMs AND machine learning OR deep
learning OR models,’’ ‘‘LLMs AND machine learning OR
deep learning OR API,’’ ‘‘LLMs AND machine learning OR
deep learning OR Dataset’’, ‘‘LLMs AND natural language
processing OR NLP’’ and ‘‘LLMs AND machine learning
OR deep learning OR tools.’’ These specific searching
techniques help to extract the eligible and quality research
papers.


#### C. INCLUSION AND EXCLUSION CRITERIA SET
To acquire the final research papers, PRISMA protocols
and principles were adhered to formulate a standard set of

Inclusion Criteria (IC) and Exclusion Criteria (EC). The
inclusion criteria define the standards of the paper that need
to be included, while the exclusion criteria eliminate articles
that do not meet the inclusion scope. Thus, this manual
screening process improves the transparency of selection
process. Table 4 presents the inclusion and exclusion criteria
set for the proposed study.


#### D. PRISMA DIAGRAM
Figure 4 depicts the PRISMA flow diagram utilized in
selecting papers for the study. It also provides the numbers
of included and excluded papers for better understanding.
The diagram begins by identifying articles from electronic
databases using keywords, queries, resulting in 355 papers.
After applying the screening method to exclude duplicated,
low-quality, and irrelevant journal papers, the total number
of papers for review is reduced to 294. Following a thorough
analysis of the titles and abstracts, a total of 207 papers were
selected. The final screening method involves the application
of inclusion and exclusion criteria. Following this process,
a total of 135 papers were ultimately selected for the final
review. The process begins with an extensive collection of
papers and reduces to the final selection that meets the pre-
defined selection criteria for the systematic review.


### V. Large Language Models
Large language models (LLMs) refer to a specific type of
AI algorithm that holds the capability to execute a diverse
range of NLP tasks. The most common tasks entail text
translation, sentiment analysis,
generation,

text analysis,

26846

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 4. Inclusion and exclusion criteria.

question answering, and other related functions. GPT-3,
GPT-4, PaLM, and LaMDA are extensively used transformer-
based LLMs models trained on a large amount of textual
data. In terms of architectural properties, these models show
variations in size and depth. For example, GPT-3 generates
parameters of 175 billion, distributed across 96 levels, while
PaLM has an even larger parameter number of 540 billion,
organized across 106 layers. All of these models have distinct
configurations. The configurations of GPT-3 and PaLM
differ in terms of their techniques for generating output.
LLMs have evaluated several datasets within Wikipedia, code
repositories, books, question sets, and social media data. They
have demonstrated their ability to execute diverse activities
successfully. Consequently, LLMs have drawn significant
attention for their effective contribution in different domains,
including education, healthcare, media marketing, and other
customer services. A particular LLMs program has superior
performance in a specific domain compared to others, such
as GPT-3, which has gained recognition for its proficiency in
generating text styles, whereas LaMDA demonstrates supe-
rior performance in providing accurate responses to factual
inquiries. LLMs are an emerging technological innovation
that holds the potential to bring about transformative changes
across various sectors.


#### A. BACKGROUND OF LARGE LANGUAGE MODELS
In this section, we present the essential aspects associated.
LLM research requires a comprehensive explanation of the
crucial concept. Various vital aspects, such as tokenization,
encoding technique, layer normalization, etc., are encom-
passed in the following background section.

1) TOKENIZATION
The primary emphasis is on tokenization, a crucial prepro-
cessing stage of LLMs that involves parsing text into discrete
parts referred to as tokens [46]. Characters, subwords,
symbols, or words may serve as tokens, contingent upon
the language model’s dimensions and nature [47], [48].
Various tokenization algorithms are utilized in LLMs, such

as WordPiece, UnigramLM, and Byte Pair Encoding (BPE).
This algorithm has distinct technique for tokenizing from the
input and then, applied for the specific tasks [47], [48], [49].

2) ATTENTION MECHANISM
The attention mechanisms used in LLMs is a crucial topic
hence it contributes in the improvement of the architecture
and performance. This mechanism helps to figure out the
representation of input sequences by forming links between
various tokens. There are several attention mechanism
available namely Self-Attention where all the queries and
values come from the same encoder-decoder block. Then,
Full Attention which is the naive understanding version of
self attention, and finally, when the output of encoder block
is used as the query of immediate decoder block, is called as
cross attention mechanism [9], [50].

3) ACTIVATION FUNCTION
The activation functions play a vital role in the curve-fitting
capacities of LLMs architectures [51]. Several activation
functions, such as ReLU, GeLU, and other GLU variations,
are explored to determine their performance in current
research on LLMs [52], [53].

4) NORMALIZATION LAYER
Layer normalization is essential for achieving faster conver-
gence in LLMs model and emphasizes their effects on stabil-
ity during training sessions. It presents different approaches,
such as LayerNorm, DeepNorm, and RMSNorm. These
layer normalization techniques offer distinct advantages and
contribute to the regularization of LLMs applications like
GPT-3, BERT, T5, etc., facilitating effective training [54].

5) TRAINING METHODS AND FRAMEWORKS
LLMs training has different distributed methodologies,
including data parallelism, pipeline parallelism, tensor par-
allelism, model parallelism, and optimizer parallelism [43],
[55]. These techniques contribute to understand the practical
and expandable training. Additionally, different libraries and
frameworks, including Transformers, DeepSpeed, PyTorch,
TensorFlow, MXNet, and MindSpore, are used frequently for
their training and further implementation [55].

6) DATA PREPROCESSING
The approaches used to preprocess data focus on the
significance of quality filtering, data de-duplication and
privacy reduction in preparing training data for LLMs.
The filtering technique helps to reduce low quality and
relevant data. Besides, it reduces the compute complexity
by ignoring the useless pattern of the input. Duplicate
samples are removed using de-duplication technique which
also avoids the overfitting tendency of the model. Finally,
privacy reduction ensures the security and compliance
of data and upholds the preservation of
the personal
data.

VOLUME 12, 2024

26847


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 5. Background of LLMs.

7) PARAMETER TUNING
The researchers explore the many stages of adaptation for
LLMs, starting from pre-training and progressing to fine-
tuning for subsequent tasks. These approaches serve as a
guide for customizing models to suit specific applications.
tuning
Several model adaptation and parameter-efficient
techniques, such as prefix tuning, prompt tuning, and adapter
tuning, provide strategies for achieving effective fine-tuning
while minimizing resource usage [56], [57], [58].

This background part aims to provide a thorough under-
standing of the underlying concepts and approaches that
form the basis of Language Models, which are constantly
developing.

The transformer is employed in most advanced LLMs as
the basic building block because its architecture, scalability,
and pretraining approach enable the model as optimal
framework for constructing robust LLMs. In addition, the
self-attention mechanism of transformers performs effec-
tively for capturing and representing long-range relationships
in language. Consequently, Transformer-based LLMs have
significantly improved the state-of-the-art achievement in
NLP related tasks. In the section V-A1, a comprehensive
overview of transformer architectures, configurations are
provided for building a high-scalable, optimized and cost-
efficient LLMs. Figure 5 depicts the visualization of the
LLMs background.

8) WHAT IS TRANSFORMER?
Transformer architecture is considered as the basic building
is intended for neural networks to
block of LLMs. It
efficiently handle sequential data [9]. This architecture does
not use iteration methods. Instead, it employs a focused (i.e.,
attention based) approach to determine global input-output
dependencies. The model can take input of varying lengths
and can change its focus depending on the length of the

sequence. As a result, it has become the go-to architecture
in many fields, often replacing sophisticated recurrent or
convolutional neural networks with much more efficient
structure [59]. In this regard, it is particularly important for
LLMs applications. Figure 6 illustrates the architecture of
the transformer model. Transformer architecture consists of
seven main components. A demonstration of each component
is shown below.

- Inputs and Input Embeddings

The ML models utilize tokens, which are units of
text like words or sub words, as the training data.
However, these models process numbers. Tokenization
begins this translation process by dividing down input
text into meaningful components. A unique number
identification is assigned to each token, connecting
the linguistic information to the numerical vector. This
numerical format is known as ‘‘input embeddings.’’
These input embeddings are numerical representations
of words, which ML models may subsequently process.
These embeddings function similarly to a dictionary,
assisting the model in understanding the meaning of
words by arranging them in a mathematical space where
comparable phrases are situated close together. The
model is trained to generate these embeddings so that
vectors of the same size represent words with similar
meanings. Figure 6A illustrates the input and input
embeddings.

- Positional Encoding

The sequence of words in a sentence frequently
conveys important semantic information. The same
set of words in a different order conveys completely
different meanings. In this regard, understanding the
word order in a sentence is essential in NLP to identify
the correct utterance meaning. In general, in terms of
neural networks, they do not perceive the order of inputs.

26848

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 6. Architecture of a Transformer model.

To address the problem, positional encoding is used to
encode the position of each word in the input sequence
as a collection of integers. The transformer model uses
integer, input embedding and positional encoding to help
GPT in understanding sentence word order and provide
grammatically accurate and semantically appropriate
output [60]. The positional encoding part is shown in
Figure 6B.

- Encoder The encoder is a crucial component of the
neural network which is responsible for processing the
input text. Its primary function is to generate a series of
hidden states that represent the input text in a meaningful
way [61]. Then, it uses a series of self-attention layers
that are often referred to metaphorically as ‘‘voodoo
magic,’’ emphasizing their complex and powerful ability
to capture relationships between different elements in
the input text. In the transformer, the encoder is used
in more than one layer. This section is depicted in
Figure 6C comprehensively.

- Outputs (shifted right) During the training process,
the decoder in the transformer model learns to predict
the next word in a sequence by analyzing the preceding
words. This is achieved through a mechanism known as
autoregressive training. The decoder’s ability to predict
the next word is critical for generating coherent and
contextually relevant sequences. Additionally, the GPT
(GPT-3) is also trained on a massive amount of text
data, that helps it to generate sense while writing any
content. Besides, several corpus including the Common
Crawl web corpus, the BooksCorpus dataset, and the
English Wikipedia are also used during the common
issue. Figure 6D highlights the transformer’s outputs
(shifted right) module.

- Output Embeddings

Input embeddings, which contain text are not directly
recognized by the model. Therefore, the output must
be converted to a format known as ‘‘output embed-
ding.’’ Similar to input embeddings, output embeddings
undergo positional encoding, enabling the model to
understand the order of words in a sentence [62].
In machine learning, the loss function evaluates the
difference between a model’s prediction and the objec-
tive value. Loss functions are essential for complex
GPT language models. The loss function modifies a
portion of the model to increase accuracy by reducing
the discrepancy between predictions and targets. The
change improves the overall performance of the model.
The loss function is calculated during training, and
the model parameters are modified. In the inference
process, the output text is created by mapping the
predicted probability of each token in the model to
the corresponding token in the vocabulary. The output
embedding part is illustrated in Figure 6E.

- Decoder

The decoder processes both positionally encoded input
and output embeddings. Positional encoding is crucial
for the model to understand the sequential order of
the tokens in both the input and output sequences.
The positional information helps the decoder effec-
tively capture the structure within the sequences. The
decoder has an attention mechanism that helps to
improve the output’s quality by leveraging contextual
information received from the encoder. The primary
function of the decoder is to create output sequences
based on the encoded input sequences. It generates
a sequence of tokens, often representing words or

VOLUME 12, 2024

26849

TABLE 5. Hardware specifications for the LLMs model.


#### M. A. K. Raiaan et al.: Review on Large Language Models

sub-words, as its output. The dependency between the
encoder-decoder in a transformer is significant where
the encoder processes the input sequence based on
the representation, the decoder provides the desired
output sequence. In addition, GPT is a decoder-only
transformer [63]. The decoder part of GPT uses a
masked self-attention mechanism which can process
the input sequence without requiring encoder explicitly.
Figure 6F demonstrates the decoder component of a
transformer.

- Linear Layer and Softmax

The linear layer is a fully connected neural network
layer that transforms the output embedding into a higher-
dimensional space. This step is required to convert
the output embedding into the original input space.
This transformation enhances the expressiveness of the
to capture more
representation, allowing the model
complex patterns and relationships in the data. Besides,
the softmax function generates a probability distribution
for each output token in the developed vocabulary,
allowing us to generate probabilistic output tokens [64].
Figure 6G shows the process by which the features
are propagated through a linear layer, followed by the
activation of the accurate output probability using the
softmax activation function.


#### B. HARDWARE SPECIFICATIONS FOR LARGE LANGUAGE
MODELS
Understanding the computing resources and training dura-
tions needed for various language models is crucial. This
estimation helps us in decision-making when choosing a
model for specific tasks. To choose a model that is appropriate
for a given task, a clear understanding of the training times
and computational resources is mandatory. Table 5 shows

the hardware specifications, number of parameters, training
duration and other configurations of
individual LLMs
model.

GPT-3: GPT-3 uses Nvidia A100 GPUs to pre-train on
a large 300 billion token set, generating around 175 billion
parameters [65]. GPT-3 has context learning features which
enables itself to understand the words reasoning, sentence,
and language properly.

BERT: Trained on an unspecified data scale, the BERT
model has a variable number of parameters that depends
on batch size and the corresponding model’s hidden layer
numbers which is around 340 million. Nvidia A100 and
V100 GPUs are used for training, and the length of the
training depends on the scale of the model’s parameters [66].
Contextual learning is incorporated in the model also.

RoBERTa: RoBERTa, an enhanced version of BERT
which has a parameter count of 340 million and conducts pre-
training on a specific amount of data. The training process
completed on 6144 TPU v4 units, running for around a
duration of two weeks [67]. The model also contains a context
learning feature.

T5: T5 uses 1024 TPU v3 units and has a number of
11 billion parameters. T5 has been pre-trained over a number
of tokens of 1 trillion [68]. There is no information available
on GPU training time. It also holds the features of contextual
learning which provides a satisfactory result.

PaLM: PaLM produces a substantial number of parame-
ters, around 540 billion, and it manages the pre-training on
a large dataset with a tokens of 780 billion. The pre-training
process is carried out utilizing by 6144 TPU v4 units [69].
The training period extends for 120 days, and the model also
incorporates contextual learning.

LaMDA: LaMDA uses 1024 TPU v3 units during the
training and the model is pre-trained over 768 billion tokens

26850

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

which generates a total of 137 billion parameters [70].
It requires a total of of 57.7 days during training.

GLM-130B: GLM-130B model possesses a total of
130 billion parameters and undergoes pre-training on a huge
amount of dataset with 400 billion tokens. The training was
conducted utilizing 1024 TPU v4 units and the training
session lasts for 60 days [71].

the experiment.

Gopher: Gopher is a language model that has been pre-
trained over 300 billion tokens and required 4096 TPU
It has a total of 280 billion
v3 for
parameters [72]. The GPU training period is precisely stated
as 920 hours. Furthermore, the model integrates context
learning to demonstrate an effective outcome.

Jurassic-1: Jurassic is a model with an impressive capacity
of 178 billion parameters. It has been pre-trained on a massive
dataset of 300 billion tokens, utilizing the computational
power of 800 GPUs [73]. No information regarding the
duration of GPU training is available.

MT-NLG: MT-NLG has a huge size of 530 billion
parameters. It has been trained on a massive dataset of
270 billion tokens, utilizing 4480 80GB A100 GPUs [74].
No data regarding the duration of GPU training is available.
The model integrates context learning features also.

LLaMA: LLaMA is a language model with an enormous
capacity with a total of 65 billion parameters. It has
undergone pre-training on a large dataset consisting of
1.4 trillion tokens. This training process was carried out
utilizing 2048 high-performance 80GB A100 GPUs [75]. The
training period is explicitly set to 21 days.

LLaMA 2: LLaMA 2 is equipped with a total of 70 billion
parameters and has performed pre-training on 2 trillion
tokens, utilizing 2000 80GB A100 GPUs [76]. The training
period is set to 25 days, and the model also contains context-
based learning.

Falcon: Falcon, equipped with 40 billion parameters,
undergoes pre-training on a large dataset of 1.3 trillion
tokens [77]. No details regarding the duration of GPU training
and it also have the context learning features.

Chinchilla: Chinchilla is a language model

that has
70 billion parameters and has been pre-trained on 1.4 trillion
tokens [78]. There is no details regarding the duration of GPU
training.

OPT: OPT, equipped with 175 billion parameters, con-
ducts pre-training on 180 billion tokens utilizing 992 A100
GPUs with a capacity of 80GB each [79]. No details
regarding the duration of GPU training.

Galactica: Galactica possesses 120 billion parameters and
has undergone pre-training using 106 billion tokens [80].
Details regarding the duration of GPU training are not given.
BLOOM: BLOOM has a remarkable capacity of 176 bil-
lion parameters and has undergone pre-training on 366 billion
tokens utilizing 384 80GB A100 GPUs [55]. The training
period lasts for 105 days, and the model
incorporates
contextual learning.

PanGU-a: PanGU-a is a language model that has been pre-
trained on a massive amount of data, specifically 1.1 billion,

employing 2048 Ascend 910 processing units [81]. It has
an impressive parameter count of 207 billion. No details
regarding the duration of GPU training.

Our comprehensive description helps to understand the
hardware specifications and the computational complexity of
each model. The researchers also find an opportunity to know
about the implementation details of these models and can
improve the performance of their studies.


#### C. DEEP NEURAL NETWORK ARCHITECTURES OF LLMS
LLMs usually employe deep neural networks to understand
and generate new content more accurately. In this section,
we include a summary of various DNN architectures used in
different LLMs based on literature studies and different real
world applications.

1) COMPARISON BETWEEN STATE-OF-THE-ART STUDIES
An LLM is a dynamic model capable of performing various
tasks, such as creating coherent text and summarizing text.
A defining feature of a language model is its ability to
assume the subsequent words from the preceding text. The
deep neural network (DNN) framework is utilized in LLMs
to enhance its performance which is similar to human-like
understanding [3], [82]. LLMs use different DNN models in
their architecture to enhance task performance.

The transformer architecture serves as the basic building
block of all language models. GPT-1, the initial version of
GPT employs the Transformer decoder architecture [66].
In GPT-1 the decoder structure operates independently from
the encoder, therefore eliminating the multi-head attention
and layer norm components that are linked to the encoder.
The pre-trained GPT model consists of 12 transformer blocks,
each with a d(model) value of 768 and a total of 110 million
parameters. GPT-2, the second version of GPT, employs
the transformer decoder architecture like GPT-1 [66]. GPT-
2 employs 50,257 BPE tokens and ensures that the masked
multi-head component
is preceded by the Layer Norm.
In GPT-2, an additional layer norm is included subsequent
to the last block. There are four pre-trained GPT-2 models
available, each with a unique quantity of decoder blocks.
The largest model, which has a d(model) value of 1600 and
48 blocks, comprises a total of 1.5 billion model parameters.
BERT employs the transformer encoder structure, in contrast
to the Transformer decoder structure utilized by GPT-1 and
GPT-2 [83]. Following the final encoder block is composed of
two fully connected output layers separated by a Layer Norm
component. The calculation of the likelihood of each token’s
output depends on both the previous and next tokens, making
BERT a bidirectional language model. The smaller variant of
BERT consists of 12 encoder blocks with a model dimension
of 768 and a parameter count that is approximately equal to
that of GPT. In contrast, the larger variant has 24 encoder
blocks with a model dimension of 1024 and 336 million
parameters [66].

In contrast to encoder-only models such as BERT and
decoder-only models like GPT-1 and GPT-2, T5 pre-train

VOLUME 12, 2024

26851

with generative span corruption and an encoder-decoder
architecture [84]. T5 models have displayed state-of-the-art
performance on a wide variety of NLP tasks, like GLUE
and SuperGLUE, and are able to expand up to hundreds of
billions of parameters. LLaMA normalizes the input for every
transformer sub-layer rather than the output [75]. To increase
performance, it employs the RMSNorm normalizing function
and the SwiGLU activation function rather than the ReLU.
Single models are utilized by LaMDA to execute multiple
duties. The model architecture is a decoder-only transformer
language model. The Transformer is comprised of 64 layers,
a d(model) value of 8192, gated-GELU as the activation
function, and relative attention the same as T5 LLMs [70].
AlphaCode employs an encoder-decoder transformer archi-
tecture in which input tokens are passed to the encoder, and
one token is extracted from the decoder until an end-of-code
token is generated [85]. When contrasting encoder-decoder
architectures with decoder-only architectures, the encoder-
decoder architecture provides the advantage of enabling
bidirectional description representation and provides addi-
tional flexibility by separating the encoder structure from
the decoder. It employs an asymmetric architecture with
1536 encoder tokens but only 768 decoder tokens. It makes
use of multi-query attention to lower sampling costs. Cache
update costs and memory utilization are greatly reduced when
all query heads are used but only shared for key and value
heads in each attention block. It employed a SentencePiece
tokenizer for tokenization,
trained on a combination of
CodeContests and GitHub data, with a vocabulary size of
8,000 tokens. Through the usage of DNNs, all of these LLMs
have demonstrated remarkable performance on various NLP
tasks like as language understanding and generation.

2) APPLICATIONS OF LLMS USING VARIOUS DNN MODELS
Pre-training Transformer models have led to the proposal
of LLMs with impressive capacities in addressing a variety
of NLP tasks,
including question-answering, document
summarization, and language translation [3]. Due to their
remarkable abilities in basic tasks of language processing
and creation, they have completely transformed the fields
of NLP and AI. Various DNN models have been employed
in different industries, such as technology, healthcare, and
retail to increase performance. DNNs have made substantial
progress in improving the capabilities of LLMs [87]. DNN
models, such as convolutional neural networks (CNNs),
recurrent neural networks (RNNs), generative adversarial
networks (GANs), capsule networks (CapsNets), transform-
ers, and BERT, have been extensively employed in diverse
applications of LLMs [94]. Numerous studies [86], [87],
[88], [89], [90], [91], [92], [93] suggest that DNN models
are utilized in several types of LLMs-based applications to
increase task efficiency.

Koizumi et al., [86] introduce an innovative method to
address the issue of insufficient
training data in audio
captioning that utilizes a pre-trained LLMs that uses a


#### M. A. K. Raiaan et al.: Review on Large Language Models

decoder for generating captions. The findings of the study
demonstrate the effectiveness of the proposed methodology in
utilizing LLMs for audio captioning. The performance of this
proposed approach outperforms the traditional approaches
which are trained from the scratch.

In a recent study, Fan et al., [87] discuss the significance
of
recommender systems in web applications and the
shortcomings of current DNN approaches in predicting user
preferences. They discuss the capacity of LLMs to tackle the
challenges in a recommender systems.

Bai et al. [88] developed an end-to-end non-autoregressive
speech recognition model namely LASO (Listen Attentively
and Spell Once) to improve the speed of inference by simul-
taneously predicting all tokens. The proposed model utilizes
attention methods to combine decoded speech information
into hidden representations for every token. Moreover, they
suggest using cross-modal transfer learning to increase the
performance of the speech-modal LASO model by utilizing
a text-modal language model to align the semantic meaning
of tokens.

Sun et al., [89] provide a new methodology to predict the
effect of news releases and to minimize potential negative
consequences by automatically forecasting responses in news
media. By utilizing an LLM which utilizes a deep neural
network, their method creates a belief-centered graph on
an existing social network to analyze social dynamics.
The proposed framework shows a satisfactory efficiency in
predicting responses.

Drossos et al., [90] present a technique that enables
an RNN to acquire LLMs for sound event detection. The
proposed approach adjusts the input of the RNN based on the
activity of classes in the preceding time step. This proposed
approach is evaluated on three distinct datasets: the TUT-SED
Synthetic 2016, TUT Sound Events 2016, and TUT Sound
Events 2017 datasets.

Chiu et al. [91] present an efficient method called TPBERT
(based on BERT) for improving the reranking of N-best
hypotheses in automatic recognition of speech. This approach
uses task-specific topic information to increase the BERT
model’s ability to create accurate embeddings of the N-best
hypotheses.

Elhafsi et al., [92] propose a monitoring methodology that
utilizes LLMs to tackle the issue of semantic irregularities in
robotic systems. The efficiency of LLMs-based monitoring
in recognizing semantic abnormalities and aligning with
human thinking is demonstrated through tests on autonomous
driving.

Shen et al.,

[93] present a self-regulating edge AI
system that utilizes a deep neural network that can plan
automatically, and adjust itself to fulfill the needs of users.
The proposed system uses a hierarchical design known as
cloud-edge-client, where the primary language model
is
located in the cloud. By leveraging the robust capabilities
of GPT in language comprehension, and code creation, they
introduce a methodology that effectively handles edge AI
models to meet users’ requirements while automatically

26852

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 6. Comparison of applications of LLMs using various DNN models.

generating new codes for training new models through edge
federated learning.

Table 6 gives a brief overview of these DNN applications-
oriented studies where they applied LLMs. These studies
suggest that employing deep neural networks in language
models increases the performance of LLMs-based applica-
tions in several industries..


#### D. ARCHITECTURAL OVERVIEW OF LARGE LANGUAGE
MODELS
In this subsection, we present a detailed overview on the
architecture of LLMs. Table 7 presents a description and
architecture of LLMs such as GPT-1, BERT, RoBERta, and
T5. The table assists researchers in selecting the optimal
model for a NLP task. GPT-1, BERT base, and BERT
large contain 12, 12, and 24 layers, respectively, in LLMs.
RoBERta is an enhanced variant of BERT, while T5 is
a decoder and encoder transformer. Diagram illustrating
BERT’s input token processing, context-aware embedding,
and masked language modeling tasks, where the masked
words are intended to predict the model. T5 demonstrates
the sequential layers of the transformer model, including the
feedforward neural network, and self-attention. T5 explains
how information flows and structures text. GPT-1 passes data
input embedding and positional encoding through multiple
transformer layers.


#### E. COMPARISON BETWEEN CONFIGURATIONS OF LLMS
Table 8 provides an extensive overview of various LLMs,
highlighting their configuration details and optimization
settings. These LLMs have played a crucial role in advancing
natural language understanding and generation tasks, making
them a key research topic in NLP. This analysis compares
and contrasts these LLMs based on critical parameters,
including model size,
learning rate, category, activation
function, batch size, bias, number of layers, optimizer,
number of attention heads, hidden state size, dropout rate,

and maximum training context length. GPT-4 considered as
one of high performing LLMs with a staggering 1.8 trillion
parameters. It is comparatively faster than the prior GPT
versions and provide many advanced features. Besides, it has
fast response system, generate more accurate output and it
has reduced the biases presented in the model substantially.
GPT-1, despite being lesser with 125 million parameters,
demonstrates the significant development of LLMs over
the years. An increased number of parameters in LLMs
enhances the model’s ability to comprehend intricate patterns
and produce text that is more contextually appropriate and
reminiscent of human language. GPT3’s selection of a
modest learning rate of 6 is notable, which highlights the
significance of cautious hyperparameter selection. Models
are categorized as Causal decoder (CD), Autoregressive
(AR), Encoder-decoder (ED), and Prefix decoder (PD) to
illustrate architectural diversity. Activation functions vary,
influencing the models’ expressive strength from GeLU in
GPT-3 to SwiGLU in LLaMA and LLaMA-2. All versions
of GPT employ the GeLU as its activation function as it
mitigates the vanishing gradient problem and facilitates the
generation of smoother gradients throughout the training
process. The utilization of SwiGLU as the activation function
is observed in models such as PaLM and LLaMA versions
1 and 2, as it has gating mechanisms that enhance its ability
to capture intricate correlations within the data. Models like
BERT, OPT, and T5 use ReLU as the activation function. The
Formula of these activation functions are given below [6],
[59]:

ReLU (x) = max(0, x) = f (x) =

GeLU (x) = 0.5x(tanh[

SwiGLU (x) = x.Sigmoid(βx).xV

(

x,
if x ≥ 0
if x < 0
0,
2/π(x + 0.44715x3)])

p

(1)

(2)
(3)

BARD is recognized for its informative response. It fea-
tures 24 attention heads and facilitates its contextually related

VOLUME 12, 2024

26853

TABLE 7. Architectural overview of different LLMs.


#### M. A. K. Raiaan et al.: Review on Large Language Models

response. BERT size is identical to BARD of 340M. The
key advantage of BERT is understanding the context of
words. It has effective training settings with a proper learning

rate, batch size, and a dropout value of 0.1, leverages the
convergence of the model, and contributes to the NLP-
based tasks precisely. PanGU BLOOM, Galactica, and

26854

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 8. Various LLMs with configuration details and optimization settings (Here, LR = learning rate, CG = Category, AF = the activation function, bs =
batch size, NL = the number of layers, NAH = the number of attention heads, SHS = the size of the hidden states, MCLDT = the maximum context length
during training, CD = causal decoder, ED = encoder-decoder, PD = prefix decoder, and AR = autoregressive).

Chinchilla are also LLMs but possess distinct configurations
and challenges. Usually, PanGU is highly effective for the
Chinese language, whereas Galactica performs well with
repeated data. Chinchilla is a scaling strategy constrained by
data limitations and creates efficient resource allocation for
training and generating output. Falcon and T5 are compact
compared to other LLMs, and both are transformer-based
models. However, they have some unique differences, such
as Falcon is a decoder-based model whereas T5 integrated
both encoder-decoders. Additionally, Falcon utilizes multi-
head query attention to increase the scalability of the model.
LLaMA-2 is the updated version of LLaMA. It is an enhanced
fine-tuned version that exploits the hardware utilization
for efficient training sessions. MT-NLG and PaLM have
substantial parameter sizes of 530B and 540B, respectively.
Both of them also use the casual decoder technique. However,
they have some architectural differences, such as PaLM
uses a SwiGLU activation function and adafactor optimizer.
Moreover, it uses a higher learning rate and batch size of
1 × 102 and 1000K. On the contrary, MT-NLG uses a lower
learning rate and batch size of 5 × 105 and 64K, respectively.
GLM-130B and LaMDA are also effective LLMs, widely
used for NLP-based tasks, including question answering, text
generation, etc. Both of them use the Gated GLU (GeGLU)
activation function, a GLU variant. The following equation is
used to express the GeGLU operation [99].

GEGLU(x, W , V , b, c) = GELU(xW + b) ⊗ (xV + c) (4)

However, there are noticeable differences between GLM-
130B and LaMDA in terms of their decoder mechanisms.
GLM-130B employs a prefix decoder, whereas LaMDA
adopts a casual decoder technique. In addition, the GLM-
130B model employs a larger batch size compared to the
LaMDA model. In addition, the presence or absence of

[]

biased terms in models, such as Falcon, T5, LLaMA 1,2,
and Galactica’s ‘‘No,’’ highlights the complexity of the
choices made. From 12 for GPT-1 to 118 for PaLM, the
number of layers affects a model’s ability to capture intricate
patterns. Optimizers are also diverse, with Adam, AdamW,
and AdaFactor playing crucial roles. All GPT variants employ
Adam as the optimizer, although models such as Galactica,
OPT, and Falcon utilize AdamW as their optimizer. Both
T5 and PaLM models utilize the Adafactor optimizer in
their respective architectures. These variations highlight the
significance of selecting models and configurations that are
tailored to particular tasks, with performance, computational
resources, and task requirements playing a central role.

The number of attention heads also exhibits variation
across different models. GPT-1 is equipped with a total
of 12 attention heads, whilst GPT-4 boasts a much larger
number of attention heads, ranging from 120 to 150 within
its model. The additional number of attention heads in the
LLMs enables the model to concurrently attend to several
segments of the input sequence, hence expediting the model’s
training process. In order to enhance the efficacy of the
LLMs, researchers employ diverse dimensions for the hidden
states within their model. The larger dimensions of the hidden
state enable the capturing of complex patterns within the
text. Both GPT 4 and MT-NLG employ hidden state sizes
of approximately 20,000, which is significantly greater in
comparison to the hidden state sizes of other LLMs included
in the table. Certain LLMs models incorporate a dropout
value of 0.1 to prevent overfitting issues, whereas others
do not employ any dropout value. The maximum context
length denotes the number of tokens that can be remembered
by the model during training. Increasing the size of the
context window boosts the model’s ability to grasp the distant
relationships between the texts. Consequently, the model is

VOLUME 12, 2024

26855

TABLE 9. Dataset for large language models.


#### M. A. K. Raiaan et al.: Review on Large Language Models

able to generate text outputs with a great coherence. Table 8
reports that GPT-4 has the context length of 32768 which is
the maximum among all the LLMs. This substantial length
number indicates the capability of GPT-4 to remember the
more extended token sequence during training. LLaMA-2
obtained the second-highest context length of 4096. Most
of the models have a context length of 2048, meaning
they can handle a maximum of 2048 tokens simultaneously
during the text generation. A few compacted models,
including BARD, BERT, and T5, possess a maximum context
length of 512. This table presents a qualitative architectural
comparison among the most popular LLMs. It also provides
comprehensive knowledge about the configurations, strength
of these models. These variations highlight the significance
of selecting models for the particular tasks considering the
performance, computational resources.


#### F. COMPARISON BETWEEN DATASETS OF LLMS
Different LLMs utilized different datasets for the training
phase, distinguishing the models from one another. A concise
overview of the datasets is provided in this section. Moreover,
it explicitly exhibits the diverse range of datasets used by
the model since understanding of these datasets facilitates
the development and training of the model and boost
the performance. The datasets used to train various large
language models (LLMs) and their compatibility with each
model are detailed in Table 9.

Table 9 demonstrates that datasets have been divided into
multiple categories: webpages, conversation data, literature,
news, scientific data, and codes. This classification enables
us to comprehend the variety of data sources that contribute
to LLMs training. C4, OpenWebText, and Wikipedia are
examples of datasets that belong to the ‘‘Webpages’’ category.
At the same time, BookCorpus, Gutenberg, CC-Stories-R,
CC-NEWES, and REALNEWS are examples of datasets
that belong to the ‘‘Books and News’’ category. These

categories reflect the richness and diversity of text data used
to train LLMs, including web content, novels, news articles,
scientific literature, and codes.

From the ✓, we observe that LLaMA has been trained
on a wide range of data sources, with significant exposure
to webpages (87%), conversation data (5%), books and
news (2%), scientific data (3%), and codes (5%). Therefore,
LLaMA becomes a versatile model suitable for a wide array
of NLP tasks that involve these mentioned data sources.
In contrast, GPT-3 and AlphaCode have limited data access
of data sources to train their models. GPT-1 and GPT-2
focus on webpages (70%) and books & news (30%) data to
train the model. GPT-3 is proficient with web pages (84%),
literature, and news (16%) but requires additional instruction
with conversation data, scientific data, and codes. Diverse
range of datasets enables the GPT models to generate more
contextual information across various domains. Specifically,
the Webpages, books, and news datasets help to employ
formal and structured language. Besides, GPT models
achieve the capability of responding in an informative and
accurate way.

AlphaCode, as its name suggests, is solely focused on
codes (100%) and does not utilize any other data sources.
This feature uniquely distinguish AlphaCode from other
models and emphasize the significance of this model for
code-based tasks. Bard, Bert, and Pangu models exhibit
identical traits, with each of them concentrating on the
extensive textual data obtained from webpage contents and
books for pretraining the models. Bloom and OPT primarily
emphasize on evaluating data from books and websites, such
as Wikipedia or other online sources. On the other hand,
GLM-130 not only analyzes books and web data but also
incorporates computer code data to provide further techno-
logical benefits. LaMDA, Galactica and CodeGen models
use scientific data source for training which advance these
models to adapt the scientific knowledge and terminology.

26856

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

Hence, these model can lead to a more accurate responses
in scientific domains. AlphaCode and GLM-130 are the
models of choice for code-related tasks, whereas LLaMA
and BERT excel in diverse text data applications. Most of
the LLMs such as T5, GPT models, Gopher, GLam, PaLM,
and BLOOM frequently utilize websource data which helps
them to automate various practical tasks such as content
creation, data analysis and virtual chatbot for answering the
question. On the contrary, some models such as Falcon and
different version of GPT models utilize books and news
data facilitates in educational application such as document
summarization, and article writings. The models trained on
scientific data have several use cases in research domain.
In addition, Table 9 provides contextual information of the
datasets to maintain the transparency of the comparison
among models and provide an effective guide to future model
implementation. The ‘‘Size’’ and ‘‘Source’’ columns of the
Table listed the additional information. The size of datasets
ranges from 5GB (BookCorpus) to a huge 800GB (several
datasets), indicating the sheer magnitude of data required
to train these LLMs. The source information reveals when
and where the data were collected, which is essential for
understanding the temporal relevance of the training data and
potential biases. Table 9 provides a multitude of information
regarding the datasets used to train LLMs and how each
model leverages these datasets. This information is invaluable
for NLP researchers, developers, and practitioners, as it
enables them to make informed decisions about which LLMs
to use for specific tasks.


#### G. PERFORMANCE ANALYSIS OF LLMS
LLMs are models that perform the majority of NLP tasks
and numerous models such as GPT-1 through GPT-4,
Bing, ChatpGPT, and BERT have developed in order to
contribute jointly to the industry and academia. Since in
the literature, we find a scarcity of adequate data pertaining
to LLMs, we present performance outcomes for diverse
tasks to publicly accessible LLMs in Table 10. All GPT
series, including GPT-1, GPT-2, GPT-3, GPT-3.5, and GPT-
4, are evaluated using a variety of metrics, including the
Stanford question answering dataset (SQuAD), language
model benchmark (LAMBADA), and general
language
understanding evaluation (GLUE), as shown in Table 10.
GPT-1 obtains a score of 68.4 on the GLUE, while GPT-
2, GPT-3, GPT-3.5, and GPT-4 attain scores of 84.6, 93.2,
93.5, and 94.4, respectively. GLUE results indicate that
GPT-4 outperforms prior versions of GPT. The GPT-4, i.e.,
in SQuAD and LAMBDA have scores of 93.6 and 82.4,
respectively. As shown in the table, GPT-4 outperforms its
predecessors in both LAMBDA and SQuAD. As GPT-4
outperforms its predecessors in all three benchmark metrics
and exhibits robust performance, it can be concluded that
GPT-4 is significantly more effective than its predecessors in
tasks involving language understanding and language model-
ing. The VietNamese High School Graduation Examination
(VNHSGE) English dataset was utilized to analyze various

LLMs, including GPT-3.5, BingChat, and BARD. Based
on the accuracy presented in Table 10, it is evident that
BingChat LLM outperforms the other two models, achieving
an accuracy of 92.4%. LLMs such as ChatGPT and Bing were
evaluated using the average intraclass correlation coefficient
(ICC) values. The ICC value for Bing was 0.975, whereas
ChatGPT has an ICC value of 0.858. The higher mean ICC
value indicates that Bing exhibited robust performance and
consistency in major NLP tasks. Table 10 depicts that, all
of the LLMs mentioned in the table have been analyzed
and tested on multiple performance metrics and datasets
to validate the robustness and reliability of these language
models.


### VI. Resources Of Large Language Models
LLMs have a wide range of potential applications and
resources available for their development, deployment, and
utilization. Figure 7 presents an LLM taxonomy that divided
into two main branches: i) pre-trained model-based and ii)
API-based. This taxonomy allows us to explore these two
distinct aspects of LLMs.


#### A. PRETRAINED MODELS
Pretrained language models play a pivotal role in NLP
tasks due to their ability to encapsulate broad language
understanding and generation skills from diverse text sources.
They offer a substantial advantage by minimizing the
computational resources and data required for fine-tuning
specific tasks. There are some of
the most common
pre-trained LLMs models, which have been depicted in
Table 11.

1) GENERATIVE PRETRAINED TRANSFORMER (GPT)
GPT [65] is an influential breakthrough in AI, particularly
in NLP tasks. Developed by OpenAI, GPT leverages the
transformer architecture and extensive pre-training on vast
internet text data to achieve a deep understanding of human
language. This generative model excels at tasks like text gen-
eration, translation, question answering, and more, making it
a versatile tool across various NLP domains. GPT’s capacity
to capture intricate language patterns and context, coupled
with its iterative improvements, has profoundly impacted
in academia and industry, revolutionizing the landscape of
language understanding and generation.

2) BERT
BERT [10], short for ‘‘Bidirectional Encoder Representations
from Transformers,’’ is a language model with a distinctive
approach. Unlike previous models, BERT is designed to pre-
train deep bidirectional representations from unlabeled text
by considering both left and right context in all layers. This
pre-trained BERT model can be fine-tuned with minimal
adjustments to create cutting-edge models for various tasks
like question answering and language inference, eliminating
the need for extensive task-specific modifications. BERT is
both conceptually straightforward and remarkably effective,

VOLUME 12, 2024

26857

TABLE 10. Accuracy of various LLMs on different datasets.


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 7. Taxonomy of LLMs.

achieving state-of-the-art results on different NLP tasks.
Notable accomplishments include raising the GLUE score to
80.5% (an impressive 7.7% absolute improvement), boosting
MultiNLI accuracy to 86.7% (a 4.6% absolute improvement),

and significantly improving SQuAD v1.1 question answering
Test F1 to 93.2 (a 1.5 point absolute improvement) and
SQuAD v2.0 Test F1 to 83.1 (a remarkable 5.1 point absolute
improvement).

26858

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 11. Description of LLMs.

In our analysis, we have considered variants of BERT that
are pre-trained on extensive text corpora and possess the
characteristics of LLMs, enabling them to understand and
generate natural language comprehensively. This deliberate
choice ensures that the models we have included in our
study harness the full spectrum of language understanding
and generation capabilities, thereby aligning with the core
objective of our research in exploring the impact and
advancements of LLMs in the field of NLP. Non-LLMs
those with significantly reduced
versions of BERT or
model sizes were excluded from our analysis to maintain
consistency and relevance in our investigation.

3) ROBERTA
RoBERTA is another LLM which replicates the BERT
pre-training approach outlined by Devlin et al.
[67].
We meticulously assess the influence of various critical
hyperparameters and training data sizes. It’s worth noting
that BERT was initially trained with room for improvement,
yet it can now perform on par with or even surpass the
performance of subsequent models that have been published.
As a result, RoBERTa achieves top-tier results in GLUE,
RACE, and SQuAD evaluations. These outcomes underscore

the significance of design decisions that were previously
overlooked and prompt inquiries into the origins of recently
reported advancements.

4) XLNET
XLNet [107] represents a versatile autoregressive pretraining
approach that achieves bidirectional context
learning by
optimizing expected likelihood across all possible combi-
nations. XLNet addresses the constraints of BERT through
its autoregressive design and incorporates insights from
Transformer-XL, a leading autoregressive model. In practical
experiments with consistent conditions, XLNet consistently
surpasses BERT on 20 diverse tasks, frequently by a sub-
stantial margin. These tasks encompass question answering,
natural language inference, sentiment analysis, and document
ranking, among others.

5) SPEECH-XLNET
Speech-XLNet [108] is a method for training unsupervised
acoustic models to learn speech representations using a Self-
Attention Network (SAN) and subsequently fine-tuning it
within the hybrid SAN/HMM framework. Speech-XLNet
regularizer, encouraging the SAN to
acts as a robust

VOLUME 12, 2024

26859


#### M. A. K. Raiaan et al.: Review on Large Language Models

make inferences by prioritizing global structures through
its attention mechanisms. Moreover, Speech-XLNet enables
the model to explore bidirectional contexts, enhancing the
effectiveness of speech representation learning. Experimental
results on TIMIT and WSJ datasets demonstrate that
Speech-XLNet significantly enhances the performance of
the SAN/HMM system in terms of both convergence speed
and recognition accuracy compared to systems trained from
randomly initialized weights. The model best achieves an
impressive relative improvement of 11.9% and 8.3% on
the TIMIT and WSJ tasks, respectively. Notably, the top-
performing system achieves a phone error rate (PER) of
13.3% on the TIMIT test set, which, to the best of our
knowledge, is the lowest PER achieved by a single system.

relation extraction, and named entity recognition. The pre-
trained weights of the model are accessible to the public,
enabling researchers to optimize it using their biomedical
text data. BioGPT has the capacity to substantially drive
biomedical research forward by facilitating the analysis of
vast quantities of biomedical text data in a more precise and
efficient manner [111], [112].

In summary, pre-trained LLMs are foundational in NLP,
providing a starting point for various applications without
the need for extensive training from scratch. They are widely
used and have access to advanced language understanding
and generation capabilities. However, responsible use and
ethical considerations are essential when working with these
models to ensure fair and unbiased outcomes.

6) DIALOGXL
DialogXL [109] introduces enhancements to tackle longer
historical context and multiparty structures in dialogues.
Initially, alterations are made to how XLNet manages
recurrence, transitioning from segment-level to utterance-
thereby improving its effectiveness in modeling
level,
the integration of dialog-
conversational data. Secondly,
aware self-attention, as opposed to the standard self-
attention in XLNet, enables capturing crucial dependencies
within and between speakers. While training the DialogXL,
a comprehensive set of experiments is conducted on four
ERC benchmarks, comparing DialogXL with mainstream
models. The experimental results consistently demonstrate
that DialogXL outperforms the baseline models across all
datasets.

7) T5
T5 (Text-to-Text Transfer Transformer) [84] is a ground-
breaking LLM developed by Google Research, revolution-
izing NLP tasks. T5’s innovation lies in framing all NLP
tasks as text-to-text tasks, simplifying the NLP pipeline
and unifying various tasks under a single framework. Built
upon the Transformer architecture, T5 utilizes multi-head
self-attention to capture intricate language relationships. Its
extensive pre-training on vast text data, followed by fine-
tuning on specific tasks, empowers T5 to excel in text
classification, translation, summarization, question answer-
ing, and more. With consistently state-of-the-art results
across NLP benchmarks, T5 has reshaped the field, offering
researchers and developers a versatile tool for comprehensive
language understanding and generation tasks.

8) BIOGPT
BioGPT [110] is a large-scale language model that was
constructed by the Allen Institute for AI (AI2) with the
explicit purpose of undertaking training on biomedical text.
It was trained on an extensive corpus of biomedical literature,
including PubMed abstracts and full-text articles, and is
based on the GPT architecture. It has been demonstrated
that BioGPT outperforms alternative biomedical language
models across a range of tasks, such as query answering,


#### B. API OF LLMS
In this section, we discuss the APIs of LLMs, which have
been described in Table 12.

Open AI API: The API provided by OpenAI offers access
to GPT models that may be utilized for a wide range of
text-related applications [119]. The API facilitates many
tasks such as coding, question and answer, analysis, and
other related activities. The available models encompass a
spectrum of options, spanning from gpt-4 to gpt-3.5-turbo,
as well as many legacy variants. The Chat Completions API
facilitates interactive dialogues by incorporating distinct roles
such as user, and assistance. The programming language
provides support for function calling, which allows for
the retrieval of structured data. The OpenAI API provides
developers with the capability to leverage advanced modeling
of languages for a diverse range of applications.

Hugging Face: Hugging Face provides a complimentary
Inference API that facilitates the examination and assessment
of more than 150,000 publicly available ML models [120].
It features predictive capabilities, and integration with more
than 20 open-source libraries, and facilitates fast change
between models. The API facilitates a range of operations,
including classification, image segmentation, text analysis,
speech recognition, and other related functionalities.

Google Cloud API: The Cloud-based NLP API developed
by Google provides support for a range of approaches, such as
sentiment analysis, text analysis, entity recognition, and other
text annotations [115]. The functionalities can be accessed by
developers through REST API calls utilizing either the client
libraries or their own custom libraries. Additionally, the API
offers moderation functionalities for the purpose of detecting
potentially sensitive content. Several API exists, and each
possesses distinct features and functions.

Microsoft Azure Language APIs: These APIs support many
activities, including sentiment analysis, text summarization,
and other related tasks [116]. Developers use RESTful
endpoints to include Azure LLMs APIs. Microsoft provides
useful SDKs and code examples in other programming
languages,
to facilitate the
utilization of these APIs.

including Python, Java, etc.

26860

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 12. Comparison of LLMs APIs.

IBM Watson Natural Language: The IBM Watson API
is a robust tool for investigating and extracting valuable
information from textual data. This API offers developers a
variety of functionalities, encompassing sentiment analysis,
emotion analysis, and additional features [117]. Due to its
provision of multilingual support and a user-friendly API,
this technology enables developers to effectively include
sophisticated text analytics into their programs.

Amazon Comprehend API: The Amazon Comprehend
API is a powerful NLP service provided by Amazon Web
Services [118]. This tool evaluates textual data, allowing the
researchers to acquire significant knowledge, such as entity
recognition, language detection, sentiment analysis, and topic
modeling. Due to its ability to accommodate many languages
the tool displays adaptability in
and simple integration,
addressing a range of use cases, including customer feedback
analysis and others. The utilization of this API can prove to
be a significant resource for enterprises’ marketing to extract
practical insights from unstructured textual data.

Facebook AI’s Fairseq: The Fairseq framework developed
by Facebook AI is a comprehensive tool for performing
sequence-to-sequence modeling, specifically designed for
handling LLMs [121]. Fairseq is a well-suited API for
many applications related to analyzing and generating natural
for advanced
language. The platform provides support
models such as BERT and RoBERTa, allowing researchers
to perform fine-tuning on these models according to specific
needs.

In this study, we have provided a comprehensive overview
of seven popular APIs in Table 12 that leverage the capabili-
ties of LLMs for the purpose of NLP-based functionalities.
However, the taxonomy revealed the presence of several
other APIs that are associated with text analysis but do
not utilize LLMs. These APIs are TextBlob, TextRazor,
Sapling AI, MonkeyLearn, and Aylien, etc., which utilize
traditional machine learning, statistical methods, and rule-
based natural NLP techniques instead of relying on extensive
pre-trained LLMs. Since, the primary focus of this study has

VOLUME 12, 2024

26861

been on describing the tools that particularly utilize LLMs
for the purpose of advanced text analysis, generation, and
comprehension, we have refrained from discussing these
APIs in depth.


### VII. Domain Specific Application
Since there are several pre-trained models in LLMs, all
of them are utilized by training or fine-tuned to perform
well-defined tasks maintained by their requirements in
different fields. Numerous research studies have consistently
employed LLMs from the diverse domains such as healthcare,
finance, education, forecasting, and natural language process-
ing. The extensive experiments of different LLMs contribute
to revolutionizing the use of AI across these domains. This
section demonstrates the potential contribution of LLMs
application in different domains. Table 13 illustrates the
major contribution of LLMs in the specific domain, as well
as outline their prospective limitations and future directions.
Bio-Medical and Healthcare: As previously stated, GPT
has several versions, ranging from GPT1 to GPT4. GPT3 is
extremely useful in the healthcare industry since it can be
trained to support customer service with no effort. GPT3 gets
all required information through a conversation rather than
an intake form, and many systems might be built to assist
numerous patients at the same time [126]. Besides, clinics
and hospitals are places to cure illness, but it is also true
that various contagious viruses are brought into these places.
Patients and healthcare providers can be better protected from
infection by replacing a human receptionist with a robot
which becomes increasingly important during the COVID-
19 epidemic [140]. Since clinics and hospitals often see a
high volume of patients on a daily basis, an optimum and
lightweight system may submit several queries for single
patients to create acceptable output.

Consequently, GPT models can also aid in cost reduction
in the medical industry. Furthermore, biomedical and clinical
text mining has always been an essential and major challenge
due to the complex nature of domain corpora and the
continually expanding number of documents. As a result,
BERT models can improve the performance of biomedical
and clinical text mining models [141]. Salam et al., [128]
and Korngiebel et al., [126] demonstrate the substantial
advantages of ChatGPT in the domains of healthcare, clinical
research, and practice, although simultaneously underscoring
the imperative necessity for proactive inspection and ethical
transparency. Several studies [125], [129], [131], [132]
explore the utilities and constraints of LLMs such as
ChatGPT in the context of clinical practice, research, and
public health. In their study, Kung et al., [130] conducted an
evaluation of ChatGPT’s performance on the United States
Medical Licensing Examination (USMLE), and the outcomes
indicate the potentiality of LLMs to support clinical decision-
making and medical education. Sorin et al., [124] evaluated
ChatGPT-3.5 as a decision support for breast tumor boards
where they compared the tumor board’s explanations, and
summaries with ChatGPT-3.5 and showed that ChatGPT-3.5


#### M. A. K. Raiaan et al.: Review on Large Language Models

and the tumor board had a high degree of decision alignment.
Huang et al., [123] investigate the prospective applications
of LLMs with a specific emphasis on ChatGPT, in the field
of dentistry, mainly focusing on automated dental diagnosis
and highlighting the efficacy of LLMs in dental diagnosis.
Furthermore, the XLNet contributes to better clinical note
representation by adding temporal information and a realistic
prediction setup [142]. Furthermore, various LLMs models
also assist the medical industry by making the procedure
easier than previously.

Education: Educators have struggled for a long time
with an unequal educational resources to student demand
across disciplines. One of the significant challenges is a
shortage of accessible educational resources for pupils to
study outside of school. Although online instructional videos
are helping to alleviate the problem, society still hopes that
AI will deliver individualized teaching services to satisfy
the learning demands of each student and increase teaching
efficiency. In the light of above discussion, LLMs have the
potential to revolutionize many facets of learning, teaching,
and educational research in the education sector [140].
The GPT model aids the students in converting the math
word problems into representative equations [143]. Kasenci
et al., [19] highlighted substantial
impact of LLMs in
education by facilitating personalized learning, automating
grading process, and accessibility of educational resources.
Hadi et al., [137] presents a thorough analysis of LLMs, cov-
ering their historical development, wide-ranging applications
in domains such as medicine, engineering, education, and
their potential impact on the trajectory of AI. Lo et al.,
[138] and Dwivedi et. al. [139] investigate the prospective
uses of ChatGpt within the realm of education and identify
the primary obstacles that have arisen during its initial
deployment. Besides, in terms of writing authentic texts in
distinct formats, including essays, summaries, and articles,
these models help to accomplish this without any error.
In contrast, the manual process may have human errors
in the documentation. In this case, the GPT model helps
to address this problem. In addition, the XLNet helps to
understand the texts and documents which can be utilized
in the academic sector [38]. Furthermore, other models may
impact the education system by making it more engaging,
accessible, and productive for both students and teachers.

Social Media: The LLMs have leveraged several aspects
of the social media industry regarding content production,
moderation, sentiment analysis, etc. There are some tasks
in the social media can be generated such as writing
content, classifying text, and even full blogs and articles for
social media. These models can also perform named entity
recognition (NER) and text classification [144], [145]. When
the GPT, XLNet, BERT, etc., models aid the writer and
content producers in generating a consistent flow of write
up. It also provides content suggestions, and to create a
safer online environment, these models are hired to assist
in discovering and filtering out different dangerous and
improper content. Abramski et al., [42] utilized network

26862

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 13. Domain specific machine learning-based study comparison in LLMs.

VOLUME 12, 2024

26863

TABLE 13. (Continued.) Domain specific machine learning-based study comparison in LLMs.


#### M. A. K. Raiaan et al.: Review on Large Language Models

science and the principles of cognitive psychology to evaluate
biases present in LLMs. Sobieszek et al., [136] presents a
critical examination of the stated semantic capabilities of
GPT-3, aiming to challenge the current view of its dismissal.
Moreover, it assists in determining public opinion on certain
topics by analyzing public interest and demand.

Business: In business, LLMs helps companies improve
their decision-making processes, product manufacturing
processes, operations, and customer interactions. Communi-
cating with customers and providing 24/7 customer service
by answering their queries, assisting them in their work,
and providing advanced advice related to areas of interest to
customers is crucial for business progress. Moreover, it is also
important to analyze customer sentiment, market trends, risk
factors, and competitive intelligence [20]. In this case, LLMs
help to fulfill all their requirements within a short period.
The LLMs models, like GPT, XLNet, BERT, etc., play a
vital role in creating customer documents and product details

and efficiently maintaining the entire business by saving
time and reducing laborious tasks. Frederico et al., [135]
presents an initial investigation into the potential applications
and effects of ChatGPT in the domain of supply chain
management. Their study provides significant insights for
professionals engaged in this domain. Mich et. al. [133]
present an initial investigation of potential hazards associated
with the implementation of ChatGPT in bussiness domain.
Yu et al., [134] presented an analysis of the capabilities
of LLMs, specifically GPT-4, in the context of financial
forecasting for a time series. Besides, their findings reveal
that the performance of LLMs outperforms other traditional
models also.

Agriculture: In agriculture, variations of GPT models,
including GPT3, BERT, and XLNet models, play a significant
role [146], [147], [148]. They are able to analyze large data
hubs of soil, crop, and weather data along with satellite
imagery. These models provide recommendations on planting

26864

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 8. Visual representation of impact on LLMs.

times, irrigation, fertilizer application, and optimizing fields
and resources. Farmers can obtain current updates and market
requirements, predict crop prices, anticipate natural disasters,
and document farmers’ and crop details. Manual agricultural
management can be time-consuming and laborious, but these
LLMs can support to accomplish these tasks to a greater
extent.


### VIII. Impact Of Large Language Models On
SOCIETY
LLMs and similar AI technologies have had a profound
impact on society across various domains. The impact
of LLMs on society is multifaceted, and it is important
to consider both the positive and negative consequences.
As these technologies continue to evolve, stakeholders,
including governments, businesses, researchers, and the
general public, must work together to harness the benefits
of LLMs while addressing their challenges and ethical
implications. The visual representation of Figure 8 effectively
demonstrates the impact of LLMs, outlining their benefits on
the left and the adversarial impacts on the right side. The
positive impacts of LLMs are as follows:

- Advancements

in Natural Language Processing
(NLP): LLMs have significantly advanced the field
of NLP, making it possible to automate and scale a
wide range of language-related tasks such as trans-
lation, summarization, sentiment analysis, and more.
In recent years, Natural Language Processing (NLP) has
witnessed significant advancements, primarily driven
by the emergence of Large Language Models (LLMs).
These advancements, exemplified by models such as
BERT [10], RoBERTa [67], and XLNet [107], have
transformed the NLP landscape. Notably, LLMs have
been fine-tuned for various specific NLP tasks, enabling
remarkable performance improvements. Multilingual
models like mBERT [149] and cross-lingual models like
XLM-R [150] have facilitated language understanding
across diverse linguistic contexts. Additionally, there
has been a focus on creating more efficient versions of
LLMs such as DistilBERT [151] and ALBERT [152].

These developments have not only expanded the
applicability of NLP but have also raised ethical consid-
erations, prompting research in bias mitigation [153] and
responsible AI. LLMs have enabled breakthroughs in
applications like conversational AI, few-shot and zero-
shot learning, and domain-specific NLP in fields like
healthcare and finance. These advancements underscore
the pivotal role of LLMs in advancing the capabilities
of NLP and continue to shape the future of language
understanding and generation.

- Automation and Efficiency: LLMs are used to automate
tasks that were previously time-consuming and labor-
intensive, leading to increased efficiency in industries
such as customer support, content generation, and data
analysis. The automation and efficiency of LLMs, driven
by models like BERT and GPT, have revolutionized
industries and applications. These models have auto-
mated intricate language-related tasks, from sentiment
analysis to language translation, making them more effi-
cient and accessible. LLMs, such as DialoGPT [154] and
ChatGPT, have powered conversational AI, streamlining
customer support and interactions. Moreover, they excel
in few-shot and zero-shot learning, as demonstrated by
GPT-3 [155], automating tasks with minimal examples.
Multilingual LLMs like mBERT have automated lan-
guage tasks across various languages, enhancing global
accessibility. Efficiency has further advanced through
models like DistilBERT and ALBERT, which maintain
performance while reducing computational resources.
These models can be fine-tuned for specific domains,
such as healthcare [156], making them indispensable in
automating domain-specific tasks efficiently.

- Content Generation: LLMs are capable of generating
human-like text, which has implications for content
creation, including automated news articles, marketing
materials, and creative writing.

- Language Translation: LLMs have improved machine
translation systems, making communication across lan-
guages more accessible and accurate.

- Virtual Assistants and Chatbots: LLMs power virtual
assistants and chatbots, enhancing customer service and
providing round-the-clock support in various industries.
- Medical and Scientific Research: LLMs are used
to analyze and summarize vast amounts of medical
and scientific literature, aiding researchers in finding
relevant information quickly.

- Accessibility: LLMs have the potential

to improve
accessibility by providing real-time translation and
transcription services for
individuals with hearing
impairments or language barriers.

- Personalization: LLMs enable personalized recommen-
dations and content curation on platforms such as social
media, e-commerce, and news websites.

- Creative Tools: LLMs are used as creative tools in
various art forms, including generating poetry, music,
and visual art.

VOLUME 12, 2024

26865

- Education and Skill Development: The rise of LLMs
underscores the importance of education and skill devel-
opment in AI and data science, as these technologies
become increasingly integral to various industries.

In addition to numerous positive sides, LLMs also entail

some downsides. These downsides are outlined as follows:

- Ethical Concerns: Bias and fairness issues in LLMs
have raised ethical concerns. LLMs may perpetuate or
amplify biases present in training data, leading to unfair
or discriminatory outcomes.

- Misinformation and Disinformation: LLMs can gener-
ate realistic-sounding fake text, raising concerns about
the spread of misinformation and disinformation.

- Job Displacement: The automation capabilities of
LLMs may lead to job displacement in certain industries,
particularly in routine data-entry and content-generation
roles.

- Data Privacy: The use of LLMs often involves pro-
cessing large amounts of user-generated text data,
which raises data privacy concerns, especially regarding
sensitive or personal information.

- Economic Impact: The adoption of LLMs can disrupt
traditional business models and create economic shifts
as industries adapt to automation and AI technologies.
- Regulation and Accountability: Policymakers and
regulators are grappling with the need to establish
guidelines and regulations for the responsible use of
LLMs, including addressing issues of bias, transparency,
and accountability.


### IX. Industrial Significance Of Large Language
MODELS
LLMs have gained substantial popularity in various indus-
tries, bringing about radical transformations. Influence of
LLMs in industries is visible which can be presented through
several key facets:

1. Enhancing NLP Applications: LLMs have ushered in
a revolution in NLP applications [157] across sectors like
customer service, chatbots, and sentiment analysis. They
contribute to more precise and efficient interactions with
users, leading to increased customer satisfaction and reduced
response times.

2. Enabling Data Analysis and Information Extraction:
LLMs play a pivotal role in extracting valuable insights
from unstructured text data [158]. This is particularly
critical in fields like finance, market research [159], and
healthcare, where deciphering market trends, sentiment in
news, or medical records hold paramount significance.

3. Facilitating Translation Services:

Industries heavily
reliant on multilingual communication [160], such as e-
commerce, travel, and international business which may be
benefited from LLMs that streamline automated translation.
Translation service saves resources and ensuring high-quality
translations across multiple languages.

4. Empowering Content Generation: LLMs are harnessed
for content generation [161], which encompasses automated


#### M. A. K. Raiaan et al.: Review on Large Language Models

article writing, social media posts [162], product descriptions,
and more. This automation simplifies content creation
processes and allows for scalable production of top-tier
content.

5. Revolutionizing Healthcare: LLMs find applications in
medical record analysis [129], diagnosis assistance, and drug
discovery. They empower healthcare professionals to access
and comprehend extensive medical literature and patient data,
thereby enhancing healthcare decision-making.

6. Revamping Education: The education sector [163]
leverages LLMs for automated grading, ensuring prompt
feedback to students. These models also contribute to the
development of intelligent tutoring systems and personalized
learning platforms.

7. Aiding Legal Practices: Legal practitioners [164]
benefit from LLMs for contract analysis, legal research,
and document review. These models assist in efficiently
extracting pertinent information and identifying potential
legal concerns.

8. Assisting Human Resources: LLMs support HR
professionals [165] in tasks like candidate screening, resume
job candidates. They
parsing, and identifying potential
streamline time-consuming processes within the recruitment
phase.

9. Empowering Financial Services: In the realm of
financial services [166], LLMs come into play for activities
like sentiment analysis of news articles, algorithmic trading,
risk assessment, and fraud detection. They are instrumental in
making informed investment choices and managing financial
risks.

10. Boosting E-commerce: LLMs enable personalized
product
recommendations [167], chatbots for customer
support, and efficient inventory management. These enhance-
ments result in enriched user experiences and heightened
sales.

11. Illuminating Customer Insights: LLMs analyze
customer reviews [168], feedback, and social media data, fur-
nishing businesses with insights into customer preferences,
opinions, and sentiments. This invaluable information aids
companies in customizing their products and services.

As LLMs continue to advance, their industrial impor-
tance is undeniable. LLMs streamline operations, enhance
decision-making, and bolster efficiency across diverse
domains, positioning them as a transformative technology in
the contemporary business landscape.


### X. Open Issues And Challenges
This section discusses critical analysis of open issues and
challenges of LLMs.


#### A. OPEN ISSUES
In this section, we delve into the open issues related to LLMs.
These issues appeared recently as focal point in AI research
and development. We raise the necessity for ongoing research
and innovation to resolve issues that have emerged alongside
the rapid development of LLMs. Our discussion will cast light

26866

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

on the significance of these unresolved issues, highlighting
their impact on various applications and the AI landscape as
a whole.

- Issue 1: Ethical and Responsible AI The question
regarding how to ensure the ethical use of large language
models remains unresolved. Filtering, moderation, and
accountability concerns regarding AI-generated content
remain problematic. Misinformation, hate speech, and
biased content generated by LLMs necessitate continu-
ous research and development [169].

- Issue 2: Multimodal Integration While LLMs are
predominantly concerned with text, there is a growing
demand for multimodal models that can comprehend
and generate content that includes text, images, and
other media types [170]. Integrating multiple modalities
into a single model poses difficulties in data acquisition,
training, and evaluation.

- Issue 3: Energy Efficiency The environmental impact
of training and deploying large language models is still
an urgent concern [171]. It is essential to develop more
energy-efficient training methods, model architectures,
and hardware solutions to reduce the carbon footprint of
LLMs.

- Issue 4: Security and Adversarial Attacks

LLMs are vulnerable to adversarial context, where
slight input modifications can lead to an unexpected
and potentially harmful outputs [172]. Improving model
robustness and security against such situation is a crucial
area of study, particularly for cybersecurity and content
moderation applications.

- Issue 5: Privacy and Data Protection As LLMs
become more competent, user privacy and data protec-
tion concerns increase. Finding methods for users to
interact with these models without compromising their
personal information is an ongoing challenge. There is a
need for research on privacy-preserving techniques and
regulatory compliance [173].

- Issue 6: Generalization and Few-Shot Learning
LLMs performs well when there is abundant data
but struggles with tasks requiring few examples or
domain-specific knowledge. Improving their capacity to
generalize and perform well with limited training data is
a crucial area of research [174].

- Issue 7: Cross-Lingual and Low-Resource Settings It
is an ongoing challenge to make LLMs more accessible
and effective in languages and regions with limited
resources and data [175]. Global applications require
developing techniques for cross-lingual transfer learning
and low-resource language support.


#### B. CHALLENGES
LLMs have rapidly evolved from being non-existent
to
becoming a ubiquitous presence in the field of machine
learning within just a few years. Its extraordinary ability
to generate text that resembles that of a human which has

attracted significant attention and applications in numerous
fields. However,
this sudden rise of these technological
dependencies with higher impact has also revealed many
challenges and concerns. In this discussion, we will examine
ten of the most significant challenges pertaining to LLMs.

- Challenge 1: Data Complexity and Scale In the era of
LLMs, the size and complexity of the datasets on which
they are trained is one of the most significant challenges.
These models are typically trained on enormous corpora
of Internet-sourced text data. These datasets are so
extensive that it is nearly impossible to understand or
investigate the totality of their information. This raises
concerns regarding the quality and biases of the training
data and the potential for the unintentional dissemination
of detrimental or inaccurate information [176].

- Challenge 2: Tokenization Sensitivity

For analysis, LLMs rely significantly on tokeniza-
tion, dividing text into smaller units (tokens) [177].
Tokenization is essential for language processing and
comprehension but can also present challenges. For
instance, the meaning of a sentence can alter signifi-
cantly based on the choice of tokens or the ordering
of words. This sensitivity to input phrasing can lead
to unintended outcomes when generating text, such
as adversarial assaults and output variations based on
minute input changes.

- Challenge 3: Computational Resource Demands

The training of LLMs is a computationally intensive
procedure that requires substantial hardware and energy
resources [178]. It
is necessary to have access to
supercomputing clusters or specialized hardware in
order to train large models, and the environmental
impact of such resource-intensive training has raised
concerns. Significant energy consumption is associated
with training LLMs at scale, contributing to the AI
industry’s overall carbon footprint.

- Challenge 4: Fine-Tuning Complexity

While pre-training gives LLMs a broad comprehension
of language, fine-tuning is required to adapt
these
models to specific tasks [179]. Fine-tuning entails
training the model on a smaller dataset, frequently
requiring human annotators to label examples. As it
involves the construction of task-specific datasets and
extensive human intervention, this process can be both
time-consuming and costly.

- Challenge 5: Real-Time Responsiveness The remark-
able training capabilities of LLMs come at the expense
of inference speed. Real-time response or prediction
generation with these models can be sluggish, limiting
their applicability in applications such as chatbots or
recommendation systems where low-latency responses
are crucial for user satisfaction.

- Challenge 6: Contextual Constraints

LLMs can only evaluate a limited number of preceding
tokens when generating text due to their limited context

VOLUME 12, 2024

26867

window [180]. This limitation presents difficulties when
working with lengthy documents or having lengthy
conversations. Maintaining coherence and relevance
over lengthy text sequences can be challenging because
the model may neglect or lose track of the relevant
information.

- Challenge 7: Bias and Undesirable Output

In the output, LLMs display biases or undesirable
characteristics. This is due to the inherent biases in
the training data, which are assimilated by the model
and reflected in its responses [181]. Such biases can
manifest as objectionable, discriminatory, or harmful
content, making it imperative to address and mitigate
these concerns to ensure the responsible deployment of
AI.

- Challenge 8: Knowledge Temporality

LLMs learn using historical data from the Internet, and
their knowledge is restricted to what is available as of
a particular date. Consequently, they may lack access
to the most recent information or events. This can be
problematic when users expect up-to-date responses or
when the conversation involves recent events.

- Challenge 9: Evaluation Complexity

Evaluation of LLMs presents significant difficulties.
Many extant evaluation metrics are insufficient
to
capture the nuances of model performance, which
raises questions about their efficacy. Additionally, these
metrics can be susceptible to manipulation or gaming,
which may provide an inaccurate image of a model’s
capabilities. To assess LLMs’ actual performance and
limitations, robust and reliable evaluation methodolo-
gies are required.

- Challenge 10: Dynamic Evaluation Needs

Frequently, evaluating LLMs entails comparing their
outputs to static benchmarks or human-authored ground
truth. However, language is dynamic and evolves, and
preset evaluation data may not adequately reflect a
model’s adaptability to language and context change.
This difficulty underscores the need for evaluation
frameworks that are more dynamic and continually
updated.


### XI. Future Research Prospects On Llms
Since LLMs are emerging research topic in recent times,
several key research focuses and directions are prominent
that may address and resolve the challenges and open issues
discussed earlier. Resolving these open issues and challenges
may harness the full potential of LLMs while ensuring its
responsible and ethical use in AI landscape.


#### A. ENHANCING BIAS MITIGATION
Researchers are dedicated to refining training data to
minimize bias, devising effective debiasing techniques, and
establishing guidelines for responsible AI development [182].


#### M. A. K. Raiaan et al.: Review on Large Language Models

They also need focus on integrating continuous monitoring
and auditing mechanisms into AI pipelines, thereby conform-
ing fairness and impartiality of the system. This commitment
to mitigating bias ensures that LLMs not only advance in
capability but LLMs also upholds ethical standards.


#### B. EFFICIENCY OPTIMIZATION
A core concern driving research is the quest of efficient
training techniques. Researchers are delving into innovative
methods like federated learning, which enables the distri-
bution of training across decentralized data sources [183].
They are also exploring knowledge distillation techniques
for model compression and finding ways to reduce the
substantial computational and environmental costs associated
with LLMs. This optimization paves the way for more
sustainable and resource-efficient AI models.


#### C. DYNAMIC CONTEXT HANDLING
LLMs are being endowed with enhanced context manage-
ment capabilities. This empowers them to comprehend longer
context windows and seamlessly handle extensive documents
or conversations. Such enhancements significantly expand
their utility in various applications and resolve previous
limitations.


#### D. CONTINUOUS LEARNING
To keep LLMs up-to-date, researchers are focusing on
developing techniques that enable these models to adapt
on evolving language and knowledge over
time. This
ensures that LLMs remain valuable and accurate sources of
information and consistently overcoming challenges of being
outdated.


#### E. INTERPRETABLE AI
The research community is committed to making LLMs’
outputs more transparent and interpretable. Improving inter-
pretability fosters the confidence and comprehension in AI
decision-making processes which has been a major concern
for a long time after the advent of LLMs [184].


#### F. MULTIMODAL LLMS
Researchers are pioneering the development of LLMs that
incorporate text, vision, and other modalities [185]. These
models can understand and generate text from images, videos,
and audio, creating new avenues for AI applications and
effectively addressing the need for multi-sensory comprehen-
sion.


#### G. HUMAN-AI COLLABORATION
Research on how humans and LLMs can collaborate
effectively, with AI assisting and augmenting human tasks,
is a crucial focal point. This collaboration bridges the gap
between AI capabilities and human needs, thereby resolving
previous challenges and issues in deployment.

26868

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models


#### H. DYNAMIC EVALUATION METRICS AND RELEVANT
BENCHMARKS
Researchers are working on dynamic evaluation metrics that
adapt to changing language and context, ensuring that LLMs
performance is accurately assessed [186]. Finding a suitable
metric along with the development of relevant and up-to-
date benchmarks which may address earlier shortcomings in
assessing AI capabilities.


### I. Personalization And Customization
Techniques to customize LLMs interactions to individual user
preferences and needs are gaining popularity nowadays. This
personalization boosts user satisfaction and resolves issues
related to one-size-fits-all AI interactions.


#### J. ETHICAL AND LEGAL FRAMEWORKS
In response to evolving AI regulation, researchers are
diligently developing ethical and legal regulatory frame-
works. These frameworks serve as guiding principles
for
the responsible use of LLMs and ensure com-
pliance with data protection and privacy regulations,
effectively addressing previous concerns about ethical AI
deployment [187].

These future research directions may overcome longstand-
ing challenges and open issues raised in LLMs domain. These
avenues may lead to the maximization of LLMs potential by
the future researchers while upholding the highest standards
of accountability and ethics in AI landscape.


### XII. Limitations
While conducting a thorough examination of LLMs, which
includes analyzing their taxonomies, comparing configura-
tions, and addressing concerns and obstacles, it is essential
to recognize the existence of limitations that should be
considered. A primary limitation of this study is the unavail-
ability of review papers that directly relate to the topic of
LLMs. Although we have made diligent attempts to address
the available research thoroughly, the limited quantity of
papers in this field restricts our potential to perform broad
comparisons and evaluations. While endeavoring to offer a
broad perspective on LLMs concepts, we recognize that this
analysis predominantly focuses on the ground-level concepts
of LLMs configurations and applications. Limited resources,
time, and page constraints affect the extensive exploration
of individual LLMs architectures. Although our goal
is
not to offer the understanding of single LLMs but instead
provide the evolution of LLMs and its application around
various domains, however, readers looking for detailed
analysis of specific architectures and advanced topics are
the impact of the
not
LLMs across various domains, including education, health,
and economy, is highlighted, but assessing the practical
impacts of LLMs in many domains can be complex and
subjective, especially when considering their impact on social
aspects.

thoroughly covered. Furthermore,


### XIII. Conclusion
The field of LLMs has witnessed a remarkable evolu-
tion and expansion, resulting in extraordinary capabilities
in NLP tasks and various applications in various areas.
Based on neural networks and the changing transformer
architecture, these LLMs have revolutionized our approach
to machine language comprehension and generation. The
thorough review of this research has provided an insightful
overview of LLMs, encompassing their historical develop-
ment, architectural foundations, training methods, and vast
advancement resources. The study has also examined the
various applications of LLMs in disciplines such as health-
care, education, social sciences, business, and agriculture,
demonstrating their potential to address real-world issues.
In addition, this review has delved into the societal effects
of LLMs, discussing how they shape the future of AI and
can be utilized to address complex problems. However, the
study has not addressed the pressing challenges and ethical
considerations associated with deploying LLMs, including
model biases, privacy concerns, and the need for enhanced
robustness and controllability. As the field of LLMs research
continues to evolve swiftly, this review could be a valuable
resource for practitioners, researchers, and experts seeking
a comprehensive understanding of LLMs’ past, present, and
future. The study emphasizes the significance of ongoing
efforts to improve the efficacy and dependability of LLMs,
as well as the need for ethical development and deployment
practices. LLMs represent a pivotal advancement
in AI
and NLP, with the potential to revolutionize a variety of
domains and solve complex problems. This article provides a
comprehensive foundation for future researcher to understand
the dynamics of ever evolving Large Language Models
research.

REFERENCES

[1] S. Pinker, The Language Instinct: How the Mind Creates Language.

London, U.K.: Penguin, 2003.

[2] M. D. Hauser, N. Chomsky, and W. T. Fitch, ‘‘The faculty of language:
What is it, who has it, and how did it evolve?’’ Science, vol. 298, no. 5598,
pp. 1569–1579, Nov. 2002.

[3] W. X. Zhao et al., ‘‘A survey of large language models,’’ 2023,

arXiv:2303.18223.

[4] I. Turing, ‘‘Computing machinery and intelligence,’’ Mind, vol. 59,

no. 236, p. 433, 2007.

[5] Y. Shen, L. Heacock, J. Elias, K. D. Hentel, B. Reig, G. Shih, and L. Moy,
‘‘ChatGPT and other large language models are double-edged swords,’’
Radiology, vol. 307, no. 2, Apr. 2023, Art. no. e230163.

[6] M. A. K. Raiaan, K. Fatema, I. U. Khan, S. Azam, M. R. U. Rashid,

#### M. S. H. Mukta, M. Jonkman, and F. De Boer, ‘‘A lightweight
robust deep learning model gained high accuracy in classifying a
wide range of diabetic retinopathy images,’’ IEEE Access, vol. 11,
pp. 42361–42388, 2023.

[7] B. Ramabhadran, S. Khudanpur, and E. Arisoy, ‘‘Proceedings of the
NAACL-HLT 2012 workshop: Will we ever really replace the N-gram
model? On the future of language modeling for HLT,’’ in Proc. NAACL-
HLT, 2012, pp. 1–11.

[8] T. Mikolov, M. Karafiát, L. Burget, J. Černock`y, and S. Khudanpur,
‘‘Recurrent neural network based language model,’’ in Proc. Annu. Conf.
Int. Speech Commun. Assoc. (ISCA), 2010, pp. 1045–1048.

[9] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
in

‘‘Attention is all you need,’’

Ł. Kaiser, and I. Polosukhin,
Proc. Adv. Neural Inf. Process. Syst., vol. 30, 2017.

VOLUME 12, 2024

26869

[10] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, ‘‘BERT: Pre-training
of deep bidirectional transformers for language understanding,’’ 2018,
arXiv:1810.04805.

[11] Y. Khare, V. Bagal, M. Mathew, A. Devi, U. D. Priyakumar, and

#### C. Jawahar, ‘‘MMBERT: Multimodal BERT pretraining for improved
medical VQA,’’ in Proc. IEEE 18th Int. Symp. Biomed. Imag. (ISBI),
Apr. 2021, pp. 1033–1036.

[12] R. Liu, C. Jia, J. Wei, G. Xu, L. Wang, and S. Vosoughi, ‘‘Mitigating
political bias in language models through reinforced calibration,’’ in
Proc. AAAI Conf. Artif. Intell., 2021, vol. 35, no. 17, pp. 14857–14866.

[13] K. Sanderson, ‘‘GPT-4 is here: What scientists think,’’ Nature, vol. 615,

no. 7954, p. 773, Mar. 2023.

[14] S. Pichai.

(2023). An Important Next Step on Our AI Jour-
ney. [Online]. Available: https://blog.google/technology/ai/bard-google-
ai-search-updates

[15] R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin,

#### P. Liang, and T. B. Hashimoto. (2023). Alpaca: A Strong, Repli-
cable Instruction-following Model. [Online]. Available: https://crfm.
stanford.edu/2023/03/13/alpaca.html

[16] L. Fan, L. Li, Z. Ma, S. Lee, H. Yu, and L. Hemphill, ‘‘A bibliometric
review of large language models research from 2017 to 2023,’’ 2023,
arXiv:2304.02020.

[17] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi,

#### C. Wang, Y. Wang, W. Ye, Y. Zhang, Y. Chang, P. S. Yu, Q. Yang,
and X. Xie, ‘‘A survey on evaluation of large language models,’’ 2023,
arXiv:2307.03109.

[18] J. Huang and K. C.-C. Chang, ‘‘Towards reasoning in large language

models: A survey,’’ 2022, arXiv:2212.10403.

[19] E. Kasneci et al., ‘‘ChatGPT for good? On opportunities and challenges
of large language models for education,’’ Learn. Individual Differences,
vol. 103, Apr. 2023, Art. no. 102274.

[20] M. U. Hadi, R. Qureshi, A. Shah, M. Irfan, A. Zafar, M. Shaikh, N. Akhtar,

#### J. Wu, and S. Mirjalili, ‘‘A survey on large language models: Applications,
challenges, limitations, and practical usage,’’ TechRxiv, 2023.

[21] B. Cronin, ‘‘Annual review of information science and technology,’’ Inf.

Today, Medford, OR, USA, 2004, vol. 39.

[22] M. Kardum, ‘‘Rudolf Carnap—The grandfather of artificial neural
networks: The influence of Carnap’s philosophy on walter pitts,’’ in Guide
to Deep Learning Basics. Cham, Switzerland: Springer, 2020, pp. 55–66.
[23] G. Leech, ‘‘Corpora and theories of linguistic performance,’’ Svartvik,

#### J. Directions Corpus Linguistics, vol. 10, pp. 22–105, Jun. 1992.

[24] J. Hirschberg, B. W. Ballard, and D. Hindle, ‘‘Natural

language

L.

and

Juang

Rabiner,

[25] B.-H.

processing,’’ AT&T Tech. J., vol. 67, no. 1, pp. 41–57, Jan. 1988.
R.

speech
recognition—A brief history of the technology development,’’ Georgia
Inst. Technol., Santa Barbara, CA, USA, Tech. Rep., 2005, vol. 1, p. 67.
[26] D. S. Hain, R. Jurowetzki, T. Buchmann, and P. Wolf, ‘‘A text-
embedding-based approach to measuring patent-to-patent technological
similarity,’’ Technol. Forecasting Social Change, vol. 177, Apr. 2022,
Art. no. 121559.

‘‘Automatic

[27] G. Curto, M. F. Jojoa Acosta, F. Comim, and B. Garcia-Zapirain,
‘‘Are AI systems biased against the poor? A machine learning analysis
using Word2Vec and GloVe embeddings,’’ AI Soc., vol. 2022, pp. 1–16,
Jun. 2022.

[28] P. Azunre, Transfer Learning for Natural Language Processing.

New York, NY, USA: Simon and Schuster, 2021.

[29] Y. Shi, M. Larson, and C. M. Jonker, ‘‘Recurrent neural network language
model adaptation with curriculum learning,’’ Comput. Speech Lang.,
vol. 33, no. 1, pp. 136–154, Sep. 2015.

[30] A. Kovačević and D. Kečo,

‘‘Bidirectional LSTM networks for
abstractive text summarization,’’ in Advanced Technologies, Systems, and
Applications VI. Cham, Switzerland: Springer, 2021, pp. 281–293.
[31] Y. Wu et al., ‘‘Google’s neural machine translation system: Bridging the
gap between human and machine translation,’’ 2016, arXiv:1609.08144.
and S. Kumar,
in

[32] R. K. Yadav, S. Harwani, S. K. Maurya,

‘‘Intelligent chatbot using GNMT, SEQ-2-SEQ techniques,’’
Proc. Int. Conf. Intell. Technol. (CONIT), Jun. 2021, pp. 1–5.

[33] D. Luitse and W. Denkena, ‘‘The great transformer: Examining the role
of large language models in the political economy of AI,’’ Big Data Soc.,
vol. 8, no. 2, Jul. 2021, Art. no. 205395172110477.

[34] M. Onat Topal, A. Bas, and I. van Heerden, ‘‘Exploring transformers
language generation: GPT, BERT, and XLNet,’’ 2021,

in natural
arXiv:2102.08036.


#### M. A. K. Raiaan et al.: Review on Large Language Models

[35] T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi, P. Cistac,

#### T. Rault, R. Louf, and M. Funtowicz, ‘‘TransFormers: State-of-the-art
natural language processing,’’ in Proc. Conf. Empirical Methods Natural
Lang. Syst. Demonstrations, 2020, pp. 38–45.

[36] C. Sur, ‘‘RBN: Enhancement in language attribute prediction using
global representation of natural language transfer learning technology like
Google BERT,’’ Social Netw. Appl. Sci., vol. 2, no. 1, p. 22, Jan. 2020.

[37] J. J. Bird, A. Ekárt, and D. R. Faria, ‘‘Chatbot interaction with artificial
intelligence: Human data augmentation with t5 and language transformer
ensemble for text classification,’’ J. Ambient Intell. Humanized Comput.,
vol. 14, no. 4, pp. 3129–3144, Apr. 2023.

[38] B. D. Lund and T. Wang, ‘‘Chatting about ChatGPT: How may AI and
GPT impact academia and libraries?’’ Library Hi Tech News, vol. 40,
no. 3, pp. 26–29, May 2023.

[39] A. Radford, K. Narasimhan, T. Salimans, and I. Sutskever. Improving
Language Understanding by Generative Pre-Training. Mikecaptain.com.
Accessed: Feb. 15, 2024. [Online]. Available: https://www.mikecaptain.
com/resources/pdf/GPT-1.pdf

[40] B. Ghojogh and A. Ghodsi. Attention Mechanism, Transformers, BERT,
and GPT: Tutorial and Survey. Osf.io. Accessed: Feb. 15, 2024. [Online].
Available: Osf.io.

[41] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever,
‘‘Language models are unsupervised multitask learners,’’ OpenAI Blog,
vol. 1, no. 8, p. 9, 2019.

[42] K. Abramski, S. Citraro, L. Lombardi, G. Rossetti, and M. Stella,
‘‘Cognitive network science reveals bias in GPT-3, GPT-3.5 turbo, and
GPT-4 mirroring math anxiety in high-school students,’’ Big Data Cognit.
Comput., vol. 7, no. 3, p. 124, Jun. 2023.

[43] M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and

#### B. Catanzaro, ‘‘Megatron-LM: Training multi-billion parameter language
models using model parallelism,’’ 2019, arXiv:1909.08053.

[44] D. M. Katz, M.

‘‘GPT-4 passes the bar exam,’’ Mar. 2023.
http://dx.doi.org/10.2139/ssrn.4389233


#### J. Bommarito, S. Gao, and P. Arredondo,
[Online]. Available:

[45] M. J. Page, J. E. McKenzie, P. M. Bossuyt, I. Boutron, T. C. Hoffmann,

#### C. D. Mulrow, L. Shamseer, J. M. Tetzlaff, E. A. Akl, and S. E. Brennan,
‘‘The prisma 2020 statement: An updated guideline for reporting
systematic reviews,’’ Int. J. Surg., vol. 88, Jan. 2020, Art. no. 105906.

[46] J. J. Webster and C. Kit, ‘‘Tokenization as the initial phase in NLP,’’ in

Proc. 14th Conf. Comput. Linguistics (COLING), vol. 4, 1992.

[47] T. Kudo, ‘‘Subword regularization: Improving neural network translation

models with multiple subword candidates,’’ 2018, arXiv:1804.10959.

[48] R. Sennrich, B. Haddow, and A. Birch, ‘‘Neural machine translation of

rare words with subword units,’’ 2015, arXiv:1508.07909.

[49] M. Schuster and K. Nakajima, ‘‘Japanese and Korean voice search,’’
in Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP),
Mar. 2012, pp. 5149–5152.

[50] R. Child, S. Gray, A. Radford, and I. Sutskever, ‘‘Generating long

sequences with sparse transformers,’’ 2019, arXiv:1904.10509.

[51] K. Hornik, M. Stinchcombe, and H. White, ‘‘Multilayer feedforward
networks are universal approximators,’’ Neural Netw., vol. 2, no. 5,
pp. 359–366, Jan. 1989.

[52] V. Nair and G. E. Hinton, ‘‘Rectified linear units improve restricted
Boltzmann machines,’’ in Proc. 27th Int. Conf. Mach. Learn., 2010,
pp. 807–814.

[53] D. Hendrycks and K. Gimpel, ‘‘Gaussian error linear units (GELUs),’’

2016, arXiv:1606.08415.

[54] B. Zhang and R. Sennrich, ‘‘Root mean square layer normalization,’’ in

Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019.

[55] B. Workshop et al., ‘‘BLOOM: A 176B-parameter open-access multilin-

gual language model,’’ 2022, arXiv:2211.05100.

[56] B. Lester, R. Al-Rfou, and N. Constant, ‘‘The power of scale for

parameter-efficient prompt tuning,’’ 2021, arXiv:2104.08691.

[57] X. Lisa Li and P. Liang, ‘‘Prefix-tuning: Optimizing continuous prompts

for generation,’’ 2021, arXiv:2101.00190.

[58] H. W. Chung et al., ‘‘Scaling instruction-finetuned language models,’’

2022, arXiv:2210.11416.

[59] I. U. Khan, M. A. K. Raiaan, K. Fatema, S. Azam, R. U. Rashid,

#### S. H. Mukta, M. Jonkman, and F. De Boer, ‘‘A computer-aided
diagnostic system to identify diabetic retinopathy, utilizing a modified
compact convolutional transformer and low-resolution images to reduce
computation time,’’ Biomedicines, vol. 11, no. 6, p. 1566, May 2023.

26870

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

[60] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neubig, ‘‘Pre-train,
prompt, and predict: A systematic survey of prompting methods in natural
language processing,’’ ACM Comput. Surv., vol. 55, no. 9, pp. 1–35,
2023.

[61] W. Ansar, S. Goswami, A. Chakrabarti, and B. Chakraborty, ‘‘A novel
selective learning based transformer encoder architecture with enhanced
word representation,’’ Appl. Intell., vol. 53, no. 8, pp. 9424–9443,
Apr. 2023.

[62] G. Dar, M. Geva, A. Gupta, and J. Berant, ‘‘Analyzing transformers in

embedding space,’’ 2022, arXiv:2209.02535.

[63] D. Hazarika, M. Namazifar, and D. Hakkani-Tür, ‘‘Attention bias-
ing and context augmentation for zero-shot control of encoder–
decoder transformers for natural language generation,’’ in Proc. AAAI
Conf. Artif. Intell., 2022, vol. 36, no. 10, pp. 10738–10748.

[64] J. Lu, J. Yao, J. Zhang, X. Zhu, H. Xu, W. Gao, C. Xu, T. Xiang, and

#### L. Zhang, ‘‘SOFT: Softmax-free transformer with linear complexity,’’ in
Proc. Adv. Neural Inf. Process. Syst., vol. 34, 2021, pp. 21297–21309.

[65] L. Floridi and M. Chiriatti, ‘‘GPT-3: Its nature, scope, limits, and

consequences,’’ Minds Mach., vol. 30, no. 4, pp. 681–694, Dec. 2020.

[66] X. Zheng, C. Zhang, and P. C. Woodland, ‘‘Adapting GPT, GPT-2
and BERT language models for speech recognition,’’ in Proc. IEEE
Autom. Speech Recognit. Understand. Workshop (ASRU), Dec. 2021,
pp. 162–168.

[67] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis,

#### L. Zettlemoyer, and V. Stoyanov, ‘‘RoBERTa: A robustly optimized
BERT pretraining approach,’’ 2019, arXiv:1907.11692.

[68] A. Roberts, C. Raffel, and N. Shazeer, ‘‘How much knowledge can you
pack into the parameters of a language model?’’ 2020, arXiv:2002.08910.
[69] A. Chowdhery et al., ‘‘PaLM: Scaling language modeling with path-

ways,’’ 2022, arXiv:2204.02311.

[70] R. Thoppilan et al., ‘‘LaMDA: Language models for dialog applications,’’

2022, arXiv:2201.08239.

[71] A. Zeng, X. Liu, Z. Du, Z. Wang, H. Lai, M. Ding, Z. Yang, Y. Xu,

#### W. Zheng, X. Xia, W. L. Tam, Z. Ma, Y. Xue, J. Zhai, W. Chen,

#### P. Zhang, Y. Dong, and J. Tang, ‘‘GLM-130B: An open bilingual pre-
trained model,’’ 2022, arXiv:2210.02414.

[72] J. W. Rae et al., ‘‘Scaling language models: Methods, analysis & insights

from training gopher,’’ 2021, arXiv:2112.11446.

[73] O. Lieber, O. Sharir, B. Lenz, and Y. Shoham, ‘‘Jurassic-1: Technical
details and evaluation,’’ White Paper. AI21 Labs, vol. 1, p. 9, 2021.
[74] S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari, J. Casper,

#### Z. Liu, S. Prabhumoye, G. Zerveas, V. Korthikanti, E. Zhang, R. Child,

#### R. Yazdani Aminabadi, J. Bernauer, X. Song, M. Shoeybi, Y. He,

#### M. Houston, S. Tiwary, and B. Catanzaro, ‘‘Using DeepSpeed and
megatron to train megatron-turing NLG 530B, a large-scale generative
language model,’’ 2022, arXiv:2201.11990.

[75] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,

#### T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez,

#### A. Joulin, E. Grave, and G. Lample, ‘‘LLaMA: Open and efficient
foundation language models,’’ 2023, arXiv:2302.13971.

[76] T. Thi Nguyen, C. Wilson, and J. Dalins, ‘‘Fine-tuning llama 2 large
language models for detecting online sexual predatory chats and abusive
texts,’’ 2023, arXiv:2308.14683.

[77] G. Penedo, Q. Malartic, D. Hesslow, R. Cojocaru, A. Cappelli, H. Alobei-
dli, B. Pannier, E. Almazrouei, and J. Launay, ‘‘The RefinedWeb dataset
for falcon LLM: Outperforming curated corpora with web data, and web
data only,’’ 2023, arXiv:2306.01116.

[78] J. Hoffmann et al., ‘‘Training compute-optimal large language models,’’

2022, arXiv:2203.15556.

[79] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan,

#### M. Diab, X. Li, X. Victoria Lin, T. Mihaylov, M. Ott, S. Shleifer,

#### K. Shuster, D. Simig, P. Singh Koura, A. Sridhar, T. Wang, and

#### L. Zettlemoyer, ‘‘OPT: Open pre-trained transformer language models,’’
2022, arXiv:2205.01068.

[80] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le,
and D. Zhou, ‘‘Chain-of-thought prompting elicits reasoning in large
language models,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022,
pp. 24824–24837.
[81] W. Zeng et al.,

‘‘PanGu-α: Large-scale autoregressive pretrained
Chinese language models with auto-parallel computation,’’ 2021,
arXiv:2104.12369.

[82] H. Naveed, A. U. Khan, S. Qiu, M. Saqib, S. Anwar, M. Usman,

#### N. Akhtar, N. Barnes, and A. Mian, ‘‘A comprehensive overview of large
language models,’’ 2023, arXiv:2307.06435.

[83] G. Jawahar, B. Sagot, and D. Seddah, ‘‘What does BERT learn about the
structure of language?’’ in Proc. 57th Annu. Meeting Assoc. Comput. Lin-
guistics, 2019, pp. 3651–3657.

[84] J. Ni, G. Hernández Ábrego, N. Constant, J. Ma, K. B. Hall, D. Cer, and

#### Y. Yang, ‘‘Sentence-t5: Scalable sentence encoders from pre-trained text-
to-text models,’’ 2021, arXiv:2108.08877.

[85] Y. Li et al., ‘‘Competition-level code generation with AlphaCode,’’

Science, vol. 378, no. 6624, pp. 1092–1097, Dec. 2022.

[86] Y. Koizumi, Y. Ohishi, D. Niizumi, D. Takeuchi, and M. Yasuda, ‘‘Audio
captioning using pre-trained large-scale language model guided by audio-
based similar caption retrieval,’’ 2020, arXiv:2012.07331.

[87] W. Fan, Z. Zhao, J. Li, Y. Liu, X. Mei, Y. Wang, Z. Wen, F. Wang, X. Zhao,

#### J. Tang, and Q. Li, ‘‘Recommender systems in the era of large language
models (LLMs),’’ 2023, arXiv:2307.02046.

[88] Y. Bai, J. Yi, J. Tao, Z. Tian, Z. Wen, and S. Zhang, ‘‘Fast end-to-
end speech recognition via non-autoregressive models and cross-modal
knowledge transferring from BERT,’’ IEEE/ACM Trans. Audio, Speech,
Language Process., vol. 29, pp. 1897–1911, 2021.

[89] C. Sun, J. Li, Y. R. Fung, H. P. Chan, T. Abdelzaher, C. Zhai, and

#### H. Ji, ‘‘Decoding the silent majority: Inducing belief augmented social
graph with large language model for response forecasting,’’ 2023,
arXiv:2310.13297.

[90] K. Drossos, S. Gharib, P. Magron, and T. Virtanen, ‘‘Language modelling
for sound event detection with teacher forcing and scheduled sampling,’’
2019, arXiv:1907.08506.

[91] S.-H. Chiu and B. Chen, ‘‘Innovative bert-based reranking language
models for speech recognition,’’ in Proc. IEEE Spoken Lang. Tech-
nol. Workshop (SLT), Jan. 2021, pp. 266–271.

[92] A. Elhafsi, R. Sinha, C. Agia, E. Schmerling, I. A. D. Nesnas, and

#### M. Pavone, ‘‘Semantic anomaly detection with large language models,’’
Auto. Robots, vol. 47, no. 8, pp. 1035–1055, Dec. 2023.

[93] Y. Shen, J. Shao, X. Zhang, Z. Lin, H. Pan, D. Li, J. Zhang, and

#### K. B. Letaief, ‘‘Large language models empowered autonomous edge AI
for connected intelligence,’’ 2023, arXiv:2307.02779.

[94] H. Abdel-Jaber, D. Devassy, A. A. Salam, L. Hidaytallah, and

#### M. El-Amir, ‘‘A review of deep learning algorithms and their applications
in healthcare,’’ Algorithms, vol. 15, no. 2, p. 71, Feb. 2022.

[95] B. Peng, C. Li, P. He, M. Galley, and J. Gao, ‘‘Instruction tuning with

GPT-4,’’ 2023, arXiv:2304.03277.

[96] J. Vig and Y. Belinkov, ‘‘Analyzing the structure of attention in a

transformer language model,’’ 2019, arXiv:1906.04284.

[97] A. McGowan, Y. Gui, M. Dobbs, S. Shuster, M. Cotter, A. Selloni,

#### M. Goodman, A. Srivastava, G. A. Cecchi, and C. M. Corcoran,
‘‘ChatGPT and bard exhibit spontaneous citation fabrication during
psychiatry literature search,’’ Psychiatry Res., vol. 326, Aug. 2023,
Art. no. 115334.

[98] R. Taylor, M. Kardas, G. Cucurull, T. Scialom, A. Hartshorn, E. Saravia,

#### A. Poulton, V. Kerkez, and R. Stojnic, ‘‘Galactica: A large language
model for science,’’ 2022, arXiv:2211.09085.

[99] N.

Shazeer,
arXiv:2002.05202.

‘‘GLU variants

improve

transformer,’’

2020,

[100] N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun,

#### Y. Zhou, A. W. Yu, and O. Firat, ‘‘GLaM: Efficient scaling of language
models with mixture-of-experts,’’ in Proc. Int. Conf. Mach. Learn., 2022,
pp. 5547–5569.

[101] S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Golding,

#### H. He, C. Leahy, K. McDonell, J. Phang, M. Pieler, U. Sai Prashanth,

#### S. Purohit, L. Reynolds, J. Tow, B. Wang, and S. Weinbach,
‘‘GPT-NeoX-20B: An open-source autoregressive language model,’’
2022, arXiv:2204.06745.

[102] E. Nijkamp, B. Pang, H. Hayashi, L. Tu, H. Wang, Y. Zhou, S. Savarese,
and C. Xiong, ‘‘CodeGen: An open large language model for code with
multi-turn program synthesis,’’ 2022, arXiv:2203.13474.

[103] T. Hagendorff, S. Fabi, and M. Kosinski, ‘‘Thinking fast and slow in large

language models,’’ 2022, arXiv:2212.05206.

[104] P. P. Ray, ‘‘ChatGPT: A comprehensive review on background, applica-
tions, key challenges, bias, ethics, limitations and future scope,’’ Internet
Things Cyber-Phys. Syst., vol. 3, pp. 121–154, Jan. 2023.

VOLUME 12, 2024

26871

[105] X.-Q. Dao, ‘‘Performance comparison of large language models on
VNHSGE English dataset: OpenAI chatGPT, Microsoft bing chat, and
Google bard,’’ 2023, arXiv:2307.02288.

[106] D. Kelly, Y. Chen, S. E. Cornwell, N. S. Delellis, A. Mayhew,

#### S. Onaolapo, and V. L. Rubin, ‘‘Bing chat: The future of search engines?’’
Proc. Assoc. Inf. Sci. Technol., vol. 60, no. 1, pp. 1007–1009, Oct. 2023.
[107] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, and

#### Q. V. Le, ‘‘XLNet: Generalized autoregressive pretraining for language
understanding,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019.

[108] X. Song, G. Wang, Z. Wu, Y. Huang, D. Su, D. Yu, and H. Meng,
‘‘Speech-XLNet: Unsupervised acoustic model pretraining for self-
attention networks,’’ 2019, arXiv:1910.10387.

[109] W. Shen, J. Chen, X. Quan, and Z. Xie, ‘‘DialogXL: All-in-one
XLNet for multi-party conversation emotion recognition,’’ in Proc. AAAI
Conf. Artif. Intell., vol. 35, no. 15, 2021, pp. 13789–13797.

[110] R. Luo, L. Sun, Y. Xia, T. Qin, S. Zhang, H. Poon, and T.-Y. Liu,
‘‘BioGPT: Generative pre-trained transformer for biomedical text gen-
eration and mining,’’ Briefings Bioinf., vol. 23, no. 6, Nov. 2022,
Art. no. bbac409.

[111] D. Deutsch, J. Juraska, M. Finkelstein, and M. Freitag, ‘‘Training and
meta-evaluating machine translation evaluation metrics at the paragraph
level,’’ 2023, arXiv:2308.13506.

[112] A. Ushio, F. Alva-Manchego, and J. Camacho-Collados, ‘‘Genera-
tive language models for paragraph-level question generation,’’ 2022,
arXiv:2210.03992.

[113] (2023). OpenAI. Accessed: Sep. 12, 2023.

[Online]. Available:

https://openai.com/blog/openai-api

[114] (2023). Huggingface. Accessed: Sep. 12, 2023. [Online]. Available:

https://huggingface.co/docs/transformers/index

[115] (2023). Google Cloud. Accessed: Sep. 12, 2023. [Online]. Available:

https://cloud.google.com/natural-language
[116] (2023). Azure. Accessed: Sep. 12, 2023.

[Online]. Available:

https://azure.microsoft.com/en-us/products/ai-services/ai-language
[117] IBM. (2023). IBM Watson Natural Language Understanding. Accessed:
https://www.ibm.com/

[Online]. Available:

12,

Sep.
products/natural-language-understanding

2023.

[118] G. Satyanarayana, J. Bhuvana, and M. Balamurugan, ‘‘Sentimental
analysis on voice using AWS comprehend,’’ in Proc. Int. Conf. Com-
put. Commun. Informat. (ICCCI), Jan. 2020, pp. 1–4.

[119] A. Kolides, A. Nawaz, A. Rathor, D. Beeman, M. Hashmi, S. Fatima,

#### D. Berdik, M. Al-Ayyoub, and Y. Jararweh, ‘‘Artificial intelligence foun-
dation and pre-trained models: Fundamentals, applications, opportunities,
and social impacts,’’ Simul. Model. Pract. Theory, vol. 126, Jul. 2023,
Art. no. 102754.

[120] S. M. Jain, ‘‘Hugging face,’’ in Introduction to Transformers for
NLP: With Hugging Face Library Models to Solve Problems. Cham,
Switzerland: Springer, 2022, pp. 51–67.

[121] J. Wang, X. Hu, W. Hou, H. Chen, R. Zheng, Y. Wang, L. Yang, H. Huang,

#### W. Ye, X. Geng, B. Jiao, Y. Zhang, and X. Xie, ‘‘On the robustness
of ChatGPT: An adversarial and out-of-distribution perspective,’’ 2023,
arXiv:2302.12095.

[122] S. Chen, Y. Li, S. Lu, H. Van, H. J. Aerts, G. K. Savova, and

#### D. S. Bitterman, ‘‘Evaluation of ChatGPT family of models for
biomedical reasoning and classification,’’ 2023, arXiv:2304.02496.
[123] H. Huang, O. Zheng, D. Wang, J. Yin, Z. Wang, S. Ding, H. Yin,

#### C. Xu, R. Yang, Q. Zheng, and B. Shi, ‘‘ChatGPT for shaping the
future of dentistry: The potential of multi-modal large language model,’’
Int. J. Oral Sci., vol. 15, no. 1, p. 29, Jul. 2023.

[124] V. Sorin, E. Klang, M. Sklair-Levy, I. Cohen, D. B. Zippel, N. Balint
Lahat, E. Konen, and Y. Barash, ‘‘Large language model (ChatGPT) as a
support tool for breast tumor board,’’ NPJ Breast Cancer, vol. 9, no. 1,
p. 44, May 2023.

[125] A. J. Thirunavukarasu, D. S. J. Ting, K. Elangovan, L. Gutierrez, T. F. Tan,
and D. S. W. Ting, ‘‘Large language models in medicine,’’ Nature Med.,
vol. 29, no. 8, pp. 1930–1940, 2023.

[126] D. M. Korngiebel and S. D. Mooney, ‘‘Considering the possibil-
ities and pitfalls of generative pre-trained transformer 3 (GPT-3)
in healthcare delivery,’’ npj Digit. Med., vol. 4, no. 1, p. 93,
Jun. 2021.

[127] L. De Angelis, F. Baglivo, G. Arzilli, G. P. Privitera, P. Ferragina,

#### A. E. Tozzi, and C. Rizzo, ‘‘ChatGPT and the rise of large language
models: The new AI-driven infodemic threat in public health,’’ Frontiers
Public Health, vol. 11, Apr. 2023, Art. no. 1166120.


#### M. A. K. Raiaan et al.: Review on Large Language Models

[128] M. Sallam, ‘‘ChatGPT utility in healthcare education, research, and
practice: Systematic review on the promising perspectives and valid
concerns,’’ Healthcare, vol. 11, no. 6, p. 887, Mar. 2023.

[129] M. Cascella, J. Montomoli, V. Bellini, and E. Bignami, ‘‘Evaluating the
feasibility of ChatGPT in healthcare: An analysis of multiple clinical and
research scenarios,’’ J. Med. Syst., vol. 47, no. 1, p. 33, Mar. 2023.
[130] T. H. Kung, M. Cheatham, A. Medenilla, C. Sillos, L. De Leon,

#### C. Elepaño, M. Madriaga, R. Aggabao, G. Diaz-Candido, J. Maningo,
and V. Tseng, ‘‘Performance of ChatGPT on USMLE: Potential for
AI-assisted medical education using large language models,’’ PLOS
Digit. Health, vol. 2, no. 2, Feb. 2023, Art. no. e0000198.

[131] Y. Gu, R. Tinn, H. Cheng, M. Lucas, N. Usuyama, X. Liu, T. Naumann,

#### J. Gao, and H. Poon, ‘‘Domain-specific language model pretraining
language processing,’’ ACM Trans. Comput.
for biomedical natural
Healthcare, vol. 3, no. 1, pp. 1–23, Oct. 2021.

[132] Z. Kraljevic, D. Bean, A. Shek, R. Bendayan, H. Hemingway, and J. Au,
‘‘Foresight-generative pretrained transformer (GPT) for modelling of
patient timelines using EHRs,’’ 2022, arXiv:2212.08072.

[133] L. Mich and R. Garigliano, ‘‘ChatGPT for e-tourism: A technological
perspective,’’ Inf. Technol. Tourism, vol. 25, no. 1, pp. 1–12, Mar. 2023.
[134] X. Yu, Z. Chen, Y. Ling, S. Dong, Z. Liu, and Y. Lu, ‘‘Temporal
data meets LLM—Explainable financial time series forecasting,’’ 2023,
arXiv:2306.11025.

[135] G. F. Frederico, ‘‘ChatGPT in supply chains: Initial evidence of
applications and potential research agenda,’’ Logistics, vol. 7, no. 2, p. 26,
Apr. 2023.

[136] A. Sobieszek and T. Price, ‘‘Playing games with ais: The limits of
GPT-3 and similar large language models,’’ Minds Mach., vol. 32, no. 2,
pp. 341–364, Jun. 2022.

[137] M. U. Hadi, R. Qureshi, A. Shah, M. Irfan, A. Zafar, M. B. Shaikh,

#### N. Akhtar, J. Wu, and S. Mirjalili, ‘‘Large language models: A
comprehensive survey of its applications, challenges, limitations, and
future prospects,’’ Tech. Rep., 2023.

[138] C. K. Lo, ‘‘What is the impact of ChatGPT on education? A rapid review

of the literature,’’ Educ. Sci., vol. 13, no. 4, p. 410, Apr. 2023.

[139] Y. K. Dwivedi, N. Kshetri, L. Hughes, E. L. Slade, A. Jeyaraj,

#### A. K. Kar, A. M. Baabdullah, A. Koohang, V. Raghavan, and M. Ahuja,
‘‘‘So what
if chatgpt wrote it?’ multidisciplinary perspectives on
opportunities, challenges and implications of generative conversational ai
for research, practice and policy,’’ Int. J. Inf. Manage., vol. 71, Jul. 2023,
Art. no. 102642.

[140] M. Zong and B. Krishnamachari,

‘‘A survey on GPT-3,’’ 2022,

arXiv:2212.00857.

[141] R. Zhu, X. Tu, and J. X. Huang, ‘‘Utilizing BERT for biomedical and
clinical text mining,’’ in Data Analytics in Biomedical Engineering and
Healthcare. Amsterdam, The Netherlands: Elsevier, 2021, pp. 73–103.
[142] K. Huang, A. Singh, S. Chen, E. T. Moseley, C.-Y. Deng, N. George,
and C. Lindvall, ‘‘Clinical XLNet: Modeling sequential clinical notes and
predicting prolonged mechanical ventilation,’’ 2019, arXiv:1912.11975.
[143] J. Zhang, L. Wang, R. K. W. Lee, Y. Bin, Y. Wang, J. Shao, and E. P. Lim,
‘‘Graph-to-tree learning for solving math word problems,’’ in Proc. 58th
Annu. Meeting Assoc. Comput. Linguistics, 2020, pp. 3928–3937.
[144] X. Dai, S. Karimi, B. Hachey, and C. Paris, ‘‘Cost-effective selection of
pretraining data: A case study of pretraining BERT on social media,’’
2020, arXiv:2010.01150.

[145] S. Biswas, ‘‘The function of chat GPT in social media: Accord-
ing to chat GPT,’’ Mar. 2023. [Online]. Available: http://dx.doi.org/
10.2139/ssrn.4405389

[146] R. Peng, K. Liu, P. Yang, Z. Yuan, and S. Li, ‘‘Embedding-based
retrieval with LLM for effective agriculture information extracting from
unstructured data,’’ 2023, arXiv:2308.03107.

[147] S. Biswas,

‘‘Importance of chat GPT in agriculture: According
[Online]. Available: http://dx.doi.org/

to chat GPT,’’ Mar. 2023.
10.2139/ssrn.4405391

[148] M. A. K. Raiaan, N. M. Fahad, S. Chowdhury, D. Sutradhar, S. S. Mihad,
and M. M. Islam, ‘‘IoT-based object-detection system to safeguard
endangered animals and bolster agricultural farm security,’’ Future
Internet, vol. 15, no. 12, p. 372, Nov. 2023.

[149] T. Pires, E. Schlinger, and D. Garrette, ‘‘How multilingual is multilingual

BERT?’’ 2019, arXiv:1906.01502.

[150] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek,

#### F. Guzmán, E. Grave, M. Ott, L. Zettlemoyer, and V. Stoyanov,
‘‘Unsupervised cross-lingual representation learning at scale,’’ 2019,
arXiv:1911.02116.

26872

VOLUME 12, 2024


#### M. A. K. Raiaan et al.: Review on Large Language Models

[151] V. Sanh, L. Debut, J. Chaumond, and T. Wolf,

‘‘DistilBERT, a
distilled version of BERT: Smaller, faster, cheaper and lighter,’’ 2019,
arXiv:1910.01108.

[152] Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut,
‘‘ALBERT: A lite BERT for self-supervised learning of language
representations,’’ 2019, arXiv:1909.11942.

[153] T. Bolukbasi, K.-W. Chang, J. Y. Zou, V. Saligrama, and A. T. Kalai,
‘‘Man is to computer programmer as woman is to homemaker? Debiasing
word embeddings,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 29,
2016.

[154] Y. Zhang, S. Sun, M. Galley, Y.-C. Chen, C. Brockett, X. Gao, J. Gao,

#### J. Liu, and B. Dolan, ‘‘DialoGPT: Large-scale generative pre-training for
conversational response generation,’’ 2019, arXiv:1911.00536.

[155] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal,

#### A. Neelakantan, P. Shyam, G. Sastry, and A. Askell, ‘‘Language models
are few-shot learners,’’ in Proc. NIPS, 2020, pp. 1877–1901.

[156] J. Lee, W. Yoon, S. Kim, D. Kim, S. Kim, C. H. So, and J. Kang,
‘‘BioBERT: A pre-trained biomedical language representation model for
biomedical text mining,’’ Bioinformatics, vol. 36, no. 4, pp. 1234–1240,
Feb. 2020.

[157] Y. Gat, N. Calderon, A. Feder, A. Chapanin, A. Sharma, and R. Reichart,
‘‘Faithful explanations of black-box NLP models using LLM-generated
counterfactuals,’’ 2023, arXiv:2310.00603.

[158] M. Josifoski, M. Sakota, M. Peyrard, and R. West,

‘‘Exploiting
asymmetry for synthetic training data generation: SynthIE and the case
of information extraction,’’ 2023, arXiv:2303.04132.

[159] M. S. H. Mukta, J. Ahmad, M. A. K. Raiaan, S. Islam, S. Azam,

#### M. E. Ali, and M. Jonkman, ‘‘An investigation of the effectiveness of
deepfake models and tools,’’ J. Sensor Actuator Netw., vol. 12, no. 4,
p. 61, Aug. 2023.

[160] A. Awasthi, N. Gupta, B. Samanta, S. Dave, S. Sarawagi, and P. Talukdar,
‘‘Bootstrapping multilingual semantic parsers using large language
models,’’ 2022, arXiv:2210.07313.

[161] P. Sridhar, A. Doyle, A. Agarwal, C. Bogart, J. Savelka, and M. Sakr,
‘‘Harnessing LLMs in curricular design: Using GPT-4 to support
authoring of learning objectives,’’ 2023, arXiv:2306.17459.

[162] M. A. K. Raiaan, A. Al Mamun, Md. A. Islam, M. E. Ali, and
Md. S. H. Mukta,
‘‘Envy prediction from Users’ photos using
convolutional neural networks,’’ in Proc. Int. Conf. Comput., Electr. Com-
mun. Eng. (ICCECE), Jan. 2023, pp. 1–7.

[163] E. Waisberg, J. Ong, M. Masalkhi, and A. G. Lee, ‘‘Large language model
(LLM)-driven chatbots for neuro-ophthalmic medical education,’’ Eye,
vol. 2023, pp. 1–3, Sep. 2023.

[164] W. Channell, ‘‘Making a difference: The role of the LLM in policy
formulation and reform,’’ in The Export of Legal Education. Evanston,
IL, USA: Routledge, 2016, pp. 13–21.

[165] P. Budhwar et al., ‘‘Human resource management in the age of generative
artificial intelligence: Perspectives and research directions on ChatGPT,’’
Hum. Resource Manage. J., vol. 33, no. 3, pp. 606–659, Jul. 2023.
[166] G. Fatouros, J. Soldatos, K. Kouroumali, G. Makridis, and D. Kyriazis,
‘‘Transforming sentiment analysis in the financial domain with Chat-
GPT,’’ Mach. Learn. Appl., vol. 14, Dec. 2023, Art. no. 100508.
[167] Y. Li, S. Ma, X. Wang, S. Huang, C. Jiang, H.-T. Zheng, P. Xie, F. Huang,
and Y. Jiang, ‘‘EcomGPT: Instruction-tuning large language models with
chain-of-task tasks for e-commerce,’’ 2023, arXiv:2308.06966.
[168] P. Weingart, T. Wambsganss, and M. Soellner, ‘‘A taxonomy for deriving
business insights from user-generated content,’’ ECIS, Res. Papers 401,
2023. [Online]. Available: https://aisel.aisnet.org/ecis2023_rp/401
[169] L. Zhu, X. Xu, Q. Lu, G. Governatori, and J. Whittle, ‘‘AI and
ethics—Operationalizing responsible AI,’’ in Humanity Driven AI: Pro-
ductivity, Well-being, Sustainability and Partnership. Cham, Switzerland:
Springer, 2022, pp. 15–33.

[170] I. Molenaar, S. D. Mooij, R. Azevedo, M. Bannert, S. Järvelä,
and D. Gašević, ‘‘Measuring self-regulated learning and the role of
AI: Five years of research using multimodal multichannel data,’’
Comput. Hum. Behav., vol. 139, Feb. 2023, Art. no. 107540.

[171] M. C. Rillig, M. Ågerstrand, M. Bi, K. A. Gould, and U. Sauerland,
‘‘Risks and benefits of large language models for the environment,’’
Environ. Sci. Technol., vol. 57, no. 9, pp. 3464–3466, Mar. 2023.
[172] B. Liu, B. Xiao, X. Jiang, S. Cen, X. He, and W. Dou, ‘‘Adversarial
attacks on large language model-based system and mitigating strategies:
A case study on ChatGPT,’’ Secur. Commun. Netw., vol. 2023, pp. 1–10,
Jun. 2023.

[173] Z. Sun, ‘‘A short survey of viewing large language models in legal

aspect,’’ 2023, arXiv:2303.09136.

[174] Y. Meng, M. Michalski, J. Huang, Y. Zhang, T. Abdelzaher, and J. Han,
‘‘Tuning language models as training data generators for augmentation-
enhanced few-shot learning,’’ in Proc. Int. Conf. Mach. Learn., 2023,
pp. 24457–24477.

[175] S. Fincke, S. Agarwal, S. Miller, and E. Boschee,

‘‘Language
model priming for cross-lingual event extraction,’’ in Proc. AAAI
Conf. Artif. Intell., 2022, vol. 36, no. 10, pp. 10627–10635.

[176] N. M. Fahad, S. Sakib, M. A. Khan Raiaan, and Md. S. Hossain
Mukta, ‘‘SkinNet-8: An efficient CNN architecture for classifying
skin cancer on an imbalanced dataset,’’ in Proc. Int. Conf. Electr.,
Comput. Commun. Eng. (ECCE), Feb. 2023, pp. 1–6.

[177] N. Jain, K. Saifullah, Y. Wen, J. Kirchenbauer, M. Shu, A. Saha,

#### M. Goldblum, J. Geiping, and T. Goldstein,
‘‘Bring your own
data! Self-supervised evaluation for large language models,’’ 2023,
arXiv:2306.13651.

[178] X. Zhu, J. Li, Y. Liu, C. Ma, and W. Wang, ‘‘A survey on model
compression for large language models,’’ 2023, arXiv:2308.07633.
[179] L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant,

#### A. Barua, and C. Raffel, ‘‘MT5: A massively multilingual pre-trained
text-to-text transformer,’’ 2020, arXiv:2010.11934.

[180] N. Ratner, Y. Levine, Y. Belinkov, O. Ram, I. Magar, O. Abend,

#### E. Karpas, A. Shashua, K. Leyton-Brown, and Y. Shoham, ‘‘Parallel
context windows for large language models,’’ 2022, arXiv:2212.10947.

[181] F. Motoki, V. Pinho Neto, and V. Rodrigues, ‘‘More human than human:
Measuring ChatGPT political bias,’’ Public Choice, vol. 2023, pp. 1–21,
Aug. 2023.

[182] K. Werder, B. Ramesh, and R. Zhang, ‘‘Establishing data provenance
intelligence systems,’’ ACM Trans. Man-

for responsible artificial
age. Inf. Syst., vol. 13, no. 2, pp. 1–23, Jun. 2022.

[183] J. Jiang, X. Liu, and C. Fan, ‘‘Low-parameter federated learning with

large language models,’’ 2023, arXiv:2307.13896.

[184] W. S. Saba, ‘‘Towards explainable and language-agnostic LLMs: Sym-
bolic reverse engineering of language at scale,’’ 2023, arXiv:2306.00017.
[185] Z. Zhang, A. Zhang, M. Li, H. Zhao, G. Karypis, and A. Smola,
‘‘Multimodal chain-of-thought reasoning in language models,’’ 2023,
arXiv:2302.00923.

[186] Z. Liu, Y. Zhang, P. Li, Y. Liu, and D. Yang, ‘‘Dynamic LLM-agent
team
network: An LLM-agent collaboration framework with agent
optimization,’’ 2023, arXiv:2310.02170.

[187] U. Iqbal, T. Kohno, and F. Roesner, ‘‘LLM platform security: Applying a
systematic evaluation framework to OpenAI’s ChatGPT plugins,’’ 2023,
arXiv:2309.10254.

MOHAIMENUL AZAM KHAN RAIAAN
received the Bachelor of Science degree in
computer science and engineering from United
International University (UIU), in 2023. Currently,
he is a Research Assistant with the Computer
Science and Engineering Department, UIU.
His professional pursuits are marked by active
involvement in diverse research areas, such as
computer vision, health informatics, explainable
intelligence, and graph optimization.
artificial
Notably, he has made significant contributions to the field, as evidenced by
his multiple research articles published in prestigious journals indexed by
Scopus and categorized under the Q1 ranking.

MD. SADDAM HOSSAIN MUKTA received
the Ph.D. degree from the Data Science and
Engineering Research Laboratory (Data Labo-
ratory), BUET,
in 2018. He is a Postdoctoral
Researcher with the LUT School of Engineering
Sciences, Lappeenranta, Finland. He was an
Associate Professor and a Undergraduate Program
Coordinator with the Department of Computer
Science and Engineering, United International
University, Bangladesh. He has a number of
quality publications in both national and international conferences and
journals. His research interests include deep learning, machine learning, data
mining, and social computing.

VOLUME 12, 2024

26873

KANIZ FATEMA received the bachelor’s degree
in computer science and engineering from Daf-
fodil International University, Dhaka, Bangladesh.
She is currently a Research Assistant
(RA)
with Charles Darwin University. She is actively
involved in research activities, especially in health
informatics, computer vision, machine learning,
deep learning, and artificial
intelligence-based
systems. She has published several research papers
in journals (Scopus) and international conferences.

NUR MOHAMMAD FAHAD received the bach-
elor’s degree from the Department of Computer
Science and Engineering, United International
University (UIU), Bangladesh. During the bach-
elor’s study, he has contributed to the academic
community as an Undergraduate Teaching Assis-
tant with the Department of Computer Science
and Engineering, UIU. In addition to his teaching
role, he has deeply engaged in cutting-edge
research across several domains, including com-
puter vision, machine learning, deep learning, health informatics, graph
theory, and mental health modeling.

SADMAN SAKIB received the bachelor’s degree
in computer science and engineering from the
Department of Computer Science and Engineer-
ing, United International University, Bangladesh,
in 2023. He was a Teaching Assistant of
undergraduate students with the Department of
Computer Science and Engineering, United Inter-
national University. Besides this, he is actively
involved in machine learning, deep learning,
artificial intelligence, computer vision, and health
informatics research.

MOST MARUFATUL JANNAT MIM is currently
pursuing the degree with the Computer Science
and Engineering Department, United International
University (UIU). She is actively involved in
research activities related to computer vision,
deep learning, graph theory, and human–computer
interaction. Her passion lies in pioneering inno-
vative research in computer science. Apart from
studies, she is involved in co-curricular activities
with the UIU APP Forum, where she is also the
President and demonstrates strong leadership by organizing various seminars
and workshops for computer science students.


#### M. A. K. Raiaan et al.: Review on Large Language Models

JUBAER AHMAD received the B.Sc. degree
in computer
science and engineering from
United International University (UIU), Dhaka,
Bangladesh, in 2022. He is currently a Research
Assistant with the IAR Project, UIU. His research
interests include computer vision, NLP, big data,
and distributed learning.

MOHAMMED EUNUS ALI is a Professor with
the Department of CSE, Bangladesh University
of Engineering and Technology (BUET), where
he is also the Group Leader of the Data Science
and Engineering Research Laboratory (DataLab).
His research papers have published in top ranking
journals and conferences, such as the VLDB
Journal, IEEE TRANSACTIONS ON KNOWLEDGE AND
DATA ENGINEERING, DMKD, Information Systems
Journal, WWWJ, DKE, ICDE, CIKM, EDBT,
PVLDB, and UbiComp. His research interests include database systems
and information management, including spatial databases, practical machine
learning, and social media analytics. He served as a Program Committee
Member for many prestigious conferences, including SIGMOD, VLDB,
AAAI, and SIGSPATIAL.

SAMI AZAM is a leading Researcher and a
Professor with the Faculty of Science and Technol-
ogy, Charles Darwin University, Australia. He is
actively involved in the research fields relating
to computer vision, signal processing, artificial
intelligence, and biomedical engineering. He has a
number of publications in peer-reviewed journals
and international conference proceedings.

26874

VOLUME 12, 2024


---

> *End of P-01*

<br><br>

<a id="p02-----automated-domain-modeling-with-large-language-models-a-comparative-study"></a>

## P-02 — Automated Domain Modeling with Large Language Models: A Comparative Study

| Field | Details |
|-------|---------|
| **Paper ID** | `P-02` |
| **Title** | Automated Domain Modeling with Large Language Models: A Comparative Study |
| **Authors** | Kua Chen, Yujing Yang, Boqi Chen, José Antonio Hernández López, Gunter Mussbacher, and Dániel Varró |
| **Affiliation(s)** | School of Computer Science, McGill University, Montréal, QC, Canada |
| **Venue** | ACM/IEEE 26th International Conference on Model Driven Engineering Languages and Systems (MODELS) |
| **Volume / Year** | 2023 |
| **DOI** | [10.1109/MODELS58315.2023.00037](https://doi.org/10.1109/MODELS58315.2023.00037) |

---

Automated Domain Modeling with
Large Language Models: A Comparative Study

Kua Chen*
Electrical and Computer Engineering
McGill University
Montreal, Canada

Yujing Yang*
Electrical and Computer Engineering
McGill University
Montreal, Canada

Boqi Chen*
Electrical and Computer Engineering
McGill University
Montreal, Canada

Jos´e Antonio Hern´andez L´opez*
DIS
University of Murcia
Murcia, Spain

Gunter Mussbacher
Electrical and Computer Engineering
McGill University
Montreal, Canada

D´aniel Varr´o
Link¨oping University
McGill University
Link¨oping, Sweden / Montreal, Canada


### Abstract

Domain modeling is an essential part of software
engineering and serves as a way to represent and understand
the concepts and relationships in a problem domain. Typically,
software engineers interpret the problem description written in
natural language and manually translate it into a domain model.
Domain modeling can be time-consuming and highly depends on
the expertise of software engineers. Recently, Large Language
Models (LLMs) have exhibited remarkable ability in language
understanding, generation, and reasoning. In this paper, we
conduct a comprehensive, comparative study of using LLMs for
fully automated domain modeling. We assess two powerful LLMs,
GPT3.5 and GPT4, employing various prompt engineering tech-
niques on a data set containing ten diverse domain modeling
examples with reference solutions created by modeling experts.
Our findings reveal that while LLMs demonstrate impressive
domain understanding capabilities, they are still impractical for
full automation, with the top-performing LLM achieving F1
scores of 0.76 for class generation, 0.61 for attribute generation,
and 0.34 for relationship generation. Moreover, the F1 score is
characterized by higher precision and lower recall; thus, domain
elements retrieved by LLMs are often reliable, but there are
many missing elements. Furthermore, modeling best practices
are rarely followed in auto-generated domain models. Our data
set and evaluation provide a valuable baseline for future research
in automated LLM-based domain modeling.


### Index Terms / Keywords

domain modeling, large language models, few-
shot learning, chain-of-thought prompting, prompt engineering


### I. Introduction
Context: Domain modeling is a core process in software
engineering that builds a domain model from various sources
of information, including documents, stakeholder interactions,
etc. This process is typically performed manually by software
engineers, which can be time-consuming and highly depen-
dent on human expertise. To mitigate this intensive manual

* All four authors contributed equally to this research.
Partially supported by grant TED2021-129381B-C22 (SATORI project)
funded by MCIN/AEI/10.13039/501100011033, a FPU grant funded by the
Universidad de Murcia,
the FRQNT-B2X project (file number: 319955),
IT30340 Mitacs Accelerate, and the Wallenberg AI, Autonomous Systems
and Software Program (WASP), Sweden

effort, many approaches aim to automate this process [1]–[4].
However, these approaches have one or two main limitations:
(1) some level of human interaction is required during gen-
eration, or (2) domain elements are extracted at the sentence
level without considering the interaction between sentences.
As such, no existing approaches can perform fully automated
domain modeling while considering textual specifications as a
whole without breaking them into sentences.

Problem statement: In this paper, we aim to address the
problem of fully automated domain modeling. Given a textual
description in its entirety, our aim is to derive a complete
domain model without any human interaction.

Existing automated domain modeling approaches rely on
rule-based techniques for the generation, while the machine
learning models used are rather simple. One reason behind
this is the lack of properly labeled training examples.

Recently, with rapid advances in auto-regressive language
modeling, large language models (LLMs) have shown power-
ful generalizability to tasks beyond natural language process-
ing [5]. LLMs can perform different tasks without supervised
training on the specific task using carefully designed input
(called prompt). Using different prompt engineering [6] tech-
niques, LLMs can achieve impressive performance on different
tasks by only using a few labeled examples in the prompt. Such
advances raise the natural question of whether these LLMs can
be used to fully automate domain modeling.

A domain model can be expressed by graphical or tex-
tual modeling languages such as UML [7], Umple [8], and
Ecore [9]. These languages have strict syntax rules for repre-
senting various modeling elements. However, because LLMs
are trained on a large corpus of text, it is difficult to con-
strain them to adhere to such strict syntax, particularly when
modeling examples may infrequently appear in the training set.
Therefore, an appropriate input prompt is necessary to instruct
LLMs to generate outputs in the desired format.

Another challenge in automated domain modeling is the
lack of proper evaluation methods. The same domain concept
may be represented differently by different solutions. While

979-8-3503-2480-8/23/$31.00 ©2023 IEEE
DOI 10.1109/MODELS58315.2023.00037

162

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.


some existing approaches can compare two domain models
automatically [4], [10]–[13], they either only provide an im-
precise estimation or only work under restricted situations.

Objectives: Our paper aims to evaluate to what extent
domain modeling can be fully automated using an LLM
without supervised training. In particular, we evaluate how
the expressiveness of LLMs and different prompt engineering
techniques can affect the quality of generated domain models.
Furthermore, we aim to identify the advantages and limitations
of current LLMs for fully automated domain modeling.

Contribution: Given a textual domain description, we
present a novel approach1 for fully automated domain model-
ing using different LLMs and prompt engineering techniques.
The specific contributions of this paper are the following:

- We formulate the automated domain modeling problem as
a text generation problem and propose a fully automated
domain modeling pipeline that relies on an LLM.

- We provide a new data set for evaluating automated do-
main modeling including ten diverse modeling examples
with reference solutions created by modeling experts.
- Our framework provides the domain model in a textual
format suitable for various prompt engineering methods.
- We provide a semantic scoring technique and a detailed
comparative evaluation of different configurations to as-
sess the quality of auto-generated domain models.

- We conduct experiments with two LLMs, GPT3.5 [14]
and GPT4 [15] with various prompt engineering methods
on the newly created data set to evaluate the generated
models with quantitative and qualitative criteria.

Added value: To our best knowledge, our paper is the
first to use LLMs for fully automatically generating domain
models from problem descriptions without supervised training.
Furthermore, we carry out comparative experiments involving
three different groups of prompt engineering techniques and
assess the generated domain models, demonstrating the current
advantages and limitations of LLMs in automated domain
modeling. Our paper provides insightful guidelines for adapt-
ing LLMs in the modeling process. We also identify common
fault patterns in the models generated by LLMs and provide
suggestions for future improvements.


### II. Background


#### A. Domain modeling

In domain modeling, engineers typically convert a textual
domain specification into a domain model represented as a
class diagram [7]. Domain modeling is a challenging and
time-consuming task that requires expertise and experience.
A domain model uses a subset of class diagram concepts to
capture essential elements of a domain, their attributes, and
their relationships but does not cover elements related to a
more detailed design (e.g., operations and interfaces).

Example 1: Figure 1 (left) shows the H2S domain model,
a delivery and pickup system, along with an excerpt of its
problem description. This example covers the key concepts of

1Artifact DOI: 10.5281/zenodo.8118642

domain models such as classes and enumerations (e.g., Person
and ItemCategory, respectively), attributes (e.g., name), and
three types of relationships among classes: a basic relationship
called association (e.g., between Resident and Item), a whole-
part relationship called composition (e.g., between Volunteer
and Date), and an is-a relationship called generalization (e.g.,
between Item and FoodItem). Classes may be abstract (i.e.,
they cannot be instantiated). Multiplicities are specified for
associations/compositions and indicate how many instances of
one class may be related to instances of the other class (e.g.,
0..1, 0..*). Role names may be specified for the classes in
an association/composition (e.g., pickUpRoute). Compositions
may also be specified by placing classes inside a composite
class (e.g., H2S). In that case, multiplicities are shown next to
the name of the contained class (e.g., Person*). Association
classes and n-ary associations are excluded since they are not
always supported (e.g., Ecore [9] does not support them).


#### B. Large language models (LLMs)

Language modeling is a traditional task in natural language
processing that aims to estimate the conditional probability of
a sequence of tokens. Recently, large language models (LLMs)
have gained significant attention for this task. LLMs use deep
neural networks, typically with transformer architecture [16],
to estimate this probability distribution.

Given a sequence of

tokens s = {s1, s2, ..., sk−1},
LLMs estimate the conditional probability of the next token
P (sk|s1, ..., sk−1). These models are typically used for text
generation through auto-regression. Specifically, in each time
step, the LLM predicts a new token that is added to the input.
As the scale of LLMs (i.e., the number of parameters)
increases, some models can be fine-tuned to perform other
specific tasks beyond text generation [17].


#### C. Fine-tuning and prompting

a) Prompt-based learning: Fine-tuning of an LLM in-
volves updating some of the parameters to fit a given task and
a given data set [18]. This fine-tuning approach enhances the
generalization ability of the trained models [18] but has two
major drawbacks: (1) the training process can be computa-
tionally expensive, and (2) some tasks may not have sufficient
training data for fine-tuning. Recently, LLMs have been used
as few-shot
learners [6], where the training examples are
used as input rather than parameter updates. As an alternative
to fine-tuning, prompt-based learning methods [19] involve
constructing examples used as input to LLMs.

Given an input and a set of examples, a typical prompt-
based learning method consists of three steps [19]: (1) trans-
form the input and the examples into task context using
a template that contains unfilled slots (a process known as
prompt engineering), (2) fill the slots with an LLM to generate
an output text, and (3) extract the final output from the output
text using a post-processor. In this approach, the parameters
of an LLM are fixed. Depending on the prompt engineering
strategy, either a small number of labeled examples are needed,
or no labeled examples are required.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

163

Fig. 1: Example domain model (left) and its textual representation (bottom right) with the problem description (top right)

m; the problem of domain model generation is to define a
generator f with m′ = f(d), where m′
is the generated
domain model. Ideally, the generated model should be similar
to the ground truth domain model, i.e., m′ ∼= m. In this paper,
domain modeling is handled as a text generation problem.
Specifically, the function f is LLM-based and the output of f
is a textual description of m′.

b) Architecture: Figure 2 depicts the overall architecture
of using an LLM for domain modeling. To generate a domain
model, we provide a task description, a modeling problem
description (domain specification), a format description (i.e.,
the expected output format for the domain model), examples
of domain modeling descriptions with reference models, and
the reasoning steps involved in the example as the task context
to the LLM. In the prompt engineering stage, we employ three
techniques: zero-shot, N-shot, and chain-of-thought (CoT).

Next, each prompt is fed into an LLM. We cover two
different LLMs: GPT-3.5 and GPT-4. The LLM accepts text
prompts as input and generates a text-based description of the
domain model based on the provided format description. Next,
a post-processor extracts classes, attributes, and relationships
from the output of the LLM. The post-processor uses rule-
based methods to parse and extract relevant results from the
LLM’s response to create the final domain model which is
evaluated using the procedure described in Section IV.


#### B. Domain model representation

Instead of depicting a domain model using a graphical view
or a specific modeling language, we present the domain model
in structured natural language to avoid any biases caused by
errors in modeling languages and to focus on the modeling
capabilities of LLMs.

Figure 3 presents our domain model representation in Ex-
tended Backus-Naur Form (EBNF) format. The specification
defines enumeration and two types of classes, regular and
abstract, with the latter indicated by the keyword abstract.

Fig. 2: Overview of automated domain modeling with LLMs

b) Prompt engineering: While many prompt engineering
approaches exist for LLMs [19], here we focus on three widely
used techniques. The zero-shot technique operates with no
labeled examples, and task context is constructed using the
task input, along with the textual
instruction of the task.
For example, in text classification, the task context can be
“classify the following text input into categories: c1, c2...”
along with the text to be classified. The N-shot technique
adds N labeled examples to the task context in addition to
the task description and input. However, using exclusively
the input/output pair in the examples may not be sufficient
for the LLM to learn a complex task involving multiple
steps to solve. The chain-of-thought (CoT) technique [20]
mitigates this issue by including a list of reasoning steps in
the examples provided to the LLM. This technique allows the
LLM to generate reasoning along with the task output and
also improves the performance of LLMs on many benchmarks
compared with N-shot techniques [20].


### III. Approach


#### A. Overview

a) Problem formulation: Given a textual description in
natural language, the domain modeling task consists of gen-
erating a domain model. More formally, let d be a domain
specification with underlying ground truth domain model

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

164

Textual Domain Description: The Helping Hand Store (H2S) collects second hand articles and non-perishable foods from residents of the city and distributes them to those in need. H2S operates in many cities,but each location is run independently. To increase the number of items available for distribution, H2S isseeking to offer a Pickup and Delivery Service to its customers, which would allow a resident to schedule apickup of items from a street address online at the H2S website. A resident enters a name, street address, phone number, optional email address, as well as a description ofthe items to be picked up. H2S has a fleet of pickup vehicles, which it uses to collect items from residents. Apickup route for that day is determined for each vehicle for which a volunteer driver is available. Volunteerdrivers indicate their available days on the H2S website. The route takes into account the available storagespace of a vehicle and the dimensions and weights of scheduled items. A scheduled pickup may occuranytime between 8:00 and 14:00. After completing all scheduled pickups, the driver drops off all collectedsecond hand articles at H2S’s distribution center. Non-perishable foods, on the other hand, are directlydropped off at the food bank, which then deals with these items without further involvement from H2S ...H2SPerson*string namestring addressstring phoneNumberstring emailAddress<<abstract>>UserRole*10..*VolunteerResidentRoute*Date date<<abstract>>Item*string descriptionstring dimensionint weightDate requestedPickUpDateSecondHandArticlestring codeRFIDboolean discardedItemCategory categoryFoodItemDate<<enumeration>>ItemCategoryBaby ClothingFridge...0..*0..*dropOffs0..1 dropOffRoute0..1 pickUpRoute10..*0..*pickUps10..*0..*Vehicle*string dimensionint weightRestriction1ClientItemCategory[] neededCategory0..10..*Enumerations:ItemCategory(Baby_Clothing, Fridge, ...)Classes:H2S()Person(string name, string address, string phoneNumber, stringemailAddress)abstract UserRole()Client(ItemCategory[] neededCategory)Volunteer()Resident()Date()FoodItem()SecondHandArticle(string codeRFID, booleandiscarded,ItemCategory category)Vehicle(string dimension, int weightRestriction)abstract item(string description, string dimension, int weight, DaterequestedPickUpDate)Route(Date date)Relationships:1 H2S contain * Item1 H2S contain * Vehicle1 H2S contain * Route1 H2S contain * UserRole1 H2S contain * Person1 Volunteer contain * DateClient inherit UserRoleVolunteer inherit UserRoleResident inherit UserRoleSecondHandArticle inherit ItemFoodItem inherit Item1 Person associate * UserRole0..1 Client associate * SecondHandArticle1 Volunteer associate * Route1 Vehicle associate * Route0..1 Route associate * Item0..1 Route associate * SecondHandArticle1 Resident associate * ItemReferenceSolutionN shot 0 shotCoTPromptEngineeringLLMsGPT-3.5GPT-4EvaluationPrecisionRecallF1 ModelingProblemDescriptionFormatDescriptionPost-processor ClassRelationDomainModelReasoningStepsAttributeExample StoreDomainModelTaskDescriptionin the defined format. The example consists of two parts: a
problem description of an example domain and a reference
domain model in textual representation for the example. One
sample prompt for N-shot learning to generate a domain model
for LabTracker, with the transportation system BTMS as an
example, is shown as the second example in Figure 4.

Chain-of-thought: In this setting, the prompt consists of
a task description, chain-of-thought reasoning steps, and a
modeling problem description. In previous N-shot settings, the
problem description and solution were provided separately,
without a clear indication of how the solution was derived
from the description. To address this issue, we use chain-of-
thought [20] prompting, which involves presenting a coherent
series of intermediate steps leading to the solution. Instead of
providing the description and solution separately, we integrate
them by appending relevant modeling elements in the solution
to each sentence, providing reasoning steps at the sentence
level. This approach offers a more comprehensive illustration
of how each element is derived from the text.

The last example in Figure 4 demonstrates a prompt that
uses CoT to generate a domain model for LabTracker, with
pairs of problem description sentences / relevant solutions for
H2S.

Fig. 3: EBNF format of a domain model

Enumeration literals are specified in brackets for each enumer-
ation, while attributes (if any) can be multi-valued indicated
by square brackets. Keywords identify three relationship types
between two classes: associate for an association relationship,
inherit for a generalization relationship, and contain for a com-
position relationship. Multiplicity is required and positioned
before each class name for association and composition. We
ignore the role names for associations and compositions in the
representation for simplicity. Figure 1 (bottom right) shows the
H2S example following the EBNF format.


#### C. Prompt engineering


#### D. Post-processing

In the next step, we take a problem description as input
and design a prompt to describe the domain model generation
task with three settings in the prompt design: zero-shot, N-
shot, and chain-of-thought. Figure 4 illustrates an example for
each prompting method.

Zero-shot learning: In the context of zero-shot learning,
the LLM is not provided with any examples, and instead,
it receives only natural language instructions describing the
task. To facilitate this, we design a prompt
that consists
of a task description, a format description, and a target
problem description for generating a domain model. The task
description serves the purpose of defining the objective of the
task for the LLM, which is to generate classes, attributes, and
relationships of a domain model in natural language format,
based on the given problem description.

The first example in Figure 4 shows a prompt based on zero-
shot learning for the LabTracker problem description, a med-
ical examination system. The format description specifies the
desired output format using textual description of the EBNF
format in Figure 3. The modeling problem description provides
information about the target modeling domain, including the
target system and its components and relationships.

N-shot learning: In the case of N-shot learning, N examples
are provided to the LLM as input-output pairs to learn both the
format and content of the desired output. To facilitate this, we
design a prompt that includes a task description, N examples of
the problem description and solution, and a modeling problem
description for the model to generate.

The task description and problem description are the same
as in the zero-shot learning setup. However, in N-shot learning,
instead of a format description, we provide a detailed example

The post-processor takes the natural language output of
LLMs and converts it into a domain model format using a
rule-based method. The output of LLMs generally follows the
structured natural language format defined before, except for
certain parts especially in zero-shot setups. In cases where
the generated text does not conform to the specified format,
the post-processor adapts the output to the desired format. In
particular, some of the generated relationships may have an
association name instead of the three relationship keywords,
and we treat all such relationships as associations. Addition-
ally, some of the generated attributes may not have a data type,
and they are set to a default type of string.


### IV. Domain Modeling Evaluation


#### A. Evaluation procedure

This paper focuses on an ideal domain modeling scenario
where the problem description is well-constructed and clear.
We gather ten problem descriptions written in English (Ta-
ble I) from an undergraduate-level, model-driven programming
course. The examples are taken from projects or exams in the
course and have been used across multiple course offerings,
covering a wide range of domains. Each example has a
domain model developed by modeling experts as a reference
solution, which is originally used to grade student models
in the course. Given a problem description, we evaluate the
quality of the generated domain models by comparing them
with the reference solution (model).

Domain model evaluation is a difficult task as there are
multiple acceptable solution models for the same problem de-
scription. Moreover, the automated comparison of two domain
models is also non-trivial. For example, there are many ways to

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

165

<class-diagram> ::= [<enumerations>] <classes> <relationships><enumerations> ::= "Enumerations: " (<enumeration>)+<enumeration> ::= <string> "(" <literals> ")"<literals> ::= <string> | <string> ", " <literals><classes> ::= "Classes: " (<class>)+<class> ::= ["abstract"] <string>"(" [<attributes>] ")"<attributes> ::= <attribute> | <attribute> ", " <attributes><attribute> ::= <type>["[]"] <string><relationships> ::= "Relationships: " [<composition>]* [<inheritance>]* [<association>]*<composition> ::= <mul> <string> "contain" <mul> <string><inheritance> ::= <string> "inherit" <string><association> ::= <mul> <string> "associate" <mul> <string><type> ::= <string><mul> ::= "*" | <num> | <num>".."("*"|<num>)Fig. 4: Example prompts for three prompting methods

name a class or an attribute where the semantics is the same.
While there are approaches to compare two domain models
automatically [4], [10]–[13], they either provide an imprecise
estimation or work under carefully selected situations.

Due to the limitation of automated evaluators, we choose to
manually evaluate the generated domain models to precisely
measure the modeling ability of LLMs. To ensure consistency
and fairness in evaluation, we conduct the manual evaluation
using a consensus approach and the process is summarized in
Figure 5. Two authors first evaluate the same two generated
models separately, then both authors compare their results,
resolve differences and come to a mutual agreement on an
evaluation scheme. Afterwards,
the first
evaluation round. For consistency, they each independently
evaluate half of all examples in all settings. After Round 1,
a calibration phase is performed where all authors review
the grading and suggest improvements for a second round
of evaluation. Finally, the same two authors start the second
evaluation round.

two authors start

We calculate Cohen’s d-score [21] between the first and
second evaluation results and get an effect size of 0.10 (small
effect), which suggests the two rounds of evaluation only have
minor differences. We use the results from the second round
of evaluation as the final result.


#### B. Evaluation scheme

The first step in evaluating each modeling element (i.e.,
class, attribute, and relationship) is to determine whether it
has a direct counterpart in the reference model. To compare
a domain model with a reference domain model, we use
an evaluation scheme. Motivated by existing work [10], we
categorize each modeling element into one of four categories
as shown in Table II
c1 Category c1 includes all domain elements that have an
exact match with the elements of the same type in the

Fig. 5: Flowchart of the evaluation process

reference model. It is important to note that this match
is based on semantics rather than string comparison.
c2 Elements in category c2 are matched with an element that
may not be the same type in the reference model but are
semantically equivalent to the matched element.

c3 Category c3 is for elements that only partially match
the element in the reference model. This category also
includes elements without a match in the reference model
due to another incorrect design decision (i.e., consequen-
tial mistakes) that are otherwise correct.

c4 Category c4 captures incorrect elements that do not match

any elements in the reference model.

We categorize all elements in both the generated and reference
model to compute precision and recall of the generated model.
Example 2: The last column of Table II shows examples
of each category for the H2S domain, separated by a colon.
Left of the colon presents the element from the reference
model, and the right is the element to be evaluated. To ensure
conciseness, we omit attributes of certain classes.

the Person class of the reference model

For c1, the elements are exactly the same or semantically
equivalent
to the reference model. For example, both the
reference model and generated model contain the H2S class.
Additionally,
is
matched with the User class, as both capture the same domain
concept. Elements in c2 are still equivalent, but may not be of
the same type. For example, the SecondHandArticle class has
a boolean attribute discarded in the reference solution, while
the generated model includes an enumeration Status with two
literals and adds an enumeration attribute to the class.

Category c3 encompasses elements that only partially match
the reference model. In the H2S domain model, for example,
there is a relationship stating that 0 or 1 Route is associated
with 0 or many Items. There are two possible cases for the
association to fall into this category: (1) Route is marked as
non-optional, leading to a partial match of the relationship with
the reference model; (2) the generated model may not have an
abstract superclass corresponding to Item; thus Route is asso-
ciated with FoodItem instead. In the latter case, although the
association does not match, it is correct given the superclass
mistake in the generated model, and we consider it as c3.

Elements in category c4 are without a match. In the H2S
example, the abstract UserRole class in the reference model
has no equivalent modeling element in the generated model.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

166

Generate a class diagram... Create a class diagram for the following description bygiving the enumerations, classes, and relationships usingthe following format:Description: The LabTracker software helps (i)doctors... 0-shotGenerate a class diagram... Description: A city is using the Bus TransportationManagement System...N-shotGenerate a class diagram... H2S has a fleet of pickup vehicles, which it uses to collectitems from residents.Chain-of-thought -> Vehicle(), 1 H2S contain * VehicleRepeat for every sentence of all N examplesEnumeration: Shift(morning, afternoon, night) ...Classes: BTMS() ...Relationships:1 BTMS contain * BusVehicle ...Repeat for N examplesDescription: The LabTracker software helps (i)doctors... Description: The LabTracker software helps (i)doctors... Relationships: mul1 Class1 associate mul2 Class2Class1 inherit Class2mul1 Class1 contain mul2 Class2Enumerations: EnumerationName(literals)Classes: ClassName(type attribute)A resident enters a name, street address, phone number,optional email address, as well as a description of the itemsto be picked up.-> Person(string name, string address, stringphoneNumber, string emailAddress), abstract item(stringdescription), 1 H2S contain * PersonEvaluation of 2samplesseparatelyComparisonandDiscussionEvaluationScheme 1EvaluationResult 1Review Samples ofEvaluation ResultEvaluationResult 2EvaluationScheme 2Evaluation round 1Evaluation round 2Name
Domain
# of classes
# of attributes
# of relationships

BTMS
Transportation
7
11
9

H2S
Delivery
13
18
18

LabTracker
Medical
16
43
22

CelO
Social
13
23
22

TeamSports
Sports
16
24
20

SHAS
Smart Home
23
26
27

OTS
Education
16
25
19

Block
Game
15
30
24

Tile-O
Game Management

HBMS

18
19
21

18
32
22

TABLE I: Collected modeling examples and their domains

Category
c1

Description
Direct match

c2

c3

c4

Semantically
equivalent

Partial match

No match

Examples
H2S():H2S(), Person(...):User(...)
SecondHandArticle(boolean discarded,...):
SecondHandArticle(Status status,...),
Status(AVAILABLE, DISCARDED)
0..1 Route associate * Item:
(1) 1 Route associate * Item
(2) 0..1 Route associate * FoodItem
abstract UserRole():(No role class)

TABLE II: Scheme for comparing two domain models

To evaluate the modeling elements (classes, attributes, and
relationships), we use a modified version of the precision,
recall, and F1 score metrics. Unlike binary scoring, we assign
0.5 points to generated elements that partially match the refer-
ence solution. Specifically, elements in the first two categories
are awarded 1 point, while elements in c3 receive 0.5 points,
and those in c4 receive 0 points. The scoring function S for
an element x can be expressed formally as follows:

S(x) =

if x is in c1 or c2


1

0.5 if x is in c3

if x is in c4
0

(1)


#### C. Evaluation criteria

We aim to evaluate the quality of the output domain model.
To do so, we consider the precision, recall, and F1 scores over
the classes, relationships, and attributes. Precision measures
the overall correctness of generated modeling elements. For
example, let C be the set of all classes and enumerations in
the generated model of size m = |C|, the precision of classes
in generated models can be expressed as

P recisionC =

(cid:80)i=m

i=0 S(Ci)
m

,

(2)

where S is the scoring function defined in Equation 1.

Recall measures the degree of the reference model covered
by the generated model. For example, let Cgt be the set of
classes and enumerations in the reference model (ground truth)
of size n = |Cgt|, the recall of classes can be expressed as

RecallC =

(cid:80)i=n

i=0 S(Ci)
n

.

Finally, we use the classical F1 score definition:

F1C =

2 × P recisionC × RecallC
P recisionC + RecallC

.

(3)

(4)

Metrics for attributes or relationships can be computed by

substituting C with the set of attributes or relationships.


### V. Experiments

The aim of this section is to assess the capability of LLMs
in domain modeling, identify areas of the domain modeling
task where these models may encounter challenges, provide
insights on the most effective prompt engineering approach
for generating domain models using such LLMs, and compare
several LLMs. More concretely, we aim to investigate the
following three research questions (RQ):

1: How do LLMs perform in automated domain modeling?
2: What is the effect of using different prompts?
3: Which one of the assessed LLMs performs best?
We begin by describing the experimental settings in Sec-
tion V-A. Subsequently, we tackle each one of the three
research questions and report findings in Sections V-B,V-C,
and V-D. Finally, we provide an in-depth analysis and discus-
sion of the results including qualitative results in Section V-E
and state threats to validity in Section V-F.


#### A. Experimental settings

Large language models. We experiment with two GPT-3.5
models (Davinci and Turbo) and one GPT4 model (GPT4).
- Davinci is the text-davinci-003 model from OpenAI
GPT3.5 API [22]. It performs text completion tasks by
receiving input text and producing output text.

- Turbo is the gpt-3.5-turbo via the OpenAI chat comple-
tion API. It uses a similar model architecture as Davinci
but it is optimized for chat completion. We adapt our
prompts to become chat-like for this model.

- GPT4 is the GPT-4 model recently released by OpenAI.
We use the web interface for accessing GPT4 via the
ChatGPT website [23] because the GPT4 API is not yet
publicly available to all developers.

Prompt settings. We experiment with one 0-shot, three N-
shot (1-shot-btms, 1-shot-h2s, and 2-shot), and one
chain-of-thought (CoT) prompt setting as described in Sec-
tion III-C. We select one simple domain (BTMS) and a
complex domain that contains many best practices (H2S) as
the two examples. 1-shot-btms uses a prompt with the
BTMS and its reference domain model, while 1-shot-h2s
uses the H2S. Furthermore, 2-shot combines the BTMS and
H2S and CoT uses H2S as the example.
Test set. To evaluate each LLM and each prompt setting, we
use the descriptions and the associated ground truth domain
models of examples in Table I. We remove the domain models
of BTMS and H2S from the test set as they are introduced in
the input prompts; thus, we consider a test set of eight samples.
Each example represents a software system, and the domain
models require the use of some advanced modeling patterns

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

167

TABLE III: Average performance scores for each setting and modelling element of Davinci

0-shot
1-shot-btms
1-shot-h2s
2-shot
CoT

Precision
0.89 ± 0.10
0.96 ± 0.06
0.95 ± 0.06
0.91 ± 0.06
0.89 ± 0.11

Class

Recall
0.39 ± 0.06
0.48 ± 0.09
0.46 ± 0.07
0.50 ± 0.06
0.47 ± 0.06

F1
0.54 ± 0.07
0.63 ± 0.08
0.62 ± 0.07
0.64 ± 0.05
0.61 ± 0.07

Precision
0.57 ± 0.20
0.73 ± 0.15
0.65 ± 0.15
0.67 ± 0.16
0.55 ± 0.16

Attribute

Recall
0.37 ± 0.14
0.31 ± 0.14
0.31 ± 0.15
0.38 ± 0.13
0.33 ± 0.14

F1
0.44 ± 0.16
0.42 ± 0.15
0.41 ± 0.18
0.48 ± 0.14
0.39 ± 0.14

Precision
0.28 ± 0.19
0.55 ± 0.16
0.51 ± 0.14
0.54 ± 0.17
0.35 ± 0.22

Relationship
Recall
0.10 ± 0.06
0.24 ± 0.10
0.18 ± 0.09
0.22 ± 0.08
0.12 ± 0.08

F1
0.14 ± 0.09
0.33 ± 0.12
0.26 ± 0.12
0.31 ± 0.11
0.17 ± 0.11

TABLE IV: Average performance scores for each setting and modelling element of Turbo

0-shot
1-shot-btms
1-shot-h2s
2-shot
CoT

Precision
0.87 ± 0.09
0.95 ± 0.05
0.85 ± 0.09
0.87 ± 0.05
0.88 ± 0.13

Class

Recall
0.41 ± 0.11
0.51 ± 0.13
0.56 ± 0.09
0.56 ± 0.09
0.44 ± 0.07

F1
0.55 ± 0.11
0.66 ± 0.12
0.67 ± 0.08
0.68 ± 0.08
0.58 ± 0.08

Precision
0.52 ± 0.22
0.64 ± 0.19
0.54 ± 0.15
0.56 ± 0.16
0.67 ± 0.23

Attribute

Recall
0.38 ± 0.20
0.33 ± 0.18
0.37 ± 0.14
0.41 ± 0.14
0.38 ± 0.21

F1
0.43 ± 0.20
0.42 ± 0.17
0.43 ± 0.14
0.46 ± 0.11
0.46 ± 0.19

Precision
0.26 ± 0.11
0.36 ± 0.23
0.35 ± 0.14
0.39 ± 0.14
0.33 ± 0.23

Relationship
Recall
0.10 ± 0.04
0.19 ± 0.11
0.20 ± 0.05
0.23 ± 0.08
0.12 ± 0.08

F1
0.14 ± 0.06
0.24 ± 0.14
0.24 ± 0.07
0.29 ± 0.10
0.17 ± 0.11

TABLE V: Average performance scores for each setting and modelling element of GPT4

0-shot
1-shot-btms
1-shot-h2s
2-shot
CoT

Precision
0.89 ± 0.05
0.93 ± 0.05
0.83 ± 0.09
0.94 ± 0.06
0.87 ± 0.09

Class

Recall
0.54 ± 0.05
0.64 ± 0.07
0.60 ± 0.05
0.63 ± 0.09
0.55 ± 0.06

F1
0.67 ± 0.04
0.76 ± 0.06
0.70 ± 0.05
0.75 ± 0.05
0.67 ± 0.06

Precision
0.64 ± 0.21
0.72 ± 0.13
0.66 ± 0.19
0.70 ± 0.18
0.64 ± 0.13

Attribute

Recall
0.53 ± 0.13
0.54 ± 0.20
0.54 ± 0.18
0.56 ± 0.14
0.45 ± 0.19

F1
0.57 ± 0.14
0.58 ± 0.16
0.58 ± 0.18
0.61 ± 0.13
0.50 ± 0.13

Precision
0.44 ± 0.11
0.50 ± 0.14
0.51 ± 0.21
0.45 ± 0.20
0.42 ± 0.13

Relationship
Recall
0.18 ± 0.03
0.26 ± 0.07
0.25 ± 0.11
0.27 ± 0.11
0.21 ± 0.06

F1
0.25 ± 0.05
0.34 ± 0.08
0.33 ± 0.14
0.34 ± 0.14
0.27 ± 0.08

(e.g., abstraction-occurrence, player-role), but the actual pat-
terns covered in various examples are different.
Statistical tests. When comparing two groups of samples
through a statistical test, the Wilcoxon signed-rank test [24]
is used as several variables of the data set do not follow a
normal distribution based on the Shapiro-Wilk normality test.
The significance level is set to 0.05.


#### B. RQ1: Performance of LLMs in domain modeling

RQ1 aims to evaluate how LLMs perform in domain models
generation. We are interested in how far the LLMs are from a
perfect performance score for this task. This will show if there
is room for improvement and whether the automated domain
model generation problem is solved with LLMs. Furthermore,
we carry out a more fine-grained analysis by highlighting
with which modeling aspects the LLMs struggle. Particularly,
we compare the performances of the LLMs when recovering
classes, attributes, and relationships; and we study for which
evaluation metrics (precision or recall) the LLMs struggle.
Results. Tables III, IV, and V show the average precision,
recall, and F1 scores for each LLM, setting, and type of
modeling element. It can be observed that the best average
F1 scores are obtained by GPT4 and they are the following:
the best F1 score is 0.76,

- Class modeling element:

achieved by 1-shot-btms.

- Attribute modeling element: the best F1 score is 0.61,

achieved by 2-shot.

- Relationship modeling element: the best F1 score is 0.34,

achieved by 1-shot-btms.

From these results, we can also infer that LLMs generate
classes from descriptions better than attributes and they gen-
erate attributes better than relationships. Using the Wilcoxon
signed-rank test, we compare the F1 scores and see if these
differences are significant. After applying the pairwise tests

TABLE VI: Patterns found when applying pairwise tests of
types of modeling elements for each LLM and setting (the
symbol > means ”statistically better than” and ≈ means that
no statistical difference is found)

Pattern
Class > Attribute > Relationship
Class ≈ Attribute > Relationship
Class > Attribute ≈ Relationship

Number of occurrences
8
5
2

TABLE VII: Positive tests when comparing the precision and
the recall scores

Type of modeling element
Class
Attribute
Relationship

Positive tests / Total tests
15/15
9/15
15/15

for each LLM and setting, we report the number of patterns
in Table VI. The pattern that mostly occurs is Class > Attribute
> Relationship (8 out of 15). Furthermore, there are important
differences between the F1 scores of each pair of modeling
elements. Particularly, the LLMs struggle when generating
relationships. Comparing the average relationship F1 score
with the other two modeling elements in Tables III, IV, and V,
one can notice the poor performance of LLMs in extracting
relationships. To better illustrate this, we show the boxplots of
the F1 scores for each type of modeling element in Figure 6
associated with GPT4 using the setting 1-shot-btms.

Finally, we study for which metric, precision or recall,
the LLMs struggle more. From the figures presented in Ta-
bles III, IV, and V, it seems clear that LLMs obtain a higher
precision score. We carry out a statistical test to compare
the precision and recall for each LLM, setting, and type of
modeling element and show the positive tests in Table VII
listed by type of modeling element. We can observe that all

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

168

TABLE VIII: Davinci comparisons for each prompting
method and for each type of model element (cell format:
p−value/mean difference; bold means significant)

Setting
1-shot-btms
1-shot-h2s
2-shot

Class
0.0391 / 0.0929
0.0078 / 0.0789
0.0225 / 0.1051

Attribute
0.4609 / -0.0244
0.0781 / -0.0367
0.4609 / 0.0353

Relationship
0.0156 / 0.1862
0.0078 / 0.1206
0.0078 / 0.1739

TABLE IX: Turbo comparisons
each prompting
method and for each type of model element (cell format:
p−value/mean difference; bold means significant)

for

Setting
1-shot-btms
1-shot-h2s
2-shot

Class
0.0781 / 0.1097
0.0547 / 0.1250
0.0547 / 0.1345

Attribute
0.3828 / -0.0112
0.8438 / -0.0009
0.5469 / 0.0250

Relationship
0.0781 / 0.1066
0.0234 / 0.1087
0.0078 / 0.1520

particularly, in Davinci and Turbo. Regarding attributes,
no significant improvement is observed in any of the LLMs.
We also study if there are differences between the 2-shot
setting and the 1-shot settings. For each LLM and type
of modeling element, we find no significant differences when
comparing 2-shot with both 1-shot settings.
Effect of reasoning steps. To address this aspect, we compare
the average F1 scores of the 1-shot-h2s and its CoT
version for each type of modeling element and LLM.
Results. Table XI shows the mean differences of the F1 scores
(µCoT − µ1-shot-h2s) for each LLM and type of modeling
element. We can observe a performance decrease for almost all
combinations. There is only one case where the performance
difference is positive but it is not statistically significant.

Answer to RQ2. Adding examples to the prompt has
positive effects on the performance of LLMs when re-
trieving classes and relations. However, we do not have
enough evidence to claim that adding two samples to
the prompt is better than adding one. Finally, adding
reasoning steps may decrease the performance.


#### D. RQ3: The best of the assessed LLMs

RQ3 aims to find out the best LLM of the ones we have
accessed. We compare the three LLMs across all settings

TABLE X: GPT4 comparisons for each prompting method and
for each type of model element (cell format: p−value/mean
difference; bold means significant)

Setting
1-shot-btms
1-shot-h2s
2-shot

Class
0.0234 / 0.0864
0.3828 / 0.0264
0.0781 / 0.0765

Attribute
0.7422 / 0.0168
0.6406 / 0.0190
0.3125 / 0.0416

Relationship
0.0547 / 0.0849
0.2500 / 0.0780
0.1484 / 0.0841

TABLE XI: Mean F1 differences (µCoT−µ1-shot-h2s) for each
LLM and type of modeling element

Type of modeling element
Class
Attribute
Relationship

Davinci
-0.0032
-0.0144
-0.0890

Turbo
-0.0865
0.0275
-0.0695

GPT4
-0.0289
-0.0827
-0.0558

Fig. 6: F1 score, precision, and recall boxplots associated with
GPT4 using the setting 1-shot-btms (x−axis represents
the type of modeling elements and y−axis the scores)

of the tests are positive in case of classes and relationships, and
the majority of tests are positive in case of attributes. We also
highlight that the recall of the LLMs is, in general, much lower
than the precision (see Tables III, IV, and V). Thus, the recall
is the one that negatively impacts the overall performance (i.e.,
the F1 score). For instance, it can be observed that the recall
score is much lower than the precision score for all modeling
elements in GPT4 with 1-shot-btms setting (Figure 6).

Answer to RQ1. While LLMs demonstrate impres-
sive domain understanding capability, they are still
impractical for fully automated domain modeling. The
top-performing LLM achieves F1 scores of 0.76 for
classes, 0.61 for attributes, and 0.34 for relationships.
Moreover, LLMs struggle the most with identifying
relationships (compared to classes and attributes). Al-
together, domain elements generated by LLMs are
often reliable but there are many missing elements.


#### C. RQ2: Effects of prompt engineering

The output of LLMs is influenced by the structure and con-
tent of the prompts. RQ2 investigates (1) if adding examples to
the prompt helps the LLMs to produce better domain models
and (2) if adding reasoning steps improves the performance
of LLMs in domain modeling.
Effect of examples. We first use the 0-shot setting as
the baseline prompting method and it is compared with the
two 1-shot settings (1-shot-btms and 1-shot-h2s) and
the 2-shot setting. Concretely, given an LLM, a type of
modeling element, and a few-shot prompting method, we run
the Wilcoxon test to compare the F1 score with respect to
the baseline. We also compare the 2-shot setting with the
1-shot-btms and 1-shot-h2s settings similarly to see
if adding more examples is better than adding one.
Results. Tables VIII IX, and X show the p−values and
the mean differences of the F1 scores (µ − µ0-shot) when
comparing each few-shot prompt setting with the 0-shot
setting for each LLM. We observe statistically significant
improvements when generating classes in Davinci and
GPT4. Significant improvements also exist in relationships,

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

169

ClassAttributeRelationshipType of modeling element0.250.500.751ScoreScore typef1precisionrecallTABLE XII: Each cell contains the model that achieves the
highest average F1 score (bold means that the comparison of
that model with the other two is significant)

Setting
0-shot
1-shot-btms
1-shot-h2s
2-shot
CoT

Class
GPT4
GPT4
GPT4
GPT4
GPT4

Attribute
GPT4
GPT4
GPT4
GPT4
GPT4

Relationship
GPT4
GPT4
GPT4
GPT4
GPT4

and modeling elements. We report which LLM obtains the
highest average F1 score for each type of modeling element
and prompt setting (a total of 15 comparisons).
Results. Table XII shows that GPT4 achieves the highest F1
score for all settings and types of modeling element. The
differences are statistically significant in only five cases and
three of them correspond to the 0-shot setting.

Answer to RQ3. GPT4 achieves the highest average
F1 score in all cases with the strongest evidence found
in the 0-shot setting, suggesting that GPT4’s mod-
eling ability is better compared to the other models.


#### E. Discussion

In this section, we discuss several aspects of our experi-

ments and possible implications.
RQ1. The experiments show that LLMs are still not able
to fully automate the domain modeling task. However, the
results obtained are promising and there is still room for
improvement. The fine-gradient analysis reveals that
these
generated domain models mainly fail to recover relationships
and miss a lot of modeling elements from the description
(low recall). Thus the focus of future work should be to
improve these two aspects. One potential future direction is to
make LLMs generate domain models multiple times for one
problem description and aggregate all the domain models in
a way that more modeling elements in the reference domain
model can be covered. At the same time, given LLMs can
often generate correct model elements, their behavior in an
interactive modeling setting can also be studied. In this case,
a human modeler can continuously provide feedback on the
generated model to continuously improve the generated model.
RQ2. By answering the second research question, we provide
insights on how to design prompts for domain modeling.
Adding examples to the prompt helps to generate classes
and relations but we do not find significant improvements
when comparing the 2-example setting and the 1-example
setting. One future direction could be to focus on devising
a method to select good examples for the prompt. There is
already existing work in the LLMs literature that deals with
this problem [25]–[27]. We found that the CoT prompting
technique may negatively impact performance. We believe the
negative impact is caused by the fact that domain modeling
tasks require full comprehension of the description and it is not
natural to see it as a sequence of independent reasoning steps.

Therefore, innovative prompting techniques designed for do-
main modeling are needed to further improve the performance.
RQ3. When comparing the performances of the LLMs, we
have found evidence that the GPT4 model performs the best
in the domain modeling task and this evidence is stronger in
the 0-shot setting. This is because GPT4 has better language
understanding skills (particularly, better comprehension skills)
than the other two models assessed in the experiments [15].
Modeling best practices. We also investigate the performance
of the LLMs qualitatively, i.e., to what an extent best modeling
practices are used. Since GPT4 is found to have the best
performance among the investigated LLMs, we analyze the 2-
shot setting results from GPT4. We find that models generated
by GPT4 tend to have a common anti-pattern that misidentifies
a domain concept as an enumeration rather than a class,
with nine cases found in all examples. However, we do not
observe any enumeration that is misidentified as a class. We
observe a similar scenario where relationships are treated as
attributes in the generated models, with 17 occurrences in eight
generated models. At the same time, there is only one case
where an attribute is treated as a relationship in the generated
models. Surprisingly, GPT4 does not generate any correct
abstract class. Meanwhile, common best-practice modeling
patterns, such as player-role and abstraction occurrence [28],
rarely appear in the generated models. No complete player-
role pattern or abstraction-occurrence pattern is found in any
generated models, and only one player-role pattern is partially
found. This result may indicate that LLMs struggle with
complex modeling that requires modeling knowledge beyond
the domain description. Thus, trying to inject such modeling
knowledge into these LLMs can be an interesting future work.


#### F. Threats to validity

Internal validity. The output of an LLM can be slightly
different for each run. We address this variation by experi-
menting on the generation of eight diverse domain examples.
The manual evaluation is done by two authors, which may
introduce bias. We mitigate this bias by having a consensus
process. We also have multiple rounds of evaluations where
other authors review the evaluation results. Meanwhile, the
selections of weights in the scoring function may influence
experiment results. We choose scoring methods widely used
to evaluate university-level assignments. There are typically
multiple ways to represent a domain model, which may
influence the performance of LLMs. To address this issue,
we define an independent (new) text-based domain model
representation that is based on natural language and use it
across all experiments.
External validity. Due to the lack of benchmark data sets for
domain modeling with both problem description and reference
solution, we curate a data set of ten modeling examples with
reference models created by domain modeling experts. We
skipped the p−value adjustment in the statistical test as the
number of modeling examples is relatively small (eight per
distinct group). Therefore, there is a higher risk of getting false
positives in the statistical tests. Furthermore, we collect models

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

170

from an undergraduate modeling course representing modeling
in education scenarios. LLMs may perform differently if used
in a different scenario or with larger models.
Construct validity. Our paper adapts metrics widely used for
evaluating the generated domain models [1]–[4].


### VI. Related Work


#### A. Automated domain modeling.

Many existing works on automated domain modeling utilize
statistical methods or rule-based methods to directly derive
complete domain modeling solutions like UML class diagrams
[1]–[4] or provide modeling assistance and suggestions [29],
[30] from textual descriptions in natural language.

Statistical methods emphasize using machine learning tech-
niques to extract domain models. Burgue˜no et al. [29] design a
framework to suggest new model elements for a given partially
completed model, by using word embeddings to capture the
lexical and semantic information from textual documents.
Several other existing approaches also combine NLP and ML
techniques to automate the model creation process [2], [4].

Rule-based methods include using hand-written grammat-
ical templates and heuristics. An example of a rule-based
method presents an algorithm with 23 heuristics to automat-
ically identify model elements from user stories [3]. Another
example of such rule-based methods is proposed by Herchi et
al. [31]. The authors begin by using an NLP toolkit including a
sentence splitter, tokenizer, and syntactic parser to decompose
the input text and then use linguistic rules (e.g., All nouns are
converted to entity types) to extract UML concepts.

Our paper proposes a statistical method for fully automated
domain modeling using LLMs. We investigate the use of pre-
trained generative LLMs, for domain modeling, with only a
limited number of labeled examples and no extra training.


#### B. Large language models for MDE.

With the advancement of LLMs, various language mod-
els have been incorporated within model-based engineering
(MDE), yielding significant improvements in various aspects
of the development process.

Weyssow et al. [30] propose a learning-based approach to
recommend relevant domain concepts to a modeler during a
meta-modeling activity by training a deep-learning model (a
RoBERTa model trained on thousands of independent meta-
models). Chaaben et al. [11] propose an approach for model
completion by generating related elements using GPT-3. They
formulate examples using classes and their relationships with
other classes and then create prompts with few-shot learning.
They also rank the generated classes by frequency in multiple
runs. Others discuss the potential of ChatGPT in software
engineering [32], [33]. For example, C´amara et al. [33] present
the use of ChatGPT to build UML class diagrams enriched
with OCL constraints in an interactive mode.

Compared with existing approaches adapting LLMs to
MDE, we investigate fully automated domain model genera-
tion tasks with pre-trained generative LLMs given problem de-
scriptions and including classes, attributes, and relationships.


#### C. Domain model evaluation.

Evaluating generated domain models can be challenging due
to the variety of model elements and intricate design patterns
involved. Many approaches have been investigated to assess
the resulting solution in comparison to the reference solution.
Yang and Sahraoui [4] combine learning-based and rule-based
approaches for the extraction of UML class diagrams from
natural language software specifications. In their evaluation,
they evaluate the result with reference solutions using exact
matching, relaxed matching, and general matching over classes
and relationships. Bien et al. [10] present an approach for
automated grading of UML class diagrams, which uses a
grading algorithm that uses syntactic, semantic, and structural
matching between two class diagrams. Boubekeur et al. [13]
propose an approach based on a simple heuristic and machine
learning that helps categorize simple domain model submis-
sions from students according to their quality. The system
determines if submissions are above a quality threshold to
assign them a letter grade. Singh et al. [12] introduce a Mistake
Detection System (MDS) designed to identify errors and offer
feedback to students by comparing their submissions with a
solution. This system is able to detect a wide range of potential
mistakes present in a submission.

In this paper, we use a carefully designed manual as-
sessment of the generated domain models. In comparison to
existing automated evaluation methods, this manual evaluation
takes into account partially correct results and separately cal-
culates scores for different types of domain elements, offering
a more comprehensive evaluation of the model’s performance.


### VII. Conclusion

This paper presents an approach for fully automated domain
modeling using Large Language Models (LLMs). Given a
domain description, the system directly generates a textual
representation of the domain model without any human inter-
action. We evaluate this approach using two powerful LLMs
(GPT-3.5 and GPT-4) along with various prompt engineering
techniques on a data set of ten domain examples with reference
solutions created by modeling experts. Our results demonstrate
that while the top-performing LLM, GPT-4, shows impres-
sive domain understanding capability without explicit train-
ing, fully automating domain modeling remains impractical.
Furthermore, LLM-generated domain elements exhibit high
precision but low recall. Specifically, LLMs struggle the most
with relationships. We also identify common fault patterns
in the models generated by LLMs and provide suggestions
for future improvements. Moreover, we note that advanced
modeling best practices are rarely applied in generated models.
This study highlights the potential of LLMs for fully
automated domain modeling and points to the challenges
that must be addressed for full automation. Future work
includes designing prompting methods designated for domain
modeling, proposing a framework for the automated selection
of examples used in prompting, and injecting explicit modeling
knowledge into LLMs.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

171

REFERENCES

[22] “GPT-3.5 models.” [Online]. Available: https://platform.openai.com/

docs/models/gpt-3-5

[23] “Introducing chatgpt.” [Online]. Available: https://openai.com/blog/

chatgpt

[24] F. Wilcoxon, Individual comparisons by ranking methods.

Springer,

1992.

[25] T. Shin, Y. Razeghi, R. L. L. IV, E. Wallace, and S. Singh, “Autoprompt:
Eliciting knowledge from language models with automatically generated
prompts,” in Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing, (EMNLP 2020).
Association for
Computational Linguistics, 2020, pp. 4222–4235.

[26] Y. Zhou, A. I. Muresanu, Z. Han, K. Paster, S. Pitis, H. Chan, and

#### J. Ba, “Large language models are human-level prompt engineers,” arXiv
preprint arXiv:2211.01910, 2022.

[27] S. Diao, P. Wang, Y. Lin, and T. Zhang, “Active prompting with chain-
of-thought for large language models,” arXiv preprint arXiv:2302.12246,
2023.

[28] T. Lethbridge and R. Lagani`ere, Object-Oriented Software Engineering:
Practical Software Development Using UML and Java. McGraw Hill,
2004.

[29] L. Burgue˜no, R. Claris´o, S. G´erard, S. Li, and J. Cabot, “An NLP-
based architecture for the autocompletion of partial domain models,” in
Advanced Information Systems Engineering: 33rd International Confer-
ence, CAiSE 2021, Melbourne, VIC, Australia, June 28–July 2, 2021,
Proceedings. Springer, 2021, pp. 91–106.

[30] M. Weyssow, H. Sahraoui, and E. Syriani, “Recommending metamodel
concepts during modeling activities with pre-trained language models,”
Software and Systems Modeling, vol. 21, no. 3, pp. 1071–1089, 2022.
[31] H. Herchi and W. B. Abdessalem, “From user requirements to UML

class diagram,” arXiv preprint arXiv:1211.0713, 2012.

[32] B. Combemale, J. Gray, and B. Rumpe, “Chatgpt in software modeling,”

Software and Systems Modeling, vol. 22, 05 2023.

[33] J. C´amara, J. Troya, L. Burgue˜no, and A. Vallecillo, “On the assessment
of generative ai in modeling tasks: An experience report with chatgpt
and uml,” Softw. Syst. Model., vol. 22, no. 3, p. 781–793, may 2023.
[Online]. Available: https://doi.org/10.1007/s10270-023-01105-5

[1] J. Franc˚u and P. Hnˇetynka, “Automated generation of implementation
from textual system requirements,” in Software Engineering Techniques:
Third IFIP TC 2 Central and East European Conference, CEE-SET
2008, Brno, Czech Republic, October 13-15, 2008, Revised Selected
Papers 3. Springer, 2011, pp. 34–47.

[2] R. Saini, G. Mussbacher, J. L. C. Guo, and J. Kienzle, “Machine
learning-based incremental learning in interactive domain modelling,”
in Proceedings of the 25th International Conference on Model Driven
Engineering Languages and Systems. ACM, 2022, p. 176–186.
[3] M. Robeer, G. Lucassen, J. M. E. M. van der Werf, F. Dalpiaz, and

#### S. Brinkkemper, “Automated extraction of conceptual models from
user stories via nlp,” in 2016 IEEE 24th International Requirements
Engineering Conference (RE), 2016, pp. 196–205.

[4] S. Yang and H. Sahraoui, “Towards automatically extracting UML class
diagrams from natural language specifications,” in Proceedings of the
25th International Conference on Model Driven Engineering Languages
and Systems: Companion Proceedings, 2022, pp. 396–403.

[5] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang,

#### J. Zhang, Z. Dong et al., “A survey of large language models,” arXiv
preprint arXiv:2303.18223, 2023.

[6] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal,

#### A. Neelakantan, P. Shyam, G. Sastry, A. Askell et al., “Language mod-
els are few-shot learners,” Advances in neural information processing
systems, vol. 33, pp. 1877–1901, 2020.

[7] J. Rumbaugh, I. Jacobson, and G. Booch, Unified Modeling Language
Reference Manual, The (2nd Edition). Pearson Higher Education, 2004.
[8] M. A. Garz´on, H. Aljamaan, and T. C. Lethbridge, “Umple: A frame-
work for model driven development of object-oriented systems,” in IEEE
22nd International Conference on Software Analysis, Evolution, and
Reengineering (saner).

IEEE, 2015, pp. 494–498.

[9] D. Steinberg, F. Budinsky, E. Merks, and M. Paternostro, EMF: Eclipse

Modeling Framework. Pearson Education, 2008.

[10] W. Bian, O. Alam, and J. Kienzle, “Automated grading of class dia-
grams,” in 2019 ACM/IEEE 22nd International Conference on Model
Driven Engineering Languages and Systems Companion (MODELS-C),
2019, pp. 700–709.

[11] M. B. Chaaben, L. Burgue˜no, and H. Sahraoui, “Towards using few-
shot prompt learning for automating model completion,” in IEEE/ACM
International Conference on Software Engineering (ICSE 2023 NIER
track), 2023, in press.

[12] P. Singh, Y. Boubekeur, and G. Mussbacher, “Detecting mistakes in a
domain model,” in Proceedings of the 25th International Conference
on Model Driven Engineering Languages and Systems: Companion
Proceedings, 2022, pp. 257–266.

[13] Y. Boubekeur, G. Mussbacher, and S. McIntosh, “Automatic assessment
of students’ software models using a simple heuristic and machine
learning,” in Proceedings of the 23rd ACM/IEEE International Confer-
ence on Model Driven Engineering Languages and Systems: Companion
Proceedings, 2020, pp. 1–10.

[14] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin,

#### C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
models to follow instructions with human feedback,” arXiv preprint
arXiv:2203.02155, 2022.

[15] OpenAI, “GPT-4 technical report,” 2023.
[16] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in
neural information processing systems, vol. 30, 2017.

[17] A. Radford, K. Narasimhan, T. Salimans, I. Sutskever et al., “Improving

language understanding by generative pre-training,” 2018.

[18] B. Min, H. Ross, E. Sulem, A. P. B. Veyseh, T. H. Nguyen, O. Sainz,

#### E. Agirre, I. Heinz, and D. Roth, “Recent advances in natural language
processing via large pre-trained language models: A survey,” arXiv
preprint arXiv:2111.01243, 2021.

[19] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neubig, “Pre-
train, prompt, and predict: A systematic survey of prompting methods
in natural language processing,” ACM Computing Surveys, vol. 55, no. 9,
pp. 1–35, 2023.

[20] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and D. Zhou,
“Chain of thought prompting elicits reasoning in large language models,”
arXiv preprint arXiv:2201.11903, 2022.

[21] J. Cohen, Statistical power analysis for the behavioral sciences. Aca-

demic press, 2013.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:47 UTC from IEEE Xplore. Restrictions apply.

172


---

> *End of P-02*

<br><br>

<a id="p03-----evaluation-of-vector-database-and-llm-models-in-retrieval-augmented-generation-rag-systems"></a>

## P-03 — Evaluation of Vector Database and LLM Models in Retrieval-Augmented Generation (RAG) Systems

| Field | Details |
|-------|---------|
| **Paper ID** | `P-03` |
| **Title** | Evaluation of Vector Database and LLM Models in Retrieval-Augmented Generation (RAG) Systems |
| **Authors** | Ahmet Furkan Tekgöz, İbrahim Kürşat Şahin, and Burak Aydın |
| **Affiliation(s)** | Loodos A.Ş., Turkey |
| **Venue** | 10th International Conference on Computer Science and Engineering (UBMK) |
| **Volume / Year** | 2025 |
| **DOI** | — |

---

Geri(cid:1) Alma-Artırılmıs¸(cid:1) ¨Uretim(RAG)(cid:1) Sistemlerinde
Vekt¨or(cid:1) Veritabanı(cid:1) ve(cid:1) LLM(cid:1) Modellerinin
De˘gerlendirilmesi
Evaluation(cid:1)of(cid:1)Vector(cid:1)Database(cid:1)and(cid:1)LLM(cid:1)Models(cid:1)in(cid:1)Retrieval-Augmented(cid:1)
Generation(cid:1)(RAG)(cid:1)Systems

Hilal Tekg¨oz
Ar-Ge Birimi
Loodos Teknoloji A.S¸
˙Istanbul, T¨urkiye
hilal.tekgoz@loodos.com

Harun Uz
Ar-Ge Birimi
Loodos Teknoloji A.S¸
˙Istanbul, T¨urkiye
harun.uz@loodos.com

Halit Erdo˘gan
Ar-Ge Birimi
Loodos Teknoloji A.S¸
˙Istanbul, T¨urkiye
halit.erdogan@loodos.com

Hatice Altınok
Ar-Ge Birimi
Loodos Teknoloji A.S¸
˙Istanbul, T¨urkiye
hatice.altınok@loodos.com

¨Oz—B ¨uy ¨uk Dil Modelleri (LLM’ler) birc¸ok farklı alanda
oldukc¸a bas¸arılı sonuc¸lar vermis¸tir. Ancak, g ¨uncelli˘gini yitirmis¸
ve yanlıs¸ bilgiler yerine gerc¸ekc¸ilikten uzak bilgiler ic¸eren
sonuc¸lar ¨uretebilirler. Bu sorunlara bir c¸ ¨oz ¨um olarak, Geri
¨Uretimi (RAG) yaklas¸ımı
¨one c¸ıkmaktadır.
Alma Artırılmıs¸
RAG, ¨uretim s ¨urecine harici bilgi kaynaklarını entegre ederek,
¨ozellikle bilgi yo˘gun g¨orevlerde do˘gruluk ve zamanındalık
ac¸ısından ¨onemli avantajlar sunmaktadır. Bu c¸alıs¸ma, T ¨urkc¸e
ic¸in tasarlanmıs¸ birden fazla RAG mimarisinin sistematik ve
kars¸ılas¸tırmalı bir de˘gerlendirmesini sunmaktadır. RAG boru
hattındaki c¸es¸itli biles¸enlerin (FAISS, QDRANT, Chroma) ve
¨Oklid vb.) geri alma perfor-
benzerlik ¨olc¸ ¨utlerinin (kosin ¨us,
manslarını kars¸ılas¸tıran bir c¸alıs¸mayı
ic¸ermektedir. Bulgu-
larımız, d ¨us¸ ¨uk kaynaklı dil ortamlarında RAG sistemlerinin ver-
imlili˘gini ve g ¨uvenilirli˘gini etkileyen kritik tasarım sec¸imlerini
vurgulamaktadır.

Anahtar S¨ozc ¨ukler—do˘gal dil

is¸leme, geri alma-artırılmıs¸

¨uretimi, vekt¨or veritabanı, benzerlik, ¨uretim


### Abstract

Large Language Models (LLMs) have achieved
notable success in various ﬁelds. However, they can generate
results that, while not necessarily outdated or factually incor-
rect, may be somewhat unrealistic. To address these issues, the
Retrieval Augmented Generation (RAG) approach has emerged
as a promising solution. RAG signiﬁcantly enhances accuracy
and timeliness, especially in information-intensive tasks, by
incorporating external
information sources into the content
generation process. This study provides a systematic and com-
parative evaluation of multiple RAG architectures speciﬁcally
designed for the Turkish language. It includes an analysis
of the retrieval performances of different components (such
as FAISS, QDRANT, and Chroma) and similarity measures
(including cosine and Euclidean distances) within the RAG
pipeline. Our ﬁndings underscore critical design choices that
inﬂuence the efﬁciency and reliability of RAG systems in low-
resource language settings.

(cid:28)(cid:26)(cid:28)(cid:16)(cid:27)(cid:16)(cid:22)(cid:22)(cid:20)(cid:24)(cid:16)(cid:28)(cid:28)(cid:26)(cid:24)(cid:16)(cid:20)(cid:18)(cid:21)(cid:24)(cid:18)(cid:7)(cid:22)(cid:20)(cid:17)(cid:19)(cid:19)(cid:3)(cid:139)(cid:21)(cid:19)(cid:21)(cid:24)(cid:3)(cid:44)(cid:40)(cid:40)(cid:40)


### Index Terms / Keywords

natural(cid:1) language(cid:1) processing,(cid:1) retrieval-augmented(cid:1)

generation,(cid:1) vector(cid:1) databasei(cid:1) similarity,(cid:1) generation

(cid:42)(cid:15) (cid:40)(cid:599)(cid:51)(cid:599)(cid:622)

G¨un¨um¨uzde(cid:1) b¨uy¨uk(cid:1) dil(cid:1) nodelleri(cid:1) (LLM’ler),(cid:1) teknolojinin(cid:1)
gelis¸mesiyle(cid:1) birlikte(cid:1) oldukc¸a(cid:1) bas¸arılı(cid:1) sonuc¸lar(cid:1) vermektedir.(cid:1)
LLM(cid:1)modelleri,(cid:1)cevap(cid:1)¨uretme,(cid:1)metin(cid:1)¨ozetleme,(cid:1)duygu(cid:1)analizi(cid:1)
ve(cid:1) anahtar(cid:1) kelime(cid:1) c¸ıkarımı(cid:1) gibi(cid:1) g¨orevlerde(cid:1) oldukc¸a(cid:1) bas¸arılı(cid:1)
sonuc¸lar(cid:1)vermektedir.(cid:1)Bununla(cid:1)birlikte,(cid:1)bu(cid:1)bas¸arılara(cid:1)ra˘gmen,(cid:1)
dil(cid:1)modellerinin(cid:1)¸co˘gu(cid:1)zaman(cid:1)etkisine(cid:1)dayalı,(cid:1)y¨uksek(cid:1)miktarda(cid:1)
ve(cid:1) dıs¸(cid:1) kaynaklara(cid:1) sahip(cid:1) iyiles¸tirilmis¸(cid:1) yanıtlar(cid:1) ¨uretememesi(cid:1)
¨onemli(cid:1)bir(cid:1)zorluk(cid:1)olarak(cid:1)mevcut(cid:1)de˘gildir.(cid:1)Ancak,(cid:1)Geri(cid:1)Alma-
Artırılmıs¸(cid:1) ¨Uretimi(cid:1) (Retrieval-(cid:1) Augmented(cid:1) Generation,(cid:1) RAG)(cid:1)
mimarisi(cid:1) ,(cid:1) modelin(cid:1) yalnızca(cid:1) kendi(cid:1) kendine(cid:1) e˘gitildi˘gi(cid:1) veriye(cid:1)
dayanmak(cid:1) yerine(cid:1) ,(cid:1) harici(cid:1) bilgi(cid:1) kaynaklarına(cid:1) saklanmasını(cid:1)
sa˘glayarak(cid:1) daha(cid:1) sa˘glam,(cid:1) ac¸ıklayıcı(cid:1) ve(cid:1) g¨uvenilir(cid:1) yanıtlar(cid:1)
¨uretmesine(cid:1) destek(cid:1) olmaktadır(cid:1) [1].(cid:1) B¨oylece(cid:1) sistem,(cid:1) ¨once(cid:1) dıs¸(cid:1)
kaynaklardan(cid:1) ilgili(cid:1) bilgiyi(cid:1) bulmakta(cid:1) ve(cid:1) ardından(cid:1) bu(cid:1) bilgiye(cid:1)
dayanarak(cid:1)kullanıcıya(cid:1)yanıt(cid:1)¨uretmektedir.

RAG(cid:1) tabanlı(cid:1) sistemler,(cid:1) elde(cid:1) edilen(cid:1) literat¨ur(cid:1) taramasında(cid:1)
˙Ingilizce(cid:1)gibi(cid:1)evrensel(cid:1)diller(cid:1)¨uzerindedir.(cid:1)Fakat,(cid:1)T¨urkc¸e(cid:1)gibi(cid:1)dil(cid:1)
yapısı(cid:1) bakımından(cid:1) zengin(cid:1) ve(cid:1) kaynak(cid:1) c¸es¸itlili˘gi(cid:1) sınırlı(cid:1) olan(cid:1)
dillerde(cid:1)RAG(cid:1)sistemlerinin(cid:1)nasıl(cid:1)performans(cid:1)g¨osterdi˘gine(cid:1)dair(cid:1)
kapsamlı(cid:1) c¸alıs¸malar(cid:1) oldukc¸a(cid:1) azdır.(cid:1) Bu(cid:1) da(cid:1) T¨urkc¸e(cid:1) dilinde(cid:1)
c¸alıs¸an(cid:1) RAG(cid:1) tabanlı(cid:1) yapay(cid:1) zeka(cid:1) sistemlerinin(cid:1) g¨uvenilirli˘gini(cid:1)
do˘grudan(cid:1)
olarak(cid:1)
de˘gerlendirilmektedir.

etkileyen(cid:1)

c¸alıs¸ma(cid:1)

alanı(cid:1)

bir(cid:1)

Bu(cid:1)¸calıs¸ma,(cid:1)T¨urkc¸e(cid:1)ic¸in(cid:1)tasarlanmıs¸(cid:1)¸ces¸itli(cid:1)RAG(cid:1)yapılarını(cid:1)
kars¸ılas¸tırmalı(cid:1)olarak(cid:1)incelemeyi(cid:1)amac¸lamaktadır.(cid:1)Gelis¸tirilen

IEEE-UBMK-2025 International Conference on Computer Science and Engineering - 572
Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:08 UTC from IEEE Xplore. Restrictions apply.


deneysel y¨ontemler, c¸es¸itli bilgi eris¸im mekanizmaları ve
ile test edilmis¸tir. Bu s¨urec¸te,
metin ¨uretim modelleri
yanıtların do˘grulu˘gu, ic¸eri˘ge uygunlu˘gu ve ¨uretim s¨uresi gibi
c¸es¸itli ¨olc¸ ¨utler ¨uzerinden de˘gerlendirmeler yapılmıs¸tır.

Bilgiye dayalı yanıtlama sistemlerinin daha g¨uvenilir,
s¸effaf ve eris¸ilebilir hale gelmesi, yalnızca akademik
aras¸tırma ic¸in de˘gil , aynı zamanda e˘gitim, kamu hizmetleri
ve m¨us¸teri destek sistemleri gibi birc¸ok alanda da kul-
lanılabilmektedir. Bu c¸alıs¸manın temel amacı da, bu potan-
siyele katkı sunacak yapısal kars¸ılas¸tırmalar ortaya koymak
ve T¨urkc¸e’de RAG mimarisinin g¨uc¸l¨u ve zayıf y¨onlerini
ortaya c¸ıkarmaktır.

II.

˙ILG˙IL˙I C¸ ALIS¸ MALAR

B¨uy¨uk Dil Modelleri (LLM’ler), do˘gal dil
is¸leme (NLP)
alanında ¨onemli bir ilerleme kaydederek c¸ok sayıda kul-
lanım alanında ¨onemli bir bas¸arı elde etmis¸tir. Generative
Pre-trained Transformers (GPT) [2], LLaMA [3] ve Gem-
ini [4] gibi ¨ornekler, ba˘glama uygun ve anlamsal olarak
olus¸turma yetene˘gine sahiptir. Aynı zamanda, bu modellerin
hatalı veya do˘gru olmayan ic¸erikler ¨uretme e˘giliminde olması
¨onemli bir gelis¸tirme konusu olarak de˘gerlendirilmektedir
[5]. Literat¨urde hal¨usinasyon olarak adlandırılan bu du-
rum g¨un¨um¨uzde hala ¨uzerinde yo˘gun bic¸imde c¸alıs¸ılan bir
aras¸tırma konusudur [6]. Hal¨usinasyon, do˘gru ve anlam-
¨uretebilmek adına Geri Alma-
sal olarak alakalı c¸ıktılar
¨Uretimi (Retrieval-Augmented Generation,RAG)
Artırılmıs¸
gibi y¨ontemler ¨one c¸ıkmaktadır.

Bilgi getirme ile ¨uretici modelleri birles¸tirerek do˘gal
is¸leme performansını artırmayı hedeﬂeyen RAG [7]
dil
yaklas¸ımı, son d¨onemde dikkat c¸eken bir y¨ontemdir [8]. Dıs¸
bilgi veri tabanlarından yararlanarak, RAG sistemleri daha
do˘gru ve anlamsal olarak alakalı c¸ıktılar ¨uretebilmektedir [8].
RAG’ın geri alma ve metin ¨uretimini birles¸ik bir c¸erc¸evede
dinamik olarak sunması NLP sistemlerinin performansını
iyiles¸tirme potansiyelini arttırmıs¸tır. RAG sistemi, bilim, ﬁ-
nans, e˘gitim, sa˘glık, hukuk ve end¨ustri gibi birc¸ok alanda
bilgi getirme ve ¨uretme yeteneklerini birles¸tirerek perfor-
mansı ¨onemli ¨olc¸ ¨ude artırmaktadır. Bu modeller, karmas¸ık
veri k¨umelerinden ba˘glama uygun, g¨uncel ve do˘gru bilgi-
leri alarak daha verimli karar destek sistemleri sunmaktadır.
RAG modelleri bilimsel aras¸tırma alanında genis¸ veri ta-
banlarından g¨uncel bilgileri c¸ekerek aras¸tırmacılara ¨onemli
¨Orne˘gin, RAG tabanlı ChemLit-
destek sunmaktadır [8].
QA [9] kimyada sentez planlama ve reaksiyon tahmini
gibi g¨orevlerde disipline ¨ozg¨u sorguları gelis¸tirmektedir.
Aynı s¸ekilde Biorag [10] sistemi, biyoloji ve yas¸am bil-
imlerinde aras¸tırmacılara hızlı ve etkili bilgi sa˘glamak ic¸in
gelis¸tirilmis¸tir. Geleneksel C¸ in tıbbında eski kaynaklarda ki
bilgilere eris¸imi kolaylas¸tırmak ic¸in RAG tabanlı bir sis-
tem gelis¸tirilmis¸tir. C¸ alıs¸mada veriler d¨u˘g¨umler ve ilis¸kiler
s¸eklinde bir graﬁk veri tabanında tutulup RAG tekni˘gi kul-
lanılarak, soru-cevap s¨urec¸lerinde ba˘glam zenginles¸tirilmis¸tir
[11]. Hukuk alanında, CBR-RAG [12] ile ba˘glamsal olarak
sa˘glanmaktadır. Yapılan
ilgili davaların geri getirilmesi
bir bas¸ka c¸alıs¸mada, hukuk ve politika alanındaki ya-
pay zeka uygulamalarında do˘grulu˘gu artırmak ic¸in sorgu

karmas¸ıklı˘gını dikkate alarak hibrit geri alma stratejileri
kullanan ve NYC Yerel Yasası 144 ¨uzerinde test edilen
RAG tabanlı HyPA-RAG [13] adlı bir sistem gelis¸tirilmis¸tir.
End¨ustride, end¨ustriyel ortamlarda gerc¸ek zamanlı sorun
c¸ ¨ozme amacıyla, bilgi c¸ekme (retrieval) ve ¨uretme (gener-
ation) yeteneklerini birles¸tiren RAG modelleri gelis¸tirilmis¸
ve kullanılmıs¸tır. Yapılan c¸alıs¸malar, RAG tabanlı sistemlerin
operasyonel verimlili˘gi artırarak arıza c¸ ¨oz¨um s¨uresini azalt-
mada etkili olmus¸tur. [14].


### III. Uygulama Metotlari


#### A. B¨uy¨uk Dil Modelleri (LLM’ler)

¨ozellikle 2020’den
B¨uy¨uk Dil Modelleri (LLM’ler) [15],
bu yana, kapsamlı ve b¨uy¨uk veri k¨umeleri
¨uzerinde
e˘gitilerek dil anlama ve ¨uretme g¨orevlerinde dikkate de˘ger
bas¸arılı sonuc¸lar elde etmis¸tir. Bu modeller, hem genel dil
¨uretimi ve soru cevaplama hem de metin tamamlama ve
¨ozetleme gibi bilgiye ihtiyac¸ olan g¨orevlerde insan d¨uzeyinde
veya insanı as¸an bas¸arılar g¨ostermektedir. LLM’lerin temel
¨ozelliklerinden biri ba˘glamsal dili anlama ve karmas¸ık
bilgileri b¨ut¨unles¸tirme kapasiteleridir. Transformer tabanlı
c¸ok katmanlı dikkat mekanizmaları sayesinde, veri ic¸indeki
ilis¸kileri kavrayıp farklı bilgileri
tutarlı ve akıcı bic¸imde
birles¸tirebilirler. LLM modelleri genis¸ c¸aplı veriler ¨uzerinde
e˘gitildikleri ic¸in, bazen g¨uncel olmayan, hatalı veya ba˘glama
uygun olmayan ic¸erikler ¨uretebilmektedir [16]. Bu olguya
literat¨urde ”hal¨usinasyon” adı verilmektedir [16]. ¨Ozellikle
y¨uksek bilgi yo˘gunlu˘gu ve do˘grulu˘gunun ¨onemli oldu˘gu
end¨ustriyel ve teknik ba˘glamlarda sistem, yanlıs¸ ve ba˘glamsal
olarak uygunsuz ic¸erik ¨uretebilmektedir. Bu nedenle, mod-
elin g¨uvenilirli˘gini etkileyen ¨onemli biles¸enlerden biri olarak
g¨osterilmektedir [17].

C¸ alıs¸mamızda metin ¨uretme biles¸eni olarak OpenAI’nin
GPT-4o modeli ve Google’ın Gemini modeli kullanılmıs¸tır.
ileri d¨uzey
GPT, c¸ok b¨uy¨uk parametre sayısına sahip,
bir transformer tabanlı dil modeli olup, do˘gal dil
is¸leme
g¨orevlerinde y¨uksek do˘gruluk oranı vermektedir [8]. Google
ise, g¨uncel mi-
tarafından gelis¸tirilen Gemini modeli
mari gelis¸tirmelerle optimize edilmis¸, c¸ok modlu ve c¸ok
¨o˘grenme ¨ozelliklerine sahip bir b¨uy¨uk dil mod-
g¨orevli
eli olarak ¨one c¸ıkar. Gemini,
¨ozellikle dil anlama ve
¨uretme s¨urec¸lerinde daha hızlı ve hassas sonuc¸lar sunabilmek
amacıyla tasarlanmıs¸tır.


#### B. Geri Alma-Artırılmıs¸ ¨Uretimi (RAG)

B¨uy¨uk dil modelleri (LLM) ola˘gan¨ust¨u yetenekleri sayesinde
do˘gal dil is¸leme (NLP) sekt¨or¨un¨un ¨onemli bir parc¸ası haline
gelmis¸tir [18]. LLM’ler b¨uy¨uk miktarda veriyle e˘gitilmis¸
olmalarına ra˘gmen hala halis¨unasyon gibi gerc¸ek dıs¸ı
yanıtlar ¨uretebilmektedirler. Bu as¸amada devreye Geri Alma-
¨Uretim (RAG) sistemleri girmis¸tir. LLM’lerin
Artırılmıs¸
hal¨usinasyon g¨ormesini ¨onlemek amacıyla, LLM’lerin harici
bilgi kaynaklarından (yani vekt¨or veritabanlarından) anlamlı
ic¸erikler alması, do˘gruluk ve g¨uvenilirlik ac¸ısından umut
verici bir yaklas¸ımdır [19]. RAG yaklas¸ımı iki as¸amadan
olus¸ur. Bunlar s¸ekil 1’de de g¨or¨uld¨u˘g¨u ¨uzere alma (retrieval)

IEEE-UBMK-2025 International Conference on Computer Science and Engineering - 573
Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:08 UTC from IEEE Xplore. Restrictions apply.

ve ¨uretme (generation) as¸amalarıdır.

¸Sekil(cid:1) 1(cid:15)(cid:1) RAG(cid:1) mimarisi.

Bu(cid:1) iki(cid:1) as¸amalı(cid:1) yapının(cid:1) ilk(cid:1) adımı(cid:1) olan(cid:1) alma(cid:1) (retrieval)(cid:1)
s¨urecinde,(cid:1) kullanıcıdan(cid:1) gelen(cid:1) sorguya(cid:1) uygun(cid:1) ic¸eriklerin(cid:1)
dıs¸(cid:1) bilgi(cid:1) kaynaklarından(cid:1) alınması(cid:1) hedeﬂenmektedir.(cid:1)Bunun(cid:1)
ic¸in(cid:1) klasik(cid:1) kelime(cid:1) temelli(cid:1) alma(cid:1) y¨ontemlerinden(cid:1) biri(cid:1) olan(cid:1)
BM25(cid:1) algoritması(cid:1) ile(cid:1) semantik(cid:1) d¨uzeyde(cid:1) benzerlik(cid:1) kurabilen(cid:1)
dense(cid:1) retriever(cid:1) yaklas¸ımları(cid:1) bir(cid:1) arada(cid:1) kullanılabilmektedir.(cid:1)
BM25,(cid:1) kelime(cid:1) frekansına(cid:1) dayalı(cid:1) olarak(cid:1) belge(cid:1) ile(cid:1) sorgu(cid:1)
arasındaki(cid:1) benzerli˘gi(cid:1) ¨olc¸erken(cid:1) [20],(cid:1) dense(cid:1) retriever(cid:1) ise(cid:1)
derin(cid:1) o¨(cid:1)˘grenme(cid:1) tabanlı(cid:1) g¨ommeler(cid:1) (embedding)(cid:1) ¨uzerinden(cid:1)
¸calıs¸arak(cid:1) daha(cid:1) anlam(cid:1) temelli(cid:1) es¸les¸meler(cid:1) sa˘glamaktadır(cid:1) [21].(cid:1)
Her(cid:1) iki(cid:1) y¨ontemin(cid:1) avantajlarını(cid:1) birles¸tirmek(cid:1) amacıyla,(cid:1) bu(cid:1)
¸calıs¸mada(cid:1) EnsembleRetriever(cid:1) yapısı(cid:1) kullanılmıs¸tır.(cid:1) Ensem-
bleRetriever,(cid:1) hem(cid:1) seyrek(sparse)(cid:1) hem(cid:1) de(cid:1) yo˘gun(dense)(cid:1)
yaklas¸ımları(cid:1) aynı(cid:1) anda(cid:1) de˘gerlendirerek(cid:1) daha(cid:1) do˘gru(cid:1) bilgi(cid:1)
alımını(cid:1)sa˘glamaktadır.(cid:1)˙Ikinci(cid:1)as¸ama(cid:1)olan(cid:1) ¨uretme(cid:1)(generation)(cid:1)
kısmında(cid:1)ise,(cid:1)alma(cid:1)as¸amasında(cid:1)getirilen(cid:1)belgeler(cid:1)ba˘glamında(cid:1)
dil(cid:1)modeli(cid:1)tarafından(cid:1)nihai(cid:1)yanıt(cid:1)olus¸turulur.(cid:1)Bu(cid:1)ba˘glamlama(cid:1)
s¨ureci,(cid:1)LLM’lerin(cid:1)yalnızca(cid:1)e˘gitim(cid:1)verisine(cid:1)dayalı(cid:1) ¨uretim(cid:1)yap-
ması(cid:1) yerine,(cid:1) g¨uncel(cid:1) ve(cid:1) do˘grulanabilir(cid:1) bilgilere(cid:1) eris¸erek(cid:1) yanıt(cid:1)
olus¸turmasını(cid:1) m¨umk¨un(cid:1) kılar.(cid:1) B¨oylece(cid:1) modelin(cid:1) hal¨usinasyon(cid:1)
¨uretme(cid:1) olasılı˘gı(cid:1) azaltılırken,(cid:1) aynı(cid:1) zamanda(cid:1) yanıtların(cid:1) bilgiye(cid:1)
dayalı(cid:1) ve(cid:1) ba˘glamsal(cid:1) olarak(cid:1) tutarlı(cid:1) olması(cid:1) sa˘glanır(cid:1) [22].

IV. DENEYSEL(cid:1) C¸(cid:1)ALI(cid:1)¸SMALAR


#### A. Sistem(cid:1) Tasarımı

Bu(cid:1) ¸calıs¸mada,(cid:1) bilgiye(cid:1) dayalı(cid:1) g¨orevlerde(cid:1) RAG(cid:1) sistemlerinin(cid:1)
performansını(cid:1) analiz(cid:1) etmek(cid:1) amacıyla(cid:1) deneysel(cid:1) c¸alıs¸malar(cid:1)
yapılmıs¸tır.(cid:1) RAG(cid:1) mimarisi,(cid:1) LLM’lere(cid:1) g¨ore(cid:1) daha(cid:1) g¨uncel,(cid:1)
do˘grulanabilir(cid:1) ve(cid:1) ba˘glamsal(cid:1) olarak(cid:1) zengin(cid:1) ic¸erikler(cid:1) ¨uretmeyi(cid:1)
amac¸lamaktadır.(cid:1) Deneysel(cid:1) ¸calıs¸mada(cid:1) kullanılan(cid:1) veri(cid:1) seti,(cid:1)
Loodos(cid:1) ﬁrmasında(cid:1)˙ Insan(cid:1)K aynakları(cid:1)( ˙IK)(cid:1)s¨urec¸lerinde(cid:1)
¸calıs¸anları(cid:1) bilgilendirmek(cid:1) amacıyla(cid:1) kullanılan(cid:1) kurumsal(cid:1)
dok¨umanlardan(cid:1)olus¸maktadır.(cid:1)Bu(cid:1)dok¨umanlar,(cid:1)s¸irket(cid:1)ic¸i(cid:1)bilgi(cid:1)
paylas¸ımını(cid:1) sa˘glamak(cid:1) ve(cid:1) c¸alıs¸anların(cid:1) sorularına(cid:1) yanıt(cid:1) ver-
mek(cid:1) ¨uzere(cid:1) yapılandırılmıs¸tır.(cid:1) Dok¨umanlar(cid:1) ¸ces¸itli(cid:1) formatlarda(cid:1)
(PDF,(cid:1)CSV,(cid:1)Excel,(cid:1)HTML,(cid:1)metin(cid:1)dosyaları)(cid:1)toplanmıs¸(cid:1) ve(cid:1) ¨on(cid:1)
is¸leme(cid:1) tabi(cid:1) tutulmus¸tur.(cid:1) Kullanılan(cid:1) veri(cid:1) seti,(cid:1) T¨urkc¸e(cid:1) dilinde(cid:1)
hazırlanmıs¸(cid:1) ve(cid:1) sadece(cid:1) kuruma(cid:1) ¨ozgu¨(cid:1) ic¸erik(cid:1) barındırması(cid:1)
bakımından(cid:1) ¨ozg¨un(cid:1) bir(cid:1) nitelik(cid:1) tas¸ımaktadır.(cid:1) Bu(cid:1) kapsamda,(cid:1)
toplamda(cid:1) 12(cid:1) farklı(cid:1) RAG(cid:1) akıs¸ları(cid:1) (pipeline)(cid:1) yapılandırılmıs¸(cid:1)
ve(cid:1) kars¸ılas¸tırmalı(cid:1) olarak(cid:1) test(cid:1) edilmis¸tir.(cid:1) C¸(cid:1)alıs¸mada(cid:1) s¸ekil(cid:1)
2’deki(cid:1) akıs¸(cid:1) ¨uzerinden(cid:1) ilerlenilmis¸tir.(cid:1) Her(cid:1) pipeline,(cid:1) iki(cid:1) ana

biles¸enden olus¸maktadır: belge eris¸imi(retrieval) ve metin
¨uretimi(generation) katmanları.

Retrieval biles¸eninde FAISS, Qdrant ve Chroma olmak
¨uzere ¨uc¸ farklı vekt¨or veritabanı kullanılmıs¸tır. Bu vekt¨or
tabanlı arama sistemleri, sorguya en yakın belgeleri bulmak
ic¸in belge g¨ommelerini kullanmaktadır. Her vekt¨or veri ta-
banı, kosin¨us ve ¨oklid olmak ¨uzere iki farklı benzerlik ¨olc¸ ¨ut¨u
ile ayrı ayrı test edilmis¸tir. B¨oylece her veritabanı ic¸in iki
ayrı yapılandırma (¨orne˘gin: “Qdrant + ¨Oklid” ve “Qdrant +
Kosin¨us”) olus¸turulmus¸tur.

Generation biles¸eninde ise OpenAI GPT-4o ve Google
Gemini Pro olmak ¨uzere iki LLM kullanılmıs¸tır. Her bir
retrieval biles¸eni bu iki LLM ile birles¸tirilerek, toplamda 3
(vekt¨or DB) × 2 (benzerlik) × 2 (LLM) = 12 farklı pipeline
tanımlanmıs¸tır.


#### B. Embedding Y¨ontemleri

Retrieval performansını etkileyen temel biles¸enlerden biri
de g¨omme y¨ontemidir. Belgeler ve sorgular, uygun vekt¨or
temsillere d¨on¨us¸t¨ur¨ulmeden vekt¨or veri tabanı ic¸inde benz-
erlik kars¸ılas¸tırması yapılamaz. Bu c¸alıs¸mada, kullanılan her
pipeline’ın g¨omme olus¸turma s¨ureci de model sec¸imine g¨ore
belirlenmis¸tir.

S¸ ekil(cid:1)2(cid:15)(cid:1)C¸(cid:1)alıs¸manın(cid:1)sistem(cid:1)tasarım(cid:1)as¸amaları.

Dok¨umanlar(cid:1) ¨once(cid:1) normalize(cid:1) edilip,(cid:1) parc¸alara(cid:1) (chunk)(cid:1)
b¨ol¨unm¨us¸t¨ur.(cid:1) Chunk(cid:1) b¨uy¨uklu¨g˘u¨(cid:1) ve(cid:1) c¸akıs¸ma(cid:1) parametreleri(cid:1)
deneysel(cid:1) olarak(cid:1) belirlenmis¸tir.(cid:1) Ardından,(cid:1) metinler(cid:1) g¨omme(cid:1)
is¸lemi(cid:1) ic¸in(cid:1) uygun(cid:1) formata(cid:1) getirilmis¸(cid:1) ve(cid:1) g¨omme(cid:1) modelleri(cid:1)
olarak(cid:1)OpenAI’nın(cid:1)text-embedding-3-large(cid:1)ve(cid:1)Google’ın(cid:1)text-
embedding-004(cid:1) modelleri(cid:1) kullanılmıs¸tır.(cid:1) text-embedding-3-
large(cid:1) modeli,(cid:1) metinleri(cid:1) en(cid:1) fazla(cid:1) 8191(cid:1) token(cid:1) sayısına(cid:1) g¨ore,(cid:1)
boyutu(cid:1)N(cid:1)=(cid:1)3072(cid:1)olan(cid:1)vekt¨orler(cid:1)olus¸turmaktadır(cid:1)[23].(cid:1)Google(cid:1)
Gemini’nin(cid:1) text-embedding-004(cid:1) modeli(cid:1) 768(cid:1) boyutlu(cid:1) bir(cid:1)
vekt¨or(cid:1) c¸ıktısı(cid:1) vermektedir.

Her(cid:1) pipeline(cid:1) ic¸in(cid:1) sec¸ilen(cid:1) vekt¨or(cid:1) depolama(cid:1) ve(cid:1) mesafe(cid:1)
metri˘giyle(cid:1)
indeksleme(cid:1)
yapılmıs¸tır.(cid:1) Ardından(cid:1)
indeksler(cid:1)
¨uzerinde(cid:1) c¸alıs¸tırılmıs¸tır.(cid:1) Retrieval(cid:1) sonuc¸ları,(cid:1) ilgili(cid:1) ¨uretim

sonuc¸ları(cid:1)
retrieval(cid:1) sorguları(cid:1) bu(cid:1)

¨uzerinden(cid:1)

g¨omme(cid:1)

IEEE-UBMK-2025 International Conference on Computer Science and Engineering - 574
Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:08 UTC from IEEE Xplore. Restrictions apply.

modeline(cid:1) girdi(cid:1) olarak(cid:1) verilmis¸tir.


#### C. De˘gerlendirme

Deneysel(cid:1) ¸calıs¸malar,(cid:1) T¨urkc¸e(cid:1) dilinde(cid:1) bilgiye(cid:1) dayalı(cid:1) soru-
cevap(cid:1) g¨orevleri(cid:1) ¨uzerinde(cid:1) gerc¸ekles¸tirilmis¸tir.(cid:1) Test(cid:1) veri(cid:1) seti,(cid:1)
Loodos(cid:1) ˙IK(cid:1) veri(cid:1) seti(cid:1) ic¸erisinde(cid:1) bulunan(cid:1) genel(cid:1) bilgiler-
den(cid:1) teknik(cid:1) bilgilere(cid:1) kadar(cid:1) ¸ces¸itli(cid:1) ic¸erikleri(cid:1) kapsamaktadır.(cid:1)
C¸(cid:1)alıs¸ma(cid:1) kapsamında(cid:1) olus¸turulan(cid:1) her(cid:1) bir(cid:1) RAG(cid:1) pipeline,(cid:1)
Loodos(cid:1) ﬁrmasının(cid:1)˙Insan(cid:1)K aynakları(cid:1)s ¨urec¸lerine(cid:1)i lis¸kin(cid:1)ku-
rumsal(cid:1) dok¨umanlar(cid:1) ¨uzerinde(cid:1) yapılandırılmıs¸(cid:1) sabit(cid:1) bir(cid:1) soru(cid:1)
seti(cid:1) ile(cid:1) test(cid:1) edilmis¸tir.(cid:1) De˘gerlendirme(cid:1) s¨urecinde,(cid:1) sistem-
lerin(cid:1) yanıt(cid:1) ¨uretme(cid:1) bas¸arımı(cid:1) iki(cid:1) temel(cid:1) ¨olc¸(cid:1)¨ut(cid:1) ¨uzerinden(cid:1)
analiz(cid:1)edilmis¸tir:(cid:1)yanıtların(cid:1)do˘grulu˘gu(cid:1)ve(cid:1) ¨uretim(cid:1)as¸amalarının(cid:1)
toplam(cid:1) yanıt(cid:1) s¨uresi.(cid:1) Bu(cid:1) de˘gerlendirme(cid:1) metrikleri(cid:1) sayesinde,(cid:1)
sadece(cid:1) yanıt(cid:1) kalitesi(cid:1) de˘gil(cid:1) aynı(cid:1) zamanda(cid:1) sistemlerin(cid:1) zaman(cid:1)
verimlili˘gi(cid:1) de(cid:1) g¨oz(cid:1) ¨on¨unde(cid:1) bulundurulmus¸tur.(cid:1) ¨Uretme(cid:1) (gen-
eration)(cid:1) as¸amasında(cid:1) yapılan(cid:1) c¸alıs¸malarda,(cid:1) OpenAI(cid:1) GPT-4o(cid:1)
modelinin(cid:1) yanıt(cid:1) ¨uretme(cid:1) s¨uresinin,(cid:1) Google(cid:1) Gemini(cid:1) modeline(cid:1)
g¨ore(cid:1) daha(cid:1) uzun(cid:1) oldu˘gu(cid:1) sonucuna(cid:1) ulas¸ılmıs¸tır.

Deneysel(cid:1) sonuc¸ların,(cid:1) tablo(cid:1) I(cid:1) incelendi˘ginde,(cid:1) pipeline(cid:1)
biles¸enlerinin(cid:1) (retrieval(cid:1) veritabanı,(cid:1) benzerlik(cid:1) metri˘gi(cid:1) ve(cid:1)
LLM)(cid:1) sistem(cid:1) performansı(cid:1) ¨uzerinde(cid:1) anlamlı(cid:1) bir(cid:1) etkiye(cid:1) sahip(cid:1)
oldu˘gunu(cid:1)g¨ostermis¸tir.(cid:1)En(cid:1)y¨uksek(cid:1)performans,(cid:1)Chroma(cid:1)vekt¨or(cid:1)
veritabanı(cid:1) ile(cid:1) kosin¨us(cid:1) benzerli˘gi(cid:1) kullanılarak(cid:1) ve(cid:1) Gemini(cid:1)
modeliyle(cid:1) yapılan(cid:1) ¨uretim(cid:1) s¨ureci(cid:1) sonucunda(cid:1) elde(cid:1) edilmis¸tir.(cid:1)
Chroma(cid:1)ve(cid:1)kosin¨us(cid:1)benzerli˘ginin(cid:1)y¨uksek(cid:1)bas¸arım(cid:1)g¨ostermesi(cid:1)
chroma(cid:1) veritabanının(cid:1) hızlı(cid:1) indeksleme(cid:1) ve(cid:1) bellek(cid:1) yapısı(cid:1)
yetenekleri(cid:1) ile(cid:1) kosin¨us(cid:1) metriklerinin(cid:1) semantik(cid:1) yakınlı˘gı(cid:1)
daha(cid:1)bas¸arılı(cid:1)yakalamasından(cid:1)kaynaklandı˘gı(cid:1)g¨ozlemlenmis¸tir.(cid:1)
Di˘ger(cid:1) yandan,(cid:1) Qdrant(cid:1) veritabanı(cid:1) ve(cid:1) GPT-4o(cid:1) modeli(cid:1) ile(cid:1)
olus¸turulan(cid:1) bazı(cid:1) pipeline’lar(cid:1) da(cid:1) 0.90(cid:1) do˘gruluk(cid:1) d¨uzeyiyle(cid:1)
oldukc¸a(cid:1) y¨uksek(cid:1) bas¸arı(cid:1) g¨ostermis¸tir.(cid:1) Buna(cid:1) kars¸ılık,(cid:1) FAISS(cid:1)
veri(cid:1)tabanının(cid:1)bazı(cid:1)varyasyonlarında,(cid:1) ¨ozellikle(cid:1)cosine(cid:1)metrikli(cid:1)
GPT-4o(cid:1) kombinasyonlarında,(cid:1) do˘gruluk(cid:1) skorlarının(cid:1) 0.81’e(cid:1)
kadar(cid:1) d¨us¸tu¨g˘u¨(cid:1) g¨ozlemlenmis¸tir.(cid:1) FAISS(cid:1) ve(cid:1) GPT-4o(cid:1) akıs¸ında(cid:1)
d¨us¸ ¨uk(cid:1) performans(cid:1) g¨ozlemlenmesi,(cid:1) text-embedding-3-large(cid:1)
g¨omme(cid:1) modelinin(cid:1) vekt¨or(cid:1)
temsillerinin(cid:1) benzerlik(cid:1) skoru(cid:1)
¨uretmede(cid:1)yetersiz(cid:1)kalması(cid:1)ile(cid:1)ilis¸kilidir.

TABLO(cid:1)I(cid:15)(cid:1)RAG(cid:1)S˙ISTEMLER˙IN˙IN(cid:1)DO(cid:1)˘GRULUK(cid:1)PERFORMANSI

Retriever DB
Chroma
Qdrant
Qdrant
Qdrant
FAISS
FAISS
FAISS
Chroma
Chroma
FAISS
Chroma
Qdrant

G¨omme
text-embedding-004
text-embedding-004
text-embedding-004
text-embedding-3-large
text-embedding-004
text-embedding-3-large
text-embedding-004
text-embedding-004
text-embedding-3-large
text-embedding-3-large
text-embedding-3-large
text-embedding-3-large

Benzerlik ¨Olc¸ ¨ut ¨u
Kosin¨us
¨Oklid
Kosin¨us
Kosin¨us
¨Oklid
Kosin¨us
Kosin¨us
¨Oklid
Kosin¨us
¨Oklid
¨Oklid
¨Oklid

¨Uretim
gemini-1.5-pro
gemini-1.5-pro
gemini-1.5-pro
GPT-4o
gemini-1.5-pro
GPT-4o
gemini-1.5-pro
gemini-1.5-pro
GPT-4o
GPT-4o
GPT-4o
GPT-4o

Bas¸arı (%)
96.00
93.00
90.00
90.00
90.00
81.00
86.00
83.00
91.00
86.00
90.00
86.00

retriever de˘gil, g¨omme katmanının kalitesi ve modelle uyumu
da belirleyici bir fakt¨ord¨ur. Ayrıca elde edilen sonuc¸lar,
sadece do˘gruluk oranı ile de˘gil, aynı zamanda kurulan sis-
temin cevap ¨uretme s¨uresi ve g¨omme y¨ontemi
ile LLM
uyumu ac¸ısından da de˘gerlendirilmis¸tir. Bu da T¨urkc¸e RAG
sistemlerinin daha verimli hale getirilmesi ic¸in ¨onemli sistem
akıs¸ı ¨onerileri sunmaktadır.

¨uretme performansı

talepleriyle sistemin yanıt

Sistem performansının canlı ortamda nasıl c¸alıs¸tı˘gını
analiz edebilmek adına, c¸alıs¸anların sıkc¸a kars¸ılas¸tı˘gı g¨unl¨uk
test
bilgi
edilmis¸tir. ¨Orne˘gin, bir kullanıcı ”Arife g¨un¨u tatil mi?” diye
bir soru sordu˘gunda gelis¸tirilen sistem ”Ramazan, Kurban
tatilleri arife g¨unleri saat 13.00
ve Cumhuriyet Bayramı
itibarıyla bas¸lar. Yani arife g¨unleri yarım g¨un resmi tatildir.”
s¸eklinde bir cevap ¨uretmektedir. Ayrıca kullanıcının detaylı
bilgiye eris¸imini kolaylas¸tırmak ic¸in s¸irket ic¸indeki ic¸ kay-
naklara y¨onlendiren bir ba˘glantı linki de g¨ondermektedir.


#### V. SONUC¸ LAR VE GELECEK C¸ ALIS¸ MALAR

¨Uretim (RAG) mimarisi
Bu c¸alıs¸ma, Geri Alma-Artırılmıs¸
kullanılarak olus¸turulan c¸es¸itli RAG (boru hattı) biles¸enleri
arasındaki etkiles¸imleri ve bunların sistem performansını
nasıl etkiledi˘gini kapsamlı bir s¸ekilde incelemis¸tir. Deneysel
bulgulara g¨ore, geri alma ve ¨uretim s¨urec¸leri ayrı ayrı de˘gil,
birbirleriyle ilis¸kili olarak de˘gerlendirilmelidir. C¸ alıs¸mada en
y¨uksek performans, Chroma vekt¨or veritabanı ile kosin¨us
benzerli˘gi kullanılarak ve Gemini modeliyle yapılan ¨uretim
s¨ureci sonucunda elde edilmis¸tir. ¨Ozellikle Chroma ve Qdrant
olmak ¨uzere g¨uncel vekt¨or veritabanlarının kullanılması,
bilgi alma kalitesini artırmakta ve genel olarak sistem per-
formansını olumlu y¨onde etkilemektedir. Benzer s¸ekilde,
kosin¨us benzerli˘gi gibi semantik yakınlık ¨olc¸ ¨um¨unde daha
etkili olan metriklerin tercih edilmesi, y¨uksek do˘gruluk oran-
larına ulas¸ılmasında belirleyici rol oynamaktadır.

Gelecekteki c¸alıs¸malarda, c¸ok modlu veri kaynaklarının
ve farklı dildeki dok¨umanların dahil edilmesi, gelis¸tirilen
sistemin dinamikles¸tirilebilirli˘gi test etme ac¸ısından ¨onemli
bir aras¸tırma alanı olarak de˘gerlendirilebilir. Bu do˘grultuda,
RAG mimarilerinin kurumsal bilgi tabanlarında daha etkin
ve s¨urd¨ur¨ulebilir s¸ekilde uygulanabilmesi ic¸in biles¸enlerin
dikkatli bir s¸ekilde sec¸ilmesi ve sistematik olarak optimize
edilmesi gerekmektedir. Ayrıca gelecekteki c¸alıs¸malarımızda,
her bir kategoriye ¨ozg¨u ayrı koleksiyonlar olus¸turarak, kul-
lanıcı sorgularının ic¸eri˘gine g¨ore ilgili kategoriyi tespit eden
ve bu do˘grultuda yalnızca o kategoriye ait koleksiyonda bilgi
araması gerc¸ekles¸tiren bir yapı tasarlanması hedeﬂenmekte-
dir.

Sonuc¸lar, g¨omme modelinin retrieval performansına
¨Ozellikle Google
do˘grudan etki etti˘gini g¨ostermektedir.
g¨omme modelinin kullanıldı˘gı Gemini
tabanlı sistemler,
genel olarak GPT-4o tabanlı pipeline’lara kıyasla daha
y¨uksek do˘gruluk sa˘glamıs¸tır. Aynı
retrieval mimarisiyle
yapılan kars¸ılas¸tırmalarda bile g¨omme modelinin farkı ortaya
c¸ıkmaktadır. ¨Orne˘gin Chroma + Kosin¨us yapılandırmasında
Gemini modeli (Google g¨omme) %96 do˘gruluk elde ederken,
GPT-4o (OpenAI g¨omme) %91’de kalmıs¸tır.Bu da g¨osteriyor
ki RAG sistemlerinin bas¸arısında yalnızca dil modeli ya da

REFERENCES

[1] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,

#### H. K¨uttler, M. Lewis, W.-t. Yih, T. Rockt¨aschel et al., “Retrieval-
augmented generation for knowledge-intensive nlp tasks,” Advances in
neural information processing systems, vol. 33, pp. 9459–9474, 2020.
[2] J. OpenAI Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya,

#### F. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al.,
“Gpt-4 technical report. arxiv,” arXiv preprint arXiv:2303.08774, 2023.
[3] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei,

#### N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale et al., “Llama
2: Open foundation and ﬁne-tuned chat models,” arXiv preprint

IEEE-UBMK-2025 International Conference on Computer Science and Engineering - 575
Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:08 UTC from IEEE Xplore. Restrictions apply.

arXiv:2307.09288, 2023.

[4] G. Team, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut,

#### J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican et al., “Gem-
ini: a family of highly capable multimodal models,” arXiv preprint
arXiv:2312.11805, 2023.

[5] A. Pal, L. K. Umapathi, and M. Sankarasubbu, “Med-halt: Medical
domain hallucination test for large language models,” arXiv preprint
arXiv:2307.15343, 2023.

[6] S. Bubeck, V. Chadrasekaran, R. Eldan, J. Gehrke, E. Horvitz, E. Ka-
mar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg et al., “Sparks of artiﬁcial
general intelligence: Early experiments with gpt-4,” 2023.

[7] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,

#### H. K¨uttler, M. Lewis, W.-t. Yih, T. Rockt¨aschel et al., “Retrieval-
augmented generation for knowledge-intensive nlp tasks,” Advances in
neural information processing systems, vol. 33, pp. 9459–9474, 2020.
[8] M. Cheng, Y. Luo, J. Ouyang, Q. Liu, H. Liu, L. Li, S. Yu, B. Zhang,

#### J. Cao, J. Ma et al., “A survey on knowledge-oriented retrieval-
augmented generation,” arXiv preprint arXiv:2503.10677, 2025.
[9] G. P. Wellawatte, H. Guo, M. Lederbauer, A. Borisova, M. Hart,

#### M. Brucka, and P. Schwaller, “Chemlit-qa: a human evaluated dataset
for chemistry rag tasks,” Machine Learning: Science and Technology,
vol. 6, no. 2, p. 020601, 2025.

[10] C. Wang, Q. Long, M. Xiao, X. Cai, C. Wu, Z. Meng, X. Wang,
and Y. Zhou, “Biorag: A rag-llm framework for biological question
reasoning,” arXiv preprint arXiv:2408.01107, 2024.

[11] M. Raja, E. Yuvaraajan et al., “A rag-based medical assistant especially
for infectious diseases,” in 2024 International Conference on Inventive
Computation Technologies (ICICT).

IEEE, 2024, pp. 1128–1133.

[12] N. Wiratunga, R. Abeyratne, L. Jayawardena, K. Martin, S. Massie,

#### I. Nkisi-Orji, R. Weerasinghe, A. Liret, and B. Fleisch, “Cbr-rag:
case-based reasoning for retrieval augmented generation in llms for
legal question answering,” in International Conference on Case-Based
Reasoning. Springer, 2024, pp. 445–460.

[13] R. Kalra, Z. Wu, A. Gulley, A. Hilliard, X. Guan, A. Koshiyama,
and P. Treleaven, “Hypa-rag: A hybrid parameter adaptive retrieval-
augmented generation system for ai legal and policy applications,”
arXiv preprint arXiv:2409.09046, 2024.

[14] A. Narimani and S. Klarmann, “Integration of large language models
for real-time troubleshooting in industrial environments based on
retrieval-augmented generation (rag).”

[15] A. Deshpande, V. Murahari, T. Rajpurohit, A. Kalyan,

and

#### K. Narasimhan, “Toxicity in chatgpt: Analyzing persona-assigned
language models,” arXiv preprint arXiv:2304.05335, 2023.

[16] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi,

#### C. Wang, Y. Wang et al., “A survey on evaluation of large language
models,” ACM transactions on intelligent systems and technology,
vol. 15, no. 3, pp. 1–45, 2024.

[17] V. Rawte, A. Sheth, and A. Das, “A survey of hallucination in large

foundation models,” arXiv preprint arXiv:2309.05922, 2023.

[18] Z. Jiang, F. F. Xu, L. Gao, Z. Sun, Q. Liu, J. Dwivedi-Yu, Y. Yang,

#### J. Callan, and G. Neubig, “Active retrieval augmented generation,” in
Proceedings of the 2023 Conference on Empirical Methods in Natural
Language Processing, 2023, pp. 7969–7992.

[19] G. Izacard, P. Lewis, M. Lomeli, L. Hosseini, F. Petroni, T. Schick,

#### J. Dwivedi-Yu, A. Joulin, S. Riedel, and E. Grave, “Few-shot
learning with retrieval augmented language models,” arXiv preprint
arXiv:2208.03299, vol. 1, no. 2, p. 4, 2022.

[20] S. Robertson, H. Zaragoza et al., “The probabilistic relevance frame-
work: Bm25 and beyond,” Foundations and Trends® in Information
Retrieval, vol. 3, no. 4, pp. 333–389, 2009.

[21] W. X. Zhao, J. Liu, R. Ren, and J.-R. Wen, “Dense text retrieval
based on pretrained language models: A survey,” ACM Transactions
on Information Systems, vol. 42, no. 4, pp. 1–60, 2024.

[22] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,

#### H. K¨uttler, M. Lewis, W.-t. Yih, T. Rockt¨aschel et al., “Retrieval-
augmented generation for knowledge-intensive nlp tasks,” Advances in
neural information processing systems, vol. 33, pp. 9459–9474, 2020.
[23] A. Topallı, “Ekobot: T¨urkc¸e destekli akıllı sanal akademik danıs¸man,”
International Journal of Advances in Engineering and Pure Sciences,
vol. 37, no. 2, pp. 196–205.

IEEE-UBMK-2025 International Conference on Computer Science and Engineering - 576
Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:08 UTC from IEEE Xplore. Restrictions apply.


---

> *End of P-03*

<br><br>

<a id="p04-----explainable-ai-for-software-engineering"></a>

## P-04 — Explainable AI for Software Engineering

| Field | Details |
|-------|---------|
| **Paper ID** | `P-04` |
| **Title** | Explainable AI for Software Engineering |
| **Authors** | Chakkrit Tantithamthavorn and Jirayus Jiarpakdee |
| **Affiliation(s)** | Faculty of Information Technology, Monash University, Melbourne, VIC, Australia |
| **Venue** | 36th IEEE/ACM International Conference on Automated Software Engineering (ASE) |
| **Volume / Year** | 2021 |
| **DOI** | [10.1109/ASE51524.2021.00009](https://doi.org/10.1109/ASE51524.2021.00009) |

---

2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE)

Explainable AI for Software Engineering

Chakkrit (Kla) Tantithamthavorn, Jirayus Jiarpakdee
Monash University, Melbourne, Australia.


### Abstract

The success of software engineering projects largely
depends on complex decision-making. For example, which tasks
should a developer do ﬁrst, who should perform this task, is
the software of high quality, is a software system reliable and
resilient enough to deploy, etc. However, erroneous decision-
making for these complex questions is costly in terms of money
and reputation. Thus, Artiﬁcial Intelligence/Machine Learning
(AI/ML) techniques have been widely used in software engineer-
ing for developing software analytics tools and techniques to
improve decision-making, developer productivity, and software
quality. However, the predictions of such AI/ML models for
software engineering are still not practical (i.e., coarse-grained),
not explainable, and not actionable. These concerns often hinder
the adoption of AI/ML models in software engineering practices.
In addition, many recent studies still focus on improving the
accuracy, while a few of them focus on improving explainability.
Are we moving in the right direction? How can we better improve
the SE community (both research and education)?

In this tutorial, we ﬁrst provide a concise yet essential
introduction to the most important aspects of Explainable AI and
a hands-on tutorial of Explainable AI tools and techniques. Then,
we introduce the fundamental knowledge of defect prediction (an
example application of AI for Software Engineering). Finally, we
demonstrate three successful case studies on how Explainable AI
techniques can be used to address the aforementioned challenges
by making the predictions of software defect prediction models
more practical, explainable, and actionable. The materials are
available at https://xai4se.github.io.


### Index Terms / Keywords

Explainable AI, Software Engineering


### I. Tutorial Outline

Our 1.5-hour tutorial consists of three parts:
- Part 1-Explainable AI: We ﬁrst provide a concise yet
essential introduction to the most important aspects of
Explainable AI and a hands-on tutorial of Explainable
AI tools and techniques.

- Part 2-Defect Prediction Models: We introduce the fun-
damental knowledge of defect prediction (an example
application of AI for Software Engineering)

- Part 3-Explainable AI for Software Engineering: We
demonstrate three successful case studies on how Ex-
plainable AI techniques can be used to address the
aforementioned challenges by making the predictions of
software defect prediction models more practical, ex-
plainable, and actionable.

Part 1: Introduction to Explainable AI

We ﬁrst provide a concise yet essential introduction to the
most important aspects of Explainable AI. At the beginning of
the tutorial, we will introduce the motivation, deﬁnitions, and
concept of Explainable AI. We will also discuss a theory of
explanations (e.g., what are the explainability goals, what are

the explanations, what are the types of intelligibility questions,
what are the scopes of explanations, what are the types of
explanations). We will also discuss the model-speciﬁc and
model-agnostic tools and techniques that are extensively-used
in the Explainable AI community (e.g., LIME [9], SHAP [5])
for explaining the predictions of AI/ML models with a hands-
on tutorial.

Part 2: Defect Prediction Models

In this part, we will ﬁrst introduce the fundamental knowl-
edge of defect prediction technologies. This include ﬁve key
steps (1) Data Collection, (2) Data Preprocessing, (3) Model
Construction, (4) Model Evaluation, and (5) Model Ranking,
along with the following empirical-grounded guidelines [10].
We describe details below.

(Step 1) Data Collection. Poor quality or noisy defect
datasets could lead to inaccurate predictions and insights. We
found that techniques for generating ground-truth data is often
not accurate, impacting the quality of defect datasets. Thus, we
will discuss how to: consider affected releases (i.e., the actual
software releases that are affected) to label whether a ﬁle is
considered to be defective or clean, instead of the assumptions
of a post-release window period (i.e., any defects that are ﬁxed
after 6 months) [17], while not to be concerned about issue
report misclassiﬁcation [12].

(Step 2) Data Analysis. Defect datasets are highly imbal-
anced with a defective ratio of <10%. Defect models trained
on class imbalance datasets often produce inaccurate models.
Our TSE’19 paper suggested to consider using optimised
SMOTE to improve the predictive accuracy, i.e., handling the
class imbalance of the training datasets prior to training the
defect models. Thus, we will discuss how to:

- Handle colliniearity and multicollinearity when interpret-
ing defect models (i.e., understanding what are the most
important variables) [2].

- Use AutoSpearman for handling collinearity and multi-
collinearity [3], and avoid using existing automated fea-
ture selection techniques (e.g., Stepwise Regression) if
the goal is to interpret defect prediction models, as they
fail to mitigate correlated features and are dependent on
random seeds [4].

(Step 3) Model Construction. There exist a large number
of off-the-shelf classiﬁcation techniques that can be used with
a large number of possible combination of hypereparameter
settings that can be conﬁgured. Sadly, practitioners often asked
which techniques and which settings should be used. Thus, we
will discuss how to:

978-1-6654-0337-5/21/$31.00 ©2021 IEEE
DOI 10.1109/ASE51524.2021.00009

1

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:59 UTC from IEEE Xplore. Restrictions apply.


- Explore various classiﬁcation techniques and hyperpa-
rameter settings. Optimised random forest and optimised
extreme gradient boosting trees often produce the most
accurate defect prediction models [13].

- Always optimize the hyperparameter settings of defect
prediction models (e.g., using Grid Search, Random
Search, Genetic Algorithm, Differential Evolution) [15].
- Use the Scott-Knott ESD test to identify the best clas-
siﬁcation techniques that are statistically signiﬁcantly
different with non-negligible Cliff’s |δ| effect size [14].
- Estimate the accuracy of defect prediction models using
out-of-sample boostrap model validation techniques when
defect datasets are very small (i.e., EPV < 10) [14].
- Using ANOVA Type-II for explaining the defect predic-
tion models (built using regression models), instead of
using ANOVA Type-I [2].

Part 3-Explainable AI for Software Engineering Including
Hands-on Examples

In this part, we will discuss three successful case studies
on how Explainable AI techniques can be used to address
the aforementioned challenges by making the predictions of
software defect prediction models more practical [6, 16],
explainable [1, 2], and actionable [7, 8, 11]. In particular,
the hands-on demo will focus on how to explain defect
prediction models in order to generate global explanations [2]
and instance explanations [1].


### II. Target Participants

The target participants of this tutorial

include: SE re-
searchers and PhD students who want to learn more about
the intersection of Explainable AI and Software Engineering.
Software practitioners who already use Python for as data
science, machine learning, research, and analysis and wish to
apply their data science knowledge to software data. Soft-
ware analysts and data scientists who want to understand
and avoid pitfalls when designing software analytics. Project
managers who involve high-stakes decision-making and need
software analytics to make smarter data-driven business de-
cisions. There are no prerequisites, no audio-visual, and no
pre-installed technical requirements for attending this tutorial.

III. INSTRUCTORS’ BIOGRAPHY AND EXPERTISE

Dr. Chakkrit (Kla) Tantithamthavorn is a Senior Lecturer
in Software Engineering and a 2020 ARC DECRA Fellow
in the Faculty of Information Technology, Monash University,
Australia. He is leading a new research area of Explaianble AI
for Software Engineering. His current fellowship is focusing
on the development of Practical and Explainable Analytics to
Prevent Future Software Defects. His work has been published
at several top-tier software engineering venues, such as TSE,
ICSE, EMSE, MSR, IST.
modelling, experimental design, and software engineering to
Dr. Jirayus Jiarpakdee is graduated from Monash Uni-
versity, Australia. His research interests include empirical
software engineering and mining software repositories (MSR).
The goal of his Ph.D. is to apply the knowledge of statistical

improve the explainability of defect prediction models. Con-
tact him at jirayus.jiar@gmail.com.

Acknowledgement. Chakkrit Tantithamthavorn was sup-

ported by ARC DECRA Fellowship (DE200100941).

REFERENCES

[1] J. Jiarpakdee, C. Tantithamthavorn, H. K. Dam, and J. Grundy, “An
Empirical Study of Model-Agnostic Techniques for Defect Prediction
Models,” IEEE Transactions on Software Engineering (TSE), p. To
Appear, 2020.

[2] J. Jiarpakdee, C. Tantithamthavorn, and A. E. Hassan, “The Impact of
Correlated Metrics on Defect Models,” IEEE Transactions on Software
Engineering (TSE), p. To Appear, 2019.

[3] J. Jiarpakdee, C. Tantithamthavorn, and C. Treude, “AutoSpearman:
Automatically Mitigating Correlated Software Metrics for Interpreting
Defect Models,” in Proceedings of the International Conference on
Software Maintenance and Evolution (ICSME), 2018, pp. 92–103.
[4] ——, “The impact of automated feature selection techniques on the in-
terpretation of defect models,” Empirical Software Engineering, vol. 25,
no. 5, pp. 3590–3638, 2020.

[5] S. M. Lundberg and S.-I. Lee, “A Uniﬁed Approach to Interpreting
Model Predictions,” in Advances in Neural Information Processing
Systems (NIPS), 2017, pp. 4765–4774.

[6] C. Pornprasit and C. Tantithamthavorn, “JITLine: A Simpler, Better,
Faster, Finer-grained Just-In-Time Defect Prediction,” in Proceedings of
the International Conference on Mining Software Repositories (MSR),
2021.

[7] C. Pornprasit, C. Tantithamthavorn, J. Jiarpakdee, M. Fu, and P. Thong-
tanunam, “PyExplainer: Explaining the Predictions of Just-In-Time
Defect Models,” in Proceedings of the 36th IEEE/ACM International
Conference on Automated Software Engineering (ASE), 2021.

[8] D. Rajapaksha, C. Tantithamthavorn, J. Jiarpakdee, C. Bergmeir,

#### J. Grundy, and W. Buntine, “SQAPlanner: Generating Data-Informed
Software Quality Improvement Plans,” IEEE Transactions on Software
Engineering (TSE), 2021.

[9] M. T. Ribeiro, S. Singh, and C. Guestrin, “Why should I trust you?:
Explaining the Predictions of Any Classiﬁer,” in Proceedings of the
International Conference on Knowledge Discovery & Data Mining
(KDD), 2016, pp. 1135–1144.

[10] C. Tantithamthavorn and A. E. Hassan, “An Experience Report on
Defect Modelling in Practice: Pitfalls and Challenges,” in In Proceedings
the International Conference on Software Engineering: Software
of
Engineering in Practice Track (ICSE-SEIP), 2018, pp. 286–295.
[11] C. Tantithamthavorn, J. Jiarpakdee, and J. Grundy, “Actionable analytics:
Stop telling me what it is; please tell me what to do,” IEEE Software,
vol. 38, no. 4, pp. 115–120, 2021.

[12] C. Tantithamthavorn, S. McIntosh, A. E. Hassan, A. Ihara, and K. Mat-
sumoto, “The Impact of Mislabelling on the Performance and Interpre-
tation of Defect Prediction Models,” in Proceeding of the International
Conference on Software Engineering (ICSE), 2015, pp. 812–823.
[13] C. Tantithamthavorn, S. McIntosh, A. E. Hassan, and K. Matsumoto,
“Automated Parameter Optimization of Classiﬁcation Techniques for
Defect Prediction Models,” in Proceedings of the International Con-
ference on Software Engineering (ICSE), 2016, pp. 321–332.

[14] ——, “An Empirical Comparison of Model Validation Techniques for
Defect Prediction Models,” IEEE Transactions on Software Engineering
(TSE), vol. 43, no. 1, pp. 1–18, 2017.

[15] ——, “The Impact of Automated Parameter Optimization on Defect
Prediction Models,” IEEE Transactions on Software Engineering (TSE),
pp. 683–711, 2018.

[16] S. Wattanakriengkrai, P. Thongtanunam, C. Tantithamthavorn, H. Hata,
and K. Matsumoto, “Predicting defective lines using a model-agnostic
technique,” IEEE Transactions on Software Engineering (TSE), 2020.

[17] S. Yathish, J. Jiarpakdee, P. Thongtanunam, and C. Tantithamthavorn,
“Mining Software Defects: Should We Consider Affected Releases?” in
In Proceedings of the International Conference on Software Engineering
(ICSE), 2019, p. To Appear.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:59 UTC from IEEE Xplore. Restrictions apply.

2


---

> *End of P-04*

<br><br>

<a id="p05-----explainable-artificial-intelligence-techniques-for-software-development-lifecycle-a-phase-specific-survey"></a>

## P-05 — Explainable Artificial Intelligence Techniques for Software Development Lifecycle: A Phase-Specific Survey

| Field | Details |
|-------|---------|
| **Paper ID** | `P-05` |
| **Title** | Explainable Artificial Intelligence Techniques for Software Development Lifecycle: A Phase-Specific Survey |
| **Authors** | Shashank Arora, Arvind Easwaran, and Abhishek Chaudhary |
| **Affiliation(s)** | Google, India |
| **Venue** | IEEE 49th Annual Computers, Software, and Applications Conference (COMPSAC) |
| **Volume / Year** | 2025 |
| **DOI** | — |

---

2025 IEEE 49th Annual Computers, Software, and Applications Conference (COMPSAC)

Explainable Artificial Intelligence Techniques for
Software Development Lifecycle: A Phase-specific
Survey

Lakshit Arora
lakshit@google.com

Aman Raj
amanraj@google.com

Sanjay Surendranath Girija
sanjaysg@google.com

Shashank Kapoor
shashankkapoor@google.com

Dipen Pradhan
dipenp@google.com

Google

Ankit Shetgaonkar
ankiit@google.com


### Abstract

Artificial Intelligence (AI) is rapidly expanding and
integrating more into daily life to automate tasks, guide decision-
making, and enhance efficiency. However, complex AI models,
which make decisions without providing clear explanations
(known as the “black-box problem”), currently restrict trust and
widespread adoption of AI.

Explainable Artificial Intelligence (XAI) has emerged to
address the black-box problem of making AI systems more
interpretable and transparent so stakeholders can trust,
verify,
and act upon AI-based outcomes. Researchers have developed
various techniques to foster XAI in the Software Development
Lifecycle. However, there are gaps in applying XAI techniques in
the Software Engineering phases. Literature review shows that
68% of XAI in Software Engineering research is focused on
maintenance as opposed to 8% on software management and
requirements.

In this paper, we present a comprehensive survey of the
applications of XAI methods such as concept-based explanations,
Local Interpretable Model-agnostic Explanations (LIME), SHapley
Additive
extraction, attention
mechanisms, counterfactual explanations, and example-based
explanations to the different phases of the Software Development
Life Cycle (SDLC), including requirements elicitation, design and
development, testing and deployment, and evolution.

exPlanations

(SHAP),

rule

To the best of our knowledge, this paper presents the first
comprehensive survey of XAI techniques for every phase of the
Software Development Life Cycle (SDLC). This survey aims to
promote explainable AI in Software Engineering and facilitate the
practical application of complex AI models in AI-driven software
development.


### Index Terms / Keywords

Software Engineering, Explainable Artificial

Intelligence, Trust, Transparency, Ethical Artificial Intelligence


### I. Introduction

Artificial

Intelligence

(AI)-aided software

techniques
supported by Large Language Models are rapidly transforming
software development with increased productivity [1]. AI-aided
Software Engineering is on the rise and is becoming vital to
deliver reliable, valid, and maintainable software systems
[2],[3]. However, trust and widespread adoption of AI are often
hindered by the “black-box” problem, where complex AI
models make decisions without providing
transparent
explanations for those decisions [5],[7]. Explainable Artificial
Intelligence (XAI) has emerged as a non-functional requirement

in AI systems to address this issue by improving the
interpretability and transparency of AI systems, allowing
stakeholders to trust, validate, and act upon AI-driven insights
[5],[9]. With the growing attention to XAI, it has become
challenging for practitioners and researchers to navigate and
select appropriate XAI methods and tools for their specific
applications [10].

Researchers have developed XAI methods for AI-aided
software development. However, this area remains understudied
[5],[11]. A blanket application of XAI to software engineering
is insufficient. Different software engineering phases require
tailored XAI techniques. For example, the literature reveals that
inconsistent XAI evaluation methods in software engineering
make it challenging to compare studies and XAI techniques
across different software engineering phases [7],[12]. This
disparity is evident in existing research, where studies indicate
that 68% of XAI in Software Engineering research focused on
the software maintenance phase versus 8% on the software
management and requirements [7].

such as Local

This paper aims to address the lack of XAI applications in
the Software Development Lifecycle and recommend ways to
apply it ethically and truthfully. We address this by finding XAI
methods
Interpretable Model-agnostic
Explanations (LIME), SHapley Additive exPlanations (SHAP),
and Rule Extraction, mixing and matching them to provide
key Software Engineering phases:
explainability
requirements elicitation, design and development, testing and
deployment, and evolution. The following research questions
guide the paper:

in

- RQ1: What are the key explainability challenges that AI

introduces in software engineering?

- RQ2: How can tailored XAI techniques for each software
engineering phase enhance the explainability of AI-aided
Software Engineering?

- RQ3: What are the limitations of existing XAI techniques

in Software Engineering?

A mixed-methods approach was employed to address these
research questions, combining a systematic literature review
(SLR) with a narrative review of relevant literature. The SLR
analyzed existing XAI in Software Engineering studies to
identify key themes, evaluate XAI methods, and identify
research gaps. Searches were conducted in IEEE Xplore, ACM
Digital Library, Science Direct, Wiley, Google Scholar, and
Scopus using keywords such as “XAI”, “Explainable Artificial

2836-3795/25/$31.00 ©2025 IEEE
DOI 10.1109/COMPSAC65507.2025.00321

2281


development stakeholders [27]. This leads to several limitations
during the requirements elicitation phase (e.g., ambiguity, lack
of tacit knowledge extraction, bias, etc.), design phase (lack of
creativity, lack of trade-off analysis, lack of contextual
awareness, etc.), code development phase (e.g., lack of
techniques for evaluating correctness, security vulnerabilities,
maintainability, etc.), and during the testing phase (e.g., test
oracle problem, test flakiness, scalability concerns, etc.
[3],[28]).

#### B. Explainable AI (XAI)

Explainability is gaining traction within AI communities as
a means to address the “black-box” problem, which stems from
a lack of transparency regarding how AI models operate and
their outputs [10],[29]. Explainable AI (XAI)
arrive at
techniques
and
to provide
understandable explanations on the complex decision-making
processes of machine learning models [5], [30]. Vilone and
Longo (2021) proposed a widely cited classification for XAI
methods [30], based on the following properties:

are designed

reasonable

- Stage of explainability: Refers to the period in the process
of generating outputs when a model generates the
explanation for the decision it provides. The authors
discuss two stages called Ante-hoc and Post-hoc. Ante-
hoc generates explanations for decisions from the
beginning of the training data while aiming to achieve
optimal performance, and Post-hoc, which provides
explanations after the model has been trained and made
predictions. Post-hoc can be either model-specific or
model-agnostic. Model-agnostic methods apply to any
model, while model-specific methods apply to specific
models.

- Scope of explainability: Refers to the extent of an
explanation produced by XAI methods. The scope can be
local or global, with local explaining only an instance of
inference to the user while global providing the entire
inference of the model to the user.

- Input and output: Refers to the format of the input and the
output that can be used by XAI techniques to explain the
model decision. The XAI technique utilizes the XAI
input to generate the explanation output. The XAI
methods need to understand the same kind of data that the
model itself uses. The most common forms of input
explanations are images, text, and vectors, while output
examples are numeric, rules, and visualizations.

In the following text, we present some of the most common
XAI techniques and provide a brief description incorporating the
stage, scope, and input/output properties. Figure 1 shows a brief
summarization and classification of standard XAI techniques.

1) Feature Attribution based techniques: These techniques
center around explaining predictions by assigning importance
or
tell
which features matter most. The most common feature
attribution based techniques are:

relevance scores

features. They

the input

to

- LIME

(Local

Interpretable

Model-agnostic
Explanations) [12],[31]: LIME is a post-hoc, model-
agnostic technique that explains individual predictions. It
works by approximating the complex model locally with

“Software

Engineering”,

Intelligence”,
“AI-aided
development”, “trust”, “transparency”, and “ethical AI”. The
Inclusion criteria focused on peer-reviewed articles published
within the last 6 years that addressed XAI in software
engineering. A narrative literature review complemented the
SLR to explore broader perspectives on XAI and Software
Engineering, which assisted in providing XAI techniques for
phase-specific Software Engineering. Through synthesizing
SLR and narrative review results, this paper proposes the first
comprehensive overview of XAI techniques tailored to each
Software Development Life Cycle (SDLC) phase.

The paper is structured as follows: Section 2 reviews the
literature on AI in Software Engineering, explainable AI, and
XAI in Software Engineering. Section 3 discusses the proposed
XAI techniques for each Software Engineering phase to improve
the explainability of AI-aided software development. Section 4
presents the discussion, and Section 5 concludes the paper with
recommendations and future research.


### II. Literature Review


#### A. AI in Software Engineering

AI applications within the Software Engineering process are
rapidly expanding and are considered significant, particularly
with the use of Generative AI for tasks like code generation
[21],[3]. Kokol (2024) conducted a comprehensive knowledge
synthesis to assess the current status of published literature in AI
in Software Engineering [11]. Martinez-Fernandz et al.
conducted a comprehensive study on software engineering for
AI-based systems, in which the authors did a systematic
literature review of software engineering practices followed in
AI-based systems [3]. Gorkem and Giray [22] conducted a study
on Software Engineering for Machine Learning (ML) systems
in which they outlined the misconception that sometimes arises
between Software Engineering for ML which refers to Software
Engineering approaches to developing ML or AI systems versus
ML for Software Engineering which deals with the use of ML
and AI in Software Engineering tasks [3]. This paper focuses on
the latter, examining explainable AI (XAI) for Software
Engineering to support the development of reliable, valid, and
maintainable software systems. Specific AI usages in Software
Engineering include:

- Requirements elicitation: Natural language processing
for document analysis, chatbots for elicitation, data
mining for user needs [11].

- Design and

implementation: System architecture
recommendations, user
interface and experience
generation, model selection, code generation, code
completion, and bug detection [11].

- Testing and Verification: Test case generation, test

prioritization, fault localization [25].

- Deployment and Monitoring: Performance evaluation,

failure detection, bias monitoring [25].
prediction,

- Maintenance:

Bug

refactoring

recommendations, and change impact analysis [25].
Despite demonstrated effectiveness and efficiency, for
example, correct code generation [21], AI adoption in Software
Engineering is often marred by the “black-box” phenomenon,
where AI outputs lack explanations understandable by software

2282


Figure 1: Summarizing and classifying common eXplainable AI (XAI) techniques.

It

for

the

that

data

using

perturbed

prediction.

a simpler, interpretable model (e.g., linear model or
decision tree). LIME generates new data points by
perturbing the input features of the instance to be
explained and then observing how the model's prediction
changes. It then trains a weighted linear model on top of
the instance,
and
resulting predictions. This local linear model’s weights
are used as explanations, stating the relevance of each
feature
can
specific
handle varying input types (e.g., tabular, text, images)
and typically outputs feature importance as output (e.g.,
numeric weights, or highlighted words/pixels). A
practical example of this technique would be explaining
why a particular image was classified as a “cat” by
highlighting
the pixels that contributed most to the classification.
- SHAP (SHapley Additive exPlanations): Messalas,
Andreas, et al. described SHAP as a post-hoc, model-
agnostic XAI technique based on game theory [17]. This
technique calculates Shapley values, which represent the
average marginal contribution of each feature to the
prediction
feature
combinations. SHAP values provide local explanations
(explanation of one prediction) and global explanations
(feature importance summary for the entire dataset). The
input can be anything, e.g., the input of the original
model. The output often features visualizable importance
scores (numeric). An example of this technique would be
explaining why a loan application was rejected by an AI
model, showing the contribution of each factor (income,
credit score, debt, etc.) to the rejection decision.

expected over

all possible

- Attention Mechanisms: These integrate into the model as
part of the model architecture, rather than post-hoc. They
are model-specific and occasionally used
in deep
learning models like Transformers for Natural Language
(NLP) and computer vision. Samek,
Processing

Wojciech, et al. (2016) in their research [16] showcased
how attention mechanisms provide a local explanation by
highlighting the input areas (e.g., words in a sentence,
regions in an image) the model is paying attention
to when making predictions. The output is attention
weights, typically viewed as a heatmap. An application
example of this method would be in machine translation,
where it shows which words the model is attending to in
the source sentence when translating each word in the
target sentence.

2) Instance based (or example based) techniques: These
methods show examples (either real or synthetic) to illustrate
the model's behavior. They explain "by analogy" or by showing
"what-if" scenarios. Common techniques include:

- Counterfactual Explanations

to

the

the

least modification

[19]: Counterfactual
explanations are a post-hoc, generally model-agnostic
method for local explanations. They show how the
model would make different predictions if certain input
features differed, giving "what-if" type responses. They
show
input
features, adequate to change the model's prediction to
a specified alternative. Input is a data point and the
point
model;
(same structure as input) that would result in a different
prediction. Mothilal, Ramaravind K., et al. (2020)
proposed a framework [4] for generating and evaluating
diverse
on
loan
determinantal point processes. Extending
application example, a counterfactual explanation could
indicate that a $10,000 boost in the applicant's income
would suffice for loan approval.

a transformed data

counterfactual

based
the

explanations

output

is

- Example-Based Explanations [10]: These are often post-
hoc and model-agnostic, although a few models like k-
nearest neighbor (k-NN) are inherently example-based.
These methods find similar cases in the training set or

2283


### III. Ai Applications, Xai Challenges & Xai Methods In
EACH SDLC PHASE

In this section, we will go over different phases of the
Software Development Lifecycle (SDLC). For each phase, we
will cover 1) the applications of AI in each phase, 2) the AI
explainability-related challenges in each phase, and 3) XAI
techniques tailored to each phase that could help address those
challenges. The SDLC is iterative; the stages often repeat
multiple times as the software evolves. This paper covers the
following SDLC phases:

- Requirement Elicitation: This phase involves discovering
the stakeholders' needs and constraints and establishing
what the software needs to do.
- Design: The design phase

the gathered
requirements and turns them into a blueprint for the
software. It involves creating the system architecture,
specifying data structures, algorithms, interfaces, and
modules, and outlining how the system will satisfy the
requirements.

takes

- Development (Implementation/Coding): This involves
coding and implementing the software according to the
design specifications. Developers transform the design
into a functional software product.

- Testing: In this phase, the software is tested to reveal
defects and ensure
the
specifications and requirements. There are several levels
of testing, including unit, integration, system, and
acceptance testing.

it functions according

to

- Deployment

and Monitoring: Deployment means
making the software available to use by releasing it to
users or deploying it into the production environment,
and monitoring means continuously
the
performance of the deployed system and collecting user
feedback.

tracking

- Maintenance and Evolution: This is the ongoing process
of modifying the software after it has been deployed to
correct faults, improve performance, or adapt to the
changing environment. It includes debugging, new
feature additions, and system updates.


#### A. Requirement Elicitation Phase

1) Most common AI Applications: A literature review from
2023 conducted by Cheligeer C et. al. demonstrated how AI
offers significant potential for automating and enhancing
requirements elicitation based on the analysis of existing
documents to infer key information and even create an initial
draft of requirements [2]. Natural Language Processing (NLP)
and Large Language Models (LLMs) can be utilized to
understand user requirements, identify contradictions, and
prioritize requirements [8],[28]. LLMs can also be used to
create and improve requirement specifications [15]. AI can also
assist in requirements elicitation by generating requirements
from high-level user
inputs or documents, eliminating
ambiguity and identifying missing information [7].

2) Most common AI Explainability (XAI) Challenges: XAI
challenges often emerge during requirement elicitation, where
appropriate XAI techniques can provide support:

produce counterfactual cases. The input is the trained
model. The output is a set of examples to clarify the
internal
representation of data. The scope can
be local (explaining a single prediction) or global
(representing the whole model).

3) Concept based techniques: These techniques go beyond
simple feature importance or examples and tries to explain in
terms of abstract concepts that the model has (implicitly or
explicitly) learned.

- Concept-Based Explanations [12]: These are typically
model-specific and post-hoc explanations and provide a
global explanation of the model. They try to discover
higher-level concepts that are driving the model’s
decisions. They work by discovering sets of inputs
activating portions of a model, developing a concept, and
measuring each discovered concept’s contribution to the
model’s prediction. The input is usually the trained
model, and the output describes the concepts involved,
usually with visualizations. An example of this type of
explanation would be determining that the concept
“striped” in an image dataset considerably influences the
classification of images into “zebra”. Yeh, Chih-Kuan, et
al. (2020) investigated concept-based explainability for
Deep Neural Networks
defining
completeness of concepts, proposed a method to discover
interpretable and complete concepts, and introduced an
approach to quantify concept importance [13].

(DNNs)

by

4) Rule based techniques: This method explicitly generates

rules for the model's logic.

- Rule Extraction [30]: These

techniques attempt to
extract human-readable rules from a trained model. These
rules state the model's decision-making process in an "if-
then" form. Both post-hoc (when applied to an existing
model) and ante-hoc (when the model is to be rule-based
from the start) are possible. The scope is typically global.
The aim is to create a simplified but interpretable model
for the decision process. The input is the trained model,
and the output is a collection of rules that approximate
the model’s decision-making. One of these methods is
exemplified by Guido Bologna by showing a rule
extraction technique [6] that has been applied to
ensembles of decision trees and neural networks.


#### C. XAI in Software Engineering

XAI in Software Engineering involves applying XAI
techniques to different Software Engineering phases and tasks.
A Comprehensive literature study conducted by A. H.
Mohammadkhani et. al. (2023) on XAI in Software Engineering
presented the following findings [7]:

- Software maintenance: SRL results show this phase is
most explored, with 68% of XAI applications in Software
Engineering.

- Software development: This phase comprises 16% of

XAI applications in software engineering.

- Software management and requirements: These two tasks
received less attention, but as reported in the studies
surveyed, each accounts for 8% of XAI applications.
- Other tasks: Software design and testing have not been

researched.

2284


recommending optimal ML models for specific tasks within the
system [3],[7].

2) Most common AI Explainability (XAI) Challenges: The
set of explainability challenges that arise during the design
phase are mostly justifying why certain architecture or design
pattern is recommended [3]. This includes highlighting the
trade-offs that AI considers, such as performance vs. security,
etc. Also, there might be areas where AI might be uncertain
while generating software design recommendations.

3) Most common & effective XAI Techniques: As per the
literature review, the most effective XAI techniques in
addressing XAI challenges include:

trade-off analysis

- Counterfactual Explanations: This is a firm fit for both
justification and
[5],[33],[35].
Counterfactuals directly answer the question, "What
would need to change in the input (requirements,
constraints) to get a different design recommendation?"
This makes them inherently good at showing trade-offs.
o Example:
a
system
microservices architecture because the requirements
emphasized scalability. If high performance was
prioritized instead, a monolithic architecture might
have been recommended."

recommended

"The

- Rule Extraction: If the underlying AI model making the
design recommendations is a decision tree or random
forest, rule extraction is highly suitable [7], [19]. The
rules directly show the decision-making logic.
o Example: "IF requirement_scalability = HIGH
AND requirement_maintainability = MEDIUM
THEN architecture = MICROSERVICES." The
rules are easy to understand and directly show the
trade-offs and the factors influencing the decision.
- Concept-Based Explanations: If the AI can be trained to
recognize and reason about high-level concepts (e.g.,
"scalability,"
then
concept-based explanations could be very effective [12],
[19]. However, this requires defining and identifying
relevant concepts, which can be challenging.
o Example: "The system chose a microservices
architecture because of its focus on the concept of
scalability."

#### C. Development Phase

"maintainability"),

"security,"

for

code generation,

1) Most common AI Applications: In the development (or
implementation/coding) phase of the SDLC, AI is primarily
used
code
summarization, and bug detection/repair [26]. AI can also be
used for code translation and refactoring. Essentially, AI
streamlines the coding process and assists developers by
automating repetitive tasks, suggesting code snippets, and
identifying potential errors [1].

completion,

code

2) Most

common

(XAI)
AI
Challenges: XAI-related challenges in this phase center mostly
around correctness and reliability. This includes understanding
why the AI made certain suggestions, so that developers can

Explainability

- Ambiguity and Incompleteness: Natural language is
inherently ambiguous, and requirements are often
incomplete. AI may misinterpret requirements or miss
crucial details. AI also might misunderstand ambiguous
or incomplete user statements, leading to incorrect
requirements. [28].

- Tacit Knowledge: Much knowledge about requirements
is tacit. Stakeholders have implicit knowledge that they
do not even realize they possess or cannot easily
articulate. AI struggles with this during requirement
elicitation because it needs concrete data [5].

- Bias and Fairness: Training data may contain biases,

leading to unfair requirements [7],[9].

3) Most common & effective XAI techniques: As per the
literature review, the most effective XAI techniques in
addressing XAI challenges include:

this

- LIME/SHAP can help by identifying which features of
existing systems [9] or user actions are most influential
in producing specific outcomes (e.g., user satisfaction,
task completion) [19]; such methods can even bring out
latent requirements. Suppose a feature repeatedly has a
high SHAP value for positive predictions. In that case,
it indicates that
is significant to users
feature
[12], even if they did not include it as a requirement.
SHAP values specifically could assist in detecting biases
by measuring the contribution of each feature to the
prediction, making it easier to identify if protected
attributes (such as race or gender, etc.) or proxies for
protected attributes are influencing the requirements.
LIME can also be used, but SHAP is generally preferred
for its stronger theoretical foundations. For instance,
analyzing user interactions with a mobile app prototype
using LIME/SHAP could reveal that users who complete
a key task often utilize a particular gesture or navigation
sequence. This could reveal an unspoken requirement for
that gesture or navigation flow, even though users did
not express it clearly through interviews or user studies.
- Counterfactual Explanations show how small changes to
input features affect the outcome. They can help
stakeholders understand the system's sensitivity and
identify potential trade-offs [9],[12]. This can be
particularly useful for clarifying ambiguous or vague
and evolving requirements. For instance, "If we add a
requirement for X, how will that affect the system's
ability to satisfy Y?" or "If we relax requirement Z, what
other requirements become feasible?"


#### B. Design Phase

1) Most common AI Applications: AI is used during the
design phase of software development for several purposes,
including architecture
recommendation, design pattern
selection, User Interface (UI) & User Experience (UX) design,
model selection, and code generation [8]. Specifically, AI can
suitable architectures based on
assist
requirements and constraints, suggesting proper design
interface mockups, and even
patterns, designing user

suggesting

in

2285


input value or a particular line of code was the primary
driver of the failure.

- Counterfactuals: These are particularly powerful for
justification [9][12]. They answer the question, "What
would need
to get
a different output?" In the testing context, this could
mean, "What small change to the test case would cause
it to pass (or fail)?".

to change

input

the

in


#### E. Deployment & Monitoring

1) Most common AI Applications: During the deployment
can
assist with
and monitoring stage of SDLC, AI
activities such as anomaly detection,
failure prediction,
performance analysis, and facilitating continuous integration
and delivery. Generative AI (GenAI) can be used for
and
monitoring against possible deployment
facilitating rollback strategies when needed, streamlining the
release process [26]. AI can be used for performance analysis by
analyzing metrics and making suggestions for enhancing
deployed software products. Measuring and collecting
performance metrics is the primary use of GenAI, providing
suggestions for improvement. [20].

anomalies

2) Most common AI Explainability (XAI) Challenges: AI
applications have several explainability challenges in the
SDLC's deployment and monitoring phase. If AI flags a
performance anomaly, what is the cause? Is it a genuine
problem, or a false alarm? Alternatively, understanding why the
AI flagged a particular log entry as suspicious. Why is AI
predicting a failure? What are the contributing factors? At the
same time, if AI is used for resource management and
optimization, it is important to know why AI made a particular
scaling, balancing, or allocation decision.

3) Most common & effective XAI Techniques: During the
literature review, the most effective XAI techniques in
addressing XAI challenges were found to be:

- LIME/SHAP (Feature Attribution): These can highlight
which performance metrics (CPU usage, memory,
latency, etc.) were most influential in triggering the
anomaly flag. This helps pinpoint the source of the
problem. If the AI is trained on log data, these can show
which words or phrases in the log entry were most
important for the "suspicious" classification. This helps a
human understand why it was flagged. LIME/SHAP can
reveal which input features (e.g., system state, recent user
actions, etc.) contributed most to the predicted failure.
This helps understand the causes and potentially prevent
the failure. LIME/SHAP can show which factors (e.g.,
current/predicted load, resource availability, etc.) drove
the scaling/balancing/allocation decision. This provides
transparency and allows for auditing.

- Counterfactuals: Extremely valuable for understanding

sensitivity and providing actionable insights.
o Explaining Performance Anomaly: "If the request
rate had been 20% lower, the anomaly would not
have been flagged."

o Explaining Suspicious Log Entry: "If the log entry
had not contained the phrase 'access denied', it would
not have been flagged."

ensure the generated code is functionally correct, secure, and
maintainable [23],[34].

3) Most Common & effective XAI Techniques: As per the
literature review, the most effective XAI techniques in
addressing XAI challenges include:

specific

- LIME/SHAP
(Feature Attribution): These model-
techniques [18-19] can be very helpful
agnostic
for debugging and
code
understanding
suggestions. They highlight which parts of the input
(e.g., the natural language prompt, the surrounding code
context) were most influential in generating a particular
line or block of code. This can help developers
understand why the AI made a specific suggestion. For
instance,
incorrect,
LIME/SHAP could show that a particular keyword
overly influenced the AI in the prompt, or that the AI
ignored a crucial part of the surrounding code.

if a generated

function

is

- Example based explanations and counterfactuals: These
for addressing

techniques are very well-suited
correctness and justification [9], [33].
o Examples: Showing similar, correct code snippets
from the training data can help developers understand
the learned patterns by the AI and feel confident
about the suggestions.

- Counterfactuals: These are particularly effective for
justification. They answer the question, "What would
have to vary in the input to get a different output?" This
can help developers understand the generated code's
sensitivity to changes in the requirements or context. For
example, "If you remove the requirement for thread
safety,
lock
mechanism."

the generated code would

lack

the


#### D. Testing

1) Most common AI Applications: AI in software
development testing can be utilized in numerous ways, from
test case generation to test prioritization, test oracle generation,
even metamorphic
fault
testing.
localization,
LLMs alone show promise
in test case generation, oracle
generation, and understanding existing tests [15].

and

2) Most common AI Explainability (XAI) Challenges: In the
testing phase of software development, the most common XAI
challenge is understanding why a particular test case failed.
Determining the expected output of a testcase (the "oracle") is
often difficult [3].

3) Most common & effective XAI Techniques: During the
literature review, the most effective XAI techniques in
addressing XAI challenges were found to be:

- LIME/SHAP (Feature Attribution) [18-19]: They show
which input features (parts of the test case, code being
tested, or execution context) were most influential in
leading to the model's prediction (pass/fail, specific
output, etc.). This helps understand why a test case failed
or produced a particular output. For instance, if a test
case fails, LIME/SHAP could highlight that a specific

2286


o Explaining Resource Management: "If the predicted
load were 10% lower, fewer servers would have
been allocated."


#### F. Maintenance & Evolution

1) Most common AI Applications: AI can greatly assist
during this phase, particularly through Large Language Models
(LLMs). AI can help identify and predict potential bugs or
vulnerabilities and even suggest or assist in developing a fix.
AI can create concise descriptions of what the code does to
make understanding and maintenance easy. AI can suggest
improvements in the structure and maintainability of the code.
AI can be further used to automatically produce or update
documentation to keep pace with code changes.

2) Most common AI Explainability (XAI) Challenges: Even
if an AI suggests a bug fix or a refactoring, developers need
to trust that the suggestion is correct and will not introduce new
problems. This is especially crucial in maintenance, where
changes can have cascading effects. Unquestioningly accepting
AI-generated changes is risky.

3) Most common & effective XAI Techniques: During the
literature review, the most effective XAI techniques in
addressing XAI challenges were found to be:

- LIME/SHAP: These can pinpoint the code elements that
the AI model associates with a bug, helping developers
focus their debugging efforts. They can also show the
most significant parts of the code in relation to the
summary generated, allowing developers to comprehend
more precisely why the summary was generated.

- Counterfactual Explanations: These explanations show
how the model's prediction would change if some input
features differed. They answer "what if" questions. They
are highly relevant for Bug Prediction/Fixing, answering
questions like "If this line of code were changed, would
the bug still be present?"

- Attention Mechanisms: Attention visualization can show
which parts of the input code are most relevant to the
generated summary, code, or translation.


### IV. Discussion

Explainable AI (XAI) is crucial for Software Engineering to
overcome the 'black-box' problem inherent in AI-aided software
development [18]. The application of XAI across various phases
increase
of Software Engineering promises
trust,
transparency, and
the AI-based software
development process [31]. Although AI techniques have been
proven to improve efficiency and decision-making, their non-
transparency typically hinders their use [9],[10]. Nevertheless,
even with advancements on XAI in software engineering, some
gaps remain to be addressed:

reliability

to

in

- The lack of standardized evaluation metrics for XAI
methods in software engineering makes it challenging to
compare and assess the effectiveness of different
methods. This gap hinders
the development of
explainable AI-driven
software by complicating
explanation quality assessment and comparison of XAI
methods across software engineering phases [7],[31]
- XAI methods are often ineffective in explaining the
behavior of advanced AI models, such as deep neural

networks. This shortcoming limits the development of
trustworthy AI-driven software systems by making it
difficult to understand the reasoning behind the model's
decisions and to identify potential biases or errors [3].
- Most XAI methods provide technical explanations that
humans cannot easily interpret. This gap hinders the
development of maintainable AI-driven software systems
because it becomes difficult for software engineers to
understand the AI system's behavior and to make changes
or updates accordingly [31].

- XAI methods often lack integration with software
development processes,
limiting practical use and
hindering the development of explainable, trustworthy,
and maintainable AI-driven systems. [32].

While existing research findings show that Software
Maintenance has received the most attention in XAI research
[22], this paper provides a comprehensive overview of XAI
techniques across all SDLC phases, particularly highlighting
opportunities in less-explored areas like requirements and
design. However, significant gaps remain in integrating XAI
into earlier stages of Software Engineering, such as
requirements elicitation and design [7]. Explainability can help
refine specifications, enhance requirement traceability, and
mitigate potential biases early in the development process
[28],[3].

One of this paper's key contributions is the comprehensive
Software Development lifecycle phase-specific summarization
of XAI techniques to improve explainability in Software
Engineering processes. This paper presents XAI techniques for
some of the key Software Engineering phases. Overall, through
this paper, we want to highlight the necessity of XAI infusion
the
across
explainability gap that would promote responsible AI-aided
software development [7],[31].

the Software Development Lifecycle

to fill


### V. Conclusion

are

and

Transparency

trustworthiness

functionally
imperative
in AI systems, particularly within Software
Engineering activities [7]. As AI continues to revolutionize
various domains, advancing XAI paradigms that elucidate these
systems' decision-making processes is critical [35]. Examining
XAI techniques in the different phases of Software Engineering
offers a fertile ground for addressing the inherent complexity in
this field [7].

Enabling explainability is vital for alleviating concerns
around reliability and ethical implications in AI systems, as
evidenced by numerous studies highlighting the necessity of
comprehensible outputs
for successful adoption of AI
within Software Engineering [32],[2].

The development of robust XAI tools capable of revealing
the decision-making processes of AI models will enhance user
confidence and facilitate broader acceptance of AI solutions
across diverse fields [35]. To the best of our knowledge, this is
the first work that presents a comprehensive overview of XAI
techniques tailored to each phase of the Software Development
Life Cycle (SDLC). By doing so, we aim to promote explainable
AI in Software Engineering and facilitate the practical use of
complex AI models in AI-driven software development.

2287


Future research needs to explore the optimal application of
the tested and realized XAI approaches in agile and DevOps
focused development paradigms. Also, research must aim to
formulate benchmarking structures that enable fair comparison
among XAI approaches to ensure a better fit with requirements
in real-world applications. This is essential in software
development for developing standard evaluation criteria for XAI
in Software Engineering to assess effectiveness uniformly
across all approaches [12].

REFERENCES

[1]


#### I. Baskhad and S. Tim, “Program Code Generation with Generative
AIs,” Algorithms, vol. 17, no. 2, 2024, doi: 10.3390/a17020062.

[2] Cheligeer C, et. al, Machine learning in requirements elicitation: a

literature review. Artificial Intelligence for Engineering Design, Analysis
and Manufacturing. 2022;36:e32. doi:10.1017/S0890060422000166

[3] S. Martínez-Fernández et al., “Software Engineering for AI-Based

Systems: A Survey,” ACM Transactions on Software Engineering and
Methodology, vol. 31, no. 2, pp. 1–59, Apr. 2022, doi:
10.1145/3487043.

[4] Mothilal, Ramaravind K., et al. “Explaining Machine Learning

Classifiers through Diverse Counterfactual Explanations.” Proceedings
of the 2020 Conference on Fairness, Accountability, and Transparency,
ACM, 2020, pp. 607–17. DOI.org (Crossref),
https://doi.org/10.1145/3351095.3372850.

[5] L. Chazette, et. al, “Explainable software systems: from requirements
analysis to system evaluation,” Requirements Engineering, 2022, doi:
10.1007/s00766-022-00393-5.

[6] Bologna, Guido. “A Rule Extraction Technique Applied to Ensembles of

Neural Networks, Random Forests, and Gradient-Boosted
Trees.” Algorithms, vol. 14, no. 12, Nov. 2021, p. 339. DOI.org
(Crossref), https://doi.org/10.3390/a14120339.

[7] A. H. Mohammadkhani et. al, “A Systematic Literature Review of

Explainable AI for Software Engineering,” arXiv.org, Feb. 2023, doi:
10.48550/arxiv.2302.06065.

[8] Hutchinson, Ben, et al. “Towards Accountability for Machine Learning
Datasets: Practices from Software Engineering and Infrastructure.”
Proceedings of the 2021 ACM Conference on Fairness, Accountability,
and Transparency, ACM, 2021, pp. 560–75. DOI.org (Crossref),
https://doi.org/10.1145/3442188.3445918.

[9] A. Bennetot et al., “A Practical tutorial on Explainable AI Techniques,”

ACM Computing Surveys, 2024, doi: 10.1145/3670685.

[10] T. Clement, et al, “XAIR: A Systematic Metareview of Explainable AI
(XAI) Aligned to the Software Development Process,” Machine
Learning and Knowledge Extraction, vol. 5, no. 1, pp. 78–108, Jan.
2023, doi: 10.3390/make5010006.

[11] K. Peter, “The Use of AI in Software Engineering: A Synthetic

Knowledge Synthesis of the Recent Research Literature,” Information,
vol. 15, no. 6, 2024, doi: 10.3390/info15060354.

[12] S. Ali et al., “Explainable Artificial Intelligence (XAI): What we know

and what is left to attain Trustworthy Artificial Intelligence,”
Information Fusion, 2023, doi: 10.1016/j.inffus.2023.101805.
[13] Yeh, Chih-Kuan, et al. "On completeness-aware concept-based

explanations in deep neural networks." Advances in neural information
processing systems 33 (2020): 20554-20565.

[14] P. J. Phillips et al., “Four Principles of Explainable Artificial

Intelligence,” null, 2021, doi: 10.6028/nist.ir.8312.

[15] Hou, Xinyi, et al. “Large Language Models for Software Engineering: A

Systematic Literature Review.” ACM Transactions on Software
Engineering and Methodology, vol. 33, no. 8, Nov. 2024, pp. 1–
79. DOI.org (Crossref), https://doi.org/10.1145/3695988.

[16] Samek, Wojciech, et al. “Evaluating the Visualization of What a Deep
Neural Network Has Learned.” IEEE Transactions on Neural Networks
and Learning Systems, vol. 28, no. 11, Nov. 2017, pp. 2660–73. IEEE
Xplore, https://doi.org/10.1109/TNNLS.2016.2599820

[17] Messalas, Andreas, et al. “Model-Agnostic Interpretability with Shapley

Values.” 2019 10th International Conference on Information,
Intelligence, Systems and Applications (IISA), IEEE, 2019, pp. 1–
7. DOI.org (Crossref), https://doi.org/10.1109/IISA.2019.8900669

[18] D. Minh, H. X. Wang, Y. F. Li, and T. N. Nguyen, “Explainable

artificial intelligence: a comprehensive review,” Artificial Intelligence
Review, pp. 1–66, Nov. 2021, doi: 10.1007/s10462-021-10088-y.
[19] Mersha, Melkamu, et al. “Explainable Artificial Intelligence: A Survey

of Needs, Techniques, Applications, and Future
Direction.” Neurocomputing, vol. 599, Sept. 2024, p. 128111. DOI.org
(Crossref), https://doi.org/10.1016/j.neucom.2024.128111.

[20] Simaremare, Mario, et al. “Exploring the Potential of Generative AI:
Use Cases in Software Startups.” Agile Processes in Software
Engineering and Extreme Programming – Workshops, edited by
Lodovica Marchesi et al., vol. 524, Springer Nature Switzerland, 2025,
pp. 3–11. DOI.org (Crossref), https://doi.org/10.1007/978-3-031-72781-
8_1.

[21] M. Merkel and J. Dorpinghaus, “A case study on the transformative
potential of AI in software engineering on LeetCode and ChatGPT,”
2025, doi: https://doi.org/10.48550/arXiv.2501.03639.

[22] Görkem Giray. 2021. A software engineering perspective on engineering
machine learning systems: State of the art and challenges. J. Syst. Softw.
180, C (Oct 2021). https://doi.org/10.1016/j.jss.2021.111031
[23] V. Hassija et al., “Interpreting Black-Box Models: A Review on

Explainable Artificial Intelligence,” Cognitive Computation, vol. 16, pp.
45–74, Aug. 2023, doi: 10.1007/s12559-023-10179-8.

[24] A. Nguyen-Duc et al., “Generative Artificial Intelligence for Software
Engineering -- A Research Agenda,” arXiv.org, Oct. 2023, doi:
10.48550/arxiv.2310.18648..

[25] F. A. Batarseh, R. Mohod, A. Kumar, and J. C. Bui, “The application of
artificial intelligence in software engineering: a review challenging
conventional wisdom,” Data Democracy, pp. 179–232, Jan. 2020, doi:
10.1016/b978-0-12-818366-3.00010-1.

[26] D. Russo, “Navigating the Complexity of Generative AI Adoption in
Software Engineering,” ACM Transactions on Software Engineering
and Methodology, 2023, doi: 10.1145/3652154.

[27] W. J. von Eschenbach and J. R. Warren, “Transparency and the Black
Box Problem: Why We Do Not Trust AI,” Philosophy & Technology,
pp. 1–16, Sep. 2021, doi: 10.1007/s13347-021-00477-0.

[28] C. Gao, X. Hu, S. Gao, X. Xia, and Z. Jin, “The Current Challenges of
Software Engineering in the Era of Large Language Models,” ACM
Transactions on Software Engineering and Methodology, 2025, doi:
10.1145/3712005.

[29] K. A. Eldrandaly, M. Abdel-Basset, M. Ibrahim, and N. M. Abdel-Aziz,
“Explainable and secure artificial intelligence: taxonomy, cases of study,
learned lessons, challenges and future directions,” Enterprise
Information Systems, Jul. 2022, doi: 10.1080/17517575.2022.2098537.

[30] G. Vilone and L. Longo, “Classification of Explainable Artificial

Intelligence Methods through Their Output Formats,” Machine Learning
and Knowledge Extraction, vol. 3, no. 3, pp. 615–661, Aug. 2021, doi:
10.3390/make3030032.

[31] W. Yang et al., “Survey on Explainable AI: From Approaches,

Limitations and Applications Aspects,” Human-Centric Intelligent
Systems, vol. 3, no. 3, pp. 161–188, Aug. 2023, doi: 10.1007/s44230-
023-00038-y.

[32] Z. U. Islam, “Software Engineering Methods for Responsible Artificial

Intelligence,” Adaptive Agents and Multi-Agent Systems, 2021, doi:
10.5555/3463952.3464248.

[33] A. Adadi and M. Berrada, “Peeking Inside the Black-Box: A Survey on
Explainable Artificial Intelligence (XAI),” IEEE Access, vol. 6, pp.
52138–52160, Sep. 2018, doi: 10.1109/access.2018.2870052.

2288


---

> *End of P-05*

<br><br>

<a id="p06-----extracting-domain-models-from-textual-requirements-in-the-era-of-large-language-models"></a>

## P-06 — Extracting Domain Models from Textual Requirements in the Era of Large Language Models

| Field | Details |
|-------|---------|
| **Paper ID** | `P-06` |
| **Title** | Extracting Domain Models from Textual Requirements in the Era of Large Language Models |
| **Authors** | Sathurshan Arulmohan, Marie-Jean Meurs, and Sébastien Mosser |
| **Affiliation(s)** | (1) Department of Computing and Software, McMaster University, Hamilton, ON, Canada<br>(2) UQAM, Montréal, QC, Canada |
| **Venue** | ACM/IEEE International Conference on Model Driven Engineering Languages and Systems Companion (MODELS-C) |
| **Volume / Year** | 2023 |
| **DOI** | [10.1109/MODELS-C59198.2023.00096](https://doi.org/10.1109/MODELS-C59198.2023.00096) |

---

2023 ACM/IEEE International Conference on Model Driven Engineering Languages and Systems Companion (MODELS-C)

Extracting Domain Models from Textual
Requirements in the Era of Large Language Models

Sathurshan Arulmohan
McMaster University
CAS & McSCert
Hamilton, Canada
arulmohs@mcmaster.ca

Marie-Jean Meurs
Universit´e du Qu´ebec `a Montr´eal
CIRST
Montreal, Canada
meurs.marie-jean@uqam.ca

S´ebastien Mosser
McMaster University
CAS & McSCert
Hamilton, Canada
mossers@mcmaster.ca


### Abstract

Requirements Engineering is a critical part of the
software lifecycle, describing what a given piece of software
will do (functional) and how it will do it (non-functional).
Requirements documents are often textual, and it is up to
software engineers to extract the relevant domain models from
the text, which is an error-prone and time-consuming task.
Considering the recent attention gained by Large Language
Models (LLMs), we explored how they could support this task.
This paper investigates how such models can be used to extract
domain models from agile product backlogs and compare them
to (i) a state-of-practice tool as well as (ii) a dedicated Natural
Language Processing (NLP) approach, on top of a reference
dataset of 22 products and 1, 679 user stories. Based on these
results, this paper is a ﬁrst step towards using LLMs and/or
tailored NLP to support automated requirements engineering
thanks to model extraction using artiﬁcial intelligence.


### Index Terms / Keywords

Domain Modeling, Natural Language Process-
ing, Large Language Models, Concept Extraction, User stories


### I. Introduction
Requirements Engineering (RE) is essential to the software
lifecycle. RE is a spectrum between two extremes: included
as an early step in the waterfall/V-cycle models or advocated
as an on-the-ﬂy activity by the Agile community (e.g., with
user stories backlogs). In both cases, requirements artifacts are
produced using natural language to express the requirements
to which the software under construction must conform.

It is up to the requirement engineers to adequately capture
such requirements from stakeholders and “formalize” them
(e.g., with use case models in UML and associated scenar-
ios, formal speciﬁcations, or a product backlog according to
agile methods). Then, software designers have to translate
these artifacts (which mainly consist of natural language) into
actionable design artifacts. This step is tricky, as ambigui-
ties/conﬂicts can exist despite all efforts put into the RE step.
This is where modelling and Natural Language Processing
(NLP) come to help [1]: automated techniques can help extract
models from these natural language artifacts [2]. By removing
“noise” and increasing “signal”, software engineers can focus
on the abstracted models to identify ambiguities, conﬂicts
and validate the completeness of requirements concerning the
involved stakeholders. Consequently, the automated support

This work is funded by the Natural Sciences and Engineering Research
Council of Canada (NSERC) under the Discovery Grant (DG) program and
McMaster’s Faculty of Engineering (Excellence in Research Award)

of model extraction from requirements artifacts is essential to
provide good support for engineers.

Recently, Large Language Models (LLMs) such as GPT [3]
and conversational agents such as ChatGPT [4] started to claim
to be breakthrough enablers for various tasks, including soft-
ware development. In this paper, we propose to investigate
how LLMs and conversational agents can support model
extraction from requirements, focusing on agile backlogs
as these are, in essence, only based on textual artifacts written
in natural language. We leverage here our expertise gained
in previous work on model composition for requirement ar-
tifacts [5]. We start by giving a comprehensive background
on such backlogs and deﬁning a baseline for evaluation using
a reference dataset for backlogs and an extraction tool from
the state of practice in SEC. II. We then describe how GPT-
3.5 can be used in conversational mode to support such a
task SEC. III, and SEC. IV does the same using a tailored
approach developed with NLP experts. In SEC. V, we evaluate
how the three approaches compare to each other, and SEC. VI
concludes this paper.


### II. Background: Agile-Driven Requirements

This paper focuses on agile backlogs to support require-
ments deﬁnition. As motivated in the previous section, this
choice is driven by multiple factors. First, being a mainstream
approach to express requirements in open-source software,
it gives us access to reference requirements,
like the one
compiled by Dalpiaz et al. [6] in 2018. Despite this paper
focusing on agile backlogs, it would be easy to transfer the
experimental contribution to classical requirements documents
and compare the result with other tooling, depending on the
availability of such data. We emphasize that our focus here
is to support the accessibility of the datasets and tools (see
SEC. V) to support reproducibility, and, as a consequence, we
ruled out of scope any dataset or tooling that would rely on
proprietary/conﬁdential information.


#### A. Related Work

A survey was published in 2021 by Zhao et al. [7] to answer
several questions, such as “What is the focus of NLP4RE
research?” (RQ3) and “What is the state of tool development
in NLP4RE research?” (RQ4). 64.59% of the studies were
working on requirement speciﬁcation as input. Among 370

979-8-3503-2498-3/23/$31.00 ©2023 IEEE
DOI 10.1109/MODELS-C59198.2023.00096

580

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.


NamedElement

name:(cid:0)String

LEVEL

PRIMARY
SECONDARY

Product

Persona

*

Backlog

*

Entity

level:(cid:0)LEVEL

*

Story

0..1

Benefit

identifier:(cid:0)int

text:(cid:0)String

triggers

Action

targets

text:(cid:0)String
level:(cid:0)LEVEL

Fig. 1. Metamodel for Agile Backlogs Domains

studies, they identiﬁed 59 studies related to modelling and
63 related to extraction (RQ4). From a tooling perspective,
they have identiﬁed 130 tools used in their collected studies.
Among this set, modelling tools represent 34 tools, and
extraction tools 24, representing 44% of the available tooling.
In total, 140 different NLP techniques are used in the corpus
of tools identiﬁed in this survey.

As the survey was published in a pre-GPT world, none
of the studies considered GPT per se, and only a few used
LLMs such as BERT. Since LLMs became popular, we
can see some preliminary results published as pre-prints or
conference papers. This paper mainly focuses (so far) on
recommendations more than extraction, such as the work
by Weyssow et al. [8] used to recommend concepts during
modelling. Related to extraction, Bajaj et al. [9] concludes that
GPT-3 outperforms classical tools from the state of practice
concerning use case extraction. These preliminary results seem
promising, so investigating how LLMs can be used to support
extraction seems legit.


#### B. Processing User stories Backlogs

According to agile methods, requirements are written as a
prioritized set of user stories, organized in a product backlog.
A story represents, using natural language, a tuple containing
the following information: (i) the persona involved in the story,
(ii) the actions this persona will perform on the system, (iii) the
entities involved in the actions, and, optionally, (iv) a beneﬁt
obtained by the persona after having completed these actions.
Classically, user stories are expressed using the Connextra
Template [10], under the form: “As a <PERSONA>, I can
<ACTIONS over ENTITIES>, so that <BENEFIT>”. Even
if other templates exist, stories following template-based writ-
ing simplify the concept extraction tasks. In FIG. 1, we depict
the associated metamodel to represent a product backlog. It is
important to note that this paper focuses on concept extraction
according to this metamodel.

To support the product development phase, extracted con-
cepts are classically organized into analysis and design models

(e.g., class diagrams, sequence diagrams) [11]. We consider
these post-extraction transformations out of scope and focus
our contribution on the extraction task. By extracting personas,
actions and entities, tools can transform the extracted material
into their chosen domain model representation using ontolo-
gies or domain-oriented class diagrams.


#### C. Annotating User Stories as a Ground Truth

Considering our choice of only using publicly available re-

quirements, we focused on the dataset published by Dalpiazet
al.. It contains 22 product backlogs and 1, 679 user stories that
the requirements engineering community curated. The dataset
is published as a raw archive, i.e., an archive of 22 text ﬁles,
each containing the user stories associated with the product
it describes, one per line. To the best of our knowledge, no
publicly available expert-based annotation establishes a ground
truth for the different concepts described in the dataset.

As a consequence, we ﬁrst started by manually annotating
the dataset, using the Doccano1 platform, as a Named Entity
Recognition task. We loaded the different labels (i.e., Persona,
Action, Entity, Beneﬁt) and two relations (i.e., triggers, targets)
used in out domain metamodel, as depicted in FIG. 2.

The annotation process was the responsibility of the 1st
author. To ensure the quality of the annotated set, we intro-
duced several cross-checks: (i) an initial calibration was done
in collaboration with the 3rd author on 75 stories randomly
sampled, (ii) validation meetings were held on a bi-weekly
basis over two months during the annotation phase, and
(iii) the 3rd author cross-checked manually 330 randomly
sampled annotated stories (19.6%). No signiﬁcant deviations
were found during this step, as only 21 stories containing (mi-
nor) disputable elements were identiﬁed, leading to an inter-
rater agreement of 94% for this sample, which is classically
considered as excellent. In case of signiﬁcant disputes, the 2nd
author would have acted as an external referee and, as such,
was kept out of the annotation process (SEC. V-C). Overall,
the annotation phase lengthed two months, and consumed in
total 10 days for the 1st author, and 1.5 days for the 3rd author
(not counting the bi-weekly meetings). The produced ground
truth is available as part of our open-data repository [12].


#### D. Creating a Baseline from the State of Practice

We complemented the ground truth by running Visual
Narrator (VN [11]) on top of the dataset and obtaining a
baseline from the state of practice. VN is an open-source
software designed to explicitly extract conceptual models from
user stories backlog. For each story,
it extracts (using an
ontological approach) the same elements as the ones described
in our domain metamodel. We ran VN on top of the provided
backlogs and extracted the concepts it extracts by parsing the
output ﬁles it produces. Internally, VN relies on spaCy [13] for
natural language processing, using the en_core_web_md
model for English. The tool also leverages the Connextra

1https://doccano.herokuapp.com/

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

581

This story is extracted from backlog #02. In this backlog, “user testing” is a ﬁrst-class entity understood as a synonym for “test reports summary”.

Fig. 2. Example of annotated user story using Doccano Annotation UI

template by looking for special keywords2 (e.g., “As a”) to
guide its extraction process.

After this step, we obtain a new annotated dataset containing
the results of a domain model extraction on top of the input
corpus.

III. A CONVERSATION WITH (CHAT)GPT 3.5

We experimented with ChatGPT to ﬁnd the best way
to extract the information from a user story backlog in a
“rapid prototyping” way. When we obtained satisfying results
through the Web interface, we translated the prompts we were
using into calls to the API and used a backlog of 25 stories
to run the extraction and manually check the results. The
following section describes in a step-by-step way how we
ended up prompting GPT the way we did for the experiment,
as we defend it is part of the contribution of this paper to
describe how LLMs can be interacted with to obtain results.


#### A. Prompt Engineering

Initially, we designed the extraction as a batch approach:
we asked the GPT agent to extract concepts, categories and
relations from a set of stories. After explaining the extraction
task to the agent, we provided a complete backlog with the
hope that this comprehensive vision of the backlog would
support good results. Unfortunately, this faced two immediate
limitations. First, a query (prompt plus response) to the GPT
API is limited to 4, 097 tokens, representing an average of
3, 000 words. This limit is not a problem for ongoing product
backlogs (which are classically maintained below 100 stories3
by product owners) but would become one if someone is
interested in extracting information from legacy software. The
second issue was identiﬁed during the manual quality check.
With this approach, the agent was fabricating data (i.e., the
so-called “hallucinations”), for example, by mixing elements
between stories. The response would claim that story Si refers
to Persona Pj, even if the story does not mention Pj. In some
cases, Pj was not even mentioned anywhere in the backlog.
this, we entered a second iteration of prompt
engineering. Both problems seemed triggered because we
provided the agent with a complete backlog. Consequently, we
transformed our prompt approach for the following: provide
stories one by one, ask GPT to extract concepts, categorize
them, and extract relations for each story independently. This
approach drastically limited “hallucinations”, as the answer

To limit

2https://github.com/MarcelRobeer/VisualNarrator/blob/master/lang/en/

indicators.py

3https://resources.scrumalliance.org/Article/

scrum-anti-patterns-large-product-backlog

mainly referred to elements in the provided story. It also ﬁxed
the request length issue. Unfortunately, it does not produce
usable results. GPT produced texts that did not respect the
input constraints (we tried JSON or CSV) and mixed up things,
e.g., categorizing an entity as a persona. When not constrained,
each request led to a different output format (e.g., the CSV row
was named Entities, Entity, and positioned at different
places). When constrained, the system was not following the
instructions, mixing up rows and concepts.

To make this more straightforward and usable, we started
investigating the function calls mechanisms introduced in
gpt-3.5-turbo-0613. This version of GPT 3.5 was re-
leased on June 13, 2023. It became the standard version
for GPT 3.5 on June 27, 2023. Function calls are designed
in the API to give control to the output produced by the
system. Developers can provide a JSON schema to model their
response, and the system will use this schema and “ﬁll in the
blanks” instead of regular text generation. For example, if one
expects their answer to be an array of strings containing the
name of the personas, they can provide a schema inside their
request, and GPT will use it as output format (as in LST. 1,
lines 3 → 12). An example of such a constrained response
is described in LST. 2. Instead of providing a content, the
agent answers with a function_call, providing its name
and how it should be called (arguments). When the engine
uses a function call as an answer, the conversation is immedi-
ately ended ("finish_reason": "function_call").
Consequently, obtaining a sequence of calls using this tech-
nique is impossible, as the engine will stop once a call is
returned in the answer.

Given this limitation, we faced two options: (i) deﬁning
a large schema containing all
the information we wanted
to extract from a user story, or (ii) engaging in a conver-
sation with the model. Without surprise, the ﬁrst approach
was inconclusive, as GPT was mixing up elements in the
way it was ﬁlling in the blanks of the schema (e.g., using
personas as entities or, more surprisingly, as actions). As this
API is designed conversationally, we opted for the second
approach. We ﬁnally designed the processing of each story as
a conversation with the model, with each answer constrained
by a dedicated (and smaller) schema [14].


#### B. Extracting domain models with GPT 3.5

Building on the different approaches described in the previ-
ous section, we used the following protocol to extract concepts
from user stories. We handle each story independently, and
for each story, we engage in a conversation with GPT 3.5 and

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

582

4

5

6

7

8

9

10

11

12

13

14

1 {
2

3

4

5

6

7

8

9

10

11

12
13 }

1 response = openai.ChatCompletion.create(
model = "gpt-3.5-turbo-0613",
2
functions = [ # constraining GPT with a schema

3

{ "name": "record_elements", # Function to be called in the response

"description": "Record the elements extracted from a story",
"parameters": { # Signature description

"type": "object",
"properties": {
"personas": {

"type": "array",
"description": "The list of personas extracted from the story",
"items": { "type": "string" }}}],

messages = conv,
temperature=0.0) # To make the answer deterministic (as much as possible)

Listing 1. Calling GPT 3.5 and specifying a function call argument

...
"choices": [{

"index": 0, "message": {
"role": "assistant", "content": null,
"function_call": {

"name": "record_elements",
"arguments":

"{\"personas\": [\"repository manager\"]}"

}},

"finish_reason": "function_call"}],
...

Listing 2. Example of answer from the API (execution of LST. 1)

constrain its responses using the function call mechanism. We
have organized the conversation into four phases:

1) Setup. First, we impersonate the system role and ask the
engine to adopt a persona. We describe the global task
that will be asked later to set up the request execution
context.

2) Concepts. Still using the system role, we now specify
with more detail the task to extract personas, entities,
actions and beneﬁts from a story. We then provide an
example of such an extraction using one of our manually
annotated stories. Finally, switching to user role, we
provide the <STORY> to process.

3) Categorization. As the model is stateless, we have to
inject the answer from the previous phase into the con-
versation. Thus, we impersonate the assistant role and
add a conversation entry describing the <CONCEPTS>
previously obtained. Following the same pattern as in the
previous phase, we describe the task using the system
role (categorizing primary and secondary actions and
entities) and provide an example of such an execution.
4) Relations. The ﬁnal step uses the same pattern. We ﬁrst
inject the <CATEGORIES> as the assistant, and then
describe the task and provide an example as the system.

As of June 2023, OpenAI lists as best practices six strategies
and 17 tactics4 to support prompt engineering. The conversa-
tion we used is described in TAB. I and follows the relevant
OpenAI tactics. We implemented (see TAB. II) completely
seven of the provided guidelines ((cid:2)), three partially (∼), and
the remaining seven were not relevant to our problem (NA).
The complete code is available on GitHub [14].

4https://platform.openai.com/docs/guides/gpt-best-practices


#### C. Discussion & Lessons learned

In this section, we only discuss the technical dimensions of
using the GPT 3.5 API to support the extraction task. We will
discuss the quality of results in SEC. V.

- Ease of use. Based on the available documentation
interacting with GPT
and documented best practices,
3.5 is straightforward and does not require specialized
programming skills: basic Python programming skills are
sufﬁcient. Using ChatGPT to support fast prototyping is
also very helpful, as it allows one to quickly interact with
the LLM in a trial/error way.

- Privacy. Being a hosted LLM, each story processed
by GPT 3.5 is sent to OpenAI. For a publicly avail-
able dataset, it might not be considered an issue, but
this should be considered for backlogs containing pro-
prietary information (usually the case for commercial
products). OpenAI enacted (05/23) a policy stating that
they are no longer using users’ data for upcoming train-
ing/improvements of their model. This policy might not
be sufﬁcient for some sovereign data, for example. This
can be mitigated by deploying an on-premise LLM.
- “Hallucination”. Being a stochastic parrot [15] by de-
sign, GPT does not understand the concepts it extracts.
Thus, even if careful prompt engineering can limit this
phenomenon, it commonly misuses concepts, e.g., con-
sider an element a persona and then an entity, despite
these two being exclusive concepts.

- JSON Schema. Constraining the answer to ﬁt a given
JSON schema helps support the automation of extracted
data. Out of 5, 193 calls to the model required to process
our backlog dataset, only two responses (0.03%) were
invalid JSON. An inconvenient of the approach is that it
complexiﬁes the interactions with the model and requires
more programming skills. We also encountered some sit-
uations where the generated JSON document was missing
elements (e.g., in a relation, the kind of relation –trigger
or target– was not speciﬁed).

- Cost. ChatGPT, used for prototyping, is free to use. When
calling the API, you need a valid account, and the system
invoices users on a pay-as-you-go. As of June 23, the
chat completion API (gpt-3.5-turbo) is offered for
$0.0015/1k input tokens. Processing the whole dataset
consumed 2, 228, 162 input tokens (85%) and produced
387, 324 completions tokens as output (15%). The overall

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

583

TABLE I
PROMPTS USED TO EXTRACT CONCEPTS FROM USER STORIES USING GPT-3.5

Phase

Setup

Concepts

Categorization

Relations

System

System
System

Role
System
System

Prompt
You are a requirements engineering assistant specialized in agile methods and backlog management.
You will be provided by the user a user story, and your task is to extract elements from these models
and call provided functions to record your ﬁndings.
You are only allowed to call the provided function in your answer.
The elements you are asked to extract from the stories are the following: Persona, Action, Entity,
and Beneﬁt. A Story can contain multiple elements in each category.
Here is an example. In the story ’As a UI designer, I want to begin user testing, so that I can
validate stakeholder UI improvement requests’, the Persona is ’UI designer’. The actions are ’begin’
and ’validate’. The entities are ’user testing’ and ’stakeholder UI improvement requests’. The beneﬁt
is ’I can validate stakeholder UI improvement requests’.
Here is the story you have to process: <STORY>
Assistant Here are the extracted concepts: <CONCEPTS>
System

You now need to make the difference between primary concepts and secondary concepts in the
information you have extracted.
In the example that was given initially, the actions primary action is ’begin’ and the secondary
one is ’validate’. The primary entity is ’user testing’ and the secondary entity is ’stakeholder UI
improvement requests’.

System

User

Assistant Here is the categorization: <CATEGORIES>
System

System

You now need to extract relationships betwen personas and actions (named trigger), and between
actions and entities (named target).
In the example that was given initially, the persona ’UI designer’ triggers the action ’begin’, and the
action ’begin’ targets the entity ’user testing’.

TABLE II
OPENAI’S TACTICS TO SUPPORT PROMPT ENGINEERING (JULY 2023)

T2
T3

Strategy #1: Write clear instructions
T1

Include details in your query to get more relevant
answers
Ask the model to adopt a persona
Use delimiters to clearly indicate distinct parts of
the input
Specify the steps required to complete a task
Provide examples
Specify the desired length of the output

T4
T5
T6
Strategy #2: Provide reference text
T7
T8

Instruct the model to answer using a reference text
Instruct the model to answer with citations from a
reference text

T10

Strategy #3: Split complex tasks into simpler subtasks
T9
Use intent classiﬁcation to identify the most relevant
instructions for a user query
For dialogue applications that require very long
conversations, summarize or ﬁlter previous dialogue
Summarize long documents piecewise and construct
a full summary recursively

T11

Strategy #4: Give GPTs time to “think”
T12

Instruct the model to work out its own solution
before rushing to a conclusion

T13 Use inner monologue or a sequence of queries to

hide the model’s reasoning process

T14 Ask the model if it missed anything on previous

passes

Strategy #5: Use external tools
T15 Use embeddings-based search to implement efﬁcient

knowledge retrieval

T16 Use code execution to perform more accurate cal-

culations or call external APIs
Strategy #6: Test changes systematically
T17

Evaluate model outputs with reference to gold-
standard answers

(cid:2)

(cid:2)
(cid:2)

(cid:2)
(cid:2)
NA

∼
NA

(cid:2)

(cid:2)

NA

NA

∼

NA

NA

NA

∼

584

cost to analyze the 1, 679 stories in the corpus is $4.12
(USD), which can be considered neglectable.

- Reliability. Interacting with the model at scale required
more engineering than the documentation described.
While running the experiment, we encountered server-
side errors (e.g., BadGateway – HTTP 502, ServiceU-
navailableError – HTTP 500) with a 2.78% rate: out of
5, 193 calls, 144 were in error. To ﬁx this, we introduced
a Circuit Breaker5 in the code. Introducing such a pattern
makes the code more complex and requires some solid
programming skills.

- Response time. When processing the ﬁrst backlogs, we
encountered a response time of up to 45 minutes for a
single request. We ﬁxed this by manually introducing a
client-side timeout mechanism, voluntarily interrupting
a call if it took more than 30 seconds. It drastically
improved the time required to process the upcoming
backlogs to the cost of a more complex code. Processing
the complete dataset consumed 200 minutes and six
seconds, equivalent to almost three hours and a half, with
no training required.


### IV. Using A Dedicated Nlp Approach (Crf)

Before jumping to conclusions, we decided to include in
the comparison of the results an upper limit, being a dedicated
Natural Language Processing (NLP) approach, by teaming up
with an NLP group (represented by the 2nd author).

Where VN combines rule-based extraction and spaCy lan-
guage model, it misses the point that extracting domain models
from user story backlog can be modelled as a contextualized
pattern recognition task. This representation allows us to use
approaches known for being more efﬁcient and accurate. The

5https://martinfowler.com/bliki/CircuitBreaker.html

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

fact that we built a ground truth of 1, 679 user stories also
allows us to rely on supervised learning approaches.


#### A. Introducing Conditional Random Fields (CRF)

CRFs [16] are a particular class of Markov Random Fields,
a statistical modelling approach supporting the deﬁnition of
discriminative models. They are classically used in pattern
recognition tasks (labelling or parsing) when context is im-
portant to identify such patterns.

To apply CRF to our task, we need to transform a given
story into a sequence of tuples. Each tuple contains minimally
three elements: (i) the original word from the story, (ii) its
syntactical role in the story, and ﬁnally (iii) its semantical role
in the story. The syntactical role in the sentence is classically
known as Part-of-Speech (POS), describing the grammatical
role of the word in the sentence. The semantical role plays
a dual role here. For training the model, the tags will be
extracted from the annotated dataset and used as target. When
used as a predictor after training, these are the data we will
ask the model to infer. Consider the following example:
S = [’As’, ’a’, ’UI’, ’designer’, ’,’, . . .]
(1)
P OS(S) = [ADP, DET, NOUN, NOUN, PUNCT, . . .]
(2)
Label(S) = [∅, ∅, PERSONA, PERSONA, ∅, . . .]
(3)
S represents a given user story (FIG. 2). P OS(S) represent
the Part-of-speech analysis of S (here using spaCy, the same
library used by Visual Narrator). The story starts with an
adposition (ADP), followed by a determiner (DET), followed
by a noun, followed by another noun, . . . . Then, Label(S)
represents what we are interested in: the ﬁrst two words are
not interesting, but the 3rd and 4th words represent a Persona.
A complete version of the example is provided in FIG 3.

The main limitations of CRF are that (i) it works at the
word level (model elements can spread across several words),
and (ii) it is not designed to identify relations between entities.
To address the ﬁrst limitation, we use a glueing heuristic.
Words that are consecutively associated with the same label
are considered as being the same model element, e.g., the
subsequence [’UI’, ’designer’] from the previous example is
considered as one single model element of type Persona. We
apply this heuristic to everything but verbs, as classically, two
verbs following each other represent different actions. Again,
we use a heuristic approach to address the second limitation.
We bound every Persona to every primary Action (as
trigger relations), and every primary Actions to every
primary Entity (as target relations).


#### B. Implementing the task using CRF

As VN is implemented in Python 3.7 and relies on spaCy
for POS tagging, we decided to use the same stack to reduce
the comparison gap. Among the different implementations of
CRF available, sklearn-crfsuite6 was the most suitable
for this reason. Unfortunately, the code was outdated (2014)
and not maintained (referring to version 0.15 of scikit-learn).
Thus, we ﬁxed the integration problems so that the code could

run in the recent scikit-learn version (1.x) and with a recent
version of Python (3.10). This version of the scikit-learn plugin
is available as an open source software [17]. The CRF tool is
available on GitHub7

Training the model is straightforward as soon as the CRF
framework is integrated. We transform each story into a
stream of words, compute the POS using spaCy, associate
the semantic label from the annotated dataset, and use this
to create our feature set used for training. The feature set
represents the context windows by associating a given word
with its POS, label, and information on the surrounding words.
In addition to the POS and labels described in the previous
section, we also provide the algorithm with the length of
the word, its capitalization, and its alphanumeric status. Our
current implementation has a sliding window of four words
preceding the current one and one following it. These values
were selected with an experimental approach to minimize
overﬁtting while maintaining a reasonable F-measure (see
SEC. V). When the model is trained, we can now provide an
unknown story to the model and obtain a sequence of semantic
labels as output. Using the previously described heuristics, we
transform these labels into instances of our domain metamodel
to obtain the ﬁnal result.


#### C. Discussions & Lessons Learned

As for GPT, we only discuss the lessons learned at the

technical level.

- Domain Knowledge. We could only implement this ap-
proach thanks to a close collaboration with NLP experts.
The landscape of NLP approaches is wide, and without
domain expertise, we would have never identiﬁed CRF as
a potential candidate for domain model extraction. Being
able to transfer our software engineering problems to AI
experts is essential to avoid reinventing a squared wheel
by simply aggregating visible solutions.

- Fighting the hype. As stated, CRF is losing popularity.
The hype/fashion lifecycle is classical in software engi-
neering. Think about Aspect-oriented Programming: sup-
posed to revolutionize software development in the ’00s,
they are now forgotten, except in particular places where
they perfectly ﬁt (e.g., Spring, a reference framework
to develop enterprise code in java, intensively rely on
aspects under the hood). It is important to build on the
shoulders of giants and not to succumb to the latest
fashionable “thing”.

- Technical Complexity. Compared to the simplicity of
the GPT code, implementing this CRF approach required
more advanced Python programming skills, including ﬁx-
ing outdated dependencies, patching a sci-kit-learn mod-
ule, and integrating the approach in a machine learning
pipeline. This is not unachievable, but the effort and skills
required are clearly different by an order of magnitude.
- Cost. Being self-hosted, the approach does not directly
the training time and resource

cost money. However,

6https://github.com/TeamHG-Memex/sklearn-crfsuite

7https://github.com/ace-design/nlp-stories/tree/main/nlp/nlp tools/crf

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

585

Word
POS
Label

Word
POS
Label

As
a
ADP DET NOUN
–

PER

UI

–

designer
NOUN
PER

,
PUNCT
–

I

want

to

begin

user

testing

,

PRON VERB PART VERB NOUN NOUN PUNCT

–

–

–

P-ACT

P-ENT

P-ENT

–

so
SCONJ
–

that
SCONJ
–

I

can
PRON AUX

–

–

validate
VERB
S-ACT

stakeholder
NOUN
S-ENT

UI
NOUN
S-ENT

improvement
NOUN
S-ENT

requests
NOUN
S-ENT

.
PUNCT
–

POS tags are the Universal POS tags (https:// universaldependencies.org/ u/ pos/ ), computed by spaCy.
Labels: PER (Persona), P-ACT (Primary Action), P-ENT (Primary Entity), S-ACT (Secondary Action), S-ENT (Secondary Entity)

Fig. 3. Minimal Feature Set, associating part-of-speech (POS) and semantic labels to each word in a given story

consumption need to be considered. On an average laptop,
the training takes less than a minute for a set of 1k stories.


### V. Validation

This section empirically evaluates the three approaches
(Visual Narrator, GPT-3.5 and CRF) to the ground truth
established during the annotation phase.


#### A. Experimental Setup

First, we had to build the corpus that would be used to
support the evaluation. We started by cleaning up the dataset
from duplicated stories. Then, we consider the intersection
set of the backlogs as the set of stories where all the tools
considered were able to produce parsable outputs. Ultimately,
we perform our evaluation with a corpus containing 1, 459
stories (87% of the initial corpus).

the dataset

As CRF requires training, we used a classical 80/20 sep-
aration. We randomly split
into a training set
containing 80% of the stories and used the remaining 20%
for evaluation with the three tools. We trained CRF in two
modes: (i) global and (ii) individual. For the global mode, we
extracted the training set from the complete corpus, mixing
different products. The individual mode applied the 80/20
partition backlog by backlog (Fig. 4).

To properly compare results, we must deﬁne whether a
result is good or bad. At best, a result is perfect when the
AI approach produces precisely the same elements as the one
available in the ground truth. We call this comparison mode
the Strict one. To relax the constraints, we also considered
a comparison where the AI tool produces a superset of
the ground truth, checking that the baseline is Included in
the produced result. Finally, we also considered a Relaxed
comparison, where we relaxed the checking by considering
plurals and singular equivalent to each other, or ignoring ad-
jective qualiﬁers. Eventually, the results are consistent for each
tool, whatever comparison measure is used. To avoid unfair
comparisons, we do not compare the identiﬁed trigger and
target relations, as VN was not designed for this task.

We represent in FIG. 4 the averaged F-measure (F1) for each
algorithm, comparison mode, and extracted model element.
Being deﬁned as the harmonic mean of precision and recall,
F1 considers correctly and incorrectly classiﬁed observations
(as opposed to accuracy, which focuses on positive cases). It
is classical to use F1 instead of accuracy when the cost of
making a wrong decision is essential (here, extracting domain
concepts that are not part of the domain). An F1 score of
1.0 means a perfect match, and a F1 score of 0.0 means that
precision or recall is null.


#### B. Result Interpretation

First, it is interesting to notice that VN (establishing a
baseline from the state of practice) performs reasonably on
Personas and Actions but quite poorly on Entity(ies),
with a maximum F1 < 0.25 (relaxed comparison).

Identifying the Persona instances is by far the most
straightforward task. The Conextra Template can explain this,
as their position in the user story is entirely predictable
(adding noise in front of the “As a” marker in a story disturbs
VN). Same for identifying the Actions, as their position is
also predictable (e.g., “I want to. . . ”). An Entity, being a
common noun that can appear anywhere in the sentence, is
harder to detect by a rule-based system. VN often fails at
identifying proper entities, and default to one named System
(even if not mentionned in the story).

When comparing GPT-3.5 with VN, it is clear that using
an LLM to support
the concept extraction task creates a
breakthrough. VN’s implementation consists of a 23 Python
ﬁle and 2, 856 lines of code, while interfacing with GPT-
3.5 requires one single script of 337 lines. Furthermore, the
obtained results outperform VN in every case. The most
signiﬁcant improvement relates to identifying Actions: VN
F1 score is around 0.2, whereas GPT-3.5 is around 0.6, without
any need for training or annotation. Based on the results,
LLMs are interesting for an average extraction, as they do not
require additional effort to outperform the state of practice.

However, it is essential to note that GPT-3.5 was systemat-
ically outperformed by our CRF implementation (its worst F1
value is 0.81, and it reaches a perfect 1.0 for Personas’
extraction). This is no surprise: LLMs are a one-size-ﬁts-
all approach, where a tailored approach developed with a
domain expert (here in NLP) to use the correct underlying
model/algorithm is precisely addressing the problem to solve.


#### C. Limitations & Threats to Validity

First, the creation of the ground truth is, by nature, inﬂu-
enced by subjective factors. We mitigated this according to
a precise protocol, including bi-weekly meetings and manual
cross-check of 19.6% of the annotated dataset with an inter-
rater agreement of 94%. However, the two authors involved in
the annotation process might have introduced unconscious bias
in their annotation guidelines. An external validation of the
annotated dataset would be beneﬁcial. This threat is mitigated
by the fact that (i) the results are provided relatively to this
ground truth, and (ii) the 3rd author has 11 years of experience
teaching agile methods and user stories writing as an academic
instructor and industrial consultant.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

586

Fig. 4. Comparing approaches to the ground truth: F-measure results for Visual Narrator, GPT-3.5 and CRF

The second threat to validity is related to the LLM model
we used and the prompt engineering method we followed. We
only used GPT-3.5, and more extensive experimentations are
needed to see if the results presented in this paper hold when
compared to GPT-4 (OpenAI), Bard (Google), or LLaMA
(Meta). Concerning prompt engineering, despite intensively
relying on OpenAI best practices, as LLMs are black boxes,
it
is very hard to identify which elements inﬂuence the
model positively or negatively. To support reproducibility, we
also had to set GPT-3.5’s temperature to 0, making it as
deterministic as possible. This choice might have introduced a
negative bias in the result, and more experiments are needed
to handle the non-deterministic nature of LLMs to evaluate
their results in the context of domain model extraction.


### VI. Conclusions

In this paper, we have experimented with how Visual
Narrator, GPT-3.5 and a CRF-based approach performed to
automate the extraction of domain concepts from agile product
backlogs. The ﬁrst contribution of this paper is an open-data
repository [12] containing an annotated version of a reference
backlog corpus (22 products, 1, 679 user stories), reusable
by other researchers. Then, for both GPT-3.5 and CRF, we
provided an in-depth discussion of the engineering dimensions
associated with their development (including prompt engineer-
ing for GPT-3.5), and we evaluated the results at scale on top
of the annotated corpus.

Out of these results, if the GPT-3.5 LLM is better (F1 ≈ 0.6)
than the state of practice concerning this task, it is outper-
formed by the CRF approach designed with NLP experts
(F1 ≈ 0.85), which require less than a minute of training.
It triggers a question for the following research efforts in this
direction: Should we, as researchers, choose to use easily in-
tegrable but far-from-ideal (energy cost, average F1) solutions
available off-the-shelf, or should we instead choose to invest
in collaborating with AI/NLP domain experts to deﬁne tailored
solutions that would support MDE intelligence?

REFERENCES

[1] F. Dalpiaz, A. Ferrari, X. Franch, and C. Palomares, “Natural language
processing for requirements engineering: The best is yet to come,” IEEE
Software, vol. 35, no. 5, pp. 115–119, 2018.

[2] G. Mussbacher, B. Combemale, J. Kienzle, S. Abrah˜ao, H. Ali,

#### N. Bencomo, M. B´ur, L. Burgue˜no, G. Engels, P. Jeanjean, J.-M.
J´ez´equel, T. K¨uhn, S. Mosser, H. A. Sahraoui, E. Syriani, D. Varr´o,
and M. Weyssow, “Opportunities in intelligent modeling assistance,”
Softw. Syst. Model., vol. 19, no. 5, pp. 1045–1053, 2020. [Online].
Available: https://doi.org/10.1007/s10270-020-00814-5

[3] T. Brown et al., “Language models are few-shot learners,” in Advances in
Neural Information Processing Systems, NeurIPS, Ed., vol. 33. Curran
Associates, Inc., 2020, pp. 1877–1901.

[4] OpenAI. [Online]. Available: https://chat.openai.com/
[5] S. Mosser, V. Reihnarz, and C. Pulgar, “Modelling Agile Backlogs as
Composable Artefacts to support Developers and Product Owners,” J.
Object Technol., 2022.

[6] F. Dalpiaz, “Requirements Data Sets (User Stories),” 2018, Mendeley
[Online]. Available: https://data.mendeley.com/datasets/

Data (v1).
7zbk8zsd8y/1

[7] L. Zhao, W. Alhoshan, A. Ferrari, K. J. Letsholo, M. A. Ajagbe, E.-V.
language processing
Chioasca, and R. T. Batista-Navarro, “Natural
for requirements engineering: A systematic mapping study,” ACM
Comput. Surv., vol. 54, no. 3, apr 2021.
[Online]. Available:
https://doi.org/10.1145/3444689

[8] M. Weyssow, H. A. Sahraoui, and E. Syriani, “Recommending
metamodel concepts during modeling activities with pre-trained
language models,” Softw. Syst. Model., vol. 21, no. 3, pp. 1071–1089,
2022. [Online]. Available: https://doi.org/10.1007/s10270-022-00975-5
[9] D. Bajaj, A. Goel, S. Gupta, and H. Batra, “Muce: a multilingual use
case model extractor using gpt-3,” International Journal of Information
Technology, vol. 14, no. 3, pp. 1543–1554, 2022.

[10] M. Cohn, User Stories Applied: For Agile Software Development. USA:

Addison Wesley Longman Publishing Co., Inc., 2004.

[11] M. Robeer, G. Lucassen, J. M. E. M. van der Werf, F. Dalpiaz, and

#### S. Brinkkemper, “Automated extraction of conceptual models from
user stories via nlp,” in 2016 IEEE 24th International Requirements
Engineering Conference (RE), 2016, pp. 196–205.

[12] S. Arulmohan, S. Mosser, and M.-J. Meurs, “ace-design/qualiﬁed-
[Online]. Available: https:

user-stories: Version 1.0,” Jul. 2023.
//doi.org/10.5281/zenodo.8136975

[13] M. Honnibal and I. Montani, “spaCy 2: Natural language understanding
with Bloom embeddings, convolutional neural networks and incremental
parsing,” 2017, to appear.

[14] S. Mosser and S. Arulmohan, “ace-design/gpt-stories: Version 1.0,” Jul.
2023. [Online]. Available: https://doi.org/10.5281/zenodo.8132676
[15] E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell,
“On the Dangers of Stochastic Parrots: Can Language Models Be
Too Big?” in Proceedings of the 2021 ACM Conference on Fairness,
Accountability, and Transparency, ser. FAccT ’21. New York, NY,
USA: Association for Computing Machinery, 2021, p. 610–623.
[Online]. Available: https://doi.org/10.1145/3442188.3445922

[16] J. Lafferty, A. McCallum, and F. Pereira, “Conditional random ﬁelds:
Probabilistic models for segmenting and labeling sequence data: pro-
ceedings of the 18th international conf. on machine learning, 2001,”
San Francisco, CA, USA, 2001.

[17] M. Korobov, S. Mosser, B. Mackintosh, C. D. Pietrantonio, M. E.
Haase, and S. Woo, “ace-design/ace-sklearn-crfsuite: Version 0.4.1,”
Jul. 2023. [Online]. Available: https://doi.org/10.5281/zenodo.8132729

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:06 UTC from IEEE Xplore. Restrictions apply.

587


---

> *End of P-06*

<br><br>

<a id="p07-----graph-retrieval-augmented-generation-for-large-language-models-a-survey"></a>

## P-07 — Graph Retrieval-Augmented Generation for Large Language Models: A Survey

| Field | Details |
|-------|---------|
| **Paper ID** | `P-07` |
| **Title** | Graph Retrieval-Augmented Generation for Large Language Models: A Survey |
| **Authors** | Cole Procko and Jill Ochoa |
| **Affiliation(s)** | Department of Electrical Engineering and Computer Science, Embry-Riddle Aeronautical University, Prescott, AZ, USA |
| **Venue** | IEEE Conference on Artificial Intelligence Enabled Software Engineering and Testing (AIxSET) |
| **Volume / Year** | 2024 |
| **DOI** | — |

---

2024 Conference on AI, Science, Engineering, and Technology (AIxSET)

Graph Retrieval-Augmented Generation for Large
Language Models: A Survey

Tyler Thomas Procko, Omar Ochoa
Department of Electrical Engineering and Computer Science
Embry-Riddle Aeronautical University
Daytona Beach, United States of America
prockot@my.erau.edu, ochoao@erau.edu


### Abstract

Large Language Models (LLMs) demonstrate general
knowledge, but they suffer when specifically needed knowledge is not
present in their training set. Two approaches to ameliorating this,
without re-training, are 1) prompt engineering and 2) Retrieval-
Augmented Generation (RAG). RAG is a form of prompt engineering,
insofar as relevant lexical snippets retrieved from RAG corpora are
vectorized and aggregated with prompts. However, RAG documents
are often noisy, i.e., while relevant to a given prompt, they can contain
much other information that obfuscates the desired snippet. If the
purpose of pre-training a LLM on massive and general corpora is to
engender a generally applicable model, RAG is not: it is a means of
LLM optimization, and as such, RAG document selection must be
precise, not general. For expert tasks, it is imperative that a RAG
corpus be as noise-free as possible, in much the same way a good
prompt should be free of irrelevant text. Knowledge Graphs (KGs)
provide a concise means of representing domain knowledge free of
noisy information. This paper surveys work incorporating KGs with
LLM RAG, intending to equip scientists with a better understanding
of this novel research area for future work.

commonly created for domain-specific use cases, providing
concise and understandable sources of subject matter expert
knowledge [6]. KGs may provide non-noisy RAG [7, 8, 9].

identifying

Pan et al. present a roadmap for the unification of KGs and
LLMs,
interaction: KG-
three archetypes of
enhanced LLMs, LLM-augmented KGs and Synergized LLMs
+ KGs [10]. Using KGs for RAG is a practice in KG-enhanced
LLMs. This research area is relatively novel and no aggregate of
its works is extant. The present paper fills this knowledge void.


### II. Background
LLMs are generally applicable to most application areas, but
require optimization for specific tasks, or when particular
constraints need to be met. There are three primary means of
optimizing a LLM: fine-tuning, RAG and prompt engineering.
These techniques aim to increase model steerability and can be
used in tandem for greater effect [11] (see Fig 1).


### Index Terms / Keywords

LLM, GPT, fine-tuning, knowledge graphs, RAG

- Fine-tuning: model trained on task-specific dataset or rule set

I.

INTRODUCTION

Large Language Models (LLMs) are at the forefront of large-
scale generative artificial
intelligence constructs being
employed in various fields [1]. In applications requiring deep
learning techniques, the traditional method of training models
uniquely fit for specific use cases has been replaced with the
“pre-train, fine-tune and predict” paradigm, which sees the use
of large, “off the shelf” models capable of accurate predictions
over a large domain knowledge space [2, 3].
Despite the general ability of LLMs, they suffer insofar as
they may lack up-to-date information, or niche information,
relevant to a given prompt, because re-training a LLM is both
time-consuming and
labor-intensive. Appropriate prompt
engineering, e.g., providing more context, can ameliorate these
issues, but it places a burden on the prompter. Another approach
is to augment a LLM prompt with a search of external resources
for relevant lexical fragments, referred to as Retrieval-
Augmented Generation (RAG) [4].
With relevant domain documents, RAG improves LLM
accuracy; but RAG documents can be noisy, i.e., they may
contain information not exactly relevant to a given prompt.
Increased document noise results in decreased accuracy from
LLMs employing RAG [5]. The ideal RAG corpus is as specific
to a given problem (prompting) set as possible.
Knowledge Graphs (KGs) are a form of knowledge
representation comprised of nodes and edges, or entities and the
relations between them. KGs may be predicated upon a rigorous
ontology, e.g., through the Web Ontology Language (OWL), or
grown rather organically with simple lexicons. KGs are

addressing, e.g., safety, fairness, etc. [12, 13, 14]

- Retrieval-Augmented Generation (RAG): prompt augmented

with relevant snippets from external documents [4]

- Prompt engineering: steering a model with task-specific
instructions, e.g., Chain-of-Thought (CoT) prompting [15],
Reasoning + Action (ReAct) [16], etc.

There are various named prompt engineering techniques
[17]. Every prompt engineering technique, at the most
fundamental level, amounts to providing a LLM with more
context: be it literally, as with few-shot prompting, or through
self-recorded logic, e.g., as with CoT prompting. RAG is itself
a prompt engineering technique, as snippets induced through
RAG are combined with a given input prompt to form a vector;
but RAG is distinguished from prompt engineering insofar as it
explicitly depends on a search of documents external to the
prompt. All modes of information have been researched as RAG
input: text, image, video, audio, code and structured knowledge,
e.g., databases and graphs [18, 19, 20].

The underpinning of prompt engineering and RAG is the
providence of relevant contextual information for a LLM to
utilize. Increased document noise significantly worsens RAG
efficacy [5], so structured, concise knowledge forms, e.g.,
knowledge graphs, are posited to be useful as RAG input [7, 8].


#### A. Knowledge Graphs and Textual Graphs
Traditional KG embedding approaches, which map KG entities
and relations into a low-dimensional vector space for various
NLP tasks, suffer from data sparsity because of the limited
context of KG triples. To address this, some have incorporated

979-8-3503-9099-5/24/$31.00 ©2024 IEEE
DOI 10.1109/AIxSET62544.2024.00030

166

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:02 UTC from IEEE Xplore. Restrictions apply.

.

.

0
3
0
0
0
4
2
0
2
4
4
5
2
6
T
E
S
X
A
/
9
0
1
1
0
1
:
I

.

I

O
D
|
E
E
E
I

.

4
2
0
2
©
0
0
1
3
$
/
4
2
/
5
-
9
9
0
9
-
3
0
5
3
-
8
-
9
7
9
|
)
T
E
S
x
I
A
(

l

y
g
o
o
n
h
c
e
T
d
n
a
,
g
n
i
r
e
e
n
g
n
E
,
e
c
n
e
i
c
S
,
I

i

A
n
o
e
c
n
e
r
e
f
n
o
C
4
2
0
2


Fig. 1 LLM optimization techniques and their relationships to model steerability (adapted from [11]).

textual entity descriptions for richer context [21]. Such a
construct is referred to as a text, or textual, graph. A textual
graph is a graph whose nodes and edges are attended with textual
attributes. Where the focus of a KG is on structured
relationships, with text providing only supplementary context, a
textual graph integrates text and structure as equally important
context.
These two graph forms are distinguished here because they
are similar but not precisely the same. Textual graphs typically
have an underlying structure, so KGs are central to the
discussion. In the present paper, both KGs and textual graphs are
considered within the context of Graph RAG, but the term KG
is used in reference to both.


### III. Graph Rag
Much of the literature in the Graph RAG research landscape
pertains to problems of Question-Answering (QA), which was
traditionally addressed by KGs interfaced with intention and
entity recognition algorithms. Knowledge graph question
answering (KGQA) is useful for factual QA but suffers on open-
ended questions. The combination of LLMs with KGQA
frameworks is a commonly researched application of RAG,
although the seminal RAG method is not always explicitly cited
[22, 23].
While RAG is useful for providing additional context to a
prompted LLM through small, relevant snippets, it suffers
insofar as it does not consider broader contextual semantics, e.g.,
correlations among documents within corpora [24, 25]. Graph
RAG approaches aim to address this limitation of naïve RAG by
incorporating broader semantics across documents within
corpora, which is made possible through searches over KGs or
sub-graphs generated therefrom. At the core of Graph RAG
research is the problem of relevant sub-graph identification from
larger KGs, which is computationally infeasible (NP-hard) if
done exhaustively [24]. See Table I for a survey summary.
He et al. present G-Retriever, a QA framework that enables
users to “chat with their graph”, useful for common sense
reasoning, visual scene understanding and general knowledge
graph reasoning [26]. Where extant RAG approaches are
designed for simpler information, e.g., text, G-Retriever
includes a new RAG approach applicable to general textual
graphs. Their sub-graph construction solution is the Prize-
Collecting Steiner Tree algorithm. They also present the
GraphQA benchmark for evaluation, demonstrating that G-

Retriever is scalable to larger graphs, applicable to tasks from
several domains and lessens LLM hallucination.
Edge et al. present a Graph RAG approach to global question
answering, framing the problem as one of query-focused
summarization (QFS) [25]. They create a KG using an LLM in
a series of steps, culminating in LLM-generated summaries of
graph communities, enabling QFS of large corpora for better
global QA.
A paper published in association with the business social
media platform, LinkedIn, reports on the efficacy of a KG-
enabled RAG system for customer service QA [27]. Traditional
RAG-based LLM customer service approaches suffer from
retrieval inaccuracy because tickets are treated as plain text,
resulting in a loss of structure. The authors construct a KG from
historical customer service issue tickets; this KG is then parsed
into sub-graphs for RAG input.

Sanmartín presents

the knowledge graph

retrieval-
augmented generation (KG-RAG) framework to perform
KGQA [28]. Operating under the analogy of the “extended
mind”, where humans augment their cognitive ability with
outside resources, e.g., books, he incorporates the novel Chain
of Explorations (CoE) algorithm for Graph RAG, which enables
an LLM to explore KG nodes and relationships for better QA.
Hu et al.
the Graph Retrieval-Augmented
Generation (GRAG) computational framework [24]. Their
GRAG approach comprises four stages: (1) generating
embeddings of k-hop ego-graphs from a main textual graph, (2)
retrieving relevant textual subgraphs, (3) applying soft pruning
to reduce irrelevant entities, and (4) utilizing graph neural
networks (GNNs) and LLMs to generate responses with both
hard and soft prompts. GRAG surpassed G-Retriever in
accuracy. The authors also discuss a notable specialization of
RAG, in the dichotomy of hard and soft prompting [24].

introduce

- Hard Prompts: Explicit, structured text inputs given to a LLM

to guide its generation

- Soft Prompts: Implicit embeddings in the LLM's input vector
space, which the model uses to guide its generation without
explicit instructions

Xu et al. present a QA system for the very specific domain
of the Chinese silk weaving craft, Nanjing Yunjin [29]. Their
system addresses the limitations of an extant KG-based QA
system, namely, the need for constant updates to the KG and the

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:02 UTC from IEEE Xplore. Restrictions apply.

167


Paper

KG(s) Used

LLM(s) Evaluated

Dataset

TABLE I. Graph RAG papers surveyed.

G-Retriever [25] Unspecified

LLaMA2

KG-RAG [27]
GRAG [23]

Generated*
Unspecified

GPT-4
LLaMA2

TRACE [8]
Triple-Aware
Reasoning [7]
RAKG [9]
GNN-RAG [31]

Generated*
ConceptNet

LLaMA3
GPT-3.5, GPT-4

ConceptNet
Freebase

Unspecified
LLaMA2

LPKG [32]

Wikidata15k

Generated*
Generated*
Generated*

LLaMA3,

GPT-3.5,
CodeQwen1.5
GPT-4
LLaMA2
GPT-4

[24]
[28]
[26]

[29]

Generated*

GPT-4

GraphQA (ExplaGraphs, SceneGraphs,
WebQSP)
Complex WebQuestions
ExplaGraphs,
Web QuestionsSP
HotPotQA, 2WikiMultiHopQA, MuSiQue
CommonsenseQA, OpenBookQA

CommonsenseQA, OpenBookQA
WebQuestionsSP,
ComplexWebQuestion
HotPotQA, 2WikiMultihopQA,
Bamboogle, MuSiQue, CLQA-Wiki
Podcast transcripts and MultiHop-RAG
100 domain questions
“Golden” dataset of queries, tickets and
solutions
Small task set

[30]

Generated*

MechGPT

Small evaluation set curated for the article

* indicates KG(s) generated through traditional approaches, e.g., relation extraction, or through the use of a LLM

Evaluation Technique

Performance, Efficiency

EM, 𝐹1, Accuracy, Hallucination
𝐹1, Hit@1, Recall; Accuracy

EM, 𝐹1
Accuracy

Accuracy
Hit, Hit@1, 𝐹1

EM

Domain

Any

Any
Any

Any
Any

Any
Any

Any

Head-to-head LLM evaluation
Accuracy
Comparison to “golden” baseline
using BLEU, METEOR, ROUGE
Comparison to baseline using human
experts; correctness, usability,
relevance, time; context recall,
context precision
Various qualitative techniques

Any
Anthropology
Customer Service

Manufacturing

Materials Science

limited scope of predefined entities and relations, by cascading
user queries first through a typical KG QA pipeline, replete with
intention and entity recognition, which may return a response; if
the KG QA pipeline is unable to return a response, the problem
is shifted to a RAG QA pipeline, which will return a response
from a LLM augmented with Nanjing Yunjin documents.
Bahr et al. present a KG-enabled RAG system to be used in
a QA chatbot for failure mode and effects analysis (FMEA) in
product manufacturing
[30]. An ontology of FMEA
observations is presented, which is used to serialize KG triples.
Vector embeddings are then created from the FMEA KG and
incorporated into LLM RAG.

Fang, Meng and Macdonald present TRACE, which
employs a KG generator to create a KG from retrieved
documents, from which reasoning chains are made, enhancing
the multi-hop reasoning abilities of RAG-enabled LLMs [8].
TRACE is similar in approach to the CoT prompting technique
but demonstrates an improvement because KG triples are
grounded in RAG documents. The authors note that noise is an
issue of RAG. Also citing the issue of noisy RAG, Zhang and
Shafiq discuss Triple-Aware Reasoning, which combines KGs
and RAG for QA [7]. Their system incorporates a three-layer
filtering mechanism to ensure that triples from the ConceptNet
KG selected for RAG do not introduce noise into prompts: first
during retrieval, again according to specific relationships and
lastly with a designed prompt to filter incorporated triples again.
Sha et al. present the retrieval-augmented knowledge graph
(RAKG) model [9]. RAKG operates by first extracting the most
relevant sub-graphs using a density matrix, then fusing
embedded questions and KG entities using a graph
convolutional network and LLM.
Buehler provides an evaluation of MechGPT, a LLM trained
on materials domain knowledge. Through a mixed-methods
evaluation of MechGPT, he ultimately asserts that a fine-tuned
LLM in combination with KG-enabled RAG results in better
accuracy and scientific replicability [31].

Mavromatis and Karypis present GNN-RAG [32]. A graph
neural network first reasons over a KG subgraph to retrieve
answer candidates for questions. Then, the shortest paths in the
KG that link questions to answers are extracted to reasoning
paths. These paths are serialized in text and used as RAG input.
Wang et al. present a framework for LLM planning derived
from KGs called Learning to Plan from Knowledge Graphs
(LPKG) [33]. The LPKG approach begins by constructing
planning data from KGs; such data is then used to fine-tune
LLMs. They compare their method against direct prompting,
CoT prompting, naïve RAG and ReAct prompting, among other
baselines.


### IV. Discussion
It is apparent, in synthesizing the literature, that there are two
main perspectives within Graph RAG research:
1. Using extant KGs for RAG
2. Generating KGs from document corpora for RAG

The former perspective sees the leveraging of pre-existing
KGs, e.g., ConceptNet, as RAG input; the latter typically
involves the creation of task-specific KGs, either with traditional
relation extraction approaches or with an LLM, to be used as
RAG
the surveyed papers, both perspectives
demonstrate efficacy, but the LLM-based generation of task-
specific KGs
is more prevalent and engenders greater
adaptability to a wider array of application areas.

input. In

HotPotQA,

Evaluations of the surveyed Graph RAG approaches vary,
but typically involve an open QA dataset and some typical
metric, e.g., accuracy and 𝐹1. The WebQuestionsSP, Complex
WebQuestions,
and
OpenBookQA datasets were commonly used to evaluate the
surveyed Graph RAG approaches. Most of the approaches
surveyed were agnostic to any particular area of interest, with
only four specifying distinct focus areas: anthropology,
customer service, manufacturing and materials science.
A commonly cited reason for incorporating RAG into LLM
workflows is to increase LLM accuracy while reducing LLM

CommonsenseQA

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:02 UTC from IEEE Xplore. Restrictions apply.

168


hallucination. The underlying structure of KGs used for RAG is
beneficial because the identification of relevant sub-graphs
directly addresses the hallucination issue. Others have framed
RAG as a hierarchical document search problem, allowing for
more efficient retrieval through global document organization
[34].
Regarding limitations, the present paper is restricted in terms
of replicability, because the survey was not conducted in a
systematic fashion, to the extent that doing so is even possible
[35]. Moreover, given the extreme novelty of the Graph RAG
research area, and the consistent publication stream, it is not
feasible to address all applicable research. At most, the present
paper provides a concise “snapshot” of current research into
Graph RAG.


### V. Conclusion
RAG is useful to the LLM prompter, and LLM-enabled
applications or enterprises, as it mitigates difficulty in explicit
prompting work by shifting the burden of context providence to
search algorithms run over large corpora. The selection of a
RAG corpus appropriately relevant to a given task is important
to the reliable fulfillment of the task. Furthermore, the level of
noise, or irrelevant information, within a RAG corpus is
inversely proportional to the level of RAG usefulness. So, a
cogent RAG corpus is beneficial. Research indicates that KGs
provide a basis for less noisy RAG in their cogent structuring of
knowledge. The present paper provides researchers with a
synthesis of Graph RAG approaches and applications. This area
of work is promising insofar as it is a means of effectively
reducing RAG noise which in turn reduces LLM response
uncertainty.


### VI. References

[1] T. T. Procko, T. Elvira and O. Ochoa, "Dawn of the Dialogue: AI's Leap from Lab

to Living Room," Frontiers in Artificial Intelligence, vol. 7, 2024.

[2] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi and G. Neubig, "Pre-train, prompt, and
predict: A systematic survey of prompting methods in natural language processing,"
ACM Computing Surveys, vol. 55, no. 9, pp. 1-35, 2023.

[3] J. Zhang, H. Jiaxing, S. Jin and S. Lu, "Vision-language models for vision tasks: A
survey," IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024.

[4] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M.
Lewis, W.-t. Yih, T. Rocktäschel, S. Riedel and D. Kiela, "Retrieval-Augmented
Generation for Knowledge-Intensive NLP Tasks," Advances in Neural Information
Processing Systems, vol. 33, pp. 9459-9474, 2020.

[12] O. Honovich, T. Scialom, O. Levy and T. Schick, "Unnatural Instructions: Tuning
(Almost) No Human Labor," arXiv preprint

Language Models with
arXiv:2212.09689, 2022.

[13] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon and C. Finn, "Direct
preference optimization: Your language model is secretly a reward model,"
Advances in Neural Information Processing Systems, vol. 36, 2024.

[14] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S.
Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens
and A. Askell, "Training language models to follow instructions with human
feedback," Advances in neural information processing systems, vol. 35, 2022.

[15] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le and D. Zhou,
"Chain-of-thought prompting elicits reasoning in large language models," Advances
in neural information processing systems, vol. 35, pp. 24824-24837, 2022.

[16] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan and Y. Cao, "React:
language models," arXiv preprint

in

Synergizing reasoning and acting
arXiv:2210.03629, 2022.

[17] P. Sahoo, A. K. Sing, S. Saha, V. Jain, S. Mondal and A. Chadha, "A Systematic
Survey of Prompt Engineering in Large Language Models: Techniques and
Applications," arXiv preprint arXiv:2402.07927, 2024.

[18] R. Zhao, H. Chen, W. Wang, F. Jiao, X. Long Do, C. Qin, B. Ding, X. Guo, M. Li,
X. Li and S. Joty, "Retrieving multimodal information for augmented generation: A
survey," arXiv preprint arXiv:2303.10868, 2023.

[19] Z. Hu, A. Iscen, C. Sun, Z. Wang, K.-W. Chang, Y. Sun, C. Schmid, D. A. Ross
and A. Fathi, "Reveal: Retrieval-augmented visual-language pre-training with
multi-source multimodal knowledge memory," Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition, pp. 23369-23379, 2023.

[20] W. Yu, "Retrieval-augmented generation across heterogeneous knowledge,"
Proceedings of the 2022 conference of the North American chapter of the
association for computational linguistics: human language technologies: student
research workshop, pp. 52-58, 2022.

[21] L. Hu, M. Zhang, S. Li, J. Shi, C. Shi, C. Yang and Z. Liu, "Text-graph enhanced
knowledge graph representation learning," Frontiers in Artificial Intelligence, vol.
4, 2021.

[22] Y. Wu, N. Hu, G. Qi, S. Bi, J. Ren, A. Xie and W. Song, "Retrieve-rewrite-answer:
A kg-to-text enhanced LLMs framework for knowledge graph question answering,"
arXiv preprint arXiv:2309.11206, 2023.

[23] P. Sen, S. Mavadia and A. Saffari, "Knowledge graph-augmented language models
for complex question answering," Proceedings of the 1st Workshop on Natural
Language Reasoning and Structured Explanations (NLRSE), pp. 1-8, 2023.

[24] Y. Hu, Z. Lei, Z. Zhang, B. Pan, C. Ling and L. Zhao, "GRAG: Graph Retrieval-

Augmented Generation," arXiv preprint arXiv:2405.16506, 2024.

[25] D. Edge, H. Trinh, N. Cheng, J. Bradley, A. Chao, A. Mody, S. Truitt and J. Larson,
"From local to global: A graph rag approach to query-focused summarization,"
arXiv preprint arXiv:2404.16130, 2024.

[26] X. He, Y. Tian, Y. Sun, N. V. Chawla, T. Laurent, Y. LeCun, X. Bresson and B.
Hooi, "G-retriever: Retrieval-augmented generation for textual graph understanding
and question answering," arXiv preprint arXiv:2402.07630, 2024.

[27] Z. Xu, M. Jerome Cruz, M. Guevara, T. Wang, M. Deshpande, X. Wang and Z. Li,
"Retrieval-Augmented Generation with Knowledge Graphs for Customer Service
Question Answering," arXiv preprint arXiv:2404.17723, 2024.

[28] D. Sanmartín, "KG-RAG: Bridging the Gap Between Knowledge and Creativity,"

arXiv preprint arXiv:2405.12035, 2024.

[5] J. Chen, H. Lin, X. Han and L. Sun, "Benchmarking large language models in
retrieval-augmented generation," Proceedings of the AAAI Conference on Artificial
Intelligence, vol. 38, no. 16, pp. 17754-17762, 2024.

[29] L. Xu, L. Lu, M. Liu, C. Song and L. Wu, "Nanjing Yunjin intelligent question-
answering system based on knowledge graphs and retrieval augmented generation
technology," Heritage Science, vol. 12, no. 1, 2024.

[6] B. Abu-Salih, "Domain-specific knowledge graphs: A survey," Journal of Network

and Computer Applications, vol. 185, 2021.

[7] H. Zhang and M. Omair Shafiq, "Triple-Aware Reasoning: A Retrieval-Augmented
Generation Approach for Enhancing Question-Answering Tasks with Knowledge
Graphs and Large Language Models," The 37th Canadian Conference on Artificial
Intelligence, 2024.

[8] J. Fang, Z. Meng and C. Macdonald, "TRACE the Evidence: Constructing
Knowledge-Grounded Reasoning Chains for Retrieval-Augmented Generation,"
arXiv preprint arXiv:2406.11460, 2024.

[9] Y. Sha, Y. Feng, M. He, S. Liu and Y. Ji, "Retrieval-Augmented Knowledge Graph
Reasoning for Commonsense Question Answering," Mathematics , vol. 11, no. 15,
2023.

[10] S. Pan, L. Luo, Y. Wang, C. Chen, J. Wang and X. Wu, "Unifying large language
models and knowledge graphs: A roadmap," IEEE Transactions on Knowledge and
Data Engineering, 2024.

[11] "Optimizing

LLMs

[Online]. Available:
https://platform.openai.com/docs/guides/optimizing-llm-accuracy. [Accessed June
2024].

accuracy," OpenAI,

for

[30] L. Bahr, C. Wehner, J. Wewerka, J. Bittencourt, U. Schmid and R. Daub,
"Knowledge Graph Enhanced Retrieval-Augmented Generation for Failure Mode
and Effects Analysis," arXiv preprint arXiv:2406.18114, 2024.

[31] M. J. Buehler, "Generative retrieval-augmented ontologic graph and multiagent
strategies for interpretive large language model-based materials design," ACS
Engineering Au, vol. 4, no. 2, pp. 241-277, 2024.

[32] C. Mavromatis and G. Karypis, "GNN-RAG: Graph Neural Retrieval for Large

Language Model Reasoning," arXiv preprint arXiv:2405.20139, 2024.

[33] J. Wang, M. Chen, B. Hu, D. Yang, Z. Liu, Y. Shen, P. Wei, Z. Zhang, J. Gu, J.
Zhou, J. Z. Pan, W. Zhang and H. Chen, "Learning to Plan for Retrieval-Augmented
Large Language Models
from Knowledge Graphs," arXiv preprint
arXiv:2406.14282, 2024.

[34] K. Goel and M. Chandak, "HIRO: Hierarchical
Optimization," arXiv preprint arXiv:2406.09979, 2024.

Information Retrieval

[35] S. K. Boell and D. Cecez-Kecmanovic, "On being ‘systematic’ in literature
reviews," Formulating Research Methods for Information Systems, pp. 48-78, 2016.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:02 UTC from IEEE Xplore. Restrictions apply.

169


---

> *End of P-07*

<br><br>

<a id="p08-----harnessing-multi-agent-llms-for-complex-engineering-problem-solving-a-framework-for-senior-design-projects"></a>

## P-08 — Harnessing Multi-Agent LLMs for Complex Engineering Problem-Solving: A Framework for Senior Design Projects

| Field | Details |
|-------|---------|
| **Paper ID** | `P-08` |
| **Title** | Harnessing Multi-Agent LLMs for Complex Engineering Problem-Solving: A Framework for Senior Design Projects |
| **Authors** | Abdullah Mushtaq, Rafay Naeem, Ibrahim Ghaznavi, Imran Taj, Imran Hashmi, and Junaid Qadir |
| **Affiliation(s)** | (1) Department of Computer Science, Information Technology University (ITU), Lahore, Pakistan<br>(2) College of Interdisciplinary Studies, Zayed University, Abu Dhabi, UAE<br>(3) Department of Computer Science, University of Oxford, UK<br>(4) Department of Computer Science and Engineering, Qatar University, Qatar |
| **Venue** | IEEE Global Engineering Education Conference (EDUCON) |
| **Volume / Year** | 2025 |
| **DOI** | — |

---

Harnessing Multi-Agent LLMs for Complex
Engineering Problem-Solving: A Framework for
Senior Design Projects

Abdullah Mushtaq∗, Rafay Naeem∗, Ibrahim Ghaznavi∗, Imran Taj†, Imran Hashmi‡, Junaid Qadir§
∗Department of Computer Science, Information Technology University, Lahore, Pakistan
{bscs20078, bscs20004, ibrahim.ghaznavi}@itu.edu.pk
†College of Interdisciplinary Studies, Zayed University, Abu Dhabi, UAE
MuhammadImran.Taj@zu.ac.ae
‡Department of Computer Science, University of Oxford, Oxford, UK
imran.hashmi@cs.ox.ac.uk
§Department of Computer Science and Engineering, Qatar University, Doha, Qatar
jqadir@qu.edu.qa


### Abstract

Multi-Agent Large Language Models (LLMs) are
gaining attention for their ability to harness collective intelli-
gence in complex problem-solving, decision-making, and planning
tasks. This aligns with the wisdom of crowds concept, where di-
verse agents collectively generate effective solutions, making them
well-suited for educational settings. Senior design projects, pivotal
in engineering education, integrate theoretical knowledge with
practical application, fostering critical thinking, teamwork, and
real-world problem-solving skills. These projects often involve
multidisciplinary considerations and conflicting objectives, such
as optimizing technical performance while addressing ethical,
social, and environmental concerns. In this paper, we explore
a framework where distinct LLM agents embody expert per-
spectives,
including problem formulation, system complexity,
societal and ethical considerations, and project management.
These agents engage in rich, collaborative dialogues, leveraging
multi-agent system principles like coordination, cooperation, and
negotiation. Prompt engineering is employed to create diverse
personas, simulating human engineering teams and incorporating
swarm AI principles to balance contributions efficiently. To
evaluate the framework, we analyzed six senior capstone project
proposals from engineering and computer science, comparing
Multi-Agent and single-agent LLMs using metrics developed
with engineering faculty and widely used NLP-based measures.
These metrics assess technical quality, ethical considerations,
impact, and feasibility, aligning with the educational
social
objectives of engineering design. Our findings suggest that Multi-
Agent LLMs can provide a richer, more inclusive problem-
solving environment compared to single-agent systems with 89%
alignment with engineering-faculty scores, offering a promising
tool for enhancing the educational experience of engineering and
computer science students by simulating the complexity and
collaboration of real-world engineering and computer science
practice. By supporting senior design projects, this tool not only
aids in achieving academic excellence but also prepares students
for the multifaceted challenges they will face in their professional
engineering careers. We have open-sourced our framework for
further development and adaptation on GitHub 1.


### Index Terms / Keywords

Large Language Models, Gen AI, LLM Agents,
LLM-Based Multi-Agent Systems, Multi-Agent Collaboration,
Agentic AI.

1Copilot

available
AbdullahMushtaq78/Multi-Agent-SDP-Copliot

at GitHub Repository:

is

https://github.com/


### I. Introduction

The senior design project (SDP), also known as the capstone
or final year project, is a vital component of engineering and
computer science education [1]. It offers students an oppor-
tunity to apply their theoretical knowledge in tackling com-
plex, real-world engineering problems, providing an authentic
learning experience that
integrates the essential competen-
cies required for 21st-century engineers [2], [3]. Accrediting
bodies, such as the US Accreditation Board for Engineering
and Technology (ABET) emphasize the importance of SDPs
as key opportunities for students to engage with the kinds
of complex, multidisciplinary challenges they will encounter
in professional practice. The problems addressed in SDPs
typically involve no straightforward solutions; instead, they
require students to balance competing objectives, such as
optimizing technical performance while addressing ethical,
environmental, and social concerns.

A hallmark of modern engineering practice is the increas-
ingly globalized context in which engineers operate. Engi-
neering products must be designed to meet the needs of a
global audience, often requiring the integration of diverse per-
spectives. This necessitates cultural intelligence—the ability
to navigate different cultural contexts and work effectively
with stakeholders from various backgrounds. Generative AI,
particularly LLMs, offers an innovative way to simulate these
diverse perspectives, providing students with an environment
to engage in interdisciplinary problem-solving [4], [5]. These
LLM agents represent different expert viewpoints and foster
a collaborative approach that reflects real-world engineering
practices.

The ability to solve complex problems is an essential com-
petence in both education and professional life, as individuals
increasingly face challenges arising from globalization and
digitalization. A complex problem occurs when a person seeks
to achieve a goal for which no clear or straightforward solution
is available. Unlike non-complex problems, complex problem-
solving (CPS) involves dynamic and opaque barriers, where

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

.

.

3
5
6
6
1
0
1
1
5
2
0
2
3
3
6
2
6
N
O
C
U
D
E
/
9
0
1
1
0
1
:
I

.

O
D
|
E
E
E
I

.

5
2
0
2
©
0
0
1
3
$
/
5
2
/
8
-
9
4
9
3
-
5
1
3
3
-
8
-
9
7
9
|
)

N
O
C
U
D
E
(
e
c
n
e
r
e
f
n
o
C
n
o
i
t
a
c
u
d
E
g
n
i
r
e
e
n
g
n
E

i

l

l

a
b
o
G
E
E
E
I

5
2
0
2


the initial information is incomplete or subject to change.
This definition, as articulated by Fischer, Greiff, and Funke,
emphasizes that complex problems require adaptive thinking
and flexibility in problem-solving approaches [6], [7]. In the
context of engineering, the complexity is further amplified
by the need to balance multiple, often conflicting objectives.
Systems thinking, as introduced by Peter Senge in The Fifth
Discipline, highlights the necessity of understanding the inter-
connections within complex systems, encouraging engineers
to consider multiple perspectives and the broader implications
of their solutions [8].

inherent

By leveraging the principle of the “wisdom of crowds”—
the idea that large groups of diverse, independent individuals
can collectively arrive at better decisions, solutions, and pre-
dictions than any single expert, as outlined by Surowiecki in
The Wisdom of Crowds [9]—MAS has the potential to en-
able collective intelligence through emergent behavior. While
intelligence is not
in MAS by design, structured
interactions, and coordination mechanisms among agents al-
low complex and intelligent behaviors to develop collectively,
leading to the emergence of intelligence [10]. The framework
we propose builds on this idea, using LLM agents to simulate
the interactions between diverse expert perspectives, such as
problem formulation agents, systems complexity agents, and
ethical and societal agents. In this way, LLM agents in the
proposed MAS can help students develop the critical thinking
and collaboration skills they need to succeed in globalized,
multidisciplinary engineering environments.

The contributions of this paper are both pedagogical and
technical. Pedagogically, it introduces a novel framework for
training engineering students and assisting supervisors in com-
plex problem-solving using multi-agent LLMs in SDPs. This
framework simulates interdisciplinary collaboration through
diverse LLM agents, enhancing critical thinking. Technically,
it advances the integration of MAS and LLMs to simulate mul-
tifaceted engineering scenarios, enabling effective problem-
solving while addressing ethical, social, and environmental
dimensions, and preparing engineers for global challenges.

The remainder of this paper is organized as follows. Section
II discusses background and related work, covering Agent-
Based Modeling, MAS, and prior AI applications in engineer-
ing education. Section III outlines the methodology, detailing
the use of Multi-Agent LLMs and evaluation criteria. Section
IV presents the results, followed by a discussion in Section V
on pedagogical and technical implications. Finally, Section VI
concludes the paper, summarizing contributions and outlining
future research directions.


### II. Background And Related Work


#### A. The Role of SDPs in Engineering Education

SDPs, also referred to as capstone or final-year projects, are
a crucial component of computing and engineering education.
As required by ABET and other accrediting bodies, SDPs
serve as a culminating experience that integrates the knowl-
edge and skills students have acquired over their academic

careers. These projects require students to solve complex, real-
world engineering problems that involve conflicting objectives,
trade-offs, and ethical considerations. For instance, engineers
must often balance cost efficiency with environmental sustain-
ability, or optimize technical performance while adhering to
regulatory constraints.

In these settings, teamwork and collaboration across diverse
skills and perspectives are essential. Given the globalized
nature of modern engineering practice, students are also re-
quired to consider cultural and social factors when designing
engineering solutions. This is especially important as engineers
increasingly work in global teams and must develop products
that meet the needs of an international audience. Therefore, en-
gaging with multiple stakeholders and considering the broader
societal and cultural contexts of engineering solutions [11] are
vital competencies that SDPs aim to cultivate.


#### B. Complex Problem Solving and Diversity Dividend

Complex engineering problems, as per the definition of
ABET2, have the following attributes, “involving wide-ranging
or conflicting technical issues, having no obvious solution,
addressing problems not encompassed by current standards
and codes, involving diverse groups of stakeholders, including
many component parts or sub-problems, involving multiple
disciplines, or having significant consequences in a range of
contexts.”

Several frameworks have been proposed that leverage di-
versity to foster effective problem-solving. One well-known
approach is Edward de Bono’s Six Thinking Hats framework,
which encourages individuals to look at problems from mul-
tiple perspectives—logical, emotional, and creative, among
others. This structured, yet flexible, approach is particularly
effective when integrated with MAS, as it mirrors the inter-
disciplinary thinking necessary to solve complex engineering
problems. Scott Page’s book The Difference [12] emphasizes
the value of diversity in problem-solving, particularly in com-
plex systems. Page argues that teams composed of individuals
with different skills, experiences, and perspectives are better
equipped to solve complex problems than homogenous teams.
This aligns with the wisdom of crowds principle, which
suggests that collective intelligence can outperform individual
expertise, particularly when the group is diverse and composed
of independent thinkers. Similarly, Minsky’s The Society of
Mind [13] underscores the importance of diverse cognitive
processes in problem-solving, positing that complex thought
emerges from the interaction of simpler, specialized processes.


#### C. Multi-Agent Systems and Agent-Based Modeling

MAS is widely applied in fields like robotics, artificial
intelligence, and complex systems modeling to simulate au-
tonomous agents acting within dynamic environments. While
each agent operates independently, their collective behavior
can lead to emergent properties—patterns or outcomes that
are challenging to predict solely from individual actions.

2https://www.abet.org/accreditation/accreditation-criteria/

criteria-for-accrediting-engineering-programs-2022-2023/

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

In engineering education, MAS can be used to simulate
stakeholder interactions in complex projects, enabling students
to experience realistic decision-making, collaboration, and
problem-solving scenarios.

Agent-Based Modeling (ABM) extends MAS by offering a
detailed computational framework for simulating interactions
between agents and their environments. ABM is especially
valuable for examining systems where individual behaviors
directly influence collective outcomes, making it ideal for
complex social or engineering contexts.
In SDPs, ABM
can simulate interactions among engineers, project managers,
regulators, and other stakeholders, giving students practical
insight into the collaborative and often unpredictable nature of
professional practice [14], [15]. These simulations provide a
flexible and dynamic approach for modeling complex systems,
allowing students to explore the consequences of various
decisions within a controlled environment


#### D. MAS and LLMs in Educational Contexts

The integration of Multi-Agent Systems (MAS) and Large
Language Models (LLMs) offers significant promise in en-
hancing engineering education by addressing complex, real-
world problems. MAS simulates interactions among diverse
autonomous agents, allowing exploration of trade-offs, dilem-
mas, and decision-making processes typical
in multidisci-
plinary projects, mirroring real-world engineering dynamics
where collaboration across domains and negotiation of con-
flicting objectives occur.
LLMs complement

this by representing expert per-
sonas—like problem formulation agents, project managers,
and ethical agents—enabling interdisciplinary dialogue. This
approach enhances innovation and solution robustness, lever-
aging the ”wisdom of crowds” effect [9], and provides deeper
insights into engineering complexities [16], [17], [18]. Re-
search highlights the potential of LLM agents in simulating
collaborative environments, aiding students in tackling ethical
dilemmas and environmental trade-offs, crucial for sustainable
design projects. This enhances critical thinking and a holistic
problem-solving approach, supported by real-time adaptive
feedback, enabling risk-free experimentation. Consequently,
it better equips students to navigate globalized engineering
challenges [16], [17].


#### E. Existing LLM Multi-Agent Frameworks

Several LLM-based multi-agent frameworks have emerged,
offering advanced capabilities for addressing complex, inter-
disciplinary challenges. In educational settings, these frame-
works are particularly valuable for their ability to simulate
real-world scenarios, fostering critical thinking, collaboration,
and problem-solving skills. Below are some examples of such
frameworks and their key features:

1) Camel-AI [16] is a communicative agent framework
that simulates a “society” of LLM agents representing
various personas, excelling in fostering interdisciplinary
dialogue and negotiating diverse viewpoints. Its ability
to explore multiple “mind” interactions makes it ideal

for projects, such as senior design projects, demanding
multiple perspectives.

2) Crew.AI [19] is an open-source multi-agent orchestra-
tion framework. This Python-based platform orchestrates
role-playing AI agents as a cohesive “crew” to complete
tasks. It excels in automating multi-agent workflows,
aiding in the coordination of diverse agent roles for
collaborative decision-making.

3) MegaAgent [17] is built to handle large-scale cooper-
ation in MAS, with scalability as its primary strength.
It enables numerous agents to operate in coordination,
making it suitable for simulating large, complex systems
and giving students insights into the functioning of
extensive teams or systems in engineering contexts.
These frameworks showcase the transformative potential of
LLM-based multi-agent systems in education, enabling highly
interactive environments where students engage with diverse
expert perspectives and solve complex engineering problems.
Their flexibility, scalability, and adaptability are invaluable for
real-world problem-solving in engineering education. For our
proposed MAS, we chose Camel AI [16] for its effective
role-playing and inception prompting, which facilitate agent
collaboration and interdisciplinary teamwork, breaking down
complex problems into manageable subtasks for each agent.


### III. Methodology

This section presents the methodology used to construct
and evaluate our Multi-Agent LLM (MAS LLM) framework
for supporting complex engineering problem-solving in SDPs.
The methodology is divided into two primary subsections:


#### A. MAS LLM Framework Construction

The first subsection outlines the technical details of how
the MAS LLM framework was developed. This includes the
LLM model used, the integration of the model into a multi-
agent system, and the customization of agent roles to simulate
diverse expert perspectives. We describe how the system
was designed to promote interdisciplinary collaboration and
support real-time feedback for students.

Concretely, we designed a copilot-style LLM-powered
MAS for engineering and computing students’ senior design
projects. Fig. 1 illustrates the system design of our proposed
MAS. This system comprises eight LLM agents:

1) Problem Formulation Agent
2) Breadth and Depth Agent
3) Ambiguity and Uncertainty Agent
4) System Complexity Agent
5) Technical Innovation and Risk Management Agent
6) Societal and Ethical Consideration Agent
7) Methodology and Approach Agent
8) Comprehensive Evaluation Agent
Each agent focuses on a different aspect of the SDP based
on its role. These agents are designed to act as experts by
crafting personas aligned with their respective roles. Each
agent receives its persona, project title, and detailed methodol-
ogy (extracted from PDF) of the proposed SDP (provided by

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

Fig. 1: Workflow Overview: 1) Input Submission: The student enters the project title and proposal PDF. 2) Proposal Processing:
Coordinator Agent forwards details to Tasks Agent to generate focused tasks. 3) Task Generation: Tasks Agent returns a list
of tasks. 4) Task Distribution: Tasks are sent to the Tasks Channel. 5) Task Assignment: Tasks are assigned to relevant agents.
6) Output Generation: Agents produce outputs and send them to the Tasks Channel and Coordinator Agent. 7) Input Linking:
Outputs from one agent can serve as inputs for others if needed. 8) User Output: Final results are displayed in the interface,
with summaries and detailed analysis.

the students). Figure 2 shows the detailed personas for each
agent used in our proposed MAS. OpenAI’s GPT-4o serves
as the primary backend LLM for these agents, as it currently
outperforms other LLMs [20].

a message history of the last 10 responses, enabling informed
outputs. Additionally, agents are equipped with Camel AI’s
Internet Search and Mathematics Toolkits, ensuring accurate
and well-rounded responses.

The proposed LLM-based MAS operates under a centralized
control mechanism managed by a Coordinator Agent, which
is responsible for overseeing task execution and ensuring
efficient collaboration between agents. Coupled with the Co-
ordinator Agent is a Task Agent, which decomposes each SDP
into a series of well-defined tasks for agents to handle. These
tasks are then assigned to agents according to their specialized
roles through a dedicated Task Channel, a feature in Camel AI
designed to streamline task distribution and monitoring [21].
Upon receiving their tasks, agents process them and return
outputs to the Task Channel, which routes them back to the
Coordinator Agent. The Coordinator evaluates these outputs
against predefined standards using a specialized feature from
Camel AI. As an LLM-based agent, the Coordinator generates
a requirements list based on the user-provided tasks, outlining
expectations with assistance from the Task Agent. If an agent’s
output falls short, the Coordinator reassigns the task—either
to another agent with relevant expertise or back to the original
agent with refined sub-goals. For tasks requiring collaboration,
the Coordinator ensures efficient routing of outputs between
agents, maintaining consistency and quality control. Once all
tasks are completed, the Coordinator synthesizes the outputs
into the final specified format. Agents operate as Critic Agents,
a Camel AI class designed to provide constructive feedback
and support complex decision-making. Each agent maintains

A snapshot of the user interface for our proposed LLM-
based MAS co-pilot is shown in Figure 7. To enhance in-
teractivity, we provide a follow-up questioning feature where
users can ask questions based on the MAS responses. The Co-
ordinator Agent analyzes the follow-up question and previous
agent responses to determine which agents are best suited to
answer, making the system dynamic and context-aware.

Box 1: Tree of Thoughts Prompting Template

“ Imagine X different experts answering this question.
All experts will write down 1 step of their thinking, and then
share it with the group.
Then all experts will go on to the next step, etc.
If any expert realizes they’re wrong at any point then they leave.
The question is... ”

Along with a MAS, we designed a single agent LLM using
GPT-4o to evaluate the SDPs to do a systematic and fair
evaluation. To make the single agent perform better from its
vanilla settings, we utilized the in-response Tree of Thoughts
(TOT) prompting technique [22], [23] to instruct this single
agent to simulate the behavior of multiple experts within its
response, each covering and evaluating different aspects of the
SDP. Box 1 shows the template we used to incorporate TOT
in our prompting. We used this template as a blueprint for

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

Fig. 2: Personas for each agent in the proposed MAS, detailing their tasks, objectives, and evaluation points for evaluating
engineering SDPs. The specialized agents—covering problem formulation, breadth and depth, ambiguity, complexity, innovation,
ethics, and methodology—enable systematic and holistic assessments across technical and non-technical dimensions.

creating a complete prompt for the single agent.


#### B. Evaluation Methodology

The second subsection explains how the framework was
evaluated. We detail the metrics used to assess the effective-
ness of the MAS LLM framework in enhancing student learn-
ing, collaboration, and problem-solving skills. This includes
both qualitative and quantitative data collection methods. We
also explain how the data was analyzed to assess the peda-
gogical and technical impact of the framework.

1) Comparing Faculty and Agent Scores: In a typical SDP
progression cycle, students write the initial proposal draft and
share it with their supervisor/advisor for feedback. Students
then incorporate the suggested changes into the proposal,
repeating this process multiple times to ensure the proposal
meets the standards set by the faculty at their institution. This
process takes a significant amount of time for both students
and supervisors to prepare the proposal before moving on to
the actual development phase of the project. We advocate for
the engineering and computing community to adopt this co-

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

#AgentsDetails1Problem Formulation AgentDescriptionYou are an AI assistant and expert in evaluation of Problem Formulation part of the Engineering Senior Year Design Projects.TaskAssess the clarity, depth, and scope of the problem statementObjectiveDetermine if the problem is appropriately complex and well-definedEvaluation Points* Does the proposal clearly articulate the engineering problem?* Is the complexity level of the problem aligned with advanced engineering challenges?* Does it highlight any interdisciplinary aspects or requirements that add to the complexity?* Are the societal, environmental, or ethical implications of the problem considered in the formulation?2Breadth and Depth AgentDescriptionYou are an AI assistant and expert in evaluation of Breadth and Depth part of the Engineering Senior Year Design Projects.TaskEvaluate the breadth (interdisciplinary aspects) and depth (in-depth analysis and specialized knowledge) required for solving the problem.ObjectiveCheck if the project goes beyond routine tasks and requires comprehensive engineering knowledge.Evaluation Points* Does the proposal show evidence of requiring interdisciplinary knowledge (e.g., integration of mechanical, electrical, or software engineering principles)?* Are specialized techniques, theories, or methods needed for this project?* Is there evidence of in-depth analysis, such as detailed background research or literature review, that supports problem formulation?3Ambiguity and Uncertainty AgentDescriptionYou are an AI assistant and expert in evaluation of Ambiguity and Uncertainty part of the Engineering Senior Year Design Projects.TaskIdentify areas in the proposal where uncertainty or ambiguity is present.ObjectiveAssess whether the project includes uncertain elements and requires assumptions or estimations.Evaluation Points* Are there data gaps or ambiguous elements in the problem that require assumptions or approximations?* Does the proposal acknowledge potential sources of uncertainty or unknown variables?* How well does the project formulation plan to address and manage this ambiguity?4System Complexity AgentDescriptionYou are an AI assistant and expert in evaluation of System Complexity part of the Engineering Senior Year Design Projects.TaskAnalyze the system complexity within the proposal.ObjectiveEvaluate whether the project involves multiple, interconnected components that add complexity.Evaluation Points* Does the problem involve managing interactions between multiple subsystems?* Are there dependencies or integrations that need special attention?* Is there a structured approach for managing these complex system interactions, such as a modular design or layered architecture?5Technical Innovation and Risk Management AgentDescriptionYou are an AI assistant and expert in evaluation of Technical Innovation and Risk Management part of the Engineering Senior Year Design Projects.TaskEvaluate the project's innovation level and technical unpredictability.ObjectiveDetermine if the project aims to push boundaries with novel approaches or technologies.Evaluation Points* Does the proposal include innovative solutions or cutting-edge technology that is technically challenging?* Are existing solutions insufficient, requiring new methods or adaptations?* Does the project plan account for or manage technical unpredictability?6Societal and Ethical Consideration AgentDescriptionYou are an AI assistant and expert in evaluation of Societal and Ethical Consideration part of the Engineering Senior Year Design Projects.TaskAssess the attention given to societal, environmental, and ethical factors.ObjectiveVerify if broader implications are acknowledged and addressed in the project.Evaluation Points* Are societal, environmental, or ethical impacts explicitly considered in the project proposal?* Does the proposal outline steps to mitigate any adverse effects or ethical concerns?* Is there a justification for how the project aligns with public safety, welfare, or environmental goals?7Methodology and Approach AgentDescriptionYou are an AI assistant and expert in evaluation of Methodology and Approach part of the Engineering Senior Year Design Projects.TaskCritique the methodology and approach proposed for solving the problem.ObjectiveEnsure that the methodology aligns with solving complex engineering problems and leverages appropriate analytical tools.Evaluation Points* Is the proposed methodology rigorous and well-suited for handling the identified complexity?* Are advanced analytical tools, simulations, or modeling approaches specified?* Does the methodology account for iterative testing, prototyping, or validation against real-world conditions?8Comprehensive Evaluation AgentDescriptionYou are an AI assistant and expert in evaluation of Comprehensive Evaluation part of the Engineering Senior Year Design Projects.TaskSynthesize evaluations from all other agents to provide an overall score and summary.ObjectiveOffer a holistic assessment of the project’s formulation, analysis, and methodology.Evaluation Points* How well does the project proposal align with ABET’s definition of complex engineering problems?* What are the overall strengths and weaknesses based on agent feedback?* Are there any key areas for improvement identified across multiple agents?Evaluation Criteria (Provided to All Agents)Evaluation Criteria* Point = Criteria: Reason* 1 = Not Addressed: The criterion is entirely absent from the proposal.* 2 = Minimally Addressed: The criterion is mentioned, but there is little or no depth in how it is addressed.* 3 = Partially Addressed: The criterion is covered, but the explanation or approach lacks completeness, depth, or detail.* 4 = Adequately Addressed: The criterion is reasonably well-addressed, with sufficient depth and clarity.* 5 = Thoroughly Addressed: The criterion is covered comprehensively, with detailed analysis and an insightful approach.Expected OutputYou should give a final score out of 5 based on the Evaluation Criteria and Evaluation Points, Strengths, Weaknesses and Suggestions.pilot system to enhance workflows and facilitate the develop-
ment of more advanced and effective co-pilot-style MAS for
SDP assistance.

For this evaluation, we asked four faculty members from the
Engineering and Computer Science departments at different
universities to provide feedback, which we used as a reference
standard. We recognize that these evaluations are subjective
and naturally vary among evaluators, so they are not an
absolute ground truth but serve as a comparative benchmark
for our system. The variability in these faculty scores is also
shown in Figure 6. This method uses three primary evaluation
scores to assess the effectiveness of our multi-agent system-
powered copilot in guiding engineering and computer science
students.

1) The Faculty Evaluation Score reflects faculty assess-
ments of key engineering and computing aspects within
each SDP proposal, providing a baseline measure of
project quality.

2) The Multi-Agent System Score represents scores gen-
erated by individual agents themselves, each focusing
on specific engineering and computing criteria aligned
with their programmed expertise.

3) The Single Agent Score represents scores generated by
a single agent itself using TOT to simulate different
experts to evaluate different aspects of the SDP.

Different engineering and computing aspects we selected
for this system are Problem Formulation, Breadth and Depth,
Ambiguity and Uncertainty, System Complexity, Technical
Innovation and Risk Management, Societal and Ethical Con-
siderations, and Methodology and Approach. Together, these
scores across each aspect offer a comprehensive view of
both the technical quality of student work and the impact
of agent-driven feedback in supporting educational outcomes
whether it is a MAS or single agent. We collected six SDP
proposals from students in the Engineering and Computer
Science departments at Information Technology University
[24]. All students had completed their SDPs (2023-2024).
To ensure anonymity, each proposal was renamed with a
randomly assigned number (between 1 & 6). In Section IV,
we will further discuss the evaluation results and performance
of our proposed methodology.

2) NLP-based Evaluation: To evaluate the performance of
both MAS and single-agent systems, we used the following
metrics as these criteria provide valuable insights into thematic
consistency, readability, and structural complexity in system
responses.

1) Clause Density [25] captures sentence complexity by
counting clauses per sentence, reflecting layered per-
spectives. Scores range from 1 (simple, single-idea sen-
tences) to 3+ (highly complex, multi-idea sentences).
2) Lexical Cohesion [26] measures thematic consistency
by analyzing word repetition or related terms, indicating
how well the content is built on multiple ideas. Scores
range from 0 (no cohesion) to 1 (full thematic consis-
tency).

3) Flesch-Kincaid Score [27] estimates readability, indi-
cating the U.S. grade level needed to understand the
text. A higher score suggests advanced content suitable
for expert readers, with an ideal range balancing ac-
cessibility and sophistication (0–16 scale) for academic
purposes.

4) Average Sentence Length indicates structural complex-
ity and content depth, with typical ranges from 10 to
40 words. Shorter sentences enhance readability, while
longer ones may reflect richer, nuanced perspectives but
can be harder to follow.

These metrics collectively assess the depth and accessibility of
each system’s response. Using these scores, we can evaluate
the performance of these systems from a NLP perspective.


### IV. Results
In this section, a comprehensive analysis of the results is
presented, focusing on faculty evaluations, error rates, and
NLP-based performance metrics. The evaluation based on
faculty scores is detailed in Figure 3. Error rates for each
system, reflecting their relative accuracy, are shown in Figure
4. Finally, the performance of each system, assessed using
NLP-based metrics, is illustrated in Figure 5.


#### A. Faculty Guided Evaluation Results

As outlined in Section III-B, we designed three distinct eval-
uation scores to assess the performance of our proposed MAS
for SDPs with respect to evaluation from faculty members.
This section further discusses key insights from the observed
scoring patterns and analysis.

The detailed results in Figure 3 show the performance of
each system across each aspect and SDP proposals. The graph
shows that the MAS consistently matches or outperforms the
single-agent system across all aspects, except for an isolated
project for the Breadth and Depth aspect. This can be seen
by the MAS score in each aspect being much closer to the
faculty evaluation scores and following the same trend.

Figure 4 presents the results showcasing the effectiveness
of the MAS in evaluating SDPs compared to the single-
agent system, with both systems benchmarked against faculty
evaluation scores. The MAS demonstrates greater alignment
with faculty evaluations, with a Mean Absolute Error (MAE)
of 0.205 compared to 0.388 for the single-agent system, an
89.3% accuracy improvement. The lower bars in the figure
represent closer alignment with faculty scores. The MAS
excels in technical categories such as Technical Innovation
and Risk Management (MAE 0.345 vs. 0.855) and System
Complexity (MAE 0.272 vs. 0.355). However,
in Breadth
and Depth, the single-agent system performs better (MAE
0.208 vs. 0.292), suggesting certain holistic aspects may favor
a unified approach. The MAS outperforms in Ambiguity
and Uncertainty (MAE 0.440 vs. 0.857) and Societal and
Ethical Considerations (MAE 0.355 vs. 0.772), demonstrating
its broader effectiveness. Both systems perform equally in
Methodology and Approach (MAE 0.293).

These results demonstrate the effectiveness of the MAS-
based approach in evaluating SDPs, with superior accuracy

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

Fig. 3: Visual representation of scores to evaluate the performance of both of our proposed multi-agent and single-agent systems
across each SDP (represented in numbers on the x-axis) for each aspect of engineering and computing. It can be seen that
multi-agent system scores are more aligned with faculty evaluation scores as compared to single-agent scores.

of complex ideation, structural coherence, and readability for
both students and supervisors.

As shown in Figure 5, the clause density of MAS-generated
responses is more aligned with the original proposals than
those from the single-agent system. This suggests the MAS
outputs are more detail-rich and convey more information per
sentence, enhancing their effectiveness. Examining the lexical
cohesion graph, MAS responses demonstrate stronger thematic
consistency, offering collaborative feedback that reflects in-
terconnected ideas. Different agents cover specific aspects,
building on each other’s inputs to produce nuanced outputs
that better aid students and supervisors.

The Flesch-Kincaid readability score indicates the U.S.
grade level required to comprehend responses on a first read.
For senior-year SDP students, an ideal score is between 14
and 16. Figure 5 shows that MAS responses mostly fall within
this range, indicating their suitability for senior students. The
Average Sentence Length metric shows sentence lengths in
both MAS and SA responses are similar to original proposals,
generally falling in the mid-range. This effect is primarily
attributed to the training methodology of the LLMs. Given
that both the MAS and single-agent systems rely on the same
backend LLM, this behavior is unsurprising.

The evaluations (§IV-A and §IV-B) reveal the MAS’s su-
perior performance over single-agent systems in evaluating
SDPs. MAS responses offer broader coverage in technical
aspects, clause density,
thematic consistency, and detailed
feedback, aligning with senior-year academic expectations but
with slightly longer sentence lengths. They excel in addressing
ethical and societal considerations. Conversely,
the single-
agent system shows higher error rates across metrics, except in
Breadth and Depth, where it aligns more closely with faculty

Fig. 4: Mean Absolute Error comparison between multi-agent
and single-agent systems against faculty evaluations. Lower
bars indicate closer alignment with faculty scores, with the
multi-agent system generally showing better accuracy.

across most assessment criteria due to its use of specialized
agents. While the MAS consistently excels in key areas,
including technical depth and ethical considerations, it lags
behind the single-agent system in the Breadth and Depth cate-
gory. This highlights an area for further refinement, reinforcing
the MAS’s potential as a robust and reliable tool for academic
project evaluation with targeted improvements.


#### B. NLP-based Evaluation Results

From an NLP perspective, we designed a mechanism to
evaluate the responses of the MAS and single-agent systems.
These metrics assess how each system performed in terms

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

Fig. 5: NLP-based performance evaluation of original student proposals, MAS responses, and single-agent system responses.
The metrics include Clause Density (complexity), Lexical Cohesion (thematic unity), Flesch-Kincaid Score (readability), and
Average Sentence Length (structural depth), designed to balance accessibility with scholarly depth. Our results show that the
MAS approach consistently outperforms the single-agent system across all evaluated metrics.

scores. This evaluation confirms that MAS-based LLMs are
better suited for complex problem-solving in engineering and
computer science due to the multifaceted demands of SDPs.


### V. Discussions


#### A. Situating our Initial Approach in the Agentic Landscape

The landscape of LLM agents and MAS is diverse, with
frameworks developed to leverage large language models for
complex, collaborative tasks. MAS, a research area since
the 1980s, underpins decentralized, autonomous problem-
solving in AI and robotics [10]. It facilitates agent
inter-
actions through cooperation, coordination, and negotiation,
often yielding emergent behaviors beyond individual agent
capabilities. However, LLMs alone lack the sophistication
to function as fully autonomous agents, needing plugins or
external tools for meaningful interaction with other systems.
Traditionally, MAS agents operate autonomously within an
environment to achieve specific goals [10].

In GenAI, an agent is typically a GenAI system, powered
by an LLM, engaging with external systems to execute actions

Fig. 6: Mean Faculty Evaluation Scores with standard de-
viations for SDP proposals. The variability illustrates the
subjective nature of assessments and the diversity in faculty
interpretations of evaluation criteria.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

more autonomous system with complex interaction capabilities
to tackle sophisticated engineering challenges.


#### B. Pedagogical Implications

instructors, and administrators. For students,

Our work significantly impacts educational stakeholders:
students,
the
multi-agent LLM system offers structured guidance through
a web-based co-pilot that aids in tackling complex, interdis-
ciplinary projects and fosters critical thinking. It provides a
practical tool to bridge knowledge gaps, covering areas like
ethics, technical complexity, and societal impact. However,
since current LLMs rely on human input and precise prompt
engineering, students may face challenges if inexperienced in
these areas [35]. The system mitigates this by offering struc-
tured problem-solving pathways. For instructors, it enhances
instructional efficiency by automating guidance, allowing fo-
cus on mentorship rather than technical issues. Administrators
find value in its support for accreditation efforts, providing a
scalable solution that aligns with multidisciplinary and real-
world educational goals.

To encourage further development and adaptation, we
have shared the code for our SDP complex problem-
solving co-pilot as an open-source resource (github.com/
AbdullahMushtaq78/ Multi-Agent-SDP-Copliot), allowing ed-
ucators and researchers to experiment with and extend the
system. By making our framework accessible, we aim to
contribute to the wider adoption of advanced multi-agent
LLM systems in engineering education, fostering a collabo-
rative movement toward practical tools that support complex
problem-solving in educational contexts.


### VI. Conclusions
In this paper, we explored Multi-Agent Large Language
Models (MAS LLMs) as an innovative framework for en-
hancing complex problem-solving in engineering senior design
projects. Leveraging the collaborative capabilities of MAS
alongside the generative strength of LLMs, we created a
dynamic and interdisciplinary environment that mirrors the
complexities faced in real-world engineering challenges. This
initiative enabled students to engage with various perspectives,
simulate trade-offs, and understand the intricacies of decision-
making within globalized engineering contexts. We conducted
evaluations of our MAS LLM system against a single-agent
system using a set of both custom-designed metrics favoring
university faculty perspectives and widely utilized NLP-based
metrics. Our results indicate that the MAS LLM framework
significantly enhances student learning by offering detailed
and ideation-rich responses, fostering collaboration, improv-
ing problem-solving skills, and facilitating real-time feedback
through follow-up questions, with MAS achieving an overall
accuracy of 89%. The findings also revealed that single-agent
systems often fail to align with faculty-assigned scores in most
engineering and computing aspects. This discrepancy arises
because single-agent systems tend to oversimplify responses,
and the response window of LLMs is inherently narrower
for individual agents than for the collective responses gen-
erated by multiple agents in MAS. The capacity of MAS to

Fig. 7: User interface for the proposed LLM-based MAS co-
pilot, enabling students to interact with a graphical interface.
Students can upload their SDP title and proposal, view sum-
maries and agent feedback, and submit follow-up questions
via the interface. This interface streamlines the feedback pro-
cess, promoting iterative learning and comprehensive project
assessment.

beyond the LLM itself [28]. For instance, ChatGPT’s code
interpreter in GPT-4 uses Python to autonomously manage
tasks like data analysis and plotting. This improves accuracy
through direct calculations based on user prompts but still
requires human oversight, not fully aligning with the tradi-
tional agent concept. There is growing interest in combining
the power of agents and LLMs3. Advanced frameworks like
the MRKL System [29] extend LLMs by using a central
LLM router to access tools for complex problem-solving.
Systems such as LangChain [30], AutoGen [31], and ReAct
[32] enhance agent autonomy by reducing human input, while
Camel AI [16] employs role-playing and inception prompting
for minimal intervention in agent collaboration. Building on
role-playing in engineering education [33] and the importance
of formative feedback [34], we harness these capacities in
multi-agent LLMs.

In this work, we introduce a Camel AI-based framework
for SDPs, providing a role-based environment simulating in-
terdisciplinary collaboration. Our system, an initial exploration
into LLM-based multi-agent systems, lacks advanced external
tool integration but still achieved 89% higher accuracy than
single-agent systems. While advanced coordination and tools
are beyond our current scope, future work aims to develop a

3https://llmagents-learning.org/f24

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.

[18] Z. Wang, S. Mao, W. Wu, T. Ge, F. Wei, and H. Ji, “Unleashing
the emergent cognitive synergy in large language models: A task-
solving agent through multi-persona self-collaboration,” arXiv preprint
arXiv:2307.05300, 2023.

[19] J. Moura, “Crew.ai: An open-source multi-agent orchestration frame-
work,” https://www.crewai.com/, 2024, accessed: October 12, 2024.
[20] OpenAI. [Online]. Available: https://openai.com/index/hello-gpt-4o
[21] CamelAI-Documentation. [Online]. Available: https://docs.camel-ai.org/

camel.html

[22] D. Hulbert, “Using tree-of-thought prompting to boost chatgpt’s rea-
soning,” https://github.com/dave1010/tree-of-thought-prompting, May
2023. [Online]. Available: https://doi.org/10.5281/zenodo.10323452
[23] E. Saravia, “Prompt Engineering Guide,” https://github.com/dair-

ai/Prompt-Engineering-Guide, 12 2022.

[24] InformationTechnologyUniversity, “Home - Information Technology

University — itu.edu.pk,” https://itu.edu.pk/, [Accessed 19-01-2025].

[25] D. Biber, B. Gray, and K. Poonpon, “Should we use characteristics
of conversation to measure grammatical complexity in L2 writing
development?” Tesol Quarterly, vol. 45, no. 1, pp. 5–35, 2011.

[26] M. A. K. Halliday and R. Hasan, Cohesion in english.

Routledge,

2014.

[27] J. Kincaid, “Derivation of new readability formulas (automated readabil-
ity index, fog count and Flesch reading ease formula) for navy enlisted
personnel,” Chief of Naval Technical Training, 1975.

[28] S. Schulhoff, M. Ilie, N. Balepur, K. Kahadze, A. Liu, C. Si, Y. Li,

#### A. Gupta, H. Han, S. Schulhoff et al., “The prompt report: A systematic
survey of prompting techniques,” arXiv preprint arXiv:2406.06608,
2024.

[29] E. Karpas, O. Abend, Y. Belinkov, B. Lenz, O. Lieber, N. Ratner,

#### Y. Shoham, H. Bata, Y. Levine, K. Leyton-Brown et al., “Mrkl systems:
A modular, neuro-symbolic architecture that combines large language
models, external knowledge sources and discrete reasoning,” arXiv
preprint arXiv:2205.00445, 2022.

[30] O. Topsakal and T. C. Akinci, “Creating large language model applica-
tions utilizing LangChain]: A primer on developing LLM apps fast,” in
International Conference on Applied Engineering and Natural Sciences,
vol. 1, no. 1, 2023, pp. 1050–1056.

[31] Q. Wu, G. Bansal, J. Zhang, Y. Wu, S. Zhang, E. Zhu, B. Li,

#### L. Jiang, X. Zhang, and C. Wang, “AutoGen: Enabling next-gen LLM
applications via multi-agent conversation framework,” arXiv preprint
arXiv:2308.08155, 2023.

[32] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao,
“ReAct: Synergizing reasoning and acting in language models,” arXiv
preprint arXiv:2210.03629, 2022.

[33] A. Hingle and A. Johri, “A framework to develop and implement role-
play case studies to teach responsible technology use,” IEEE Transac-
tions on Technology and Society, 2024.

[34] J. Qadir, A.-E. M. Taha, K.-L. A. Yau, J. Ponciano, S. Hussain, A. Al-
Fuqaha, and M. A. Imran, “Leveraging the force of formative assessment
& feedback for effective engineering education,” 2020.

[35] G. Sawalha, I. Taj, and A. Shoufan, “Analyzing student prompts and their
effect on chatgpt’s performance,” Cogent Education, vol. 11, no. 1, p.
2397200, 2024.

simulate expert personas that represent diverse stakeholders
and viewpoints allows for responses with higher attention
to detail, enhancing students’ understanding of the ethical,
technical, and social dimensions of their projects. Furthermore,
the framework’s adaptability to different project types across
various disciplines makes it a promising tool for broader adop-
tion by the engineering and computing education community.
While our study underscores the potential of MAS LLMs
in educational settings, future research can explore further
customization of agent behaviors and extend the framework to
fields beyond engineering and computer science. Additionally,
integrating more advanced evaluation metrics and conducting
longitudinal studies could offer deeper insights into the long-
term educational benefits of this approach, potentially influ-
encing curriculum development and instructional strategies.

REFERENCES

[1] A. R. Fernando, J. G. U. Vergara, and C. A. D. Canlapan, “Work in
progress: Perception of complex engineering problem among capstone
design students,” in 2022 IEEE Global Engineering Education Confer-
ence (EDUCON).

IEEE, 2022, pp. 14–16.

[2] J. Qadir, K.-L. A. Yau, M. A. Imran, and A. Al-Fuqaha, “Engineering
education, moving into 2020s: Essential competencies for effective 21st
century electrical & computer engineers,” in 2020 IEEE Frontiers in
Education Conference (FIE).

IEEE, 2020, pp. 1–9.

[3] J. Qadir and A. Al-Fuqaha, “A student primer on how to thrive
in engineering education during and beyond COVID-19,” Education
Sciences, vol. 10, no. 9, p. 236, 2020.

[4] J. Qadir, “Engineering education in the era of ChatGPT: Promise
and pitfalls of generative AI for education,” in 2023 IEEE Global
Engineering Education Conference (EDUCON).
IEEE, 2023, pp. 1–9.
[5] A. Johri, A. S. Katz, J. Qadir, and A. Hingle, “Generative artificial intel-
ligence and engineering education.” Journal of Engineering Education,
vol. 112, no. 3, 2023.

[6] A. Fischer, S. Greiff, and J. Funke, “The process of solving complex
problems,” The Journal of Problem Solving, vol. 4, no. 1, pp. 19–42,
2012.

[7] P. A. Frensch and J. Funke, “Definitions, traditions, and a general frame-
work for understanding complex problem solving,” in Complex problem
solving: The European perspective.
Lawrence Erlbaum Associates,
Hillsdale, NJ, 1995, pp. 24–43.

[8] P. M. Senge, The Fifth Discipline: The Art and Practice of the Learning

Organization. Doubleday, 1990.

[9] J. Surowiecki, The Wisdom of Crowds: Why the Many Are Smarter
Than the Few and How Collective Wisdom Shapes Business, Economies,
Societies, and Nations. Anchor, 2004.

[10] M. Wooldridge, An introduction to multiagent systems.

John wiley &

sons, 2009.

[11] M. A. Kuhail, I. Taj, S. Alimamy, and B. Abu-Shawar, “A review on
polyadic chatbots: trends, challenges, and future research directions,”
Knowledge and Information Systems, 2024.

[12] S. E. Page, The Difference: How the Power of Diversity Creates Better
Princeton University Press,

Groups, Firms, Schools, and Societies.
2007.

[13] M. Minsky, The Society of Mind. Simon and Schuster, 1986.
[14] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen,

#### J. Tang, X. Chen, Y. Lin et al., “A survey on large language model based
autonomous agents,” Frontiers of Computer Science, vol. 18, no. 6, p.
186345, 2024.

[15] T. Guo, X. Chen, Y. Wang, R. Chang, S. Pei, N. V. Chawla, O. Wiest,
and X. Zhang, “Large language model based multi-agents: A survey of
progress and challenges,” arXiv preprint arXiv:2402.01680, 2024.
[16] G. Li, H. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem, “Camel:
Communicative agents for “mind”’ exploration of large language model
society,” Advances in Neural Information Processing Systems, vol. 36,
pp. 51 991–52 008, 2023.

[17] Q. Wang, T. Wang, Q. Li, J. Liang, and B. He, “Megaagent: A
practical framework for autonomous cooperation in large-scale LLM
agent systems,” arXiv preprint arXiv:2408.09955, 2024.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:30:23 UTC from IEEE Xplore. Restrictions apply.


---

> *End of P-08*

<br><br>

<a id="p09-----llm-powered-multi-agent-systems-a-technical-framework-for-collaborative-intelligence-through-optimized-knowledge-retrieval-and-communication"></a>

## P-09 — LLM-Powered Multi-Agent Systems: A Technical Framework for Collaborative Intelligence Through Optimized Knowledge Retrieval and Communication

| Field | Details |
|-------|---------|
| **Paper ID** | `P-09` |
| **Title** | LLM-Powered Multi-Agent Systems: A Technical Framework for Collaborative Intelligence Through Optimized Knowledge Retrieval and Communication |
| **Authors** | Vineeth Gogineni |
| **Affiliation(s)** | Columbia Business School, Columbia University, New York, NY, USA |
| **Venue** | IEEE 3rd International Conference on Artificial Intelligence in Computing, Engineering and Sciences (AIRC) |
| **Volume / Year** | 2025 |
| **DOI** | — |

---

2025 6th International Conference on Artificial Intelligence, Robotics, and Control

LLM-Powered Multi-Agent Systems: A Technical
Framework for Collaborative Intelligence through
Optimized Knowledge Retrieval and
Communication

Vineeth Gogineni
Columbia Business School
Columbia University
NewYork, United States
goginenivineeth@gmail.com


### Abstract

This paper presents a comprehensive technical
framework for constructing effective multi-agent systems pow-
ered by large language models (LLMs). We examine how multiple
LLM-based agents can collaborate to solve complex problems
beyond the capabilities of single agents through specialized
knowledge integration and optimized communication protocols.
Our novel architecture enables efficient collaboration between
heterogeneous LLM agents, each with domain-specific capabili-
ties and knowledge bases. Experimental results demonstrate that
our multi-agent LLM system achieves 42% higher accuracy
on complex knowledge tasks, 37% reduction in hallucinations,
and 29% faster convergence on collaborative problem-solving
compared to baseline approaches. By implementing optimized
knowledge retrieval mechanisms and structured communica-
tion patterns, our system reduces token usage by 45% while
maintaining semantic fidelity across agent interactions. These
findings establish key design principles for building more effective
and reliable collaborative LLM-based multi-agent systems for
enterprise applications


### Index Terms / Keywords

Large language models, multi-agent systems,
retrieval-augmented generation, vector databases, prompt engi-
neering, knowledge retrieval

1) How can Retrieval-Augmented Generation (RAG) be
effectively integrated in a multi-agent context to ensure
knowledge consistency and accuracy?

2) What prompt engineering techniques optimize inter-
agent communication while minimizing token usage?
3) How can vector databases be structured to enable effi-
cient knowledge sharing across specialized agents with
distinct capabilities?


### II. Related Work


#### A. LLM-Based Multi-Agent Systems

Foundation models have increasingly become the basis
for agent-based systems. Park et al. [2] demonstrated how
LLM-based agents could be trained centrally but operate with
decentralized execution. Li and Singh [3] explored emergent
communication between foundation model agents, showing
that LLMs can develop specialized communication patterns.
Wang et al. [4] introduced a framework for multi-agent debate
using chain-of-thought prompting to enhance reasoning.


### I. Introduction


#### B. Retrieval-Augmented Generation

Recent advances in large language models (LLMs) have
created unprecedented opportunities for building sophisticated
multi-agent systems capable of complex problem solving
through collaboration. Unlike traditional multi-agent architec-
tures that rely on predefined rules, modern LLM-based agents
can leverage their emergent capabilities for flexible commu-
nication, task decomposition, and knowledge integration [1].
However, significant challenges remain in optimizing knowl-
edge retrieval across agents, ensuring coherent reasoning, and
maintaining factual accuracy in collaborative settings.

This research addresses three critical technical challenges

in LLM-based multi-agent systems:

RAG techniques have emerged as crucial components for
enhancing LLM factuality. Lewis et al. [5] introduced the
foundational RAG architecture combining dense retrieval with
generation. Nakano et al. [6] extended this to include recursive
retrieval for complex queries. However, these approaches
primarily focus on single-agent implementations, leaving open
questions about RAG optimization in multi-agent contexts
where retrieved knowledge must be shared and integrated
across agents.


#### C. Vector Databases and Knowledge Representation

Vector databases have become essential for efficient sim-
ilarity search in LLM applications. Johnson et al. [7] com-
pared performance characteristics of various vector database
implementations for semantic search. Zhang and Rodriguez

979-8-3315-4348-8/25/$31.00 ©2025 IEEE

452
Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:03 UTC from IEEE Xplore. Restrictions apply.

.

.

0
8
4
7
7
0
1
1
5
2
0
2
1
3
9
4
6
C
R
A
/
9
0
1
1
0
1
:
I

.

I

O
D
|
E
E
E
I

.

5
2
0
2
©
0
0
1
3
$
/
5
2
/
8
-
8
4
3
4
-
5
1
3
3
-
8
-
9
7
9
|
)
C
R
A
(

I

l

o
r
t
n
o
C
d
n
a
s
c
i
t
o
b
o
R

,
e
c
n
e
g

i
l
l

e
t
n

I

l

a
i
c
i
f
i
t
r
A
n
o
e
c
n
e
r
e
f
n
o
C

l

a
n
o
i
t
a
n
r
e
t
n

I

h
t
6
5
2
0
2


[8] proposed hierarchical embedding structures for organizing
knowledge in specialized domains.


#### D. Prompt Engineering and Optimization

Prompt engineering has emerged as a crucial discipline for
controlling LLM behaviors. Zhao et al. [9] explored how dif-
ferent prompting strategies impact reasoning capabilities. Wei
et al. [10] demonstrated the effectiveness of chain-of-thought
prompting for complex tasks. However, prompt optimization
specifically for agent communication remains underexplored.


### III. Methodology


#### A. System Architecture

Our experimental framework consists of a population of N
specialized LLM agents (N=5-20), each implemented using a
foundation model architecture tuned for specific capabilities.
Each agent incorporates:

Fig. 1. Architecture diagram of the multi-agent LLM system showing
the integration of RAG components, vector databases, and communication
protocols. Each agent contains its own specialized knowledge base and
retrieval system while sharing a common vector space for communication.

1) Core LLM: Foundation model (like GPT-4 or Claude)
fine-tuned on domain-specific data to specialize in the
agent’s area of expertise.

2) RAG Module: Retrieval system that accesses domain-
specific knowledge bases when the agent needs factual
information beyond its parameters. Includes custom doc-
ument processing, optimized chunking strategies, and
context integration mechanisms specific to the agent’s
domain.

3) Vector Database Interface: System for creating, stor-
ing, and querying semantic embeddings of knowledge
fragments for efficient similarity search.

4) Prompt Template Library: Collection of pre-optimized
instruction patterns designed for different agent interac-
tion scenarios and tasks. Templates are systematically
refined to maximize performance while minimizing to-
ken usage across various communication contexts.

5) Communication Protocol: Standardized message for-

mat for inter-agent exchanges

Fig. 1 illustrates the overall system architecture, highlighting
the integration between components.

Fig. 2 presents a comprehensive process flow diagram of
our multi-agent LLM system, showing the lifecycle of a task
from initial request to final output synthesis.
The process flow operates as follows:
1) Task Reception & Analysis: The coordinator agent re-
ceives the initial task, performs complexity assessment,
and identifies required domain expertise.

2) Task Decomposition: Complex tasks are broken down
into subtasks with defined dependencies and interfaces
between them.

3) Agent Selection & Assignment: Based on the task
requirements, appropriate specialized agents are selected
from the agent pool and assigned specific responsibili-
ties.

4) Parallel Knowledge Retrieval: Agents simultaneously
retrieve relevant information from their specialized
knowledge bases using optimized retrieval parameters.

Fig. 2. Process flow diagram of the multi-agent LLM system. The diagram
illustrates: (1) Task reception and decomposition by the coordinator agent,
(2) Task allocation to specialized agents based on capabilities, (3) Parallel
knowledge retrieval and processing by individual agents, (4) Inter-agent
communication and knowledge sharing, (5) Progressive refinement through
collaborative reasoning, (6) Conflict resolution and consensus building, and
(7) Final output synthesis and validation. Feedback loops enable iterative
improvement throughout the process.

5) Initial Processing: Each agent processes its retrieved
information and generates preliminary insights or solu-
tions for its assigned subtask.

6) Structured Communication: Agents exchange infor-
mation using optimized communication protocols, shar-
ing relevant insights and requesting additional informa-
tion as needed.

7) Collaborative Reasoning: Through multiple rounds of
interaction, agents build upon each other’s work, chal-
lenge assumptions, and refine their understanding.

8) Conflict Resolution: When disagreements arise, agents
engage in structured debate using evidence from their
knowledge bases to reach consensus.

9) Progressive Synthesis: As subtasks are completed, re-
sults are progressively integrated into a cohesive solu-
tion.

10) Validation & Refinement: The emerging solution un-

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:03 UTC from IEEE Xplore. Restrictions apply.

453
dergoes continuous validation against requirements, with
feedback loops triggering additional retrieval or reason-
ing as needed.

11) Final Output Generation: Once validation criteria are
met, the coordinator agent synthesizes the final output
with appropriate confidence levels and supporting evi-
dence.

This process flow is designed to maximize parallel processing
while ensuring effective knowledge integration across agent
boundaries. The structured communication protocols and de-
fined interfaces between subtasks enable efficient collaboration
without excessive coordination overhead.


#### B. RAG Integration for Multi-Agent Systems

We implement and compare three different RAG architec-

tures for multi-agent knowledge retrieval:

2) Task Delegation: Templates for assigning responsibili-

ties

3) Consensus Building: Templates for resolving disagree-

ments

4) Status Updates: Templates for progress reporting
5) System Prompts: Templates for defining agent roles and

constraints

For each template category, we performed systematic opti-
mization through:

1) Token usage minimization while preserving semantic

content

2) Explicit structure markers for reliable parsing
3) Few-shot examples tailored to specific interaction types
4) Strategic use of delimiter tokens for consistent extraction


#### E. Evaluation Tasks

1) Independent RAG: Each agent maintains its own re-

We evaluated system performance across three task do-

trieval system with no knowledge sharing

mains:

2) Centralized RAG: All agents access a common retrieval

system

3) Federated RAG: Agents maintain specialized knowl-
edge bases but share retrievals through a distributed
protocol

1) Complex Knowledge Synthesis: Requiring integration
of information across multiple specialized domains
2) Collaborative Problem-Solving: Multi-step reasoning

tasks requiring diverse capabilities

3) Adversarial Fact-Checking: Identifying and correcting


#### C. Vector Database Implementation

We implemented and evaluated three vector database con-

figurations:

1) Flat Namespace: All embeddings stored in a single
collection without any hierarchical organization. This
approach offers simplicity and ease of implementation
but suffers from degrading performance as collection
size increases.

2) Hierarchical Collections: Embeddings organized by
domain and subtopic in a predefined taxonomy. This
structure enables more targeted retrieval by limiting
search to relevant domains, improving both precision
and latency.

3) Dynamic Clustering: Embeddings automatically orga-
nized based on semantic similarity using unsupervised
clustering algorithms. This approach adapts to emergent
patterns in the data but may create less intuitive group-
ings than human-designed hierarchies.

The vector databases were implemented using FAISS (Face-
book AI Similarity Search) and Pinecone, with hybrid search
capabilities incorporating sparse and dense representations.
Specifically, the FAISS implementation used HNSW (Hierar-
chical Navigable Small World) indices for the Flat Namespace,
while Pinecone’s pod-based architecture was leveraged for the
Hierarchical Collections.

errors in presented information
For each task domain, we measured:

1) Accuracy: Correctness of final outputs
2) Hallucination Rate: Frequency of generated facts with-

out support

3) Token Efficiency: Total tokens used to complete tasks
4) Time to Convergence: Steps required to reach stable

solutions

5) Knowledge Integration: Effective utilization of infor-

mation across agent boundaries


#### A. RAG Architecture Performance


### IV. Results

Our experiments revealed significant performance differ-
ences between RAG integration approaches. Fig. 3 illustrates
the relative performance of each RAG architecture on knowl-
edge synthesis tasks.

Federated RAG demonstrated superior performance with 42%

fewer hallucinations compared to Independent RAG and 23%
better knowledge integration compared to Centralized RAG.

These metrics were measured through expert evaluation of
outputs on medical literature analysis, financial document syn-
thesis, and scientific research integration tasks. Hallucination
rates were assessed by domain experts identifying unsupported
claims, while knowledge integration was scored based on
effective cross-domain synthesis.


#### D. Prompt Engineering for Agent Communication


#### B. Vector Database Efficiency

We developed a comprehensive prompt template library

optimized for different inter-agent interaction patterns:

1) Knowledge Requests: Templates for requesting specific

Analysis of vector database implementations revealed sub-
stantial differences in retrieval performance and storage effi-
ciency. The hierarchical collection organization demonstrated

information

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:03 UTC from IEEE Xplore. Restrictions apply.

454• 45% reduction in token usage
- 29% faster convergence on collaborative problem-solving
We evaluated against industry baselines from Thomson
Reuters, Bloomberg Terminal, Capital IQ, and a leading finan-
cial firm’s in-house workflow, using a standardized test suite
with blind assessment protocols by financial professionals.

In our financial document analysis case study, the system
with 8 specialized agents processed 500+ documents totaling
over 15,000 pages and outperformed industry baselines with:
- 41% more identified risk factors with supporting evidence
- 52% reduction in false positives
- 37% higher specificity in recommendations
- 68% faster processing time


### V. Discussion

The experimental results highlight several key technical

insights for building effective multi-agent LLM systems:


#### A. RAG Architecture Design Principles

Our findings suggest specific design principles for imple-

menting RAG in multi-agent contexts:

1) Balancing Specialization and Integration: Federated
RAG maintains specialized knowledge bases with struc-
tured sharing protocols, outperforming both fully inde-
pendent and centralized approaches.

2) Retrieval Depth vs. Breadth: Domain-specific queries
perform better with deeper retrieval within a narrow
domain, while integrative tasks benefit from broader
retrieval across domains.

3) Cross-Agent Reranking: Secondary reranking consid-
ering retrievals from multiple agents reduced redundancy
by 43% while improving coverage of relevant informa-
tion.


#### B. Vector Database Optimizations

Our vector database experiments revealed several critical

design considerations:

1) Embedding Specialization: Domain-specific

tuning of embedding models
precision by 23% compared
embeddings.

fine-
improved
retrieval
to general-purpose

2) Hybrid Indexing Strategies: Combining dense vector
search with sparse retrieval (BM25) provided 31% im-
provement in retrieval accuracy compared to embedding-
only approaches.

3) Namespace Design: Hierarchical collections outper-
formed flat namespace approaches with 40% faster query
times and 25% higher precision, particularly as collec-
tion size scaled.

Fig. 3. Performance comparison of RAG architectures on knowledge synthesis
tasks. The radar chart shows normalized scores across five dimensions: accu-
racy, hallucination reduction, token efficiency, query latency, and knowledge
breadth. Note the superior performance of Federated RAG in balancing these
factors.

superior performance for domain-specific queries, while dy-
namic clustering showed better adaptability to evolving knowl-
edge.

These substantial differences

in performance metrics
demonstrate why the choice of vector database implementation
is critical. The Hierarchical Collections approach achieved 40%
faster query times compared to Flat Namespace, with 25%
higher precision at the cost of slower update times. Dy- namic
Clustering offered a balance between performance and
adaptability, particularly valuable for domains with evolving
terminology and concepts.


#### C. Prompt Engineering Impact

Our prompt optimization techniques demonstrated signif-
icant improvements in communication efficiency and task
performance.

The optimized prompt library reduced total token consump-
tion by 45% while maintaining equivalent task performance,
from an average of 24,856 tokens per complex task before op-
timization to 13,670 tokens after optimization. This reduction
was achieved through several complementary techniques:
1) Standardized prefix tokens for message typing
2) Consistent JSON schema for structured data exchange
3) Explicit chain-of-thought sections for sharing reasoning

steps

4) Compressed instruction formats with shared defaults


#### D. Overall System Performance

Our integrated system combining optimized RAG architec-
ture, vector database implementation, and prompt engineering
demonstrated substantial performance improvements across all
evaluation tasks:


#### C. Prompt Engineering and Communication Efficiency

Our prompt optimization experiments yielded several valu-

able insights:

- 42% higher accuracy on complex knowledge tasks
- 37% reduction in hallucinations

1) Structural Consistency: Standardized message formats
with consistent delimiters reduced token usage from

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:03 UTC from IEEE Xplore. Restrictions apply.

455


[3] Y. Li and A. Singh, ”Emergent communication in LLM-based multi-
agent systems,” in Conference on Neural Information Processing Sys-
tems, 2023, pp. 5782-5794.

[4] L. Wang et al., ”Chain-of-thought reasoning for multi-agent debate,”
in Proceedings of the 61st Annual Meeting of the Association for
Computational Linguistics, 2023, pp. 789-801.

[5] P. Lewis et al., ”Retrieval-augmented generation for knowledge-intensive
NLP tasks,” in Advances in Neural Information Processing Systems,
2020, pp. 9459-9468.

[6] R. Nakano et al., ”WebGPT: Browser-assisted question-answering with

human feedback,” arXiv preprint arXiv:2112.09332, Dec. 2021.

[7] M. Johnson, J. Lee, and R. Chen, ”Performance evaluation of vector
databases for similarity search applications,” in Proceedings of the
International Conference on Very Large Data Bases, 2023, pp. 245-257.
[8] Q. Zhang and M. Rodriguez, ”Hierarchical embedding struc-
tures for domain-specialized knowledge retrieval,” arXiv preprint
arXiv:2309.09425, Sep. 2023.

[9] H. Zhao et al., ”Prompt engineering strategies for large language models:
A comprehensive analysis,” Journal of Artificial Intelligence Research,
vol. 68, pp. 231-270, Mar. 2023.

[10] J. Wei et al., ”Chain-of-thought prompting elicits reasoning in large lan-
guage models,” in Advances in Neural Information Processing Systems,
2022, pp. 24824-24837.

[11] T. Brown et al., ”Language models are few-shot learners,” in Advances
in Neural Information Processing Systems, 2020, pp. 1877-1901.
[12] J. Devlin et al., ”BERT: Pre-training of deep bidirectional transformers
for language understanding,” in Proceedings of the 2019 Conference
of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies, 2019, pp. 4171-4186.
[13] K. Guu et al., ”REALM: Retrieval-augmented language model pre-
training,” in Proceedings of the 37th International Conference on
Machine Learning, 2020, pp. 3929-3938.

[14] S. Robertson and H. Zaragoza, ”The probabilistic relevance framework:
BM25 and beyond,” Foundations and Trends in Information Retrieval,
vol. 3, no. 4, pp. 333-389, 2009.

[15] N. Malkin et al., ”RAG vs. fine-tuning: Comparing effectiveness, effi-
ciency, and controllability,” arXiv preprint arXiv:2307.09288, Jul. 2023.
[16] J. Du et al., ”GLAM: Efficient scaling of language models with mixture-
of-experts,” in Proceedings of the 39th International Conference on
Machine Learning, 2022, pp. 5547-5569.

[17] Y. Liu et al., ”Improving language understanding by generative pre-

training,” OpenAI Technical Report, 2018.

[18] T. Z. Zhao et al., ”WebGLM: Towards browser-assisted large language

models,” arXiv preprint arXiv:2306.03500, Jun. 2023.

[19] A. Talmor et al., ”CommonsenseQA: A question answering challenge
targeting commonsense knowledge,” in Proceedings of the 2019 Con-
ference of the North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies, 2019, pp. 4149-4158.
[20] A. Vaswani et al., ”Attention is all you need,” in Advances in Neural

Information Processing Systems, 2017, pp. 5998-6008.

[21] D. Khashabi et al., ”UNIFIEDQA: Crossing format boundaries with a
single QA system,” in Findings of the Association for Computational
Linguistics: EMNLP 2020, 2020, pp. 1896-1907.

[22] D. Adiwardana et al., ”Towards a human-like open-domain chatbot,”

arXiv preprint arXiv:2001.09977, Jan. 2020.

[23] A. Radford et al., ”Language models are unsupervised multitask learn-

ers,” OpenAI blog, vol. 1, no. 8, p. 9, 2019.

[24] R. Cai et al., ”Hierarchical vector search for efficient knowledge
retrieval,” in Proceedings of the 29th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, 2023, pp. 4567-4576.

[25] S. Li et al., ”Efficient vector databases for AI applications: A per-
formance comparison,” IEEE Transactions on Knowledge and Data
Engineering, 2023, (in press).

24,856 to 13,670 tokens per complex task while main-
taining performance.

2) Context Management: Shared context registry with
versioning allowed agents to reference rather than repeat
common knowledge, reducing redundant information
transfer.

3) Reasoning Transparency: Chain-of-thought prompt-
ing improved collaborative problem-solving by making
agent reasoning steps transparent to other agents.


#### D. Implementation Costs and Considerations

While our multi-agent architecture demonstrated significant
performance improvements, implementation involves several
cost considerations:

1) Computational Resources: Federated RAG requires
3-5x more GPU memory than single-agent systems,
increasing per-query costs from approximately $0.08 to
$0.23.

2) Training and Fine-tuning: Each specialized agent re-
quired 2-5 hours of fine-tuning on 8 A100 GPUs, with
costs ranging from $500-$1,200 per agent.

3) Knowledge Base Development: Initial corpus develop-
ment and annotation required approximately 120 person-
hours per specialized domain.

4) System Integration: Communication protocols and co-
ordination mechanisms required substantial development
effort, though these costs amortize with scale.

5) Maintenance Overhead: Ongoing knowledge base up-
dates, embedding refreshes, and prompt optimization
require dedicated resources.

For high-value applications where accuracy and comprehen-
sive knowledge integration are critical, these higher imple-
mentation costs may be justified by the performance improve-
ments.


### VI. Conclusion

This research establishes a comprehensive technical frame-
work for enhancing multi-agent LLM systems through opti-
mized RAG integration, vector database design, and prompt
engineering. Our Federated RAG architecture, hierarchical
vector collections, and communication-optimized prompting
techniques demonstrate significant performance improvements
across knowledge-intensive collaborative tasks.

The findings provide practical design principles for building
more effective and efficient multi-agent AI systems that can
maintain factual accuracy while enabling sophisticated col-
laborative reasoning. The demonstrated reductions in hallu-
cinations, token usage, and convergence time address critical
limitations in current LLM-based agent systems.

REFERENCES

[1] A. B. Chen and M. Singh, ”Foundation models as the basis for
collaborative AI,” in Proceedings of the International Conference on
Autonomous Agents and Multiagent Systems, 2023, pp. 412-421.

[2] J. Park, C. Williams, and S. Lee, ”Centralized training for decen-
tralized execution in large language model agents,” arXiv preprint
arXiv:2310.12823, Oct. 2023.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:29:03 UTC from IEEE Xplore. Restrictions apply.

456


---

> *End of P-09*

<br><br>

<a id="p10-----large-language-models-for-software-engineering-survey-and-open-problems"></a>

## P-10 — Large Language Models for Software Engineering: Survey and Open Problems

| Field | Details |
|-------|---------|
| **Paper ID** | `P-10` |
| **Title** | Large Language Models for Software Engineering: Survey and Open Problems |
| **Authors** | Angela Fan, Beliz Gokkaya, Mark Harman, Mitya Lyubarskiy, Shubho Sengupta, Shin Yoo, and Jie M. Zhang |
| **Affiliation(s)** | (1) Meta Platforms Inc. (Generative AI Team / PyTorch / Instagram / FAIR / Developer Infrastructure), USA<br>(2) School of Computing, KAIST, Daejeon, Republic of Korea<br>(3) Department of Informatics, King's College London, UK |
| **Venue** | IEEE/ACM International Conference on Software Engineering: Future of Software Engineering (ICSE-FoSE) |
| **Volume / Year** | 2023 |
| **DOI** | [10.1109/ICSE-FoSE59343.2023.00008](https://doi.org/10.1109/ICSE-FoSE59343.2023.00008) |

---

2023 IEEE/ACM International Conference on Software Engineering: Future of Software Engineering (ICSE-FoSE)

Large Language Models for Software Engineering:
Survey and Open Problems

Angela Fan
Generative AI Team
Meta Platforms Inc.
New York, NY, USA

Beliz Gokkaya
PyTorch Team
Meta Platforms Inc.
Menlo Park, CA, USA

Mark Harman
Instagram Product Foundation
Meta Platforms Inc.
London, UK

Mitya Lyubarskiy
Developer Infrastructure
Meta Platforms Inc.
London, UK

Shubho Sengupta
FAIR
Meta Platforms Inc.
Menlo Park, CA, USA

Shin Yoo
School of Computing
KAIST
Daejeon, Korea

Jie M. Zhang
Department of Informatics
King’s College London
London, UK


### Abstract

This paper provides a survey of the emerging area
of Large Language Models (LLMs) for Software Engineering
(SE). It also sets out open research challenges for the application
of LLMs to technical problems faced by software engineers.
LLMs’ emergent properties bring novelty and creativity with
applications right across the spectrum of Software Engineering
activities including coding, design, requirements, repair, refac-
toring, performance improvement, documentation and analytics.
However, these very same emergent properties also pose signif-
icant technical challenges; we need techniques that can reliably
weed out incorrect solutions, such as hallucinations. Our survey
reveals the pivotal role that hybrid techniques (traditional SE
plus LLMs) have to play in the development and deployment of
reliable, efﬁcient and effective LLM-based SE.


### Index Terms / Keywords

Automated Program Repair, Documentation
generation, Generative AI, Genetic Improvement, Human-
Computer Interaction, Large Language Models, Refactoring,
Requirements engineering, Search Based Software Engineering
(SBSE), Software Analytics, Software Engineering Education,
Software Processes, Software Maintenance and Evolution, Soft-
ware Testing.


### I. Introduction

This paper surveys the recent developments, advances and
empirical results on LLM-based SE; the application of Large
Language Models (LLMs) to Software Engineering (SE) ap-
plications. We use the survey to highlight gaps in this rapidly
developing, but as yet embryonic, research literature. Based
on gaps in the literature and technical opportunities, we
also identify open problems and challenges for the software
engineering research community.

While any survey of such a rapidly expanding area can
neither aspire nor claim to be comprehensive, we hope that this
survey will provide a useful and relatively complete snapshot
of the early universe of this exciting new subdiscipline of
Software Engineering: LLM-based Software Engineering. Al-
though the scientiﬁc and technical structure of the ﬁeld is still
emerging, it is already possible to identify trends, productive
avenues for future research, and important technical challenges
that need to be addressed.

In particular, we are already able to discern important
connections to (and resonance with) existing trends and well-
established approaches and subdisciplines within Software En-
gineering. Furthermore, although we ﬁnd considerable grounds
for optimism, there remain important technical challenges,
which are likely to inform the research agenda for several
years. Many authors have highlighted, both scientiﬁcally and
anecdotally,
that hallucination is a pervasive problem for
LLMs [1] and also that it poses speciﬁc problems for LLM-
based SE [2]. As with human intelligence, hallucination means
that the LLM can create ﬁctitious output. In the context of
software engineering, it means that the engineering artefacts
created could be incorrect, yet appear plausible; LLMs may
introduce bugs.

However, unlike many other applications of LLMs, software
engineers are typically blessed with automatable ground truth
(software execution), against which most software engineering
artefacts can be evaluated. Also,
the software engineering
research community has already devoted a great deal of time
to producing automated and semi-automated techniques for
checking the potentially incorrect results produced by humans.
This means that, for the discipline and the research community,
there is a great deal of experience and expertise on which
to draw, when tackling the challenges posed by issues like
hallucination.

Clearly, automated testing techniques [3]–[5] will have a
central role to play in ensuring correctness, just as they already
do for human-engineered artefacts. When generating entirely
new features and systems, automated test data generation
suffers from the lack of an automatable oracle [6] (an au-
tomated technique for determining whether output behaviour
is correct for a given input stimulus). Given LLMs’ propensity
to hallucinate, the Oracle Problem will remain highly relevant,
and solutions to it will become all the more impactful [7].

However, some SE applications concern adaption, improve-
ment and development of existing software systems, for which
there is a readily-available automatable oracle: the functional
behaviour of the original system.

979-8-3503-2496-9/23/$31.00 ©2023 IEEE
DOI 10.1109/ICSE-FoSE59343.2023.00008

31

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

.

.

8
0
0
0
0
3
2
0
2
3
4
3
9
5
E
S
O
F
-
E
S
C
I
/
9
0
1
1
0
1
:
I

.

O
D
|
E
E
E
I

.

3
2
0
2
©
0
0
1
3
$
/
3
2
/
9
-
6
9
4
2
-
3
0
5
3
-
8
-
9
7
9
|
)
E
S
o
F
-
E
S
C
I
(
g
n
i
r
e
e
n
g
n
E
e
r
a
w

i

t
f
o
S
f
o
e
r
u
t
u
F
:
g
n
i
r
e
e
n
g
n
E
e
r
a
w

i

t
f
o
S
n
o
e
c
n
e
r
e
f
n
o
C

l

a
n
o
i
t
a
n
r
e
t
n

I

M
C
A
/
E
E
E
I

3
2
0
2


In this paper, we call this the ‘Automated Regression Ora-
cle’, an approach that has already proved advantageous in the
ﬁeld of Genetic Improvement [8]. The Automated Regression
Oracle simply uses the existing version of the software system
as a reference against which to benchmark output from any
subsequent adaptions and changes.

Of course, there is a risk of ‘baking in’ functional incor-
rectness, since the Automated Regression Oracle cannot detect
what the system should do, but only capture what it currently
does. Therefore, the Automated Regression Oracle can test
only for functional regressions so it is best suited to use cases
where the existing functionality is to be maintained. For ex-
ample, for non-functional improvements such as performance
optimisation and for semantics-preserving refactoring.

The input provided to an LLM will be a natural focus of
growing research, and we can expect a rapid development of
the literature on prompt engineering and prompt optimisation
[9]. In this survey, we highlight existing work and open
challenges for prompt engineering with regard to several
speciﬁc aspects of software engineering.

The output from an LLM need not be conﬁned purely to
code, but can also include other software engineering arte-
facts, such as requirements, test cases, design diagrams, and
documentation. In general, the language-based nature of an
LLM, allows it to generate any linguistically-deﬁned software
engineering artefact.

We typically think of the software engineering artefact as
the primary output of the LLM, but it is not the only output.
The explanation provided with the primary output is also an
important output of any LLM. Our survey highlights the need
for much more research, not only into optimising prompt
engineering (which focuses on the input to the LLM) but also
the need for work on the optimisation of explanations provided
with the primary output.

LLMs are inherently nondeterministic: the same prompt
produces different answers on different inference executions
(unless the temperature is set to zero, which has often been
found to be suboptimal over multiple executions) [10]. Further-
more, irrespective of the temperature setting, subtle changes
in the prompt can lead to very different outputs [10]. As well
as motivating ‘prompt engineering’ and output processing, this
nondeterministic behaviour raises challenges for the scientiﬁc
evaluation of LLM-based Software Engineering:

If results can vary each time we run the process,
how can we determine whether a proposed technique
achieves an advance over the state of the art?

This is a problem that has already been well studied in the
context of Empirical Software Engineering [11] and Search
Based Software Engineering (SBSE) [12]. In particular, SBSE
bears many similarities to LLM-based Software Engineering,
sharing with it the need to achieve robust scientiﬁc evaluation
in the presence of noisy, non-deterministic, and incomplete
results [13], [14]. There is, therefore, already a mature soft-
ware engineering literature on just the kind of robust scientiﬁc
evaluation techniques needed to cater for LLM-based scientiﬁc
evaluation.

For example, well-studied techniques, such as parametric
and non-parametric inferential statistics, are now routinely
used to provide robust scientiﬁc conclusions in the presence
of highly non-deterministic algorithms in the SBSE discipline.

TABLE I
A (ALL) DENOTES ALL PREPRINTS THAT ARE CATEGORISED UNDER CS
(COMPUTER SCIENCE). L (LLM) DENOTES PREPRINTS WHOSE TITLE OR

### Abstract

INCLUDES “LLM”, “LARGE LANGUAGE MODEL”, OR “GPT”.
L ∩ S DENOTES PREPRINTS IN CS.SE OR CS.PL CATEGORY WHOSE TITLE
OR ABSTRACT INCLUDES THE SAME KEYWORDS. NOTE THAT THE YEAR
2023 ONLY INCLUDES DATA UP TO 27 JULY 2023.

Year

2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023

|A|

|L|

|L ∩ S|

|L|
|A| (%)

|L∩S|
|L|

(%)

2,238
3,645
4,873
7,543
9,114
12,316
14,933
16,320
18,818
23,707
30,746
41,927
55,325
71,431
77,520
81,964
52,547

0
0
0
0
0
0
0
0
0
0
0
0
36
99
192
434
1,665

0
0
0
0
0
0
0
0
0
0
0
0
0
5
13
45
181

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.25
0.53
3.17

0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
5.05
6.77
10.36
10.87

In order to understand the growth trends within LLM-based
Software Engineering, we performed a manual analysis of data
on the number of publications on speciﬁc topics from arXiv.
Table I contains the raw data1, which was manually extracted
from the arXiv metadata dump made publicly available via
Kaggle (https://www.kaggle.com/datasets/Cornell-University/
arxiv), accessed on the 27th. July 2023. We ﬁrst ﬁltered
out publications for which the classiﬁcation code does not
start with the cs preﬁx (i.e., Computer Science), resulting in
column A.

To identify Computer Science papers that are relevant to
LLMs, we ﬁltered the publications into subcategories on
artiﬁcial intelligence (cs.AI), machine learning (cs.LG), neural
and evolutionary computation (cs.NE), software engineering
(cs.SE), and programming language (cs.PL) using the queries
“Large Language Model”, “LLM”, and “GPT” in either the
title or the abstract (we manually excluded instances of over-
loaded acronyms such as GPT for General Planning Tool),
resulting in column L. Finally, we used the same queries to
identify LLM-based Software Engineering papers in software
engineering (cs.SE) and programming language (cs.PL). These
queries are inherently approximate, so we conﬁne ourselves
only to conclusions based on overall trends for which there
is strong evidence rather than speciﬁc details of the numbers
observed. Nevertheless, we report the raw numbers observed
to support replication by others.

1The numbers for 2023 are underestimated since the data was accessed in

July 2023.

32

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

Fig. 1. A mapping between software development activities, research domains, and the paper structure

Also, given the recent upsurge in attention for LLMs, the
exponential rise in the number of papers on LLMs is relatively
unsurprising.

Perhaps more interesting is the rapid uptake of Software
Engineering applications of LLMs, as revealed by the growth
trend, pictured in green on this ﬁgure. In order to examine
this trend in more detail, we plot the proportion of LLM pub-
lications (L) to all CS publications (A) in blue, as well as the
proportions of LLM-based software engineering publications
(L ∩ S) to all LLM publications in orange in Figure 3. As
can be seen, the proportion of LLM papers on LLM-based
Software Engineering has been rising dramatically since 2019.
Already, more than 10% of all papers on LLMs are concerned
with LLM-based Software Engineering.

As a result of this growth, we can expect many other surveys
of LLM-Based SE. The rapid expansion of the literature makes
it unlikely that further comprehensive SE-wide studies will ﬁt
the space constraints of a single paper, but we can expect many
speciﬁc comprehensive surveys of sub-areas of interest, and
also Systematic Literature Reviews (SLRs) that tackle SE-wide
crosscutting issues by asking speciﬁc research questions of
the primary literature in the systematic review. Already, such
SLRs are appearing. For example, Hou et al. [15] provided
an excellent recent SLR covering 229 research papers from
2017 to 2023 reporting SE tasks tackled, data collection and
preprocessing techniques, and strategies for optimising LLM
performance (such as prompt engineering).

The remainder of this paper is organised to follow the top-
level software development activities and research domains as
depicted in Figure 1.


### II. Preliminaries


#### A. Large Language Models

A Large Language Model (LLM) refers to an Artiﬁcial
Intelligence (AI) model that has been trained on large amounts
of data and is able to generate text in a human-like fashion.
Table III provides a glossary of LLM terminology to make the
paper self-contained.

Fig. 2. Trends in number of arXiv preprints. The blue line denotes the number
of preprints categorised under “CS”. The orange line denotes the number of
preprints in AI (cs.AI), Machine Learning (cs.LG), Neural and Evolutionary
Computing (cs.NE), Software Engineering (cs.SE), and Programming Lan-
guage (cs.PL) whose title or abstract contains either “Large Language Model”,
“LLM”, or “GPT”. The green line denotes the number of preprints in SE and
PL categories whose title or abstract contains either “Large Language Model”,
“LLM”, or “GPT”

Fig. 3. Proportions of LLM papers and SE papers about LLMs. By “about
LLMs”, we mean that either the title or the abstract of a preprint contains
“LLM”, “Large Language Model”, or “GPT”. The blue line denotes the
percentage of the number of preprints about LLMs out of the number of
all preprints in the CS category. The orange line denotes the percentage of
the number of preprints about LLMs in cs.SE and cs.PL categories out of all
preprints about LLMs

Figure 2, shows the growth in the number of arXiv-
published papers on Computer Science (|A|, in Blue), and on
LLMs (|L|, in orange). Those papers speciﬁcally on Software
Engineering and LLMs are depicted in Green (|L ∩ S|).
Given the rapid rise in overall publication volumes, we use
a logarithmic scale for the vertical axis. Unsurprisingly, we
see an overall rise in the number of CS publications.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

33

LLMs are typically based on deep learning techniques, such
as transformers, and have the capability to generate useful
language output. As a result, they have been found capable of
performing a wide range of language-related tasks, including
text generation [16], answering questions [17], translation [18],
summarization [19], and sentiment analysis [20].

Rumelhart et al. [21] introduced the concept of Recurrent
Neural Network, opening up the possibility of processing
sequential data. Long Short Term Memory (LSTM) archi-
tecture, an extension of the RNN architecture introduced by
Hochreiter and Schmidhuber [22], signiﬁcantly improved their
performance in many applications.

In 2017, Vaswani et al. [23] introduced the Transformer
architecture, which captures word relationships with the self-
attention mechanism. The transformer architecture had a pro-
found impact on language modelling and triggered an explo-
sion of activity on LLMs.

In 2018, OpenAI released the Generative Pre-trained Trans-
former (GPT) model, followed by subsequent iterations (GPT-
2, GPT-3, GPT-3.5, and GPT-4). With GPT-3 and 3.5, many
observers noticed a signiﬁcant step change in generative
performance, thereby attracting a great deal of interest in GPT
(and ChatGPT) in particular, and also in LLMs more generally.
LLMs achieve this performance, in part, due to the large
corpora on which they are trained: For example, GPT-3 is
trained on 45TB of text data and has 175 billion parameters.
Meta launched open-sourced LLaMA in February 2023, which
is trained on 1.4 trillion tokens with a variety of model sizes
ranging from 7 billion to 65 billion parameters [24].


#### B. Categories of Large Language Models

There are three categories of large language models:

1) Encoder-only model: also known as an autoencoder,
consists of an encoder network but does not have a separate
decoder network. It takes an input sequence and maps it to a
lower-dimensional representation. The purpose of an autoen-
coder is to learn an encoding of the input data. Examples of
Encoder-only LLMs are BERT from Google, RoBERTa from
Meta, and DeBERTa from Microsoft [1].
2) Encoder-decoder model: in addition to the encoder net-
work, there is a decoder network that generates an output
sequence by iteratively generating tokens or symbols based on
the context vector and previously generated tokens. It can be
adopted for tasks like machine translation or text generation.
Examples of Encoder-decoder LLMs are T5 from Google and
BART from Meta [1].
3) Decoder-only model: Unlike the previous two types of
LLMs, decoder-only LLMs do not have an encoder component
to process the input data, but only a decoder component
that directly generates an output sequence based on a given
context or input. Decoder-only models are often based on
architectures such as autoregressive models, where the output
is generated token-by-token. Each token generated by the
decoder is conditioned on the previous tokens generated and
the context.

Popular examples of decoder-only models are the GPT
(Generative Pre-trained Transformer) series developed by Ope-
nAI, LLaMA from Meta, Claude from Anthropic, and PaLM
from Google [1].


#### C. Large Language Models for Software Engineering

While LLMs have been widely applied to tasks involving
natural languages, their application to software development
tasks, involving programming languages, has also gained sig-
niﬁcant recent attention.

In 2021, OpenAI introduced CodeX, a ﬁned-tuned descen-
dant of GPT-3. CodeX is used by GitHub’s Copilot, which
provides users of Visual Studio Code, Visual Studio, Neovim,
and JetBrains with code completion. The new version of Copi-
lot, GitHub Copilot X2, is based on GPT-4. In February 2023,
GitHub reported that, on average, 46%3 of the developers’
code was written by Copilot [25]. For Java only, that number
is 62%. Thomas Dohmke, CEO of GitHub, said Copilot will
write 80% of code “sooner than later” in June 2023 [26].

In 2022, DeepMind introduced AlphaCode [27], trained
with 40B parameters on selected public GitHub repositories. It
achieved on average a ranking in the top 54% in competitions
with more than 5,000 participants in simulated evaluations.

The most recent GPT model, GPT-4, also performs code
generation. According to GPT-4’s technical report [28], the
zero-shot pass@1 accuracy is 67% with GPT-4 on HumanEval,
an open-source dataset from OpenAI consisting of 164 pro-
gramming problems.

On a benchmark of 100 LeetCode problems, GPT-4 has
comparable performance with human developers [29]. On
the 24th. August 2023, Meta released open-sourced Code
Llama [30], a state-of-the-art for publicly available LLMs on
coding tasks.

Table II lists the representative LLMs that are designed
language

for code generation/completion based on natural
descriptions.


### III. Requirements Engineering And Design

Requirements engineering is an important discipline in
software engineering. It forms the fundamental link between
the technical attributes of the system software engineers build,
and the purpose for which the systems are built. There is a
mature literature, and a large research community concerned
speciﬁcally with problems associated with requirements engi-
neering problems [31].

There has also been previous work on artiﬁcial intelligence
approaches to support requirements engineering, notably in
the form of computational search for requirements engineering
[32]. However, hitherto, the discipline of requirements engi-
neering has received less attention from the emerging literature
on LLM-based software engineering.

2GitHub Copilot X is under technical preview at the time we accessed it

on July 17th 2023.

3In this paper, all percentages are reported with a precision of 2 signiﬁcant

digits.

34

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

TABLE II
EXISTING LARGE LANGUAGE MODELS FOR CODE GENERATION

Name

Release date

Produced by

Parameters

Open-sourced

Price

Supported languages

Type

CodeBERT
InCoder
AlphaCode
CodeX
Copilot
CodeT5
CodeT5+
PolyCoder
CodeWhisperer
WizardCoder
CodeGeeX
CodeGen
StarCoder
phi-1
Code Llama

February 2020 Microsoft
April 2022
February 2022
August 2021
October 2021
Nov 2021
May 2023
Oct 2022
April 2023
June 2023
Sep 2022
March 2022
May 2023
June 2023
August 2023

Meta
DeepMind
OpenAI
Github and OpenAI
Salesforce Research
Salesforce Research
Carnegie Mellon University
Amazon
Microsoft
Tsinghua University et al.
Salesforce Research
BigCode
Microsoft
Meta

125M
6.7B, 1.3B
300M, 1B, 3B, 9B, and 41B
12B
12B
60M, 220M, 770M
2B, 6B, 16B
160M, 400M, 2.7B
unknown
15B
13B
350M, 1B, 3B, 7B, 16B
15B
1.3B
7B, 13B, 34B

YES
YES
NO
NO
NO
YES
YES
YES
NO
YES
YES
YES
YES
NOT YET
YES

6
free
30
free
Python or C++
free
>11
free
free for individual developers and organisations >11
free
free
free
free for individual developers
free
free
free
free
free
free

6
9
>11
15
unknown
23
Python
>80
Python
>7

Encoder-decoder
Decoder-only
Encoder-decoder
Decoder-only
Decoder-only
Encoder-decoder
Encoder-decoder
Decoder-only
unknown
Encoder-only
Decoder-only
Decoder-only
Encoder-only
Decoder-only
Decoder-only

TABLE III
KEY TERMINOLOGY RELATED TO LARGE LANGUAGE MODELS

Term

Explanation

Chain of Thoughts (CoT)

In the context of LLMs, chain of thought represents the logical ﬂow of ideas and reasoning within the text generated by LLMs.

Encoder & Decoder

Few-shot learning

Fine-tuning

Generative AI

Parameters

Encoders are components of LLMs that map any given input of a speciﬁc type (such as image, audio, text) into a latent vector
space. Decoders perform the reversal: they can take an input from a latent vector space, and (re)constructdata of the original type.

A machine learning technique that aims to train models to perform well on new tasks or classes with only a few new items of
labelled training data. It is also known as in-context learning. With LLMs, few-shot examples are typically included in the prompt.

A process by which a model, trained on a large dataset or a related task, is further trained on a smaller or more speciﬁc dataset
to improve its performance on the target task or domain.

A category of artiﬁcial intelligence that focuses on generating or creating new content, such as images, text, music, and videos.

Parameters are the numerical values inside LLMs that are adjusted during training, and primarily include weights and biases.
Weights dictate the strength of connections between neurons and serve as coefﬁcients to the input values or activation thresholds
for preceding neurons. Biases shift the weighted sum of inputs, before this sum is fed into the activation function. The number of
parameters is often used as a measure of the size of an LLM.

Prompt

The input provided to the LLM to stimulate the generation of a response.

Prompt engineering

The process of designing and optimising prompts to achieve desired outcomes.

ReAct

Temperature

Token

Top-N, Pass@N

The ReAct (Reasoning and Acting) prompting framework allows LLMs to generate reasoning traces as well as actions speciﬁc to
the given task. Once an LLM generates an action, it can be carried out externally, and the observation of the output of the action
can be included in the next prompt, providing information to the LLM. This enables LLMs to use external tools.

A parameter that affects the randomness of the generated content. A higher value (e.g., 1.0) yields more diverse and creative
content, while a lower value (e.g., 0.2) yields more deterministic content.

A token is the atomic unit with which an LLM represents its input and output. Tokens are enumerations, and can represent words,
characters, subwords or other segments of text and/or code.

For many applications, LLMs will typically generate a number of candidate solutions in a ranking. Top-N metrics count the number
of problems correctly solved by an LLM with an answer among its Top N candidates. Similarly, Pass@N counts the number of
programming questions for which a candidate program within the Top N rank has passed the test case.

Zero-shot learning

A machine learning technique that enables models to generalize and make predictions on classes or tasks that were not seen during
the training phase. There is no labelled data available for these new classes.

Zhang et al. [33] conducted a preliminary evaluation of
ChatGPT’s zero-shot requirement retrieval performance on
two requirements analysis tasks over four data sets. Although
these results are only preliminary, they provide optimism that
LLMs can be used as a support for efﬁcient and effective
requirements engineering. Luo et al. [34] conducted prompt
engineering with BERT for automatic requirement classiﬁca-
tion. Luitel et al. [35] focused on requirements completeness
and used BERT to generate predictions for ﬁlling masked slots
in requirements.


#### A. Open Problems in LLMs for Requirement Engineering

Unlike other software development activities, we did not
ﬁnd much work on LLM-based requirements engineering or
on LLM-based design. Indeed, there was even evidence that
practising engineers are reluctant to rely on LLMs for higher-
level design goals [36]. There is thus a great opportunity to
expand on this open ﬁeld of research.

The majority of LLM applications are focused on tasks such
as code generation, testing, and repair. These tasks beneﬁt
from LLM’s capability to generate code. Nevertheless, LLMs
also have signiﬁcant potential to support requirements engi-
neering activities, thanks to their natural language processing
capabilities.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

35

For example, traceability is a long-standing, cross-cutting
concern in software engineering. In particular,
identifying
traceability links between requirements and other engineering
artefacts, such as code and tests, are especially challenging
because requirements are often written in natural language; a
natural ﬁt for LLMs.


### IV. Code Generation And Completion

Of all the Software Engineering application areas for LLMs,
code completion is the area that has been most thoroughly
explored hitherto. Even prior to the advent of LLMs, it was
suggested that learning from existing code repositories is the
key to successful and intelligent code completion [37]: pre-
trained LLMs deliver on these early aspirations for code
completion. While hallucination has been pointed out as the
weakness of LLMs more generally, the speciﬁc task of code
completion sidesteps hallucination problems by acting as a
recommender system to the developer. The developer thus
bears the responsibility to weed out any hallucinated LLM
output before it leaks into the code base.

Of course, a high degree of hallucination would have
made code completion recommender systems ineffective. The
widespread and rapid adoption, and the positive results already
reported for code completion, provide early indications that
this has not happened. For example, Murali et al. [38] reported
the experience of deploying CodeCompose, a code completion
tool based on the Incoder LLM [39], at Meta. During 15
days, 4.5 million code completion suggestions were made by
CodeCompose, and the acceptance rate from developers was
22%. The qualitative feedback was highly positive, with 92%
positive. Similarly, Peng et al. [40] reported that programmers
could complete a non-trivial task (implementing an HTTP
server in JavaScript) 56% faster when paired with GitHub
Copilot, compared to the control group that did not receive
any such support.

Many software engineers already appear to have decided
that beneﬁts outweigh any necessary human ﬁltration effort,
with enthusiastic levels and rates of adoption already being
reported. Once LLM-based code completion is fully adopted,
there are expectations that programmers will spend more time
reviewing rather than writing code [41].


#### A. Code Generation Models

Automated code generation has a long history, tracing its
origins back to early visions of automated program synthesis
[42], which have continued to develop and have generated
impressive results [43].

From the pioneering work of Hindle et al. on the naturalness
of software [44], we know that programmers write code (and
languages enforce code writing styles), that make code highly
predictable. Furthermore, Barr et al. [45] found that 43%
of commits to a large repository of Java projects could be
reconstituted from existing code. They called this ‘The Plastic
Surgery Hypothesis’ because of the way automated repair
proceeds by scavenging for existing code to patch up issues
elsewhere [46].

Their empirical study provided evidence for the efﬁcacy of
this scavenging approach, but also underlined the repetitive
and predictable nature of software. In a larger repository
(sourceforge), Gabel and Su [47] found that a programmer
would have to write more than six lines of code in order to
create a novel code fragment.

These research ﬁndings on code naturalness, reusability
and predictability, make it unsurprising that LLMs have been
able to exploit that same predictable reusability to produce
effective recommendations for code generation. These ob-
servations have underpinned the growth of generate-and-test
approaches to repair and genetic improvement [8], [46]. The
generate-and-test approach offers greater code transformation
freedom (compared to more traditional correct-by-construction
approaches [48]), precisely because the generated code may
not preserve strict, mathematically-deﬁned (and not always
appropriate, nor useful) interpretations of correctness.

This freedom to explore a wider space of “semantic near
neighbours” allows Genetic Improvement
to ﬁnd dramatic
optimisations (see Section VI-C). The Genetic Improvement
approach, nomenclature, and evaluation methodologies also
provide a scientiﬁc framework within which to understand and
evaluate LLM-based code generation. Both technologies share
the ‘generate-and-test’ approach to program transformation
and code generation, potentially making much of the existing
work on genetic improvement directly applicable to LLM-
based code generation.

In 2021, Chen et al. [49] introduced CodeX, a GPT language
model ﬁne-tuned on publicly available code from GitHub, and
evaluated its Python code-writing capabilities. They released a
new evaluation set called ‘HumanEval’ to measure functional
correctness for synthesizing programs from docstrings, and
found that CodeX outperformed GPT-3 and GPT-J when tack-
ling these problems. Since then there has been an explosion in
research on LLM-based code generation and the HumanEval
dataset has been used in many subsequent studies.

In 2022, Li et al. [27] introduced AlphaCode, a system for
code generation that creates novel solutions to competitive
programming problems. They found that three key components
were critical to achieving reliable performance:

1) An extensive programming dataset for training and eval-

uation.

2) Large and efﬁcient-to-sample transformer-based archi-

tectures.

3) Large-scale model sampling to explore the search space,

followed by behaviour-based ﬁltering.

In simulated evaluations on programming competitions on
the Codeforces platform, AlphaCode achieved, on average, a
ranking of the top 54% in competitions with more than 5,000
participants.

Several papers also introduced code synthesis LLMs [50]–
[53], based on large data sets with little pre-ﬁltering of the
training data. However, in 2023, Gunasekar et al. [54] reported
that, by training with only a textbook-quality code corpus,
LLMs with lower parameter counts could achieve performance
comparable to much larger models.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

36

They classiﬁed an existing Python code corpus with the
GPT-4 model, by prompting it to determine the educational
value of the given code for a student who wants to learn
programming. Second, they used GPT-3.5 to create synthetic
textbooks about Python. Speciﬁc code generation use cases
have also been tackled, such as numerical algorithm code
[55], and generation of code from behavioural
generation
descriptions [56]. More examples of the existing LLMs for
code generation and the code generation leaderboard can be
found in Table II and Figure 4.


#### B. Prompt Engineering for Improved Code Generation

Prompt engineering has been extensively used as a way to
improve code generation. For example, Li et al. [57] reported
pass@1 improvements of between approximately 50% and
80% on CodeX, CodeGeeX, CodeGen, and InCoder on several
benchmarks (MBPP for Python, MBJP for Java, and MBJSP
for JavaScript). D¨oderlein et al. [58] reported the prompt-
engineered improvement of Copilot and CodeX success rates
from approximately 1/4 to 3/4 on HumanEval and LeetCode.
He and Vechev [59] used prompt engineering to improve the
security of LLM-generated code, reporting an improvement
in security from 59% (of cases considered) to 92%. White
et al. [60] provided a catalogue of prompt engineering design
patterns for various software engineering tasks, including code
generation. Denny et al. [61] argued that prompt engineering
is a useful learning activity that fosters software engineering
students’ computational thinking.

Other authors have considered ways to decompose prompt
engineering into iterative and multiphase conversations with
the LLM, moving it closer to Chain of Thought reasoning.
For example, Li et al. [62], [63] reported an 18% increase in
ChatGPT Pass@1 using a two-stage sketch-based approach,
SkCoder, in which the LLM ﬁrst creates a sketch and then
subsequently implements these sketches. Jiang et. al. [64] and
Zhang et al. [65] also sought to deploy Chain-of-Thought-style
reasoning by prompting LLMs to reﬂect and self-edit.

Existing software engineering analysis techniques can also
provide additional
information for ﬁne-tuning and prompt
engineering. For example, Ahmed et al. [66] show how simple
static analysis can be used in the prompt to improve the
performance of code generation with few-shot learning.

Shin et al. [67] compared prompt engineering and ﬁne
tuning with GPT-4 for code generation tasks, demonstrating
that ﬁne-tuning works better than prompt engineering.


#### C. Hybrids of LLMs and other Techniques

Throughout our survey of the literature, we found strong
evidence that some of the most promising results can be
achieved by hybridising; combining LLMs with other existing
software engineering techniques. This section surveys work on
hybrid LLMs for code generation.

Several authors have developed hybrids of LLMs combined
with planning and search. For example, Zhang et al. [68],
[69] reported improvements over baselines of between approx-
imately 11% and 27%, while Zhang et al. [70] hybridized code
generation with API search techniques.

Hybrid approaches have also used existing software engi-
neering and/or AI techniques to select the best candidate from
an LLM’s top-n outputs. For example, Chen et al. [71] use test
generation to choose candidates and reported improvement of
approximately 20% on ﬁve pre-trained LLMs; Inala et al. [72]
use a neural network-based ranker to predict code correctness
and potential faults. Jain et al. [73] proposed Jigsaw, which
post-processes the generated code based on program analysis
and synthesis techniques.

Dong et al. [74] treated LLMs as agents, letting multiple
LLMs play distinct roles in addressing code generation tasks
collaboratively and interactively. They reported improvements
of approximately 30%-47%.


#### D. Scientiﬁc Evaluation of LLM-based Code Generation

There is a pressing need for more thorough scientiﬁc
evaluation. Many authors have anecdotally reported on cases
where LLMs failed to generate correct, secure, and reliable
code. Poldrack et al. [75] also highlight the need for substantial
human validation. In this section, we survey the literature on
the empirical evaluation of LLM-based code generation in
terms of correctness, robustness, explainability, determinism,
and security.

1) Correctness Evaluation: The GPT-4 Technical Re-
port [28] evaluated the correctness of GPT-4’s code generation
on the HumanEval dataset, reporting a zero-shot accuracy of
67%, a modest improvement on the (earlier ChatGPT) results
reported by Yetistiren et al. [76].

Borji [77] presented a rigorous, categorised and systematic
analysis of LLM code generation failures for ChatGPT. Eleven
categories of failures,
including reasoning, factual errors,
mathematics, coding, and bias, are presented and discussed
in their work.

Figure 4 shows the leaderboard of code generation correct-
ness in terms of the pass@1 (i.e., the test pass rate for the top-1
code candidate) on the HumanEval dataset according to Papers
With Code, a platform that highlights trending AI research and
the code behind the method and models.4 The LLM models
behind each method are shown in brackets. At the time of
writing, the best code generation model, Reﬂexion [78], can
generate correct code for over 90% of the generation tasks.
However, these numbers and the relative rankings of different
language models are inherently subject to change in such a
rapidly developing ﬁeld. For example, the ﬁgure given for
correct code on HumanEval in the original GPT-4 Report [28]
was only 67%, so the updated ﬁgure of 80% (at the time of
writing, which is ﬁve months later) retrieved from the Papers-
With-Code website presumably represents the evolution of
GPT4 since then.

Despite the promising results in the literature on code
generation and completion, Din et al. [79] reported that the
performance of code completion dropped by more than 50%
on HumanEval when the context contains bugs.

4The actual leaderboard can be found at https://paperswithcode.com/sota/
code-generation-on-humaneval/; results in Figure 4 accessed on 24th August
2023.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

37

(cid:53)(cid:72)(cid:73)(cid:79)(cid:72)(cid:91)(cid:76)(cid:82)(cid:81)(cid:3)(cid:11)(cid:42)(cid:51)(cid:55)(cid:16)(cid:23)(cid:12)

(cid:51)(cid:68)(cid:85)(cid:86)(cid:72)(cid:79)(cid:3)(cid:11)(cid:42)(cid:51)(cid:55)(cid:16)(cid:23)(cid:14)(cid:38)(cid:82)(cid:71)(cid:72)(cid:55)(cid:12)

(cid:48)(cid:72)(cid:87)(cid:68)(cid:42)(cid:51)(cid:55)

(cid:42)(cid:51)(cid:55)(cid:16)(cid:23)(cid:3)

(cid:38)(cid:50)(cid:39)(cid:40)(cid:16)(cid:55)(cid:3)(cid:11)(cid:70)(cid:82)(cid:71)(cid:72)(cid:16)(cid:71)(cid:68)(cid:89)(cid:76)(cid:81)(cid:70)(cid:76)(cid:16)(cid:19)(cid:19)(cid:21)(cid:12)

(cid:38)(cid:82)(cid:71)(cid:72)(cid:3)(cid:47)(cid:79)(cid:68)(cid:80)(cid:68)(cid:3)(cid:11)(cid:88)(cid:81)(cid:81)(cid:68)(cid:87)(cid:88)(cid:85)(cid:68)(cid:79)(cid:12)

(cid:58)(cid:76)(cid:93)(cid:68)(cid:85)(cid:71)(cid:38)(cid:82)(cid:71)(cid:72)(cid:85)

(cid:83)(cid:75)(cid:76)(cid:16)(cid:20)(cid:14)(cid:20)(cid:17)(cid:22)(cid:37)

(cid:42)(cid:51)(cid:55)(cid:16)(cid:22)(cid:17)(cid:24)(cid:3)(cid:93)(cid:72)(cid:85)(cid:82)(cid:16)(cid:86)(cid:75)(cid:82)(cid:87)

(cid:44)(cid:81)(cid:86)(cid:87)(cid:85)(cid:88)(cid:70)(cid:87)(cid:38)(cid:82)(cid:71)(cid:72)(cid:55)(cid:24)(cid:14)(cid:20)(cid:25)(cid:37)(cid:3)

(cid:38)(cid:82)(cid:71)(cid:72)(cid:42)(cid:72)(cid:81)

(cid:38)(cid:82)(cid:71)(cid:72)(cid:55)(cid:24)(cid:14)(cid:3)(cid:20)(cid:25)(cid:37)(cid:3)

(cid:38)(cid:82)(cid:71)(cid:72)(cid:91)(cid:14)(cid:20)(cid:21)(cid:37)

(cid:47)(cid:47)(cid:68)(cid:48)(cid:36)(cid:14)(cid:25)(cid:24)(cid:37)(cid:3)

(cid:47)(cid:68)(cid:48)(cid:39)(cid:36)(cid:14)(cid:20)(cid:22)(cid:26)(cid:37)

(cid:3)

(cid:71)
(cid:82)
(cid:75)
(cid:87)
(cid:72)
(cid:80)
(cid:81)
(cid:82)
(cid:76)
(cid:87)
(cid:68)
(cid:85)
(cid:72)
(cid:81)
(cid:72)
(cid:74)
(cid:3)
(cid:72)
(cid:71)
(cid:82)
(cid:70)
(cid:3)
(cid:71)
(cid:72)
(cid:86)
(cid:68)
(cid:69)
(cid:16)
(cid:48)
(cid:47)
(cid:47)

(cid:19)

(cid:20)(cid:19)

(cid:21)(cid:19)

(cid:22)(cid:19)

(cid:23)(cid:19)

(cid:24)(cid:19)

(cid:25)(cid:19)

(cid:26)(cid:19)

(cid:27)(cid:19)

(cid:28)(cid:19)

(cid:20)(cid:19)(cid:19)

(cid:51)(cid:68)(cid:86)(cid:86)(cid:35)(cid:20)(cid:3)(cid:73)(cid:82)(cid:85)(cid:3)(cid:70)(cid:82)(cid:71)(cid:72)(cid:3)(cid:74)(cid:72)(cid:81)(cid:72)(cid:85)(cid:68)(cid:87)(cid:76)(cid:82)(cid:81)(cid:3)(cid:82)(cid:81)(cid:3)(cid:43)(cid:88)(cid:80)(cid:68)(cid:81)(cid:40)(cid:89)(cid:68)(cid:79)

Fig. 4. Code generation leaderboard for the HumanEval benchmark. These methods are either based on LLMs or LLMs themselves.

2) Robustness Evaluation: LLM code generation robust-
ness is the degree to which similar prompts elicit semantically
and syntactically similar code generation. Treude [80] intro-
duced GPTCOMPARE, a prototype tool for visually highlight-
ing similarities and differences between LLM code outputs.
Yan et al. [81] introduced COCO to test the robustness and
consistency of LLM-based code generation systems.

3) Explainability Evaluation: One considerable advantage
of LLMs, over previous machine learning techniques, is the
way in which the code generation artefacts are accompa-
nied by explanations. Such explanations have the potential
to increase adoption, by providing additional conﬁdence and
faster understanding. More work is needed to evaluate and
optimise explanations that accompany generated code and
other software engineering artefacts.

Initial evaluation by MacNeil et al. [82] on their interactive
Web development e-book, suggested that a majority of students
perceived LLM-generated code explanations to be helpful.
Noever and Williams [83] also showed the potential for
explanations to help human engineers, particularly where code
is obfuscated or lacks sufﬁcient existing documentation. In
this way, the ability to produce insight and explanation may
go beyond simply justifying the code generated by the LLM
itself, but may become a valuable source of education and
documentation (See Section XI).

Sun et al. [84] focus on users’ explainability needs for gen-
erative AI in three software engineering use cases: code gen-
eration based on natural language description (with Copilot),
translation between different programming languages (with
Transcoder), and code autocompletion (with Copilot). Their
investigation was conducted as 9 workshops with 43 software
engineers and identiﬁed 11 categories of explainability needs
in the context of Generative AI (GenAI) for code. It also
proposed 4 types of features for generative AI: AI documenta-
tion, model uncertainty, attention distribution, and social trans-
parency (i.e., making visible the socio-organizational factors
that govern the use of AI).

Mohammadkhani et al. [85]used the attention mechanism
to study CodeBERT and GraphCodeBERT on tasks including
code documentation generation, code reﬁnement, and code
translation.

4) Determinism Evaluation: LLMs are nondeterministic.
Ouyang et al. [10] empirically studied the non-determinism of
ChatGPT in code generation, founding that over 60% of tasks
had zero equal test output across different requests. Neverthe-
less, their study of the literature in LLM-based code generation
demonstrate that only 21.1% of these papers consider the non-
determinism threat in their experiments.

5) Security Evaluation: Hajipour et al. [86] proposed a few-
shot prompting approach to detecting security vulnerabilities,
reporting that their approach automatically ﬁnds thousands of
security vulnerabilities in several models. Khoury et al. [87]
found that the code generated by ChatGPT often fell way
below even minimal standards of secure coding. Risse and
B¨ome [88] reported results that indicated vulnerability de-
tection accuracy may be over-reported, due to the model
overﬁtting to unrelated training set features .

In addition, Yetistiren et al. [76] presented a comprehensive
evaluation of the performance of Copilot, CodeWhisperer, and
ChatGPT, covering different aspects including code validity,
code correctness, code security, code reliability, and Their
results show a wide degree of divergence in performance,
motivating the need for further research and investigation. For
example, they found 65%, 46%, and 31% of the programs
generated by ChatGPT, Copilot, and CodeWhisperer (respec-
tively) were correct.

6) Benchmarks: As with other scientiﬁc evaluations, soft-
ware engineering evaluation relies on publicly available and
representative benchmark suites. A number of these have
already emerged and can support software engineering evalu-
ation of LLM-based applications. The Papers-With-Code plat-
form5 provides a summary of 15 benchmarks for evaluating
code generation.

5https://paperswithcode.com/task/code-generation

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

38

Evaluations have often relied on small programming prob-
lems from programming courses [89], synthetically generated
problem sets [90], and online judging platforms such as
Leetcode [29], [65], [91]. Although results reported naturally
vary by LLM in training sets, the overall conclusions of these
evaluations indicate success rates of between 20% and 80%.
Nevertheless, existing code generation benchmarks tend to
rely on test suites to automatically judge code correctness,
which can be inadequate, leading to false judgements [92].
This highlights the need for more work on evaluation bench-
marks that are speciﬁcally tailored to LLM-based code gener-
ation evaluation. Liu et al. [93] draw attention to the problem,
showing how existing test suites can lead to high degrees
of false positive conclusions (also a serious problem for
online judge platforms [92]). To alleviate this problem, they
propose EvalPlus – a code synthesis benchmarking frame-
work that automatically generates test inputs and rigorously
evaluates the functional correctness of LLM-generated code.
Their evaluation of 14 popular LLMs (including GPT-4 and
ChatGPT) demonstrated that with the newly generated tests for
HumanEval, the assessment of pass@k drops by up to 15%,
averaged over problems considered.

Jimenez et al. [94] introduced SWE-bench with the aim of
evaluating LLMs on code generation problems in a realistic
software engineering setting. SWE-bench contains 2,294 soft-
ware engineering problems, drawn from real GitHub issues.
The results suggest that Claude 2 and GPT-4 solve only 4.8%
and 1.7% of the coding tasks, respectively.


#### E. Open Problems in Code Generation and Completion

Fortunately,

Assessing the generated code remains a critical problem for
LLM-based code generation and completion: while much work
already started applying existing software testing knowledge to
this problem, we expect closer integration of automated testing
techniques with code generation and completion techniques.
there is a large body of existing work on
automated test data generation [3]–[5], much of which will
have an important role to play in ensuring the correctness
of the engineering artefacts generated by LLMs. A recurring
theme of the challenges covered in this paper, is that code
execution provides precisely the ‘ground truth’ needed to ﬁlter
hallucinated responses. It can also provide guidance as part of
interactive reasoning/action (‘ReAct’) dialogue [95], both with
and within LLMs.

Automated test data generation allows the software engineer
to target
the exploration of the most relevant regions of
this run-time ground truth. This test-based targeting can help
ﬁlter, ﬁne-tune and to optimise prompts, thereby minimising
problems posed by hallucination. LLMs also have considerable
potential for automating the process of constructing effective
and efﬁcient software test suites.

Another important problem is how to efﬁciently ﬁne-tune
pre-trained LLMs so that they perform better for a speciﬁc
programming language, codebase, or domain: this is especially
important because training an LLM from scratch requires
signiﬁcant computational resources.

For example, transfer learning has been proposed as a way
to improve code completion performance when the volume
of training examples for a speciﬁc programming language is
inadequate [96].

The current focus of research is on the code produced by
LLMs. However, the explanations produced by LLMs may
turn out to be at least as important. One could imagine many
scenarios in which an engineer would prefer to accept a
(possibly) suboptimal software engineering artefact that comes
with a compelling explanation, over a potentially more per-
formant solution with a less compelling explanation. After all,
engineers regularly make the same judgement call for human-
designed engineering artefacts, so why would we expect it to
be any different for those produced by machines? As with
prompt engineering, which focuses on optimising the input to
the LLM, explanation engineering is also likely to become an
area of study in its own right.


### V. Software Testing

Software testing is a well-established research discipline,
the origins of which can be traced back to Turing’s pioneering
work in the late 1940s [97]. Much of the focus of this research
has been on the automated generation of test suites, able to
achieve high fault revelation potential at low computational
cost [3]–[5]. This provides us with, not only techniques able
to weed out incorrect LLM-generated code, but also a mature
baseline against which to compare novel LLM-based and
hybrid techniques for test suite generation.

There is already a sufﬁciently large body of work to warrant
a survey speciﬁcally on LLM-based Software Testing: Wang
et al. [98] presented a survey of papers primarily on testing,
but also including debugging and repair. They reported on
52 papers (33 published since 2022) of which approximately
one-third concerned test-based LLM ﬁne-tuning, while the
remainder relied upon prompt engineering.


#### A. Generating New Tests Using LLMs

In this section, we review existing work on LLMs for
test data generation, before highlighting open problems and
challenges for the development of this emerging ﬁeld. The
tests generated may not be executable because the LLM is not
guaranteed to generate compilable code. Nie et al. [99] report
29% of tests generated using TeCo are executable, while Yuan
et al. [100] found that approximately one-quarter of the tests
generated by ChatGPT were executable, rising to one-third
with suitable prompt engineering.

Of those tests that do compile, several authors have re-
ported on the code coverage achieved. For example, Bareiß
et al. [101] reported an increase from the 10% achieved using
Randoop [102] to 14% with CodeX. Hashtroudi et al. [103]
reported a 50% increase in line coverage for the tests they
generated by fune-tuning CodeT5. Siddiq et al. [104] reported
80% coverage on the HumanEval dataset using CodeX, but
also found that neither the studied LLMs could achieve more
than 2% coverage on the EvoSuite SF110 dataset.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

39

Hybrid approaches that combine existing test generation and
evaluation techniques, such as fuzz-based testing and search-
based testing, with LLMs have already demonstrated promis-
ing results. For example, Lemieux et al. [105] introduced
CODAMOSA, an algorithm that combines Search-Based Soft-
ware Testing (SBST) [5] and CodeX to generate high-coverage
test cases for programs under test. When SBST’s coverage
improvements stall, CODAMOSA asks CodeX to provide
example test cases for under-covered functions. This helps
SBST redirect its search to more useful areas of the search
space. In an evaluation of 486 benchmarks, CODAMOSA
achieved signiﬁcantly higher coverage compared to SBST
and LLM-only baselines. Hu et al. [106] introduced Chat-
Fuzz, which augments the widely studied fuzzer, AFL, with
ChatGPT, in order to get more format-conforming mutants.
In an evaluation of 12 target programs chosen from three
benchmarks, ChatFuzz achieved higher branch coverage than
AFL by 13%. Dakhel et al. [107] used mutation testing to
help LLMs to generate tests. In particular, they augmented
prompts for Codex and Llama-2-chat with surviving mutants.
They report that their approach detects 28% more human-
written faults. Xia et al. [108] recently demonstrate that LLMs
can serve as a universal fuzzer for systems across different
application domains and programming languages, including
C/C++ compilers, JDK, SMT solvers, and even quantum
computing systems.

Deng et al. [109] propose TitanFuzz, which uses LLMs
(i.e., Codex) to generate valid input DL programs to test DL
libraries. The results on PyTorch and TensorFlow reveal that
TitanFuzz can achieve 30%/51% higher code coverage than
state-of-the-art fuzzers. Later on, they further introduced Fuz-
zGPT [110], which synthesizes unusual programs for fuzzing
DL libraries. Their results indicated that CodeX and CodeGen
could outperform TitanFuzz on PyTorch and TensorFlow when
re-targeted for fuzz-based testing.

Li et al. [111] used a hybrid of differential testing and
ChatGPT to elevate the latter’s ability to generate failure-
inducing test cases of buggy programs. They report a test
effectiveness improvement from 29% to 78%.

A promising area for LLM-based test generation is GUI
testing, because the manipulation of the application state via
GUI often requires a semantic understanding of both the user
interface as well as the application domain. Sun et al. [112]
described user interface via text, and asked ChatGPT which
action it would like to perform next based on the text, then
convert the answer into actual GUI interaction. This resulted in
32% higher activity coverage compared to the state-of-the-art.
One particularly important problem that is challenging for
classical techniques is the construction of test cases from user
reports. The user reports are written in natural language. This
has presented considerable challenges for existing techniques,
but is ideally suited to LLMs. Kang et al. [113] introduced
Libro, a few-shot learning failure reproduction technique that
automatically generates tests from general bug reports, based
on CodeX. Libro successfully reproduced approximately one
third of the failures.

Feng and Chen [114] demonstrated a replicability rate of
80% on bug reports with natural-language-deﬁned steps to
reproduce, using an LLM out of the box (ChatGPT) with
Chain of Thought prompt engineering alone.

that

Several authors have considered prompt engineering to im-
prove the results of test generation [115], [116]. For example,
Schafer et al. [116] proposed TESTPILOT, which re-prompts
with failing tests and associated error messages, achieving
reported average statement coverage of 68%. Xie et al. [117]
create prompts for test generation by parsing the project and
includes the focal
creating an adaptive focal context
method and its dependencies. They further used rule-based
repair to ﬁx syntactic and simple compile errors in the tests.
Although the outcomes of LLM-based testing may be un-
certain, researchers have explored cross reference or majority
of votes [118], [119] methods to estimate the conﬁdence of
LLMs, based on the notion of ‘self-consistency’ [120]. For
example,
the Libro introduced by Kang et al. [113] uses
CodeX to generate tests from bug reports that can reproduce
failures. If multiple tests show similar failure behavior, Libro
estimates that LLM is “conﬁdent” in its predictions. Further-
more, where there is partial oracle information, this can also
be used to augment conﬁdence estimates. Such partial oracle
information is often available when the goal of the overall
processes to improve on existing code. For example, when
improving the efﬁciency of an existing test, automated partial
oracle information can be gathered from observing whether
the test behaves similarly to the original (passing and failing
in the same situations), and is also faster to execute.


#### B. Test Adequacy Evaluation

Test effectiveness is typically measured in terms of ‘ade-
quacy criteria’ [121], [122]. Since testing cannot exhaustively
explore every possibility, adequacy criteria provide a form of
lower bound on the effectiveness achieved by a suite of tests.
Mutation testing is a widely-studied technique for assessing
the adequacy of software test suites [123], [124], in which
synthetic faults (called ‘mutants’), are deliberately injected
in order to assess test adequacy. Mutation testing has been
shown to provide more stringent adequacy criteria than other
structural coverage-based criteria such as statement and branch
coverage [125].

One of the challenging open problems for mutation testing
is to generate mutants that faithfully model important classes
of real-world faults. Khanﬁr et al. [126] used CodeBert to
generate developer-like mutants and found that their approach
has better fault revelation ability than PiTest. Garg et al. [127]
applied CodeBERT to generate mutants that faithfully capture
vulnerabilities. They evaluation found that 17% of the mutants
fail the tests that are failed by 89% of the respective vulner-
abilities. Brownlee [128] used GPT-3.5 to generate mutants
for genetic improvemnt and observed that randomly sampled
LLM-based edits compiled and passed unit tests more often
compared to standard GI edits.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

40


#### C. Test Minimisation

Test minimisation improves the efﬁciency of software test-
ing by removing redundant test cases. Pan et al. [129] ap-
plied CodeBERT, GraphCodeBERT, and UniXcoder to extract
embeddings of test code to conduct test minimisation. Their
approach achieves a 0.84 fault detection rate and runs much
faster (26.73 minutes on average) than the baseline.


#### D. Test Output Prediction

Liu et al. [130] proposed CodeExecutor, a pre-trained Trans-
former model, to predict the program’s whole execution trace.
The purpose is to imitate the real-world arbitrary program
execution behaviour. Their evaluation compares CodeExecutor
with CodeX, and shows that CodeExecutor signiﬁcantly out-
performs Codex in execution trace prediction (e.g., 76% vs.
13% output accuracy for the Tutorial dataset).


#### E. Test Flakiness

A test is ﬂaky if it can pass on some occasions and fail
on others without any apparent (tester-controllable) change
in the execution context. Test ﬂakiness is one of the most
pressing and impactful problems that inhibit test effectiveness
in industry [131]. LLMs have been used to predict ﬂakiness
with high accuracy (with 73% F1 score [132], [133] and 97%
accuracy [134] reported).


#### F. Open problems in LLMs for Software Testing

There are many open problems in LLM-based software test
data generation, most of which lie well within the grasp of
existing software testing techniques. We can thus expect an
exciting explosion in LLM-based software test generation in
the coming years. This section outlines some directions for
this research agenda.

1) Prompt Engineering: There are many aspects of a good
software test that could be favoured by suitable prompt engi-
neering. For example, we need to understand how to engineer
prompts that

- Predict and reduce generated test ﬂakiness;
- Reveal likely faults, for example via training on historic

fault data;

- Optimise the balance between mocking and integration

testing;

- Make realistic data builders, mock objects, parameters

and inputs;

- Predict tests that are most likely to elicit tests that cover

corner cases;

- Tailor test generation to focus behaviour that is prevalent

in production.

2) Augmenting Existing Tests: Work on LLM-based test
generation has focused on the automated generation of novel
test suites. However, given the array of existing test generation
techniques, there remains an important (and comparatively less
well-studied) open problem of augmentation and regeneration
based on existing test suites [135], [136].

Test augmentation and regeneration can exploit few-shot
learning and/or can ﬁne-tune (on an existing suite of test data
and historical faults), to generate augmented test suites.

More work is needed on LLMs for generating additional test
assertions that capture corner cases, historical faults, and likely
programmer errors, drawing on the training data available.
Hybridization between LLMs and existing automated test
generation techniques is also a productive theme [105].

3) Test Correctness: Traditional software test generation
has suffered from the Oracle Problem [6],
they are
inhibited by the lack of an automated oracle that determines
whether a test outcome is correct. Two cases pertain to AI-
generated tests:

i.e.,

1) The generated test passes on the current release: We
might assume that the functionality is correctly tested
and that the generated test thus acts as a regression test,
against which future changes can be checked.

2) The generated test fails on the current release: We
need to know whether the assertion is wrong or whether
the generated test has found a bug.

Both cases can have pernicious consequences when they are
not imbued with self-regulation. A test case that passes may
merely reﬂect coincidental correctness [137], [138]. Worse, it
might be the case that the code is, in fact, incorrect (and that
the test is equally incorrect yet captures, and thereby enforces,
the incorrect behaviour). In such cases,
the generation of
the test will tend to inhibit fault remediation, by failing on
future ﬁxes. This problem also affects LLM-generated test
cases, and may be more pernicious in cases where such tests
hallucinate oracle properties, baking into the generated tests
these incorrect oracle assertions.

On the other hand, when a generated test case fails, this may
indicate a bug. This bug revelation would denote a ‘win’ for
LLM-based testing. However, should it turn out that the ratio
of false positives to true positives are high, then the cost (e.g.,
in human assessment) may make the technique impractical,
even when it does reveal true positive bugs [131]. More work
is needed on self-assessment of conﬁdence, self-checking for
correctness, consistency, and robustness of generated tests.
We need to develop techniques for automatically assessing,
augmenting and ﬁltering raw outcomes from execution of
LLM-based tests, before presenting the ‘test signal’ to the
developer.

The interaction between LLM hallucination and test correct-
ness is an important topic in its own right. Since LLM-based
code generation is generally driven by what is most likely,
rather than what is most correct, hallucination poses threats
to any questions of correctness. However, interestingly, Feldt
et al. [139] reported a case of hallucination being helpful for
software testing, because it may reveal discrepancies between
the actual program semantics and the programmer’s perception
of the semantics. They suggested a form of conversational
testing agents (i.e., any generated tests are ﬁltered by the
programmer via the conversation) to harness this capability
without posing any threats to overall test correctness.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

41

More work is also required on the scientiﬁc foundations on
which evaluations of LLM-based software testing rest. More
care and attention are clearly needed to heed the ‘best practice’
advice for the scientiﬁc analysis and reporting from previous
work on foundations of Empirical and Search Based Software
Engineering [11], [13], [14].

4) Mutation Testing: More work is needed to explore the
adequacy achievable with LLM-based test generation, and also
to use LLM-based techniques to support and enhance test
adequacy investigation and assessment. LLMs can be ﬁne-
tuned on a fault model, and thereby used to suggest mutants
that are highly coupled to real faults, and can thus be used to
assess test adequacy.


### VI. Maintenance, Evolution And Deployment

Software maintenance and evolution have been important
topics of study for many decades. They are concerned with
existing code bases from which we seek understanding and
business logic extraction, and for which we seek to re-
engineer, repair and refactor. Maintenance problems, such as
these, all reside within language-rich problem domains. It is
therefore unsurprising that this area ﬁnds many applications
of LLM-based techniques, as we review in this section.


#### A. Debugging

Kang et al. [140] studied GPT-3.5’s fault localisation ability,
and found that LLM could often identify the faulty method
on the ﬁrst try. Wu et al. [141] present a comprehensive
investigation into the capability of GPT-3.5 and GPT-4 for fault
localisation accuracy, stability, and explainability. The results
demonstrate that GPT-4 achieves 47% higher fault localisation
accuracy over the state-of-the-art, but the performance declines
dramatically with a longer code context.

Feng and Chen [142] proposed AdbGPT, which reproduces
Android bugs from bug reports through prompt engineering
with ChatGPT. With a dataset of 88 bug reports, AdbGPT
was able to successfully reproduce 81%, outperforming the
baselines and ablations. Joshi et al. [143] focused on mul-
tilingual debugging and proposed RING, which proposes a
prompt-based strategy that conceptualizes repair as localiza-
tion, transformation, and candidate ranking.

To address the data leakeage threat in fault localisation and
program repair, Wu et al. [144] introduced ConDefects with
1,254 Java bugs and 1,625 Python bugs that were produced
between October 2021 and September 2023. Researchers
are allowed to select code samples based on their creation
period, thereby allowing them to evaluate the effectiveness of
different LLMs according to their training data cut-off date. In
addition, there has been work on predicting bug severity with
LLMs [145].


#### B. Program Repair

Repairing bugs has been a topic of much interest for over a
decade in the software engineering research community [146],
[147], and has already found its way into initial industrial
deployment [148].

Much of the work on automated repair has used the
generate-and-test approach widely adopted in the ﬁeld of
Genetic Improvement and readily applicable to LLM-based
techniques. As a result, LLMs are certain to have a positive im-
pact on automated software repair, but there remain technical
challenges in taming the hallucination problem and managing
scalability, as we report in this section.

the more important

In order to achieve scalability, all generate-and-test ap-
proaches need to address the build time problem [149]. LLM-
based repair is no exception; the propensity to hallucinate
the test phase can
makes it all
be executed regularly. It is likely that using ReAct deploy-
ment models [95] will help to ﬁnd efﬁcient and effective
engineering trade-offs. When ReAct is applied to repair, the
overall approach would alternate between the ‘Reason’ phase
(generating candidate ﬁxes) and the ‘Action’ phase (evaluating
ﬁxes through testing, which involves the build problem).

that

To address this issue, we can refer to the well-established
literature on software repair [46], [150], grounded in over two
decades of the development of search-based approaches to
software engineering [12], [151]. This literature provides the
research community with a ﬁrm foundation of experience and
expertise, making it very well-placed to develop LLM-based
generate-and-test approaches to the problem.

Recent work on repair has started to use neural AI models,
such as the seminal work of Tufano et al. [152]. More recently,
since 2022, there has been a rapid development of emergent
embryonic research literature on LLM-based repair. For ex-
ample, Xia et al. [153] proposed AlphaRepair. It redeﬁnes
the APR problem as a cloze (or inﬁlling) task, where the
LLMs are leveraged to directly ﬁll-in correct code based on
the bi-directional context of the potential buggy code portions.
AlphaRepair also demonstrates for the ﬁrst time that LLMs can
outperform all prior APR techniques.

They further conducted an empirical study [154] on nine
LLMs across ﬁve datasets in three different languages. Their
ﬁndings not only afﬁrmed the superiority of LLM-based APR
(especially the cloze-style approach) but also offered a number
of practical guidelines. Wei et al. [155] synthesize a patch
through the interaction between an LLM and a Completion
the approach surpasses the best-
Engine, and found that
performing baseline by 14 and 16 bugs ﬁxed.

Program repair naturally ﬁts a conversational model of
prompt engineering. Xia et al. [156] proposed conversational
APR, which alternates between patch generation and vali-
dation in a conversational manner. Their evaluation on ten
LLMs demonstrated that their approach has superiority in both
effectiveness and efﬁciency.

They further proposed ChatRepair [157], showing that
the conversational approach ﬁxes 162 out of 337 bugs for
only $0.42 per bug, thereby also addressing potential con-
cerns about the computational resources required. Chen et
al. [158] introduced SELF-DEBUGGING, which teaches an
LLM to debug its predicted code via few-shot learning, SELF-
DEBUGGING reports baseline accuracy improvements of up
to 12%.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

42

Studies have also reported results for particular classes of
bugs, for example, Pearce et al. [159] reported repair results
from ﬁve commercial LLMs on security bugs, Charalambous
et al. [160] combined ChatGPT with with formal veriﬁcation
strategies to verify and automatically repair software vulner-
abilities. Cao et al. [161] report ChatGPT results for Deep
Learning (DL) program repair.

Repair does not always start with an existing failing test
case, but can start with a natural language description of a
failure in production. Automation opens the door to faster
responses to user-generated bug reports. This is a route to
repair that has also been explored for LLMs in the work of
Fakhoury et al. [162], who generated functionally correct code
edits from natural language issue descriptions. They propose
Defects4J-Nl2ﬁx, a dataset of 283 Java programs from the
Defects4J dataset with high-level descriptions of bug ﬁxes. The
state-of-the-art LLMs evaluated on this benchmark achieve up
to 21% Top-1 and 36% Top-5 accuracy.

Automated repair can also reduce the burden on engineers,
managing DevOps-style on-call for production systems. For
example, Ahmed et al. [163] studied the use of LLM-based
root causing and remediation of 40,000 incidents on Microsoft
cloud services. The authors evaluated multiple LLMs using
semantic and lexical metrics in zero-shot, ﬁne-tuned, and mul-
titask settings, showing that ﬁne-tuning signiﬁcantly improves
incident response effectiveness.

The ability to perform ﬁne-tuning for a speciﬁc task or
domain can signiﬁcantly improve the model performance in
program repair. Jiang et al. [164] empirically evaluated the
performance of 10 different Code Language Models (CLMs)
and 4 fault benchmarks, and showed that repair-speciﬁc ﬁne-
tuning could signiﬁcantly improve success rates. On aver-
age, the 10 CLMs already successfully repaired 72% more
faults than state-of-the-art DL-based APR techniques. After
ﬁne-tuning, the number increased to 160%. Jin et al. [165]
proposed InferFix, which contains a LLM (Codex Cushman)
ﬁnetuned on supervised bug-ﬁx data. InferFix achieves a
76% Top-1 repair accuracy on Java, and over 65% on C#
using the InferredBugs dataset. Berabi et al. [166] introduced
TFix, a T5 model ﬁne-tuned on bug-ﬁxing data, reporting
that it outperformed existing learning-based approaches. Xia
et al. [167] combines LLM ﬁne-tuning and prompting to
automate the plastic surgery hypothesis and demonstrated
that their approach ﬁxes 89 and 44 bugs (outperforming the
baseline by 15 and 8).

LLMs can also help to explain the patches that

they
generate. Kang et al. [168] proposed AutoSD to provide
debugging explanation with LLMs to help developers judge
the correctness of patches. They found that AutoSD produced
comparable results to existing baselines with high-quality
repair explanations. Sobania [169] studied the capability of
GPT 3.5 in explaining the patches generated a search-based
repair tool, ARJA-e, on 30 bugs from Defects4J. 84% of the
LLM explanations are found to be correct.


#### C. Performance Improvement

the

Since

inception of

computer programming,

the
paramount importance of performance optimisation has been
recognised. Indeed, performance optimisation is even men-
tioned by Ada Lovelace in her nineteenth-century notes on
the analytical engine [170]. Much initial practical deployment
of optimisation took place in compiler development, through
work on optimising compilers [171]. This is the bedrock on
which current practical and efﬁcient computation rests, but it is
necessarily a one-size-ﬁts-all approach; widely applicable due
to its generality, yet suboptimal for bespoke problem domains
for the same reason. There has, therefore, also been much
work on speciﬁc source-to-source transformations to improve
optimisation, dating back to the 1970s [172], [173].

For a long time, the focus of this work was on ﬁnding
suitable sets of meaning-preserving transformations, the moti-
vation being that a correct program can be transformed into a
more efﬁcient version of itself, while retaining its correctness.
However, more recently, research on program synthesis took
a different turn: Inspired by Genetic Programming [174], and
early results from Automated Program Repair [146], [175], it
considered a wider set of transformations in an approach that
has come to be known as ‘Genetic Improvement’ [8], [176].
The wider set of transformations may produce incorrect
code, but automated testing can ﬁlter these, to ensure sufﬁ-
cient faithfulness to the intended semantics. Furthermore, the
freedom to treat existing code as a kind of ‘genetic material’
produced dramatic improvements in non-functional properties,
such as execution time, memory and power consumption (e.g.,
70x speed up of a non-trivial gene sequencing system [177]).
Although the potential for artiﬁcial intelligence techniques,
such as evolutionary algorithms, to improve performance has
been well studied, researchers have only just begun to consider
the potential for LLM-based performance improvement. In the
work by Madaan et al. [178], the authors use CODEGEN
and CodeX to suggest functionally correct, Performance-
Improving Edits (PIEs), improving execution time of Python
and C++ (already pre-optimised with the maximally opti-
mising compiler option -O3). Similarly, Garg et al.
[179]
proposed DeepDev-PERF, a performance improvement sug-
gestion approach for C# applications that. DeepDev-PERF
took the English-pretrained BART-large model and further
pretrained it on Source code. Kang and Yoo [180] proposed the
use of LLMs to suggest objective-speciﬁc mutation operators
for genetic improvement, and provided demonstrations on
improving efﬁciency and decreasing memory consumption.
Garg et al. [181] proposed RAPGen, which generates zero-
shot prompts for LLMs to improve performance. The prompts
are generated via retrieving a prompt instruction from a pre-
constructed knowledge base of previous performance improve-
ments. Chen et al. [182] used GPT models as baselines for
their source code optimisation method, Supersonic, and found
that Supersonic improves running time for 26.0% of the
programs, compared to only 12.0% for GPT-3.5-Turbo and
4.0% for GPT-4.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

43

Cummins et al. [183] focused on the performance of com-
pilers and presented results on LLMs for optimising compiler
instructions. Their results demonstrate that a relatively small
(7B-parameter) LLM, trained to generate instruction counts
and optimized compiler LLVM code, can generate 3% im-
provements in reducing compiler instruction counts, outper-
forming the state-of-the-art. Their results are also promising
in terms of correctness, with 91% compilable and 70% func-
tionally correct wrt the original compiler output.

1970s
“Correct by
Construction”
Transformations
(e.g., peephole
optimisation)

2010s
“Syntactically Correct”
Transformations
(e.g., Genetic Improvements,
Automated Program Repair)

2020s
“Unconstrained”
Transformations
(e.g., Neural Machine Translations,
Large Language Models)

Fig. 5. The Widening Scope of Program Transformation

Over a period of some 50 years, the software engineering
community has evolved its conception of what
it means
to transform an existing software system into an equivalent
system that improves performance while retaining functional
behaviour. In the 1970s, the strongest concern was correctness,
so transformation palettes were deﬁned to consist solely of
transformation steps that were (functionally) correct by con-
struction.

However, by 2010 the community was already exploring
the application of considerably more relaxed notions of equiv-
alence that merely retain sufﬁcient operational faithfulness
to the behaviour of the original. The tight semantic strait-
jacket of the 1970s was thereby considerably relaxed to allow
transformations that might even fail some test cases. During
the same period, operational performance became increasingly
important. A key underlying principle of this research agenda
is that no overall software system can be deemed functionally
correct, when it is executed on a system in which inefﬁciency
has left insufﬁcient remaining resources. This principle applies
even in the (comparatively rare) cases where the software has
been fully proven to be functionally correct. As the more pithy
slogan has it:

“There is nothing correct about a ﬂat battery” [8].

This evolution of the community’s approach to code trans-
formation and synthesis is depicted in Figure 5 (red and yellow
regions).

In the context of this increasing relaxation of semantic
constraints, we can view LLM-based code optimisation as a
further development of this overall direction of travel: Code
optimised by LLMs may not be even syntactically correct, let
alone semantically correct (depicted by the green region of
Figure 5).

inherent

Despite these correctness challenges,

in LLM-
Based SE, there is a large pool of training data, and LLMs
have a propensity to exhibit emergent behaviour. These obser-
vations combine to yield surprising results that, although not
guaranteed to be correct, can potentially dramatically change
performance characteristics in useful ways.

Of course, as we increasingly allow more permissive trans-
formation pallets in the hope of optimising multiple non-
functional properties, we simultaneously place far greater
reliance upon the ability of testing to provide reassurance
of functional faithfulness. Testing is also vital to check for
regressions in those non-functional properties that are not
targeted by the improvement process. As a result, software
testing in general (and automated high coverage test generation
in particular), will become ever more important.


#### D. Clone Detection and Re-use

There has been much previous work on managed software
reuse [184] in order to extract value and avoid duplication,
a topic also tackled using LLMs [185]. Software typically
contains large numbers of clones, arising from ad hoc re-use,
resulting in much work on automated clone detection [186],
a topic for which fuzz-based ﬁne-tuned LLMs have also been
applied [187].


#### E. Refactoring

When we refactor code, we generally expect its behaviour to
remain unchanged. This is particularly attractive for automated
approaches (such as search-based refactoring [188]) because
it means that we can simply rely on the Automated Regres-
sion Oracle. This ‘automatable oracle for free’ advantage is
signiﬁcant and will also apply to LLM-based refactoring.

Poldrack et al. [75] show that GPT-4 refactoring of existing
code can signiﬁcantly improve code quality according to long-
established structural metrics such as Halstead [189] and Mc-
Cabe [190] complexity. Noever and Williams [83] emphasize
the value of AI-driven code assistants in refactoring legacy
code and simplifying the explanation or functionality of high-
value repositories.


#### F. Open Problems in Maintenance and Evolution

Since so many of the subdomains of software maintenance
and evolution are concerned with existing legacy system
source code, we can expect rapid growth in the application
of LLMs. This section outlines some existing open problems
in this nascent sub-area of research.

1) Open Problems in Performance Improvement: Much
more work is needed on the development of LLM-based tech-
niques for automatically ﬁnding performance improvements.
As with Genetic Improvement, these need not be conﬁned
merely to execution time, but can also consider other non-
functional attributes such as power consumption [191]–[193]
and memory footprint [194] as well as multi-objective, trade-
offs between sets of non-functional properties [195]. We
expect more work on Genetic Improvement-style LLM-based
code optimisation techniques, with the potential for many
dramatic advances and breakthroughs.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

44

2) Open Problems in Refactoring: By deﬁnition, refactor-
ing does not change semantics, so LLM-based refactoring
can rely on the Automated Regression Oracle. It is therefore
surprising that there is not already more work on LLM-based
refactoring. In this subsection, we outline possible directions.
Design patterns have played a critical role in practical
software engineering for three decades [196]. LLMs may help
engineers to refactor existing code to use design patterns, while
providing developer-friendly explanations and documentation.
Refactoring also becomes necessary whenever new tech-
nologies emerge. For example, when an API is updated or a
new API becomes available. Although they can be (sometimes
automatically [197]) repaired, API misuse remains a common
source of software engineering bugs. Automating the process
of refactoring for new APIs is less challenging than other code
transformations, because of the presence of the Automated
Regression Oracle.

Finally, the few-shot learning capabilities of LLMs may
enable more bespoke refactoring. The emergent work on LLM-
based refactoring has focused on global refactoring according
to well-known refactoring patterns. However, programmers
often have project-speciﬁc refactoring requirements. Up to
a third of software engineering effort
is spent on largely
repetitive, tedious, and potentially error-prone refactoring ac-
tivities that implement these project-speciﬁc refactoring needs.
The few-shot learning potential of LLMs may automatically
generalise from speciﬁc examples, automating what we call
‘bespoke’ refactoring. More work is needed to develop tech-
niques for reliable few-shot-learnt bespoke refactorings.


### VII. Documentation Generation

Most of the work on LLM-based software engineering has
focused on the generation of code, but there is also consider-
able potential for LLM-based documentation generation.

Sun et al. [198] explored how ChatGPT performs on code
summarisation of Python code. They used CSN-Python and
compared ChatGPT with NCS, CodeBERT, and CodeT5. They
adopted three widely-used metrics: BLEU, METEOR, and
ROUGE-L. Surprisingly,
the results show that ChatGPT’s
performance is signiﬁcantly worse than the baseline models
in terms of BLEU and ROUGE-L.

Ahmed et al. [66] conducted prompt engineering for code
summarisation on GPT-3.5, while Geng et al. [199] performed
experiments on two Java language datasets, Funcom and TLC,
using Codex: to generate multiple-intent comments. Gent et
al. [200] demonstrate that pre-trained LLMs already have suf-
ﬁcient context to generate multiple different code summaries
from different technical perspectives.


#### A. Open Problems in Documentation Generation and Code
Summarization

Many existing code summarization techniques are retrieval-
based: the given code is represented in a vector format using
a neural representation, which is subsequently used to retrieve
the most relevant textual summarization from the corpus.

There is a clear limitation to this approach due to the fact
that the set of summaries that can be generated are constrained
by the training corpus. LLMs may enable automated code
summarization that is not restricted to this training corpus,
assisted by their natural language processing capabilities.

While this may result in richer and more semantically rele-
vant summaries, we also note that existing evaluation metrics
are often lexical in nature, hindering our ability to compare and
evaluate richer summaries generated by LLMs [198]. Recent
advances in ReAct-based approaches [95] may open up other
avenues for greater assurance in the documentation generated,
even when it cannot be executed.


### VIII. Software Analytics And Repository Mining

There is a well-established ﬁeld of software analytics; how
to yield insight for human engineers from existing software
artefacts [201]. The large amount of software artefact infor-
mation publicly available online has stimulated the growth
of scientiﬁc insights gained by Mining Software Repositories
(MSR) [202], [203]. While MSR tends to focus on scientiﬁc
research insights from such mining, software analytics tends
to focus on opportunities for organisations to gain insight from
the analysis of their own repositories, which can also beneﬁt
AI understandability [204].

Hitherto, in both cases, much of the collection, curation
and analysis of data has relied upon labour-intensive human
analysis. We found no work on the use of LLMs to support
this activity. Nevertheless, because many LLMs have already
ingested this software artefact data, and are capable of provid-
ing reasoning and insight, it seems natural to expect them to
play a signiﬁcant role.

For example, LLMs may identify interesting new MSR
research questions, based on their ability to ingest
large
amounts of data, including research questions and hypotheses
that have previously proved interesting to researchers. They
may also assist with traceability, which software engineers
have great difﬁculty maintaining [205], [206].


### IX. Human Computer Interaction

Finding productive interfaces between human engineers
and software infrastructure has remained a recurring theme
throughout the lifetime of the development of software en-
gineering [207], [208], dating back to the inception of the
discipline in the 1960s [209].

We found evidence of many interesting research ques-
tions. For example, Vaithilingam et al. [210] reported on
the difﬁculties 24 participants had in understanding, editing,
and debugging the Copilot-generated code, while Feldt et
al. [139] proposed a hierarchy of design architecture for LLM-
based software testing agents. Liang et al. [36] surveyed 410
practising software engineers, ﬁnding widespread use of LLMs
to facilitate low-level programming tasks, but also resistance
to using LLMs for more design-level software engineering
activities. Feng et al. [211] collected 316K tweets and 3.2K
Reddit posts about ChatGPT’s code generation to understand
social media’s attitudes toward AI-assisted coding tools.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

45

They found that fear is the dominant emotion associated
with ChatGPT’s code generation, overshadowing other emo-
tions such as happiness and surprise. Ahmad et al. [212]
explore the way in which a novice software architect could
interact with ChatGPT.


### X. Software Engineering Process

Software engineering concerns, not only software products,
but also the process by which they are constructed [213].
Previous research on software assistants [207], [214]–[217]
is clearly of particular relevance to LLM-based software
engineering, a topic some authors have already started to
consider. For example, Ross et al. [218], introduced an LLM-
based programmers’ assistant, evaluating its deployment with
42 participants while Tian et al. [219] highlighted the attention
span limitations of ChatGPT.


### XI. Software Engineering Education

Teachers have expressed concern at

the difﬁculties of
identifying cases where students have relied on LLMs to
construct their assignments [220], while other authors have
argued that the long-term impact of LLMs on education will
be beneﬁcial [221]. However, our present focus rests more
narrowly on the speciﬁc impact of LLMs on the ﬁeld of
software engineering education, where the current literature
focuses on LLM-based tutorial support.

For example, Jalil et al. [222] explored opportunities for
(and issues with) ChatGPT in software testing education.
Savelka et al. [223] analysed the effectiveness of three models
in answering multiple-choice questions from introductory and
intermediate programming courses at the postsecondary level.
Several other authors
[82], [83], [224] explored the capa-
bilities of CodeX for generating programming exercises and
code explanations. Their general ﬁnding was that the majority
of the generated content was novel, sensible, and useful (see
also Section IV-D3).


### XII. Crosscutting Open Research Topics

A number of patterns emerge from the embryonic literature
on LLM-based software engineering. In this section, we out-
line those that raise open research questions that cut across all
software engineering applications

More work is needed on new forms of LLMs, speciﬁ-
cally tailored for software engineering that take advantage of
software’s unique properties and distinguish it from natural
language. Dynamic information is one such key differentiator
currently missing from most of the work. We expect the next
generation of SE-speciﬁc LLMs to address this.

An important aspect of building and training LLMs is their
energy consumption. LLM capabilities have been associated
with their size [226], resulting in rapid growth of model
size [227], [228]. The training and developing of larger models
may have direct environmental impact [229]. While it has been
suggested that the model performance depends not only on
model size but also on the volume of training data [230], the
question of the right model size required to achieve the desired
performance remains unclear.

Lighter models may also widen adoption, thereby leading
to enhanced deployability. Recently, techniques such as low-
rank adaptation (lora) [231] and model quantization [232] have
shown potential, but they remain to be empirically evaluated
with respect to speciﬁc applications.


#### B. The Need for Dynamic Adaptive Prompt Engineering and
Parameter Tuning

Initial work on prompt engineering has demonstrated its
potential to considerably improve the software engineering
artefacts generated by LLMs. However, as already found
[58], the results are highly problem-speciﬁc, so a one-size-
ﬁts-all approach is unrealistic. Furthermore, very few papers
report model parameter settings, yet we know that many of
these, such as the temperature setting, play a crucial role in
determining the nature of the generated LLM output.

As an immediate starting point, it is imperative that authors
make a point of conspicuously reporting these parameter
settings to support replication. However, we also need more
research on dynamic adaptive prompt engineering and model
parameter tuning. This research agenda may draw inspiration
from existing work on parameter tuning for other dynamic
adaptive tasks, such as fuzzing [233]. Dynamic prompt opti-
misation may also exploit techniques associated with SBSE
[12], reformulating prompt optimisation as a multi-objective
computational search process.


#### A. Building and Tuning LLMs for SE


#### C. Hybridisation

Most of the previous work has treated LLMs as atomic
components, with a focus on incorporating these in wider soft-
ware engineering workﬂows. While there have been attempts
to tailor the behaviour, these have tended to focus on prompt
engineering, with a few examples of ﬁne-tuning.

A more challenging but potentially impactful problem lies
in training and ﬁne-tuning models, speciﬁcally for software
engineering tasks. Ding et al. [225] train a BERT-like LLM
with execution inputs and dynamic execution traces. They
show how this dynamic information improves (up to 25%) the
accuracy of the model for downstream software engineering
predictive tasks: vulnerability and clone detection and cover-
age prediction (full execution path and branch coverage).

LLMs are seldom most effective when used in isolation,
but can be highly effective as part of an overall SE process.
More work is needed to understand the design patterns for
SE workﬂows into which LLMs can safely, efﬁciently and
effectively reside. We believe that existing SE theory and
practice associated with generate-and-test approaches, such
as Automated Repair and Genetic Improvement, are already
highly amenable to LLMs.

We expect to see much more work incorporating LLMs
into these existing software engineering frameworks. However,
more work is required to tailor and extend these frameworks,
to best take advantage of the opportunities offered by LLM-
based software engineering.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

46

In particular, we expect to see a rapid development of work
on static and dynamic analyses for prompt engineering and
post-processing of LLM responses. We also expect to see
hybrid software engineering processes, adapting Continuous
Integration pipelines to incorporate LLMs.


#### D. Harnessing Hallucination

While hallucination has widely been regarded as a problem,
as reported in this survey,
it may also prove to provide
beneﬁts when applied to software engineering domains. LLM
hallucinations are seldom entirely random incorrect responses.
Rather, because of their inherent statistical properties, they
would be better characterised as ‘plausible futures’, and this
may often make them useful when set in the right context.

Hallucination can be repurposed to provide potentially use-
ful suggestions for software enhancement. For example, when
hallucinating a test case, the LLM may be repurposed to
suggest new features, while a hallucinated code summarisation
might indicate potential for (human) code misunderstanding;
if the LLM ‘misunderstood’ the code, might not a human also
misunderstand it? When the LLM hallucinates an non-existent
API, it may be repurposed as a way to suggest refactoring to
simplify or extend existing APIs. More work is needed to
exploit this positive potential, and to harness hallucination for
software improvement.


#### E. Robust, Reliable, and Stable Evaluation

Hort et al. [234] conducted a review of 293 papers on LLMs
for code generation, to determine the degree to which sufﬁcient
information was shared to support replication. They found that
only 33% shared source code and 27% shared trained artefacts.
They also evaluated the papers from the perspective of energy
consumption, assessing the degree to which it was possible
for an independent researcher to assess the energy consumed
during training. They report
that approximately 38% (30
out of 79 publications which involve model training) shared
sufﬁcient information to estimate their energy consumption
during training.

Further evidence that there may be a growing issue with
scientiﬁc evaluation quality in the literature on LLM-Based
Software Engineering can be found in the survey of LLM-
Based Testing by Wang et al. [98]. In their survey, they ﬁltered
an initial pool of papers on LLM-Based Testing to remove
those that did not meet standard evaluation quality constraints.
These constraints required papers to include a clear, deﬁned,
repeatable evaluation methodology that includes a control or
baseline against which to measure effectiveness. This ﬁltration
criterion removed more than 90% of the papers that initially
met keyword search criteria.

As these analyses of the literature demonstrate, more work
is clearly needed to establish ﬁrm scientiﬁc foundations for
the emerging discipline of LLM-based Software Engineering.
Such foundations may draw on existing foundations for Em-
pirical Software Engineering in general and, more speciﬁcally,
on AI-based Software Engineering, such as SBSE (where there
is a natural similarity [105], [235]).

Nevertheless, LLMs have their own unique properties, such
as the ability to provide explanations, which will require
domain-speciﬁc theoretical and empirical scientiﬁc founda-
tions.

LLMs inherently exhibit non-deterministic behaviour. Re-
searchers need to carefully design their experiments, conﬁgure
their LLMs (e.g., evaluating the effects of different distribution
sampling strategies), and take into account non-determinism
when drawing their conclusions on LLMs. The SBSE literature
provides advice on the inferential statistics required to support
such evaluation [13], [14].

We will witness a rapid growth in the number and diversity
of language models for software engineers in the coming years.
Both practitioners and practising software engineers will need
reliable, efﬁcient and comprehensive benchmarking systems.
Benchmarking platforms such as TESTPILOT [116] and plat-
forms such as Papers With Code (https://paperswithcode.com/
sota/code-generation-on-humaneval/) will become increas-
ingly important.

As well as generic scientiﬁc foundations, benchmarks and
evaluation platforms, we also expect to see longitudinal stud-
ies of developer behaviour when programming with LLM
assistance, so that we can understand the programmer-LLM
interaction better and design more effective use case scenarios.


#### F. Thorough Testing

The problem of hallucination has already been widely
studied. It will continue to be a topic of great interest, both
within the software engineering community and in the wider
computer science community. While it is likely great progress
will be made, the inherent risk of hallucination is unlikely to
be completely eradicated, since it is as germane to the LLM
technology, as it is to human intelligence. Fortunately, over
more than six decades, software engineers have developed
robust automated veriﬁcation and testing technologies that
help to reduce the impact of human mistakes. We expect that
such technologies will also carry over to artiﬁcial intelligence
mistakes.


#### G. Handling Longer Textual Inputs

The performance of LLMs on large-sized input prompts is
likely to be a topic of great interest in the artiﬁcial intelligence
community [236]. Advances in this area will have a strong
impact on software engineering, because of the considerable
size of software systems and the consequent opportunities that
additionally open when larger prompts are to be effectively
handled.


#### H. Less Well-covered Subdomains of Software Engineering

As our survey reveals, some subdomains of software engi-
neering are notably under-represented in the literature; some
surprisingly so. For example, Requirements Engineering and
Design (Section III), and Refactoring (Section VI-E) enjoy
very little coverage, yet they are surely ripe for consideration,
since they rely heavily upon linguistic forms of analysis and
the recognition and prediction of patterns.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

47

REFERENCES

[1] J. Yang, H. Jin, R. Tang, X. Han, Q. Feng, H. Jiang, B. Yin, and X. Hu,
“Harnessing the Power of LLMs in Practice: A Survey on ChatGPT
and Beyond,” Apr. 2023, arXiv:2304.13712.

[2] W. Ma, S. Liu, W. Wang, Q. Hu, Y. Liu, C. Zhang, L. Nie, and

#### Y. Liu, “The scope of ChatGPT in software engineering: A thorough
investigation,” 2023, arXiv:2305.12138.

[3] S. Anand, A. Bertolino, E. Burke, T. Y. Chen, J. Clark, M. B. Cohen,

#### W. Grieskamp, M. Harman, M. J. Harrold, J. Li, P. McMinn, and

#### H. Zhu, “An orchestrated survey of methodologies for automated soft-
ware test case generation,” Journal of Systems and Software, vol. 86,
no. 8, pp. 1978–2001, August 2013.

[4] C. Cadar and K. Sen, “Symbolic execution for software testing: Three
decades later,” Communications of the ACM, vol. 56, no. 2, pp. 82–90,
Feb. 2013.

[5] M. Harman, Y. Jia, and Y. Zhang, “Achievements, open problems and
challenges for search based software testing (keynote paper),” in 8th
IEEE International Conference on Software Testing, Veriﬁcation and
Validation (ICST 2015), Graz, Austria, April 2015.

[6] E. T. Barr, M. Harman, P. McMinn, M. Shahbaz, and S. Yoo, “The
oracle problem in software testing: A survey,” IEEE Transactions on
Software Engineering, vol. 41, no. 5, pp. 507–525, May 2015.

[7] J. Shin, H. Hemmati, M. Wei, and S. Wang, “Assessing evaluation met-
rics for neural test oracle generation,” arXiv preprint arXiv:2310.07856,
2023.

[8] J. Petke, S. O. Haraldsson, M. Harman, W. B. Langdon, D. R. White,
and J. R. Woodward, “Genetic improvement of software: a comprehen-
sive survey,” IEEE Transactions on Evolutionary Computation, vol. 22,
no. 3, pp. 415–432, Jun. 2018.

[9] A. Cantino, “Prompt engineering tips and tricks with GPT-3,” 2021.
[Online]. Available: https://blog.andrewcantino.com/blog/2021/04/21/
prompt-engineering-tips-and-tricks/

[10] S. Ouyang, J. M. Zhang, M. Harman, and M. Wang, “Llm is like a
box of chocolates: the non-determinism of chatgpt in code generation,”
arXiv prnote arXiv:2308.02828, 2023.

[11] S. Easterbrook, “Empirical research methods for software engineering,”
in Proceedings of the 22nd IEEE/ACM International Conference on
Automated Software Engineering, ser. ASE ’07. New York, NY, USA:
Association for Computing Machinery, 2007, p. 574.

[12] M. Harman, A. Mansouri, and Y. Zhang, “Search based software
engineering: Trends, techniques and applications,” ACM Computing
Surveys, vol. 45, no. 1, pp. 11:1–11:61, November 2012.

[13] A. Arcuri and L. Briand, “A practical guide for using statistical tests
to assess randomized algorithms in software engineering,” in 33rd
International Conference on Software Engineering (ICSE’11). New
York, NY, USA: ACM, 2011, pp. 1–10.

[14] M. Harman, P. McMinn, J. Souza, and S. Yoo, “Search based software
engineering: Techniques, taxonomy, tutorial,” in Empirical software
engineering and veriﬁcation: LASER 2009-2010, B. Meyer and M. Nor-
dio, Eds. Springer, 2012, pp. 1–59, LNCS 7007.

[15] X. Hou, Y. Zhao, Y. Liu, Z. Yang, K. Wang, L. Li, X. Luo,

#### D. Lo, J. Grundy, and H. Wang, “Large language models for
software engineering: A systematic literature review,” arXiv prnote
arXiv:2308.10620, 2023.

[16] T. Goyal, J. J. Li, and G. Durrett, “News summarization and evaluation

in the era of gpt-3,” 2023, arXiv:2209.12356.

[17] R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim, C. Hesse,

#### S. Jain, V. Kosaraju, W. Saunders, X. Jiang, K. Cobbe, T. Eloundou,

#### G. Krueger, K. Button, M. Knight, B. Chess, and J. Schulman,
“Webgpt: Browser-assisted question-answering with human feedback,”
2022, arXiv:2112.09332.

[18] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhari-
wal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal,

#### A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh,

#### D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin,

#### S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford,

#### I. Sutskever, and D. Amodei, “Language models are few-shot learners,”
in Advances in Neural Information Processing Systems, H. Larochelle,

#### M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, Eds., vol. 33. Curran
Associates, Inc., 2020, pp. 1877–1901.

[19] Q. Xie, Z. Luo, B. Wang, and S. Ananiadou, “A survey for biomedical
text summarization: From pre-trained to large language models,” 2023,
arXiv:2304.08763.

[20] K. Kheiri and H. Karimi, “Sentimentgpt: Exploiting gpt for advanced
sentiment analysis and its departure from current machine learning,”
2023, arXiv:2307.10234.

[21] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning repre-
sentations by back-propagating errors,” nature, vol. 323, no. 6088, pp.
533–536, 1986.

[22] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural

computation, vol. 9, no. 8, pp. 1735–1780, 1997.

[23] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N.
Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” 2017,
arXiv:1706.03762.

[24] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,

#### T. Lacroix, B. Rozi`ere, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez,

#### A. Joulin, E. Grave, and G. Lample, “Llama: Open and efﬁcient
foundation language models,” 2023, arXiv:2302.13971.

now has
[25] S. Zhao,
and
[Online]. Available:
2023-02-14-github-copilot-now-has-a-better-ai-model-and-new-capabilities/

better AI model
https://github.blog/

new capabilities.”

“Github Copilot

a

[26] “GitHub CEO says Copilot will write 80% of code sooner than
later,” https://www.freethink.com/robots-ai/github-copilot, accessed:
2023-07-27.

[27] Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond,

#### T. Eccles, J. Keeling, F. Gimeno, A. D. Lago, T. Hubert, P. Choy,
C. d. M. d’Autume, I. Babuschkin, X. Chen, P.-S. Huang, J. Welbl,

#### S. Gowal, A. Cherepanov, J. Molloy, D. J. Mankowitz, E. S. Robson,

#### P. Kohli, N. de Freitas, K. Kavukcuoglu, and O. Vinyals, “Competition-
Level Code Generation with AlphaCode,” Science, vol. 378, no. 6624,
pp. 1092–1097, Dec. 2022, arXiv:2203.07814.

[28] OpenAI, “GPT-4 Technical report,” 2023, arXiv:2303.08774.
[29] S. Bubeck, V. Chandrasekaran, R. Eldan, J. Gehrke, E. Horvitz,

#### E. Kamar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg, H. Nori, H. Palangi,

#### M. T. Ribeiro, and Y. Zhang, “Sparks of Artiﬁcial General Intelligence:
Early experiments with GPT-4,” Apr. 2023, arXiv:2303.12712.
[30] B. Rozi`ere, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X. E. Tan,

#### Y. Adi, J. Liu, T. Remez, J. Rapin, A. Kozhevnikov, I. Evtimov,

#### J. Bitton, M. Bhatt, C. C. Ferrer, A. Grattaﬁori, W. Xiong, A. D´efossez,

#### J. Copet, F. Azhar, H. Touvron, L. Martin, N. Usunier, T. Scialom, and

#### G. Synnaeve, “Code llama: Open foundation models for code,” 2023,
arXiv:2308.12950.

[31] C. J. Neill and P. A. Laplante, “Requirements engineering: the state of

the practice,” IEEE software, vol. 20, no. 6, pp. 40–45, 2003.

[32] Y. Zhang, A. Finkelstein, and M. Harman, “Search based requirements
optimisation: Existing work and challenges,” in International Working
Conference on Requirements Engineering: Foundation for Software
Quality (REFSQ’08), vol. 5025. Montpellier, France: Springer LNCS,
2008, pp. 88–94.

[33] J. Zhang, Y. Chen, N. Niu, and C. Liu, “A Preliminary Evalua-
tion of ChatGPT in Requirements Information Retrieval,” Apr. 2023,
arXiv:2304.12562.

[34] X. Luo, Y. Xue, Z. Xing, and J. Sun, “Prcbert: Prompt learning for
requirement classiﬁcation using bert-based pretrained language mod-
els,” in Proceedings of the 37th IEEE/ACM International Conference
on Automated Software Engineering, 2022, pp. 1–13.

[35] D. Luitel, S. Hassani, and M. Sabetzadeh, “Improving requirements
completeness: Automated assistance through large language models,”
arXiv prnote arXiv:2308.03784, 2023.

[36] “A large-scale survey on the usability of ai programming assistants:
Successes and challenges,” in 46th International Conference on Soft-
ware Engineering (ICSE 2024), April 2024, to appear.

[37] M. Bruch, M. Monperrus, and M. Mezini, “Learning from examples
to improve code completion systems,” in Proceedings of the 7th Joint
Meeting of the European Software Engineering Conference and the
ACM SIGSOFT Symposium on The Foundations of Software Engi-
neering, ser. ESEC/FSE ’09. New York, NY, USA: Association for
Computing Machinery, 2009, p. 213–222.

[38] V. Murali, C. Maddila, I. Ahmad, M. Bolin, D. Cheng, N. Ghor-
bani, R. Fernandez, and N. Nagappan, “Codecompose: A large-
scale industrial deployment of ai-assisted code authoring,” 2023,
arXiv:2305.12050.

[39] D. Fried, A. Aghajanyan, J. Lin, S. Wang, E. Wallace, F. Shi, R. Zhong,
W. tau Yih, L. Zettlemoyer, and M. Lewis, “Incoder: A generative
model for code inﬁlling and synthesis,” 2023, arXiv:2204.05999.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

48

[40] S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer, “The impact of
AI on developer productivity: Evidence from GitHub Copilot,” 2023,
arXiv:2302.06590.

[41] C. Bird, D. Ford, T. Zimmermann, N. Forsgren, E. Kalliamvakou,

#### T. Lowdermilk, and I. Gazit, “Taking ﬂight with copilot: Early insights
and opportunities of ai-powered pair-programming tools,” Queue,
vol. 20, no. 6, pp. 35–57, 2022.

[42] Z. Manna and R. J. Waldinger, “Toward automatic program synthesis,”
Communications of the ACM, vol. 14, no. 3, pp. 151–164, 1971.
[43] S. Gulwani, O. Polozov, R. Singh et al., “Program synthesis,” Foun-
dations and Trends in Programming Languages, vol. 4, no. 1-2, pp.
1–119, 2017.

[44] A. Hindle, E. Barr, Z. Su, P. Devanbu, and M. Gabel, “On the
naturalness of software,” in International Conference on Software
Engineering (ICSE 2012), Zurich, Switzerland, 2012.

[45] E. T. Barr, Y. Brun, P. Devanbu, M. Harman, and F. Sarro, “The plastic
surgery hypothesis,” in 22nd ACM SIGSOFT International Symposium
on the Foundations of Software Engineering (FSE 2014), Hong Kong,
China, November 2014, pp. 306–317.

[46] C. L. Goues, M. Pradel, and A. Roychoudhury, “Automated program
repair,” Communications of the ACM, vol. 62, no. 12, pp. 56–65, 2019.
[47] M. Gabel and Z. Su, “A study of the uniqueness of source code,”
in 18th ACM SIGSOFT international symposium on foundations of
software engineering (FSE 2010).
Santa Fe, New Mexico, USA:
ACM, 7-11 Nov. 2010, pp. 147–156.

[48] J. Darlington and R. M. Burstall, “A transformation system for devel-

oping recursive programs,” J. ACM, vol. 24, no. 1, pp. 44–67, 1977.

[49] Mark Chen et al., “Evaluating Large Language Models Trained on

Code,” Jul. 2021, arXiv:2107.03374.

[50] E. Nijkamp, B. Pang, H. Hayashi, L. Tu, H. Wang, Y. Zhou,

#### S. Savarese, and C. Xiong, “Codegen: An open large language model
for code with multi-turn program synthesis,” 2022, accepted at ICLR
2023.

[51] E. Nijkamp, H. Hayashi, C. Xiong, S. Savarese, and Y. Zhou,
“Codegen2: Lessons for training llms on programming and natural
languages,” 2023, arXiv:2305.02309.

[52] F. F. Xu, U. Alon, G. Neubig, and V. J. Hellendoorn, “A systematic
evaluation of large language models of code,” in Proceedings of the 6th
ACM SIGPLAN International Symposium on Machine Programming.
San Diego CA USA: ACM, Jun. 2022, pp. 1–10.

[53] E. Jiang, E. Toh, A. Molina, K. Olson, C. Kayacik, A. Donsbach, C. J.
Cai, and M. Terry, “Discovering the Syntax and Strategies of Natural
Language Programming with Generative Language Models,” in CHI
Conference on Human Factors in Computing Systems. New Orleans
LA USA: ACM, Apr. 2022, pp. 1–19.

[54] S. Gunasekar, Y. Zhang, J. Aneja, C. C. T. Mendes, A. D. Giorno,

#### S. Gopi, M. Javaheripi, P. Kauffmann, G. de Rosa, O. Saarikivi,

#### A. Salim, S. Shah, H. S. Behl, X. Wang, S. Bubeck, R. Eldan, A. T.
Kalai, Y. T. Lee, and Y. Li, “Textbooks are all you need,” 2023,
arXiv:2306.11644.

[55] A. Kasheﬁ and T. Mukerji, “ChatGPT for Programming Numerical

Methods,” Apr. 2023, arXiv:2303.12093.

[56] L. Chemnitz, D. Reichenbach, H. Aldebes, M. Naveed, K. Narasimhan,
and M. Mezini, “Towards code generation from bdd test case speciﬁ-
cations: A vision,” 2023, arXiv:2305.11619.

[57] J. Li, Y. Zhao, Y. Li, G. Li, and Z. Jin, “Towards Enhancing In-Context
Learning for Code Generation,” Mar. 2023, arXiv:2303.17780.
[58] J.-B. D¨oderlein, M. Acher, D. E. Khelladi, and B. Combemale, “Pi-
loting Copilot and Codex: Hot Temperature, Cold Prompts, or Black
Magic?” Feb. 2023, arXiv:2210.14699.

[59] J. He and M. Vechev, “Controlling Large Language Models to Generate

Secure and Vulnerable Code,” Feb. 2023, arXiv:2302.05319.

[60] J. White, S. Hays, Q. Fu, J. Spencer-Smith, and D. C. Schmidt,
“ChatGPT Prompt Patterns for Improving Code Quality, Refactor-
ing, Requirements Elicitation, and Software Design,” Mar. 2023,
arXiv:2303.07839.

[61] P. Denny, V. Kumar, and N. Giacaman, “Conversing with copilot:
Exploring prompt engineering for solving cs1 problems using natural
language,” in Proceedings of the 54th ACM Technical Symposium on
Computer Science Education V. 1, 2023, pp. 1136–1142.

[62] J. Li, Y. Li, G. Li, Z. Jin, Y. Hao, and X. Hu, “Skcoder: A
sketch-based approach for automatic code generation,” arXiv prnote
arXiv:2302.06144, 2023.

[63] J. Li, G. Li, Y. Li, and Z. Jin, “Enabling programming thinking in large

language models toward code generation,” 2023, arXiv:2305.06599.

[64] S. Jiang, Y. Wang, and Y. Wang, “Selfevolve: A code evolution
framework via large language models,” arXiv prnote arXiv:2306.02907,
2023.

[65] K. Zhang, Z. Li, J. Li, G. Li, and Z. Jin, “Self-edit: Fault-aware code

editor for code generation,” 2023, arXiv:2305.04087.

[66] T. Ahmed, K. S. Pai, P. Devanbu, and E. T. Barr, “Improving Few-
Shot Prompts with Relevant Static Analysis Products,” Apr. 2023,
arXiv:2304.06815.

[67] J. Shin, C. Tang, T. Mohati, M. Nayebi, S. Wang, and H. Hemmati,
“Prompt engineering or ﬁne tuning: An empirical assessment of large
language models in automated software engineering tasks,” arXiv
preprint arXiv:2310.10508, 2023.

[68] S. Zhang, Z. Chen, Y. Shen, M. Ding, J. B. Tenenbaum, and C. Gan,
“Planning with large language models for code generation,” arXiv
prnote arXiv:2303.05510, 2023, to appear, ICLR 2023.

[69] X.

Jiang, Y. Dong, L. Wang, Q. Shang, and G. Li, “Self-
planning Code Generation with Large Language Model,” Mar. 2023,
arXiv:2303.06689.

[70] K. Zhang, G. Li, J. Li, Z. Li, and Z. Jin, “Toolcoder: Teach code

generation models to use api search tools,” 2023, arXiv:2305.04032.

[71] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, and W. Chen,

“CODET: Code Generation With Generated Tests,” 2023.

[72] J. P. Inala, C. Wang, M. Yang, A. Codas, M. Encarnaci´on, S. K. Lahiri,

#### M. Musuvathi, and J. Gao, “Fault-aware neural code rankers,” 2022,
arXiv:2206.03865.

[73] N. Jain, S. Vaidyanath, A. Iyer, N. Natarajan, S. Parthasarathy, S. Ra-
jamani, and R. Sharma, “Jigsaw: large language models meet program
synthesis,” in Proceedings of the 44th International Conference on
Software Engineering.
Pittsburgh Pennsylvania: ACM, May 2022,
pp. 1219–1231.

[74] Y. Dong, X. Jiang, Z. Jin, and G. Li, “Self-collaboration Code Gener-

ation via ChatGPT,” Apr. 2023, arXiv:2304.07590.

[75] R. A. Poldrack, T. Lu, and G. Beguˇs, “AI-assisted coding: Experiments

with GPT-4,” Apr. 2023, arXiv:2304.13187.

[76] B. Yetis¸tiren, I. ¨Ozsoy, M. Ayerdem, and E. T¨uz¨un, “Evaluating the
Code Quality of AI-Assisted Code Generation Tools: An Empirical
Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT,”
Apr. 2023, arXiv:2304.10778.

[77] A. Borji, “A Categorical Archive of ChatGPT Failures,” Apr. 2023,

arXiv:2302.03494.

[78] N. Shinn, F. Cassano, B. Labash, A. Gopinath, K. Narasimhan, and

#### S. Yao, “Reﬂexion: Language Agents with Verbal Reinforcement
Learning,” May 2023, arXiv:2303.11366.

[79] T. Dinh, J. Zhao, S. Tan, R. Negrinho, L. Lausen, S. Zha, and

#### G. Karypis, “Large language models of code fail at completing code
with potential bugs,” 2023, arXiv:2306.03438.

[80] C. Treude, “Navigating Complexity in Software Engineering: A Proto-
type for Comparing GPT-n Solutions,” Jan. 2023, arXiv:2301.12169.
[81] M. Yan, J. Chen, J. M. Zhang, X. Cao, C. Yang, and M. Harman,
“Coco: Testing code generation systems via concretized instructions,”
2023, arXiv:2308.13319.

[82] S. MacNeil, A. Tran, A. Hellas, J. Kim, S. Sarsa, P. Denny, S. Bern-
stein, and J. Leinonen, “Experiences from Using Code Explanations
Generated by Large Language Models in a Web Software Development
E-Book,” in Proceedings of the 54th ACM Technical Symposium on
Computer Science Education V. 1. Toronto ON Canada: ACM, Mar.
2023, pp. 931–937.

[83] D. Noever and K. Williams, “Chatbots as ﬂuent polyglots: Revisiting

breakthrough code snippets,” 2023, arXiv:2301.03373.

[84] J. Sun, Q. V. Liao, M. Muller, M. Agarwal, S. Houde, K. Talamadupula,
and J. D. Weisz, “Investigating Explainability of Generative AI for
Code through Scenario-based Design,” in 27th International Confer-
ence on Intelligent User Interfaces. Helsinki Finland: ACM, Mar.
2022, pp. 212–228.

[85] A. H. Mohammadkhani, C. Tantithamthavorn, and H. Hemmati, “Ex-
plainable ai for pre-trained code models: What do they learn? when
they do not work?” arXiv preprint arXiv:2211.12821, 2022.

[86] H. Hajipour, T. Holz, L. Sch¨onherr, and M. Fritz, “Systematically Find-
ing Security Vulnerabilities in Black-Box Code Generation Models,”
Feb. 2023, arXiv:2302.04012.

[87] R. Khoury, A. R. Avila, J. Brunelle, and B. M. Camara, “How Secure
is Code Generated by ChatGPT?” Apr. 2023, arXiv:2304.09655.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

49

[88] N. Risse and M. B¨ohme, “Limits of machine learning for automatic

vulnerability detection,” 2023, arXiv:2306.17193.

[89] J. Savelka, A. Agarwal, C. Bogart, Y. Song, and M. Sakr, “Can Gen-
erative Pre-trained Transformers (GPT) Pass Assessments in Higher
Education Programming Courses?” Mar. 2023, arXiv:2303.09325.
[90] A. Liu, X. Hu, L. Wen, and P. S. Yu, “A comprehensive evalu-
ation of ChatGPT’s zero-shot Text-to-SQL capability,” Mar. 2023,
arXiv:2303.13547.

[91] N. Nguyen and S. Nadi, “An empirical evaluation of github copilot’s
code suggestions,” in Proceedings of the 19th International Conference
on Mining Software Repositories, ser. MSR ’22. New York, NY, USA:
Association for Computing Machinery, 2022, p. 1–5.

[92] K. Liu, Y. Han, J. Zhang, Z. Chen, F. Sarro, M. Harman, G. Huang,
and Y. Ma, “Who judges the judge: An empirical study on online judge
tests,” in ACM SIGSOFT International Symposium on Software Testing
and Analysis (ISSTA 2023), Jan. 2023.

[93] J. Liu, C. S. Xia, Y. Wang, and L. Zhang, “Is Your Code Generated
by ChatGPT Really Correct? Rigorous Evaluation of Large Language
Models for Code Generation,” May 2023, arXiv:2305.01210.

[94] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and

#### K. Narasimhan, “Swe-bench: Can language models resolve real-world
github issues?” arXiv preprint arXiv:2310.06770, 2023.

[95] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao,
“ReAct: Synergizing reasoning and acting in language models,” 2023,
arXiv:2210.03629.

[96] W. Zhou, S. Kim, V. Murali, and G. A. Aye, “Improving code autocom-
pletion with transfer learning,” in 2022 IEEE/ACM 44th International
Conference on Software Engineering: Software Engineering in Practice
(ICSE-SEIP), 2022, pp. 161–162.

[97] A. M. Turing, “Checking a large routine,” in Report of a Conference on
High Speed Automatic Calculating Machines. Cambridge, England:
University Mathematical Laboratory, Jun. 1949, pp. 67–69.

[98] J. Wang, Y. Huang, C. Chen, Z. Liu, S. Wang, and Q. Wang, “Software
testing with large language model: Survey, landscape, and vision,”
2023, arXiv:2307.07221.

[99] P. Nie, R. Banerjee, J. J. Li, R. J. Mooney, and M. Gligoric, “Learning

deep semantics for test completion,” 2023, arXiv:2302.10166.
[100] Z. Yuan, Y. Lou, M. Liu, S. Ding, K. Wang, Y. Chen, and X. Peng,
“No More Manual Tests? Evaluating and Improving ChatGPT for Unit
Test Generation,” May 2023, arXiv:2305.04207.

[101] P. Bareiß, B. Souza, M. d’Amorim, and M. Pradel, “Code generation
tools (almost) for free? a study of few-shot, pre-trained language
models on code,” arXiv prnote arXiv:2206.01335, 2022.

[102] C. Pacheco and M. D. Ernst, “Randoop: feedback-directed random
testing for java,” in Companion to the 22nd ACM SIGPLAN conference
on Object-oriented programming systems and applications companion,
2007, pp. 815–816.

[103] S. Hashtroudi, J. Shin, H. Hemmati, and S. Wang, “Automated test case
generation using code models and domain adaptation,” arXiv preprint
arXiv:2308.08033, 2023.

[104] M. L. Siddiq, J. C. S. Santos, R. H. Tanvir, N. Ulfat, F. A. Rifat, and

#### V. C. Lopes, “Exploring the Effectiveness of Large Language Models
in Generating Unit Tests,” Apr. 2023, arXiv:2305.00418.

[105] C. Lemieux, J. P. Inala, S. K. Lahiri, and S. Sen, “CODAMOSA:
Escaping Coverage Plateaus in Test Generation with Pre-trained Large
Language Models,” 2023.

[106] J. Hu, Q. Zhang, and H. Yin, “Augmenting greybox fuzzing with

generative ai,” 2023, arXiv:2306.06782.

[107] A. Moradi Dakhel, A. Nikanjam, V. Majdinasab, F. Khomh, and M. C.
Desmarais, “Effective test generation using pre-trained large language
models and mutation testing,” arXiv e-prints, pp. arXiv–2308, 2023.

[108] C. S. Xia, M. Paltenghi, J. L. Tian, M. Pradel, and L. Zhang, “Universal
fuzzing via large language models,” arXiv preprint arXiv:2308.04748,
2023.

[109] Y. Deng, C. S. Xia, H. Peng, C. Yang, and L. Zhang, “Large Language
Models are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via
Large Language Models,” Mar. 2023, arXiv:2212.14834.

[110] Y. Deng, C. S. Xia, C. Yang, S. D. Zhang, S. Yang, and L. Zhang,
“Large Language Models are Edge-Case Fuzzers: Testing Deep Learn-
ing Libraries via FuzzGPT,” Apr. 2023, arXiv:2304.02014.

[111] T.-O. Li, W. Zong, Y. Wang, H. Tian, Y. Wang, and S.-C. Cheung,
“Finding Failure-Inducing Test Cases with ChatGPT,” Apr. 2023,
arXiv:2304.11686.

[112] W. Sun, C. Fang, Y. You, Y. Miao, Y. Liu, Y. Li, G. Deng,

#### S. Huang, Y. Chen, Q. Zhang, H. Qian, Y. Liu, and Z. Chen,
“Automatic code summarization via ChatGPT: How far are we?” 2023,
arXiv:2305.12865.

[113] S. Kang, J. Yoon, and S. Yoo, “Large language models are few-
shot testers: Exploring llm-based general bug reproduction,” in 2023
IEEE/ACM 45th International Conference on Software Engineering
(ICSE), 2023, pp. 2312–2323.

[114] “Prompting is all you need: Automated Android bug replay with Large
Language Models,” in 46th International Conference on Software
Engineering (ICSE 2024), April 2024, to appear.

[115] Z. Yuan, Y. Lou, M. Liu, S. Ding, K. Wang, Y. Chen, and X. Peng,
“No more manual tests? evaluating and improving chatgpt for unit test
generation,” 2023, arXiv:2305.04207.

[116] M. Sch¨afer, S. Nadi, A. Eghbali, and F. Tip, “Adaptive Test Generation
Using a Large Language Model,” Feb. 2023, arXiv:2302.06527.
[117] Z. Xie, Y. Chen, C. Zhi, S. Deng, and J. Yin, “ChatUniTest: a
test generation tool,” May 2023,

ChatGPT-based automated unit
arXiv:2305.04764.

[118] Z. Sun, J. M. Zhang, M. Harman, M. Papadakis, and L. Zhang,
“Automatic testing and improvement of machine translation,” in
ICSE ’20: 42nd International Conference on Software Engineering,
Seoul, South Korea, 27 June - 19 July, 2020, G. Rothermel and

#### D. Bae, Eds. ACM, 2020, pp. 974–985.
[Online]. Available:
https://doi.org/10.1145/3377811.3380420

[119] Z. Sun, J. M. Zhang, Y. Xiong, M. Harman, M. Papadakis, and

#### L. Zhang, “Improving machine translation systems via isotopic
replacement,” in 44th IEEE/ACM 44th International Conference
on Software Engineering, ICSE 2022, Pittsburgh, PA, USA, May
25-27, 2022. ACM, 2022, pp. 1181–1192.
[Online]. Available:
https://doi.org/10.1145/3510003.3510206

[120] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowd-
hery, and D. Zhou, “Self-consistency improves chain of thought rea-
soning in language models,” 2023.

[121] T. J. Ostrand and E. J. Weyuker, “Data ﬂow-based test adequacy anal-
ysis for languages with pointers,” in Symposium on Testing, Analysis,
and Veriﬁcation (TAV4), Victoria, BC, Canada, 1991, pp. 74–86.
[122] A. Bertolino, “Software testing research: Achievements, challenges,
IEEE, 2007,

dreams,” in Future of Software Engineering (FOSE’07).
pp. 85–103.

[123] Y. Jia and M. Harman, “An analysis and survey of the development of
mutation testing,” IEEE Transactions on Software Engineering, vol. 37,
no. 5, pp. 649 – 678, September–October 2011.

[124] M. Papadakis, M. Kintis, J. Zhang, Y. Jia, Y. L. Traon, and M. Harman,
“Mutation testing advances: An analysis and survey,” Advances in
Computers, vol. 112, pp. 275–378, 2019.

[125] T. T. Chekam, M. Papadakis, Y. L. Traon, and M. Harman, “An empir-
ical study on mutation, statement and branch coverage fault revelation
that avoids the unreliable clean program assumption,” in Proceedings
of the 39th International Conference on Software Engineering, ICSE
2017, Buenos Aires, Argentina, May 20-28, 2017, 2017, pp. 597–608.
[126] A. Khanﬁr, R. Degiovanni, M. Papadakis, and Y. L. Traon, “Efﬁcient
mutation testing via pre-trained language models,” arXiv preprint
arXiv:2301.03543, 2023.

[127] A. Garg, R. Degiovanni, M. Papadakis, and Y. L. Traon, “Vulnerability

Mimicking Mutants,” Mar. 2023, arXiv:2303.04247.

[128] A. E. I. Brownlee, J. Callan, K. Even-Mendoza, A. Geiger, C. Hanna,

#### J. Petke, F. Sarro, and D. Sobania, “Enhancing genetic improvement
mutations using large language models,” in SSBSE 2023: Challenge
Track. San Francisco, USA: Springer, 8 Dec 2023, to appear.
[129] R. Pan, T. A. Ghaleb, and L. Briand, “LTM: Scalable and Black-box
Similarity-based Test Suite Minimization based on Language Models,”
arXiv prnote arXiv:2304.01397, 2023.

[130] C. Liu, S. Lu, W. Chen, D. Jiang, A. Svyatkovskiy, S. Fu, N. Sun-
daresan, and N. Duan, “Code Execution with Pre-trained Language
Models,” May 2023, arXiv:2305.05383.

[131] M. Harman and P. O’Hearn, “From start-ups to scale-ups: Opportu-
nities and open problems for static and dynamic program analysis
(keynote paper),” in 18th IEEE International Working Conference on
Source Code Analysis and Manipulation (SCAM 2018), Madrid, Spain,
September 23rd-24th 2018, pp. 1–23.

[132] A. Akli, G. Haben, S. Habchi, M. Papadakis, and Y. Le Traon,
“FlakyCat: Predicting ﬂaky tests categories using few-shot learning,” in

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

50

2023 IEEE/ACM International Conference on Automation of Software
Test (AST), 2023, pp. 140–151.

[133] S. Fatima, T. A. Ghaleb, and L. Briand, “Flakify: A black-box,
language model-based predictor for ﬂaky tests,” IEEE Transactions on
Software Engineering, 2022.

[134] S. Fatima, H. Hemmati, and L. Briand, “Black-box prediction of ﬂaky

test ﬁx categories using language models,” 2023, arXiv:2307.00012.

[135] R. A. Santelices, P. K. Chittimalli, T. Apiwattanapong, A. Orso, and

#### M. J. Harrold, “Test-suite augmentation for evolving software,” in 23rd
Automated Software Engineering (ASE ’08). L’Aquila, Italy: IEEE,
2008, pp. 218–227.

[136] S. Yoo and M. Harman, “Test data regeneration: Generating new test
data from existing test data,” Journal of Software Testing, Veriﬁcation
and Reliability, vol. 22, no. 3, pp. 171–201, May 2012.

[137] R. Abou Assi, C. Trad, M. Maalouf, and W. Masri, “Coincidental
correctness in the defects4j benchmark,” Software Testing, Veriﬁcation
and Reliability, vol. 29, no. 3, p. e1696, 2019.

[138] K. Androutsopoulos, D. Clark, H. Dan, M. Harman, and R. Hierons,
“An analysis of the relationship between conditional entropy and
failed error propagation in software testing,” in 36th International
Conference on Software Engineering (ICSE 2014), Hyderabad, India,
June 2014, pp. 573–583.

[139] R. Feldt, S. Kang, J. Yoon, and S. Yoo, “Towards autonomous
large language models,” 2023,

testing agents via conversational
arXiv:2306.05152.

[140] S. Kang, G. An, and S. Yoo, “A preliminary evaluation of llm-based

fault localization,” arXiv preprint arXiv:2308.05487, 2023.

[141] Y. Wu, Z. Li, J. M. Zhang, M. Papadakis, M. Harman, and Y. Liu,
“Large language models in fault localisation,” 2023, arXiv:2308.15276.
[142] S. Feng and C. Chen, “Prompting Is All Your Need: Automated
Android Bug Replay with Large Language Models,” Jun. 2023,
arXiv:2306.01987.

[143] H. Joshi, J. C. Sanchez, S. Gulwani, V. Le, G. Verbruggen, and

#### I. Radiˇcek, “Repair is nearly generation: Multilingual program repair
with LLMs,” in Proceedings of the AAAI Conference on Artiﬁcial
Intelligence, vol. 37, no. 4, 2023, pp. 5131–5140.

[144] Y. Wu, Z. Li, J. M. Zhang, and Y. Liu, “Condefects: A new dataset to
address the data leakage concern for llm-based fault localization and
program repair,” arXiv preprint arXiv:2310.16253, 2023.

[145] E. Mashhadi, H. Ahmadvand, and H. Hemmati, “Method-level bug
severity prediction using source code metrics and llms,” 2023.
[146] C. Le Goues, T. Nguyen, S. Forrest, and W. Weimer, “GenProg: A
generic method for automatic software repair,” IEEE Transactions on
Software Engineering, vol. 38, no. 1, pp. 54–72, 2012.

[147] K. Huang, Z. Xu, S. Yang, H. Sun, X. Li, Z. Yan, and Y. Zhang, “A sur-
vey on automated program repair techniques,” 2023, arXiv:2303.18184.
[148] A. Marginean, J. Bader, S. Chandra, M. Harman, Y. Jia, K. Mao,

#### A. Mols, and A. Scott, “SapFix: Automated end-to-end repair at scale,”
in International Conference on Software Engineering (ICSE) Software
Engineering in Practice (SEIP) track, Montreal, Canada, 2019.
[149] M. Harman, “Scaling genetic improvement and automated program
repair (keynote paper),” in 3rd IEEE/ACM International Workshop on
Automated Program Repair, APR@ICSE 2022, Pittsburgh, PA, USA,
May 19, 2022.

IEEE, 2022, pp. 1–7.

[150] M. Monperrus, “Automatic software repair: a bibliography,” ACM

Computing Surveys (CSUR), vol. 51, no. 1, p. 17, 2018.

[151] M. Harman and B. F. Jones, “Search based software engineering,”
Information and Software Technology, vol. 43, no. 14, pp. 833–839,
Dec. 2001.

[152] M. Tufano, C. Watson, G. Bavota, M. D. Penta, M. White, and

#### D. Poshyvanyk, “An empirical study on learning bug-ﬁxing patches
in the wild via neural machine translation,” 2019, arXiv:1812.08693.
[153] C. S. Xia and L. Zhang, “Less training, more repairing please: revisiting
automated program repair via zero-shot learning,” in Proceedings of
the 30th ACM Joint European Software Engineering Conference and
Symposium on the Foundations of Software Engineering, 2022, pp.
959–971.

[154] C. S. Xia, Y. Wei, and L. Zhang, “Practical program repair in the era
of large pre-trained language models,” 2022, arXiv:2210.14179.
[155] Y. Wei, C. S. Xia, and L. Zhang, “Copiloting the Copilots: Fusing Large
Language Models with Completion Engines for Automated Program
Repair,” in FSE 2023, 2023.

[156] C. S. Xia and L. Zhang, “Conversational Automated Program Repair,”

Jan. 2023, arXiv:2301.13246.

[157] ——, “Keep the Conversation Going: Fixing 162 out of 337 bugs for

$0.42 each using ChatGPT,” Apr. 2023, arXiv:2304.00385.

[158] X. Chen, M. Lin, N. Sch¨arli, and D. Zhou, “Teaching Large Language

Models to Self-Debug,” Apr. 2023, arXiv:2304.05128.

[159] H. Pearce, B. Tan, B. Ahmad, R. Karri, and B. Dolan-Gavitt, “Exam-
ining zero-shot vulnerability repair with large language models,” 2022,
arXiv:2112.02125.

[160] Y. Charalambous, N. Tihanyi, R. Jain, Y. Sun, M. A. Ferrag, and

#### L. C. Cordeiro, “A new era in software security: Towards self-healing
software via large language models and formal veriﬁcation,” arXiv
preprint arXiv:2305.14752, 2023.

[161] J. Cao, M. Li, M. Wen, and S.-c. Cheung, “A study on Prompt Design,
Advantages and Limitations of ChatGPT for Deep Learning Program
Repair,” Apr. 2023, arXiv:2304.08191.

[162] S. Fakhoury, S. Chakraborty, M. Musuvathi, and S. K. Lahiri, “Towards
Generating Functionally Correct Code Edits from Natural Language
Issue Descriptions,” Apr. 2023, arXiv:2304.03816.

[163] T. Ahmed, S. Ghosh, C. Bansal, T. Zimmermann, X. Zhang, and

#### S. Rajmohan, “Recommending Root-Cause and Mitigation Steps
for Cloud Incidents using Large Language Models,” Feb. 2023,
arXiv:2301.03797.

[164] N. Jiang, K. Liu, T. Lutellier, and L. Tan, “Impact of code language
models on automated program repair,” 2023, arXiv:2302.05020.
[165] M. Jin, S. Shahriar, M. Tufano, X. Shi, S. Lu, N. Sundaresan, and

#### A. Svyatkovskiy, “InferFix: End-to-End Program Repair with LLMs,”
Mar. 2023, arXiv:2303.07263.

[166] B. Berabi, J. He, V. Raychev, and M. T. Vechev, “TFix: Learning to
ﬁx coding errors with a text-to-text transformer,” in Proceedings of
the 38th International Conference on Machine Learning, ICML 2021,
18-24 July 2021, Virtual Event, ser. Proceedings of Machine Learning
Research, M. Meila and T. Zhang, Eds., vol. 139. PMLR, 2021, pp.
780–791.

[167] C. S. Xia, Y. Ding, and L. Zhang, “Revisiting the plastic surgery

hypothesis via large language models,” in ASE 2023, 2023.

[168] S. Kang, B. Chen, S. Yoo, and J.-G. Lou, “Explainable automated
debugging via large language model-driven scientiﬁc debugging,” 2023,
arXiv:2304.02195.

[169] D. Sobania, A. Geiger, J. Callan, A. Brownlee, C. Hanna, R. Moussa,

#### M. Zamorano Lopez, J. Petke, and F. Sarro, “Evaluating explanations
for software patches generated by large language models,” in SSBSE
2023: Challenge Track, ser. LNCS. San Francisco, USA: Springer, 8
Dec 2023, to appear.

[170] A. A. Lovelace, “Sketch of the analytical engine invented by Charles
Babbage by L. F. Menabrea of Turin, ofﬁcer of the military engineers,
with notes by the translator,” 1843, translation with notes on article in
italian in Biblioth`eque Universelle de Gen`eve, October, 1842, Number
82.

[171] A. V. Aho, R. Sethi, and J. D. Ullman, Compilers: Principles, tech-

niques and tools, 1986.

[172] J. Darlington and R. M. Burstall, “A system which automatically
improves programs,” Acta Informatica, vol. 6, pp. 41–60, 1976.
[173] H. Partsch, The CIP Transformation System, 1984, pp. 305–322, peter

Pepper (ed.).

[174] J. R. Koza, Genetic Programming: On the Programming of Computers
by Means of Natural Selection. Cambridge, MA: MIT Press, 1992.
[175] J. H. Perkins, S. Kim, S. Larsen, S. P. Amarasinghe, J. Bachrach,

#### M. Carbin, C. Pacheco, F. Sherwood, S. Sidiroglou, G. Sullivan, W.-

#### F. Wong, Y. Zibin, M. D. Ernst, and M. C. Rinard, “Automatically
patching errors in deployed software,” in Proceedings of the 22nd
Symposium on Operating Systems Principles (SOSP’09), Operating
Systems Review (OSR), October 2009, pp. 87–102.

[176] M. Harman, Y. Jia, W. B. Langdon, J. Petke, I. H. Moghadam, S. Yoo,
and F. Wu, “Genetic improvement for adaptive software engineering
(keynote paper),” in 9th International Symposium on Software Engi-
neering for Adaptive and Self-Managing Systems (SEAMS 2014). New
York, NY, USA: ACM, 2014, pp. 1–4.

[177] W. B. Langdon and M. Harman, “Optimising existing software with ge-
netic programming,” IEEE Transactions on Evolutionary Computation
(TEVC), vol. 19, no. 1, pp. 118–135, Feb 2015.

[178] A. Madaan, A. Shypula, U. Alon, M. Hashemi, P. Ranganathan,

#### Y. Yang, G. Neubig, and A. Yazdanbakhsh, “Learning Performance-
Improving Code Edits,” Feb. 2023, arXiv:2302.07867.

[179] S. Garg, R. Z. Moghaddam, C. B. Clement, N. Sundaresan, and

#### C. Wu, “Deepdev-perf: a deep learning-based approach for improving

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

51

software performance,” in Proceedings of the 30th ACM Joint European
Software Engineering Conference and Symposium on the Foundations
of Software Engineering, 2022, pp. 948–958.

[180] S. Kang and S. Yoo, “Towards objective-tailored genetic improvement

through large language models,” 2023, arXiv:2304.09386.

[181] S. Garg, R. Z. Moghaddam, and N. Sundaresan, “Rapgen: An ap-
proach for ﬁxing code inefﬁciencies in zero-shot,” arXiv preprint
arXiv:2306.17077, 2023.

[182] Z. Chen, S. Fang, and M. Monperrus, “Supersonic: Learning
to generate source code optimisations in c/c++,” arXiv preprint
arXiv:2309.14846, 2023.

[183] C. Cummins, V. Seeker, D. Grubisic, M. Elhoushi, Y. Liang, B. Roziere,

#### J. Gehring, F. Gloeckle, K. Hazelwood, G. Synnaeve, and H. Leather,
“Large language models for compiler optimization,” 2023.

[184] C. W. Krueger, “Software reuse,” ACM Computing Surveys (CSUR),

vol. 24, no. 2, pp. 131–183, 1992.

[185] Q. Huang, J. Zhu, Z. Li, Z. Xing, C. Wang, and X. Xu, “PCR-
Chain: Partial code reuse assisted by hierarchical chaining of prompts
on frozen copilot,” in 2023 IEEE/ACM 45th International Conference
on Software Engineering: Companion Proceedings (ICSE-Companion),
2023, pp. 1–5.

[186] M. Zakeri-Nasrabadi, S. Parsa, M. Ramezani, C. Roy,

and

#### M. Ekhtiarzadeh, “A systematic literature review on source code
similarity measurement and clone detection: Techniques, applications,
and challenges,” Journal of Systems and Software, p. 111796, 2023.

[187] J. Zhao, Y. Rong, Y. Guo, Y. He, and H. Chen, “Understand-
test cases,” arXiv prnote

ing programs by exploiting (fuzzing)
arXiv:2305.13592, 2023.

[188] T. Mariani and S. R. Vergilio, “A systematic review on search-based
refactoring,” Information and Software Technology, vol. 83, pp. 14–34,
2017.

[189] M. H. Halstead, Elements of Software Science. Elsevier, 1977.
[190] T. J. McCabe, “A complexity measure,” vol. 2, pp. 308–320, 1976.
[191] B. R. Bruce, J. Petke, M. Harman, and E. T. Barr, “Approximate oracles
and synergy in software energy search spaces,” IEEE Transactions on
Software Engineering, vol. 45, no. 11, pp. 1150–1169, 2019.
[192] D. Li, A. H. Tran, and W. G. J. Halfond, “Making web applications
more energy efﬁcient for OLED smartphones,” in 36th International
Conference on Software Engineering (ICSE 2014). New York, NY,
USA: ACM, 2014, pp. 527–538.

[193] D. R. White, J. Clark, J. Jacob, and S. Poulding, “Searching for
resource-efﬁcient programs: Low-power pseudorandom number gen-
erators,” in 2008 Genetic and Evolutionary Computation Conference
(GECCO 2008), Atlanta, USA, Jul. 2008, pp. 1775–1782.

[194] F. Wu, M. Harman, Y. Jia, J. Krinke, and W. Weimer, “Deep parameter
optimisation,” in Genetic and evolutionary computation conference
(GECCO 2015), Madrid, Spain, July 2015, pp. 1375–1382.

[195] M. Harman, W. B. Langdon, Y. Jia, D. R. White, A. Arcuri, and

#### J. A. Clark, “The GISMOE challenge: Constructing the Pareto program
surface using genetic programming to ﬁnd better programs (keynote
paper),” in 27th IEEE/ACM International Conference on Automated
Software Engineering (ASE 2012), Essen, Germany, September 2012,
pp. 1–14.

[196] E. Gamma, R. Helm, R. Johnson, and J. Vlissides, Design Patterns.

Addison-Wesley, 1995.

[197] M. Kechagia, S. Mechtaev, F. Sarro, and M. Harman, “Evaluating
automatic program repair capabilities to repair API misuses,” IEEE
Transactions on Software Engineering, vol. 48, no. 7, pp. 2658–2679,
2022.

[198] W. Sun, C. Fang, Y. You, Y. Miao, Y. Liu, Y. Li, G. Deng, S. Huang,

#### Y. Chen, Q. Zhang, H. Qian, Y. Liu, and Z. Chen, “Automatic
Code Summarization via ChatGPT: How Far Are We?” May 2023,
arXiv:2305.12865.

[199] M. Geng, S. Wang, D. Dong, H. Wang, G. Li, Z. Jin, X. Mao, and

#### X. Liao, “An Empirical Study on Using Large Language Models for
Multi-Intent Comment Generation,” Apr. 2023, arXiv:2304.11384.

[200] “Large language models are few-shot summarizers: Multi-intent com-
ment generation via in-context learning,” in 46th International Con-
ference on Software Engineering (ICSE 2024), April 2024, to appear.
[201] T. Menzies and T. Zimmermann, “Software analytics: so what?” IEEE

Software, vol. 30, no. 4, pp. 31–37, 2013.

[202] A. E. Hassan, “The road ahead for mining software repositories,” in

2008 Frontiers of Software Maintenance.

IEEE, 2008, pp. 48–57.

[203] W. Martin, F. Sarro, Y. Jia, Y. Zhang, and M. Harman, “A survey of
app store analysis for software engineering,” IEEE Transactions on
Software Engineering, vol. 43, no. 9, 2017.

[204] T. Menzies and T. Zimmermann, “Software analytics: What’s next?”

IEEE Software, vol. 35, no. 5, pp. 64–70, 2018.

[205] G. Spanoudakis and A. Zisman, “Software traceability: a roadmap,” in
Handbook of software engineering and knowledge engineering: vol 3:
recent advances. World Scientiﬁc, 2005, pp. 395–428.

[206] J. Cleland-Huang, O. Gotel, A. Zisman et al., Software and systems

traceability. Springer, 2012, vol. 2, no. 3.

[207] C. Lebeuf, M.-A. Storey, and A. Zagalsky, “Software bots,” IEEE

Software, vol. 35, no. 1, pp. 18–23, 2017.

[208] M. Lehman and W. Turski, “Essential properties of ipses,” ACM
SIGSOFT Software Engineering Notes, vol. 12, no. 1, pp. 52–55, 1987.
[209] M. H. Hamilton and W. R. Hackler, “Universal systems language:
lessons learned from apollo,” Computer, vol. 41, no. 12, pp. 34–43,
2008.

[210] P. Vaithilingam, T. Zhang, and E. L. Glassman, “Expectation vs. Ex-
perience: Evaluating the Usability of Code Generation Tools Powered
by Large Language Models,” in CHI Conference on Human Factors
in Computing Systems Extended Abstracts. New Orleans LA USA:
ACM, Apr. 2022, pp. 1–7.

[211] Y. Feng, S. Vanam, M. Cherukupally, W. Zheng, M. Qiu, and H. Chen,
“Investigating code generation performance of ChatGPT with crowd-
sourcing social data,” in 2023 IEEE 47th Annual Computers, Software,
and Applications Conference (COMPSAC), 2023, pp. 876–885.
[212] A. Ahmad, M. Waseem, P. Liang, M. Fehmideh, M. S. Aktar, and

#### T. Mikkonen, “Towards Human-Bot Collaborative Software Architect-
ing with ChatGPT,” Feb. 2023, arXiv:2302.14600.

[213] R. Pressman, Software Engineering: A Practitioner’s Approach, 3rd ed.
Maidenhead, Berkshire, England, UK.: McGraw-Hill Book Company
Europe, 1992, european adaptation (1994). Adapted by Darrel Ince.
ISBN 0-07-707936-1.

[214] K. Bojarczuk, I. Dvortsova, J. George, N. Gucevska, M. Harman,

#### M. Lomeli, S. Lucas, E. Meijer, R. Rojas, and S. Sapora, “Measure-
ment challenges for cyber cyber digital twins: Experiences from the
deployment of Facebook’s WW simulation system (keynote paper),”
in ACM/IEEE International Symposium on Empirical Software Engi-
neering and Measurement (ESEM ’21), October 2021, keynote talk
given jointly by Maria Lomeli and Mark Harman.

[215] C. Cornes, J. Courant, J.-C. Filliatre, G. Huet, P. Manoury, C. Munoz,

#### C. Murthy, C. Paulin-Mohring, A. Saibi, and B. Werner, “The coq proof
assistant, reference manual, version 5.10,” Inria, Institut National de
Recherche en Informatique et en Automatique, Technical Report RT-
0177, Jul. 1995.

[216] K. B. Gallagher, “Evaluating the surgeon’s assistant: Results of a pilot
study,” in International Conference on Software Maintenance (ICSE
’92), Los Alamitos, California, USA, Nov. 1992, pp. 236–244.
[217] M. Ward, F. W. Calliss, and M. Munro, “The maintainer’s assistant,” in
International Conference on Software Maintenance (ICSM 1989), Los
Alamitos, California, USA, 1989, p. 307.

[218] S. I. Ross, F. Martinez, S. Houde, M. Muller, and J. D. Weisz,
“The Programmer’s Assistant: Conversational Interaction with a Large
Language Model for Software Development,” in Proceedings of the
28th International Conference on Intelligent User Interfaces. Sydney
NSW Australia: ACM, Mar. 2023, pp. 491–514.

[219] H. Tian, W. Lu, T. O. Li, X. Tang, S.-C. Cheung, J. Klein, and T. F.
Bissyand´e, “Is ChatGPT the Ultimate Programming Assistant – How
far is it?” Apr. 2023, arXiv:2304.11938.

[220] L. Meckler and P. Verma, “Teachers are on alert for inevitable cheating

after release of ChatGPT,” The Washington post, December 2022.

[221] W. Heaven, “ChatGPT is going to change education, not destroy it,”

MIT Technology review, April 2023.

[222] S. Jalil, S. Raﬁ, T. D. LaToza, K. Moran, and W. Lam, “ChatGPT
and Software Testing Education: Promises & Perils,” Mar. 2023,
arXiv:2302.03287.

[223] J. Savelka, A. Agarwal, C. Bogart, and M. Sakr, “Large Language
Models (GPT) Struggle to Answer Multiple-Choice Questions about
Code,” Mar. 2023, arXiv:2303.08033.

[224] S. Sarsa, P. Denny, A. Hellas, and J. Leinonen, “Automatic Genera-
tion of Programming Exercises and Code Explanations Using Large
Language Models,” in Proceedings of the 2022 ACM Conference on
International Computing Education Research V.1. Lugano and Virtual
Event Switzerland: ACM, Aug. 2022, pp. 27–43.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

52

[225] “TRACED: Execution-aware pre-training for source code,” in 46th
International Conference on Software Engineering (ICSE 2024), April
2024, to appear.

[226] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess,

#### R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei, “Scaling laws
for neural language models,” 2020, arXiv:2001.08361.

[227] Aakanksha Chowdhery et al., “PaLM: Scaling language modeling with

pathways,” 2022, arXiv:2204.02311.

[228] Jack W. Rae et al., “Scaling language models: Methods, analysis &

insights from training gopher,” 2022, arXiv:2112.11446.

[229] P. Henderson, J. Hu, J. Romoff, E. Brunskill, D. Jurafsky, and J. Pineau,
“Towards the systematic reporting of the energy and carbon footprints
of machine learning,” J. Mach. Learn. Res., vol. 21, no. 1, jan 2020.
[230] J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai,

#### E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark,

#### T. Hennigan, E. Noland, K. Millican, G. van den Driessche, B. Damoc,

#### A. Guy, S. Osindero, K. Simonyan, E. Elsen, J. W. Rae, O. Vinyals,
and L. Sifre, “Training compute-optimal large language models,” 2022,
arXiv:2203.15556.

[231] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang,
and W. Chen, “Lora: Low-rank adaptation of large language models,”
2021, arXiv:2106.09685.

[232] A. Polino, R. Pascanu, and D. Alistarh, “Model compression via

distillation and quantization,” 2018, arXiv:1802.05668.

[233] V. J. M. Man`es, H. Han, C. Han, S. K. Cha, M. Egele, E. J. Schwartz,
and M. Woo, “The art, science, and engineering of fuzzing: A survey,”
CoRR, vol. abs/1812.00140, 2018, 1812.00140.

[234] M. Hort, A. Grishina, and L. Moonen, “An exploratory literature study
on sharing and energy use of language models for source code,” 2023,
arXiv:2307.02443.

[235] Y. Tang, Z. Liu, Z. Zhou, and X. Luo, “ChatGPT vs SBST: A compara-
tive assessment of unit test suite generation,” 2023, arXiv:2307.00588.
[236] U. Shaham, E. Segal, M. Ivgi, A. Efrat, O. Yoran, A. Haviv, A. Gupta,

#### W. Xiong, M. Geva, J. Berant, and O. Levy, “SCROLLS: Stan-
dardized CompaRison Over Long Language Sequences,” Oct. 2022,
arXiv:2201.03533.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:27:45 UTC from IEEE Xplore. Restrictions apply.

53


---

> *End of P-10*

<br><br>

<a id="p11-----survey-of-different-large-language-model-architectures-trends-benchmarks-and-challenges"></a>

## P-11 — Survey of Different Large Language Model Architectures: Trends, Benchmarks, and Challenges

| Field | Details |
|-------|---------|
| **Paper ID** | `P-11` |
| **Title** | Survey of Different Large Language Model Architectures: Trends, Benchmarks, and Challenges |
| **Authors** | Minghao Shao, Abdul Basit, Ramesh Karri, and Muhammad Shafique |
| **Affiliation(s)** | (1) New York University Tandon School of Engineering, New York, NY, USA<br>(2) NYU Abu Dhabi, Abu Dhabi, UAE |
| **Venue** | IEEE Access |
| **Volume / Year** | Vol. 12, 2024 |
| **DOI** | [10.1109/ACCESS.2024.3482107](https://doi.org/10.1109/ACCESS.2024.3482107) |
| **Dates** | Received: 13 August 2024 | Accepted: 8 October 2024 | Published: 16 October 2024 | Current Version: 20 December 2024 |

---

Received 13 August 2024, accepted 8 October 2024, date of publication 16 October 2024, date of current version 20 December 2024.

Digital Object Identifier 10.1109/ACCESS.2024.3482107

Survey of Different Large Language Model
Architectures: Trends, Benchmarks,
and Challenges

MINGHAO SHAO 1, (Graduate Student Member, IEEE), ABDUL BASIT 2,
RAMESH KARRI 1, (Fellow, IEEE), AND MUHAMMAD SHAFIQUE 2, (Senior Member, IEEE)
1New York University Tandon School of Engineering, New York University, New York, NY 10012, USA
2Abu Dhabi Engineering Division, New York University Abu Dhabi, Abu Dhabi, United Arab Emirates

Corresponding author: Minghao Shao (shao.minghao@nyu.edu)

This work was supported in part by the New York University Abu Dhabi (NYUAD) Center for Artificial Intelligence and Robotics (CAIR),
funded by Tamkeen under the NYUAD Research Institute under Award CG010; and in part by the NYUAD Center for CyberSecurity
(CCS), funded by Tamkeen under the NYUAD Research Institute under Award G1104.


### Abstract

Large Language Models (LLMs) represent a class of deep learning models adept at
understanding natural language and generating coherent responses to various prompts or queries. These
models far exceed the complexity of conventional neural networks, often encompassing dozens of neural
network layers and containing billions to trillions of parameters. They are typically trained on vast datasets,
utilizing architectures based on transformer blocks. Present-day LLMs are multi-functional, capable of
performing a range of tasks from text generation and language translation to question answering, as well as
code generation and analysis. An advanced subset of these models, known as Multimodal Large Language
Models (MLLMs), extends LLM capabilities to process and interpret multiple data modalities, including
images, audio, and video. This enhancement empowers MLLMs with capabilities like video editing, image
comprehension, and captioning for visual content. This survey provides a comprehensive overview of the
recent advancements in LLMs. We begin by tracing the evolution of LLMs and subsequently delve into the
advent and nuances of MLLMs. We analyze emerging state-of-the-art MLLMs, exploring their technical
features, strengths, and limitations. Additionally, we present a comparative analysis of these models and
discuss their challenges, potential limitations, and prospects for future development.


### Index Terms / Keywords

Large language models (LLMs), Transformer architecture, generative models, survey,
multimodal learning, deep learning, natural language processing (NLP).


### I. Introduction
The introduction of the Transformer architecture [1] in
in the trajectory of
2017 marked an inflection point
Natural Language Processing (NLP) technology. One notable
derivative of this innovation is Large Language Models
(LLMs). Demonstrating proficiency across multiple NLP
tasks, LLMs have been integral for text generation, machine
translation, and natural
language understanding. Their
evolution, spanning several years, has not only underlined

The associate editor coordinating the review of this manuscript and

approving it for publication was Sangsoon Lim .

their power in linguistic tasks but also showcased their
versatility in handling diverse formats like images, videos,
and robotic interfaces.

Notable tasks for which LLMs have been used include:
- Text generation of coherent text from structured input

upon receiving pertinent instructions.

- Logical reasoning: Analysis and inference based on

logic intrinsic to a given scenario.

- Machine Translation across linguistic frameworks.
- Summarization: Contextual abridgment of content.
- Multimodal support: Beyond textual content, LLMs
also facilitate inputs and outputs in various formats,

188664


2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

FIGURE 1. Structured layout of the paper is presented, detailing the organization of sections including introduction,
background and comparison, state-of-the-art LLMs and methodologies, challenges, and conclusion.

including images, videos, and interactions in robotic
environments, leveraging multiple modalities.

The genesis of LLM development can be traced back to
2018 with the advent of GPT [2] and BERT [3]. Each model,
crafted with distinct architectures, catered to specific niches
within the LLM spectrum. Contemporary LLMs primarily
leverage the foundational Transformer architecture and can
be grouped as:

- Auto-encoding: Primarily encoder-based, these models
are tailored for contextual NLP tasks. E.g., BERT and
its derivatives.

- Auto-regressive: Decoder-centric,

these models are

optimized for generative tasks. E.g., GPT series.

- Encoder-Decoder: Amalgamating both encoder and
decoder structures, these LLMs harness the strengths of
the preceding two types, albeit with certain trade-offs.
E.g., the Pangu series, including Pangu-α and Pangu-(cid:54)
[4], [5].

The structure of this paper is designed to furnish a concise
yet thorough overview of LLMs. Initially, we delve into the
essentials of LLMs, elucidating the underlying technologies
and key terminology. We then provide a panoramic view
of the LLM evolution, spotlighting influential contributors
and institutions. Next, we explore avant-garde LLMs, pivotal
in shaping the history of this domain. We culminate with
a performance review of LLMs in their designated tasks,
concluding with insights and reflections. In essence, our
contributions encompass:

1) Constructing a detailed timeline of seminal LLMs up to

the release of this paper.

2) Distilling and collating pioneering technologies and

strategies pivotal in the evolution of LLMs.

3) Undertaking a holistic comparison of LLMs across
architectures and evaluating their performance metrics.
4) Assessing the overarching impacts and challenges posed

by contemporary LLMs.


### II. Background
LLMs predominantly encompass three architectural catego-
rizations: encoder-only, decoder-only, and encoder-decoder.
Each category has its unique strengths and constraints and
finds relevance across various applications and contexts.
This section explains the architecture behind modern LLMs,
starting with the general transformer architecture, followed
by an exploration of the three categories built upon this
architecture.


#### A. TRANSFORMER
The contemporary landscape of LLMs predominantly
employs the Transformer architecture, introduced by Vaswani
et al. in 2017 [1]. This architecture represents a paradigm
shift away from the recurrent sequence-to-sequence models,
such as Long Short-Term Memory (LSTM) networks [6]
and Recurrent Neural Networks (RNNs) [7], which were
conventionally used. The key innovation of the Transformer
lies in its ability to process tokens in parallel, in contrast
to the sequential processing constraint
in LSTMs and
RNNs, where the processing of each token depends on
its predecessors. The Transformer achieves this through its
multi-head self-attention mechanism, which allows for the
parallelized training of models [1].

Conceptually,

the Transformer architecture consists of
encoder and decoder components. The encoder maps input
sequences to a higher-dimensional embedding space, while

VOLUME 12, 2024

188665

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 1. Comparison of Auto-Encoding, Auto-Regressive, and Sequence-to-Sequence models.

position in the input sequence, thus enabling the model to
interpret the order of words effectively, despite processing
inputs in parallel.

A particular mathematical formula involving the sine and
cosine functions is used in positional encoding. This formula
ensures that a distinct encoding is assigned to every position
in the sequence, enabling the model to be informed about the
token’s position by appending this encoding to the token’s
embedding. The precise equations employed are:
(cid:17)

(cid:16)

E(pos, 2i) = sin

pos
100002i/dim
(cid:16)
pos
100002i/dim

(1)

(cid:17)

(2)

E(pos, 2i + 1) = cos

FIGURE 2. The architecture of the Transformer model, which includes an
encoder-decoder structure. Key components such as multi-head
attention, positional encoding, and residual connections facilitate
efficient learning and performance in tasks such as natural language
processing and machine translation.

the decoder generates output sequences from these embed-
dings. Typically, a Transformer model includes multiple
layers of both encoders and decoders. Figure 2 provides an
illustrative representation of the Transformer architecture.

Unlike traditional models that process data sequentially,
Transformers enable significantly faster and more efficient
parallel processing by handling all parts of the input data
simultaneously. To address the challenge of maintaining
sequence information without inherent sequential processing,
Transformers use a technique called positional encoding.
This mechanism allows each token, such as a word in a
sentence, to encode its relative position in the sequence.
Positional encoding is essential; without it, the Transformer
would treat a sentence as a bag of words, completely oblivious
to the order of those words.

Positional encoding utilizes a specific mathematical
formula involving sine and cosine functions. This formula
ensures that each position in the sequence receives a
unique encoding. By appending this encoding to the token’s
embedding, the model gains insight into the token’s position
within the sequence. The precise equations used are designed
to provide a distinct positional signal for every possible

The token’s position in the sequence is denoted by pos,
while i spans from 0 to half of the embedding dimension
(dim), indexing even and odd positions respectively. The
choice of sine and cosine functions is particularly advanta-
geous because they provide a unique and consistent way to
encode positional information across the embedding space.
This setup not only simplifies the model’s learning to attend
based on relative positions but also enables generalization to
sequence lengths beyond those encountered during training.
The elegance of this method lies in its ability to imbue
the model with the capacity to discern patterns in the
data, enriched with positional context. This straightforward
yet profound approach has been pivotal to the success of
Transformer models in diverse tasks, ranging from text
generation and language translation to applications beyond
language, such as image recognition.


#### B. AUTO-ENCODING MODELS
Primarily tailored for natural
language processing tasks
centered around comprehension, encoder-only models like
BERT [3], ERNIE [8], and ALBERT [9] have carved a niche
for themselves. Training techniques such as bidirectional
learning and masking enable them to excel in contextual
understanding. However, they have certain limitations:
- Constrained to fixed-length input sequences.
- Inherent context-dependency can be a hindrance for text

generation.

- Given their composition lacks a decoder, downstream

task adaptation necessitates fine-tuning.


#### C. AUTO-REGRESSIVE MODELS
These models, including renowned ones like GPT [2] and the
LLaMA series [10], have gained prominence in recent times.

188666

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

Their auto-regressive design implies that token generation
hinges on preceding tokens, rendering them apt for generation
tasks. These models offer:

- Flexibility in accepting varied input lengths, making

them adept at extended data generation.

- Proficiency in few-shot or zero-shot tasks, circumvent-

ing the need for specific fine-tuning.

- However, their inability to capture overall context means

they draw insights from antecedent tokens.


#### D. SEQUENCE-TO-SEQUENCE MODELS
Models such as T5 [11] and GLM [12], harmonize strengths
of the preceding two types. These models are adept at map-
ping input sequences to fixed-length embeddings, allowing
the decoder to generate contextually relevant outputs. This
makes them particularly effective for conditional generation
tasks, such as summarization,
translation, and question
answering, where the output depends closely on the provided
input.

The integration of encoder and decoder components
enables Seq2Seq models to handle complex inputs but comes
with drawbacks:

- Amalgamation increases parameter count, potentially

affecting efficiency.

- Training such models requires substantial computational
resources due to the complexity of aligning the input and
output sequences.


#### E. VARIATIONAL AUTO-ENCODER
Variational Auto-encoder (VAE) [13] is a sophisticated
generative model that evolves from traditional auto-encoders
(AE) by integrating probabilistic modeling to develop a
meaningful and versatile latent space. Unlike standard AEs,
which compress input data into a static representation that
the decoder uses to reconstruct the original data, in VAE,
the encoder produces a probability distribution defined by
means and variances instead of a singular deterministic point.
Figure 3 show the difference between of the principle of
auto-encoders and variational auto-encoders.

FIGURE 3. (A) Workflow of Auto-encoder, auto-encoder encode the
feature attribute directly. (B) Workflow of Variational Auto-encoder,
different from auto-encoder, VAEs encode the feature distribution and
reconstruct the image based on the sample of distribution, which give the
VAEs the ability to generate new images.

VAE utilizes probabilistic encoding to create a dynamic
and adaptable latent space, allowing not only data reconstruc-
tion but also new data generation by sampling from learned
probability distributions. This enhances model generalization
and ensures smooth transitions in the latent space, crucial
for tasks like data generation and augmentation. It leverages
the reparameterization trick to keep gradients flowing
through stochastic sampling processes during backpropa-
gation, maintaining the differentiability of latent variables
for conventional training. Their objective function balances
reconstruction loss, assessing the accuracy of decoded
samples against original inputs, with Kullback-Leibler (KL)
divergence, promoting approximations of latent distributions
to a standard Gaussian. This dual focus ensures both precise
input reconstruction and a smooth, continuous latent space,
making VAE powerful
tools for applications in image
generation, data augmentation, and anomaly detection. At the
time this paper was released, VAEs had diversified into
a wide array of variants. For a comprehensive overview
and comparison of these different VAE variants, readers are
encouraged to refer to [14] and [15] which provide extensive
analyses and insights into the evolution and functionalities of
these models.The training of VAE can be represented with
following formula

L(θ, φ; x) = Eqφ (z|x)[log pθ (x|z)] − KL[qφ(z|x)∥p(z)]
where Eqφ (z|x)[·] represents the expectation under the distri-
bution qφ(z|x), log pθ (x|z) is the logarithm of the likelihood,
which is how well the model can reconstruct the input from
the latent variables, KL[qφ(z|x)∥p(z)] is the KL divergence
between the approximate posterior qφ(z|x) as a regularization
by encouraging the posterior to be close to the prior with a
Gaussian distribution.


#### F. GENERATIVE ADVERSARIAL NETWORK
Generative Adversarial Networks (GANs) are a class of
DL frameworks introduced by Goodfellow et al. [16].
GANs consist of two neural networks, a generator and
a discriminator, which are trained simultaneously through
adversarial processes. The generator aims to create synthetic
data that resembles the real data, while the discriminator’s
role is to distinguish between real and synthetic data. Over
time, as training progresses, the generator becomes better at
creating realistic data, and the discriminator becomes better
at differentiating real from fake data, illustrated in Figure 4.

- Generator: Takes a noise vector (randomly sampled)
and maps it into a data space, aiming to produce samples
that resemble the training data. The generator’s goal is
to generate data that is indistinguishable from the real
data.

- Discriminator: Takes a sample (real or generated) and
predicts whether it is real (from the training dataset)
or fake (generated by the generator). It is trained to
maximize the probability of correctly classifying real
and generated samples.

VOLUME 12, 2024

188667

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

FIGURE 4. Basic architecture of a Generative Adversarial Network (GAN).
The generator creates synthetic images from a latent space, while the
discriminator distinguishes between real images from the dataset and
generated images. The generator is trained to maximize the
discriminator’s error, while the discriminator is trained to minimize its
error in distinguishing real from fake images, leading to adversarial
learning between the two components.

The training process of GANs can be described as
a min-max game where G is the Generator, D is the
Discriminator, x represents real data samples, z is a noise
vector, pdata denotes the data distribution, and pz is the noise
distribution.

min
G

max
D

V (D, G) = Ex∼pdata(x)[log D(x)]

+ Ez∼pz(z)[log(1 − D(G(z)))]

1) VARIANTS OF GANs
Since their inception, numerous variations of GANs have
been proposed to address specific challenges such as mode
collapse, training stability, and applicability to different types
of data (e.g., images, text, or audio). Table 2 contains the
summary of some of the most widely used GAN variants
along with their unique characteristics.

Several surveys have extensively covered the advance-
ments and applications of GANs. Wang et al. [28] provide
a detailed overview of GAN architectures and challenges like
mode collapse. Gui et al. [29] review methods to stabilize
training and improve image quality, while Creswell et al.
[30] focus on GANs’ creative applications, including style
transfer. Given the depth of these reviews, our paper will
concentrate on Large Language Models (LLMs), exploring
their generative capabilities and contributions to natural
language understanding.


### III. Previous Domain-Based Llm Surveys
In this section, we conduct a comprehensive analysis of
the existing surveys on large language models (LLMs).
We provide a comparative evaluation of
these survey
papers based on the topics they address. The surveys are
chronologically organized in Table 3, allowing readers to
track the evolution of research focus over time. By examining
the content covered in these surveys, as summarized in
the table, readers can gain a nuanced understanding of the
progress made in the development of advanced LLMs. The
categories are comprised of:

- Architecture: Details about the structural design of
the LLMs discussed,
types and
configurations, including Decoder only, Encoder only,
and Decoder-Encoder Models.

including model

- Dataset:

Information about

the datasets used for

training and evaluating the LLMs.

- Pre-training: Methods and techniques used for training

the foundation LLMs.

- Fine-tuning: Strategies for adapting pre-trained LLMs
to specific tasks or domains to improve domain-specific
performance.

- Benchmark: Evaluation metrics

and benchmark

datasets used to assess LLM/MLLM performance.

- Challenges: Identification of challenges and techniques
to optimize development and deployment of LLMs.
- MLLMs: Discussion on Multilingual Language Models

and their specific considerations.

- Applications: Real-world applications and use cases of

state-of-the-art LLMs.

Our survey provides a brief overview of all these categories
but delves deeply into the Architecture, Benchmark, and
Challenges aspects. This in-depth focus aims to offer
a detailed understanding of
innovations,
evaluation methodologies, and challenges in the field of large
language models. Some notable surveys in the domain of
LLM/MLLMs are highlighted:

the structural

- The survey by Xiao et al. [40] provides an extensive
overview of LLMs and MLLMs within the medical
domain. However, our survey addresses the general
methodologies for fine-tuning and LLM architectures,
applicable to a wide range of use cases beyond the
medical field. By addressing these broader aspects,
our survey provides a more holistic view of
the
advancements, challenges, and future directions in the
field of LLMs, making it a valuable resource for a wider
audience.

- The survey by Yin et al. [49] offers an overview
of the progress in multimodal large language models
(MLLMs). It covers the basic formulation, related con-
cepts, research topics, technical points, challenges, and
future directions of MLLMs. While the MLLM survey
provides valuable insights, our survey fills the gaps
by offering detailed technical analysis, broader domain
coverage, comprehensive comparative evaluations, and
in-depth discussions on challenges. Our survey is a more
versatile and informative resource for a wider audience
in regards to MLLMs.

- The notable survey from Zhao et al. [81] from early
2023 offers a comprehensive review of the development
and applications of LLMs. However, this survey does
the latest developments and models in
not cover
the fast-evolving field of LLMs. Since the pace of
advancement in LLMs is rapid, many newer models
and techniques that have emerged in the latter part of
2023 and early 2024 are not included. Our survey fills
this gap by including the most recent advancements
and models, and providing an in-depth benchmarking
analysis for researchers and practitioners.

Table 4 presents a review of the available survey papers on
large language models (LLMs) as of the time of this writing.

188668

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 2. Summary of different GAN models and their key ideas.

TABLE 3. Survey Papers on Large Language Models: A comparative analysis.

Each survey offers unique insights into the application
of LLMs across various domains. To facilitate a clearer
understanding,
these surveys are categorized into three
types:

- General surveys providing an overview of the evolution

of LLMs.

- Application-oriented surveys

focusing on specific

fields.

VOLUME 12, 2024

188669

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 4. Collection of previous LLM survey paper categorized into the
major topic of their discussion.

FIGURE 5. Performance trajectory of various LLMs on the MMLU
benchmark illustrating average accuracy percentages. The ‘Random
Baseline’ represents a lower bound of performance, while the highlighted
teal line traces the models with the highest average scores each year,
culminating with the introduction of models like GPT-4o and Gemini Ultra
that set new benchmarks for language understanding.

- Technical surveys detailing the algorithms and tech-

niques used in modern LLMs.

This comprehensive categorization aids in understanding
how LLMs adapt to specialized vocabularies and regulatory
frameworks across different settings.

Overall, our survey on LLMs serve as a valuable resource
for researchers and practitioners, offering a consolidated view
of the state-of-the-art in LLMs.

IV. COMPARATIVE ANALYSIS OF LLMs
This section provides a comparative analysis of prominent
Language Models using various benchmarks, which assess
the models’ capabilities in language understanding, reason-
ing, and multimodal tasks. These benchmarks are designed
to evaluate different aspects of language comprehension and
cognitive abilities.


#### A. MAJOR BENCHMARKS
Standardized benchmarks are essential for evaluating LLMs’
performance across tasks, offering a means to compare
models and identify their strengths and weaknesses. This
section highlights some of the most widely used benchmarks.

1) MMLU (MASSIVE MULTITASK LANGUAGE
UNDERSTANDING)
The Massive Multitask Language Understanding (MMLU)
benchmark is a collection of 57 tasks that cover a wide
range of subjects from human-level concepts to high school
examinations. This benchmark evaluates the comprehensive

FIGURE 6. Comparative performance visualization of models on the GLUE
benchmark, adjusted to a unified scale with human performance
normalized to a score of 1.0. The summary score represents an aggregate
of nine individual tasks, with an averaged score for tasks containing
multiple metrics. The breakdown across the tasks demonstrates the
relative strengths and weaknesses of each submitted system in various
areas of language understanding.

understanding and generalization power of language models
across diverse topics.
Key Features:
- Coverage: Broad domain coverage from humanities to

STEM.

- Task Types: Multiple choice questions with four
options, requiring not only language understanding but
also domain-specific knowledge.

- Evaluation Metric: Accuracy of predicting the correct

answer among the given choices.

2) SuperGLUE
SuperGLUE is designed as an advanced benchmark to
evaluate and promote improvements in the critical reasoning
and prediction-making abilities of AI models beyond the
GLUE benchmark. It includes a set of more challenging
tasks that require deeper natural language understanding and
broader reasoning capabilities.

Key Features:
- Complexity: Tasks are specifically chosen to be more

difficult and diverse than those in GLUE.

- Task Variety: Includes question answering, entailment,
coreference resolution, and word sense disambiguation,
among others.

188670

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

- Data Sources: Comprises datasets that have been
either newly created or significantly expanded upon for
heightened difficulty and variability.

- Evaluation Metric: Composite score that is calculated
tasks,
based on performance across all constituent
promoting models that achieve balanced capabilities
across a broader array of challenges.

3) HELLASWAG
HellaSwag is a benchmark designed to test a model’s
common sense and ability to complete scenarios using
everyday knowledge. The tasks involve predicting the ending
of descriptions of everyday activities.

Key Features:
- Contexts: Comes

from diverse sources

such as

Wikipedia and instructional videos.

- Task Type: Choose the most plausible continuation

among four provided options.

- Evaluation Metric: Accuracy of predictions.

FIGURE 8. Advancement in accuracy of various LLMs on the AI2
Reasoning Challenge (ARC) aimed at appraising common sense
reasoning. Newer models like GPT-4 and PaLM demonstrate significantly
improved common sense reasoning capabilities. Notably, variations in
model training approaches, such as zero-shot and few-shot learning, are
reflected in differentiated performance levels.

- Evaluation Metric: Accuracy of choosing the correct

entity.

FIGURE 7. Progression of HellaSwag benchmark accuracy scores from
tracks the performance of various LLMs achieving the highest HellaSwag
scores. Notable milestones include the introduction of models like GPT-4
and PaLM 2, which significantly surpass previous models in accuracy,
indicating substantial advancements in AI’s commonsense reasoning and
contextual understanding abilities.

4) ARC (AI2 REASONING CHALLENGE)
ARC presents models with grade-school-level multiple-
choice science questions, testing their ability to understand
text and apply reasoning skills.

Key Features:
- Difficulty Levels: Contains both Easy and Challenge

sets to adapt to different model capabilities.

- Evaluation Metric: Accuracy on correctly answered

questions.

5) WINOGRANDE
WinoGrande is a large-scale dataset of winograd schemas
that are designed to test common sense reasoning within AI
models.

Key Features:
- Scale: One of the largest datasets for commonsense

reasoning.

- Task Type: Sentence completion that requires resolving

ambiguous pronouns.

FIGURE 9. Showcasing the ascent in accuracy of diverse LLMs on the
WinoGrande benchmark. Remarkable progress is seen with the likes of
GPT-4 and the various iterations of the PaLM model, reflecting significant
advancements in the field’s pursuit of nuanced language understanding
and common sense inference capabilities.


#### B. BENCHMARKS FOR MULTIMODAL LLMs
As the field of AI progresses, benchmarks for evaluating
multimodal capabilities of LLMs have become increasingly
relevant. Some notable multimodal benchmarks include:

1) NLVR2 (NATURAL LANGUAGE FOR VISUAL REASONING
FOR REAL)
The NLVR2 benchmark is a challenging dataset designed
for evaluating AI models’ ability in visual reasoning with
natural language. It requires models to determine whether
a given natural language statement accurately describes a
pair of images. Unlike standard object recognition or image
captioning tasks, NLVR2 demands a deeper understanding of
both the visual content and the semantics of the language,
making it a more complex challenge.

Key Features:
- Data Composition: Consists of pairs of

images
accompanied by a textual description. The model’s task
is to verify the truthfulness of the description given the
image pair.

- Reasoning Requirement: The models must interpret
the images in the context of spatial relations, counting,

VOLUME 12, 2024

188671

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

counting, color determination, spatial understanding,
and inferential reasoning based on the image content.
- Answer Formats: The answers may be in various
including single words, numbers, or short

forms,
phrases.

- Performance Metrics: Accuracy is the primary metric,
supplemented by consistency and plausibility scores in
some variations of the benchmark.

- Challenges: The task challenges models to understand
and process visual data in conjunction with textual
information,
requiring a high level of multimodal
integration and reasoning.

The VQA benchmark is crucial for the development of AI
systems that interact with the visual world in a meaningful
and contextually aware manner, a necessity for applications
ranging from assistive technologies to automated content
moderation.

These benchmarks test

the integration of visual and
textual data, crucial for applications requiring a holistic
understanding of multimodal inputs.


#### V. FINE-TUNING TECHNIQUES FOR LLMs
Fine-tuning methods for LLMs are utilized in a variety of
applications including domain specialization, performance
improvement, and bias mitigation. Key approaches to
fine-tuning LLMs, such as Parameter-Efficient Fine-Tuning
(PEFT), are often emphasized due to their diverse applica-
tions and reduced computational demands as compared to
complete model training and these techniques are detailed in
this section.


#### A. LOW-RANK ADAPTATION IN LLMs
Low-Rank Adaptation (LoRA) [130], and specifically Low-
Rank-parametrized Update Matrices, provides an efficient
strategy for fine-tuning pre-trained Transformer-based lan-
guage models. This technique is articulated by the following
update rule:

(cid:49)W = BA
(3)
where W0 ∈ Rd×k is the original weight matrix, and (cid:49)W is
the low-rank update represented by matrices B ∈ Rd×r and
A ∈ Rr×k , with the rank r ≪ min(d, k). During adaptation,
W0 remains unchanged, and only B and A are trained.

LoRA posits a reduction in the number of trainable
parameters, significantly reducing computational overhead.
It also generalizes full fine-tuning, theoretically allowing a
model to approximate the expressiveness of full-rank weight
matrices by selecting an appropriate r. For new tasks, one
can quickly adapt the base model W0 by adjusting BA, thus
avoiding additional inference latency.

Furthermore, LoRA introduces a scaling parameter α in the

adaptation step:

(cid:49)Wx = α

(cid:49)Wx
r

(4)

VOLUME 12, 2024

FIGURE 10. This graph depicts the accuracy trend of models on the NLVR2
benchmark. The multi-modal LLMs showcase rapid improvements in
visual and linguistic reasoning capabilities. Notable performers such as
BEiT-3 and X2-VLM (L) represent the cutting edge of multi-modal LLMs,
indicating their superior proficiency in interpreting complex
visual-language tasks.

and comparison, making this benchmark particularly
suited for evaluating multimodal comprehension.

- Performance Metrics: The main metric is accuracy,
indicating the model’s ability to correctly validate the
statement against the visuals.

- Challenges: Involves disambiguating ambiguous lan-
guage, understanding complex statements, and a deep
integration of visual and textual information.

Models successful on NLVR2 must not only integrate
visual and textual information but also accurately capture the
subtleties of language that relate to the visual world.

2) VISUAL QUESTION ANSWERING (VQA) BENCHMARK
The Visual Question Answering (VQA) benchmark stands
as a measure of an AI system’s ability to answer questions
pertaining to given images. This multimodal benchmark com-
bines natural language processing with image recognition to
test a model’s comprehensive understanding of visual content
as it relates to conceptual and factual queries.

FIGURE 11. Accuracy performance graph for various AI models on the
VQA, illustrating the evolution of AI in comprehending and answering
visually grounded questions. The graph underscores the significant
strides made in multimodal AI, with models like BEiT-3 showing
remarkable precision in visual-textual understanding.

Key Features:
- Task Composition: Involves an open-ended task where
a model is presented with an image and a related
question in natural language. The model must provide
an accurate answer to the question, reflecting a correct
understanding of the visual context.

- Diversity of Questions: The questions are designed to
cover a wide array of types, including object detection,

188672

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 5. Parameter efficient fine-tuning methods for pre-trained language models.

which helps maintain stability in the learning rate when
varying the rank r, reducing the necessity for hyper-
parameter retuning. This parameter-efficient method for
adapting LLMs presents an avenue for tailoring models to
specialized domains or tasks without forfeiting their original
capabilities.


#### B. CONTINUAL LEARNING
Continual Learning (CL) with PEFT for LLMs is an
approach that focuses on adapting a model to new tasks
over time while avoiding catastrophic forgetting of previously
learned information. It leverages PEFT methods to introduce
minimal, task-specific updates to the model’s parameters.
Techniques such as AdapterCL use residual adapters to
encapsulate new knowledge for each task. These strategies
help maintain the model’s performance across a sequence
of tasks by incorporating mechanisms like entropy-based
classifiers for adapter selection, and by employing strategies
to ensure knowledge transfer between tasks. The goal is to
achieve a balance where the model continually accumulates
and refines knowledge without substantial
loss of prior
learning.


#### C. CONTEXT WINDOW EXTENSION
Context Window Extension in PEFT refers to the adaptation
of LLMs to process input sequences that exceed their
initially defined context lengths. Through PEFT, such as
LongLoRA [145], LLMs can be efficiently fine-tuned to
extend their context windows, allowing them to handle
longer input sequences without a significant increase in
computational requirements. This is particularly useful for
is
tasks where the ability to maintain longer context
crucial for performance. LongLoRA and similar techniques
modify attention mechanisms and introduce sparse attention
patterns to manage longer sequences, enhancing the model’s
applicability to real-world scenarios with lengthy textual
data.


#### D. VISUAL INSTRUCTION TUNING
One notable PEFT technique is visual instruction tuning,
where LLMs, traditionally text-based, are adapted to handle
visual inputs, enabling them to perform tasks like image
captioning and visual question answering. The integration
of visual and language processing in LLMs through visual
instruction tuning represents a significant leap in multimodal
AI capabilities. The process involves using LLMs like
GPT-4 to generate language-image instruction-following
data, which is then used to fine-tune a model capable of
understanding and interacting with both textual and visual
inputs. The resulting model, dubbed LLaVA (Large Language
and Vision Assistant) [157], showcases impressive multi-
modal conversational abilities and has set new benchmarks in
accuracy for tasks such as Science QA [158]. This approach
underscores the potential of LLMs in general-purpose
visual and language understanding tasks. Alternatively, PEFT
approaches such as adapter modules are employed to refine
models like VL-BART [159] for image-text
tasks more
efficiently.

These methods represent only a fraction of the PEFT
techniques used to adapt LLMs for specialized applications,
highlighting the field’s adaptability and ongoing innovation.
Table 5 offers an in-depth categorization of these PEFT
methods for LLMs, showcasing their variety and application
potential in NLP.

VI. CUTTING EDGE LLMs
In the following section, we provide an overview of large
language models (LLMs) based on their architecture and
the series they belong to, as of the date of this survey.
This will offer a comprehensive understanding of the various
LLMs and their respective design frameworks. Figure 12
illustrates the evolutionary tree showing the progression of
LLMs across different architectures. Figure 13 presents a plot
of parameter counts for prominent LLMs, highlighting the
trend of increasing parameter sizes over the years. Similarly,

VOLUME 12, 2024

188673

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

FIGURE 12. An evolutionary tree illustrating the progression of mainstream LLMs. Models are categorized based on their architectural construct:
encoder-only, decoder-only, and encoder-decoder. Models stemming from the same lineage or released by identical entities are interconnected with solid
lines. Independent research contributions are demarcated by purple lines.

Figure 14 displays the average scores from the Open-LLM
Leaderboard for various benchmarks,
including MMLU,
ARC, HellaSwag, and TruthfulQA.


#### A. AUTO-ENCODING MODELS
Auto-encoding models, often referred to as ‘encoder-only
models,’ utilize solely the encoder component of the Trans-
former architecture. Their primary function is to map input
data from a higher-dimensional space to a lower-dimensional
vector space, effectively capturing and integrating contextual
information into the data representation. These models
commonly employ training strategies like masked language

modeling and bi-directional
training. The inception of
auto-encoding models can be traced back to 2018 with
the release of BERT, a pioneering model that harnessed
the encoder-only architecture. This innovation significantly
augmented the capabilities of natural language understanding
models, enabling them to tackle a diverse range of NLU tasks,
including reading comprehension, cloze tasks, and question
answering.

1) BERT
BERT [9] stands out as one of the pioneering pre-trained
models employing an auto-encoding architecture. Its training

188674

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

FIGURE 13. Developments in LLMs and their parameter count reflecting quantitative increase in model sizes across time. The models are
color coded based on their research organization.

FIGURE 14. Open-LLM Leader-board benchmark competing various state-of-the-art LLMs across diverse benchmarks, encompassing TruthfulQA, MMLU,
ARC, and HellaSwag for a comprehensive evaluation.

strategy primarily hinges on two tasks. The first, Masked
Language Modeling (MLM), involves randomly masking
tokens in the input data during the preprocessing phase. The
majority of these masked tokens are hidden, prompting the
model to predict them during training. However, a fraction
of these tokens might be substituted with random ones.
Occasionally, these replacements are erroneously embedded,
compelling the model to forecast the original tokens using
cross-entropy loss. It’s worth noting that some of these tokens
remain unaltered. This methodology equips BERT with the
capability to anticipate contextual information at the token
level.

In addition to MLM, BERT introduced the Next Sentence
Prediction (NSP) task to capture information at the sentence
level. In the NSP task, the model determines whether an input
sentence sequentially follows another within the broader
context.

For effective NSP task training, both positive and negative
samples are used to enhance the model’s robustness. BERT
also incorporates a unique tokenization system, marking the
start of a sentence with [CLS], the end with [SEP], and using
the [MASK] token to obscure certain tokens during training.
This approach allows BERT to generate contextually accurate
and coherent language representations.

2) VARIENTS OF BERT
Several BERT variants have emerged to cater to diverse
tasks. BERT-wwm [160] employs a whole-word masking
(WWM) approach for the MLM task. Contrary to the
original BERT’s subword-based tokenization, BERT-wwm
applies masking to entire words, mitigating issues associated
with subwords. BERT-wwm-ext [161] extends BERT-wwm
by training on more extensive datasets over increased
iterations. SpanBERT [162] offers an expanded MLM version

VOLUME 12, 2024

188675

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

in their study,

for
that employs static masks in a consistent manner
each input sample, RoBERTa’s mask selection is dynamic.
this sequence undergoes
For any given input sequence,
multiple masking processes;
the authors
adopted a hyper-parameter value of 10. During each masking
iteration, a unique set of tokens is selected to be masked,
eschewing the repetitive use of static masks. Addition-
ally, RoBERTa’s research evaluated various sentence pair
configurations for the NSP tasks. Findings suggested that
certain sentence-pair configurations adversely impacted the
fine-tuning of downstream tasks. Consequently, to maintain
document integrity during training, RoBERTa omits the NSP
task. To optimize performance, RoBERTa employs larger
batch sizes, an expansive training corpus, and deeper training
iterations.

A notable variant of RoBERTa,

termed RoBERTa-
wwm [172], aims to fine-tune RoBERTa for the Chinese
corpus. Unique to this adaptation, tokenization and masking
occur at the character, rather than word level.

FIGURE 17. Changed version of NSP in RoBERTA, different from BERT
which used fixed two sentences, RoBERTA would have a fixed length of
the whole input sequences and give the NSP input until this fixed length
was reached.

4) ERNIE
ERNIE [8] employs a multi-level masking strategy distinct
from BERT to optimize its performance for Chinese
languages. This strategy encompasses basic-level masking,
which masks out characters or words similar to BERT’s
MLM approach; phrase-level, where entire phrases are
masked rather
than individual words; and entity-level,
which targets and masks entire entities within the input
sequence. Additionally, ERNIE introduces the Dialogue
Language Model (DLM) technique. It leverages both genuine
dialogues from online forums and artificially generated
ones. Within DLM, the model’s training loss incorporates
its capability to differentiate between authentic and fake
dialogues. Like many auto-encoding model variants, ERNIE
utilizes an expansive training dataset, which includes content
from Chinese Wikipedia and news articles from Baidu.
Architecturally, ERNIE is built upon the Transformer-XL
framework. Traditional multi-task learning, which trains
tasks sequentially, often grapples with efficiency and ‘‘forget-
ting’’ challenges. To address this, ERNIE 2.0 [173] introduces
continual multi-task learning. This method deviates from

FIGURE 15. Masked-Language Modeling used by BERT, in this case, the
word ‘‘how’’ and ‘‘weather’’ were masked out for BERT to perform
prediction tasks.

where masked tokens extend to neighboring ones based
on a geometric distribution with predefined randomness.
SpanBERT omits the NSP task. Efficiency-enhancing adap-
tations of BERT have emerged. DistillBERT [163] leverages
knowledge distillation to derive a streamlined BERT model
with half the original’s layers. It adopts RoBERTa’s [164]
optimization techniques, featuring dynamic masking and
enlarged batch sizes, while discarding the NSP task. Tiny-
BERT [165] employs distillation techniques but optimizes
BERT’s efficiency further. VisualBERT [166] incorporates
multimodal support into BERT, pairing it with a convolu-
tional neural network (CNN) to extract features from images.
Unlike the original BERT, VisualBERT’s token predictions
rely on textual context and image-derived information.
Lastly, MacBERT [167] introduces synonyms (sourced from
word2vec) as MLM replacements and integrates both WWM
and n-gram masking. This aims to mirror the objectives of
BEiT [168], BEiT v2 [169], and BEiT v3 [170], which fuse a
BERT-based encoder with dVAE [171].

FIGURE 16. Next Sentence Prediction used by BERT, the model was asked
to justify if the sequence ‘‘is it raining’’ should be the next sentence of
‘‘how is the weather today’’.

3) RoBERTa
Several models, while distinct
from BERT, owe their
genesis to the original BERT framework. One such is
RoBERTa [164], designed to enhance the robustness of
BERT’s training process, primarily through the introduction
of a dynamic mask strategy. Contrary to BERT’s MLM

188676

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

the conventional sequential approach by integrating new
tasks directly into the existing task set, facilitating combined
training. ERNIE 2.0 also proposes three types of aware
pre-training tasks. The word-aware task is an enhanced
version of ERNIE’s multi-level masking that incorporates
token-documentation relation tasks. It predicts a token’s
likelihood of appearing in segments and its case (uppercase
or lowercase). The structure-aware task involves the permuta-
tion of sentences into sub-sentences, predicting their original
order and establishing if sentences are adjacent. Lastly,
the semantic-aware task determines relationships between
sentences, deducing their cohesive structure and relationships
between queries and titles at the information relevance level.
ERNIE 3.0 [174] introduces both universal representation
and task-specific representation. The former is utilized for
natural language understanding tasks, while the latter aids
in natural language generation tasks to extract contextual
semantic features. A novel knowledge-aware pre-training
task is also added, which uses universal knowledge-text
prediction to discern the relationships between various
knowledge points within the training set. Keeping pace with
modern large language models, ERNIE 3.0 expanded its
parameters to 10B, supported by a larger dataset. ERNIE has
a multimodal variant, ERNIE-VilG [175]. It trains on image
datasets through three foundational tasks: object prediction,
where associated tokens in the text are masked in relation
to image data; attribute prediction, masking attributes of
randomly selected objects; and relationship prediction, which
targets and predicts the relationship between two objects
in an image. ERNIE-Vil 2.0 [176] introduces multi-view
contrastive learning. This approach trains image-text pairs
based on various pairings, differing from ERNIE-Vil’s
single image-text pairing strategy, to enhance cross-modality
representation.

FIGURE 18. ERNIE would mask out the whole related word of the chosen
masked word to perform predict, this strategy could improve the
capability of the model to infer the relationship between tokens.

5) ALBERT
ALBERT [9] was developed to optimize training as model
parameters grew. It observed that in earlier models like BERT,
XLNet, and RoBERTa, the size of embedding layers was
equivalent to that of hidden layers. These embedding layers
focused on acquiring context-independent representations,
while the hidden layers concentrated on context-dependent
representations. Given that the models typically experienced
greater enhancements from context-dependent information,
it stood to reason that the dimensions of hidden layers

should surpass those of embedding layers. To address this,
ALBERT introduced the concept of factorized embedding
Instead of directly transitioning from
parameterization.
one-hot encoding to vector embedding,
this technique
employs one-hot embeddings to first map to a relatively
smaller embedding layer. Subsequently, this is mapped to
considerably larger hidden layers. This separation ensures
that the model doesn’t heavily rely on the direct mapping
of the vector embedding from the one-hot encoding, which
can be restrictive given the differing roles of embeddings
and hidden layers. Moreover, ALBERT shared parameters
between the feed-forward network and attention layers,
leading to further efficiency in training. In a departure
from models like RoBERTa which eliminated the NSP task
outright, ALBERT evolved the task into Sentence Order
Prediction (SOP). This modification expanded upon the NSP
concept by transitioning from predicting the subsequent
sentence to deducing the order of sentences, addressing the
criticism that NSP was rudimentary for the model’s potential.

FIGURE 19. ALBERT used sentence-order prediction instead of NSP,
during the training, the negative sample were rotated and the model
should discriminate if the sentance order was correct.

in ELECTRA,

6) ELECTRA
ELECTRA [177] was introduced with the intention of effec-
tively training auto-encoding models on smaller-scale cor-
pora. Unlike traditional Masked Language Models (MLM)
the
that only predict masked-out words,
objective is shifted towards predicting all words in the input
sentence. Different from the previous models which used
different tasks such as masks to enhance the capability of
the model during the pre-training process, the key innovation
in ELECTRA is to take the feature of generative adversarial
network (GAN) [178] which introduced a two-part system:
a generator and a discriminator. The generator, akin to
the traditional MLM, randomly masks certain tokens and
then attempts to predict them. The discriminator’s role is
to examine each token from the generator’s output and
determine if it is the actual token from the original input or if
it’s the token produced by the generator.

By employing this adversarial

the
model can more effectively understand contextual informa-
tion. An important detail is that the token embeddings’
parameters are shared between the generator and the
discriminator. This shared parameterization not only reduces

training technique,

VOLUME 12, 2024

188677

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

tokens are segmented
presents challenges. Specifically,
into fixed-length sub-sequences. Post-encoding, the model
lacks a mechanism to discern relationships between these
segments. This limitation hinders the flow of contextual
information, as the model cannot ascertain how the fragments
relate within the entire sequence,
leading to context
fragmentation. Transformer-XL [180] is another family of
auto-encoding model
that addresses this by introducing
segment-level recurrence coupled with state reuse. This
method integrates a memory layer to retain information
from preceding sequences, facilitating the establishment of
relationships between sub-sequences during encoding. Such
a mechanism not only enables the model to understand
semantic connections between segments but also encodes
relationships in longer sequences. Moreover, Transformer-
XL employs relative positional encoding, replacing absolute
positional encoding to mitigate confusion between the
current sub-sequence and the entire sequence. XLNet [181]
adopts the Transformer-XL architecture to rectify the MLM
drawbacks found in BERT. The authors postulated that the
introduction of masks might disrupt contextual information
construction. To counteract this, XLNet introduces a suite
of techniques. One key method is the permutation language
model, which factorizes input sequences in varying orders.
This replaces BERT’s bi-directional training, enabling the
model to learn contextual information bidirectionally by
alternating factorization permutation orders while sharing
parameters. To facilitate factorization permutation, XLNet
introduces a two-stream self-attention mechanism that
employs two hidden states instead of one, alleviating issues
induced by permutation. Additionally, in lieu of complete
predictions, XLNet employs partial prediction, akin to
BERT’s sub-wording,
to predict only a token segment,
enhancing the model’s convergence speed.


#### B. AUTO-REGRESSIVE MODELS
Auto-regressive models are often referred to as ‘‘decoder-
only’’ models. In contrast, auto-encoding models compute
attention bi-directionally, enhancing the model’s capacity
for natural language understanding by perceiving the entire
context. While self-attention computes attention scores
globally, assessing the correlation between each token in
a sequence, auto-regressive models utilize uni-directional
attention. This means that the current generation is dependent
solely on previously generated sequences; tokens following
the current one are masked out. Compared to auto-encoding
models, this architecture excels in generation tasks. The
uni-directional attention offers superior performance in
handling long sequences, which is one of the reasons
this architecture is widely adopted in contemporary large
language models.

FIGURE 20. ELECTRA used replaced token detection instead of MLM.
In this case, the word ‘‘how’’ and ‘‘weather’’ were masked and passed the
masked sentence into the generator, the generator produced the
predicted masked word ‘‘why’’ and ‘‘weather’’ and used the discriminator
to discriminate if the generated word matched the original word, in this
case, the word ‘‘why’’ was discriminated as ‘‘replaced’’ and the word
‘‘weather’’ was regarded as the original correct word.

the model’s overall parameters but also ensures consistent
representation between the two parts, enabling them to better
work in tandem. The result is a model that can be trained
efficiently on smaller datasets, yet achieve competitive, if not
superior, performance compared to its counterparts trained on
much larger corpora.

7) DeBERTa
In conventional auto-encoding models, the Masked Language
Model (MLM) technique is typically not employed during the
fine-tuning stage. This omission often leads to discrepancies
between the pre-training accuracy and the fine-tuning accu-
racy. Furthermore, the attention score is somewhat influenced
by the token positions. To address the inconsistency in accu-
racy and the distribution of token positions, DeBERTa [179]
was introduced. This model incorporates a novel attention
mechanism termed ‘‘disentangled attention,’’ which factors in
the relative positional information of tokens when computing
the attention score. In addition, DeBERTa employs an
enhanced mask decoder
replaces the conventional
that
softmax function with an Extended Mask Decoder (EMD)
and adds several transformer layers prior to the original
softmax function. Within the Enhanced Mask Decoder,
10% of the relative positional embedding information is
substituted with absolute positional embedding, bolstering
the attention across diverse positional information.

8) TRANSFORMER-XL
Despite of the wide usage of BERT and its derived models,
handling long sequences in the standard transformer model

1) GPT
GPT [2] was one of the early auto-regressive models
released in 2018, contemporaneously with BERT. It was a

188678

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

pioneer in introducing auto-regression techniques. Before
GPT’s inception, language model training largely relied on
large corpora, often manually or automatically annotated,
which were costly to assemble. Many of these earlier
limiting their zero-shot
models were domain-specific,
capabilities. GPT uniquely adopted unsupervised learning,
training generatively on unlabeled datasets and subsequently
fine-tuning for specific tasks. It incorporated strategies such
as natural language inference to assess relationships between
sentences, question answering and commonsense reasoning
for semantic comprehension, semantic similarity evaluations,
and classification tasks. Despite utilizing a relatively smaller
dataset,
it employed a 12-layer
transformer encoder.

the BookCorpus [182],

GPT-2 [183], a successor to GPT, embraced multi-task
learning. Building on GPT’s foundation, it postulated that
with sufficiently large data and model size, supervised tasks
could be implicitly learned, as indicated in decaNLP [184].
Consequently, GPT-2 leveraged WebText, a dataset vastly
larger than GPT’s BookCorpus, comprising over 8 million
websites from Reddit, exceeding 40GB. The architecture was
also expanded to 48 layers, enlarging the parameter count to
nearly 13 times that of GPT.

GPT-3 [185] continued GPT-2’s ethos of expanding dataset
size and model depth. It adopted an in-context learning
training strategy, aiding in faster convergence through the
model-agnostic meta-learning method [186]. The distinct
fine-tuning phase, present post-pretraining in GPT and
GPT-2, was eschewed in GPT-3 due to the reasons mentioned
and the enormity of its dataset. GPT-3 sourced data from
five diverse repositories, including Common Crawl [187],
WebText 2, two iterations of BookCorpus, and Wikipedia,
aggregating over 45TB. The model architecture doubled
GPT-2’s, employing 96 layers of
transformer decoder,
culminating in a staggering 175B parameters, more than
100 times that of GPT-2.

InstructGPT [188] melded reinforcement learning with
human feedback into GPT-3’s fine-tuning process. Using the
SFT dataset, it established a reward model reflecting human
feedback on the model’s output through proximal policy
optimization, enhancing the model’s human-like behavior.
Drawing from InstructGPT’s technology, OpenAI unveiled
ChatGPT [189], a fine-tuned iteration of GPT-3, colloquially
termed GPT-3.5.

GPT-4’s [190] technical report, while not fully revealing
its strategies, highlights some salient features. GPT-4 can
inputs, producing textual
handle both image and text
outputs, classifying it as a genuine MLLM. This flexibility
broadens GPT-4’s task repertoire, especially for multimodal
requirements. While ChatGPT, based on GPT-3.5, supports
up to 4096 tokens (roughly 3000 English words), GPT-4
manages a remarkable 32767 tokens, or about 25000 words,
enabling the processing of more extended text sequences
with heightened accuracy. GPT-4 emphasizes security,
addressing challenges like Adversarial Usage, Unwanted
Content, and Privacy Concerns through strategies like RLHF

FIGURE 21. The comparison between GPT series models.

(reinforcement learning with human feedback), real-world
use case simulations, and an adversarial testing program.
Additionally, GPT-4 allows users to use precise prompts,
granting more control over the model’s behavior.

Several models have been derived from or inspired
by the GPT series. GPT-Neo [191] seeks to offer an
open-sourced version of GPT-3 for
local deployment.
GPT-GNN [192] integrates pre-training on graph neural
networks to understand node interrelations. GPT-J [193] is
GPT-inspired, grounded on the Mesh-transformer-JAX [194].
GPT-NeoX [195] succeeds GPT-Neo, integrating parallel
computing from GPT-J using the Deepspeed [196] frame-
work. DialoGPT [197], an extension of GPT-2, aims to refine
text generation using maximum mutual information to elevate
hypothesis ranking.

2) PATHWAYS AND PaLM
The ‘‘Pathways’’ architecture, as introduced by Google [198],
represents a significant shift in AI design. Instead of the
traditional method of constructing distinct models for indi-
vidual tasks, Pathways proposes a single AI system capable
of generalizing over thousands, if not millions, of tasks. This
versatility is attributed to the ‘‘mixture-of-experts’’ (MoE)
concept. By constructing a single model that can be trained on
extensive datasets encompassing both text and code, different
tasks or inputs are managed using a gate function, directed by
the respective experts. A notable feature of models built using
the Pathways architecture is their ability to be fine-tuned
for specific tasks through few-shot learning. This approach
empowers the model to master a new task using only a
handful of examples, ensuring efficiency, versatility, and
precision in its applications. PaLM [199] is the first language
model trained by Pathways architecture which is a model
contains up to 540B number of parameters due to the sparsity
architecture of Pathways. PaLM used a variant version of

VOLUME 12, 2024

188679

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

traditional transformer decoder which made the modification
below:

1) used SwiGLU [200] activation function
2) used multi-query attention, sharing all parameters
between all heads of multi-head attention to boost the
efficiency of decoding

3) put the feed forward network in parallel with attention

layers

4) used RoPE [201] positional embedding
5) Remove all bias in the neural network
6) sharing the embedding among the input and output
The ‘‘Pathways’’ architecture’s utilization of few-shot
learning, as detailed in PaLM, yielded state-of-the-art
outcomes closely paralleling human performance across
four tasks. Moreover, the introduction of the BIG-bench,
encompassing 150 tasks, further highlighted its prowess,
especially in comparison to models like GPT-3.

The Embodied Pathways Language Model, or PaLM-
E [202], is an evolution of the preceding PaLM. It dis-
tinguishes itself as the premier Large Language Model
(LLM) developed using Google’s Pathways architecture. This
architecture was crafted to facilitate sparse activations across
multimodal and multi-task scenarios, implying that for a
distinct task, only a section of the model activates, curtailing
computational
intricacy. PaLM-E, much like Microsoft’s
KOSMOS-1, is adept at deciphering both natural language
and imagery, and boasts potential applications in robotics
for accomplishing embodied tasks. Training for this model
is conducted on the expansive GEM dataset, encompassing
both textual and visual data sources like ImageNet [203],
COCO [204], and Visual Genome [205]. PaLM-E integrates
two primary components: the language pathway, rooted in
the Transformer-XL framework, and the visual pathway,
modeled after the Vision Transformer (ViT) framework.
A fusion module bridges these pathways, enabling seamless
integration of both modalities. Its efficacy is demonstrated
through exceptional performances across a gamut of tasks
such as image captioning, visual question answering, and
embodied navigation. Architecturally, PaLM-E synergizes
two distinct models: the PaLM, which serves as a textual
decoder, and the ViT 22B [206], a dedicated visual trans-
former. The PaLM delivers linguistic processing proficiency,
while the ViT 22B specializes in image processing. The
default model amalgamates a 540B PaLM model and a
22B ViT model, cumulating to a massive 562B parameters.
In terms of training data, PaLM-E benefits from a staggering
780B tokens, derived from diverse sources like social
media, web content, Wikipedia, and GitHub. Meanwhile,
the ViT 22B module trains on the JFT dataset [207],
encompassing roughly 4B semi-automatically annotated
images. The model’s input representation strategy mirrors
KOSMOS-1 [208], where visual or robotic-related inputs
receive specific tags, and distinct encoding techniques
interpret the content within these tags. Directly, textual data is
channeled into the language model. Additionally, the Minerva
model [209], fine-tuned from a vast 118G dataset teeming

with scientific publications and mathematical expressions,
is predicated on PaLM and targets challenges in scientific
and mathematical domains. Lastly, PaLi [210], another
PaLM derivative, tackles text-vision quandaries using an
image-and-text to text-only paradigm, incorporating models
like mT5-XXL [211], ViT-G [212], and ViT-e [213].

FIGURE 22. The relationship between models under PaLM family by
Google.

FIGURE 23. Architecture of PaLM-E, first the visual information would go
pass the ViT, and the scene would be embedded into vector format, then
all the token embedding would go through a PaLM model to generate the
response text, that response text would then be transferred to the control
signal.

The PaLM-2 model [214] augments the capabilities of
its predecessor, the PaLM, with enhanced performance in
mathematics, coding, inference, and multi-language tasks.
Leveraging JAX and TPU technology, the primary objective
the PaLM
of PaLM-2 is to amplify the efficacy of
model while simultaneously utilizing fewer parameters.
In contrast to PaLM-E, PaLM-2 does not offer multi-modal
support. The PaLM-2 architecture encompasses four variants
differentiated by parameter size: Gecko, Otter, Bison, and
Unicorn. These versions ensure versatility, catering to varied
deployment needs across diverse platforms. Notably, the
Gecko model, being the most compact, is optimized for
deployment on mobile devices. In the realm of medical
question-answering (QA),
the Med-PaLM 2 [215] was
introduced. This specialized version, derived from PaLM-2,
employs fine-tuning techniques centered on the ensemble
refinement approach applied to medical datasets. Impres-
sively, it registered an accuracy rate of 86.5% on the MedQA

188680

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

benchmark [216], marking a significant improvement from
its antecedent, the Med-PaLM [217].

3) MICROSOFT KOSMOS-1
The KOSMOS-1 model [208] is underpinned by the magneto
transformer [218], a derivative of the original transformer
architecture. The primary distinction between the two
lies in the magneto transformer’s integration of a layer
normalization between its linear layer and the activation
function, a modification that enhances training stability
and scalability. Specifically designed with 24 decoder
layers, each having 2048 dimensions, 8192 hidden size,
and 32 attention heads, KOSMOS-1 boasts approximately
1.6 billion parameters.

Rather

than directly processing images, KOSMOS-
1 expedites training by harnessing the CLIP ViT-L/14
to capture image features with 1,024 dimen-
model
sions. Moreover, it employs the XPOS technique, leverag-
ing length-extrapolation to reconcile disparities in length
between training tokens and predicted tokens. These inno-
vations equip KOSMOS-1 with the versatility to excel in a
range of tasks, such as image captioning and visual question
answering, underscoring its prowess in multimodal learning.
KOSMOS-1 is enriched by three primary datasets. The
text corpus includes The Pile, a vast English text dataset
resources like Common
tailored for LLMs, and other
Crawl, CC-Stories, and RealNews. Image-caption pairings
are sourced from datasets such as English LAION-2B,
LAION-400M, COYO-700M, and Conceptual Captions, all
of which were acquired through web crawling. Additionally,
there’s an interleaved image-text compilation featuring
combined image and text fragments. This data is culled
from an initial collection of 2 billion web pages, which was
subsequently condensed to 71 million pages in the finalized
dataset.

For data preprocessing, text sequences were designated
with the <s> tag, while images received the <image> label.
Notably, while KOSMOS-1 also extends support to audio
sequences, the associated paper lacks comprehensive details
on this aspect, hinting at its potential developmental stage.

Conclusively, KOSMOS-1 signifies a monumental stride
in the evolution of multimodal large language models, poised
to have transformative impacts on both natural language
processing and computer vision research arenas.

4) MEGATRON
Nvidia Megatron [219] is a framework proposed by Nvidia to
solve the parallel computing of the LLM training, it mainly
used two strategies to boost the model training and relief the
shortage of VRAM during the training process. Inter-layer
parallel, also known as tensor parallel, aimed to divide a
single model into several layers and deploy each layer into
separate devices, while intra-layer parallel, also known as
tensor parallel, divided a single model into multiple layers
to deploy on different devices. The final output would be

concatenated from these model segments after processing
directly. Data parallel, divides the whole dataset into different
devices while each device still holds a full copy of the
model to boost the training process of the model. Megatron
LM [220] is a LLM trained with Megatron framework with
8.3B parameters and trained distributively on multi-GPU
with both tensor parallel and data parallel strategies. While
its successor, Megatron LM 2 [221], introduced a strategy
called PTD-P which combined all of the tensor parallel,
pipeline parallel and data parallel to train the model which
it claimed,
is able to train a model over 1T size with
IO 502 PTFLOG/S. Megatron LM 3 [222] introduced
sequence parallel which divide the non-tensor part of the
model along the sequence dimensions and also introduced a
reduce-scatter operation which reduce the VRAM required
for the activation function. Turing NLG [223] was an early
LLM released by Microsoft which aimed to solve the similar
parallel computing problem as Megatron models, which used
DeepSpeed [196] and ZeRO [224] to boost the training based
on distributed computing which is a breakthrough of both
hardware and software with reduced training time around
2/3. Turing NLG contains 78 layers of transformer decoder
and 170B parameter which is the largest model when it
was released following by Megatron LM. ChatGPT Nvidia’s
Megatron [219] is a framework specifically designed to
address the challenges associated with the parallel computing
of large language model (LLM) training. The architecture
primarily incorporates two strategies to expedite model
training and alleviate the constraints of VRAM during the
training phase. Firstly, the intra-layer parallelism, also known
as tensor parallelism, partitions the layers of a single model
into fragments that are then distributed across different
devices. Once these individual segments process the data,
their outputs are concatenated to produce the final result.
In contrast, inter-layer parallelism involves segmenting a
model into distinct layers, with each layer being allocated to
a separate device. Another strategy, data parallelism, involves
distributing the dataset across multiple devices, but each
device retains a full copy of the model, thereby accelerating
the model’s training process.

Megatron LM [220], a large language model nurtured
using the Megatron framework, boasts 8.3B parameters.
The model is trained distributively across multiple GPUs,
leveraging both tensor parallelism and data parallelism. Its
successor, Megatron LM 2 [221], integrated a method termed
PTD-P, which synergistically combines tensor parallelism,
pipeline parallelism, and data parallelism. This integrated
approach empowers the framework to train models exceeding
1T in size, achieving an impressive IO of 502 PTFLOG/S.
Subsequently, Megatron LM 3 [222] incorporated sequence
parallelism, which segments the non-tensor components of
the model along the sequence dimensions. This edition
also introduced a ‘‘reduce-scatter’’ operation, significantly
diminishing the VRAM demands of the activation function.
On a parallel trajectory, Microsoft’s Turing NLG [223]
emerged as an early contender in the LLM space, targeting

VOLUME 12, 2024

188681

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

FIGURE 24. Structure of the foundation transformer used in KOSMOS-1.

TABLE 6. Training dataset of Megatron-Turing NLG.

FIGURE 25. Left: Post Layer Norm, the LN layers were applied after the
attention and activation function; Middle: Pre Layer Norm, the LN layers
were applied before the attention and activation function; Right: Sub
Layer Norm proposed by Microsoft, which was the transformer
architecture used in KOSMOS-1, in addition to the Pre Layer Norm,
an extra layer norm was applied inside the decoder.

parallel computing challenges akin to those addressed by the
Megatron models. Turing NLG integrates the capabilities of
DeepSpeed [196] and ZeRO [224], pioneering advancements
in both hardware and software realms. This integration
reduction in training
has culminated in a substantial
time, approximately by two-thirds. Architecturally, Turing
NLG comprises 78 transformer decoder layers and 170B
parameters. At the time of its release, it held the title of
the largest model in its category, subsequently succeeded by
Megatron LM.

Megatron-Tuiring NLG [225] is the successor of Turing
NLG in combination with the Megatron architecture which
contains over 530B of the parameters over the Turing NLG.
It was trained based on 280 Nvidia A100 GPUs and contains

105 layers of transformer deocder. The training data was from
a variety of sources shown below:

There are other models that leverage the power of parallel
computing from Megatron architecture, BioMegatron [226]
used Megatron to train a LLM based with biomedical domain
specific and Megatron-CNTRL [227] which proposed a
framework of LLM that has controllability output by keyword
prediction, knowledge retrieval, contextual knowledge rank
and conditional text generation.

5) LLaMA
The LLaMA model was introduced by Meta in 2022 and
made open-source. Its primary aim was to enhance model
capabilities while maintaining a smaller size suitable for local
deployment [10]. LLaMA employed three distinct strategies.
Firstly, it adopted the RMS Pre-Norm [228] in the transformer

188682

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

layer normalization.
decoder, replacing the conventional
This modification eliminated the re-centering operation,
retaining only the re-scaling operation, thereby facilitating
smoother gradient descent. Additionally, LLaMA utilized
methods similar to PaLM, incorporating both SwiGLU [200]
and RoPE positional embedding. The LLaMA model suite
consists of four variants: 7B, 13B, 33B, and 65B parameters.
Despite having significantly fewer parameters than GPT-3,
Meta suggested that LLaMA could be locally deployed.
However, the performance of LLaMA, with its reduced
parameter count, did not significantly surpass that of GPT-3.
Following LLaMA, a series of derivative models emerged.
Alpaca [229] sought to fine-tune the original LLaMA model
using over 52,000 fine-tuning data samples extracted from
the text-davinci-003 model [230] developed by OpenAI for
GPT-3. The resulting Alpaca model achieved performance
comparable to text-davinci-003 but at a reduced cost.
Subsequently, Guanaco [231] was introduced as Alpaca’s
successor, integrating block-wise k-bit quantization. This fea-
ture marked the LLaMA series’ first foray into quantization
methods, compressing the model by converting the original
FP32 data format to a more compact int8. Additionally,
Guanaco employed low-rank adapters (LoRA) to keep model
parameters constant, only adjusting the optimizer with a
smaller dataset batch. This approach further reduced the
fine-tuning costs. Alpaca-LoRA [232] combined Alpaca
with the LoRA technology. Vicuna [233], with its 13B
parameters, represented a fine-tuned LLaMA model derived
from dialogue datasets from ShareGPT [234], achieving
approximately 90% of ChatGPT’s performance.

Distinct from earlier iterations, which primarily fine-tuned
the original LLaMA, Dolly [235] employed GPT-J-6B [193]
to emphasize the importance of fine-tuning over base-
line models. Dolly v2 [236] transitioned to using the
databricks-dolly-15k dataset and replaced GPT-J-6B with
Pythia [237], making the model more accessible for business
applications. Koala [238], applied to FastChat [239], adopted
approaches similar to Vicuna, drawing from dialogue data
for its fine-tuning. LLaMA 2 [10], a direct successor
of LLaMA, presented three versions with 7B, 13B, and
70B parameters. It increased the original LLaMA training
dataset by approximately 40%. LLaMA 2 introduced the
grouped-query attention (GQA) strategy, which grouped
attention calculations between K and V values into sets
of 8,
thereby optimizing attention score computations.
A notable distinction between LLaMA 2 and its predecessor
length, coupled with
was the doubling of the context
enhanced data cleaning methods. Baize [240] offered a novel
pipeline leveraging ChatGPT to autonomously generate new
fine-tuning data.

Several LLaMA derivatives aimed to achieve multi-
lingual capabilities. Chinese-Vicuna and Luotuo (also termed
Chinese-alpaca-lora [241]) fine-tuned the LLaMA model
using the LoRA approach to support Chinese, among other
languages. Chinese Llama Alpaca 2 [242] expanded upon

[243]

to integrate multimodal support

this, incorporating datasets from various languages, including
German and French.
Others sought

into
LLaMA. LLaMA adapter
introduced a pipeline
adapting LLaMA for visual instruction-following, yielding
a smaller and quicker fine-tuning model. Its successor,
LLaMA adapter V2 [244], preserved instructions from its
predecessor while refining the image-text projection to
enhance visual-text alignment. MiniGPT-4 [245], grounded
in the Vicuna model, implemented a two-phase pre-training
approach. After freezing both the language model and
visual encoder,
it constructed a new image-text dataset
for fine-tuning MiniGPT-4, ensuring superior visual-text
alignment. Both Chinese-LLaVA [246] and LLaSM [247]
were derived from LLaMA 2 but incorporated multi-modal
support. Visual-LLaMA [248] utilized a technique consis-
tent with KOSMOS-1 and PaLM-E, merging visual and
tokens for training. Video-LLaMA [249] integrated
text
both audio and visual
information, using a two-layer
Q-former [250] for video embedding. This model underwent
training on the Webvid-2M dataset and the image captioning
dataset from LLaVA [157], a visual-language model built
on 150K multimodal data samples generated by GPT-4.
Post pre-training, fine-tuning instructions from MiniGPT-4,
LLaVA, and VideoChat [251] were applied. The audio data
in Video-LLaMA was processed similarly, but with the
inclusion of the ImageBind-Huge encoder [252] for audio
information embedding.

6) GOPHER AND DEEPMIND
Gopher, introduced by DeepMind, is a large language model
(LLM) with a training pipeline that encompasses six models,
varying in parameter count from 44M to 280B [253].
This model employs the RMS Pre-norm strategy [228]
and incorporates relative positional embeddings using a
32,000 token SentencePiece tokenizer [254]. For training and
evaluation, the Gopher utilizes the JAX [255] and Haiku [256]
frameworks. Parallel computing is facilitated by JAX pump,
and the model is trained using the MassiveText dataset.

Chinchilla, also a product of DeepMind and the suc-
cessor to Gopher, posits that as the size of the model
increases, the number of tokens trained should proportionally
increase [257]. It suggests that the optimal Gopher model
should be four times smaller when trained on a dataset that
is four times larger. Various fine-tuning strategies based on
Gopher were explored to ascertain the optimal ratio between
model size and training data. These included altering the
number of tokens per batch, maintaining consistent FLOPs,
and training with a parameterized loss function. The latter
was identified as the optimal approach.

DeepMind further developed a visual model named
Flamingo, with 80B parameters,
few-shot
learning [258]. It employs the Perceiver resampler, training
with a pre-established visual model known as NFNet [259].

tailored for

VOLUME 12, 2024

188683

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

During the pre-training phase of the language model, NFNet
remains static. Subsequently,
the Perceiver resampler is
integrated with the frozen language model and the visual
model, yielding visual representations. The language model
is then fine-tuned, leveraging these visual representations,
which strengthens the nexus between the language and visual
models, resulting in state-of-the-art performance.

7) OTHER AUTO-REGRESSIVE MODELS
Jurassic-1, introduced by AI21 Lab in collaboration with
the AI21 Studio, was developed with the objective of
offering an open conversational API [260]. At the time
of its release, the Jumbo edition of Jurassic-1, with its
178B parameters, was heralded as the most intricate and
expansive model available [261]. This model was trained
on a corpus encompassing 250K labeled datasets. AI21
asserted that the dataset underpinning the Jurassic-1 model
was quintuple the size of concurrent datasets. Succeeding
Jurassic-1, Jurassic-X integrated the Modular Reasoning,
Knowledge, and Language (MRKL) system—a composite of
mixed expert data extraction from multiple databases. The
outputs from these extractions are then processed by the
language model, achieving a balance between universality
and sparsity in large language models [262]. In 2023, AI21
Lab unveiled the Jurassic-2 model [263] with enhancements
spanning multilingual capabilities, accuracy, and latency.

in the InstructGPT paper—namely,

Anthropic launched the Claude model series, comprising
two iterations: Claude [264] and Claude 2 [265]. The
foundational ethos of Claude echoes the principles laid
the creation of
out
AI language models that are helpful, honest, and harm-
less [188]. With this framework, Claude was trained on a
dataset meticulously curated to align with these objectives,
blending datasets that were both assistance-focused and
harm-avoidant. This amalgamated dataset bolstered the
performance model’s propensity for helpfulness while
eschewing potentially detrimental instructions. Claude 2,
the subsequent model, showcased amplified performance
metrics, supporting extended sequences, enhanced coding
proficiency, and heightened security measures. Anthropic
posited that Claude 2 boasts a security standard twice as
robust as its predecessor, Claude 1.3.

Falcon, a pioneering model accessible to the public,
to several proprietary
stands as a worthy counterpart
models [266].
It comprises three variants: Falcon-7B,
Falcon-40B, and Falcon-180B. Predominantly trained on the
RefinedWeb dataset—a refined iteration of the Common-
Crawl dataset [187], [267]—Falcon harnesses multi-query
attention, mirroring the PaLM model. This approach
substantially curtails the memory overhead of the K, V values
during training, slashing memory usage by factors ranging
from 10 to 100.

OpenAI, beyond the GPT series, has released several
domain-specific models. DALL-E [268] is a model designed
for image generation. It incorporates three distinct models:

the dVAE [171], which encodes and compresses the input
image; a BPE Encoder combined with a transformer
for auto-regressive training; and CLIP [269] to measure
the similarity between text-image pairs. DALL-E 2 [270]
employs CLIP to align the feature spaces of both text and
image data. Subsequently, it introduces a module named
‘‘prior’’ that uses caption data to embed the data from
the CLIP model, then decodes this data into an image.
Notably, DALL-E 2 has approximately 3.5B parameters,
substantially fewer than DALL-E’s 12B parameters. DALL-E
3 [271], released in 2023, is reportedly built on ChatGPT,
though detailed technical information had not been disclosed
at
the time of this survey. Whisper [272] is designed
for audio-to-text conversion and boasts 1550M parameters.
The training of Whisper utilized over 680K audio samples
from 98 languages, supporting multi-tasking in a supervised
learning context. Each audio sample was segmented into
30-second chunks and processed into log-Mel-frequency
cepstrum. Codex [273] targets coding challenges, comprising
12B parameters with [274] which is also a model
that
is specific on coding tasks. It is trained using a dataset
amalgamated from GPT data and open-source code from
more than 5400 GitHub repositories, which, post-cleaning,
amounted to 159G. Its efficacy was validated using the
HumanEval dataset, which includes 164 manually generated
programming problems to ensure the output’s accuracy.

In addition to the PaLM series model developed using
the Pathways architecture, Google has unveiled several
domain-specific models. Meena targets end-to-end question
answering and employs the evolved transformer architec-
ture [275]. Its performance is assessed through human
evaluation and perplexity metrics. LaMDA [276] employs
knowledge-based queries, building on Meena to endow
industry-related
the model with the ability to answer
knowledge questions. ALIGN [277] is designed to tackle
representation learning for visual-textual data. It processes an
extensive dataset containing over 1B noisy image captions,
incorporating EfficientNet [278] for image-text matching,
retrieval, and visual classification tasks. The objective of
GaLM [279] is to harness the sparsity of LLM for efficient
few-shot
is trained on a colossal
dataset
featuring 1600B tokens, predominantly sourced
from websites. GaLM utilizes the MoE architecture for
training and houses approximately 1.2T parameters across
64 experts. Intriguingly, during inference, only 97B of these
parameters are activated, enabling rapid response times.
Lastly, Gemini [280] is a model that recently released by
Google as their next-generation of large language model,
which contains Gemini Ultra, Gemini Pro and Gemini Nano,
Genmini.

learning. The model

In June 2023, Microsoft proposed Phi-1, a model with
just 1.3 billion parameters. Its goal
is to achieve high
accuracy performance with a small model, highlighting the
significance of high-quality data during the pre-training
phase. They stated that they used exercises using 1B tokens

188684

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

and GPT-3.5 along with 6B tokens from online and artificially
generated textbooks, all of which were of ‘‘textbook quality’’.
Following the release of Phi-1, Microsoft also released
Phi-1.5 [281], which was the same size as Phi-1, and Phi-2
[282], which was their most recent model and a foundation
model with 2.7B of parameters to exhibit
the potential
capability on small language models (SLMs).

tasks within a single model, yet

mPLUG is a series of models developed by Alibaba,
tailored for multimodal support in Large Language Models
(LLMs). The conceptual
foundation of mPLUG [283]
draws inspiration from the modularity of the human brain.
In this architecture, each modality is treated as a separate
module, allowing for specialized task handling. Conversely,
mPLUG-2 [284] adopts a unified model approach, managing
all
through different
modules. mPLUG-Owl is a conversational LLM that has
been open-sourced. It employs a Vision Transformer (ViT)
to learn from visual-language captioning data. Subsequently,
the model is fine-tuned using LoRA to align both uni-modal
and multi-modal data, while preserving the foundational
visual-text modules trained in the initial phase. There are
other models like MM-REACT [285] and HuggingGPT [286]
that serve to facilitate collaboration across various modal-
ities. Additionally, models such as Youku-mPLUG [287],
mPLUG-DOCOWL [288], and MultiVENT [289] are deriva-
tives of the original mPLUG design.

Numerous institutions, companies, and research affili-
ations have released auto-regressive models to push the
boundaries of machine learning. AlexaTM [290], a multi-
lingual model housing 20B parameters, has achieved
state-of-the-art performance, especially for low-resource
languages. PLATO [291] leverages discrete latent variables to
encapsulate invisible background knowledge. Its successor,
PLATO-2 [292], refines the original by expanding both the
training data and the number of parameters, incorporating
a curriculum learning approach. The WuDao series boasts
models like WuDao 2.0 [293], one of the most extensive
LLMs with 1.75T parameters, and WenLan [294], a
5.3B parameter model tailored for Chinese-English visual
captioning, rooted in a 650M image-captioning dataset and
utilizing the Deep Structured Semantic Model (DSSM)
[295] technology. Cogview [296], a 4T parameter Chinese
multimodal LLM, and Lawformer [297], an early LLM
dedicated to the legal domain, are noteworthy contributions.
OPT [298], developed by Meta, is an endeavor towards
open-sourcing LLMs, with models ranging from 120M to
175B parameters. Its enhanced version, OPT-IML [299],
comprises two models with 30B and 175B parameters,
respectively, and is fine-tuned using datasets spanning over
2000 languages. YaLM [300], a 100B LLM by Yandex,
is trained on 1.7T text data sourced from websites, books,
and other mediums. BLOOM [301] is a comprehensive
model with 176B parameters, trained on data from 46 natural
languages and 13 programming languages, representing
the collaborative efforts of over 1000 scholars. Lastly,

TABLE 7. Training strategies used in BART.

Galactica [302], developed in partnership between Meta
and Papers with Code, mirrors the ambitions of GLaM in
addressing scientific challenges. Mistral [303] claimed it uses
mix-of-expert outperformed GPT-3.5 with smaller model size
with the usage of mix-of-expert.


#### C. SEQUENCE TO SEQUENCE MODELS
Another prominent architecture in the domain of large lan-
guage models combines the features of both Auto-encoding
and Auto-regressive models, known as the sequence-
to-sequence model. Typically,
it employs the complete
Transformer framework, encompassing both encoder and
decoder structures. This hybrid model amalgamates the
strengths of its predecessors, inheriting the natural language
understanding capabilities from the encoder and the gen-
eration competencies from the decoder. To integrate the
functionalities of both encoder and decoder, cross-attention
is implemented between their respective layers, facilitating
the interplay between different sequences. Owing to their
distinctive advantages over models that solely use an encoder
or decoder, sequence-to-sequence models are predominantly
chosen for conditional generation tasks like summarization
and machine translation. Compared to the previous two
architectures, which multiple models may share one single
origin, sequence to sequence models are more independent,
which means it has fewer models derived from previous
predecessors but normally, they formed their own family
by them own regarding different tasks hence cause less
consistency compared with the auto-encoding models and
auto-regressive models.

1) BART
BART [304] represents a significant development in the
Sequence-to-Sequence model lineage and stands as one of the
earliest models harnessing the full Transformer architecture.
It masterfully combines BERT’s [3] bi-directional encoder
characteristics with the auto-regressive decoder features from
GPT. In training BART for sequence generation tasks,
the Google research team employed a reconstruction loss,
defined as the cross-entropy between the conditionally
generated output based on the input and the actual ground
truth. They also enhanced the masking technique inherited
from BERT. Several masking strategies were adopted:

BART’s training strategies can vary depending on the
targeted downstream tasks. For sequence classification tasks,
both the encoder and decoder process the sequence, and

VOLUME 12, 2024

188685

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

the final state of the output is utilized. Similarly, for token
classification tasks, the decoder’s final state serves as the
definitive representation for each token, though these tokens
are considered independent. In machine translation tasks,
the encoder’s embedding is supplanted with an additional
encoder termed the ‘‘randomly initialized encoder,’’ which
can leverage a disjoint vocabulary.

In a step forward, mBART [305] harnesses corpora from
multiple languages, bestowing BART with multi-linguistic
capabilities. This version was fine-tuned from the founda-
tional BART model.

2) BASED ON T5
T5 [11] introduced a universal framework in the realm
of pre-trained models. One of its major contributions was
presenting a clear guide for future researchers concerning
parameter and architecture selection. The model underwent
training on 750G of tokens, encompassing 11B parameters.
In T5’s approach, every NLP task was conceptualized as a
text-to-text task, leading to the adoption of the Sequence-
to-Sequence architecture. The model utilized three distinct
masking techniques: fully-visible masks where attention
scores are computed from all input and output tokens; causal
masks, similar to GPT’s, where scores are derived only
from the current token and its antecedents, predicting the
subsequent token based on previously generated content; and
causal masks with prefix, where the input sequence employs a
fully-visible mask, but for the output’s predicted tokens, only
causal masks are used.

The study also evaluated three architectures: the encoder-
decoder,
the encoder-only (as seen in GPT-2), and the
Prefix LM. In the latter, while the encoder can perceive
bi-directional information, the decoder is limited to previ-
ously generated tokens. Furthermore, the C4 dataset, crafted
from the Common Crawl database [187], emerged from
this work. The dataset
involved a refinement of about
750GB of web data, retaining lines that ended with standard
punctuation, eliminating offensive words, omitting lines
containing Javascript, discarding pages that resembled code,
excluding lorem ipsum passages, and ensuring sentences that
appeared more than three times were uniquely preserved.

1) Only Kept lines end with normal punctuation
2) Deleted all bad words
3) Removed lines with Javascript
4) Deleted all pages like code
5) Removed lorem ipsum
6) Only kept once for same sentences appears more than

three times

Building on T5’s foundation, mT5 [211] aimed at machine
translation tasks within a multilingual context. It borrowed
incorporated
strategies from the original T5 model but
more vocabulary to ensure a broader linguistic coverage.
This was realized by drawing samples from languages with
limited training data, using an approximation technique as
suggested by [306]. T0 [307], evolving from T5, explored
the enhancement possibilities of LLM focusing on prompt

FIGURE 26. The architecture of Pangu-(cid:54), the query layer proposed in that
model was used after the embedding passed through the transformer
layers, then the prediction of the next token wouold be produced from
the query layer with position embedding.

engineering for multitasking and robustness. Trained atop
T5-LM, T0 incorporated training prompts from 177 datasets,
amassing 2073 prompts in total. The performance indicated
marked improvements in comparison to GPT-3. In a departure
from FLAN [306], which also built upon T5, T0 retained
the encoder-decoder architecture, whereas FLAN was solely
anchored on T5’s decoder.

3) PANGU
Pangu is a series of models comprising Pangu − α [4],
Pangu−Coder [308], and Pangu−(cid:54) [5]. Unlike its precursor,
Pangu − α, the Pangu − Coder was specifically designed
as a decoder-only model tailored for generation tasks in both
Chinese corpus and code generation. In contrast, Pangu − (cid:54)
adopts an Encoder-Decoder architecture.
Introduced in
March 2023, the primary goal of Pangu − (cid:54) was to develop a
large language model focusing on the Chinese corpus, while
also being adept at multilingual tasks. Huawei announced
that this model was the first China-centric LLM boasting
a colossal 1T parameters size, approximately 1.085T, and
underwent training with 2.17T data spanning over 300B
tokens. The data sources for its training included 200G
from WuDaoCopora 2.0 [309], 100G from CLUECorpus
2020 [310], 800G from the Pile [311], and 750G from C4
[11]. Given its capability to execute code-related tasks, the
Pangu − (cid:54) also incorporated 157G of Python code and 161G
of Java code.

Two innovative technologies bolstered the model’s effi-
ciency. The first was a novel sparsity technique termed
‘‘Random Routed Experts’’ (RRE). Implemented in two
phases,
the initial step involved grouping the experts
based on their parameters by the same task. Then, for
every prompt, RRE deviated from the conventional MoE
approach. Instead of allocating tokens to a specific expert
with the most compatible matchup governed by a gate

188686

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

of experts needed. This calculation takes into account the
number of tokens in each batch and the number of experts
active at a given stage. The ‘‘capacity factor’’ introduced
in this mechanism serves as a buffer, permitting a surplus
of experts to counter potential token overflows during the
routing process.

5) GLM
GLM [12] introduced an innovative approach known as
auto-regressive blank infilling to refine the masking and
from models like
infilling techniques, setting it apart
BERT and T5. Instead of simply masking out
tokens,
GLM strategically removes continuous words from the
input and then attempts to reconstruct them. A distinctive
feature of GLM is that the prediction of masked regions
can be permuted. Moreover, its positional embedding is
designed in a 2-dimensional format. Impressively, with
fewer parameters, GLM managed to outperform BERT on
the SuperGLUE benchmark [313]. By leveraging Pattern
Exploiting Training [314], GLM transformed various natural
language understanding tasks into cloze-style problems,
which could potentially have multiple correct answers.

Building upon the capabilities of GLM, ChatGLM [315]

was developed to provide conversational support.

Further expanding its applications, a multimodal version
of GLM was introduced as VisualGLM [316]. This model
supports visual conversations in both English and Chinese
languages. Beyond the foundational architecture of GLM-6B,
VisualGLM incorporates image data training based on the
BLIP2-Qformer framework [317].

VII. PRE-TRAINING METHODS FOR LLMs
Pre-training is a critical phase in the development of
Large Language Models (LLMs). This phase involves
training the models on vast amounts of textual data to
learn language patterns, structures, and contextual nuances.
The effectiveness of pre-training significantly impacts the
performance of LLMs on downstream tasks such as text
generation, machine translation, summarization, and more.
This section delves into various state-of-the-art pre-training
methods for LLMs, categorized into different strategies
such as training data reduction, neural architecture search,
progressive learning, mixed precision training.


#### A. TRAINING DATA REDUCTION
Training data reduction techniques aim to minimize redun-
dancy and improve the efficiency of the training process by
selecting or augmenting the most relevant data.

- COPA [318]: Combining pre-training and adaptation

strategies to enhance generalization.

- MixMAE [319]: Data augmentation and masking
strategies to create diverse and challenging training
examples.

- Deduplicate Text Datasets [320]: This method involves
removing duplicate entries from the training data to
reduce redundancy and improve training efficiency.

FIGURE 27. Noise used by BART. 1. Original sequences, different
sequence denoted by different colour 2. Token masking, in this case, the
word ‘‘is, today, it, want’’ were masked 3. Token deletion, the word ‘‘how,
weather, raining, know’’ were deleted 4. Token infilling, token ‘‘is, to’’
were masked and it was required to infill the token ‘‘how, the’’ and
‘‘want, know’’ spanned from the masked tokens 4. Document rotation,
in this case the last sentence ‘‘I want to know’’ was rotated to the front of
the document 5. Sentence Permutation: the order of the sentence in the
document was changed, in this case, the last sentence ‘‘I want to know’’
was changed to the second sentence to find the contextual information
between sentences.

function, RRE would haphazardly assign an expert for
a token. This gate-free procedure enabled researchers to
derive sub-models from Pangu − (cid:54),
facilitating their
application to other downstream activities like translation
and chatting. The second technological breakthrough was
the ‘‘Expert Computation and Storage Separation’’. This
mechanism strategically distributed model training across
clusters, resulting in a remarkable 69,905 tokens-per-second
I/O efficiency and a substantial reduction in communication
overhead between servers and devices.

4) SWITCH TRANSFORMER
Switch Transformer [312] employs the sparsity inherent in
LLMs to accelerate both training and inference. The term
‘‘switch’’ in its name refers to the shifting between experts.
Thus, its primary technology is the Mixture of Experts
(MoE). In the architecture of this model, there are several
experts, each having distinct parameters that are regulated
by a gating function. For any given input or prompt, only
certain sections of the model are activated based on the input
parameters, thereby reducing the computational complexity
associated with each task. As an illustrative example from the
paper, a particular task might comprise a sequence of tokens,
with each token designated to different experts.

Another significant advancement introduced in the Switch
Transformer is the concept of ‘‘Simplified Sparse Routing’’.
Traditionally, a single token would be routed to multiple
‘k’ experts, and the optimal response would be selected as
the output to ensure both relevance and accuracy. Google
streamlined this process. They posited that even if k equals 1,
meaning each token is processed by just a single expert,
the model can maintain its accuracy, all the while boosting
efficiency.

Lastly, the model introduces ‘‘Efficient Sparse Routing’’.
Google provided a formula to compute the optimal number

VOLUME 12, 2024

188687

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

- TRIPS [321]: Task-aware pre-training data selection to
ensure that the training data is relevant to the specific
tasks the model will perform.

- PatchDropout [322]: Randomly dropping patches of

input data to reduce computational requirements.

- TPS [323]: Token Pruning Strategy for efficient training

by selectively pruning less important tokens.


#### B. NEURAL ARCHITECTURE SEARCH
Neural Architecture Search (NAS) involves automatically
finding the best neural network architecture for a given task.
These methods optimize the model design to achieve better
performance.

- PreNAS [324]: Informed architecture search based on

pre-training results.

- PASHA [325]: Progressive architecture search that

evolves hybrid architectures over multiple stages.

- ZICO [326]: Zero-shot architecture search to identify
optimal model structures without extensive training.
- ElasticViT [327]: Adaptive vision transformer architec-
ture that adjusts computation based on input complexity.
- RankNAS [328]: Ranking neural architectures based on

performance metrics.

and implementing novel pre-training methods will be crucial
for further advancements.

VIII. CHALLENGES OF LLMs
Large language models are the result of the development
of neural networks and the technologies that followed such
as like deep learning. For the modern cutting edge models,
challenges still exist in the following phases:

- Data Drawbacks: Large language models requires a
massive computational resource for the pre-training and
fine-tuning.

- Model Compression: Large language models normally
contains over billions of parameters, which cause mem-
ory intensive during both the training and deployment
phase.

- Distributed Computation: Due to the increasing model
size, some state-of-the-art large language models are
trained on high performance clusters rather than local
devices, which presents a challenge for distribution
computation in the LLM field.

- Multimodal Support: Large language models can not
only handle natural language processing tasks, but also
dealing with data from different format, that casues the
multimodality support challenge of LLMs.


#### C. PROGRESSIVE LEARNING
Progressive learning strategies involve training models in
stages, gradually increasing the complexity and scale to
improve performance and stability.

- LiGO [329]: Layerwise growth optimization to effi-

Cutting edge methods like Chain of Thought, Reinforce-
ment Learning with Human Feedback, Transformer, and Mix
of Expert have been proposed to train a model on a massive
scale. A cursory review of the technologies that underpin the
LLM technique will be provided in this section.

ciently scale models.

- Staged Training [330]: Gradual increase in training

complexity through multiple stages.

- Knowledge Inheritance [331]: Transferring knowledge

progressively across model versions.

- CompoundGrow [332]: A strategy for progressively

increasing model size during training.

- stackingBERT [333]: Stack-based training approach

for incremental learning in BERT models.


#### D. MIXED PRECISION TRAINING
Mixed precision training techniques aim to balance training
speed and model precision by using different numerical
precisions for different parts of the model.

- Mesa [334]: Scheduling multi-epoch training with

mixed precision adaptations.

- GACT [335]: Gradient accumulation with compression

techniques to train large models efficiently.

- blpa [336]: Block-level precision adaptation for effi-

cient training.

- Mixture [337]: Employing mixed precision training to

enhance speed while maintaining accuracy.

The pre-training phase is vital for developing robust and
efficient LLMs. The methods described represent recent
advancements in pre-training, improving model performance,
efficiency, and applicability. These strategies highlight the
dynamic nature of NLP research. As LLMs evolve, exploring


#### A. DATA DRAWBACKS
The use of massive datasets is one of the main char-
acteristics of LLMs. These datasets are essential to the
pre-training, fine-tuning, and evaluation processes of these
models, as demonstrated by the experiment in [257], which
demonstrates the superior performance of a smaller model
trained with more labelled data than a larger model trained
with less labelled data. However, as LLMs scale up, data
challenges persist. The main points of the LLM problems
pertaining to the data will be summarized in this section.

1) QUALITY OF DATA
When it comes to relevance, richness, and redundancy, the
quality of the data used to train LLMs is just as crucial as
the model itself. Poor data quality can provide inaccurate
and unreliable knowledge to the model as it learns from the
datasets. The following factors could be the cause of the
taxonomy of the data quality in this survey: (1. Inaccurate
Data: The model will pick up problematic knowledge from
these data, resulting to inaccurate or deceptive information in
the model. (2. Outdated Data, this is particularly problematic
in domains like technology and public events that are
changing quickly. As an illustration, the most recent version
of GPT-4, GPT-4 Turbo [338], used knowledge up to April
2023, but the original GPT-4 [190] used knowledge dated
back to September 2021. Various technologies, including

188688

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 8. Open-Sourced datasets for training large language models.

FIGURE 28. The common source of the dataset used for pre-training.

machine learning [339] and model editing [340], [341], [342],
could be employed to mitigate this drawback. (3. Redundancy
of the data describes the existence of redundant or overly
similar information in the training dataset; if a dataset has
multiple copies of the same content, this will lead to an
overrepresentation of the model on the viewpoints, which
will increase the model’s biased understanding of particular
topics. Certain measurements, like data deduplication [343],
or the common solution from a range of state-of-the-art
models, like Llama [10] and GPT [190], involve using data
from many sources.

2) BIAS OF THE DATA
The training data frequently involves biases in human
languages or other forms of data input. These biases can
span a wide range of topics,
including gender, color,
culture, religion, profession, and philosophy, along with
preconceptions. As a result, concerns over justice and
ethnicity may arise.The bias of
language models was
characterized by [344] from many perspectives with respect
to the social impact. A few studies have tried to lessen the
effects of language model bias. For example, [345] uses
local edit to lessen gender bias, and [346] uses reinforced
calibration to lessen political bias. [347] offered a novel way
to measure the bias stereotype on these pretrianed models.

3) SCALE OF DATA
LLMs require massive amount of data to improve its
accuracy and understanding of the prompts, which caused the
challenge on the scale of the data regarding data collection,
precessing and storage. The figure 15 shows the common
source of the the datasets.

Following table shows the size of come popular datasets
used by modern LLMs, single dataset such as The Pile and C4
already have hundreds of gigabytes and web-based database
such as Common Crawl has already reached terabytes
level.

Current cutting edge models normally applied datasets
from different sources such as LLama [10] used up to 4.5T of
the datasets and [5] applied 1.1T of the training data, which is
also a huge challenge for the device used for the pre-training
tasks.


#### B. MODEL COMPRESSION
In response to the space challenges posed by LLMs, this
section provides a brief overview of three state-of-the-art
model compression technologies. ‘‘Space challenges’’ in
LLMs refer
to the device memory limitations during
pre-training, fine-tuning, and deployment due to the large
size of model parameters. As LLMs grow larger to increase
accuracy, more parameters are added, which intensifies
computational demands. Model compression offers a solution
by optimizing the internal structure of models to improve effi-
ciency without significantly sacrificing performance. Three
methods comprise the state-of-the-art model compression
technique: (1) Pruning; (2) Quantization; and (3) Knowledge
Distillation. These methods effectively address the efficiency
and scalability challenges of LLMs by reducing model size
and computational requirements.

1) PRUNING
Pruning in large language models refers to the process of
reducing model size by eliminating redundant and less critical
structures. It can be categorized into two types: unstructured
pruning and structured pruning. This optimization technique
aims to shrink LLMs without significantly compromising
their performance by selectively removing parameters con-
sidered less important for the model’s task. Pruning methods
eliminate redundant or non-informative parameters and can
be performed in a structured or unstructured manner, each
with its own strategies and impacts on model performance
and efficiency. Typically, pruning involves a criterion to
determine which weights to remove, based on factors like
weight magnitude, training gradients, or other measures of
importance. After pruning, the model usually undergoes
fine-tuning to recover any lost performance due to parameter
removal.

Structured pruning refers the pruning on the entire sets
of the model structure such as channels, layers and weights.
Structured pruning is advantageous for its compatibility
with hardware optimization as it leads to a more regular
and streamlined model structure with the trade-off of the
substantial impact on the model’s accuracy due to the removal
of the entire structure.

Unstructured pruning only removes certain individual
weights or nodes from a neural network with the least

VOLUME 12, 2024

188689

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 9. Pruning techniques used in Large language models categorized
in structured, unstructured, and their combination.

importance inside the model connection, which leads to a
more fine-grained pruning results with significant reduction
on the model size. Different from the structured pruning
which has the regular structure, unstructured pruning is hard
to be implemented on the hardware due to its irregularity.

Table 7 shows transformer based pruning technology that

can be applied on large langauge models

2) QUANTIZATION
Quantization aims to decrease the memory footprint and
computational demands of neural network models by
converting high-precision model parameters,
typically in
extended data formats like 32-bit,
into more compact
representations, such as 8-bit formats, without significantly
compromising performance. This technique is vital in model
compression technologies and can be categorized into two
main types: Post-Training Quantization (PTQ) [374] and
Quantization Aware Training (QAT) [375].

In the context of LLMs, quantization reduces com-
putational resource requirements by transforming model
parameters from high to low precision, typically converting
32-bit floating-point weights and activations to 8-bit integer
format. This approach benefits both the storage footprint and
computation speed.

Quantization employs a graded approach, ranging from
3-bit quantization for the most compact model size to
8-bit for nearly full precision. Each increase in bit-size
generally improves the model’s accuracy but also increases
its size and computational demands. The most aggressive
3-bit quantization combines different techniques for various
parts of the model, while higher bit-sizes use more refined
methods, allocating more bits to parts sensitive to precision
loss. At the high end, 8-bit quantization closely approaches
the model’s original floating-point precision, yielding high
accuracy at the expense of size and speed. This spectrum of
quantization strategies allows flexible deployment of LLMs
like LLaMA 2 across different use cases, balancing resource
constraints and accuracy needs. Table 6 summarizes these
quantization methods, detailing the techniques, bit sizes, and
model sizes.

a: POST-TRAINING QUANTIZATION
(PTQ) is a static quantization method applied after the
model training process. It directly alters the original data

format of the model without the need for additional data or
modifications, aside from a few supplemental steps. In deep
neural networks, the input typically adheres to a distinct
pattern, facilitating statistical analysis. In PTQ, quantization
algorithms convert the data format to a lower precision,
guided by training data characteristics like the minimum
and maximum weights and the distribution of activations.
PTQ can be further subdivided into two methods: saturation
and no saturation. The saturation approach employs KL
divergence to identify a threshold T , which then rescales the
data range. In contrast, the no saturation method determines
the maximum value of the model weights and then maps this
value to a more confined data format range.

b: QUANTIZATION AWARE TRAINING
In PTQ, quantization algorithms rely on statistical data from
the model to determine the mapping, leading to a more
significant discrepancy between the original and compressed
models. On the other hand, Quantization Aware Training
(QAT) adopts an online approach. Unlike the static methods
in PTQ, QAT learns the scale and threshold during the
training process by simulating the quantization effects.
During QAT, a scaling ratio is established to map intermediate
values. By allowing quantization to be back-propagated, this
method results in a reduced quantization loss, making the
quantized weights more akin to the original model’s weights.

3) KNOWLEDGE DISTILLATION
Knowledge distillation in large language models (LLMs)
is a technique aimed at streamlining their vast knowledge
into more compact and efficient
forms. This process
involves training a smaller, student model to emulate the
behavior of a larger, teacher model, effectively transferring
the sophisticated decision-making abilities of LLMs to
smaller models. This makes the smaller models suitable
for environments with limited computational resources,
maintaining core functionalities while significantly reducing
computational overhead.

Knowledge Distillation (KD) compresses the knowledge
of a larger, more complex teacher model into a smaller, more
efficient student model. This allows the student model to
perform at a level close to the teacher but with a fraction
of the computational requirements. Two main approaches,
White-Box and Black-Box KD, are used in this process.

a: WHITE-BOX KNOWLEDGE DISTILLATION
This method involves using not only the outputs of the
teacher model but also its internal representations and states
to guide the training of the student model. This richer transfer
of knowledge provides the student with insights into the
intermediate processing of the teacher.

b: BLACK-BOX KNOWLEDGE DISTILLATION
In contrast, Black-Box KD uses only the final outputs of
the teacher model. The student learns to mimic the teacher’s
output distribution without access to its internal workings,

188690

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 10. Summary of different quantization methods for the LLaMA 2 model with a focus on k-quant strategies and resource implications.

TABLE 11. Quantization algorithms using QAT and PTQ.

making this method more flexible as it doesn’t require
the student’s architecture to match the teacher’s internal
structure.

The key challenge in both types of Knowledge Distillation
(KD) is transferring as much relevant information as possible
from the teacher to the student model. This often involves
training the student
to reproduce the teacher’s output
probabilities, which carry more information than just the final
predicted class. The effectiveness of KD can be measured by
how well the student model performs compared to the teacher
on a set of tasks, ideally achieving similar performance while
being more efficient to run.

Advancements in this domain have introduced innovative
strategies to enhance the student model’s learning process,
such as selecting the most
informative elements from
the teacher model’s knowledge and utilizing intermediate
training experience. These
representations for a richer
techniques ensure that the distilled model replicates the
critical aspects of the teacher model’s performance. The
impact of knowledge distillation extends beyond model
efficiency, enabling the deployment of advanced language
processing tools in diverse applications and promoting
sustainable AI practices by reducing computational and
energy demands.


#### C. DISTRIBUTION COMPUTATION
Owing to the immense scale of large language models,
which can reach up to trillions of parameters, traditional
deep learning methods using single-device training or
deployment are insufficient to handle the vast datasets and
expansive parameter sizes associated with these models. As a
result, distributed computation has emerged as a pivotal
solution. Presently, three primary distributed computation
methods are employed to address these challenges: data

parallelism enhances the speed of model training, while
tensor parallelism and pipeline parallelism enable the training
of models that exceed the device’s memory capacity.

1) TENSOR PARALLEL
The fundamental concept of tensor parallelism involves
dividing the entire tensor of a model into distinct segments.
Each device retains one segment of the tensor, and the
final results can be procured by concatenating these tensor
segments based on the dimensions from which they were
partitioned. As an intra-layer parallelism method, its primary
advantage is the ability to obtain results through a singular
concatenation operation. However, a drawback of tensor
parallelism is the necessity for an additional step to ensure
the accuracy of the concatenation.

2) PIPELINE PARALLEL
Pipeline parallelism involves segmenting the entire model
into multiple sections based on its layers, a method also
referred to as inter-layer parallelism. In this approach, each
device manages several layers of the model, and data is
sequentially processed through the devices in accordance
with the model’s structure. Unlike tensor parallelism, pipeline
parallelism doesn’t require additional operations, as each
device contains a complete segment of the model. However,
a limitation is that devices must await data output from
the preceding device, leading to idle periods. Consequently,
pipeline parallelism can result in the underutilization of
computational resources.

3) DATA PARALLEL
Unlike the previously mentioned approaches, which focus
on accommodating models larger than what a single device
can handle, the objective of data parallelism is to expedite
the training process by harnessing computational power from
multiple devices. In data parallelism, every device retains a
copy of the model and is assigned a distinct data batch. This
setup facilitates parallelized training, thereby enhancing the
training speed. However, because each device has to store a
complete replica of the model, a notable drawback of data
parallelism is the inefficient use of device memory.


#### D. MULTIMODAL SUPPORT
A significant challenge for contemporary Large Language
Models (LLMs) is supporting multimodality, especially

VOLUME 12, 2024

188691

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

since the advent of the Vision Transformer (ViT) [213],
which showcased the potential of transformers for visual
tasks. Unlike conventional LLMs,
training models with
multimodal support is more intricate due to the need for
aligning representations across different modalities. This
introduces distinct training tasks for these multimodal LLMs.
This section is structured based on these tasks, which are
categorized into pre-training tasks and downstream tasks.

1) IMAGE-TEXT MATCHING
Image-Text Matching (ITM) is a method that aligns data
from different modalities from a coarse-grained perspective.
The primary objective of ITM is to predict the relationship
between two segments, typically an image-captioning pair.
This enables the model to learn the representation of text
and its corresponding images. ITM has been extensively
employed in state-of-the-art models. Examples include VIL-
BERT [402], B2T2 [403] — which employs bounding boxes
to fuse image patches with textual information for enhanced
visual-text
integration — as well as LXMERT [404],
XLXMERT [405], VisualBERT [166], UNITER [406],
Unicoder-VL [407], Pixel-BERT [408], ERNIE-VIL [175],
ERNIE-VIL 2.0 [176], and UNIMO [409], [410]. Further-
more, the BLIP series of models [paper, paper, paper] also
incorporated ITM as one of their training tasks.

2) CROSS-MODAL CONTRASTIVE LEARNING
In the Image-Text Matching (ITM) task, the model typically
determines whether a visual-text pair’s information aligns.
Meanwhile, Cross-Modal Contrastive Learning (CMCL)
seeks to enhance the association between image and text pairs
based on their similarity. More specifically, CMCL operates
like a clustering task, aiming to differentiate unrelated
visual-text pairs and cluster closely related ones. The study
[Leveraging Visual Knowledge in Language Tasks] explored
the efficacy of the CMCL task. Several models employed
this strategy,
including UNIMO [409], UNIMO2 [409],
WudaoMM [411], Taisu [412], CLIP [269], CLIP 2 [413],
and ALIGN [277].

3) CROSS-MODAL MASKED LANGUAGE MATCHING
Cross-modal masked language modeling (MLM) draws
parallels to BERT by masking a portion of the input
data, prompting the model to predict it during training.
This straightforward approach is particularly effective for
semantically dependent data. It’s one of the earliest strategies
introduced by ViT and has become popular in LLMs with
multimodal support due to its adaptability. Numerous mul-
timodal large language models, such as VisualBERT [166],
ViLT [414], and InterBERT [415], incorporate MLM in their
training processes.

4) MASKED REGION MODELING
Unlike Masked Language Modeling (MLM) which masks
information, Masked Region Modeling (MRM)
textual

input masking tasks and can be
is designed for visual
categorized into two main approaches: classification and
regression.

Masked Region Classification (MRC) has its origins in the
Masked Region Prediction task (MRP). However, in MRC,
masking is applied to an entire region of interest rather than
lower-level tokens like patches or pixels. The objective is
to predict the higher-level semantics of multimodal input
by determining the classification of the masked region,
using visible regions as context. Much like the ubiquity of
MLM in text-based models, many multimodal large language
models adopt MRC during training, notable examples being
VL-BERT and Unicoder-VL. While the conventional MRC
task utilizes cross-entropy, some models, such as UNIMO,
have incorporated a variant known as MRC-kl, which
employs KL-divergence as introduced by the UNITER
framework.

Masked Region Feature Regression (MRSR), another
offspring of MRP, employs regression techniques to recon-
struct
the feature map, rather than classifying masked
regions. Models like ImageBERT [416] and UNITER have
incorporated MRSR into their training paradigms.

5) OTHER PRE-TRAINING TASKS
Except the tasks mentioned above, there is other tasks used
by either pre-training tasks and downstream tasks on LLMs,
which is not as commonly used compared with the previous
mentioned models but were used by some specific models

1) WRA: Word Region Alignment
2) Seq2Seq: Sequence to Sequence generation
3) VQA: Visual Question Answering
4) MRFR: Masked Region Feature Regression
5) SGP: Scene Graph Prediction
6) VLC: Vision-Language Contrastive Learning
7) MTL: Multi Task Learning
8) WPA: Word-Patch Alignment
9) MVM (MFC): Masked Vision Modeling
10) VLM: Vision-Language Matching
11) ITC: Image-Text Contrastive
12) ITG: Image-Text Generation
13) PrefixLM: Prefix Language Modeling
14) MOC: Masked Object Classification


#### E. PROMPT ENGINEERING
Another essential technique that speeds up the compre-
hension of LLMs in context is prompt engineering, which
strategically formulates input queries that include content and
instruction. This technique is simpler than pre-training and
fine-tuning and allows users to interact with the LLM to
control the token datastream.

The following advantages arise from using prompt
engineering during LLM inference. Prompt strategies reduce
human bias in training data for LLMs by making it easier
for users to find relevant results. This is primarily because
of the interaction between the user and the system. Second,

188692

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

FIGURE 29. The most commonly utilized Prompt Engineering strategies.

the model users’ prompts have a high information density
when compared to the training data used for pre-training and
fine-tuning, suggesting that prompting is worth hundreds of
data points on average ( [417]). Thirdly, prompt engineering
can be customized so that users can achieve excellent
accuracy performance even in the absence of training,
particularly for downstream tasks. This feature offers prompt
engineering unparalleled benefits in addition to training
phases. Figure 29 is a taxonomy of some popular prompting
techniques.

IX. APPLICATIONS OF LLMs
LLMs have revolutionized various domains by leveraging
their capabilities to understand, generate, and manipulate
human language. Their applications span a wide array of
fields, including visual content creation, audio generation,
text generation, code generation, and design automation.
While LLMs primarily handle text, they are often integrated
with other systems to process and generate multimedia
content. The versatility and efficacy of LLMs have led
to significant advancements in these areas, with numerous
companies developing notable products to harness their
potential.


#### A. TEXT GENERATION
Text generation is one of the most prominent applications of
LLMs. It encompasses several tasks such as creative writing,
chat-bots, and language translation.

FIGURE 30. Applications of LLMs and MLLMs across various domains
including text generation, code generation, and visual content. These
applications showcase the versatility and impact of large language
models in enhancing productivity and innovation.

- Creative Writing: LLMs based tools like OpenAI’s
GPT-4 and -4o, Bard, Gemini and other writing
assistants help authors generate content, brainstorm
ideas, and overcome writer’s block.

- Chat-bots: Companies like Google, Apple, and Ama-
zon utilize LLMs in their virtual assistants (Google
Assistant, Siri, Alexa)
to provide intelligent and
conversational responses, improving user interaction.
- Language Translation: Tools like Google Translate
and Microsoft’s translation services leverage LLMs to
provide accurate and context-aware translations across
multiple languages.


#### B. CODE GENERATION
LLMs have also made significant strides in the field of code
generation, aiding developers in writing and optimizing code.
- Code Generation: Products like GitHub Copilot and
OpenAI Codex assist developers by generating code
snippets and automating repetitive tasks, thus speeding
up the development process.

- Code Completion: Tools such as Tabnine and Microsoft
Copilot offer real-time code suggestions and comple-
tions, enhancing coding efficiency and reducing errors.
- Bug Fixing: Services like Amazon CodeWhisperer and
other AI-powered code analysis tools help in identifying

VOLUME 12, 2024

188693

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 12. LLMs categorized into their Architectures, parameter count, and the Base LLM from which they are derived.

188694

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 12. (Continued.) LLMs categorized into their Architectures, parameter count, and the Base LLM from which they are derived.

TABLE 13. Multimodal support for MLLMs.

and fixing bugs, improving the overall quality of the
software.


#### C. VISUAL CONTENT UNDERSTANDING
In addition to text and code, LLMs are instrumental in under-
standing visual content. This includes tasks like text-based
image description, caption generation, and document reading
through OCR (Optical Character Recognition).

to provide detailed descriptions of images, enhancing
accessibility for visually impaired users.

- Caption Generation: Applications like SeeingAI and
DALL-E 3 generate captions for images, making content
more accessible and searchable.

- Document Reader: Products such as Descript and
other OCR technologies convert scanned documents and
images into machine-readable text, facilitating easier
access and analysis.

- Text-based Image Description: Tools like Google
Vision API and Azure Cognitive Services use LLMs

The applications of LLMs across various domains
demonstrate their vast potential in enhancing productivity and

VOLUME 12, 2024

188695

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

TABLE 14. Multimodal training approaches for MLLMs.

fostering innovation. As these models continue to evolve,
we can expect even more groundbreaking applications that
will further transform the way we interact with and utilize
technology.


### X. Conclusion
This paper offers an exhaustive review of Large Language
Models (LLMs) and their evolution within the domain
of Natural Language Processing (NLP). It explores the
diverse proficiencies of LLMs across various NLP tasks,
including text generation, logical reasoning, machine trans-
lation, summarization, and multimodal integration. LLMs
are systematically categorized into three primary archi-
tectures: encoder-only, decoder-only, and encoder-decoder
frameworks. Additionally, the paper highlights the inher-
ent challenges and constraints of LLMs, notably their
dependency on statistical patterns as opposed to genuine

understanding, and showcases state-of-the-art methodologies
in pre-training and fine-tuning. The paper also discusses
various model compression techniques, benchmarks, and
applications. Overall, this paper offers valuable insights into
the capabilities, challenges, and future prospects of LLMs in
NLP applications.


#### A. MODEL PARAMETERS
As the evolution of LLMs, the number of parameters is also
evolving from the BERT and GPT with only millions level
of data to current trillion level of model parameters, the table
below shows the models architecture and other metrics.


#### B. MULTIMODAL SUPPORT
The table below is the multimodal support
of the multimodal LLMs mentioned in this survey,

for each
the

188696

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

multimodality was classified into the following categories:
Text, Image, Video, Audio, Embodied


#### C. TRAINING APPROACHES OF MULTIMODAL LARGE
LANGUAGE MODELS
The table below outlines the commonly used training
approaches for multimodal large language models, highlight-
ing techniques for several models discussed in this survey
paper. It compares the data inputs, integration algorithms, and
training objectives across different models.

REFERENCES

[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, ‘‘Attention is all you need,’’ in Proc. Adv.
Neural Inf. Process. Syst., vol. 30, 2017, pp. 1–26.

[2] A. Radford, K. Narasimhan, T. Salimans, and I. Sutskever, ‘‘Improving
language understanding by generative pre-training,’’ OpenAI, USA,
Tech. Rep., 2018.

[3] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, ‘‘BERT: Pre-training
of deep bidirectional transformers for language understanding,’’ 2018,
arXiv:1810.04805.
[4] W. Zeng et al.,

‘‘PanGu-α: Large-scale autoregressive pretrained
Chinese language models with auto-parallel computation,’’ 2021,
arXiv:2104.12369.

[5] X. Ren, P. Zhou, X. Meng, X. Huang, Y. Wang, W. Wang, P. Li,

#### X. Zhang, A. Podolskiy, G. Arshinov, A. Bout, I. Piontkovskaya, J. Wei,

#### X. Jiang, T. Su, Q. Liu, and J. Yao, ‘‘PanGu-Sigma: Towards trillion
parameter language model with sparse heterogeneous computing,’’ 2023,
arXiv:2303.10845.

[6] A. Graves and A. Graves, ‘‘Long short-term memory,’’ in Supervised
Sequence Labelling With Recurrent Neural Networks. Berlin, Germany:
Springer, 2012, pp. 37–45.

[7] L. R. Medsker and L. Jain, ‘‘Recurrent neural networks,’’ Design Appl.,

vol. 5, nos. 64–67, p. 20, 2001.

[8] Z. Zhang, X. Han, Z. Liu, X. Jiang, M. Sun, and Q. Liu, ‘‘ERNIE:
Enhanced language representation with informative entities,’’ 2019,
arXiv:1905.07129.

[9] Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut,
‘‘ALBERT: A lite BERT for self-supervised learning of language
representations,’’ 2019, arXiv:1909.11942.

[10] H. Touvron et al., ‘‘Llama 2: Open foundation and fine-tuned chat

models,’’ 2023, arXiv:2307.09288.

[11] C. Raffel, ‘‘Exploring the limits of transfer learning with a unified text-
to-text transformer,’’ J. Mach. Learn. Res., vol. 21, no. 1, pp. 5485–5551,
2020.

[12] Z. Du, Y. Qian, X. Liu, M. Ding, J. Qiu, Z. Yang, and J. Tang, ‘‘GLM:
General language model pretraining with autoregressive blank infilling,’’
2021, arXiv:2103.10360.

[13] D. P Kingma and M. Welling, ‘‘Auto-encoding variational Bayes,’’ 2013,

arXiv:1312.6114.

[14] J. Zhai, S. Zhang, J. Chen, and Q. He, ‘‘Autoencoder and its various
variants,’’ in Proc. IEEE Int. Conf. Syst. Man, Cybern. (SMC), Apr. 2018,
pp. 415–419.

[15] R. Wei, C. Garcia, A. El-Sayed, V. Peterson, and A. Mahmood,
‘‘Variations in variational autoencoders—A comparative evaluation,’’
IEEE Access, vol. 8, pp. 153651–153670, 2020.

[16] I. J. Goodfellow, ‘‘Generative adversarial networks,’’ Proc. Neural Inf.

Process. Syst., vol. 3, pp. 2672–2680, Jul. 2014.

[17] J. Li, J. Jia, and D. Xu, ‘‘Unsupervised representation learning of
image-based plant disease with deep convolutional generative adversarial
networks,’’ in Proc. 37th Chin. Control Conf. (CCC), Jul. 2018, pp. 1–26.
[18] M. Mirza and S. Osindero, ‘‘Conditional generative adversarial nets,’’

2014, arXiv:1411.1784.

[19] M. Arjovsky, S. Chintala, and L. Bottou, ‘‘Wasserstein GAN,’’ 2017,

arXiv:1701.07875.

[20] I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. Courville,
‘‘Improved training of Wasserstein GANs,’’ in Proc. Adv. Neural Inf.
Process. Syst., 2017, pp. 5768–5778.

[21] X. Mao, Q. Li, H. Xie, R. Y. K. Lau, Z. Wang, and S. P. Smolley,
‘‘Least squares generative adversarial networks,’’ in Proc. IEEE Int. Conf.
Comput. Vis. (ICCV), Oct. 2017, pp. 2813–2821.

[22] J. Y. Zhu, T. Park, P. Isola, and A. A. Efros, ‘‘Unpaired image-to-image
translation using cycle-consistent adversarial networks,’’ in Proc. IEEE
Int. Conf. Comput. Vis., May 2017, pp. 2242–2251.

[23] T. Karras, S. Laine, and T. Aila, ‘‘A style-based generator architecture
for generative adversarial networks,’’ IEEE Trans. Pattern Anal. Mach.
Intell., vol. 43, no. 12, pp. 4217–4228, Dec. 2021.

[24] H. Zhang, I. Goodfellow, D. Metaxas, and A. Odena, ‘‘Self-attention
generative adversarial networks,’’ in Proc. 36th Int. Conf. Mach. Learn.,
Nov. 2019, pp. 12744–12753.

[25] A. Brock, J. Donahue, and K. Simonyan, ‘‘Large scale GAN training
for high fidelity natural image synthesis,’’ in Proc. 7th Int. Conf. Learn.
Represent., 2019, pp. 1–44.

[26] T. Karras, T. Aila, S. Laine, and J. Lehtinen, ‘‘Progressive growing of
GANs for improved quality, stability, and variation,’’ in Proc. 6th Int.
Conf. Learn. Represent., 2018, pp. 1–14.

[27] Y. Choi, M. Choi, M. Kim, J. W. Ha, S. Kim, and J. Choo,
‘‘Stargan: Unified generative adversarial networks for multi-domain
image-to-image translation,’’ in Proc. IEEE Comput. Soc. Conf. Comput.
Vis. Pattern Recognit., Apr. 2017, pp. 8789–8797.

[28] Z. Wang, Q. She, and T. E. Ward, ‘‘Generative adversarial networks
in computer vision: A survey and taxonomy,’’ ACM Comput. Surveys,
vol. 54, no. 2, pp. 1–38, Mar. 2022.

[29] J. Gui, Z. Sun, Y. Wen, D. Tao, and J. Ye, ‘‘A review on generative
adversarial networks: Algorithms, theory, and applications,’’ IEEE Trans.
Knowl. Data Eng., vol. 35, no. 4, pp. 3313–3332, Apr. 2023.

[30] A. Creswell, T. White, V. Dumoulin, K. Arulkumaran, B. Sengupta, and

#### A. A. Bharath, ‘‘Generative adversarial networks: An overview,’’ IEEE
Signal Process. Mag., vol. 35, no. 1, pp. 53–65, Jan. 2018.

[31] I. O. Gallegos, R. A. Rossi, J. Barrow, M. M. Tanjim, S. Kim,

#### F. Dernoncourt, T. Yu, R. Zhang, and N. K. Ahmed, ‘‘Bias and fairness in
large language models: A survey,’’ 2023, arXiv:2309.00770.

[32] H. Shi, Z. Xu, H. Wang, W. Qin, W. Wang, Y. Wang, Z. Wang,

#### S. Ebrahimi, and H. Wang, ‘‘Continual learning of large language models:
A comprehensive survey,’’ 2024, arXiv:2404.16789.

[33] Z. Zhou, X. Ning, K. Hong, T. Fu, J. Xu, S. Li, Y. Lou, L. Wang,

#### Z. Yuan, X. Li, S. Yan, G. Dai, X.-P. Zhang, Y. Dong, and Y. Wang,
‘‘A survey on efficient inference for large language models,’’ 2024,
arXiv:2404.14294.

[34] X. Fang, W. Xu, F. A. Tan, J. Zhang, Z. Hu, Y. Qi, S. Nickleach,

#### D. Socolinsky, S. Sengamedu, and C. Faloutsos, ‘‘Large language models
(LLMs) on tabular data: Prediction, generation, and understanding—A
survey,’’ arXiv:2402.17944, 2024.

[35] B. Chandra Das, M. Hadi Amini, and Y. Wu, ‘‘Security and privacy chal-

lenges of large language models: A survey,’’ 2024, arXiv:2402.00888.

[36] H. Jin, L. Hu, X. Li, P. Zhang, C. Chen, J. Zhuang, and H. Wang,
‘‘JailbreakZoo: Survey, landscapes, and horizons in jailbreaking large
language and vision-language models,’’ 2024, arXiv:2407.01599.
[37] L. Wu, Z. Zheng, Z. Qiu, H. Wang, H. Gu, T. Shen, C. Qin, C. Zhu, H.
Zhu, Q. Liu, H. Xiong, and E. Chen, ‘‘A survey on large language models
for recommendation,’’ 2023, arXiv:2305.19860.

[38] M. Akyash and H. Mardani Kamali, ‘‘Evolutionary large language models
for hardware security: A comparative survey,’’ 2024, arXiv:2404.16651.
[39] T. Bai, H. Liang, B. Wan, Y. Xu, X. Li, S. Li, L. Yang, B. Li, Y. Wang,

#### B. Cui, P. Huang, J. Shan, C. He, B. Yuan, and W. Zhang, ‘‘A survey of
multimodal large language model from a data-centric perspective,’’ 2024,
arXiv:2405.16640.

[40] H. Xiao, F. Zhou, X. Liu, T. Liu, Z. Li, X. Liu, and X. Huang, ‘‘A
comprehensive survey of large language models and multimodal large
language models in medicine,’’ 2024, arXiv:2405.08603.

[41] H. Zhou, C. Hu, Y. Yuan, Y. Cui, Y. Jin, C. Chen, H. Wu, D. Yuan, L. Jiang,

#### D. Wu, X. Liu, C. Zhang, X. Wang, and J. Liu, ‘‘Large language model
(LLM) for telecommunications: A comprehensive survey on principles,
key techniques, and opportunities,’’ 2024, arXiv:2405.10825.

[42] Y. Huang, K. Tang, M. Chen, and B. Wang, ‘‘A comprehensive survey on
evaluating large language model applications in the medical industry,’’
2024, arXiv:2404.15777.

[43] C. Qu, S. Dai, X. Wei, H. Cai, S. Wang, D. Yin, J. Xu, and
J.-R. Wen, ‘‘Tool learning with large language models: A survey,’’ 2024,
arXiv:2405.17935.

[44] L. Qin, Q. Chen, X. Feng, Y. Wu, Y. Zhang, Y. Li, M. Li, W. Che,
and P. S. Yu, ‘‘Large language models meet NLP: A survey,’’ 2024,
arXiv:2405.12819.

[45] Z. Zhang, Y. Sun, Z. Wang, Y. Nie, X. Ma, P. Sun, and R. Li, ‘‘Large
language models for mobility in transportation systems: A survey on
forecasting tasks,’’ 2024, arXiv:2405.02357.

VOLUME 12, 2024

188697

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[46] S. Kukreja, T. Kumar, A. Purohit, A. Dasgupta, and D. Guha, ‘‘A literature
survey on open source large language models,’’ in Proc. 7th Int. Conf.
Comput. Manage. Bus., vol. 2212, Jan. 2024, pp. 133–143.

[47] L. Qin, Q. Chen, Y. Zhou, Z. Chen, Y. Li, L. Liao, M. Li, W. Che, and

#### P. S. Yu, ‘‘Multilingual large language model: A survey of resources,
taxonomy and frontiers,’’ 2024, arXiv:2404.04925.

[48] S. Dai, C. Xu, S. Xu, L. Pang, Z. Dong, and J. Xu, ‘‘Bias and unfairness
in information retrieval systems: New challenges in the LLM era,’’ 2024,
arXiv:2404.11457.

[49] S. Yin, C. Fu, S. Zhao, K. Li, X. Sun, T. Xu, and E. Chen, ‘‘A survey on

multimodal large language models,’’ 2023, arXiv:2306.13549.

[50] Z. Zhang, X. Bo, C. Ma, R. Li, X. Chen, Q. Dai, J. Zhu, Z. Dong, and
J.-R. Wen, ‘‘A survey on the memory mechanism of large language model
based agents,’’ 2024, arXiv:2404.13501.

[51] S. Hu, T. Huang, F. Ilhan, S. Tekin, G. Liu, R. Kompella, and

#### L. Liu, ‘‘A survey on large language model-based game agents,’’ 2024,
arXiv:2404.02039.

[52] Z. Bai, P. Wang, T. Xiao, T. He, Z. Han, Z. Zhang, and M. Z. Shou,
‘‘Hallucination of multimodal large language models: A survey,’’ 2024,
arXiv:2404.18930.

[53] Y. Huang and J. Huang, ‘‘A survey on retrieval-augmented text generation

for large language models,’’ 2024, arXiv:2404.10981.

[54] J. Li, T. Tang, W. X. Zhao, J.-Y. Nie, and J.-R. Wen, ‘‘Pre-trained language
models for text generation: A survey,’’ ACM Comput. Surveys, vol. 56,
no. 9, pp. 1–39, Oct. 2024.

[55] Y. Liu, Y. Yao,

J.-F. Ton, X. Zhang, R. Guo, H. Cheng,

#### Y. Klochkov, M. F. Taufiq, and H. Li, ‘‘Trustworthy LLMs: A survey
and guideline for evaluating large language models’ alignment,’’ 2023,
arXiv:2308.05374.

[56] Y. Yao, J. Duan, K. Xu, Y. Cai, Z. Sun, and Y. Zhang, ‘‘A survey
on large language model (LLM) security and privacy: The good, the
bad, and the ugly,’’ High-Confidence Comput., vol. 4, no. 2, Jun. 2024,
Art. no. 100211.

[57] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi,

#### C. Wang, and Y. Wang, ‘‘A survey on evaluation of large language
models,’’ ACM Trans. Intell. Syst. Technol., vol. 15, no. 3, pp. 1–45, 2024.
[58] Y. Gao, Y. Xiong, X. Gao, K. Jia, J. Pan, Y. Bi, Y. Dai, J. Sun,

#### M. Wang, and H. Wang, ‘‘Retrieval-augmented generation for large
language models: A survey,’’ 2023, arXiv:2312.10997.

[59] S. Zhang, L. Dong, X. Li, S. Zhang, X. Sun, S. Wang, J. Li, R. Hu,

#### T. Zhang, F. Wu, and G. Wang, ‘‘Instruction tuning for large language
models: A survey,’’ 2023, arXiv:2308.10792.

[60] R. Hong, X. Pang, and C. Zhang, ‘‘Advances in reasoning by prompting
large language models: A survey,’’ Cybern. Intell., vol. 1, pp. 1–18,
Apr. 2024.

[61] B. Yan, K. Li, M. Xu, Y. Dong, Y. Zhang, Z. Ren, and X. Cheng, ‘‘On
protecting the data privacy of large language models (LLMs): A survey,’’
2024, arXiv:2403.05156.

[62] Y. Cao, H. Zhao, Y. Cheng, T. Shu, Y. Chen, G. Liu, G. Liang,

#### J. Zhao, J. Yan, and Y. Li, ‘‘Survey on large language model-enhanced
reinforcement
taxonomy, and methods,’’ 2024,
arXiv:2404.00282.

learning: Concept,

[63] X. Liu, P. Xu, J. Wu, J. Yuan, Y. Yang, Y. Zhou, F. Liu, T. Guan,

#### H. Wang, T. Yu, J. McAuley, W. Ai, and F. Huang, ‘‘Large language
models and causal inference in collaboration: A comprehensive survey,’’
2024, arXiv:2403.09606.

[64] A. Esmradi, D. W. Yip, and C. F. Chan, ‘‘A comprehensive survey
of attack techniques, implementation, and mitigation strategies in large
language models,’’ in Proc. Int. Conf. Ubiquitous Secur., 2023, pp. 76–95.
[65] A. G. Chowdhury, M. M. Islam, V. Kumar, F. H. Shezan, V. Kumar,

#### V. Jain, and A. Chadha, ‘‘Breaking down the defenses: A comparative
survey of attacks on large language models,’’ 2024, arXiv:2403.04786.

[66] Z. Sun, ‘‘A short survey of viewing large language models in legal

aspect,’’ 2023, arXiv:2303.09136.

[67] H. Zhao, H. Chen, F. Yang, N. Liu, H. Deng, H. Cai, S. Wang, D. Yin,
and M. Du, ‘‘Explainability for large language models: A survey,’’ ACM
Trans. Intell. Syst. Technol., vol. 15, no. 2, pp. 1–38, Apr. 2024.

[68] Y. Zhu, H. Yuan, S. Wang, J. Liu, W. Liu, C. Deng, H. Chen, Z. Liu,

#### Z. Dou, and J.-R. Wen, ‘‘Large language models for information retrieval:
A survey,’’ 2023, arXiv:2308.07107.

[69] J. Li, Y. Liu, C. Liu, L. Shi, X. Ren, Y. Zheng, Y. Liu, and Y. Xue,
‘‘A cross-language investigation into jailbreak attacks in large language
models,’’ 2024, arXiv:2401.16765.

[70] Z. Xi et al., ‘‘The rise and potential of large language model based agents:

A survey,’’ 2023, arXiv:2309.07864.

[71] L. Huang, W. Yu, W. Ma, W. Zhong, Z. Feng, H. Wang, Q. Chen, W. Peng,

#### X. Feng, B. Qin, and T. Liu, ‘‘A survey on hallucination in large language
models: Principles, taxonomy, challenges, and open questions,’’ 2023,
arXiv:2311.05232.

[72] E. Shayegani, M. Abdullah Al Mamun, Y. Fu, P. Zaree, Y. Dong, and

#### N. Abu-Ghazaleh, ‘‘Survey of vulnerabilities in large language models
revealed by adversarial attacks,’’ 2023, arXiv:2310.10844.

[73] H. Zhang, H. Song, S. Li, M. Zhou, and D. Song, ‘‘A survey of
controllable text generation using transformer-based pre-trained language
models,’’ ACM Comput. Surveys, vol. 56, no. 3, pp. 1–37, Mar. 2024.
[74] B. Min, H. Ross, E. Sulem, A. P. B. Veyseh, T. H. Nguyen, O. Sainz,

#### E. Agirre, I. Heintz, and D. Roth, ‘‘Recent advances in natural language
processing via large pre-trained language models: A survey,’’ ACM
Comput. Surveys, vol. 56, no. 2, pp. 1–40, Feb. 2024.

[75] Y. Zhang, Y. Li, L. Cui, D. Cai, L. Liu, T. Fu, X. Huang, E. Zhao, Y. Zhang,

#### Y. Chen, L. Wang, A. Tuan Luu, W. Bi, F. Shi, and S. Shi, ‘‘Siren’s song
in the AI ocean: A survey on hallucination in large language models,’’
2023, arXiv:2309.01219.

[76] X. Zhu, J. Li, Y. Liu, C. Ma, and W. Wang, ‘‘A survey on model
compression for large language models,’’ 2023, arXiv:2308.07633.
[77] L. Hu, Z. Liu, Z. Zhao, L. Hou, L. Nie, and J. Li, ‘‘A survey of knowledge
enhanced pre-trained language models,’’ IEEE Trans. Knowl. Data Eng.,
vol. 36, no. 4, pp. 1413–1430, Apr. 2024.

[78] B. Wang, Q. Xie, J. Pei, Z. Chen, P. Tiwari, Z. Li, and J. Fu, ‘‘Pre-trained
language models in biomedical domain: A systematic survey,’’ ACM
Comput. Surveys, vol. 56, no. 3, pp. 1–52, Mar. 2024.

[79] J. Huang and K. Chen-Chuan Chang, ‘‘Towards reasoning in large

language models: A survey,’’ 2022, arXiv:2212.10403.

[80] E. Kasneci, K. Seßler, S. Küchemann, M. Bannert, D. Dementieva,

#### F. Fischer, U. Gasser, G. Groh, S. Günnemann, and E. Hüllermeier,
‘‘ChatGPT for good? On opportunities and challenges of
large
language models for education,’’ Learn. Individual Differences, vol. 103,
Apr. 2023, Art. no. 102274.

[81] W. X. Zhao et al., ‘‘A survey of large language models,’’ 2023,

arXiv:2303.18223.

[82] G. Mialon, R. Dessì, M. Lomeli, C. Nalmpantis, R. Pasunuru,

#### R. Raileanu, B. Rozière, T. Schick, J. Dwivedi-Yu, A. Celikyilmaz,

#### E. Grave, Y. LeCun, and T. Scialom, ‘‘Augmented language models: A
survey,’’ 2023, arXiv:2302.07842.

[83] K. S. Kalyan, A. Rajasekharan, and S. Sangeetha, ‘‘AMMU: A survey of
transformer-based biomedical pretrained language models,’’ J. Biomed.
Informat., vol. 126, Feb. 2022, Art. no. 103982.

[84] K. Subramanyam Kalyan, A. Rajasekharan, and S. Sangeetha, ‘‘AMMUS
: A survey of transformer-based pretrained models in natural language
processing,’’ 2021, arXiv:2108.05542.

[85] M. Zaib, Q. Z. Sheng, and W. Emma Zhang, ‘‘A short survey of
pre-trained language models for conversational AI—A new age in NLP,’’
in Proc. Australas. Comput. Sci. Week Multiconference, Feb. 2020,
pp. 1–4.

[86] N. Houlsby, ‘‘Parameter-efficient transfer learning for NLP,’’ in Proc. Int.

Conf. Mach. Learn., 2019, pp. 2790–2799.

[87] J. He, C. Zhou, X. Ma, T. Berg-Kirkpatrick, and G. Neubig,
‘‘Towards a unified view of parameter-efficient transfer learning,’’ 2021,
arXiv:2110.04366.

[88] Y. Zhu, J. Feng, C. Zhao, M. Wang, and L. Li, ‘‘Counter-interference
adapter for multilingual machine translation,’’ 2021, arXiv:2104.08154.
[89] T. Lei, J. Bai, S. Brahma, J. Ainslie, K. Lee, Y. Zhou, N. Du,

#### V. Y. Zhao, Y. Wu, B. Li, Y. Zhang, and M.-W. Chang, ‘‘Conditional
adapters: Parameter-efficient transfer learning with fast inference,’’ 2023,
arXiv:2304.04947.

[90] J. Pfeiffer, A. Kamath, A. Rucklé, K. Cho, and I. Gurevych,
‘‘AdapterFusion: Non-destructive task composition for transfer learning,’’
2020, arXiv:2005.00247.

[91] Y. Wang, S. Agarwal, S. Mukherjee, X. Liu, J. Gao, A. Hassan Awadallah,
and J. Gao, ‘‘AdaMix: Mixture-of-Adaptations for parameter-efficient
model tuning,’’ 2022, arXiv:2205.12410.

[92] H. Zhao, J. Fu, and Z. He, ‘‘Prototype-based HyperAdapter for sample-

efficient multi-task tuning,’’ 2023, arXiv:2310.11670.

188698

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[93] A. Chronopoulou, M. E. Peters, A. Fraser, and J. Dodge, ‘‘AdapterSoup:
Weight averaging to improve generalization of pretrained language
models,’’ 2023, arXiv:2302.07027.

[94] S. He, R.-Z. Fan, L. Ding, L. Shen, T. Zhou, and D. Tao, ‘‘MerA: Merging
pretrained adapters for few-shot learning,’’ 2023, arXiv:2308.15982.
[95] R. Karimi Mahabadi, S. Ruder, M. Dehghani, and J. Henderson,
‘‘Parameter-efficient multi-task fine-tuning for transformers via shared
hypernetworks,’’ 2021, arXiv:2106.04489.

[96] X. Lisa Li and P. Liang, ‘‘Prefix-tuning: Optimizing continuous prompts

for generation,’’ 2021, arXiv:2101.00190.

[97] J. Li, W. Aitken, R. Bhambhoria, and X. Zhu, ‘‘Prefix propagation:
Parameter-efficient tuning for long sequences,’’ 2023, arXiv:2305.12086.
[98] X. Liu, K. Ji, Y. Fu, W. Lam Tam, Z. Du, Z. Yang, and J. Tang, ‘‘P-tuning
v2: Prompt tuning can be comparable to fine-tuning universally across
scales and tasks,’’ 2021, arXiv:2110.07602.

[99] Z.-R. Zhang, C. Tan, H. Xu, C. Wang, J. Huang, and S. Huang,
‘‘Towards adaptive prefix tuning for parameter-efficient language model
fine-tuning,’’ 2023, arXiv:2305.15212.

[100] X. Liu, Y. Zheng, Z. Du, M. Ding, Y. Qian, Z. Yang, and J. Tang, ‘‘GPT

understands, too,’’ 2021, arXiv:2103.10385.

[101] B. Lester, R. Al-Rfou, and N. Constant, ‘‘The power of scale for

parameter-efficient prompt tuning,’’ 2021, arXiv:2104.08691.

[102] F. Ma, C. Zhang, L. Ren, J. Wang, Q. Wang, W. Wu, X. Quan, and

#### D. Song, ‘‘XPrompt: Exploring the extreme of prompt tuning,’’ 2022,
arXiv:2210.04457.

[103] Z. Wu, S. Wang, J. Gu, R. Hou, Y. Dong, V. G. V. Vydiswaran, and

#### H. Ma, ‘‘IDPG: An instance-dependent prompt generation method,’’
2022, arXiv:2204.04497.

[104] X. Liu, T. Sun, X. Huang, and X. Qiu, ‘‘Late prompt tuning: A late prompt

could be better than many prompts,’’ 2022, arXiv:2210.11292.

[105] W. Zhu and M. Tan, ‘‘SPT: Learning to selectively insert prompts for
better prompt tuning,’’ in Proc. Conf. Empirical Methods Natural Lang.
Process., 2023, pp. 11862–11878.

[106] Q. Wang, Y. Mao, J. Wang, H. Yu, S. Nie, S. Wang, F. Feng, L. Huang,

#### X. Quan, and Z. Xu, ‘‘Aprompt: Attention prompt tuning for efficient
adaptation of pre-trained language models,’’ in Proc. Conf. Empirical
Methods Natural Lang. Process., 2023, pp. 9147–9160.

[107] T. Vu, B. Lester, N. Constant, R. Al-Rfou, and D. Cer, ‘‘SPoT:
Better frozen model adaptation through soft prompt transfer,’’ 2021,
arXiv:2110.07904.

[108] Y. Su, X. Wang, Y. Qin, C.-M. Chan, Y. Lin, H. Wang, K. Wen, Z. Liu,

#### P. Li, J. Li, L. Hou, M. Sun, and J. Zhou, ‘‘On transferability of prompt
tuning for natural language processing,’’ 2021, arXiv:2111.06719.
[109] J. Wu, T. Yu, R. Wang, Z. Song, R. Zhang, H. Zhao, C. Lu, S. Li, and

#### R. Henao, ‘‘InfoPrompt: Information-theoretic soft prompt tuning for
natural language understanding,’’ 2023, arXiv:2306.04933.

[110] L. Chen, H. Huang, and M. Cheng, ‘‘PTP: Boosting stability and
tuning with perturbation-based regularizer,’’

performance of prompt
2023, arXiv:2305.02423.

[111] Y. Qin, X. Wang, Y. Su, Y. Lin, N. Ding, J. Yi, W. Chen, Z. Liu, J. Li,

#### L. Hou, P. Li, M. Sun, and J. Zhou, ‘‘Exploring universal intrinsic task
subspace via prompt tuning,’’ 2021, arXiv:2110.07867.

[112] J.-Y. Choi, J. Kim, J.-H. Park, W.-L. Mok, and S. Lee, ‘‘Smop: Towards
efficient and effective prompt tuning with sparse mixture-of-prompts,’’
in Proc. Conf. Empirical Methods Natural Lang. Process., 2023,
pp. 14306–14316.

[113] Z. Shi and A. Lipani, ‘‘DePT: Decomposed prompt tuning for parameter-

efficient fine-tuning,’’ 2023, arXiv:2309.05173.

[114] H. Liu, D. Tam, M. Muqeeth, J. Mohta, T. Huang, M. Bansal, and

#### C. A. Raffel, ‘‘Few-shot parameter-efficient fine-tuning is better and
cheaper than in-context learning,’’ in Proc. Adv. Neural Inf. Process. Syst.,
vol. 35, 2022, pp. 1950–1965.

[115] T. Zadouri, A. Üstun, A. Ahmadian, B. Ermis, A. Locatelli, and

#### S. Hooker, ‘‘Pushing mixture of experts to the limit: Extremely parameter
efficient MoE for instruction tuning,’’ 2023, arXiv:2309.05444.
[116] D. Lian, D. Zhou, J. Feng, and X. Wang, ‘‘Scaling & shifting your
features: A new baseline for efficient model tuning,’’ in Proc. Adv. Neural
Inf. Process. Syst., vol. 35, 2022, pp. 109–123.

[117] X. Lu, F. Brahman, P. West, J. Jang, K. Chandu, A. Ravichander, L. Qin,

#### P. Ammanabrolu, L. Jiang, S. Ramnath, N. Dziri, J. Fisher, B. Yuchen
Lin, S. Hallinan, X. Ren, S. Welleck, and Y. Choi, ‘‘Inference-time policy
adapters (IPA): Tailoring extreme-scale LMs without fine-tuning,’’ 2023,
arXiv:2305.15065.

[118] D. Guo, A. M. Rush, and Y. Kim, ‘‘Parameter-efficient transfer learning

with diff pruning,’’ 2020, arXiv:2012.07463.

[119] N. Lawton, A. Kumar, G. Thattai, A. Galstyan, and G. Ver Steeg, ‘‘Neural
architecture search for parameter-efficient fine-tuning of large pre-trained
language models,’’ 2023, arXiv:2305.16597.

[120] B. Liao, Y. Meng, and C. Monz, ‘‘Parameter-efficient fine-tuning without

introducing new latency,’’ 2023, arXiv:2305.16742.

[121] Y. L. Sung, V. Nair, and C. A. Raffel, ‘‘Training neural networks with
fixed sparse masks,’’ in Proc. Neural Inf. Process. Syst. (NIPS), 2021,
pp. 24193–24205.

[122] S. Snigdha Sarathi Das, R. Haoran Zhang, P. Shi, W. Yin, and R. Zhang,
‘‘Unified low-resource sequence labeling by sample-aware dynamic
sparse finetuning,’’ 2023, arXiv:2311.03748.

[123] A. Ansell, E. Maria Ponti, A. Korhonen, and I. Vulic, ‘‘Composable sparse
fine-tuning for cross-lingual transfer,’’ 2021, arXiv:2110.07560.
[124] Z. Fu, H. Yang, A. M.-C. So, W. Lam, L. Bing, and N. Collier, ‘‘On
the effectiveness of parameter-efficient fine-tuning,’’ in Proc. AAAI Conf.
Artif. Intell., vol. 37, 2023, pp. 12799–12807.

[125] R. Xu, F. Luo, Z. Zhang, C. Tan, B. Chang, S. Huang, and

#### F. Huang, ‘‘Raise a child in large language model: Towards effective and
generalizable fine-tuning,’’ 2021, arXiv:2109.05687.

[126] D. Vucetic, M. Tayaranian, M. Ziaeefard, J. J. Clark, B. H. Meyer, and

#### W. J. Gross, ‘‘Efficient fine-tuning of BERT models on the edge,’’ in Proc.
IEEE Int. Symp. Circuits Syst. (ISCAS), Jun. 2022, pp. 1838–1842.
[127] E. Ben Zaken, S. Ravfogel, and Y. Goldberg, ‘‘BitFit: Simple parameter-
efficient fine-tuning for transformer-based masked language-models,’’
2021, arXiv:2106.10199.

[128] M. Gheini, X. Ren, and J. May, ‘‘Cross-attention is all you need:
Adapting pretrained transformers for machine translation,’’ 2021,
arXiv:2104.08771.

[129] A. Aghajanyan, L. Zettlemoyer, and S. Gupta, ‘‘Intrinsic dimensionality
language model fine-tuning,’’ 2020,

explains the effectiveness of
arXiv:2012.13255.

[130] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and

#### W. Chen, ‘‘LoRA: Low-rank adaptation of large language models,’’ 2021,
arXiv:2106.09685.

[131] R. K. Mahabadi, J. Henderson, and S. Ruder, ‘‘Compacter: Efficient low-
rank hypercomplex adapter layers,’’ in Proc. Adv. Neural Inf. Process.
Syst., vol. 34, 2021, pp. 1022–1035.

[132] A. Edalati, M. Tahaei, I. Kobyzev, V. Partovi Nia, J. J. Clark, and

#### M. Rezagholizadeh, ‘‘KronA: Parameter efficient tuning with Kronecker
adapter,’’ 2022, arXiv:2212.10650.

[133] X. He, C. Li, P. Zhang, J. Yang, and X. E. Wang, ‘‘Parameter-efficient
model adaptation for vision transformers,’’ Proc. AAAI Conf. Artif. Intell.,
vol. 37, no. 1, pp. 817–825, Jun. 2023.

[134] D. J. Kopiczko, T. Blankevoort, and Y. M. Asano, ‘‘VeRA: Vector-based

random matrix adaptation,’’ 2023, arXiv:2310.11454.

[135] S.-Y. Liu, C.-Y. Wang, H. Yin, P. Molchanov, Y.-C. F. Wang, K.-T. Cheng,
and M.-H. Chen, ‘‘DoRA: Weight-decomposed low-rank adaptation,’’
2024, arXiv:2402.09353.

[136] M. Valipour, M. Rezagholizadeh, I. Kobyzev, and A. Ghodsi, ‘‘DyLoRA:
Parameter efficient tuning of pre-trained models using dynamic search-
free low-rank adaptation,’’ 2022, arXiv:2210.07558.

[137] Q. Zhang, M. Chen, A. Bukharin, N. Karampatziakis, P. He, Y. Cheng,

#### W. Chen, and T. Zhao, ‘‘AdaLoRA: Adaptive budget allocation for
parameter-efficient fine-tuning,’’ 2023, arXiv:2303.10512.

[138] N. Ding, X. Lv, Q. Wang, Y. Chen, B. Zhou, Z. Liu, and M. Sun,
‘‘Sparse low-rank adaptation of pre-trained language models,’’ 2023,
arXiv:2311.11696.

[139] S. Haobo, H. Zhao, S. Majumder, and T. Lin, ‘‘Increasing model capacity
for free: A simple strategy for parameter efficient fine-tuning,’’ in Proc.
12th Int. Conf. Learn. Represent., 2023, pp. 1–24.

[140] R. Zhang, R. Qiang, S. Ashish Somayajula, and P. Xie, ‘‘AutoLoRA:
Automatically tuning matrix ranks in low-rank adaptation based on meta
learning,’’ 2024, arXiv:2403.09113.

[141] A. X. Yang, M. Robeyns, X. Wang, and L. Aitchison, ‘‘Bayesian low-rank
adaptation for large language models,’’ 2023, arXiv:2308.13111.
[142] Y. Lin, X. Ma, X. Chu, Y. Jin, Z. Yang, Y. Wang, and H. Mei,
‘‘LoRA dropout as a sparsity regularizer for overfitting control,’’ 2024,
arXiv:2404.09610.

[143] X. Meng, D. Dai, W. Luo, Z. Yang, S. Wu, X. Wang, P. Wang, Q. Dong,

#### L. Chen, and Z. Sui, ‘‘PeriodicLoRA: Breaking the low-rank bottleneck
in LoRa optimization,’’ 2024, arXiv:2402.16141.

VOLUME 12, 2024

188699

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[144] S. Hayou, N. Ghosh, and B. Yu, ‘‘LoRA+: Efficient low rank adaptation

of large models,’’ 2024, arXiv:2402.12354.

[145] Y. Chen, S. Qian, H. Tang, X. Lai, Z. Liu, S. Han, and J. Jia, ‘‘LongLoRA:
Efficient fine-tuning of long-context large language models,’’ 2023,
arXiv:2309.12307.

[146] C. Huang, Q. Liu, B. Yuchen Lin, T. Pang, C. Du, and M. Lin, ‘‘LoRaHub:
Efficient cross-task generalization via dynamic LoRa composition,’’
2023, arXiv:2307.13269.

[147] Q. Liu, X. Wu, X. Zhao, Y. Zhu, D. Xu, F. Tian, and Y. Zheng, ‘‘When
MOE meets LLMs: Parameter efficient fine-tuning for multi-task medical
applications,’’ 2023, arXiv:2310.18339.

[148] W. Feng, C. Hao, Y. Zhang, Y. Han, and H. Wang, ‘‘Mixture-of-LoRAs:
large language models,’’ 2024,

An efficient multitask tuning for
arXiv:2403.03432.

[149] X. Wu, S. Huang, and F. Wei, ‘‘Mixture of LoRa experts,’’ 2024,

arXiv:2404.13628.

[150] D. Li, Y. Ma, N. Wang, Z. Ye, Z. Cheng, Y. Tang, Y. Zhang,

#### L. Duan, J. Zuo, C. Yang, and M. Tang, ‘‘MixLoRA: Enhancing large
language models fine-tuning with LoRA-based mixture of experts,’’
2024, arXiv:2404.15159.

[151] Y. Mao, L. Mathias, R. Hou, A. Almahairi, H. Ma, J. Han, W.-T. Yih,
and M. Khabsa, ‘‘UniPELT: A unified framework for parameter-efficient
language model tuning,’’ 2021, arXiv:2110.07577.

[152] J. Chen, A. Zhang, X. Shi, M. Li, A. Smola, and D. Yang, ‘‘Parameter-

efficient fine-tuning design spaces,’’ 2023, arXiv:2301.01821.

[153] Y. Zhang, K. Zhou, and Z. Liu. (2022). Neural Prompt Search. [Online].

Available: https://arxiv.org/abs/2206.04673

[154] S. Zhong, J. Mo, and Z. Liu, ‘‘AutoPET challenge 2022: Automatic
segmentation of whole-body tumor lesion based on deep learning and
FDG PET/CT,’’ 2022, arXiv:2209.01212.

[155] Z. Hu, L. Wang, Y. Lan, W. Xu, E.-P. Lim, L. Bing, X. Xu, S. Poria, and

#### R. K.-W. Lee, ‘‘LLM-adapters: An adapter family for parameter-efficient
fine-tuning of large language models,’’ 2023, arXiv:2304.01933.
[156] S. Hu, Z. Zhang, N. Ding, Y. Wang, Y. Wang, Z. Liu, and

#### M. Sun, ‘‘Sparse structure search for parameter-efficient tuning,’’ 2022,
arXiv:2206.07382.

[157] H. Liu, C. Li, Q. Wu, and Y. J. Lee, ‘‘Visual instruction tuning,’’ 2023,

arXiv:2304.08485.

[158] P. Lu, S. Mishra, T. Xia, L. Qiu, K.-W. Chang, S.-C. Zhu, O. Tafjord,

#### P. Clark, and A. Kalyan, ‘‘Learn to explain: Multimodal reasoning via
thought chains for science question answering,’’ 2022, arXiv:2209.09513.
[159] Y.-L. Sung, J. Cho, and M. Bansal, ‘‘VL-adapter: Parameter-efficient
2021,

vision-and-language

tasks,’’

for

transfer
learning
arXiv:2112.06825.

[160] Y. Cui, W. Che, T. Liu, B. Qin, and Z. Yang, ‘‘Pre-training with whole
word masking for Chinese BERT,’’ IEEE/ACM Trans. Audio, Speech,
Language Process., vol. 29, no. 1, pp. 3504–3514, Apr. 2021.

[161] Y. Cui, W. Che, T. Liu, B. Qin, and Z. Yang, ‘‘Pre-training with whole

word masking for Chinese BERT,’’ 2019, arXiv:1906.08101.

[162] M. Joshi, D. Chen, Y. Liu, D. S. Weld, L. Zettlemoyer, and

#### O. Levy, ‘‘SpanBERT: Improving pre-training by representing and
predicting spans,’’ Trans. Assoc. Comput. Linguistics, vol. 8, pp. 64–77,
Dec. 2020.

[163] V. Sanh, L. Debut, J. Chaumond, and T. Wolf,

‘‘DistilBERT, a
distilled version of BERT: Smaller, faster, cheaper and lighter,’’ 2019,
arXiv:1910.01108.

[164] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis,

#### L. Zettlemoyer, and V. Stoyanov, ‘‘RoBERTa: A robustly optimized
BERT pretraining approach,’’ 2019, arXiv:1907.11692.

[165] X. Jiao, Y. Yin, L. Shang, X. Jiang, X. Chen, L. Li, F. Wang, and Q. Liu,
‘‘TinyBERT: Distilling BERT for natural language understanding,’’ 2019,
arXiv:1909.10351.

[166] L. Harold Li, M. Yatskar, D. Yin, C.-J. Hsieh, and K.-W. Chang,
‘‘VisualBERT: A simple and performant baseline for vision and
language,’’ 2019, arXiv:1908.03557.

[167] Y. Cui, W. Che, T. Liu, B. Qin, S. Wang, and G. Hu, ‘‘Revisiting
pre-trained models for Chinese natural language processing,’’ 2020,
arXiv:2004.13922.

[168] H. Bao, L. Dong, S. Piao, and F. Wei, ‘‘BEiT: BERT pre-training of image

transformers,’’ 2021, arXiv:2106.08254.

[169] Z. Peng, L. Dong, H. Bao, Q. Ye, and F. Wei,

‘‘BEiT v2:
Masked image modeling with vector-quantized visual tokenizers,’’ 2022,
arXiv:2208.06366.

[170] W. Wang, H. Bao, L. Dong, J. Bjorck, Z. Peng, Q. Liu, K. Aggarwal,

#### O. K. Mohammed, S. Singhal, S. Som, and F. Wei, ‘‘Image as a foreign
language: BEiT pretraining for all vision and vision-language tasks,’’
2022, arXiv:2208.10442.

[171] A. Vahdat, E. Andriyash, and W. Macready, ‘‘Dvae: Discrete variational
autoencoders with relaxed Boltzmann priors,’’ in Proc. Adv. Neural Inf.
Process. Syst., vol. 31, 2018, pp. 1–24.

[172] Z. Xu, ‘‘RoBERTa-wwm-ext fine-tuning for Chinese text classification,’’

2021, arXiv:2103.00492.

[173] Y. Sun, S. Wang, Y. Li, S. Feng, H. Tian, H. Wu, and H. Wang,
‘‘ERNIE 2.0: A continual pre-training framework for language under-
standing,’’ in Proc. AAAI Conf. Artif. Intell., 2020, vol. 34, no. 5,
pp. 8968–8975.

[174] Y. Sun et al., ‘‘ERNIE 3.0: Large-scale knowledge enhanced pre-training

for language understanding and generation,’’ 2021, arXiv:2107.02137.

[175] F. Yu, J. Tang, W. Yin, Y. Sun, H. Tian, H. Wu, and H. Wang, ‘‘ERNIE-
ViL: Knowledge enhanced vision-language representations through scene
graphs,’’ Proc. AAAI Conf. Artif. Intell., vol. 35, no. 4, pp. 3208–3216,
May 2021.

[176] B. Shan, W. Yin, Y. Sun, H. Tian, H. Wu, and H. Wang, ‘‘ERNIE-ViL
2.0: Multi-view contrastive learning for image-text pre-training,’’ 2022,
arXiv:2209.15270.

[177] K. Clark, M.-T. Luong, Q. V. Le, and C. D. Manning, ‘‘ELECTRA:
Pre-training text encoders as discriminators rather than generators,’’ 2020,
arXiv:2003.10555.

[178] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,

#### S. Ozair, A. Courville, and Y. Bengio, ‘‘Generative adversarial networks,’’
Commun. ACM, vol. 63, no. 11, pp. 139–144, 2020.

[179] P. He, X. Liu, J. Gao, and W. Chen, ‘‘DeBERTa: Decoding-enhanced

BERT with disentangled attention,’’ 2020, arXiv:2006.03654.

[180] Z. Dai, Z. Yang, Y. Yang, J. Carbonell, Q. V. Le, and R. Salakhutdinov,
‘‘Transformer-XL: Attentive language models beyond a fixed-length
context,’’ 2019, arXiv:1901.02860.

[181] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, and

#### Q. V. Le, ‘‘Xlnet: Generalized autoregressive pretraining for language
understanding,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019,
pp. 1–24.

[182] Y. Zhu, R. Kiros, R. Zemel, R. Salakhutdinov, R. Urtasun, A. Torralba,
and S. Fidler, ‘‘Aligning books and movies: Towards story-like visual
explanations by watching movies and reading books,’’ in Proc. IEEE Int.
Conf. Comput. Vis. (ICCV), Dec. 2015, pp. 19–27.

[183] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever,
‘‘Language models are unsupervised multitask learners,’’ OpenAI blog,
vol. 1, no. 8, p. 9, 2019.

[184] B. McCann, N. Shirish Keskar, C. Xiong, and R. Socher, ‘‘The natural
language decathlon: Multitask learning as question answering,’’ 2018,
arXiv:1806.08730.

[185] T. B. Brown, ‘‘Language models are few-shot

learners,’’ in Proc.

NeurIPS, 2020, pp. 1877–1901.

[186] C. Finn, P. Abbeel, and S. Levine, ‘‘Model-agnostic meta-learning for
fast adaptation of deep networks,’’ in Proc. 34th Int. Conf. Mach. Learn.,
vol. 70, Aug. 2017, pp. 1126–1135.

[187] (2022). Commoncrawl. [Online]. Available: https://commoncrawl.org/
[188] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,

#### C. Zhang, S. Agarwal, K. Slama, A. Ray, and J. Schulman, ‘‘Training
language models to follow instructions with human feedback,’’ in Proc.
Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 27730–27744.
[189] (2022). Chatgpt. [Online]. Available: https://openai.com/chatgpt
[190] (2023).

Available:

[Online].

Report.

Gpt-4

Technical
https://arxiv.org/abs/2303.08774

[191] S. Black, L. Gao, P. Wang, C. Leahy, and S. R. Biderman.
(2021). Gpt-NEO: Large Scale Autoregressive Language Modeling
With Mesh-Tensorflow. [Online]. Available: https://api.semanticscholar.
org/CorpusID

[192] Z. Hu, Y. Dong, K. Wang, K.-W. Chang, and Y. Sun, ‘‘GPT-GNN:
Generative pre-training of graph neural networks,’’ in Proc. 26th
ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, Aug. 2020,
pp. 1857–1867.

[193] A. Komatsuzaki.

[Online]. Available:
06/04/gpt-j/

(2021). GPT-J-6B: 6B Jax-Based Transformer.
https://arankomatsuzaki.wordpress.com/2021/

[194] C. Huebner.

(2023). Mesh Transformer JAX.

[Online]. Available:

https://www.eleuther.ai/artifacts/mtj

188700

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[195] S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Golding,

#### H. He, C. Leahy, K. McDonell, J. Phang, M. Pieler, U. Sai Prashanth,

#### S. Purohit, L. Reynolds, J. Tow, B. Wang, and S. Weinbach,
‘‘GPT-NeoX-20B: An open-source autoregressive language model,’’
2022, arXiv:2204.06745.

[196] Microsoft.

(2022). Deepspeed is a Deep Learning Optimization
Library That Makes Distributed Training and Inference Easy, Effi-
cient, and Effective. [Online]. Available: https://github.com/microsoft/
DeepSpeed

[197] Y. Zhang, S. Sun, M. Galley, Y.-C. Chen, C. Brockett, X. Gao, J. Gao,

#### J. Liu, and B. Dolan, ‘‘DialoGPT: Large-scale generative pre-training for
conversational response generation,’’ 2019, arXiv:1911.00536.

[198] Google. (2022). Introducing Pathways: A Next-generation AI Architec-
ture. [Online]. Available: https://blog.google/technology/ai/introducing-
pathways-next-generation-ai-architecture/

[199] (2022). Pathways Language Model (palm): Scaling to 540 Billion
[Online]. Available:

for Breakthrough Performance.

Parameters
https://blog.research.google/2022/04/pathways-language-model-palm-
scaling-to.html
Shazeer,
arXiv:2002.05202.

‘‘GLU variants

transformer,’’

[200] N.

improve

2020,

[201] J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu, ‘‘RoFormer:
Enhanced transformer with rotary position embedding,’’ 2021,
arXiv:2104.09864.

[202] D. Driess et al., ‘‘PaLM-E: An embodied multimodal language model,’’

2023, arXiv:2303.03378.

[203] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, ‘‘ImageNet:
A large-scale hierarchical image database,’’ in Proc. CVPR, Jun. 2009,
pp. 248–255.

[204] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, and

#### C. L. Zitnick, ‘‘Microsoft COCO: Common objects in context,’’ in Proc.
ECCV, vol. 14, 2014, pp. 740–755.

[205] R. Krishna, Y. Zhu, O. Groth, J. Johnson, K. Hata, J. Kravitz, S. Chen,

#### Y. Kalantidis, L.-J. Li, D. A. Shamma, M. S. Bernstein, and L. Fei-Fei,
‘‘Visual genome: Connecting language and vision using crowdsourced
dense image annotations,’’ Int. J. Comput. Vis., vol. 123, no. 1, pp. 32–73,
May 2017.

[206] M. Dehghani, J. Djolonga, B. Mustafa, P. Padlewski, J. Heek, J. Gilmer,

#### A. P. Steiner, M. Caron, R. Geirhos, and I. Alabdulmohsin, ‘‘Scaling
vision transformers to 22 billion parameters,’’ in Proc. Int. Conf.
Mach. Learn., 2023, pp. 7480–7512.

[207] H. Mehta, A. Thakurta, A. Kurakin, and A. Cutkosky, ‘‘Large scale
transfer learning for differentially private image classification,’’ 2022,
arXiv:2205.02973.

[208] S. Huang, L. Dong, W. Wang, Y. Hao, S. Singhal, S. Ma, T. Lv,

#### L. Cui, O. Khan Mohammed, B. Patra, Q. Liu, K. Aggarwal, Z. Chi,

#### J. Bjorck, V. Chaudhary, S. Som, X. Song, and F. Wei, ‘‘Language is
not all you need: Aligning perception with language models,’’ 2023,
arXiv:2302.14045.

[209] A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski,

#### V. Ramasesh, A. Slone, C. Anil, I. Schlag, and T. Gutman-Solo, ‘‘Solving
quantitative reasoning problems with language models,’’ in Proc. Adv.
Neural Inf. Process. Syst., vol. 35, 2022, pp. 3843–3857.

[210] X. Chen et al., ‘‘PaLI: A jointly-scaled multilingual language-image

[218] H. Wang, S. Ma, S. Huang, L. Dong, W. Wang, Z. Peng, Y. Wu, P. Bajaj,

#### S. Singhal, A. Benhaim, B. Patra, Z. Liu, V. Chaudhary, X. Song, and

#### F. Wei, ‘‘Foundation transformers,’’ 2022, arXiv:2210.06423.

[219] (2023). Nvidia Nemo2023. [Online]. Available: https://docs.nvidia.com/
deeplearning/nemo/user-guide/docs/en/main/nlp/megatron.html
[220] M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and

#### B. Catanzaro, ‘‘Megatron-LM: Training multi-billion parameter language
models using model parallelism,’’ 2019, arXiv:1909.08053.

[221] D. Narayanan, ‘‘Efficient large-scale language model training on GPU

clusters using Megatron-lm,’’ in Proc. IEEE SC, Nov. 2021, pp. 1–15.

[222] V. A. Korthikanti, J. Casper, S. Lym, L. McAfee, M. Andersch,

#### M. Shoeybi, and B. Catanzaro, ‘‘Reducing activation recomputation in
large transformer models,’’ Proc. Mach. Learn. Syst., vol. 5, no. 1,
pp. 1–25, 2023.

[223] (2020). Turing-NLG: A 17-Billion-parameter Language Model
By Microsoft.
https://www.microsoft.com/
en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-
by-microsoft/

[Online]. Available:

[224] S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He, ‘‘Zero: Memory
optimizations toward training trillion parameter models,’’ in Proc. Int.
Conf. High Perform. Comput., Netw., Storage Anal., 2020, pp. 1–16.

[225] S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari, J. Casper,

#### Z. Liu, S. Prabhumoye, G. Zerveas, V. Korthikanti, E. Zhang, R. Child,

#### R. Y. Aminabadi, J. Bernauer, X. Song, M. Shoeybi, Y. He, M. Houston,

#### S. Tiwary, and B. Catanzaro, ‘‘Using DeepSpeed and megatron to train
megatron-turing NLG 530B, a large-scale generative language model,’’
2022, arXiv:2201.11990.

[226] H.-C. Shin, Y. Zhang, E. Bakhturina, R. Puri, M. Patwary, M. Shoeybi,
and R. Mani, ‘‘BioMegatron: Larger biomedical domain language
model,’’ 2020, arXiv:2010.06060.

[227] P. Xu, M. Patwary, M. Shoeybi, R. Puri, P. Fung, A. Anandkumar,
and B. Catanzaro, ‘‘MEGATRON-CNTRL: Controllable story generation
with external knowledge using large-scale language models,’’ 2020,
arXiv:2010.00840.

[228] B. Zhang and R. Sennrich, ‘‘Root mean square layer normalization,’’ in

Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019, pp. 1–17.

[229] R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin,
(2019). Alpaca: A Strong,
[Online]. Available:


#### P. Liang,
Replicable
https://crfm.stanford.edu/2023/03/13/alpaca.html

Instruction-Following Model.

and T. B. Hashimoto.

[230] (2020). Models—OpenAI.

[Online]. Available:

https://platform.

openai.com/docs/models

[231] (2020). Guanaco—Generative Universal Assistant for Natural-Language
Adaptive Context-Aware Omnilingual Outputs. [Online]. Available:
https://guanaco-model.github.io/

[232] (2020). Alpaca-LoRa.

[Online]. Available: https://github.com/tloen/

alpaca-lora

[233] W.-L. Chiang, Z. Li, Z. Lin, Y. Sheng, Z. Wu, H. Zhang, L. Zheng,

#### S. Zhuang, Y. Zhuang, J. E. Gonzalez, I. Stoica, and E. P. Xing.
(2023). Vicuna: An Open-Source Chatbot Impressing GPT-4 With 90%*
ChatGPT Quality. [Online]. Available: https://lmsys.org/blog/2023-03-
30-vicuna/

[234] (2020). ShareGPT. [Online]. Available: https://sharegpt.com/
[235] (2020). Dolly. [Online]. Available: https://github.com/databrickslabs/

model,’’ 2022, arXiv:2209.06794.

dolly

[211] L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant,

#### A. Barua, and C. Raffel, ‘‘MT5: A massively multilingual pre-trained
text-to-text transformer,’’ 2020, arXiv:2010.11934.

[212] X. Zhai, A. Kolesnikov, N. Houlsby, and L. Beyer, ‘‘Scaling vision
transformers,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.
(CVPR), Jun. 2022, pp. 1204–1213.

[213] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai,

#### T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly,

#### J. Uszkoreit, and N. Houlsby, ‘‘An image is worth 16×16 words:
Transformers for image recognition at scale,’’ 2020, arXiv:2010.11929.

[214] R. Anil et al., ‘‘PaLM 2 technical report,’’ 2023, arXiv:2305.10403.
[215] K. Singhal et al., ‘‘Towards expert-level medical question answering with

large language models,’’ 2023, arXiv:2305.09617.

[216] D. Jin, E. Pan, N. Oufattole, W.-H. Weng, H. Fang, and P. Szolovits,
‘‘What disease does this patient have? A large-scale open domain
question answering dataset from medical exams,’’ Appl. Sci., vol. 11,
no. 14, p. 6421, Jul. 2021.

[217] K. Singhal et al., ‘‘Large language models encode clinical knowledge,’’

2022, arXiv:2212.13138.

[236] M. Conover, M. Hayes, A. Mathur, J. Xie, J. Wan, S. Shah,

#### A. Ghodsi, P. Wendell, M. Zaharia, and R. Xin. (2023). Free Dolly:
Introducing the World’s First Truly Open Instruction-tuned LLM.
[Online]. Available: https://www.databricks.com/blog/2023/04/12/dolly-
first-open-commercially-viable-instruction-tuned-llm

[237] S. Biderman, H. Schoelkopf, Q. G. Anthony, H. Bradley, K. O’Brien,

#### E. Hallahan, M. A. Khan, S. Purohit, U. S. Prashanth, and E. Raff,
‘‘Pythia: A suite for analyzing large language models across training and
scaling,’’ in Proc. Int. Conf. Mach. Learn., 2023, pp. 2397–2430.
[238] X. Geng, A. Gudibande, H. Liu, E. Wallace, P. Abbeel, S. Levine, and

#### D. Song. (2023). Koala: A Dialogue Model for Academic Research.
[Online]. Available: https://bair.berkeley.edu/blog/2023/04/03/koala/

[239] L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin,

#### Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica, ‘‘Judging
LLM-as-a-judge with MT-bench and chatbot arena,’’ in Proc. Adv. Neural
Inf. Process. Syst., 2023, pp. 1–14.

[240] C. Xu, D. Guo, N. Duan, and J. McAuley, ‘‘Baize: An open-source
chat model with parameter-efficient tuning on self-chat data,’’ 2023,
arXiv:2304.01196.

VOLUME 12, 2024

188701

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[241] L. L. Ziang Leng, Qiyuan Chen. (2023). Luotuo: Chinese-Alpaca-LoRa.

[Online]. Available: https://github.com/LC1332/Chinese-alpaca-lora

[242] Y. Cui, Z. Yang, and X. Yao, ‘‘Efficient and effective text encoding for

Chinese LLaMA and alpaca,’’ 2023, arXiv:2304.08177.

[243] R. Zhang, J. Han, C. Liu, P. Gao, A. Zhou, X. Hu, S. Yan, P. Lu, H. Li,
and Y. Qiao, ‘‘LLaMA-adapter: Efficient fine-tuning of language models
with zero-init attention,’’ 2023, arXiv:2303.16199.

[244] P. Gao, J. Han, R. Zhang, Z. Lin, S. Geng, A. Zhou, W. Zhang,

#### P. Lu, C. He, X. Yue, H. Li, and Y. Qiao, ‘‘LLaMA-adapter v2:
Parameter-efficient visual instruction model,’’ 2023, arXiv:2304.15010.
[245] D. Zhu, J. Chen, X. Shen, X. Li, and M. Elhoseiny, ‘‘MiniGPT-4:
Enhancing vision-language understanding with advanced large language
models,’’ 2023, arXiv:2304.10592.

[246] (2023). Chinese Llava. [Online]. Available: https://github.com/LinkSoul-

AI/Chinese-LLaVA

[247] Y. Shu, S. Dong, G. Chen, W. Huang, R. Zhang, D. Shi, Q. Xiang,
and Y. Shi, ‘‘LLaSM: Large language and speech model,’’ 2023,
arXiv:2308.15930.
[248] (2023). Visual-LLaMA.
feizc/Visual-LLaMA

[Online]. Available:

https://github.com/

[249] H. Zhang, X. Li, and L. Bing, ‘‘Video-LLaMA: An instruction-
tuned audio-visual language model for video understanding,’’ 2023,
arXiv:2306.02858.

[250] Q. Zhang, J. Zhang, Y. Xu, and D. Tao, ‘‘Vision transformer with

quadrangle attention,’’ 2023, arXiv:2303.15105.

[251] K. Li, Y. He, Y. Wang, Y. Li, W. Wang, P. Luo, Y. Wang, L. Wang,
and Y. Qiao, ‘‘VideoChat: Chat-centric video understanding,’’ 2023,
arXiv:2305.06355.

[252] R. Girdhar, A. El-Nouby, Z. Liu, M. Singh, K. Vasudev Alwala, A. Joulin,
and I. Misra, ‘‘ImageBind one embedding space to bind them all,’’
in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR),
Jun. 2023, pp. 15180–15190.

[253] J. W. Rae et al., ‘‘Scaling language models: Methods, analysis insights

from training gopher,’’ 2021, arXiv:2112.11446.

[254] T. Kudo and J. Richardson, ‘‘SentencePiece: A simple and language inde-
pendent subword tokenizer and detokenizer for neural text processing,’’
2018, arXiv:1808.06226.

[255] J. Bradbury, R.

Johnson,

#### P. Hawkins, M.
Frostig,

#### J. VanderPlas,

#### C. Leary, D. Maclaurin, G. Necula, A. Paszke,
(2018). JAX: Composable

#### S. Wanderman-Milne, and Q. Zhang.
Transformations of Python+NumPy Programs. [Online]. Available:
http://github.com/google/jax

J.

[256] T. Hennigan, T. Cai, T. Norman, L. Martens, and I. Babuschkin.
Available:

[Online].

Haiku:

Sonnet

JAX.

for

(2020).
http://github.com/deepmind/dm-haiku

[257] J. Hoffmann et al., ‘‘Training compute-optimal large language models,’’

2022, arXiv:2203.15556.

[258] J.-B. Alayrac, ‘‘Flamingo: A visual

language model for few-shot
learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022,
pp. 23716–23736.

[259] A. Brock, S. De, S. L. Smith, and K. Simonyan, ‘‘High-performance
large-scale image recognition without normalization,’’ in Proc. Int. Conf.
Mach. Learn., 2021, pp. 1059–1071.

[260] (2021). AI21
ai21.com/studio

Studio Logo.

[Online]. Available:

https://www.

[261] O. Lieber, O. Sharir, B. Lenz, and Y. Shoham, ‘‘Jurassic-1: Technical
details and evaluation,’’ White Paper. AI21 Labs, vol. 1, no. 9, pp. 1–17,
2021.

[262] E. Karpas, O. Abend, Y. Belinkov, B. Lenz, O. Lieber, N. Ratner,

#### Y. Shoham, H. Bata, Y. Levine, K. Leyton-Brown, D. Muhlgay,

#### N. Rozen, E. Schwartz, G. Shachaf, S. Shalev-Shwartz, A. Shashua,
‘‘MRKL systems: A modular, neuro-symbolic
and M. Tenenholtz,
architecture that combines large language models, external knowledge
sources and discrete reasoning,’’ 2022, arXiv:2205.00445.

[263] (2022). Announcing Jurassic-2 and Task-specific Apis. [Online]. Avail-

able: https://www.ai21.com/blog/introducing-j2

[264] (2023).

Introducing Claude.
anthropic.com/index/introducing-claude

[Online]. Available:

https://www.

[265] (2023). Claude 2.
index/claude-2

[Online]. Available: https://www.anthropic.com/

[266] L. Mei, J. Mao, Z. Wang, C. Gan, and J. B. Tenenbaum, ‘‘FALCON: Fast
visual concept learning by integrating images, linguistic descriptions, and
conceptual relations,’’ 2022, arXiv:2203.16639.

[267] G. Penedo, Q. Malartic, D. Hesslow, R. Cojocaru, A. Cappelli,

#### H. Alobeidli, B. Pannier, E. Almazrouei, and J. Launay, ‘‘The refined
web dataset for falcon LLM: Outperforming curated corpora with web
data, and web data only,’’ 2023, arXiv:2306.01116.

[268] A. Ramesh, ‘‘Zero-shot text-to-image generation,’’ in Proc. Int. Conf.

Mach. Learn. (ICML), Jul. 2021, pp. 8821–8831.

[269] A. Radford, ‘‘Learning transferable visual models from natural language

supervision,’’ in Proc. ICML, 2021, pp. 8748–8763.

[270] A. Ramesh, P. Dhariwal, A. Nichol, C. Chu, and M. Chen, ‘‘Hier-
archical text-conditional image generation with CLIP latents,’’ 2022,
arXiv:2204.06125.

[271] (2023). Dall Ensuremath 3. [Online]. Available: https://openai.com/

dall-e-3

[272] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey,
and I. Sutskever, ‘‘Robust speech recognition via large-scale weak
supervision,’’ in Proc. Int. Conf. Mach. Learn., 2023, pp. 28492–28518.
[273] M. Chen et al., ‘‘Evaluating large language models trained on code,’’

2021, arXiv:2107.03374.

[274] R. Li et al., ‘‘StarCoder: May the source be with you!’’ 2023,

arXiv:2305.06161.

[275] D. So, Q. Le, and C. Liang, ‘‘The evolved transformer,’’ in Proc. Int. Conf.

Mach. Learn., vol. 97, 2019, pp. 5877–5886.

[276] R. Thoppilan et al., ‘‘LaMDA: Language models for dialog applications,’’

2022, arXiv:2201.08239.

[277] G. E. Cohen, ‘‘ALIGN: A program to superimpose protein coordinates,
accounting for insertions and deletions,’’ J. Appl. Crystallogr., vol. 30,
no. 6, pp. 1160–1161, Dec. 1997.

[278] B. Koonce, ‘‘EfficientNet,’’ in Convolutional Neural Networks With Swift
for Tensorflow: Image Recognition and Dataset Categorization. Berkeley,
CA, USA: Apress, 2021, pp. 109–123, doi: 10.1007/978-1-4842-6168-2.
[279] N. Du, ‘‘GLaM: Efficient scaling of language models with mixture-of-
experts,’’ in Proc. Int. Conf. Mach. Learn., vol. 162, 2022, pp. 5547–5569.
[280] G. Team et al., ‘‘Gemini: A family of highly capable multimodal models,’’

2023, arXiv:2312.11805.

[281] (2023).

Phi-1.5.

[Online].

Available:

https://huggingface.co/

microsoft/phi-15

[282] (2023). Phi-2: The Surprising Power of Small Language Models.
[Online]. Available: https://www.microsoft.com/en-us/research/blog/phi-
2-the-surprising-power-of-small-language-models/

[283] C. Li, H. Xu, J. Tian, W. Wang, M. Yan, B. Bi, J. Ye, H. Chen,

#### G. Xu, Z. Cao, J. Zhang, S. Huang, F. Huang, J. Zhou, and

#### L. Si, ‘‘MPLUG: Effective and efficient vision-language learning by
cross-modal skip-connections,’’ 2022, arXiv:2205.12005.

[284] H. Xu, Q. Ye, M. Yan, Y. Shi, J. Ye, Y. Xu, C. Li, B. Bi, Q. Qian,

#### W. Wang, G. Xu, J. Zhang, S. Huang, F. Huang, and J. Zhou, ‘‘MPLUG-2:
A modularized multi-modal foundation model across text, image and
video,’’ 2023, arXiv:2302.00402.

[285] Z. Yang, L. Li, J. Wang, K. Lin, E. Azarnasab, F. Ahmed, Z. Liu,

#### C. Liu, M. Zeng, and L. Wang, ‘‘MM-REACT: Prompting ChatGPT for
multimodal reasoning and action,’’ 2023, arXiv:2303.11381.

[286] Y. Shen, K. Song, X. Tan, D. Li, W. Lu, and Y. Zhuang, ‘‘HuggingGPT:
Solving AI tasks with ChatGPT and its friends in hugging face,’’ 2023,
arXiv:2303.17580.

[287] H. Xu, Q. Ye, X. Wu, M. Yan, Y. Miao, J. Ye, G. Xu, A. Hu, Y. Shi,

#### G. Xu, C. Li, Q. Qian, M. Que, J. Zhang, X. Zeng, and F. Huang,
‘‘Youku-mPLUG: A 10 million large-scale Chinese video-language
dataset for pre-training and benchmarks,’’ 2023, arXiv:2306.04362.
[288] J. Ye, A. Hu, H. Xu, Q. Ye, M. Yan, Y. Dan, C. Zhao, G. Xu, C. Li,

#### J. Tian, Q. Qi, J. Zhang, and F. Huang, ‘‘MPLUG-DocOwl: Modularized
multimodal large language model for document understanding,’’ 2023,
arXiv:2307.02499.

[289] K. Sanders, D. Etter, R. Kriz, and B. Van Durme, ‘‘MultiVENT:
text,’’ 2023,

Multilingual videos of events with aligned natural
arXiv:2307.03153.

[290] S. Soltan, S. Ananthakrishnan, J. FitzGerald, R. Gupta, W. Hamza,

#### H. Khan, C. Peris, S. Rawls, A. Rosenbaum, A. Rumshisky, C. Satya
Prakash, M. Sridhar, F. Triefenbach, A. Verma, G. Tur, and P. Natarajan,
‘‘AlexaTM 20B: Few-shot learning using a large-scale multilingual
Seq2Seq model,’’ 2022, arXiv:2208.01448.

[291] S. Bao, H. He, F. Wang, H. Wu, and H. Wang, ‘‘PLATO: Pre-trained
dialogue generation model with discrete latent variable,’’ 2019,
arXiv:1910.07931.

188702

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[292] S. Bao, H. He, F. Wang, H. Wu, H. Wang, W. Wu, Z. Guo, Z. Liu,
and X. Xu, ‘‘PLATO-2: Towards building an open-domain chatbot via
curriculum learning,’’ 2020, arXiv:2006.16779.

[293] (2023). BAAI 23. [Online]. Available: https://2023.baai.ac.cn/about
[294] Y. Huo et al., ‘‘WenLan: Bridging vision and language by large-scale

multi-modal pre-training,’’ 2021, arXiv:2103.06561.

[295] P.-S. Huang, X. He, J. Gao, L. Deng, A. Acero, and L. Heck, ‘‘Learning
deep structured semantic models for web search using clickthrough data,’’
in Proc. 22nd ACM Int. Conf. Inf. Knowl. Manage., 2013, pp. 2333–2338.
[296] M. Ding, ‘‘CogView: Mastering text-to-image generation via transform-

ers,’’ in Proc. NeurlPS, vol. 34, 2021, pp. 19822–19835.

[297] C. Xiao, X. Hu, Z. Liu, C. Tu, and M. Sun, ‘‘Lawformer: A pre-trained
language model for Chinese legal long documents,’’ AI Open, vol. 2,
pp. 79–84, May 2021.

[298] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen,

#### C. Dewan, M. Diab, X. Li, X. Victoria Lin, T. Mihaylov, M. Ott, S.
Shleifer, K. Shuster, D. Simig, P. S. Koura, A. Sridhar, T. Wang, and

#### L. Zettlemoyer, ‘‘OPT: Open pre-trained transformer language models,’’
2022, arXiv:2205.01068.

[299] S. Iyer, X. V. Lin, R. Pasunuru, T. Mihaylov, D. Simig, P. Yu, K. Shuster,

#### T. Wang, Q. Liu, P. S. Koura, X. Li, B. O’Horo, G. Pereyra, J. Wang,

#### C. Dewan, A. Celikyilmaz, L. Zettlemoyer, and V. Stoyanov, ‘‘OPT-IML:
Scaling language model instruction meta learning through the lens of
generalization,’’ 2022, arXiv:2212.12017.

[300] M. Khrushchev, R. Vasilev, A. Petrov, and N. Zinov. (2022). YaLM 100B.

[Online]. Available: https://github.com/yandex/YaLM-100B

[301] B. Workshop et al., ‘‘Bloom: A 176B-parameter open-access multilingual

language model,’’ 2022, arXiv:2211.05100.

[302] R. Taylor, M. Kardas, G. Cucurull, T. Scialom, A. Hartshorn, E. Saravia,

#### A. Poulton, V. Kerkez, and R. Stojnic, ‘‘Galactica: A large language
model for science,’’ 2022, arXiv:2211.09085.

[303] A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot,
D. de las Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier,

#### L. R. Lavaud, M.-A. Lachaux, P. Stock, T. Le Scao, T. Lavril, T. Wang,

#### T. Lacroix, and W. E. Sayed, ‘‘Mistral 7B,’’ 2023, arXiv:2310.06825.

[304] M. Lewis, Y. Liu, N. Goyal, M. Ghazvininejad, A. Mohamed, O. Levy,

#### V. Stoyanov, and L. Zettlemoyer, ‘‘BART: Denoising sequence-to-
sequence pre-training for natural language generation, translation, and
comprehension,’’ 2019, arXiv:1910.13461.

[305] H. A. Chipman, E. I. George, R. E. McCulloch, and T. S. Shively,
‘‘MBART: Multidimensional monotone BART,’’ Bayesian Anal., vol. 17,
no. 2, pp. 515–544, Jun. 2022.

[306] S. Zhang, V. Chaudhary, N. Goyal, J. Cross, G. Wenzek, M. Bansal,
and F. Guzman, ‘‘How robust is neural machine translation to language
imbalance in multilingual tokenizer training?’’ 2022, arXiv:2204.14268.
[307] J. Wei, M. Bosma, V. Y. Zhao, K. Guu, A. Wei Yu, B. Lester, N. Du,

#### A. M. Dai, and Q. V. Le, ‘‘Finetuned language models are zero-shot
learners,’’ 2021, arXiv:2109.01652.

[308] F. Christopoulou et al., ‘‘PanGu-coder: Program synthesis with function-

level language modeling,’’ 2022, arXiv:2207.11280.

[309] S. Yuan, H. Zhao, Z. Du, M. Ding, X. Liu, Y. Cen, X. Zou, Z. Yang,
and J. Tang, ‘‘WuDaoCorpora: A super large-scale Chinese corpora for
pre-training language models,’’ AI Open, vol. 2, pp. 65–68, Apr. 2021.

[310] L. Xu, X. Zhang, and Q. Dong, ‘‘CLUECorpus2020: A large-scale Chi-
nese corpus for pre-training language model,’’ 2020, arXiv:2003.01355.
[311] L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster,

#### J. Phang, H. He, A. Thite, N. Nabeshima, S. Presser, and C. Leahy, ‘‘The
pile: An 800GB dataset of diverse text for language modeling,’’ 2021,
arXiv:2101.00027.

[312] W. Fedus, B. Zoph, and N. Shazeer, ‘‘Switch transformers: Scaling
to trillion parameter models with simple and efficient sparsity,’’ J.
Mach. Learn. Res., vol. 23, no. 1, pp. 5232–5270, 2022.

[313] (2022). Superglue Benchmarking. [Online]. Available: https://super.

gluebenchmark.com/

[314] T. Schick and H. Schütze, ‘‘Exploiting cloze questions for few shot text
classification and natural language inference,’’ 2020, arXiv:2001.07676.
[Online]. Available: https://github.com/THUDM/

[315] (2022). Glm6b.

ChatGLM-6B/blob/main/READMEen.md

[316] (2022). Chinese and English Multimodal Conversational Langauge
Model. [Online]. Available: https://github.com/THUDM/VisualGLM-6B
‘‘BLIP-2: Bootstrapping
language-image pre-training with frozen image encoders and large
language models,’’ 2023, arXiv:2301.12597.

[317] J. Li, D. Li, S. Savarese, and S. Hoi,

[318] C. Jiang, H. Xu, W. Ye, Q. Ye, C. Li, M. Yan, B. Bi, S. Zhang, J. Zhang,
and F. Huang, ‘‘COPA: Efficient vision-language pre-training through
collaborative object- and patch-text alignment,’’ 2023, arXiv:2308.03475.
[319] J. Liu, X. Huang, J. Zheng, Y. Liu, and H. Li, ‘‘MixMAE: Mixed
and masked autoencoder for efficient pretraining of hierarchical vision
transformers,’’ 2022, arXiv:2205.13137.

[320] K. Lee, D. Ippolito, A. Nystrom, C. Zhang, D. Eck, C. Callison-Burch,
and N. Carlini, ‘‘Deduplicating training data makes language models
better,’’ in Proc. 60th Annu. Meeting Assoc. Comput. Linguistics, 2022,
pp. 8424–8445.

[321] C. Jiang, H. Xu, C. Li, M. Yan, W. Ye, S. Zhang, B. Bi, and S. Huang,
‘‘TRIPS: Efficient vision-and-language pre-training with text-relevant
image patch selection,’’ in Proc. Conf. Empirical Methods Natural
Language Process., 2022, pp. 4084–4096.

[322] Y. Liu, C. Matsoukas, F. Strand, H. Azizpour, and K. Smith,
‘‘PatchDropout: Economizing vision transformers using patch dropout,’’
2022, arXiv:2208.07220.

[323] S. Wei, T. Ye, S. Zhang, Y. Tang, and J. Liang, ‘‘Joint token pruning and
squeezing towards more aggressive compression of vision transformers,’’
2023, arXiv:2304.10716.

[324] H. Wang, C. Ge, H. Chen, and X. Sun,

‘‘PreNAS: Preferred
one-shot learning towards efficient neural architecture search,’’ 2023,
arXiv:2304.14636.

[325] O. Bohdal, L. Balles, M. Wistuba, B. Ermis, C. Archambeau, and

#### G. Zappella, ‘‘PASHA: Efficient HPO and NAS with progressive resource
allocation,’’ 2022, arXiv:2207.06940.

[326] G. Li, Y. Yang, K. Bhardwaj, and R. Marculescu, ‘‘ZiCo: Zero-
shot NAS via inverse coefficient of variation on gradients,’’ 2023,
arXiv:2301.11300.

[327] C. Tang, L. Lyna Zhang, H. Jiang, J. Xu, T. Cao, Q. Zhang, Y. Yang,

#### Z. Wang, and M. Yang, ‘‘ElasticViT: Conflict-aware supernet training
for deploying fast vision transformer on diverse mobile devices,’’ 2023,
arXiv:2303.09730.

[328] C. Hu, C. Wang, X. Ma, X. Meng, Y. Li, T. Xiao, J. Zhu, and C. Li,
‘‘RankNAS: Efficient neural architecture search by pairwise ranking,’’ in
Proc. 2021 Conf. Empirical Methods Natural Lang. Process., Nov. 2021,
pp. 2469–2480.

[329] P. Wang, R. Panda, L. T. Hennigen, P. Greengard, L. Karlinsky, R. Feris,

#### D. D. Cox, Z. Wang, and Y. Kim, ‘‘Learning to grow pretrained models
for efficient transformer training,’’ 2023, arXiv:2303.00980.

[330] S. Shen, P. Walsh, K. Keutzer, J. Dodge, M. Peters, and I. Beltagy,
‘‘Staged training for transformer language models,’’ in Proc. 39th Int.
Conf. Mach. Learn., vol. 162, 2022, pp. 19893–19908.

[331] Y. Qin, Y. Lin, J. Yi, J. Zhang, X. Han, Z. Zhang, Y. Su, Z. Liu, P. Li,

#### M. Sun, and J. Zhou, ‘‘Knowledge inheritance for pre-trained language
models,’’ in Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics,
Hum. Lang. Technol., Jul. 2022, pp. 3921–3937.

[332] X. Gu, L. Liu, H. Yu, J. Li, C. Chen, and J. Han, ‘‘On the transformer
growth for progressive BERT training,’’ in Proc. Conf. North Amer.
Chapter Assoc. Comput. Linguistics, Human Lang. Technol., Jun. 2021,
pp. 5174–5180.

[333] L. Gong, D. He, Z. Li, T. Qin, L. Wang, and T. Liu, ‘‘Efficient training of
BERT by progressively stacking,’’ in Proc. 36th Int. Conf. Mach. Learn.,
vol. 97, 2019, pp. 2337–2346.

[334] Z. Pan, P. Chen, H. He, J. Liu, J. Cai, and B. Zhuang, ‘‘Mesa: A memory-

saving training framework for transformers,’’ 2021, arXiv:2111.11124.

[335] X. Liu, L. Zheng, D. Wang, Y. Cen, W. Chen, X. Han, J. Chen,

#### Z. Liu, J. Tang, J. Gonzalez, M. Mahoney, and A. Cheung, ‘‘GACT:
Activation compressed training for generic network architectures,’’ 2022,
arXiv:2206.11357.

[336] A. Chakrabarti and B. Moseley, ‘‘Backprop with approximate activations
for memory-efficient network training,’’ 2019, arXiv:1901.07988.
[337] P. Micikevicius, S. Narang, J. Alben, G. Diamos, E. Elsen, D. Garcia,

#### B. Ginsburg, M. Houston, O. Kuchaiev, G. Venkatesh, and H. Wu,
‘‘Mixed precision training,’’ 2017, arXiv:1710.03740.

[338] (2023). New Models and Developer Products Announced At Devday.
[Online]. Available: https://openai.com/blog/new-models-and-developer-
products-announced-at-devday

[339] L. Bourtoule, V. Chandrasekaran, C. A. Choquette-Choo, H. Jia,

#### A. Travers, B. Zhang, D. Lie, and N. Papernot, ‘‘Machine unlearning,’’
in Proc. IEEE Symp. Secur. Privacy (SP), May 2021, pp. 141–159.
[340] E. Mitchell, C. Lin, A. Bosselut, C. Finn, and C. D. Manning, ‘‘Fast model

editing at scale,’’ 2021, arXiv:2110.11309.

VOLUME 12, 2024

188703

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[341] E. Mitchell, C. Lin, A. Bosselut, C. D. Manning, and C. Finn, ‘‘Memory-
based model editing at scale,’’ in Proc. Int. Conf. Mach. Learn., 2022,
pp. 15817–15831.

[342] M. Reid and G. Neubig, ‘‘Learning to model editing processes,’’ 2022,

arXiv:2205.12374.

[343] Q. He, Z. Li, and X. Zhang, ‘‘Data deduplication techniques,’’ in Proc. Int.
Conf. Future Inf. Technol. Manage. Eng., vol. 1, Oct. 2010, pp. 430–433.
[344] P. P. Liang, C. Wu, L.-P. Morency, and R. Salakhutdinov, ‘‘Towards
understanding and mitigating social biases in language models,’’ in Proc.
38th Int. Conf. Mach. Learn., vol. 139, 2021, pp. 6565–6576.

[345] S. Bordia and S. R. Bowman, ‘‘Identifying and reducing gender bias in

word-level language models,’’ 2019, arXiv:1904.03035.

[346] R. Liu, C. Jia, J. Wei, G. Xu, L. Wang, and S. Vosoughi, ‘‘Mitigating
political bias in language models through reinforced calibration,’’
Proc. AAAI Conf. Artif. Intell., vol. 35, no. 17, pp. 14857–14866,
May 2021.

[347] M. Nadeem, A. Bethke, and S. Reddy, ‘‘StereoSet: Measuring stereotyp-
ical bias in pretrained language models,’’ 2020, arXiv:2004.09456.
[348] V. Sanh, T. Wolf, and A. Rush, ‘‘Movement pruning: Adaptive sparsity by
fine-tuning,’’ in Proc. Int. Conf. Neural Inf. Process. Syst., vol. 33, 2020,
pp. 20378–20389.

[349] R. Cheong and R. Daniel, ‘‘Transformers Zip: Compressing transformers
with pruning and quantization,’’ Stanford Univ., Stanford, CA,
USA, Tech. Rep., 2019. [Online]. Available: https://web.stanford.edu/
class/archive/cs/cs224n/cs224n.1194/reports/custom/15763707.pdf
[350] M. A. Gordon, K. Duh, and N. Andrews, ‘‘Compressing BERT:
Studying the effects of weight pruning on transfer learning,’’ 2020,
arXiv:2002.08307.

[351] Z. Wang, J. Wohlwend, and T. Lei, ‘‘Structured pruning of large language

models,’’ 2019, arXiv:1910.04732.

[352] B. Cui, Y. Li, and Z. Zhang, ‘‘Joint structured pruning and dense
knowledge distillation for efficient transformer model compression,’’
Neurocomputing, vol. 458, pp. 56–69, Oct. 2021.

[353] Z. Yang, Y. Cui, and Z. Chen, ‘‘TextPruner: A model pruning toolkit for

pre-trained language models,’’ 2022, arXiv:2203.15996.

[354] E. Frantar and D. Alistarh, ‘‘SparseGPT: Massive language models can

be accurately pruned in one-shot,’’ 2023, arXiv:2301.00774.

[355] M. Zhang, H. Chen, C. Shen, Z. Yang, L. Ou, X. Yu, and B. Zhuang,
‘‘LoRAPrune: Structured pruning meets low-rank parameter-efficient
fine-tuning,’’ 2023, arXiv:2305.18403.

[356] T. Chen, T. Ding, B. Yadav, I. Zharkov, and L. Liang, ‘‘LoRAShear:
large language model structured pruning and knowledge

Efficient
recovery,’’ 2023, arXiv:2310.18356.

[357] M. Sun, Z. Liu, A. Bair, and J. Zico Kolter, ‘‘A simple and effective
pruning approach for large language models,’’ 2023, arXiv:2306.11695.
[358] M. Xia, Z. Zhong, and D. Chen, ‘‘Structured pruning learns compact and

accurate models,’’ 2022, arXiv:2204.00408.

[359] M. Zhu, Y. Tang, and K. Han, ‘‘Vision transformer pruning,’’ 2021,

arXiv:2104.08500.

[360] E. Voita, D. Talbot, F. Moiseev, R. Sennrich, and I. Titov, ‘‘Analyzing
multi-head self-attention: Specialized heads do the heavy lifting, the rest
can be pruned,’’ 2019, arXiv:1905.09418.

[361] A. Fan, E. Grave, and A. Joulin, ‘‘Reducing transformer depth on demand

with structured dropout,’’ 2019, arXiv:1909.11556.

[362] F. Lagunas, E. Charlaix, V. Sanh, and A. M. Rush, ‘‘Block pruning for

faster transformers,’’ 2021, arXiv:2109.04838.

[363] P. Michel, O. Levy, and G. Neubig, ‘‘Are sixteen heads really better than

one?’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019, pp. 1–14.

[364] D. Campos, A. Marques, T. Nguyen, M. Kurtz, and C. Zhai,
‘‘Sparse*BERT: Sparse models generalize to new tasks and domains,’’
2022, arXiv:2205.12452.

[365] M. Santacroce, Z. Wen, Y. Shen, and Y. Li, ‘‘What matters in the struc-
tured pruning of generative language models?’’ 2023, arXiv:2302.03773.
[366] X. Ma, G. Fang, and X. Wang, ‘‘LLM-pruner: On the structural pruning

of large language models,’’ 2023, arXiv:2305.11627.

[367] S. Guo, J. Xu, L. Lyna Zhang, and M. Yang, ‘‘Compresso: Structured
pruning with collaborative prompting learns compact large language
models,’’ 2023, arXiv:2310.05015.

[368] M. Xia, T. Gao, Z. Zeng, and D. Chen, ‘‘Sheared LLaMA: Accel-
erating language model pre-training via structured pruning,’’ 2023,
arXiv:2310.06694.

[369] A. Mishra, J. Albericio Latorre, J. Pool, D. Stosic, D. Stosic,

#### G. Venkatesh, C. Yu, and P. Micikevicius, ‘‘Accelerating sparse deep
neural networks,’’ 2021, arXiv:2104.08378.

[370] C. Fang, A. Zhou, and Z. Wang, ‘‘An algorithm–hardware co-optimized
framework for accelerating N: M sparse transformers,’’ IEEE Trans.
Very Large Scale Integr. (VLSI) Syst., vol. 30, no. 11, pp. 1573–1586,
Nov. 2022.

[371] C. Holmes, M. Zhang, Y. He, and B. Wu, ‘‘Nxmtransformer: Semi-
structured sparsification for natural language understanding via admm,’’
in Proc. Adv. Neural Inf. Process. Syst., vol. 34, 2021, pp. 1818–1830.

[372] C. Fang, S. Guo, W. Wu, J. Lin, Z. Wang, M. K. Hsu, and L. Liu, ‘‘An
efficient hardware accelerator for sparse transformer neural networks,’’ in
Proc. IEEE Int. Symp. Circuits Syst. (ISCAS), May 2022, pp. 2670–2674.
[373] R. Xu, F. Luo, C. Wang, B. Chang, J. Huang, S. Huang, and F. Huang,
‘‘From dense to sparse: Contrastive pruning for better pre-trained
language model compression,’’ Proc. AAAI Conf. Artif. Intell., vol. 36,
no. 10, pp. 11547–11555, Jun. 2022.

[374] J. Zhang, Y. Zhou, and R. Saab, ‘‘Post-training quantization for neural
networks with provable guarantees,’’ SIAM J. Math. Data Sci., vol. 5,
no. 2, pp. 373–399, Jun. 2023.

[375] B. Jacob, S. Kligys, B. Chen, M. Zhu, M. Tang, A. Howard, H. Adam,
and D. Kalenichenko, ‘‘Quantization and training of neural networks for
efficient integer-arithmetic-only inference,’’ in Proc. IEEE/CVF Conf.
Comput. Vis. Pattern Recognit., Jun. 2018, pp. 2704–2713.

[376] Z. Liu, B. Oguz, C. Zhao, E. Chang, P. Stock, Y. Mehdad, Y. Shi,

#### R. Krishnamoorthi, and V. Chandra, ‘‘LLM-QAT: Data-free quantization
aware training for large language models,’’ 2023, arXiv:2305.17888.

[377] J. Kim, J. H. Lee, S. Kim, J. Park, K. M. Yoo, S. J. Kwon, and D. Lee,
‘‘Memory-efficient fine-tuning of compressed large language models via
sub-4-bit integer quantization,’’ 2023, arXiv:2305.14152.

[378] T. Dettmers, A. Pagnoni, A. Holtzman, and L. Zettlemoyer, ‘‘QLoRA:
Efficient finetuning of quantized LLMs,’’ 2023, arXiv:2305.14314.
[379] E. Frantar, S. Ashkboos, T. Hoefler, and D. Alistarh, ‘‘GPTQ: Accurate
post-training quantization for generative pre-trained transformers,’’ 2022,
arXiv:2210.17323.

[380] E. Frantar, S. Ashkboos, T. Hoefler, and D. Alistarh, ‘‘Optq: Accurate
quantization for generative pre-trained transformers,’’ in Proc. 11th Int.
Conf. Learn. Represent., 2022, pp. 1–27.

[381] Z. Yuan, L. Niu, J. Liu, W. Liu, X. Wang, Y. Shang, G. Sun, Q. Wu, J. Wu,
and B. Wu, ‘‘RPTQ: Reorder-based post-training quantization for large
language models,’’ 2023, arXiv:2304.01089.

[382] Q. Li, Y. Zhang, L. Li, P. Yao, B. Zhang, X. Chu, Y. Sun, L. Du,
and Y. Xie, ‘‘FPTQ: Fine-grained post-training quantization for large
language models,’’ 2023, arXiv:2308.15987.

[383] Z. Yao, R. Yazdani Aminabadi, M. Zhang, X. Wu, C. Li, and Y. He,
‘‘Zeroquant: Efficient and affordable post-training quantization for
large-scale transformers,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35,
2022, pp. 27168–27183.

[384] Z. Yao, X. Wu, C. Li, S. Youn, and Y. He, ‘‘ZeroQuant-v2: Exploring
post-training quantization in LLMs from comprehensive study to low rank
compensation,’’ 2023, arXiv:2303.08302.

[385] X. Wu, Z. Yao, and Y. He, ‘‘ZeroQuant-FP: A leap forward in LLMs
post-training W4A8 quantization using floating-point formats,’’ 2023,
arXiv:2307.09782.

[386] G. Xiao, J. Lin, M. Seznec, H. Wu, J. Demouth, and S. Han,
‘‘Smoothquant: Accurate and efficient post-training quantization for
large language models,’’ in Proc. Int. Conf. Mach. Learn., 2023,
pp. 38087–38099.

[387] W. Shao, M. Chen, Z. Zhang, P. Xu, L. Zhao, Z. Li, K. Zhang,

#### P. Gao, Y. Qiao, and P. Luo, ‘‘OmniQuant: Omnidirectionally calibrated
quantization for large language models,’’ 2023, arXiv:2308.13137.
[388] C. Lee, J. Jin, T. Kim, H. Kim, and E. Park, ‘‘OWQ: Outlier-aware weight
quantization for efficient fine-tuning and inference of large language
models,’’ 2023, arXiv:2306.02272.

[389] J. Lin, J. Tang, H. Tang, S. Yang, W.-M. Chen, W.-C. Wang,

#### G. Xiao, X. Dang, C. Gan, and S. Han, ‘‘AWQ: Activation-aware
weight quantization for LLM compression and acceleration,’’ 2023,
arXiv:2306.00978.

[390] T. Dettmers, M. Lewis, Y. Belkada, and L. Zettlemoyer, ‘‘LLM.int8():
scale,’’ 2022,

transformers

at

8-bit matrix multiplication for
arXiv:2208.07339.

[391] X. Wu, C. Li, R. Y. Aminabadi, Z. Yao, and Y. He, ‘‘Understanding int4
quantization for language models: Latency speedup, composability, and
failure cases,’’ in Proc. 40th Int. Conf. Mach. Learn., 2023, pp. 1–12.

[392] D. Abati, H. B. Yahia, M. Nagel, and A. Habibian, ‘‘Resq: Residual
quantization for video perception-supplementary material,’’ in Proc.
ICCV, 2023, pp. 1–28.

188704

VOLUME 12, 2024

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

[393] S. Kim, C. Hooper, A. Gholami, Z. Dong, X. Li, S. Shen, M. W. Mahoney,
and K. Keutzer, ‘‘SqueezeLLM: Dense-and-Sparse quantization,’’ 2023,
arXiv:2306.07629.

[394] J. Chee, Y. Cai, V. Kuleshov, and C. De Sa, ‘‘QuIP: 2-Bit quantization of
large language models with guarantees,’’ 2023, arXiv:2307.13304.
[395] W. Cheng, W. Zhang, H. Shen, Y. Cai, X. He, K. Lv, and Y. Liu, ‘‘Optimize
weight rounding via signed gradient descent for the quantization of
LLMs,’’ 2023, arXiv:2309.05516.

[396] L. Li, Q. Li, B. Zhang, and X. Chu, ‘‘Norm tweaking: High-performance
low-bit quantization of large language models,’’ 2023, arXiv:2309.02784.
[397] C. Guo, J. Tang, W. Hu, J. Leng, C. Zhang, F. Yang, Y. Liu,

#### M. Guo, and Y. Zhu, ‘‘Olive: Accelerating large language models via
hardware-friendly outlier-victim pair quantization,’’ in Proc. 50th Annu.
Int. Symp. Comput. Archit., 2023, pp. 1–15.

[398] K. Behdin, A. Acharya, A. Gupta, Q. Song, S. Zhu, S. Keerthi,
and R. Mazumder, ‘‘QuantEase: Optimization-based quantization for
language models,’’ 2023, arXiv:2309.01885.

[399] X. Wei, Y. Zhang, X. Zhang, R. Gong, S. Zhang, Q. Zhang, F. Yu, and

#### X. Liu, ‘‘Outlier suppression: Pushing the limit of low-bit transformer
language models,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022,
pp. 17402–17414.

[400] X. Wei, Y. Zhang, Y. Li, X. Zhang, R. Gong, J. Guo, and X. Liu,
‘‘Outlier Suppression+: Accurate quantization of large language models
by equivalent and optimal shifting and scaling,’’ 2023, arXiv:2304.09145.
[401] G. Park, B. Park, M. Kim, S. Lee, J. Kim, and B. Kwon, ‘‘Lut-gemm:
Quantized matrix multiplication based on LUTs for efficient inference in
large-scale generative language models,’’ 2022, arXiv:2206.09557.

[402] J. Lu, D. Batra, D. Parikh, and S. Lee,

‘‘VilBERT: Pretraining
task-agnostic visiolinguistic representations for vision-and-language
tasks,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019, pp. 1–26.
[403] C. Alberti, J. Ling, M. Collins, and D. Reitter, ‘‘Fusion of detected objects
in text for visual question answering,’’ 2019, arXiv:1908.05054.
[404] H. Tan and M. Bansal, ‘‘LXMERT: Learning cross-modality encoder

representations from transformers,’’ 2019, arXiv:1908.07490.

[405] J. Cho, J. Lu, D. Schwenk, H. Hajishirzi, and A. Kembhavi,
‘‘X-LXMERT: Paint, caption and answer questions with multi-modal
transformers,’’ 2020, arXiv:2009.11278.

[406] Y.-C. Chen, L. Li, L. Yu, A. E. Kholy, F. Ahmed, Z. Gan, Y. Cheng, and

#### J. Liu, ‘‘Uniter: Universal image-text representation learning,’’ in Proc.
ECCV, Aug. 2020, pp. 104–120.

[407] G. Li, N. Duan, Y. Fang, M. Gong, and D. Jiang, ‘‘Unicoder-VL: A
universal encoder for vision and language by cross-modal pre-training,’’
in Proc. AAAI Conf. Artif. Intell., 2020, vol. 34, no. 7, pp. 11336–11344.
[408] Z. Huang, Z. Zeng, B. Liu, D. Fu, and J. Fu, ‘‘Pixel-BERT: Aligning
transformers,’’ 2020,

image pixels with text by deep multi-modal
arXiv:2004.00849.

[409] W. Li, C. Gao, G. Niu, X. Xiao, H. Liu, J. Liu, H. Wu, and H. Wang,
‘‘UNIMO: Towards unified-modal understanding and generation via
cross-modal contrastive learning,’’ 2020, arXiv:2012.15409.

[410] W. Li, C. Gao, G. Niu, X. Xiao, H. Liu, J. Liu, H. Wu, and H. Wang,
‘‘UNIMO-2: End-to-end unified vision-language grounded learning,’’
2022, arXiv:2203.09067.

[411] S. Yuan, S. Zhao, J. Leng, Z. Xue, H. Zhao, P. Liu, Z. Gong, W. Xin
Zhao, J. Li, and J. Tang, ‘‘WuDaoMM: A large-scale multi-modal dataset
for pre-training models,’’ 2022, arXiv:2203.11480.

[412] Y. Liu, G. Zhu, B. Zhu, Q. Song, G. Ge, H. Chen, G. Qiao, R. Peng,

#### L. Wu, and J. Wang, ‘‘Taisu: A 166m large-scale high-quality dataset for
Chinese vision-language pre-training,’’ in Proc. Adv. Neural Inf. Process.
Syst., vol. 35, 2022, pp. 16705–16717.

[413] Y. Zeng, C. Jiang, J. Mao, J. Han, C. Ye, and Q. Huang, ‘‘Clip2:
Contrastive language-image-point pretraining from real-world point
cloud data,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.,
Jun. 2023, pp. 15244–15253.

[414] W. Kim, B. Son, and I. Kim, ‘‘ViLT: Vision-and-language transformer
Int. Conf.

region supervision,’’

in Proc.

without convolution or
Mach. Learn., 2021, pp. 5583–5594.

[415] J. Lin, A. Yang, Y. Zhang, J. Liu, J. Zhou, and H. Yang, ‘‘InterBERT:
Vision-and-language interaction for multi-modal pretraining,’’ 2020,
arXiv:2003.13198.

[416] D. Qi, L. Su, J. Song, E. Cui, T. Bharti, and A. Sacheti, ‘‘ImageBERT:
Cross-modal pre-training with large-scale weak-supervised image-text
data,’’ 2020, arXiv:2001.07966.

[417] T. Le Scao and A. M. Rush, ‘‘How many data points is a prompt worth?’’

2021, arXiv:2103.08493.

[418] S. Bao, H. He, F. Wang, H. Wu, H. Wang, W. Wu, Z. Wu, Z. Guo,

#### H. Lu, X. Huang, X. Tian, X. Xu, Y. Lin, and Z.-Y. Niu, ‘‘PLATO-XL:
Exploring the large-scale pre-training of dialogue generation,’’ 2021,
arXiv:2109.09519.

[419] S. Wu, O. Irsoy, S. Lu, V. Dabravolski, M. Dredze, S. Gehrmann,

#### P. Kambadur, D. Rosenberg, and G. Mann, ‘‘BloombergGPT: A large
language model for finance,’’ 2023, arXiv:2303.17564.

[420] N. Shirish Keskar, B. McCann, L. R. Varshney, C. Xiong, and R. Socher,
‘‘CTRL: A conditional transformer language model for controllable
generation,’’ 2019, arXiv:1909.05858.

[421] J. Yu, Z. Wang, V. Vasudevan, L. Yeung, M. Seyedhosseini, and Y. Wu,
‘‘CoCa: Contrastive captioners are image-text foundation models,’’ 2022,
arXiv:2205.01917.

[422] J. Li, R. Selvaraju, A. Gotmare, S. Joty, C. Xiong, and S. C. H. Hoi,
‘‘Align before fuse: Vision and language representation learning with
Inf. Process. Syst.
momentum distillation,’’
(NeurIPS), vol. 34, 2021, pp. 9694–9705.

in Proc. Adv. Neural

[423] Z. Wang, J. Yu, A. Wei Yu, Z. Dai, Y. Tsvetkov, and Y. Cao, ‘‘SimVLM:
Simple visual language model pretraining with weak supervision,’’ 2021,
arXiv:2108.10904.

[424] H. Bao, W. Wang, L. Dong, Q. Liu, O. K. Mohammed, K. Aggarwal,

#### S. Som, S. Piao, and F. Wei, ‘‘Vlmo: Unified vision-language pre-training
with mixture-of-modality-experts,’’ in Proc. Adv. Neural Inf. Process.
Syst., vol. 35, 2022, pp. 32897–32912.

[425] Z. Huang, Z. Zeng, Y. Huang, B. Liu, D. Fu, and J. Fu, ‘‘Seeing out
of the box: End-to-end pre-training for vision-language representation
learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.,
May 2021, pp. 12976–12985.

[426] J. Lin, Y. Qu, W. Guo, X. Dai, R. Tang, Y. Yu, and W. Zhang, ‘‘Map: A
model-agnostic pretraining framework for click-through rate prediction,’’
in Proc. 29th ACM SIGKDD Conf. Knowl. Discovery Data Mining,
Dec. 2023, pp. 1384–1395.

MINGHAO SHAO (Graduate Student Member,
IEEE) received the B.S. degree in computer
science with artificial intelligence from the Uni-
in 2020,
versity of Nottingham (UoN), U.K.,
and the M.S. degree in computer science from
New York University (NYU), USA,
in 2023.
He is currently pursuing the Ph.D. degree in
computer science with New York University Abu
Dhabi (NYUAD), co-advised by Prof. Muhammad
Shafique and Prof. Ramesh Karri with New
York University Tandon School of Engineering. His research interests
include agent systems for cybersecurity, machine learning security, model
compression and efficient inference for large language models, and deep
neural networks.

ABDUL BASIT received the B.S. degree in
electrical engineering from the National Uni-
versity of Sciences and Technology (NUST),
Pakistan, in 2021. Since August 2023, he has
been with New York University Abu Dhabi
(NYUAD), where he is currently a Research
Engineer with the eBrain Laboratory. His research
interests include autonomous driving, large lan-
guage models, robotic systems, and security of
face recognition models. He received the Rector’s
Gold Medal in B.S. EE.

VOLUME 12, 2024

188705

M. Shao et al.: Survey of Different LLM Architectures: Trends, Benchmarks, and Challenges

RAMESH KARRI (Fellow, IEEE) received the
B.E. degree in electrical and computer engineering
from Andhra University and the Ph.D. degree
in computer science from the University of
California San Diego. He is currently a Professor
of electrical and computer engineering with
New York University (NYU) Tandon School of
Engineering. He co-directs the NYU Center for
Cyber Security, co-founded the Trust Hub, and
founded the Embedded Systems Challenge, the
Annual Red Team Blue Team Event. He has published more than
300 papers in leading journals and conference proceedings. His research
and education in hardware cybersecurity include trustworthy ICs, processors,
and cyber-physical systems; security-aware computer-aided design, test,
verification, and nano meets security; hardware security competitions,
benchmarks, and metrics; and additive manufacturing security.

MUHAMMAD SHAFIQUE (Senior Member,
IEEE) received the Ph.D. degree in computer
science from Karlsruhe Institute of Technology,
Karlsruhe, Germany,
in 2011. He was a Full
Professor with the Institute of Computer Engi-
neering, TU Wien, Vienna, Austria, from October
2016 to August 2020. Since September 2020,
he has been with the Division of Engineering, New
York University Abu Dhabi, Abu Dhabi, United
Arab Emirates, and is a Global Network Faculty
Member with the NYU Tandon School of Engineering, Brooklyn, NY,
USA. His research interests include system-level design for brain-inspired
computing, AI/machine learning hardware, wearables, autonomous systems,
energy-efficient and robust computing, the IoT, and smart CPS. He received
the 2015 ACM/SIGDA Outstanding New Faculty Award, the AI 2000 Chip
Technology Most Influential Scholar Award, in 2020, 2022, and 2023,
six gold medals, and several best paper awards and nominations. He has
given several keynotes, talks, and tutorials and organized special sessions
at premier venues. He has served as the PC chair, the general chair, the track
chair, and a PC member for several conferences.

188706

VOLUME 12, 2024


---

> *End of P-11*

<br><br>

<a id="p12-----towards-retrieval-augmented-large-language-models-data-management-and-system-design"></a>

## P-12 — Towards Retrieval-Augmented Large Language Models: Data Management and System Design

| Field | Details |
|-------|---------|
| **Paper ID** | `P-12` |
| **Title** | Towards Retrieval-Augmented Large Language Models: Data Management and System Design |
| **Authors** | Wenqi Fan, Pangjing Wu, Yujuan Ding, Liangbo Ning, Shijie Wang, Qing Li, and others |
| **Affiliation(s)** | Department of Computing / School of Fashion and Textile, The Hong Kong Polytechnic University, Hong Kong |
| **Venue** | IEEE 41st International Conference on Data Engineering (ICDE) |
| **Volume / Year** | 2025 |
| **DOI** | [10.1109/ICDE65448.2025.00341](https://doi.org/10.1109/ICDE65448.2025.00341) |

---

2025 IEEE 41st International Conference on Data Engineering (ICDE)

Towards Retrieval-Augmented Large Language
Models: Data Management and System Design

1st Wenqi Fan
Department of Computing
The Hong Kong Polytechnic University
Hong Kong, Hong Kong
wenqifan03@gmail.com

2nd Pangjing Wu
Department of Computing
The Hong Kong Polytechnic University
Hong Kong, Hong Kong
pang-jing.wu@connect.polyu.hk

3rd Yujuan Ding
School of Fashion and Textile
The Hong Kong Polytechnic University
Hong Kong, Hong Kong
dingyujuan385@gmail.com

4th Liangbo Ning
Department of Computing
The Hong Kong Polytechnic University
Hong Kong, Hong Kong
liangbo.ning@connect.polyu.hk

5th Shijie Wang
Department of Computing
The Hong Kong Polytechnic University
Hong Kong, Hong Kong
shijie.wang@connect.polyu.hk

6th Qing Li
Department of Computing
The Hong Kong Polytechnic University
Hong Kong, Hong Kong
qing-prof.li@polyu.edu.hk


### Abstract

Retrieval-augmented generation (RAG) has become
a transformative approach for enhancing large language models
(LLMs) by integrating external, reliable, and up-to-date knowl-
edge. This addresses critical limitations such as hallucinations
and outdated internal information. This tutorial delves into the
evolution and frameworks of RAG, emphasizing the pivotal role
of data management technologies in optimizing query processing,
storage, indexing, and efficiency. It explores how RAG systems
can deliver high-quality, context-aware outputs through efficient
retrieval and integration, covering key topics such as retrieval-
augmented LLM (RA-LLM) architectures, retrieval techniques,
learning methodologies, and applications in NLP and domain-
specific tasks. Challenges like customized query and generation,
real-time retrieval, and trustworthy RAG are discussed alongside
future directions and opportunities for innovation. Designed for
students, researchers, and industry practitioners with basic ar-
tificial intelligence and data engineering knowledge, this tutorial
offers practical insights into designing data management-powered
RAG systems. It inspires the exploration of novel solutions in this
rapidly evolving field.


### Index Terms / Keywords

Retrieval-Augmented Generation, Data manage-

ment, Large Language Model


### I. Introduction

Retrieval-augmented generation (RAG) is a pivotal tech-
nique in AI, enhancing the capabilities of Large Language
Models (LLMs) by integrating external, up-to-date knowledge
into their workflows. LLMs, such as GPT [1] and BERT [2],
have revolutionized natural language understanding and gener-
ation but suffer limitations like hallucinations, domain knowl-
edge gaps, and the need for costly fine-tuning [3]. RAG bridges
these gaps by leveraging retrieval mechanisms to access rel-
evant external databases during generation, thus improving
accuracy and relevance [4]. It has proven instrumental
in
knowledge-intensive tasks like answering questions, chatbots,
and recommender systems and mitigating issues like hallu-
cinations in legal [5] and medical queries [6]. For instance,
retrieval-enhanced systems [7], [8] integrate retrieved infor-
mation with input queries to refine response generation, while

retrieval-augmented frameworks [9], [10] dynamically access
external knowledge bases for domain-specific applications.
Recent advancements also include self-reflective retrieval sys-
tems [11] that assess the utility of retrieved content and dense
retrieval frameworks [12] that enhance attention mechanisms.
These innovations underscore the evolving synergy between
retrieval and generation, showcasing RAG as a cornerstone of
AI-driven applications.

Data management technologies significantly enhance RAG
systems by improving query processing, storage, indexing,
and execution, making them an important topic to explore
for both research and application value. Efficient similarity-
based search methods optimize query performance for open-
domain tasks [13]–[15]. Advanced storage and indexing tech-
niques enable scalable handling of high-dimensional embed-
dings, supporting large-scale nearest neighbor search capa-
bilities [16], [17]. Query optimization frameworks improve
system efficiency by balancing latency and quality through
pipeline management and adaptive retrieval intervals [18]–
[20]. Furthermore, knowledge management modules integrate
domain-specific augmentation by leveraging vector databases,
supporting both structured and unstructured data queries
through RAG-enhanced LLMss [21].

To this end, we propose to present

the tutorial on the
targeted topic to share our knowledge and insights with prac-
titioners from both the academia and industry communities
who are interested in this topic and try to apply in their
own projects. Our tutor team consists of well-experienced
researchers with expertise relevant to the topic, which will be
introduced in the following Sections (Sec. II–Sec. IV). We plan
to organize the tutorial in six major parts, which is detailed in
Section VI.


### II. Tutorial Presenters

Six tutors will contribute to this tutorial. Their brief infor-

mation is as follows.

2375-026X/25/$31.00 ©2025 IEEE
DOI 10.1109/ICDE65448.2025.00341

4509

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:55 UTC from IEEE Xplore. Restrictions apply.

.

.

1
4
3
0
0
5
2
0
2
8
4
4
5
6
E
D
C
I
/
9
0
1
1
0
1
:
I

.

O
D
|
E
E
E
I

.

5
2
0
2
©
0
0
1
3
$
/
5
2
/
9
-
3
0
6
3
-
5
1
3
3
-
8
-
9
7
9
|
)
E
D
C
I
(
g
n
i
r
e
e
n
g
n
E
a
t
a
D
n
o
e
c
n
e
r
e
f
n
o
C

i

l

a
n
o
i
t
a
n
r
e
t
n

I

t
s
1
4
E
E
E
I

5
2
0
2


### III. Tutor Information

- Wenqi Fan, The Hong Kong Polytechnic University, 11
Yuk Choi Rd, Kowloon, HK, wenqifan03@gmail.com
- Pangjing Wu, The Hong Kong Polytechnic Uni-
versity, 11 Yuk Choi Rd, Kowloon, HK, pang-
jing.wu@connect.polyu.hk

- Yujuan Ding, The Hong Kong Polytechnic University, 11
Yuk Choi Rd, Kowloon, HK, dingyujuan385@gmail.com
Polytechnic
11 Yuk Choi Rd, Kowloon, HK,

The Hong Kong

- Liangbo

Ning,

University,
liangbo.ning@connect.polyu.hk

- Shijie Wang,

The Hong Kong

Polytechnic
11 Yuk Choi Rd, Kowloon, HK,

University,
shijie.wang@connect.polyu.hk

- Qing Li, The Hong Kong Polytechnic University, 11 Yuk

Choi Rd, Kowloon, HK, qing-prof.li@polyu.edu.hk


### IV. Brief Bios

In this section, we will give brief bios for all presenters.
- Dr. Wenqi Fan is an assistant professor of the De-
partment of Computing at The Hong Kong Polytechnic
University (PolyU). He received his Ph.D. degree from
the City University of Hong Kong (CityU) in 2020. From
2018 to 2020, he was a visiting research scholar at Michi-
gan State University. His research interests are machine
learning and data mining, focusing on Recommender
Systems, Graph Neural Networks, and Large Language
Models (LLMs). He has published innovative papers in
top-tier journals and conferences such as IEEE TKDE,
KDD, WWW, NeurIPS, ICDE, IJCAI, AAAI, RecSys,
WSDM, and SDM. He serves as a top-tier conference
(senior) program committee member (e.g., ICML, ICLR,
NeurIPS, KDD, WWW, AAAI, IJCAI, CIKM, WSDM)
and journal reviewers (e.g., TKDE, TIST, TKDD, TOIS,
TAI). He also serves as the lead tutor of tutorials in top-
tier conferences (e.g., WSDM 2023, WWW 2021/2022,
IJCAI 2021, and ICAPS 2021). More information about
him can be found at https://wenqifan03.github.io/.

- Pangjing Wu is currently a PhD student at The Hong
Kong Polytechnic University, supervised by Dr. Wenqi
Fan and Prof. Qing Li. He got his BSc and M.Eng.
degree at Hohai University (HHU). His research interests
include data integrity, data pricing, large language models
(LLMs), and reinforcement learning. More information
about him can be found at https://pangjing-wu.github.io/.
- Dr. Yujuan Ding is a research assistant professor at
school of fashion and textile, The Hong Kong Polytechnic
University (PolyU). She received her Ph.D. degree from
the same university in 2021. From 2019 to 2020, she
visited the school of Computing at National University
of Singapore as a research student. She has extensive
research experience in the field of multimedia analysis,
large language models (LLMs), and information retrieval
across various domains, specifically focusing on the
topics of recommender systems, time-series modeling,

vision-language modeling and other AI applications. She
has published her research outcome in top-tier journals
and conferences including ACM CSUR, IEEE TMM,
IEEE TSCVT, ACM MM, ICCV, etc. She was the re-
cipient of the best student paper award of ICMR 2021.
She serves as the program committee members for top-
tier conferences (e.g., AAAI, ACL, ACM MM, EMNLP)
and reviewers for journals. More information about her
can be found at https://joanding.github.io/.

- Liangbo Ning is currently a PhD student at The
Hong Kong Polytechnic University, supervised by Prof.
Qing Li and Dr. Wenqi Fan. He got his B.Eng. and
MSc degrees at Northwestern Polytechnical University
(NPU). His research interests include adversarial attacks,
large language models (LLMs), and pattern recognition.
More information about him can be found at https:
//biglemon-ning.github.io/.

- Shijie Wang is currently a PhD student at The Hong
Kong Polytechnic University, supervised by Dr. Wenqi
Fan. He got his BSc degree at the University of Liver-
pool (Uol). His research interests include recommender
systems, large language models (LLMs), and graph neural
networks. More information about him can be found at
https://sjay-wang.github.io/.

- Prof. Qing Li is currently a Chair Professor (data sci-
ence) and the Head of the Department of Computing,
The Hong Kong Polytechnic University. He received
the B.Eng. degree from Hunan University, Changsha,
China, the M.Sc. and Ph.D. degrees from the University
of Southern California, Los Angeles, all in computer
science. His research interests include object modeling,
multimedia databases, social media, and recommender
systems. He is a Fellow of IEEE and IET, a member
of ACM SIGMOD and IEEE Technical Committee on
Data Engineering. He is the chairperson of the Hong
Kong Web Society and is a steering committee member of
DASFAA, ICWL, and WISE Society. More information
about him can be found at https://www4.comp.polyu.edu.
hk/∼csqli/.


### V. Tutorial Length

We plan to make a 3-hour length tutorial at ICDE 2025.


### VI. Outline Of The Tutorial

This tutorial is expected to be presented as a half-day lecture
with slides and handouts to the audience. The arrangement of
detailed content to be introduced in this tutorial is given as
follows:

- Introduction (10 mins)

– Background of the topic, basic concept and ideas of

LLM, RAG and data management

– The tutorial organization

- Architecture of Combining RAG with LLMs (40 mins)

– RA-LLM architecture overview
– Retriever in RAG-LLMs

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:55 UTC from IEEE Xplore. Restrictions apply.

4510

– Retrieval results integration
– Pre/Post-retrieval techniques
– Special RA-LLM paradigms
- Data Management for RAG (40 mins)
– Preliminaries of Data Management
– RAG-powered by Data Management
– Popular Vector Database Management Systems

- Learning of RAG (30 mins)

– Training-free methods
– Training-based methods
- Applications of RAG (30 mins)

– NLP application
– Downstream tasks
– Domain-specific applications

- Future Directions of Data Management and RAG (20

mins)

– Customized Query and Generation
– Challenges in Real-Time Retrieval
– Trustworthy RAG
- QA session (10 mins)


### VII. Potential Target Audience

The audience of this tutorial could be college students, re-
searchers in academic institutions, and industrial database and
AI labs interested in data engineering, artificial intelligence,
and the latest trends in LLMs. Audiences are expected to
have some basic understanding of data engineering, artificial
intelligence, information retrieval, and natural language pro-
cessing. However, the tutorial will be presented at the college
junior/senior level so that
it can be comfortably followed
by academic researchers or industrial practitioners who are
interested in this emerging field. After attending this tutorial,
the audience is expected to comprehensively understand data
management in retrieval augmented generation and learn how
to design data management-powered RAG for real-world ap-
plications. It is also hopeful that the audience gets inspired by
this tutorial and can step further in this field to explore novel
opportunities in data management-powered RAG.


### VIII. Hands-On Tutorial

This tutorial will primarily consist of a presentation de-
livered through detailed slides to introduce and explain the
related technology. It is not a hands-on session; attendees will
not need to perform tasks during the tutorial.


### IX. Prior Offerings

Our tutorial will partly overlap with one tutorial made
titled RAG Meets LLMs: Towards
in KDD’24 presented,
Retrieval-Augmented Large Language Models1 [22] on August
25, 2024. It comprehensively reviews existing research studies
in retrieval-augmented large language models (RA-LLMs),
covering three primary technical perspectives: architectures,
training strategies, and applications. This tutorial and ours

1https://advanced-recommender-systems.github.io/RAG-Meets-LLMs/

cover two main technical parts of RAG: the model archi-
tecture and learning strategy. We believe these two aspects
are essential to learning in technical when teaching about
RAG. However, instead of introducing RAG for LLMs, we
pay special attention to how data management technologies
power retrieval-augmented generation. More specifically, we
will introduce several key methods highlighting the role of data
management technologies in enhancing retrieval-augmented
generation as well as challenges [23]. These include large-
scale vector search [16] and advanced indexing techniques,
such as graph-based similarity search [24]–[26], which facili-
tate efficient nearest-neighbor searches in large-scale datasets.
Dynamic embedding updates address embedding drift, en-
suring that the data storage remain relevant over time [27].
Furthermore, data management-powered frameworks enable
real-time query execution, crucial for applications requiring
immediate responses [20], [28]. These advancements under-
score the essential role of data management in scaling RAG
systems and delivering high-quality, contextually enriched
outputs.

REFERENCES

[1] T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal,

#### A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-
Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler,

#### J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray,

#### B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever,
and D. Amodei, “Language models are few-shot learners,” in Pro-
ceedings of the 34th International Conference on Neural Information
Processing Systems, ser. NIPS ’20. Curran Associates Inc., 2020.
[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
training of deep bidirectional transformers for language understanding,”
in Proceedings of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers).
Minneapolis,
Minnesota: Association for Computational Linguistics, 2019, pp. 4171–
4186.

[3] Z. Gekhman, G. Yona, R. Aharoni, M. Eyal, A. Feder, R. Reichart,
and J. Herzig, “Does fine-tuning LLMs on new knowledge encourage
hallucinations?” in Proceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing. Association for Computa-
tional Linguistics, 2024, pp. 7765–7784.

[4] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,

#### H. K¨uttler, M. Lewis, W.-t. Yih, T. Rockt¨aschel et al., “Retrieval-
augmented generation for knowledge-intensive nlp tasks,” Advances in
Neural Information Processing Systems, vol. 33, pp. 9459–9474, 2020.
[5] Y. Zhang, S. Sun, M. Galley, Y.-C. Chen, C. Brockett, X. Gao,

#### J. Gao, J. Liu, and B. Dolan, “DIALOGPT : Large-scale generative pre-
training for conversational response generation,” in Proceedings of the
58th Annual Meeting of the Association for Computational Linguistics:
System Demonstrations. Association for Computational Linguistics,
2020, pp. 270–278.
[6] K. Kharitonova, D.


#### J. Guti´errez-Hernando,
P´erez-Fern´andez,

#### A. Guti´errez-Fandi˜no, Z. Callejas, and D. Griol, “Leveraging retrieval-
augmented generation for reliable medical question answering using
large language models,” in International Conference on Hybrid Artificial
Intelligence Systems. Springer, 2024, pp. 141–153.

[7] G. Izacard and ´E. Grave, “Leveraging passage retrieval with genera-
tive models for open domain question answering,” in Proceedings of
the 16th Conference of the European Chapter of the Association for
Computational Linguistics: Main Volume, 2021, pp. 874–880.

[8] S. Singla, A. Eldawy, T. Diao, A. Mukhopadhyay, and E. Scudiero,
“Experimental study of big raster and vector database systems,” in
2021 IEEE 37th International Conference on Data Engineering (ICDE).
IEEE, 2021, pp. 2243–2248.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:55 UTC from IEEE Xplore. Restrictions apply.

4511

[9] K. Guu, K. Lee, Z. Tung, P. Pasupat, and M. Chang, “Retrieval
augmented language model pre-training,” in International conference
on machine learning. PMLR, 2020, pp. 3929–3938.

[10] G. Izacard, P. Lewis, M. Lomeli, L. Hosseini, F. Petroni, T. Schick,

#### J. Dwivedi-Yu, A. Joulin, S. Riedel, and E. Grave, “Atlas: Few-shot
learning with retrieval augmented language models,” Journal of Machine
Learning Research, vol. 24, no. 251, pp. 1–43, 2023.

[11] A. Asai, Z. Wu, Y. Wang, A. Sil, and H. Hajishirzi, “Self-rag: Self-
reflective retrieval augmented generation,” in NeurIPS 2023 Workshop
on Instruction Tuning and Instruction Following, 2023.

[12] S. Borgeaud, A. Mensch, J. Hoffmann, T. Cai, E. Rutherford, K. Milli-
can, G. B. Van Den Driessche, J.-B. Lespiau, B. Damoc, A. Clark et al.,
“Improving language models by retrieving from trillions of tokens,” in
International conference on machine learning. PMLR, 2022, pp. 2206–
2240.

[13] V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen,
and W.-t. Yih, “Dense passage retrieval for open-domain question an-
swering,” in Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), 2020, pp. 6769–6781.
[14] R. Ren, Y. Qu, J. Liu, W. X. Zhao, Q. She, H. Wu, H. Wang, and J.-R.
Wen, “Rocketqav2: A joint training method for dense passage retrieval
and passage re-ranking,” in Proceedings of the 2021 Conference on
Empirical Methods in Natural Language Processing, 2021, pp. 2825–
2835.

[15] K. Echihabi, K. Zoumpatianos, and T. Palpanas, “New trends in high-d
vector similarity search: al-driven, progressive, and distributed,” Pro-
ceedings of the VLDB Endowment, vol. 14, no. 12, pp. 3198–3201,
2021.

[16] J. Johnson, M. Douze, and H. J´egou, “Billion-scale similarity search
with gpus,” IEEE Transactions on Big Data, vol. 7, no. 3, pp. 535–547,
2019.

[17] Q. Chen, B. Zhao, H. Wang, M. Li, C. Liu, Z. Li, M. Yang, and J. Wang,
“Spann: Highly-efficient billion-scale approximate nearest neighborhood
search,” Advances in Neural Information Processing Systems, vol. 34,
pp. 5199–5212, 2021.

[18] C. Wei, B. Wu, S. Wang, R. Lou, C. Zhan, F. Li, and Y. Cai, “Analyticdb-
v: a hybrid analytical engine towards query fusion for structured and
unstructured data,” Proceedings of
the VLDB Endowment, vol. 13,
no. 12, pp. 3152–3165, 2020.

[19] H. Li, Q. Ai, J. Zhan, J. Mao, Y. Liu, Z. Liu, and Z. Cao, “Constructing
tree-based index for efficient and effective dense retrieval,” in Proceed-
ings of the 46th International ACM SIGIR Conference on Research and
Development in Information Retrieval, 2023, pp. 131–140.

[20] W. Jiang, S. Zhang, B. Han, J. Wang, B. Wang, and T. Kraska, “Piperag:
Fast retrieval-augmented generation via algorithm-system co-design,”
arXiv preprint arXiv:2403.05676, 2024.

[21] X. Zhao, X. Zhou, and G. Li, “Chat2data: An interactive data analysis
system with rag, vector databases and llms,” Proceedings of the VLDB
Endowment, vol. 17, no. 12, pp. 4481–4484, 2024.

[22] W. Fan, Y. Ding, L. Ning, S. Wang, H. Li, D. Yin, T.-S. Chua, and

#### Q. Li, “A survey on rag meeting llms: Towards retrieval-augmented large
language models,” in Proceedings of the 30th ACM SIGKDD Conference
on Knowledge Discovery and Data Mining, 2024, pp. 6491–6501.
[23] Y. Zhang, S. Liu, and J. Wang, “Are there fundamental limitations
in supporting vector data management in relational databases? a case
study of postgresql,” in International Conference on Data Engineering
(ICDE), 2024.

[24] P. Ciaccia, M. Patella, and P. Zezula, “M-tree: An efficient access method
for similarity search in metric spaces,” in Proceedings of the 23rd
International Conference on Very Large Data Bases, 1997, pp. 426–
435.

[25] Y. A. Malkov and D. A. Yashunin, “Efficient and robust approxi-
mate nearest neighbor search using hierarchical navigable small world
graphs,” IEEE transactions on pattern analysis and machine intelligence,
vol. 42, no. 4, pp. 824–836, 2018.

[26] I. Azizi, K. Echihabi, and T. Palpanas, “Elpis: Graph-based similarity
search for scalable data science,” Proceedings of the VLDB Endowment,
vol. 16, no. 6, pp. 1548–1559, 2023.

[27] R. Bamler and S. Mandt, “Dynamic word embeddings,” in International

conference on Machine learning. PMLR, 2017, pp. 380–389.

[28] Y. Su, Y. Sun, M. Zhang, and J. Wang, “Vexless: A serverless vector data
management system using cloud functions,” Proceedings of the ACM on
Management of Data, vol. 2, no. 3, pp. 1–26, 2024.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:55 UTC from IEEE Xplore. Restrictions apply.

4512


---

> *End of P-12*

<br><br>

<a id="p13-----unifying-large-language-models-and-knowledge-graphs-a-roadmap"></a>

## P-13 — Unifying Large Language Models and Knowledge Graphs: A Roadmap

| Field | Details |
|-------|---------|
| **Paper ID** | `P-13` |
| **Title** | Unifying Large Language Models and Knowledge Graphs: A Roadmap |
| **Authors** | Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, and Xindong Wu |
| **Affiliation(s)** | (1) Griffith University, Australia<br>(2) Monash University, Australia<br>(3) Nanyang Technological University, Singapore<br>(4) Beijing Jiaotong University, China<br>(5) Hefei University of Technology, China |
| **Venue** | IEEE Transactions on Knowledge and Data Engineering (TKDE) |
| **Volume / Year** | Vol. 36, No. 7, July 2024 |
| **DOI** | [10.1109/TKDE.2024.3352100](https://doi.org/10.1109/TKDE.2024.3352100) |

---

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

Unifying Large Language Models and Knowledge
Graphs: A Roadmap

Shirui Pan , Senior Member, IEEE, Linhao Luo , Yufei Wang, Chen Chen , Jiapu Wang ,
and Xindong Wu , Fellow, IEEE

(Survey Paper)


### Abstract

Large language models (LLMs), such as ChatGPT
and GPT4, are making new waves in the ﬁeld of natural language
processing and artiﬁcial intelligence, due to their emergent ability
and generalizability. However, LLMs are black-box models, which
often fall short of capturing and accessing factual knowledge. In
contrast, Knowledge Graphs (KGs), Wikipedia, and Huapu for
example, are structured knowledge models that explicitly store rich
factual knowledge. KGs can enhance LLMs by providing external
knowledge for inference and interpretability. Meanwhile, KGs are
difﬁcult to construct and evolve by nature, which challenges the
existing methods in KGs to generate new facts and represent unseen
knowledge. Therefore, it is complementary to unify LLMs and KGs
together and, simultaneously, leverage their advantages. In this
article, we present a forward-looking roadmap for the uniﬁcation
of LLMs and KGs. Our roadmap consists of three general frame-
works, namely: 1) KG-enhanced LLMs, which incorporate KGs
during the pre-training and inference phases of LLMs, or for the
purpose of enhancing understanding of the knowledge learned by
LLMs; 2) LLM-augmented KGs, that leverage LLMs for different
KG tasks such as embedding, completion, construction, graph-to-
text generation, and question answering; and 3) Synergized LLMs
+ KGs, in which LLMs and KGs play equal roles and work in a
mutually beneﬁcial way to enhance both LLMs and KGs for bidi-
rectional reasoning driven by both data and knowledge. We review
and summarize existing efforts within these three frameworks in
our roadmap and pinpoint their future research directions.

Manuscript received 26 June 2023; revised 27 December 2023; accepted
5 January 2024. Date of publication 10 January 2024; date of current version
10 June 2024. This work was supported by the Australian Research Council
(ARC) under Grants FT210100097 and DP240101547, and in part by the Na-
tional Natural Science Foundation of China (NSFC) under Grant 62120106008.
Recommended for acceptance by Yongxin Tong. (Shirui Pan and Linhao Luo
contributed equally to this work.) (Corresponding Author: Xindong Wu.)

Shirui Pan is with the School of Information and Communication Technology
and Institute for Integrated and Intelligent Systems (IIIS), Grifﬁth University,
Nathan, QLD 4111, Australia (e-mail: s.pan@grifﬁth.edu.au).

Linhao Luo and Yufei Wang are with the Department of Data Science
and AI, Monash University, Melbourne, VIC 3800, Australia (e-mail: linhao
.luo@monash.edu; garyyufei@gmail.com).

Chen Chen is with Nanyang Technological University, Singapore 639798

(e-mail: s190009@ntu.edu.sg).

Jiapu Wang is with the Faculty of Information Technology, Beijing University

of Technology, Beijing 100124, China (e-mail: jpwang@emails.bjut.edu.cn).

Xindong Wu is with the Key Laboratory of Knowledge Engineering with Big
Data (the Ministry of Education of China), Hefei University of Technology, Hefei
230002, China, and also with the Research Center for Knowledge Engineering,
Zhejiang Lab, Hangzhou 310058, China (e-mail: xwu@hfut.edu.cn).

This article has

supplementary downloadable material available at

https://doi.org/10.1109/TKDE.2024.3352100, provided by the authors.

Digital Object Identiﬁer 10.1109/TKDE.2024.3352100


### Index Terms / Keywords

Natural

large language
models, generative pre-training, knowledge graphs, roadmap,
bidirectional reasoning.

language processing,


### I. Introduction

L ARGE language models (LLMs)1

(e.g., BERT [1],
RoBERTA [2], and T5 [3]), pre-trained on the large-scale
corpus, have shown great performance in various natural lan-
guage processing (NLP) tasks, such as question answering [4],
machine translation [5], and text generation [6]. Recently, the
dramatically increasing model size further enables the LLMs
with the emergent ability [7], paving the road for applying LLMs
as Artiﬁcial General Intelligence (AGI). Advanced LLMs like
ChatGPT2 and PaLM23, with billions of parameters, exhibit
great potential in many complex practical tasks, such as edu-
cation [8], code generation [9] and recommendation [10].

Despite their success in many applications, LLMs have been
criticized for their lack of factual knowledge. Speciﬁcally, LLMs
memorize facts and knowledge contained in the training cor-
pus [14]. However, further studies reveal that LLMs are not able
to recall facts and often experience hallucinations by generating
statements that are factually incorrect [15], [28]. For example,
LLMs might say “Einstein discovered gravity in 1687” when
asked, “When did Einstein discover gravity?”, which contradicts
the fact that Isaac Newton formulated the gravitational theory.
This issue severely impairs the trustworthiness of LLMs.

As black-box models, LLMs are also criticized for their lack
of interpretability. LLMs represent knowledge implicitly in their
parameters. It is difﬁcult to interpret or validate the knowledge
obtained by LLMs. Moreover, LLMs perform reasoning by a
probability model, which is an indecisive process [16]. The
speciﬁc patterns and functions LLMs used to arrive at predic-
tions or decisions are not directly accessible or explainable to
humans [17]. Even though some LLMs are equipped to explain
their predictions by applying chain-of-thought [29], their reason-
ing explanations also suffer from the hallucination issue [30].
This severely impairs the application of LLMs in high-stakes
scenarios, such as medical diagnosis and legal judgment. For
instance, in a medical diagnosis scenario, LLMs may incorrectly

1LLMs are also known as pre-trained language models (PLMs).
2https://openai.com/blog/chatgpt
3https://ai.google/discover/palm2

1041-4347 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3581

In LLM-augmented KGs, LLMs have been used in various KG-
related tasks, e.g., KG embedding [40], KG completion [26], KG
construction [41], KG-to-text generation [42], and KGQA [43],
to improve the performance and facilitate the application of KGs.
In Synergized LLM + KG, researchers marries the merits of
LLMs and KGs to mutually enhance performance in knowledge
representation [44] and reasoning [45], [46]. Although there are
some surveys on knowledge-enhanced LLMs [47], [48], [49],
which mainly focus on using KGs as an external knowledge
to enhance LLMs, they ignore other possibilities of integrating
KGs for LLMs and the potential role of LLMs in KG applica-
tions.

In this article, we present a forward-looking roadmap for
unifying both LLMs and KGs, to leverage their respective
strengths and overcome the limitations of each approach, for
various downstream tasks. We propose detailed categorization,
conduct comprehensive reviews, and pinpoint emerging direc-
tions in these fast-growing ﬁelds. Our main contributions are
summarized as follows:

1) Roadmap: We present a forward-looking roadmap for
integrating LLMs and KGs. Our roadmap, consisting
of three general frameworks to unify LLMs and KGs,
namely, KG-enhanced LLMs, LLM-augmented KGs, and
Synergized LLMs + KGs, provides guidelines for the uni-
ﬁcation of these two distinct but complementary technolo-
gies.

2) Categorization and review: For each integration frame-
work of our roadmap, we present a detailed categorization
and novel taxonomies of research on unifying LLMs and
KGs. In each category, we review the research from the
perspectives of different integration strategies and tasks,
which provides more insights into each framework.
3) Coverage of emerging advances: We cover the advanced
techniques in both LLMs and KGs. We include the discus-
sion of state-of-the-art LLMs like ChatGPT and GPT-4
as well as the novel KGs e.g., multi-modal knowledge
graphs.

4) Summary of challenges and future directions: We high-
light the challenges in existing research and present several
promising future research directions.

The rest of this article is organized as follows. Section II
ﬁrst explains the background of LLMs and KGs. Section III
introduces the roadmap and the overall categorization of this
article. Section IV presents the different KGs-enhanced LLM
approaches. Section V describes the possible LLM-augmented
KG methods. Section VI shows the approaches of synergizing
LLMs and KGs. Section VII discusses the challenges and future
research directions. Finally, Section VIII concludes this paper.


### II. Background

In this section, we will ﬁrst brieﬂy introduce a few represen-
tative large language models (LLMs) and discuss the prompt
engineering that efﬁciently uses LLMs for varieties of appli-
cations. Then, we illustrate the concept of knowledge graphs
(KGs) and present different categories of KGs.

Summarization of the pros and cons for LLMs and KGs. LLM pros:
Fig. 1.
General Knowledge [11], Language Processing [12], Generalizability [13];
LLM cons: Implicit Knowledge [14], Hallucination [15], Indecisiveness [16],
Black-box [17], Lacking Domain-speciﬁc/New Knowledge [18]. KG pros: Struc-
tural Knowledge [19], Accuracy [20], Decisiveness [21], Interpretability [22],
Domain-speciﬁc Knowledge [23], Evolving Knowledge [24]; KG cons: Incom-
pleteness [25], Lacking Language Understanding [26], Unseen Facts [27]. Pros.
and Cons. are selected based on their representativeness. Detailed discussion can
be found in Appendix A, available online.

diagnose a disease and provide explanations that contradict med-
ical commonsense. This raises another issue that LLMs trained
on general corpus might not be able to generalize well to speciﬁc
domains or new knowledge due to the lack of domain-speciﬁc
knowledge or new training data [18].

To address the above issues, a potential solution is to in-
corporate knowledge graphs (KGs) into LLMs. Knowledge
graphs (KGs), storing enormous facts in the way of triples, i.e.,
(head entity, relation, tail entity), are a structured and deci-
sive manner of knowledge representation (e.g., Wikidata [20],
YAGO [31], and NELL [32]). KGs are crucial for various appli-
cations as they offer accurate explicit knowledge [19]. Besides,
they are renowned for their symbolic reasoning ability [22],
which generates interpretable results. KGs can also actively
evolve with new knowledge continuously added in [24]. Addi-
tionally, experts can construct domain-speciﬁc KGs to provide
precise and dependable domain-speciﬁc knowledge [23].

Nevertheless, KGs are difﬁcult to construct [25], and current
approaches in KGs [27], [33], [34] are inadequate in handling the
incomplete and dynamically changing nature of real-world KGs.
These approaches fail to effectively model unseen entities and
represent new facts. In addition, they often ignore the abundant
textual information in KGs. Moreover, existing methods in KGs
are often customized for speciﬁc KGs or tasks, which are not
generalizable enough. Therefore, it is also necessary to utilize
LLMs to address the challenges faced in KGs. We summarize
the pros and cons of LLMs and KGs in Fig. 1, respectively.

Recently, the possibility of unifying LLMs with KGs has
attracted increasing attention from researchers and practitioners.
LLMs and KGs are inherently interconnected and can mutually
enhance each other. In KG-enhanced LLMs, KGs can not only be
incorporated into the pre-training and inference stages of LLMs
to provide external knowledge [35], [36], [37], but also used for
analyzing LLMs and providing interpretability [14], [38], [39].

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3582

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

Fig. 2. Representative large language models (LLMs) in recent years. Open-source models are represented by solid squares, while closed source models are
represented by hollow squares.

the entire sentence, such as text classiﬁcation [26] and named
entity recognition [53].

2) Encoder-Decoder LLMs: Encoder-decoder

large lan-
guage models adopt both the encoder and decoder module. The
encoder module is responsible for encoding the input sentence
into a hidden-space, and the decoder is used to generate the
target output text. The training strategies in encoder-decoder
LLMs can be more ﬂexible. For example, T5 [3] is pre-trained
by masking and predicting spans of masking words. UL2 [54]
uniﬁes several training targets such as different masking spans
and masking frequencies. Encoder-decoder LLMs (e.g., T0 [55],
ST-MoE [56], and GLM-130B [57]) are able to directly resolve
tasks that generate sentences based on some context, such as
summariaztion, translation, and question answering [58].

3) Decoder-Only LLMs: Decoder-only large language mod-
els only adopt the decoder module to generate target output
text. The training paradigm for these models is to predict the
next word in the sentence. Large-scale decoder-only LLMs can
generally perform downstream tasks from a few examples or
simple instructions, without adding prediction heads or ﬁnetun-
ing [59]. Many state-of-the-art LLMs (e.g., Chat-GPT [60] and
GPT-44) follow the decoder-only architecture. However, since
these models are closed-source, it is challenging for academic
researchers to conduct further research. Recently, Alpaca5 and
Vicuna6 are released as open-source decoder-only LLMs. These
models are ﬁnetuned based on LLaMA [61] and achieve com-
parable performance with ChatGPT and GPT-4.

4) Prompt Engineering: Prompt engineering is a novel ﬁeld
that focuses on creating and reﬁning prompts to maximize the

4https://openai.com/product/gpt-4
5https://github.com/tatsu-lab/stanford_alpaca
6https://lmsys.org/blog/2023-03-30-vicuna/

Fig. 3.
anism.

Illustration of the Transformer-based LLMs with self-attention mech-


#### A. Large Language Models (LLMs)

Large language models (LLMs) pre-trained on large-scale
corpus have shown great potential in various NLP tasks [13].
As shown in Fig. 3, most LLMs derive from the Transformer
design [50], which contains the encoder and decoder mod-
ules empowered by a self-attention mechanism. Based on the
architecture structure, LLMs can be categorized into three
groups: 1) encoder-only LLMs, 2) encoder-decoder LLMs, and
3) decoder-only LLMs. As shown in Fig. 2, we summarize
several representative LLMs with different model architectures,
model sizes, and open-source availabilities.

1) Encoder-Only LLMs: Encoder-only large language mod-
els only use the encoder to encode the sentence and under-
stand the relationships between words. The common training
paradigm for these model is to predict the mask words in an input
sentence. This method is unsupervised and can be trained on
the large-scale corpus. Encoder-only LLMs like BERT [1], AL-
BERT [51], RoBERTa [2], and ELECTRA [52] require adding
an extra prediction head to resolve downstream tasks. These
models are most effective for tasks that require understanding

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3583

Fig. 4. Example of sentiment classiﬁcation prompt.

effectiveness of large language models (LLMs) across various
applications and research areas [62]. As shown in Fig. 4, a
prompt is a sequence of natural language inputs for LLMs
that are speciﬁed for the task, such as sentiment classiﬁcation.
A prompt could contain several elements, i.e., 1) Instruction,
2) Context, and 3) Input Text. Instruction is a short sentence that
instructs the model to perform a speciﬁc task. Context provides
the context for the input text or few-shot examples. Input Text is
the text that needs to be processed by the model.

Prompt engineering seeks to improve the capacity of large
large language models (e.g., ChatGPT) in diverse complex
tasks such as question answering, sentiment classiﬁcation, and
common sense reasoning. Chain-of-thought (CoT) prompt [63]
enables complex reasoning capabilities through intermediate
reasoning steps. Prompt engineering also enables the integration
of structural data like knowledge graphs (KGs) into LLMs. Li
et al. [64] simply linearizes the KGs and uses templates to
convert the KGs into passages. Mindmap [65] designs a KG
prompt to convert graph structure into a mind map that enables
LLMs to perform reasoning on it. Prompt offers a simple way
to utilize the potential of LLMs without ﬁnetuning. Proﬁciency
in prompt engineering leads to a better understanding of the
strengths and weaknesses of LLMs.


#### B. Knowledge Graphs (KGs)

Knowledge graphs (KGs) store structured knowledge as a
collection of triples KG = {(h, r, t) ⊆ E × R × E}, where E
and R respectively denote the set of entities and relations.
Existing knowledge graphs (KGs) can be classiﬁed into four
groups based on the stored information: 1) encyclopedic KGs,
2) commonsense KGs, 3) domain-speciﬁc KGs, and 4) multi-
modal KGs. We illustrate the examples of KGs of different
categories in Fig. 5.

1) Encyclopedic Knowledge Graphs: Encyclopedic knowl-
edge graphs are the most ubiquitous KGs, which represent
the general knowledge in real-world. Encyclopedic knowledge
graphs are often constructed by integrating information from
diverse and extensive sources, including human experts, ency-
clopedias, and databases. Wikidata [20] is one of the most widely

Fig. 5. Examples of different categories’ knowledge graphs, i.e., encyclopedic
KGs, commonsense KGs, domain-speciﬁc KGs, and multi-modal KGs.

used encyclopedic knowledge graphs, which incorporates vari-
eties of knowledge extracted from articles on Wikipedia. Other
typical encyclopedic knowledge graphs, like Freebase [66],
Dbpedia [67], and YAGO [31] are also derived from Wikipedia.
In addition, NELL [32] is a continuously improving encyclo-
pedic knowledge graph, which automatically extracts knowl-
edge from the web, and uses that knowledge to improve its
performance over time. There are several encyclopedic knowl-
edge graphs available in languages other than English such
as CN-DBpedia [68] and Vikidia [69]. The largest knowledge
graph, named Knowledge Occean (KO)7, currently contains
4,8784,3636 entities and 17,3115,8349 relations in both English
and Chinese.

as

as well

Knowledge

and events,

e.g., objects,

2) Commonsense

Graphs: Commonsense
knowledge graphs formulate the knowledge about daily
their
concepts,
relationships [70]. Compared with encyclopedic knowledge
graphs, commonsense knowledge graphs often model the tacit
knowledge extracted from text such as (Car, UsedFor, Drive).
ConceptNet [71] contains a wide range of commonsense
concepts and relations, which can help computers understand
the meanings of words people use. ATOMIC [72], [73]
and ASER [74] focus on the causal effects between events,
which can be used for commonsense reasoning. Some other
commonsense knowledge graphs, such as TransOMCS [75]
and CausalBanK [76] are automatically constructed to provide
commonsense knowledge.

7https://ko.zhonghuapu.com/

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3584

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

TABLE I
REPRESENTATIVE APPLICATIONS OF USING LLMS AND KGS


#### A. Roadmap

The roadmap of unifying KGs and LLMs is illustrated in
Fig. 6. In the roadmap, we identify three frameworks for the
uniﬁcation of LLMs and KGs, including KG-enhanced LLMs,
LLM-augmented KGs, and Synergized LLMs + KGs. The KG-
enhanced LLMs and LLM-augmented KGs are two parallel
frameworks that aim to enhance the capabilities of LLMs and
KGs, respectively. Building upon these frameworks, Synergized
LLMs + KGs is a uniﬁed framework that aims to synergize LLMs
and KGs to mutually enhance each other.

1) Kg-Enhanced LLMs: LLMs are renowned for their ability
to learn knowledge from large-scale corpus and achieve state-of-
the-art performance in various NLP tasks. However, LLMs are
often criticized for their hallucination issues [15], and lacking
of interpretability. To address these issues, researchers have
proposed to enhance LLMs with knowledge graphs (KGs).

KGs store enormous knowledge in an explicit and structured
way, which can be used to enhance the knowledge awareness
of LLMs. Some researchers have proposed to incorporate KGs
into LLMs during the pre-training stage, which can help LLMs
learn knowledge from KGs [35], [91]. Other researchers have
proposed to incorporate KGs into LLMs during the inference
stage. By retrieving knowledge from KGs, it can signiﬁcantly
improve the performance of LLMs in accessing domain-speciﬁc
knowledge [92]. To improve the interpretability of LLMs, re-
searchers also utilize KGs to interpret the facts [14] and the
reasoning process of LLMs [38].

2) Llm-Augmented KGs: KGs store structure knowledge
playing an essential role in many real-word applications [19].
Existing methods in KGs fall short of handling incomplete
KGs [33] and processing text corpus to construct KGs [93].
With the generalizability of LLMs, many researchers are trying
to harness the power of LLMs for addressing KG-related tasks.
The most straightforward way to apply LLMs as text encoders
for KG-related tasks. Researchers take advantage of LLMs to
process the textual corpus in the KGs and then use the repre-
sentations of the text to enrich KGs representation [94]. Some
studies also use LLMs to process the original corpus and extract
relations and entities for KG construction [95]. Recent studies
try to design a KG prompt that can effectively convert structural
KGs into a format that can be comprehended by LLMs. In this
way, LLMs can be directly applied to KG-related tasks, e.g., KG
completion [96] and KG reasoning [97].

3) Synergized LLMs + KGs: The synergy of LLMs and
KGs has attracted increasing attention from researchers these
years [40], [42]. LLMs and KGs are two inherently comple-
mentary techniques, which should be uniﬁed into a general
framework to mutually enhance each other.

To further explore the uniﬁcation, we propose a uniﬁed frame-
work of the synergized LLMs + KGs in Fig. 7. The uniﬁed
framework contains four layers: 1) Data, 2) Synergized Model,
3) Technique, and 4) Application. In the Data layer, LLMs
and KGs are used to process the textual and structural data,
respectively. With the development of multi-modal LLMs [98]
and KGs [99], this framework can be extended to process multi-
modal data, such as video, audio, and images. In the Synergized
Model layer, LLMs and KGs could synergize with each other to

3) Domain-Speciﬁc Knowledge Graphs: Domain-speciﬁc
knowledge graphs are often constructed to represent knowl-
edge in a speciﬁc domain, e.g., medical, biology, and ﬁ-
nance [23]. Compared with encyclopedic knowledge graphs,
domain-speciﬁc knowledge graphs are often smaller in size,
but more accurate and reliable. For example, UMLS [77] is
a domain-speciﬁc knowledge graph in the medical domain,
which contains biomedical concepts and their relationships. In
addition, there are some domain-speciﬁc knowledge graphs in
other domains, such as ﬁnance [78], geology [79], biology [80],
chemistry [81] and genealogy [82].

4) Multi-Modal Knowledge Graphs: Unlike conventional
knowledge graphs that only contain textual information, multi-
modal knowledge graphs represent facts in multiple modali-
ties such as images, sounds, and videos [83]. For example,
IMGpedia [84], MMKG [85], and Richpedia [86] incorporate
both the text and image information into the knowledge graphs.
These knowledge graphs can be used for various multi-modal
tasks such as image-text matching [87], visual question answer-
ing [88], and recommendation [89].


#### C. Applications

LLMs as KGs have been widely applied in various real-world
applications. We summarize some representative applications
of using LLMs and KGs in Table I. ChatGPT/GPT-4 are LLM-
based chatbots that can communicate with humans in a natural
dialogue format. To improve knowledge awareness of LLMs,
ERNIE 3.0 and Bard incorporate KGs into their chatbot applica-
tions. Instead of Chatbot. Fireﬂy develops a photo editing appli-
cation that allows users to edit photos by using natural language
descriptions. Copilot, New Bing, and Shop.ai adopt LLMs to
empower their applications in the areas of coding assistant, web
search, and recommendation, respectively. Wikidata and KO are
two representative knowledge graph applications that are used to
provide external knowledge. OpenBG [90] is a knowledge graph
designed for recommendation. Doctor.ai develops a health care
assistant that incorporates LLMs and KGs to provide medical
advice.


### III. Roadmap & Categorization

In this section, we ﬁrst present a road map of explicit frame-
works that unify LLMs and KGs. Then, we present the catego-
rization of research on unifying LLMs and KGs.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3585

Fig. 6. General roadmap of unifying KGs and LLMs.

1) KG-enhanced LLM pre-training includes works that ap-
ply KGs during the pre-training stage and improve the
knowledge expression of LLMs.

2) KG-enhanced LLM inference includes research that uti-
lizes KGs during the inference stage of LLMs, which
enables LLMs to access the latest knowledge without
retraining.

3) KG-enhanced LLM interpretability includes works that
use KGs to understand the knowledge learned by LLMs
and interpret the reasoning process of LLMs.

LLM-augmented KGs: LLMs can be applied to augment
various KG-related tasks. We categorize the research on LLM-
augmented KGs into ﬁve groups based on the task types:

1) LLM-augmented KG embedding includes studies that ap-
ply LLMs to enrich representations of KGs by encoding
the textual descriptions of entities and relations.

2) LLM-augmented KG completion includes papers that uti-
lize LLMs to encode text or generate facts for better KGC
performance.

3) LLM-augmented KG construction includes works that
apply LLMs to address the entity discovery, coreference
resolution, and relation extraction tasks for KG construc-
tion.

4) LLM-augmented KG-to-text Generation includes research
that utilizes LLMs to generate natural language that de-
scribes the facts from KGs.

5) LLM-augmented KG question answering includes studies
that apply LLMs to bridge the gap between natural lan-
guage questions and retrieve answers from KGs.

Synergized LLMs + KGs: The synergy of LLMs and KGs aims
to integrate LLMs and KGs into a uniﬁed framework to mutually
enhance each other. In this categorization, we review the recent
attempts of Synergized LLMs + KGs from the perspectives of
knowledge representation and reasoning.

In the following sections (Sec Sections IV, V, and VI), we

will provide details on these categorizations.


### IV. Kg-Enhanced Llms

Large language models (LLMs) achieve promising results
in many natural language processing tasks. However, LLMs
have been criticized for their lack of practical knowledge and
tendency to generate factual errors during inference. To address

Fig. 7. General framework of the Synergized LLMs + KGs, which contains
four layers: 1) Data, 2) Synergized Model, 3) Technique, and 4) Application.

improve their capabilities. In Technique layer, related techniques
that have been used in LLMs and KGs can be incorporated
into this framework to further enhance the performance. In the
Application layer, LLMs and KGs can be integrated to address
various real-world applications, such as search engines [100],
recommender systems [10], and AI assistants [101].


#### B. Categorization

To better understand the research on unifying LLMs and
KGs, we further provide a ﬁne-grained categorization for each
framework in the roadmap. Speciﬁcally, we focus on different
ways of integrating KGs and LLMs, i.e., KG-enhanced LLMs,
KG-augmented LLMs, and Synergized LLMs + KGs. The ﬁne-
grained categorization of the research is illustrated in Fig. 8.

KG-enhanced LLMs: Integrating KGs can enhance the per-
formance and interpretability of LLMs in various downstream
tasks. We categorize the research on KG-enhanced LLMs into
three groups:

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3586

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

Fig. 8.

Fine-grained categorization of research on unifying large language models (LLMs) with knowledge graphs (KGs).

TABLE II
SUMMARY OF KG-ENHANCED LLM METHODS

this issue, researchers have proposed integrating knowledge
graphs (KGs) to enhance LLMs. In this section, we ﬁrst intro-
duce the KG-enhanced LLM pre-training, which aims to inject
knowledge into LLMs during the pre-training stage. Then, we in-
troduce the KG-enhanced LLM inference, which enables LLMs
to consider the latest knowledge while generating sentences.
Finally, we introduce the KG-enhanced LLM interpretability,
which aims to improve the interpretability of LLMs by using
KGs. Table II summarizes the typical methods that integrate
KGs for LLMs.


#### A. KG-Enhanced LLM Pre-Training

Existing large language models mostly rely on unsupervised
training on the large-scale corpus. While these models may
exhibit impressive performance on downstream tasks, they often
lack practical knowledge relevant to the real world. Previous
works that integrate KGs into large language models can be
categorized into three parts: 1) Integrating KGs into training

objective, 2) Integrating KGs into LLM inputs, and 3) KGs
Instruction-tuning.

1) Integrating KGs Into Training Objective: The research
efforts in this category focus on designing novel knowledge-
aware training objectives. An intuitive idea is to expose more
knowledge entities in the pre-training objective. GLM [102]
leverages the knowledge graph structure to assign a masking
probability. Speciﬁcally, entities that can be reached within a
certain number of hops are considered to be the most important
entities for learning, and they are given a higher masking prob-
ability during pre-training. Furthermore, E-BERT [103] further
controls the balance between the token-level and entity-level
training losses. The training loss values are used as indications
of the learning process for token and entity, which dynamically
determines their ratio for the next training epochs. SKEP [124]
also follows a similar fusion to inject sentiment knowledge
during LLMs pre-training. SKEP ﬁrst determines words with
positive and negative sentiment by utilizing PMI along with a
predeﬁned set of seed sentiment words. Then, it assigns a higher
masking probability to those identiﬁed sentiment words in the
word masking objective.

The other line of work explicitly leverages the connections
with knowledge and input text. As shown in Fig. 9, ERNIE [35]
proposes a novel word-entity alignment training objective as a
pre-training objective. Speciﬁcally, ERNIE feeds both sentences
and corresponding entities mentioned in the text into LLMs, and
then trains the LLMs to predict alignment links between textual
tokens and entities in knowledge graphs. Similarly, KALM [91]
enhances the input tokens by incorporating entity embeddings
and includes an entity prediction pre-training task in addition
to the token-only pre-training objective. This approach aims to
improve the ability of LLMs to capture knowledge related to
entities. Finally, KEPLER [40] directly employs both knowl-
edge graph embedding training objective and Masked token
pre-training objective into a shared transformer-based encoder.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3587

the input sentences form a fully connected word graph where
tokens aligned with knowledge entities are connected with their
neighboring entities.

The above methods can indeed inject a large amount of knowl-
edge into LLMs. However, they mostly focus on popular entities
and overlook the low-frequent and long-tail ones. DkLLM [108]
aims to improve the LLMs representations towards those enti-
ties. DkLLM ﬁrst proposes a novel measurement to determine
long-tail entities and then replaces these selected entities in the
text with pseudo token embedding as new input to the large
language models. Furthermore, Dict-BERT [125] proposes to
leverage external dictionaries to solve this issue. Speciﬁcally,
Dict-BERT improves the representation quality of rare words
by appending their deﬁnitions from the dictionary at the end of
input text and trains the language model to locally align rare word
representations in input sentences and dictionary deﬁnitions as
well as to discriminate whether the input text and deﬁnition are
correctly mapped.

3) KGs Instruction-Tuning: Instead of

injecting factual
knowledge into LLMs, the KGs Instruction-tuning aims to ﬁne-
tune LLMs to better comprehend the structure of KGs and effec-
tively follow user instructions to conduct complex tasks. KGs
Instruction-tuning utilizes both facts and the structure of KGs
to create instruction-tuning datasets. LLMs ﬁnetuned on these
datasets can extract both factual and structural knowledge from
KGs, enhancing the reasoning ability of LLMs. KP-PLM [109]
ﬁrst designs several prompt templates to transfer structural
graphs into natural language text. Then, two self-supervised
tasks are proposed to ﬁnetune LLMs to further leverage the
knowledge from these prompts. OntoPrompt [110] proposes an
ontology-enhanced prompt-tuning that can place knowledge of
entities into the context of LLMs, which are further ﬁnetuned
on several downstream tasks. ChatKBQA [111] ﬁnetunes LLMs
on KG structure to generate logical queries, which can be
executed on KGs to obtain answers. To better reason on graphs,
RoG [112] presents a planning-retrieval-reasoning framework.
RoG is ﬁnetuned on KG structure to generate relation paths
grounded by KGs as faithful plans. These plans are then used to
retrieve valid reasoning paths from the KGs for LLMs to conduct
faithful reasoning and generate interpretable results.

KGs Instruction-tuning can better leverage the knowledge
from KGs for downstream tasks. However, it requires retrain-
ing the models, which is time-consuming and requires lots of
resources.


#### B. KG-Enhanced LLM Inference

The above methods could effectively fuse knowledge into
LLMs. However, real-world knowledge is subject to change and
the limitation of these approaches is that they do not permit
updates to the incorporated knowledge without retraining the
model. As a result, they may not generalize well to the unseen
knowledge during inference [126]. Therefore, considerable re-
search has been devoted to keeping the knowledge space and
text space separate and injecting the knowledge while inference.
These methods mostly focus on the Question Answering (QA)
tasks, because QA requires the model to capture both textual
semantic meanings and up-to-date real-world knowledge.

Fig. 9.
Injecting KG information into LLMs training objective via text-
knowledge alignment loss, where h denotes the hidden representation generated
by LLMs.

Fig. 10.

Injecting KG information into LLMs inputs using graph structure.

Deterministic LLM [104] focuses on pre-training language mod-
els to capture deterministic factual knowledge. It only masks the
span that has a deterministic entity as the question and introduces
additional clue contrast learning and clue classiﬁcation objec-
tive. WKLM [106] ﬁrst replaces entities in the text with other
same-type entities and then feeds them into LLMs. The model is
further pre-trained to distinguish whether the entities have been
replaced or not.

2) Integrating KGs Into LLM Inputs: As shown in Fig. 10,
this kind of research focus on introducing relevant knowledge
sub-graph into the inputs of LLMs. Given a knowledge graph
triple and the corresponding sentences, ERNIE 3.0 [101] repre-
sents the triple as a sequence of tokens and directly concatenates
them with the sentences. It further randomly masks either the
relation token in the triple or tokens in the sentences to bet-
ter combine knowledge with textual representations. However,
such direct knowledge triple concatenation method allows the
tokens in the sentence to intensively interact with the tokens
in the knowledge sub-graph, which could result in Knowledge
Noise [36]. To solve this issue, K-BERT [36] takes the ﬁrst step
to inject the knowledge triple into the sentence via a visible
matrix where only the knowledge entities have access to the
knowledge triple information, while the tokens in the sentences
can only see each other in the self-attention module. To fur-
ther reduce Knowledge Noise, Colake [107] proposes a uniﬁed
word-knowledge graph (shown in Fig. 10) where the tokens in

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3588

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

are prompted to generate meaningful logical rules that can be
used for reasoning. CoK [117] proposes a chain-of-knowledge
prompting that uses a sequence of triples to elicit the reasoning
ability of LLMs to reach the ﬁnal answer.

KGs prompting presents a simple way to synergize LLMs and
KGs. By using the prompt, we can easily harness the power of
LLMs to perform reasoning based on KGs without retraining
the models. However, the prompt is usually designed manually,
which requires lots of human effort.


#### C. Comparison Between KG-Enhanced LLM Pre-Training
and Inference

KG-enhanced LLM Pre-training methods commonly enrich
large-amount of unlabeled corpus with semantically relevant
real-world knowledge. These methods allow the knowledge rep-
resentations to be aligned with appropriate linguistic context and
explicitly train LLMs to leverage those knowledge from scratch.
When applying the resulting LLMs to downstream knowledge-
intensive tasks, they should achieve optimal performance. In
contrast, KG-enhanced LLM inference methods only present the
knowledge to LLMs in the inference stage and the underlying
LLMs may not be trained to fully leverage these knowledge
when conducting downstream tasks, potentially resulting in
sub-optimal model performance.

However, real-world knowledge is dynamic and requires
frequent updates. Despite being effective, the KG-enhanced
LLM Pre-training methods never permit knowledge updates or
editing without model re-training. As a result, the KG-enhanced
LLM Pre-training methods could generalize poorly to recent or
unseen knowledge. KG-enhanced LLM inference methods can
easily maintain knowledge updates by changing the inference
inputs. These methods help improve LLMs performance on new
knowledge and domains.

In summary, when to use these methods depends on the appli-
cation scenarios. If one wishes to apply LLMs to handle time-
insensitive knowledge in particular domains (e.g., commonsense
and reasoning knowledge), KG-enhanced LLM Pre-training
methods should be considered. Otherwise, KG-enhanced LLM
inference methods can be used to handle open-domain knowl-
edge with frequent updates.


#### D. KG-Enhanced LLM Interpretability

Although LLMs have achieved remarkable success in many
NLP tasks, they are still criticized for their lack of interpretabil-
ity. The large language model (LLM) interpretability refers to
the understanding and explanation of the inner workings and
decision-making processes of a large language model [17]. This
can improve the trustworthiness of LLMs and facilitate their
applications in high-stakes scenarios such as medical diagnosis
and legal judgment. Knowledge graphs (KGs) represent the
knowledge structurally and can provide good interpretability for
the reasoning results. Therefore, researchers try to utilize KGs
to improve the interpretability of LLMs, which can be roughly
grouped into two categories: 1) KGs for language model probing,
and 2) KGs for language model analysis.

Fig. 11. Retrieving external knowledge to enhance the LLM generation.

1) Retrieval-Augmented Knowledge Fusion: Retrieval-
Augmented Knowledge Fusion is a popular method to inject
knowledge into LLMs during inference. The key idea is to
retrieve relevant knowledge from a large corpus and then fuse
the retrieved knowledge into LLMs. As shown in Fig. 11,
RAG [92] proposes to combine non-parametric and parametric
modules to handle the external knowledge. Given the input
text, RAG ﬁrst searches for relevant KG in the non-parametric
module via MIPS to obtain several documents. RAG then treats
these documents as hidden variables z and feeds them into the
output generator, empowered by Seq2Seq LLMs, as additional
context information. The research indicates that using different
retrieved documents as conditions at different generation
steps performs better than only using a single document
to guide the whole generation process. The experimental
results show that RAG outperforms other parametric-only and
non-parametric-only baseline models in open-domain QA.
RAG can also generate more speciﬁc, diverse, and factual text
than other parameter-only baselines. Story-fragments [127]
further improves architecture by adding an additional module
to determine salient knowledge entities and fuse them into
the generator to improve the quality of generated long stories.
EMAT [115] further improves the efﬁciency of such a system
by encoding external knowledge into a key-value memory and
exploiting the fast maximum inner product search for memory
querying. REALM [114] proposes a novel knowledge retriever
to help the model to retrieve and attend over documents from
a large corpus during the pre-training stage and successfully
improves the performance of open-domain question answering.
KGLM [113] selects the facts from a knowledge graph using
the current context to generate factual sentences. With the help
of an external knowledge graph, KGLM could describe facts
using out-of-domain words or phrases.

2) KGs Prompting: To better feed the KG structure into the
LLM during inference, KGs prompting aims to design a crafted
prompt that converts structured KGs into text sequences, which
can be fed as context into LLMs. In this way, LLMs can better
take advantage of the structure of KGs to perform reasoning. Li
et al. [64] adopt the pre-deﬁned template to convert each triple
into a short sentence, which can be understood by LLMs for
reasoning. Mindmap [65] designs a KG prompt to convert graph
structure into a mind map that enables LLMs to perform reason-
ing by consolidating the facts in KGs and the implicit knowledge
from LLMs. ChatRule [116] samples several relation paths from
KGs, which are verbalized and fed into LLMs. Then, LLMs

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3589

Fig. 12. General framework of using knowledge graph for language model
probing.

1) KGs for LLM Probing: The large language model (LLM)
probing aims to understand the knowledge stored in LLMs.
LLMs, trained on large-scale corpus, are often known as con-
taining enormous knowledge. However, LLMs store the knowl-
edge in a hidden way, making it hard to ﬁgure out the stored
knowledge. Moreover, LLMs suffer from the hallucination prob-
lem [15], which results in generating statements that contradict
facts. This issue signiﬁcantly affects the reliability of LLMs.
Therefore, it is necessary to probe and verify the knowledge
stored in LLMs.

LAMA [14] is the ﬁrst work to probe the knowledge in LLMs
by using KGs. As shown in Fig. 12, LAMA ﬁrst converts the facts
in KGs into cloze statements by a pre-deﬁned prompt template
and then uses LLMs to predict the missing entity. The prediction
results are used to evaluate the knowledge stored in LLMs. For
example, we try to probe whether LLMs know the fact (Obama,
profession, president). We ﬁrst convert the fact triple into a cloze
question “Obama’s profession is _.” with the object masked.
Then, we test if the LLMs can predict the object “president”
correctly.

However, LAMA ignores the fact that the prompts are inap-
propriate. For example, the prompt “Obama worked as a _” may
be more favorable to the prediction of the blank by the language
models than “Obama is a _ by profession”. Thus, LPAQA [118]
proposes a mining and paraphrasing-based method to automat-
ically generate high-quality and diverse prompts for a more
accurate assessment of the knowledge contained in the language
model. Moreover, Adolphs et al. [128] attempt to use exam-
ples to make the language model understand the query, and
experiments obtain substantial improvements for BERT-large
on the T-REx data. Unlike using manually deﬁned prompt
templates, Autoprompt [119] proposes an automated method,
which is based on the gradient-guided search to create prompts.
LLM-facteval [121] designs a systematic framework that auto-
matically generates probing questions from KGs. The generated
questions are then used to evaluate the factual knowledge stored
in LLMs.

Instead of probing the general knowledge by using the ency-
clopedic and commonsense knowledge graphs, BioLAMA [129]
and MedLAMA [120] probe the medical knowledge in LLMs
by using medical knowledge graphs. Alex et al. [130] investigate
the capacity of LLMs to retain less popular factual knowledge.
They select unpopular facts from Wikidata knowledge graphs
which have low-frequency clicked entities. These facts are then

Fig. 13. General framework of using knowledge graph for language model
analysis.

used for the evaluation, where the results indicate that LLMs
encounter difﬁculties with such knowledge, and that scaling fails
to appreciably improve memorization of factual knowledge in
the tail.

2) KGs for LLM Analysis: Knowledge graphs (KGs) for
pre-train language models (LLMs) analysis aims to answer the
following questions such as “how do LLMs generate the re-
sults?”, and “how do the function and structure work in LLMs?”.
To analyze the inference process of LLMs, as shown in Fig. 13,
KagNet [38] and QA-GNN [131] make the results generated by
LLMs at each reasoning step grounded by knowledge graphs.
In this way, the reasoning process of LLMs can be explained
by extracting the graph structure from KGs. Shaobo et al. [123]
investigate how LLMs generate the results correctly. They adopt
the causal-inspired analysis from facts extracted from KGs. This
analysis quantitatively measures the word patterns that LLMs
depend on to generate the results. The results show that LLMs
generate the missing factual more by the positionally closed
words rather than the knowledge-dependent words. Thus, they
claim that LLMs are inadequate to memorize factual knowledge
because of the inaccurate dependence. To interpret the training
of LLMs, Swamy et al. [122] adopt the language model during
pre-training to generate knowledge graphs. The knowledge ac-
quired by LLMs during training can be unveiled by the facts in
KGs explicitly. To explore how implicit knowledge is stored
in parameters of LLMs, Dai et al. [39] propose the concept
of knowledge neurons. Speciﬁcally, activation of the identiﬁed
knowledge neurons is highly correlated with knowledge expres-
sion. Thus, they explore the knowledge and facts represented by
each neuron by suppressing and amplifying knowledge neurons.


### V. Llm-Augmented Kgs

Knowledge graphs are famous for representing knowledge in
a structural manner. They have been applied in many down-
stream tasks such as question answering, recommendation,
and web search. However, the conventional KGs are often
incomplete and existing methods often lack considering tex-
tual information. To address these issues, recent research has
explored integrating LLMs to augment KGs to consider the
textual information and improve the performance in downstream
tasks. In this section, we will introduce the recent research
on LLM-augmented KGs. We will introduce the methods that

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3590

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

Fig. 15. LLMs for joint text and knowledge graph embedding.

Fig. 14. LLMs as text encoder for knowledge graph embedding (KGE).

integrate LLMs for KG embedding, KG completion, KG con-
struction, KG-to-text generation, and KG question answering,
respectively. Table that summarizes representative works can be
found in the Appendix B, available online.


#### A. LLM-Augmented KG Embedding

Knowledge graph embedding (KGE) aims to map each entity
and relation into a low-dimensional vector (embedding) space.
These embeddings contain both semantic and structural infor-
mation of KGs, which can be utilized for various tasks such
as question answering [132], reasoning [38], and recommenda-
tion [133].

LLMs as Text Encoders: Conventional knowledge graph em-
bedding methods mainly rely on the structural information of
KGs to optimize a scoring function deﬁned on embeddings (e.g.,
TransE [33], and DisMult [134]). However, these approaches
often fall short in representing unseen entities and long-tailed
relations due to their limited structural connectivity [135], [136].
To address this issue, as shown in Fig. 14, recent research adopt
LLMs to enrich representations of KGs by encoding the textual
descriptions of entities and relations [40], [94].

LLMs for Joint Text and KG Embedding: Instead of using
KGE model to consider graph structure, another line of methods
directly employs LLMs to incorporate both the graph structure
and textual information into the embedding space simultane-
ously [137], [138], [139]. As shown in Fig. 15, they treat the en-
tities and relations as special tokens in the LLM. During training,
it transfers each triple and corresponding text description into a
sentence where the tailed entities are replaced by [MASK]. The
sentence is fed into a LLM, which then ﬁnetunes the model to
predict the masked entity.

More details about LLM-augmented KG embedding can be

found in the Appendix B.1, available online.


#### B. LLM-Augmented KG Completion

Knowledge Graph Completion (KGC) refers to the task of
inferring missing facts in a given knowledge graph. Similar

Fig. 16.

Framework of prompt-based PaG for KG Completion.

to KGE, conventional KGC methods mainly focused on the
structure of the KG, without considering the extensive textual
information. However, the recent integration of LLMs enables
KGC methods to encode text or generate facts for better KGC
performance. These methods fall into two distinct categories
based on their utilization styles: 1) LLM as Encoders (PaE), and
2) LLM as Generators (PaG).

LLM as Encoders (PaE): This line of work [26], [140], [141],
[142], [143] ﬁrst uses encoder-only LLMs to encode textual
information as well as KG facts. Then, they predict the plausi-
bility of the triples or masked entities by feeding the encoded
representation into a prediction head, which could be a simple
MLP or conventional KG score function (e.g., TransE [33] and
TransR [144]).

LLM as Generators (PaG): Recent works use LLMs as
sequence-to-sequence generators in KGC [96], [145], [146].
These approaches involve encoder-decoder or decoder-only
LLMs. The LLMs receive a sequence text input of the query
triple (h, r, ?), and generate the text of tail entity t directly.
For closed-source LLMs (e.g., ChatGPT and GPT-4), AutoKG
adopts prompt engineering to design customized prompts [93].
As shown in Fig. 16, these prompts contain the task description,
few-shot examples, and test input, which instruct LLMs to
predict the tail entity for KG completion.

More details about the LLM-augmented KG completion can

be found in the Appendix B.2, available online.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3591

the general framework of applying LLMs for each stage in KG
construction. More details about each sub-task are presented in
the Appendix B.3.1, B.3.2, available online, and B.3.3, available
online, respectively.

Recent approaches have explored 4) end-to-end knowledge
graph construction, which involves constructing a complete
knowledge graph in one step or directly 5) distilling knowledge
graphs from LLMs.

End-to-End KG Construction: Currently, researchers are ex-
ploring the use of LLMs for end-to-end KG construction. Kumar
et al. [95] propose a uniﬁed approach to build KGs from raw
text, which contains two LLMs powered components. They ﬁrst
ﬁnetune a LLM on named entity recognition tasks to make it
capable of recognizing entities in raw text. Then, they propose
another “2-model BERT” for solving the relation extraction task,
which contains two BERT-based classiﬁers. The ﬁrst classiﬁer
learns the relation class whereas the second binary classiﬁer
learns the direction of the relations between the two entities. The
predicted triples and relations are then used to construct the KG.
Guo et al. [157] propose an end-to-end knowledge extraction
model based on BERT, which can be applied to construct KGs
from Classical Chinese text. Grapher [41] presents a novel
end-to-end multi-stage system. It ﬁrst utilizes LLMs to generate
KG entities, followed by a simple relation construction head,
enabling efﬁcient KG construction from the textual description.
PiVE [158] proposes a prompting with an iterative veriﬁcation
framework that utilizes a smaller LLM like T5 to correct the
errors in KGs generated by a larger LLM (e.g., ChatGPT). To fur-
ther explore advanced LLMs, AutoKG design several prompts
for different KG construction tasks (e.g., entity typing, entity
linking, and relation extraction). Then, it adopts the prompt to
perform KG construction using ChatGPT and GPT-4.

Distilling Knowledge Graphs from LLMs: LLMs have been
shown to implicitly encode massive knowledge [14]. Some
research aims to distill knowledge from LLMs to construct
KGs. For example, COMET [159] proposes a commonsense
transformer model that constructs commonsense KGs by using
existing tuples as a seed set of knowledge on which to train.
Using this seed set, a LLM learns to adapt its learned representa-
tions to knowledge generation, and produces novel tuples that are
high quality. Experimental results reveal that implicit knowledge
from LLMs is transferred to generate explicit knowledge in
commonsense KGs. More details can be found in the Appendix
B.3.4, available online.


#### D. LLM-Augmented KG-to-Text Generation

The goal of Knowledge-graph-to-text (KG-to-text) generation
is to generate high-quality texts that accurately and consis-
tently describe the input knowledge graph information [160].
KG-to-text generation connects knowledge graphs and texts,
signiﬁcantly improving the applicability of KG in more realistic
NLG scenarios, including storytelling [161] and knowledge-
grounded dialogue [162]. However, it is challenging and costly
to collect large amounts of graph-text parallel data, resulting in
insufﬁcient training and poor generation quality. Thus, many
research efforts resort to either: 1) leverage knowledge from

Fig. 17. General framework of LLM-based KG construction.

Comparison between PaE and PaG: LLMs as Encoders (PaE)
applies an additional prediction head on the top of the rep-
resentation encoded by LLMs. Therefore, the PaE framework
is much easier to ﬁnetune since we can only optimize the
prediction heads and freeze the LLMs. Moreover, the output of
the prediction can be easily speciﬁed and integrated with existing
KGC functions for different KGC tasks. However, during the
inference stage, the PaE requires to compute a score for every
candidate in KGs, which could be computationally expensive.
Besides, they cannot generalize to unseen entities. Furthermore,
the PaE requires the representation output of the LLMs, whereas
some state-of-the-art LLMs (e.g. GPT-41) are closed sources and
do not grant access to the representation output.

LLMs as Generators (PaG), on the other hand, which does
not need the prediction head, can be used without ﬁnetuning
or access to representations. Therefore, the framework of PaG
is suitable for all kinds of LLMs. In addition, PaG directly
generates the tail entity, making it efﬁcient in inference without
ranking all the candidates and easily generalizing to unseen
entities. But, the challenge of PaG is that the generated entities
could be diverse and not lie in KGs. What is more, the time of a
single inference is longer due to the auto-regressive generation.
Last, how to design a powerful prompt that feeds KGs into
LLMs is still an open question. Consequently, while PaG has
demonstrated promising results for KGC tasks, the trade-off be-
tween model complexity and computational efﬁciency must be
carefully considered when selecting an appropriate LLM-based
KGC framework.


#### C. LLM-Augmented KG Construction

Knowledge graph construction involves creating a structured
representation of knowledge within a speciﬁc domain. This
includes identifying entities and their relationships with each
other. The process of knowledge graph construction typically
involves multiple stages, including 1) entity discovery [147],
[148], [149], [150], 2) coreference resolution [151], [152], [153],
and 3) relation extraction [154], [155], [156]. Fig 17 presents

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3592

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

TABLE III
SUMMARY OF METHODS THAT SYNERGIZE KGS AND LLMS

Fig. 18. General framework of KG-to-text generation.

LLMs or 2) construct large-scale weakly-supervised KG-text
corpus to solve this issue.

Leveraging Knowledge from LLMs: As pioneering research
efforts in using LLMs for KG-to-Text generation, Ribeiro
et al. [163] and Kale and Rastogi [164] directly ﬁne-tune various
LLMs, including BART and T5, with the goal of transferring
LLMs knowledge for this task. As shown in Fig. 18, both works
simply represent the input graph as a linear traversal and ﬁnd that
such a naive approach successfully outperforms many existing
state-of-the-art KG-to-text generation systems.

Constructing large weakly KG-text aligned Corpus: Although
LLMs have achieved remarkable empirical success, their unsu-
pervised pre-training objectives are not necessarily aligned well
with the task of KG-to-text generation, motivating researchers
to develop large-scale KG-text aligned corpus. Jin et al. [165]
propose a 1.3 M unsupervised KG-to-graph training data from
Wikipedia. Similarly, Chen et al. [166] also propose a KG-
grounded text corpus collected from the English Wikidump.

More details about the LLM-augmented KG-to-text genera-

tion can be found in the Appendix B.4, available online.


#### E. LLM-Augmented KG Question Answering

Knowledge graph question answering (KGQA) aims to ﬁnd
answers to natural language questions based on the structured
facts stored in knowledge graphs [167], [168]. The inevitable
challenge in KGQA is to retrieve related facts and extend the
reasoning advantage of KGs to QA. Therefore, recent stud-
ies adopt LLMs to bridge the gap between natural language
questions and structured knowledge graphs [169], [170], [171],
where LLMs can be used as 1) entity/relation extractors, and 2)
answer reasoners.

LLMs as Entity/relation Extractors: Entity/relation extractors
are designed to identify entities and relationships mentioned in
natural language questions and retrieve related facts in KGs.
Given the proﬁciency in language comprehension, LLMs can
be effectively utilized for this purpose. Lukovnikov et al. [172]
are the ﬁrst to utilize LLMs as classiﬁers for relation prediction,
resulting in a notable improvement in performance compared
to shallow neural networks. Nan et al. [171] introduce two
LLM-based KGQA frameworks that adopt LLMs to detect
mentioned entities and relations. Then, they query the answer
in KGs using the extracted entity-relation pairs. QA-GNN [131]
uses LLMs to encode the question and candidate answer pairs,
which are adopted to estimate the importance of relative KG
entities. The entities are retrieved to form a subgraph, where an
answer reasoning is conducted by a graph neural network.

LLMs as Answer Reasoners: Answer reasoners are designed
to reason over the retrieved facts and generate answers. LLMs
can be used as answer reasoners to generate answers directly.
DEKCOR [169] concatenates the retrieved facts with questions
and candidate answers as sentences. Then, it feeds them into
LLMs to predict answer scores. GreaseLM [173] fuses the repre-
sentations from LLMs and graph neural networks to effectively
reason over KG facts and language context. UniKGQA [43]
uniﬁes the facts retrieval and reasoning into a uniﬁed framework.
ReLMKG [174] performs joint reasoning on a large language
model and the associated knowledge graph. StructGPT [175]
adopts a customized interface to allow large language models
(e.g., ChatGPT) directly reasoning on KGs to perform multi-step
question answering.

More details about LLM-augmented KG question answering

can be found in the Appendix B.5, available online.

VI. SYNERGIZED LLMS + KGS

The synergy of LLMs and KGs has attracted increasing at-
tention these years, which marries the merits of LLMs and KGs
to mutually enhance performance in various downstream appli-
cations. For example, LLMs can be used to understand natural
language, while KGs are treated as a knowledge base, which
provides factual knowledge. The uniﬁcation of LLMs and KGs
could result in a powerful model for knowledge representation
and reasoning.

In this section, we will discuss the state-of-the-art Synergized
LLMs + KGs from two perspectives: 1) Synergized Knowledge
Representation, and 2) Synergized Reasoning. Representative
works are summarized in Table III.


#### A. Synergized Knowledge Representation

Text corpus and knowledge graphs both contain enormous
knowledge. However, the knowledge in text corpus is usually
implicit and unstructured, while the knowledge in KGs is ex-
plicit and structured. Synergized Knowledge Representation
aims to design a synergized model that can effectively represent
knowledge from both LLMs and KGs. The synergized model
can provide a better understanding of the knowledge from both
sources, making it valuable for many downstream tasks.

To jointly represent the knowledge, researchers propose the
synergized models by introducing additional KG fusion mod-
ules, which are jointly trained with LLMs. As shown in Fig. 19,
ERNIE [35] proposes a textual-knowledge dual encoder archi-
tecture where a T-encoder ﬁrst encodes the input sentences,

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3593

Fig. 19.
ules.

Synergized knowledge representation by additional KG fusion mod-

then a K-encoder processes knowledge graphs which are fused
them with the textual representation from the T-encoder. BERT-
MK [179] employs a similar dual-encoder architecture but it
introduces additional information of neighboring entities in the
knowledge encoder component during the pre-training of LLMs.
However, some of the neighboring entities in KGs may not be
relevant to the input text, resulting in extra redundancy and
noise. CokeBERT [180] focuses on this issue and proposes a
GNN-based module to ﬁlter out irrelevant KG entities using the
input text. JAKET [181] proposes to fuse the entity information
in the middle of the large language model.

KEPLER [40] presents a uniﬁed model for knowledge em-
bedding and pre-trained language representation. In KEPLER,
they encode textual entity descriptions with a LLM as their
embeddings, and then jointly optimize the knowledge embed-
ding and language modeling objectives. JointGT [42] proposes a
graph-text joint representation learning model, which proposes
three pre-training tasks to align representations of graph and text.
DRAGON [44] presents a self-supervised method to pre-train a
joint language-knowledge foundation model from text and KG.
It takes text segments and relevant KG subgraphs as input and
bidirectionally fuses information from both modalities. Then,
DRAGON utilizes two self-supervised reasoning tasks, i.e.,
masked language modeling and KG link prediction to optimize
the model parameters. HKLM [176] introduces a uniﬁed LLM
which incorporates KGs to learn representations of domain-
speciﬁc knowledge.


#### B. Synergized Reasoning

To better utilize the knowledge from text corpus and knowl-
edge graph reasoning, Synergized Reasoning aims to design a
synergized model that can effectively conduct reasoning with
both LLMs and KGs.

LLM-KG Fusion Reasoning: LLM-KG Fusion Reasoning
leverages two separated LLM and KG encoders to process
the text and relevant KG inputs [182]. These two encoders
are equally important and jointly fusing the knowledge from
two sources for reasoning. To improve the interaction between
text and knowledge, KagNet [38] proposes to ﬁrst encode the
input KG, and then augment the input textual representation.
In contrast, MHGRN [168] uses the ﬁnal LLM outputs of the
input text to guide the reasoning process on the KGs. Yet, both
of them only design a single-direction interaction between the

Fig. 20.

Framework of LLM-KG Fusion Reasoning.

Fig. 21. Using LLMs as agents for reasoning on KGs.

text and KGs. To tackle this issue, QA-GNN [131] proposes to
use a GNN-based model to jointly reason over input context and
KG information via message passing. Speciﬁcally, QA-GNN
represents the input textual information as a special node via
a pooling operation and connects this node with other entities
in KG. However, the textual inputs are only pooled into a sin-
gle dense vector, limiting the information fusion performance.
JointLK [183] then proposes a framework with ﬁne-grained
interaction between any tokens in the textual inputs and any
KG entities through LM-to-KG and KG-to-LM bi-directional
attention mechanism. As shown in Fig. 20, pairwise dot-product
scores are calculated over all textual tokens and KG entities,
the bi-directional attentive scores are computed separately. In
addition, at each jointLK layer, the KGs are also dynamically
pruned based on the attention score to allow later layers to focus
on more important sub-KG structures. Despite being effective,
in JointLK, the fusion process between the input text and KG
still uses the ﬁnal LLM outputs as the input text representations.
GreaseLM [173] designs deep and rich interaction between the
input text tokens and KG entities at each layer of the LLMs. The
architecture and fusion approach is mostly similar to ERNIE [35]
discussed in Section VI-A, except that GreaseLM does not use
the text-only T-encoder to handle input text.

LLMs as Agents Reasoning: Instead using two encoders to
fuse the knowledge, LLMs can also be treated as agents to
interact with the KGs to conduct reasoning [184], as illustrated
in Fig. 21. KD-CoT [185] iteratively retrieves facts from KGs
and produces faithful reasoning traces, which guide LLMs to
generate answers. KSL [177] teaches LLMs to search on KGs
to retrieve relevant facts and then generate answers. Struct-
GPT [175] designs several API interfaces to allow LLMs to
access the structural data and perform reasoning by traversing
on KGs. Think-on-graph [178] provides a ﬂexible plug-and-play

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3594

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

framework where LLM agents iteratively execute beam searches
on KGs to discover the reasoning paths and generate answers. To
enhance the agent abilities, AgentTuning [186] presents several
instruction-tuning datasets to guide LLM agents to perform
reasoning on KGs.

Comparison and Discussion: LLM-KG Fusion Reasoning
combines the LLM encoder and KG encoder to represent knowl-
edge in a uniﬁed manner. It then employs a synergized reasoning
module to jointly reason the results. This framework allows for
different encoders and reasoning modules, which are trained
end-to-end to effectively utilize the knowledge and reasoning ca-
pabilities of LLMs and KGs. However, these additional modules
may introduce extra parameters and computational costs while
lacking interpretability. LLMs as Agents for KG reasoning pro-
vides a ﬂexible framework for reasoning on KGs without addi-
tional training cost, which can be generalized to different LLMs
and KGs. Meanwhile, the reasoning process is interpretable,
which can be used to explain the results. Nevertheless, deﬁning
the actions and policies for LLM agents is also challenging. The
synergy of LLMs and KGs is still an ongoing research topic, with
the potential to have more powerful frameworks in the future.


### VII. Future Directions And Milestones

In this section, we discuss the future directions and several

milestones in the research area of unifying KGs and LLMs.


#### A. KGs for Hallucination Detection in LLMs

The hallucination problem in LLMs, which generates fac-
tually incorrect content, signiﬁcantly hinders the reliability of
LLMs. As discussed in Section IV, existing studies try to uti-
lize KGs to obtain more reliable LLMs through pre-training
or KG-enhanced inference. Despite the efforts, the issue of
hallucination may continue to persist in the realm of LLMs
for the foreseeable future. Consequently, in order to gain the
public’s trust and border applications, it is imperative to detect
and assess instances of hallucination within LLMs and other
forms of AI-generated content (AIGC). Existing methods strive
to detect hallucination by training a neural classiﬁer on a small
set of documents [187], which are neither robust nor powerful to
handle ever-growing LLMs. Recently, researchers try to use KGs
as an external source to validate LLMs [188]. Further studies
combine LLMs and KGs to achieve a generalized fact-checking
model that can detect hallucinations across domains [189].
Therefore, it opens a new door to utilizing KGs for hallucination
detection.

edit knowledge in LLMs. Recently, researchers try to leverage
KGs to edit knowledge in LLMs efﬁciently.


#### C. KGs for Black-Box LLMs Knowledge Injection

Although pre-training and knowledge editing could update
LLMs to catch up with the latest knowledge, they still need to
access the internal structures and parameters of LLMs. However,
many state-of-the-art large LLMs (e.g., ChatGPT) only provide
APIs for users and developers to access, making themselves
black-box to the public. Consequently, it is impossible to follow
conventional KG injection approaches described [38], [182] that
change LLM structure by adding additional knowledge fusion
modules. Converting various types of knowledge into different
text prompts seems to be a feasible solution. However, it is
unclear whether these prompts can generalize well to new LLMs.
Moreover, the prompt-based approach is limited to the length of
input tokens of LLMs. Therefore, how to enable effective knowl-
edge injection for black-box LLMs is still an open question for
us to explore [193], [194].


#### D. Multi-Modal LLMs for KGs

Current knowledge graphs typically rely on textual and graph
structure to handle KG-related applications. However, real-
world knowledge graphs are often constructed by data from
diverse modalities [99], [195], [196]. Therefore, effectively
leveraging representations from multiple modalities would be
a signiﬁcant challenge for future research in KGs [197]. One
potential solution is to develop methods that can accurately en-
code and align entities across different modalities. Recently, with
the development of multi-modal LLMs [98], [198], leveraging
LLMs for modality alignment holds promise in this regard. But,
bridging the gap between multi-modal LLMs and KG structure
remains a crucial challenge in this ﬁeld, demanding further
investigation and advancements.


#### E. LLMs for Understanding KG Structure

Conventional LLMs trained on plain text data are not designed
to understand structured data like knowledge graphs. Thus,
LLMs might not fully grasp or understand the information con-
veyed by the KG structure. A straightforward way is to linearize
the structured data into a sentence that LLMs can understand.
However, the scale of the KGs makes it impossible to linearize
the whole KGs as input. Moreover, the linearization process
may lose some underlying information in KGs. Therefore, it is
necessary to develop LLMs that can directly understand the KG
structure and reason over it [175].


#### B. KGs for Editing Knowledge in LLMs

Although LLMs are capable of storing massive real-world
knowledge, they cannot quickly update their internal knowledge
updated as real-world situations change. There are some research
efforts proposed for editing knowledge in LLMs [190] without
re-training the whole LLMs. Yet, such solutions still suffer from
poor performance or computational overhead [191]. Existing
studies [192] also reveal that edit a single fact would cause
a ripple effect for other related knowledge. Therefore, it is
necessary to develop a more efﬁcient and effective method to


#### F. Synergized LLMs and KGs for Birectional Reasoning

KGs and LLMs are two complementary technologies that can
synergize each other. However, the synergy of LLMs and KGs
is less explored by existing researchers. A desired synergy of
LLMs and KGs would involve leveraging the strengths of both
technologies to overcome their individual limitations. LLMs,
such as ChatGPT, excel in generating human-like text and under-
standing natural language, while KGs are structured databases
that capture and represent knowledge in a structured manner.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3595

[4] D. Su et al., “Generalizing question answering system with pre-trained
language model ﬁne-tuning,” in Proc. 2nd Workshop Mach. Reading
Question Answering, 2019, pp. 203–211.

[5] M. Lewis et al., “BART: Denoising sequence-to-sequence pre-training for
natural language generation, translation, and comprehension,” in Proc.
Annu. Meeting Assoc. Comput. Linguistics, 2020, pp. 7871–7880.
[6] J. Li, T. Tang, W. X. Zhao, and J.-R. Wen, “Pretrained language models

for text generation: A survey,” 2021, arXiv:2105.10311.

[7] J. Wei et al., “Emergent abilities of large language models,” Trans. Mach.
Learn. Res., 2022. [Online]. Available: https://openreview.net/forum?id=
yzkSU5zdwD

[8] K. Malinka, M. Perešíni, A. Firc, O. Hujˇník, and F. Januš, “On the
educational impact of ChatGPT: Is artiﬁcial intelligence ready to obtain
a university degree?,” 2023, arXiv:2303.11146.

[9] Z. Li, C. Wang, Z. Liu, H. Wang, S. Wang, and C. Gao, “CCTest: Testing
and repairing code completion systems,” in Proc. IEEE/ACM Int. Conf.
Softw. Eng., 2023, pp. 1238–1250.

[10] J. Liu, C. Liu, R. Lv, K. Zhou, and Y. Zhang, “Is ChatGPT a good

recommender? A preliminary study,” 2023, arXiv:2304.10149.

[11] W. X. Zhao et

al.,
2023, arXiv:2303.18223.

“A survey of

large

language models,”

[12] X. Qiu, T. Sun, Y. Xu, Y. Shao, N. Dai, and X. Huang, “Pre-trained models
for natural language processing: A survey,” Sci. China Technological Sci.,
vol. 63, no. 10, pp. 1872–1897, 2020.

[13] J. Yang et al., “Harnessing the power of LLMs in practice: A survey on

ChatGPT and beyond,” 2023, arXiv:2304.13712.

[14] F. Petroni et al., “Language models as knowledge bases?,” in Proc. Conf.
Empir. Methods Natural Lang. Joint Conf. Natural Lang. Process., 2019,
pp. 2463–2473.

[15] Z. Ji et al., “Survey of hallucination in natural language generation,” ACM

Comput. Surv., vol. 55, no. 12, pp. 1–38, 2023.

[16] H. Zhang, H. Song, S. Li, M. Zhou, and D. Song, “A survey of controllable
text generation using transformer-based pre-trained language models,”
2022, arXiv:2201.05337.

[17] M. Danilevsky, K. Qian, R. Aharonov, Y. Katsis, B. Kawas, and P. Sen,
“A survey of the state of explainable AI for natural language processing,”
2020, arXiv: 2010.00711.

[18] J. Wang et al., “On the robustness of ChatGPT: An adversarial and out-

of-distribution perspective,” 2023, arXiv:2302.12095.

[19] S. Ji, S. Pan, E. Cambria, P. Marttinen, and S. Y. Philip, “A survey
on knowledge graphs: Representation, acquisition, and applications,”
IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 2, pp. 494–514,
Feb. 2022.

[20] D. Vrandeˇci´c and M. Krötzsch, “Wikidata: A free collaborative knowl-

edgebase,” Commun. ACM, vol. 57, no. 10, pp. 78–85, 2014.

[21] S. Hu, L. Zou, and X. Zhang, “A state-transition framework to answer
complex questions over knowledge base,” inProc. Conf. Empirical Meth-
ods Natural Lang. Process., 2018, pp. 2098–2108.

[22] J. Zhang, B. Chen, L. Zhang, X. Ke, and H. Ding, “Neural, symbolic
and neural-symbolic reasoning on knowledge graphs,” AI Open, vol. 2,
pp. 14–35, 2021.

[23] B. Abu-Salih, “Domain-speciﬁc knowledge graphs: A survey,” J. Netw.

Comput. Appl., vol. 185, 2021, Art. no. 103076.

[24] T. Mitchell et al., “Never-ending learning,” Commun. ACM, vol. 61, no. 5,

pp. 103–115, 2018.

[25] L. Zhong, J. Wu, Q. Li, H. Peng, and X. Wu, “A comprehensive survey
on automatic knowledge graph construction,” 2023, arXiv:2302.05019.
[26] L. Yao, C. Mao, and Y. Luo, “KG-BERT: BERT for knowledge graph

completion,” 2019, arXiv: 1909.03193.

[27] L. Luo, Y.-F. Li, G. Haffari, and S. Pan, “Normalizing ﬂow-based neural
process for few-shot knowledge graph completion,” in Proc. 46th Int.
ACM SIGIR Conf. Res. Develop. Inf. Retrieval, 2023, pp. 900–910.
[28] Y. Bang et al., “A multitask, multilingual, multimodal evalua-
tion of ChatGPT on reasoning, hallucination, and interactivity,”
2023, arXiv:2302.04023.

[29] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, and D. Zhou, “Self-
consistency improves chain of thought reasoning in language models,”
2022, arXiv:2203.11171.

[30] O. Golovneva et al., “ROSCOE: A suite of metrics for scoring step-by-

step reasoning,” in Proc. 11th Int. Conf. Learn. Representations, 2023.

[31] F. M. Suchanek, G. Kasneci, and G. Weikum, “YAGO: A core of semantic
knowledge,” in Proc. World Wide Web Conf., 2007, pp. 697–706.
[32] A. Carlson, J. Betteridge, B. Kisiel, B. Settles, E. Hruschka, and

#### T. Mitchell, “Toward an architecture for never-ending language learning,”
in Proc. AAAI Conf. Artif. Intell., 2010, pp. 1306–1313.

Fig. 22. Milestones of unifying KGs and LLMs.

By combining their capabilities, we can create a powerful sys-
tem that beneﬁts from the contextual understanding of LLMs
and the structured knowledge representation of KGs. To better
unify LLMs and KGs, many advanced techniques need to be
incorporated, such as multi-modal learning [199], graph neural
network [200], and continuous learning [201]. Last, the synergy
of LLMs and KGs can be applied to many real-world applica-
tions, such as search engines [100], recommender systems [10],
[89], and drug discovery.

With a given application problem, we can apply a KG to
perform a knowledge-driven search for potential goals and
unseen data, and simultaneously start with LLMs to perform
a data/text-driven inference to see what new data/goal items
can be derived. When the knowledge-based search is combined
with data/text-driven inference, they can mutually validate each
other, resulting in efﬁcient and effective solutions powered by
dual-driving wheels. Therefore, we can anticipate increasing
attention to unlock the potential of integrating KGs and LLMs
for diverse downstream applications with both generative and
reasoning capabilities in the near future.


### VIII. Conclusion

Unifying large language models (LLMs) and knowledge
graphs (KGs) is an active research direction that has attracted
increasing attention from both academia and industry. In this
article, we provide a thorough overview of the recent research
in this ﬁeld. We ﬁrst introduce different manners that integrate
KGs to enhance LLMs. Then, we introduce existing methods that
apply LLMs for KGs and establish taxonomy based on varieties
of KG tasks. Finally, we discuss the challenges and future
directions in this ﬁeld. We envision that there will be multiple
stages (milestones) in the roadmap of unifying KGs and LLMs,
as shown in Fig. 22. In particular, we will anticipate increasing
research on three stages: Stage 1: KG-enhanced LLMs, LLM-
augmented KGs, Stage 2: Synergized LLMs + KGs, and Stage
3: Graph Structure Understanding, Multi-modality, Knowledge
Updating. We hope that this article will provide a guideline to
advance future research.

REFERENCES

[1] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
training of deep bidirectional transformers for language understanding,”
2018, arXiv: 1810.04805.

[2] Y. Liu et al., “RoBERTa: A robustly optimized bert pretraining approach,”

2019, arXiv: 1907.11692.

[3] C. Raffel et al., “Exploring the limits of transfer learning with a uni-
ﬁed text-to-text transformer,” J. Mach. Learn. Res., vol. 21, no. 1,
pp. 5485–5551, 2020.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3596

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

[33] A. Bordes, N. Usunier, A. Garcia-Duran, J. Weston, and O. Yakhnenko,
“Translating embeddings for modeling multi-relational data,” in Proc.
Int. Conf. Neural Inf. Process. Syst., 2013.

[34] G. Wan, S. Pan, C. Gong, C. Zhou, and G. Haffari, “Reasoning like
human: Hierarchical reinforcement learning for knowledge graph rea-
soning,” in Proc. AAAI Conf. Artif. Intell., 2021, pp. 1926–1932.
[35] Z. Zhang, X. Han, Z. Liu, X. Jiang, M. Sun, and Q. Liu, “ERNIE:
Enhanced language representation with informative entities,” in Proc.
Annu. Meeting Assoc. Comput. Linguistics, 2019, pp. 1441–1451.
[36] W. Liu et al., “K-BERT: Enabling language representation with knowl-

edge graph,” in Proc. AAAI Conf. Artif. Intell., 2020, pp. 2901–2908.

[37] Y. Liu, Y. Wan, L. He, H. Peng, and P. S. Yu, “KG-BART: Knowledge
graph-augmented BART for generative commonsense reasoning,” in
Proc. AAAI Conf. Artif. Intell., 2021, pp. 6418–6425.

[38] B. Y. Lin, X. Chen, J. Chen, and X. Ren, “KagNet: Knowledge-aware
graph networks for commonsense reasoning,” in Proc. Conf. Empir.
Methods Natural Lang. Joint Conf. Natural Lang. Process., 2019,
pp. 2829–2839.

[39] D. Dai, L. Dong, Y. Hao, Z. Sui, B. Chang, and F. Wei, “Knowledge

neurons in pretrained transformers,” 2021, arXiv:2104.08696.

[40] X. Wang et al., “KEPLER: A uniﬁed model for knowledge embedding and
pre-trained language representation,” Trans. Assoc. Comput. Linguistics,
vol. 9, pp. 176–194, 2021.

[41] I. Melnyk, P. Dognin, and P. Das, “Grapher: Multi-stage knowledge graph
construction using pretrained language models,” in Proc. NeurIPS 2021
Workshop Deep Generative Models Downstream Appl., 2021.

[42] P. Ke et al., “JointGT: Graph-text joint representation learning for text
generation from knowledge graphs,” in Proc. Annu. Meeting Assoc.
Comput. Linguistics Finding, 2021, pp. 2526–2538.

[43] J. Jiang, K. Zhou, W. X. Zhao, and J.-R. Wen, “UniKGQA: Uniﬁed
retrieval and reasoning for solving multi-hop question answering over
knowledge graph,” in Proc. 11th Int. Conf. Learn. Representations, 2023.
[44] M. Yasunaga et al., “Deep bidirectional language-knowledge graph
pretraining,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2022,
pp. 37 309–37 323.

[45] N. Choudhary and C. K. Reddy, “Complex logical reasoning over knowl-
edge graphs using large language models,” 2023, arXiv:2305.01157.
[46] S. Wang, Z. Wei, J. Xu, and Z. Fan, “Unifying structure rea-
soning and language model pre-training for complex reasoning,”
2023, arXiv:2301.08913.

[47] C. Zhen, Y. Shang, X. Liu, Y. Li, Y. Chen, and D. Zhang,
“A survey on knowledge-enhanced pre-trained language models,”
2022, arXiv:2212.13428.

[48] X. Wei, S. Wang, D. Zhang, P. Bhatia, and A. Arnold, “Knowl-
edge enhanced pretrained language models: A compreshensive survey,”
2021, arXiv:2110.08455.

[49] D. Yin et al., “A survey of knowledge-intensive NLP with pre-trained

language models,” 2022, arXiv:2202.08772.

[50] A. Vaswani et al., “Attention is all you need,” in Proc. Adv. Neural Inf.
Process. Syst., I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach, R.
Fergus, S. Vishwanathan, R. Garnett, Eds., vol. 30, 2017, pp. 6000–6010.
[51] Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut,
“ALBERT: A lite bert for self-supervised learning of language represen-
tations,” in Proc. Int. Conf. Learn. Representations, 2020.

[52] K. Clark, M.-T. Luong, Q. V. Le, and C. D. Manning, “ELECTRA:
Pre-training text encoders as discriminators rather than generators,”
2020, arXiv: 2003.10555.

[53] K. Hakala and S. Pyysalo, “Biomedical named entity recognition with
multilingual BERT,” in Proc. 5th Workshop BioNLP Open Shared Tasks,
2019, pp. 56–61.

[54] Y. Tay et al., “UL2: Unifying language learning paradigms,” in Proc. 11th

Int. Conf. Learn. Representations, 2023.

[55] V. Sanh et al., “Multitask prompted training enables zero-shot task
generalization,” in Proc. Int. Conf. Learn. Representations, 2022.
[56] B. Zoph et al., “ST-MoE: Designing stable and transferable sparse expert

models,” 2022. [Online]. Available: https://arxiv.org/abs/2202.08906

[57] A. Zeng et al., “GLM-130B: An open bilingual pre-trained model,” in
Proc. 11th Int. Conf. Learn. Representations, 2023. [Online]. Available:
https://openreview.net/forum?id=-Aw0rrrPUF

[58] L. Xue et al., “mT5: A massively multilingual pre-trained text-to-text
transformer,” in Proc. Conf. North Amer. Chapter Assoc. Comput. Lin-
guistics, 2021, pp. 483–498.

[59] T. Brown et al., “Language models are few-shot learners,” in Proc. Adv.

Neural Inf. Process. Syst., 2020, pp. 1877–1901.

[60] L. Ouyang et al., “Training language models to follow instructions with
human feedback,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2022,
pp. 27 730–27 744.

[61] H. Touvron et al., “LLaMA: Open and efﬁcient foundation language

models,” 2023, arXiv:2302.13971.

[62] E. Saravia, “Prompt engineering guide,” 2022, Accessed: Dec. 2022.

https://github.com/dair-ai/Prompt-Engineering-Guide

[63] J. Wei et al., “Chain-of-thought prompting elicits reasoning in large
language models,” in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022,
pp. 24824–24837.

[64] S. Li et al., “Graph reasoning for question answering with triplet re-
trieval,” in Proc. Annu. Meeting Assoc. Comput. Linguistics, 2023,
pp. 3366–3375.

[65] Y. Wen, Z. Wang, and J. Sun, “MindMap: Knowledge graph
thoughts in large language models,”

prompting sparks graph of
2023, arXiv:2308.09729.

[66] K. Bollacker, C. Evans, P. Paritosh, T. Sturge, and J. Taylor, “Free-
base: A collaboratively created graph database for structuring human
knowledge,” in Proc. ACM SIGMOD Int. Conf. Manage. Data, 2008,
pp. 1247–1250.

[67] S. Auer, C. Bizer, G. Kobilarov, J. Lehmann, R. Cyganiak, and Z. Ives,
“DBpedia: A nucleus for a web of open data,” in Proc. 6th Int. Semantic
Web Conf., 2007, pp. 722–735.

[68] B. Xu et al., “CN-DBpedia: A never-ending Chinese knowledge extrac-
tion system,” in Proc. 30th Int. Conf. Ind. Eng. Other Appl. Appl. Intell.
Syst., 2017, pp. 428–438.

[69] P. Hai-Nyzhnyk, “Vikidia as a universal multilingual online encyclo-
pedia for children,” Encyclopedia Herald Ukraine, vol. 14, pp. 81–87,
2022.

[70] F. Ilievski, P. Szekely, and B. Zhang, “CSKG: The commonsense knowl-

edge graph,” in Proc. Extended Semantic Web Conf., 2021.

[71] R. Speer, J. Chin, and C. Havasi, “ConceptNet 5.5: An open multilingual
graph of general knowledge,” in Proc. AAAI Conf. Artif. Intell., vol. 31,
no. 1, Feb. 2017, doi: 10.1609/aaai.v31i1.11164. [Online]. Available:
https://ojs.aaai.org/index.php/AAAI/article/view/11164

[72] H. Ji, P. Ke, S. Huang, F. Wei, X. Zhu, and M. Huang, “Lan-
guage generation with multi-hop reasoning on commonsense knowledge
graph,” in Proc. Conf. Empirical Methods Natural Lang. Process., 2020,
pp. 725–736.

[73] J. D. Hwang et al., “(Comet-) atomic 2020: On symbolic and neural
commonsense knowledge graphs,” in Proc. AAAI Conf. Artif. Intell.,
vol. 35, no. 7, 2021, pp. 6384–6392.

[74] H. Zhang, X. Liu, H. Pan, Y. Song, and C. W.-K. Leung, “ASER: A
large-scale eventuality knowledge graph,” in Proc. Web Conf., 2020,
pp. 201–211.

[75] H. Zhang, D. Khashabi, Y. Song, and D. Roth, “TransOMCS: From
linguistic graphs to commonsense knowledge,” in Proc. Int. Joint Conf.
Artif. Intell., 2021, pp. 4004–4010.

[76] Z. Li, X. Ding, T. Liu, J. E. Hu, and B. Van Durme, “Guided gen-
eration of cause and effect,” in Proc. Int. Joint Conf. Artif. Intell.,
2020.

[77] O. Bodenreider, “The uniﬁed medical language system (UMLS): Inte-
grating biomedical terminology,” Nucleic acids Res., vol. 32, no. suppl_1,
pp. D267–D270, 2004.

[78] Y. Liu, Q. Zeng, J. Ordieres Meré, and H. Yang, “Anticipating stock
market of the renowned companies: A knowledge graph approach,”
Complexity, vol. 2019, 2019, Art. no. 9202457.

[79] Y. Zhu et al., “Intelligent learning for knowledge graph towards geolog-

ical data,” Sci. Program., vol. 2017, 2017, Art. no. 5072427.

[80] W. Choi and H. Lee, “Inference of biomedical relations among chemicals,
genes, diseases, and symptoms using knowledge representation learning,”
IEEE Access, vol. 7, pp. 179 373–179 384, 2019.

[81] F. Farazi et al., “Knowledge graph approach to combustion chemistry
and interoperability,” ACS Omega, vol. 5, no. 29, pp. 18 342–18 348,
2020.

[82] X. Wu, T. Jiang, Y. Zhu, and C. Bu, “Knowledge graph for China’s
genealogy,” IEEE Trans. Knowl. Data Eng., vol. 35, no. 1, pp. 634–646,
Jan. 2023.

[83] X. Zhu et al., “Multi-modal knowledge graph construction and ap-
plication: A survey,” IEEE Trans. Knowl. Data Eng., vol. 36, no. 2,
pp. 715–735, 2024, doi: 10.1109/TKDE.2022.3224228.

[84] S. Ferrada, B. Bustos, and A. Hogan, “IMGpedia: A linked dataset with
content-based analysis of WIKIMEDIA images,” in Proc. Int. Semantic
Web Conf., 2017, pp. 84–93.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3597

[85] Y. Liu, H. Li, A. Garcia-Duran, M. Niepert, D. Onoro-Rubio, and

#### D. S. Rosenblum, “MMKG: Multi-modal knowledge graphs,” in Proc.
16th Int. Conf. Semantic Web, 2019, pp. 459–474.

[86] M. Wang, H. Wang, G. Qi, and Q. Zheng, “Richpedia: A large-scale,
comprehensive multi-modal knowledge graph,” Big Data Res., vol. 22,
2020, Art. no. 100159.

[87] B. Shi, L. Ji, P. Lu, Z. Niu, and N. Duan, “Knowledge aware semantic
concept expansion for image-text matching,” in Proc. Int. Joint Conf.
Artif. Intell., 2019, Art. no. 2.

[88] S. Shah, A. Mishra, N. Yadati, and P. P. Talukdar, “KVQA: Knowledge-
aware visual question answering,” in Proc. AAAI Conf. Artif. Intell.,
vol. 33, no. 01, 2019, pp. 8876–8884.

[89] R. Sun et al., “Multi-modal knowledge graphs for recommender systems,”

in Proc. Conf. Inf. Knowl. Manage., 2020, pp. 1405–1414.

[90] S. Deng et al., “Construction and applications of billion-scale pre-trained
multimodal business knowledge graph,” in Proc. IEEE 39th Int. Conf.
Data Eng., 2023, pp. 2988–3002.

[91] C. Rosset, C. Xiong, M. Phan, X. Song, P. Bennett, and S. Ti-
wary, “Knowledge-aware language model pretraining,” 2020, arXiv:
2007.00655.

[92] P. Lewis et al., “Retrieval-augmented generation for knowledge-intensive
NLP tasks,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2020,
pp. 9459–9474.

[93] Y. Zhu et al., “LLMs

for knowledge graph construction and
reasoning: Recent capabilities and future opportunities,” 2023,
arXiv:2305.13168.

[94] Z. Zhang, X. Liu, Y. Zhang, Q. Su, X. Sun, and B. He, “Pretrain-KGE:
Learning knowledge representation from pretrained language models,”
in Proc. Conf. Empirical Methods Natural Lang. Process. Finding, 2020,
pp. 259–266.

[95] A. Kumar, A. Pandey, R. Gadia, and M. Mishra, “Building knowledge
graph using pre-trained language model for learning entity-aware rela-
tionships,” in Proc. IEEE Int. Conf. Comput. Power Commun. Technol.,
2020, pp. 310–315.

[96] X. Xie et al., “From discrimination to generation: Knowledge graph
completion with generative transformer,” in Proc. World Wide Web Conf.,
2022, pp. 162–165.

[97] Z. Chen, C. Xu, F. Su, Z. Huang, and Y. Dou, “Incorporating structured
sentences with time-enhanced bert for fully-inductive temporal relation
prediction,” in Proc. 46th Int. ACM SIGIR Conf. Res. Develop. Inf.
Retrieval, 2023.

[98] D. Zhu, J. Chen, X. Shen, X. Li, and M. Elhoseiny, “MiniGPT-4: En-
hancing vision-language understanding with advanced large language
models,” 2023, arXiv:2304.10592.

[99] M. Warren, D. A. Shamma, and P. J. Hayes, “Knowledge engineering
with image data in real-world settings,” in Proc. AAAI Spring Symp.
Combining Mach. Learn. Knowl. Eng., Mar. 2021.

[100] R. Thoppilan et al., “LaMDA: Language models for dialog applica-

tions,” 2022, arXiv:2201.08239.

[101] Y. Sun et al., “ERNIE 3.0: Large-scale knowledge enhanced
language understanding and generation,” 2021,

pre-training for
arXiv:2107.02137.

[102] T. Shen, Y. Mao, P. He, G. Long, A. Trischler, and W. Chen, “Exploit-
ing structured knowledge in text via graph-guided representation learn-
ing,” in Proc. Conf. Empirical Methods Natural Lang. Process., 2020,
pp. 8980–8994.

[103] D. Zhang, Z. Yuan, Y. Liu, F. Zhuang, H. Chen, and H. Xiong, “E-
BERT: A phrase and product knowledge enhanced language model for
E-commerce,” 2020, arXiv: 2009.02835.

[104] S. Li et al., “Pre-training language models with deterministic factual
knowledge,” in Proc. Conf. Empirical Methods Natural Lang. Process.,
2022, pp. 11 118–11 131.

[105] M. Kang, J. Baek, and S. J. Hwang, “KAL: Knowledge-augmented
language model adaptation,” in Proc. Conf. North Amer. Chapter Assoc.
Comput. Linguistics, 2022, pp. 5144–5167.

[106] W. Xiong, J. Du, W. Y. Wang, and V. Stoyanov, “Pretrained ency-
clopedia: Weakly supervised knowledge-pretrained language model,”
in Proc. Int. Conf. Learn. Representations, 2020. [Online]. Available:
https://openreview.net/forum?id=BJlzm64tDH

[107] T. Sun et al., “CoLAKE: Contextualized language and knowledge
embedding,” in Proc. 28th Int. Conf. Comput. Linguistics, 2020,
pp. 3660–3670.

[108] T. Zhang et al., “DKPLM: Decomposable knowledge-enhanced pre-
trained language model for natural language understanding,” in Proc.
AAAI Conf. Artif. Intell., 2022, pp. 11 703–11 711.

[109] J. Wang et al., “Knowledge prompting in pre-trained language model
for natural language understanding,” in Proc. Conf. Empirical Methods
Natural Lang. Process., 2022, pp. 3164–3177.

[110] H. Ye et al., “Ontology-enhanced prompt-tuning for few-shot learning,”

in Proc. ACM Web Conf., 2022, pp. 778–787.

[111] H. Luo et al., “ChatKBQA: A generate-then-retrieve framework for
knowledge base question answering with ﬁne-tuned large language mod-
els,” 2023, arXiv:2310.08975.
[112] L. Luo, Y.-F. Li, G. Haffari,

“Reasoning on
graphs: Faithful and interpretable large language model reasoning,”
2023, arxiv:2310.01061.

and S. Pan,

[113] R. Logan, N. F. Liu, M. E. Peters, M. Gardner, and S. Singh, “Barack’s
wife Hillary: Using knowledge graphs for fact-aware language mod-
eling,” in Proc. Annu. Meeting Assoc. Comput. Linguistics, 2019,
pp. 5962–5971.

[114] K. Guu, K. Lee, Z. Tung, P. Pasupat, and M.-W. Chang, “REALM:
Retrieval-augmented language model pre-training,” in Proc. Int. Conf.
Mach. Learn., 2020, pp. 3929–3938.

[115] Y. Wu, Y. Zhao, B. Hu, P. Minervini, P. Stenetorp, and S. Riedel, “An
efﬁcient memory-augmented transformer for knowledge-intensive NLP
tasks,” in Proc. Conf. Empirical Methods Natural Lang. Process., 2022,
pp. 5184–5196.

[116] L. Luo, J. Ju, B. Xiong, Y.-F. Li, G. Haffari, and S. Pan, “ChatRule:
Mining logical rules with large language models for knowledge graph
reasoning,” 2023, arXiv:2309.01538.

[117] J. Wang, Q. Sun, N. Chen, X. Li, and M. Gao, “Boosting
language models reasoning with chain-of-knowledge prompting,”
2023, arXiv:2306.06427.

[118] Z. Jiang, F. F. Xu, J. Araki, and G. Neubig, “How can we know what
language models know?,” Trans. Assoc. Comput. Linguistics, vol. 8,
pp. 423–438, 2020.

[119] T. Shin, Y. Razeghi, R. L. Logan IV, E. Wallace, and S. Singh, “Auto-
Prompt: Eliciting knowledge from language models with automatically
generated prompts,” 2020, arXiv: 2010.15980.

[120] Z. Meng, F. Liu, E. Shareghi, Y. Su, C. Collins, and N. Collier, “Rewire-
then-probe: A contrastive recipe for probing biomedical knowledge of
pre-trained language models,” 2021, arXiv:2110.08173.

[121] L. Luo, T.-T. Vu, D. Phung, and G. Haffari, “Systematic assessment of
factual knowledge in large language models,” in Proc. Conf. Empirical
Methods Natural Lang. Process., 2023.

[122] V. Swamy, A. Romanou, and M. Jaggi, “Interpreting language models
through knowledge graph extraction,” 2021, arXiv:2111.08546.
[123] S. Li et al., “How pre-trained language models capture factual knowl-

edge? A causal-inspired analysis,” 2022, arXiv:2203.16747.

[124] H. Tian et al., “SKEP: Sentiment knowledge enhanced pre-training for
sentiment analysis,” in Proc. Annu. Meeting Assoc. Comput. Linguistics,
2020, pp. 4067–4076.

[125] W. Yu et al., “Dict-BERT: Enhancing language model pre-training with
dictionary,” in Proc. Annu. Meeting Assoc. Comput. Linguistics, 2022,
pp. 1907–1918.

[126] T. McCoy, E. Pavlick, and T. Linzen, “Right for the wrong reasons:
Diagnosing syntactic heuristics in natural language inference,” in Proc.
Annu. Meeting Assoc. Comput. Linguistics, 2019, pp. 3428–3448.
[127] D. Wilmot and F. Keller, “Memory and knowledge augmented language
models for inferring salience in long-form stories,” in Proc. Conf. Em-
pirical Methods Natural Lang. Process., 2021, pp. 851–865.

[128] L. Adolphs, S. Dhuliawala, and T. Hofmann, “How to query language

models?,” 2021, arXiv:2108.01928.

[129] M. Sung, J. Lee, S. Yi, M. Jeon, S. Kim, and J. Kang, “Can language mod-
els be biomedical knowledge bases,” in Proc. Conf. Empirical Methods
Natural Lang. Process., 2021, pp. 4723–4734.

[130] A. Mallen, A. Asai, V. Zhong, R. Das, H. Hajishirzi, and D.
Khashabi, “When not to trust language models: Investigating effective-
ness and limitations of parametric and non-parametric memories,” 2022,
arXiv:2212.10511.

[131] M. Yasunaga, H. Ren, A. Bosselut, P. Liang, and J. Leskovec, “QA-GNN:
Reasoning with language models and knowledge graphs for question
answering,” in Proc. Conf. North Amer. Chapter Assoc. Comput. Lin-
guistics, 2021, pp. 535–546.

[132] X. Huang, J. Zhang, D. Li, and P. Li, “Knowledge graph embedding based
question answering,” in Proc. ACM Int. Conf. Web Search Data Mining,
2019, pp. 105–113.

[133] H. Wang, F. Zhang, X. Xie, and M. Guo, “DKN: Deep knowledge-aware
network for news recommendation,” in Proc. World Wide Web Conf.,
2018, pp. 1835–1844.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

3598

IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING, VOL. 36, NO. 7, JULY 2024

[134] B. Yang, S. W.-T. Yih, X. He, J. Gao, and L. Deng, “Embedding entities
and relations for learning and inference in knowledge bases,” in Proc.
Int. Conf. Learn. Representations, 2015.

[135] W. Xiong, M. Yu, S. Chang, X. Guo, and W. Y. Wang, “One-shot rela-
tional learning for knowledge graphs,” in Proc. Conf. Empirical Methods
Natural Lang. Process., 2018, pp. 1980–1990.

[136] P. Wang, J. Han, C. Li, and R. Pan, “Logic attention based neighborhood
aggregation for inductive knowledge graph embedding,” in Proc. AAAI
Conf. Artif. Intell., 2019, pp. 7152–7159.

[137] N. Zhang et al., “Reasoning through memorization: Nearest neighbor

knowledge graph embeddings,” 2022, arXiv:2201.05575.

[138] X. Wang, Q. He, J. Liang, and Y. Xiao, “Language models as knowledge

embeddings,” 2022, arXiv:2206.12617.

[139] X. Xie et al., “LambdaKG: A library for pre-trained language model-

based knowledge graph embeddings,” 2022.

[140] J. Shen, C. Wang, L. Gong, and D. Song, “Joint language semantic and
structure embedding for knowledge graph completion,” in Proc. Int. Conf.
Comput. Linguistics, 2022, pp. 1965–1978.

[141] B. Choi, D. Jang, and Y. Ko, “MEM-KGC: Masked entity model for
knowledge graph completion with pre-trained language model,” IEEE
Access, vol. 9, pp. 132 025–132 032, 2021.

[142] B. Wang, T. Shen, G. Long, T. Zhou, Y. Wang, and Y. Chang, “Structure-
augmented text representation learning for efﬁcient knowledge graph
completion,” in Proc. World Wide Web Conf., 2021, pp. 1737–1748.

[143] L. Wang, W. Zhao, Z. Wei, and J. Liu, “SimKGC: Simple contrastive
knowledge graph completion with pre-trained language models,” in Proc.
Annu. Meeting Assoc. Comput. Linguistics, 2022, pp. 4281–4294.
[144] Y. Lin, Z. Liu, M. Sun, Y. Liu, and X. Zhu, “Learning entity and relation
embeddings for knowledge graph completion,” in Proc. AAAI Conf. Artif.
Intell., 2015.

[145] A. Saxena, A. Kochsiek, and R. Gemulla, “Sequence-to-sequence knowl-
edge graph completion and question answering,” in Proc. Annu. Meeting
Assoc. Comput. Linguistics, 2022, pp. 2814–2828.

[146] C. Chen, Y. Wang, B. Li, and K. Lam, “Knowledge is ﬂat: A Seq2Seq
generative framework for various knowledge graph completion,” in Proc.
Int. Conf. Comput. Linguistics, 2022, pp. 4005–4017.

[147] M. E. Peters et al., “Deep contextualized word representations,” in
Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics, 2018,
pp. 2227–2237.

[148] Y. Onoe and G. Durrett, “Learning to denoise distantly-labeled data
for entity typing,” in Proc. Conf. North Amer. Chapter Assoc. Comput.
Linguistics, 2019, pp. 2407–2417.

[149] N. D. Cao, G. Izacard, S. Riedel, and F. Petroni, “Autoregressive entity
retrieval,” in Proc. Int. Conf. Learn. Representations, Austria, 2021, 2021.
[150] T. Ayoola, S. Tyagi, J. Fisher, C. Christodoulopoulos, and A. Pierleoni,
“Reﬁned: An efﬁcient zero-shot-capable approach to end-to-end entity
linking,” in Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics,
2022, pp. 209–220.

[151] M. Joshi, O. Levy, L. Zettlemoyer, and D. S. Weld, “BERT for coreference
resolution: Baselines and analysis,” in Proc. Conf. Empirical Methods
Natural Lang. Process., 2019, pp. 5802–5807.

[152] M. Joshi, D. Chen, Y. Liu, D. S. Weld, L. Zettlemoyer, and O. Levy,
“SpanBERT: Improving pre-training by representing and predicting
spans,” Trans. Assoc. Comput. Linguistics, vol. 8, pp. 64–77, 2020.
[153] A. Cattan, A. Eirew, G. Stanovsky, M. Joshi, and I. Dagan, “Cross-
document coreference resolution over predicted mentions,” in Proc.
Annu. Meeting Assoc. Comput. Linguistics, 2021, pp. 5100–5107.
[154] P. Shi and J. Lin, “Simple BERT models for relation extraction and

semantic role labeling,” 2019, arXiv: 1904.05255.

[155] C. Alt, M. Hübner, and L. Hennig, “Improving relation extraction by pre-
trained language representations,” in Proc. 1st Conf. Automated Knowl.
Base Construction, Amherst, MA, USA, 2019.

[156] Y. Ma, A. Wang, and N. Okazaki, “DREEAM: Guiding attention
with evidence for improving document-level relation extraction,” in
Proc. 13th Conf. Eur. Chapter Assoc. Comput. Linguistics, 2023,
pp. 1963–1975.

[157] Q. Guo et al., “Constructing chinese historical literature knowledge graph
based on BERT,” in Proc. 18th Int. Conf. Web Inf. Syst. Appl., Kaifeng,
China, 2021, 2021, pp. 323–334.

[158] J. Han, N. Collier, W. Buntine, and E. Shareghi, “PiVe: Prompting
with iterative veriﬁcation improving graph-based generative capability
of LLMs,” 2023, arXiv:2305.12392.

[159] A. Bosselut, H. Rashkin, M. Sap, C. Malaviya, A. Celikyilmaz, and

#### Y. Choi, “COMET: Commonsense transformers for knowledge graph
construction,” in Proc. 57th Annu. Meeting Assoc. Comput. Linguistics,


#### A. Korhonen, D. Traum, and Luis Márquez, Eds., Florence, Italy:
Association for Computational Linguistics, pp. 4762–4779, Jul. 2019,
doi: 10.18653/v1/P19-1470. [Online]. Available: https://aclanthology.
org/P19-1470

[160] C. Gardent, A. Shimorina, S. Narayan, and L. Perez-Beltrachini, “The
WebNLG challenge: Generating text from RDF data,” in Proc. 10th Int.
Conf. Natural Lang. Gener., 2017, pp. 124–133.

[161] J. Guan, Y. Wang, and M. Huang, “Story ending generation with incre-
mental encoding and commonsense knowledge,” in Proc. AAAI Conf.
Artif. Intell., 2019, pp. 6473–6480.

[162] H. Zhou, T. Young, M. Huang, H. Zhao, J. Xu, and X. Zhu, “Common-
sense knowledge aware conversation generation with graph attention,” in
Proc. Int. Joint Conf. Artif. Intell., 2018, pp. 4623–4629.

[163] L. F. R. Ribeiro, M. Schmitt, H. Schütze, and I. Gurevych, “Inves-
tigating pretrained language models for graph-to-text generation,” in
Proc. 3rd Workshop Natural Lang. Process. Conversational AI, 2021,
pp. 211–227.

[164] M. Kale and A. Rastogi, “Text-to-text pre-training for data-to-text tasks,”
in Proc. 13th Int. Conf. Natural Lang. Gener., 2020, pp. 97–102.
[165] Z. Jin, Q. Guo, X. Qiu, and Z. Zhang, “GenWiki: A dataset of
1.3 million content-sharing text and graphs for unsupervised graph-to-
text generation,” in Proc. 28th Int. Conf. Comput. Linguistics, 2020,
pp. 2398–2409.

[166] W. Chen, Y. Su, X. Yan, and W. Y. Wang, “KGPT: Knowledge-grounded
pre-training for data-to-text generation,” in Proc. Conf. Empirical Meth-
ods Natural Lang. Process., 2020, pp. 8635–8648.

[167] A. Saxena, A. Tripathi, and P. Talukdar, “Improving multi-hop ques-
tion answering over knowledge graphs using knowledge base em-
beddings,” in Proc. Annu. Meeting Assoc. Comput. Linguistics, 2020,
pp. 4498–4507.

[168] Y. Feng, X. Chen, B. Y. Lin, P. Wang, J. Yan, and X. Ren, “Scalable
multi-hop relational reasoning for knowledge-aware question answer-
ing,” in Proc. Conf. Empirical Methods Natural Lang. Process., 2020,
pp. 1295–1309.

[169] Y. Xu, C. Zhu, R. Xu, Y. Liu, M. Zeng, and X. Huang, “Fusing context
into knowledge graph for commonsense question answering,” in Proc.
Annu. Meeting Assoc. Comput. Linguistics, 2021, pp. 1201–1207.
[170] Y. Yan et al., “Large-scale relation learning for question answering over
knowledge bases with pre-trained language models,” in Proc. Conf.
Empirical Methods Natural Lang. Process., 2021, pp. 3653–3660.
[171] N. Hu et al., “An empirical study of pre-trained language models in simple
knowledge graph question answering,” 2023, arXiv:2303.10368.
[172] D. Lukovnikov, A. Fischer, and J. Lehmann, “Pretrained transformers
for simple question answering over knowledge graphs,” in The Semantic
Web–ISWC in Proc. 18th Int. Semantic Web Conf., Auckland, New
Zealand, 2019, pp. 470–486.

[173] X. Zhang et al., “GreaseLM: Graph reasoning enhanced language mod-

els,” in Proc. Int. Conf. Learn. Representations, 2022.

[174] X. Cao and Y. Liu, “ReLMKG: Reasoning with pre-trained language
models and knowledge graphs for complex question answering,” Appl.
Intell., vol. 53, pp. 12032–12046, 2023.

[175] J. Jiang, K. Zhou, Z. Dong, K. Ye, W. X. Zhao, and J.-R. Wen, “StructGPT:
A general framework for large language model to reason over structured
data,” 2023, arXiv:2305.09645.

[176] H. Zhu, H. Peng, Z. Lyu, L. Hou, J. Li, and J. Xiao, “Pre-training
language model incorporating domain-speciﬁc heterogeneous knowl-
edge into a uniﬁed representation,” Expert Syst. Appl., vol. 215, 2023,
Art. no. 119369.

[177] C. Feng, X. Zhang, and Z. Fei, “Knowledge solver: Teaching
LLMs to search for domain knowledge from knowledge graphs,”
2023, arXiv:2309.03118.

[178] J. Sun et al., “Think-on-graph: Deep and responsible reasoning of large
language model with knowledge graph,” 2023, arXiv:2307.07697.
[179] B. He et al., “BERT-MK: Integrating graph contextualized knowledge
into pre-trained language models,” in Proc. Conf. Empirical Methods
Natural Lang. Process., 2020, pp. 2281–2290.

[180] Y. Su et al., “CokeBERT: Contextual knowledge selection and embed-
ding towards enhanced pre-trained language models,” AI Open, vol. 2,
pp. 127–134, 2021.

[181] D. Yu, C. Zhu, Y. Yang, and M. Zeng, “JAKET: Joint pre-training of
knowledge graph and language understanding,” in Proc. AAAI Conf. Artif.
Intell., 2022, pp. 11 630–11 638.

[182] X. Wang et al., “Improving natural language inference using external
knowledge in the science questions domain,” in Proc. AAAI Conf. Artif.
Intell., 2019, pp. 7208–7215.

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.

PAN et al.: UNIFYING LARGE LANGUAGE MODELS AND KNOWLEDGE GRAPHS: A ROADMAP

3599

[183] Y. Sun, Q. Shi, L. Qi, and Y. Zhang, “JointLK: Joint reasoning with lan-
guage models and knowledge graphs for commonsense question answer-
ing,” in Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics,
2022, pp. 5049–5060.

[184] X. Liu et

al.,

“AgentBench: Evaluating LLMs

as

agents,”

2023, arXiv:2308.03688.

[185] Y. Wang, N. Lipka, R. A. Rossi, A. Siu, R. Zhang, and T. Derr,
“Knowledge graph prompting for multi-document question answering,”
2023, arXiv:2308.11730.

[186] A. Zeng et al., “AgentTuning: Enabling generalized agent abilities for

LLMs,” 2023, arXiv:2310.12823.

[187] W. Kry´sci´nski, B. McCann, C. Xiong, and R. Socher, “Evaluating the
factual consistency of abstractive text summarization,” 2019, arXiv:
1910.12840.

[188] Z. Ji et al., “RHO (\ρ): Reducing hallucination in open-domain dialogues

with knowledge grounding,” 2022, arXiv:2212.01588.

[189] S. Feng, V. Balachandran, Y. Bai, and Y. Tsvetkov, “FactKB: Generaliz-
able factuality evaluation using language models enhanced with factual
knowledge,” 2023, arXiv:2305.08281.

[190] Y. Yao et al., “Editing large language models: Problems, methods, and

opportunities,” 2023, arXiv:2305.13172.

[191] Z. Li, N. Zhang, Y. Yao, M. Wang, X. Chen, and H. Chen, “Un-
veiling the pitfalls of knowledge editing for large language models,”
2023, arXiv:2310.02129.

[192] R. Cohen, E. Biran, O. Yoran, A. Globerson, and M. Geva, “Eval-
uating the ripple effects of knowledge editing in language models,”
2023, arXiv:2307.12976.

[193] S. Diao et al., “Black-box prompt learning for pre-trained language

models,” 2022, arXiv:2201.08531.

[194] T. Sun, Y. Shao, H. Qian, X. Huang, and X. Qiu, “Black-box tuning for
language-model-as-a-service,” in Proc. Int. Conf. Mach. Learn., 2022,
pp. 20 841–20 855.

[195] X. Chen, A. Shrivastava, and A. Gupta, “NEIL: Extracting visual knowl-
edge from web data,” in Proc. IEEE Int. Conf. Comput. Vis., Sydney,
Australia, 2013, pp. 1409–1416.

[196] M. Warren and P. J. Hayes, “Bounding ambiguity: Experiences with an
image annotation system,” in Proc. 1st Workshop Subjectivity Ambiguity
Disagreement Crowdsourcing, 2018, pp. 41–54.

[197] Z. Chen et al., “LaKo: Knowledge-driven visual estion answering via
late knowledge-to-text injection,” in Proc. 11th Int. Joint Conf. Knowl.
Graphs, 2022, pp. 20–29.

[198] R. Girdhar et al., “ImageBind: One embedding space to bind them all,”
in Proc. IEEE Int. Conf. Comput. Vis., 2023, pp. 15 180–15 190.
[199] J. Zhang, Z. Yin, P. Chen, and S. Nichele, “Emotion recognition using
multi-modal data and machine learning techniques: A tutorial and re-
view,” Inf. Fusion, vol. 59, pp. 103–126, 2020.

[200] H. Zhang, B. Wu, X. Yuan, S. Pan, H. Tong, and J. Pei, “Trustworthy graph
neural networks: Aspects, methods and trends,” 2022, arXiv:2205.07424.
[201] T. Wu, M. Caccia, Z. Li, Y.-F. Li, G. Qi, and G. Haffari, “Pretrained
language model in continual learning: A comparative study,” in Proc.
Int. Conf. Learn. Representations, 2022.

Shirui Pan (Senior Member, IEEE) received the PhD
degree in computer science from the University of
Technology Sydney (UTS), Ultimo, NSW, Australia.
He is a professor with the School of Information
and Communication Technology, Grifﬁth University,
Australia. Prior to this, he was a senior lecturer with
the Faculty of IT at Monash University. His research
interests include data mining and machine learning.
To date, he has published more than 100 research
papers in top-tier journals and conferences, including
IEEE Transactions on Pattern Analysis and Machine
Intelligence, IEEE Transactions on Knowledge and Data Engineering, IEEE
Transactions on Neural Networks and Learning Systems, ICML, NeurIPS,
and KDD. His research has attracted more than 20 000 citations. His research
received the 2024 CIS IEEE TNNLS Oustanding Paper Award and the 2020
IEEE ICDM Best Student Paper Award. He is recognised as one of the AI 2000
AAAI/IJCAI Most Inﬂuential Scholars in Australia (2021). He is an ARC Future
fellow and a fellow of Queensland Academy of Arts and Sciences (FQA).

Linhao Luo received the bachelor degree from the
Harbin Institute of Technology, Shenzhen, in 2021.
He is currently working toward the PhD degree with
the Faculty of Information and Technology, Monash
University. His research interests include machine
learning, data mining, and graph neural networks.

Yufei Wang received the bachelor’s degree jointly
from the University of Queensland and Sun-Yat Sen
University, in 2016, and the master’s and PhD de-
grees from Macquarie University, under supervision
of Prof. Mark Johnson, in 2019 and 2023, respec-
tively. He is a research associate with Monash Uni-
versity, Australia. His research interests include large
language models, natural language processing, and
controllable text generation.

Chen Chen received the bachelor’s degree from the
University of Science and Technology Beijing, China,
in 2012, and the Msc degree from the University of
New South Wales, Australia, in 2018. He is currently
working toward the doctor of philosophy (PhD) de-
gree with Nanyang Technological University, Singa-
pore. His research interests include the area of natural
language processing, knowledge graphs, and large
language model.

Jiapu Wang is currently working toward the PhD
degree with the Beijing Municipal Key Laboratory
of Multimedia and Intelligent Software Technology,
Beijing University of Technology, Beijing. His re-
search interests include knowledge graph completion,
computer vision, and pattern recognition.

Xindong Wu (Fellow, IEEE) received the bachelor’s
and master’s degrees in computer science from the
Hefei University of Technology, China, and the PhD
degree in artiﬁcial intelligence from the University
of Edinburgh, Britain. He is director and professor
with the Key Laboratory of Knowledge Engineering
with Big Data (the Ministry of Education of China),
Hefei University of Technology, China. He is also
a senior research scientist with Zhejiang Lab, China.
His research interests include Big Data analytics, data
mining, and knowledge engineering. He is a foreign
member of the Russian Academy of Engineering, and a fellow of the AAAS
(American Association for the Advancement of Science). He is the Steering
Committee Chair of the IEEE International Conference on Data Mining (ICDM),
and the editor in-chief of Knowledge and Information Systems (KAIS, by
Springer). He was the editor-in-chief of IEEE Transactions on Knowledge
and Data Engineering (TKDE) between 2005 and 2008, and co-editor-in-chief
of the ACM Transactions on Knowledge Discovery from Data Engineering
between 2017 and 2020. He served as a program committee chair/co-chair
for ICDM 2003 (the 3rd IEEE International Conference on Data Mining),
KDD 2007 (the 13th ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining), CIKM 2010 (the 19th ACM Conference on
Information and Knowledge Management), and ICBK 2017 (the 8th IEEE
International Conference on Big Knowledge). One of his completed projects
is Knowledge Engineering With Big Data (BigKE), which was a 54-month,
45-million RMB, 15-institution national grand project, as described in detail at
https://ieeexplore.ieee.org/abstract/document/7948800

Authorized licensed use limited to: COLLEGE OF ENGINEERING - Pune. Downloaded on May 10,2026 at 08:28:57 UTC from IEEE Xplore. Restrictions apply.


---

> *End of P-13*

<br><br>
