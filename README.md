# StructAI: LLM-Powered Multi-Agent System for Automated Software Architecture Design and Education

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Node.js 20+](https://img.shields.io/badge/node.js-20+-green.svg)](https://nodejs.org/)
[![Next.js 14](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-00a86b.svg)](https://fastapi.tiangolo.com/)

---

## 🎯 Overview

**StructAI** is a full-stack, production-grade web application that automates software architecture design through an intelligent multi-agent Large Language Model (LLM) pipeline. Given a natural language problem statement, StructAI generates a complete, production-ready cloud-native architecture as an interactive visualization, explains each component's design rationale, and provides structured learning through adaptive quizzes.

### The Problem It Solves

Software architecture design is knowledge-intensive and time-consuming:
- **Manual Design**: Takes 45+ minutes for experienced engineers
- **Limited Tools**: Lucidchart, draw.io require manual placement; ChatGPT produces unstructured prose
- **Knowledge Gap**: Junior engineers and students lack deep architectural expertise
- **No Education**: Generated architectures lack pedagogical explanation

### The Solution

StructAI combines:
- **Automated Generation** via multi-agent LLM orchestration
- **Real-World Grounding** through RAG with 25 curated architecture patterns
- **Interactive Visualization** with React Flow diagrams
- **Explainability Engine** for component-level decision rationales
- **Integrated Learning** with 10 system design topics and adaptive quizzes

---

## 🚀 Key Features

### Core Functionality

| Feature | Description |
|---------|-------------|
| **Multi-Agent Pipeline** | Four-stage LangGraph orchestration: extraction → clarification → retrieval → synthesis |
| **RAG-Augmented Generation** | FAISS vector store with 25 real-world architecture patterns (Netflix, Uber, Discord, etc.) |
| **Interactive Visualization** | React Flow diagrams with automatic DAG layout and pan/zoom controls |
| **13 Component Types** | Load balancers, databases, caches, message queues, CDNs, ML services, and more |
| **Explainability** | Structured five-field explanations: what, why, alternatives, trade-offs, learn-more |
| **Adaptive Quizzes** | 10 system design topics with difficulty-level-based question generation |
| **Export Formats** | PDF and Markdown document generation |
| **User Analytics** | Design history, quiz performance, activity tracking |
| **OAuth Authentication** | Google Sign-In with role-based access control |
| **Multi-User Support** | Per-user design persistence and isolated workspaces |

### Evaluation Results

- **11× Faster**: 4.2 minutes vs 46.8 minutes for manual design
- **34% More Complete**: RAG improves architectural completeness over non-RAG baselines
- **High Quality**: Explanation quality rated **4.1/5.0** in user studies
- **User Study**: 20 participants with 90%+ task completion rate

---

## 🏗️ System Architecture

### Three-Tier Architecture

```
┌─────────────────────────────────────────────────────┐
│          PRESENTATION LAYER (Port 3000)             │
│   Next.js 14 • React • Tailwind • React Flow       │
│  ┌────────┬──────────┬────────┬────────┬─────────┐ │
│  │Landing │Dashboard │Builder │ Learn  │Analytics│ │
│  └────────┴──────────┴────────┴────────┴─────────┘ │
│              ↓ Axios (Bearer JWT)                   │
└─────────────────────────────────────────────────────┘
                      ↓ HTTPS REST
┌─────────────────────────────────────────────────────┐
│          APPLICATION LAYER (Port 8000)              │
│   FastAPI • LangGraph • Python 3.11                │
│  ┌────────┬────────┬────────┬──────────────────┐   │
│  │ Auth   │Designs │ Learn  │   Analytics      │   │
│  └────────┴────────┴────────┴──────────────────┘   │
│           LangGraph Pipeline (4 Nodes)             │
│      extract → clarify → retrieve → generate       │
└─────────────────────────────────────────────────────┘
      ↓           ↓              ↓           ↓
   OpenAI      FAISS Index    MongoDB    Integration
   GPT-4o      (25 patterns)   Atlas      Services
```

### LangGraph Pipeline

```
Problem Statement
       ↓
┌──────────────────┐
│   Extract Node   │ (GPT-4o, T=0)
└────────┬─────────┘
         ↓
    Has Ambiguities?
    ├─── YES ───→ Clarify Node ─→ User Input
    │                              ↓
    └─── NO ────┐                  │
                ↓                  ↓
            Retrieve Node      Retrieve Node (Again)
            (FAISS top-3)      (FAISS top-3)
                ↓                  ↓
            Generate Node (GPT-4o, T=0.2)
                ↓
            Architecture JSON
```

### Component Types Supported

| Component | Examples | Use Cases |
|-----------|----------|-----------|
| **Client** | React Native, Flutter | Mobile/Web frontends |
| **API Gateway** | Kong, AWS API Gateway | Request routing, rate limiting |
| **Load Balancer** | Nginx, HAProxy, AWS ALB | Traffic distribution |
| **Web Server** | Node.js, Spring, FastAPI | Application logic |
| **SQL Database** | PostgreSQL, MySQL | Structured data |
| **NoSQL Database** | MongoDB, Cassandra | Document/distributed data |
| **Cache** | Redis, Memcached | Performance optimization |
| **Message Queue** | Kafka, RabbitMQ, SQS | Async communication |
| **CDN** | CloudFront, Cloudflare | Static content delivery |
| **Object Storage** | S3, GCS | Blob storage |
| **Auth Service** | OAuth, Auth0, Keycloak | Identity & access |
| **Monitoring** | Prometheus, Grafana, Datadog | Observability |
| **ML Service** | TensorFlow Serving, SageMaker | ML inference |

---

## 💾 Tech Stack

### Backend
- **Framework**: FastAPI 0.111+
- **Server**: Uvicorn
- **LLM Orchestration**: LangGraph 0.1.19, LangChain 0.2.5
- **Vector Store**: FAISS (faiss-cpu 1.8.0)
- **Database Driver**: Motor 3.4.0 (async MongoDB)
- **LLM**: OpenAI GPT-4o via `langchain-openai`
- **Embeddings**: OpenAI text-embedding-ada-002
- **Authentication**: python-jose (HS256 JWT)
- **Document Export**: ReportLab 4.2.2, Markdown 3.6
- **HTTP Client**: httpx 0.27.0
- **Type Validation**: Pydantic 2.7.4
- **Python Version**: 3.11+

### Frontend
- **Framework**: Next.js 14 (App Router)
- **UI Library**: React 18
- **Styling**: Tailwind CSS 3.4.1
- **Visualization**: React Flow (@xyflow/react 12.0), DAG layout (@dagrejs/dagre 1.1.3)
- **Components**: Radix UI (Dialog, Select, Tabs, Toast, Progress)
- **HTTP Client**: Axios 1.7.2
- **State Management**: Zustand 4.5.2
- **Authentication**: NextAuth.js 4.24.7, jose 6.2.3
- **Icons**: Lucide React 0.383
- **Animations**: Framer Motion 11.2.10
- **Markdown**: react-markdown 9.0.1
- **TypeScript**: 5.x with strict mode

### Database & Services
- **Database**: MongoDB Atlas (M0 free tier for dev)
- **Authentication**: Google OAuth 2.0
- **LLM API**: OpenAI (GPT-4o)
- **Embeddings API**: OpenAI (text-embedding-ada-002)

### Development & Deployment
- **Containerization**: Docker
- **Version Control**: Git
- **Package Managers**: npm (Node.js), pip (Python)

---

## 📦 Installation & Setup

### Prerequisites

- **Python**: 3.11 or higher
- **Node.js**: 20 or higher
- **MongoDB**: Atlas account (free tier) or local MongoDB
- **OpenAI API Key**: For GPT-4o and embeddings
- **Google OAuth Credentials**: For authentication

### Backend Setup

1. **Create Python virtual environment**
   ```bash
   cd /path/to/StructAI/backend
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with:
   ```env
   # OpenAI
   OPENAI_API_KEY=sk-...
   
   # MongoDB
   MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/structai?retryWrites=true&w=majority
   MONGODB_DB_NAME=structai
   
   # JWT
   JWT_SECRET_KEY=your-secret-key-min-32-chars
   
   # Google OAuth (from Google Cloud Console)
   GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secret
   
   # CORS
   CORS_ORIGINS=["http://localhost:3000"]
   
   # API
   API_HOST=0.0.0.0
   API_PORT=8000
   
   # Logging
   LOG_LEVEL=INFO
   ```

4. **Initialize FAISS index**
   ```bash
   python scripts/initialize_faiss.py
   ```
   
   This loads 25 architecture patterns and creates the FAISS index.

5. **Run FastAPI server**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
   
   The API will be available at `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. **Install Node.js dependencies**
   ```bash
   cd /path/to/StructAI/frontend
   npm install
   ```

2. **Configure environment variables**
   ```bash
   cp .env.local.example .env.local
   ```
   
   Edit `.env.local` with:
   ```env
   # API
   NEXT_PUBLIC_API_URL=http://localhost:8000
   
   # OAuth
   NEXTAUTH_SECRET=your-nextauth-secret-min-32-chars
   NEXTAUTH_URL=http://localhost:3000
   
   # Google OAuth
   GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secret
   ```

3. **Run development server**
   ```bash
   npm run dev
   ```
   
   The frontend will be available at `http://localhost:3000`

4. **Build for production**
   ```bash
   npm run build
   npm start
   ```

---

## 🔧 Usage Guide

### For End Users

#### 1. Sign In
- Navigate to `http://localhost:3000`
- Click "Sign in with Google"
- Authorize the application

#### 2. Generate Architecture
1. Click **"New Design"** on the dashboard
2. Enter a natural language problem statement:
   ```
   Example: "Build a real-time collaboration platform like Figma
   that supports concurrent editing, persistence, and 10M+ daily users."
   ```
3. If ambiguities are detected, answer clarifying questions
4. Review the generated architecture diagram
5. Click any component to see its explanation

#### 3. Understand Components
- **What**: Component description and purpose
- **Why**: Rationale for its selection in this architecture
- **Alternatives**: Other viable options and when to use them
- **Trade-offs**: Performance, cost, complexity considerations
- **Learn More**: Link to deeper learning material

#### 4. Learn & Quiz
1. Navigate to **"Learn"** section
2. Select a topic (e.g., "Load Balancing Strategies")
3. Take adaptive quizzes (3 difficulty levels)
4. View explanations for each answer
5. Track progress on dashboard

#### 5. Export Design
- Click **"Export"** on completed design
- Choose **PDF** or **Markdown** format
- Download professionally formatted document

### For Developers

#### API Endpoints

**Authentication**
```bash
POST /api/v1/auth/login
POST /api/v1/auth/logout
GET  /api/v1/auth/me
```

**Design Generation**
```bash
POST /api/v1/designs/generate
  Request: { "problem_statement": "..." }
  Response: { "design_id": "...", "architecture": {...}, "status": "pending|awaiting_clarification|complete" }

POST /api/v1/designs/{design_id}/clarify
  Request: { "clarifications": {...} }
  Response: { "architecture": {...}, "status": "complete" }

GET /api/v1/designs/{design_id}
GET /api/v1/designs
DELETE /api/v1/designs/{design_id}
```

**Learn & Quiz**
```bash
GET /api/v1/topics
GET /api/v1/topics/{topic_id}
POST /api/v1/quizzes
  Request: { "topic_id": "...", "answers": [...] }
  Response: { "score": 85, "passed": true, "explanations": [...] }

GET /api/v1/quiz-history
```

**Analytics**
```bash
GET /api/v1/analytics/dashboard
GET /api/v1/analytics/quiz-history
```

---

## 📁 Project Structure

```
StructAI/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application entry point
│   │   ├── config.py               # Configuration & environment variables
│   │   ├── dependencies.py         # Dependency injection (auth, database)
│   │   ├── models/
│   │   │   ├── user.py            # User schema
│   │   │   ├── design.py          # Design schema
│   │   │   └── quiz.py            # Quiz schema
│   │   ├── schemas/
│   │   │   ├── design_request.py   # Request/response schemas
│   │   │   ├── architecture.py     # Architecture output schema
│   │   │   └── quiz_schema.py      # Quiz schemas
│   │   ├── routers/
│   │   │   ├── auth.py            # /api/v1/auth endpoints
│   │   │   ├── designs.py         # /api/v1/designs endpoints
│   │   │   ├── learn.py           # /api/v1/learn endpoints
│   │   │   └── analytics.py       # /api/v1/analytics endpoints
│   │   ├── core/
│   │   │   ├── security.py        # JWT utilities, OAuth
│   │   │   ├── database.py        # MongoDB client setup
│   │   │   └── llm.py             # LLM client setup
│   │   ├── services/
│   │   │   ├── design_service.py  # Architecture generation logic
│   │   │   ├── rag_service.py     # FAISS & pattern retrieval
│   │   │   ├── explanation_service.py # Component explanations
│   │   │   ├── quiz_service.py    # Quiz generation & grading
│   │   │   └── export_service.py  # PDF/Markdown export
│   │   ├── agents/
│   │   │   ├── extract_agent.py   # Requirement extraction
│   │   │   ├── clarify_agent.py   # Ambiguity clarification
│   │   │   ├── retrieve_agent.py  # Pattern retrieval
│   │   │   └── generate_agent.py  # Architecture synthesis
│   │   └── pipeline/
│   │       └── design_pipeline.py # LangGraph orchestration
│   ├── scripts/
│   │   ├── initialize_faiss.py    # Build FAISS index from patterns
│   │   └── seed_patterns.py       # Load architecture patterns
│   ├── patterns/                  # 25 real-world architecture patterns
│   │   ├── netflix.md
│   │   ├── uber.md
│   │   ├── discord.md
│   │   └── ... (22 more)
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example               # Environment template
│   └── README.md                  # Backend documentation
│
├── frontend/
│   ├── app/
│   │   ├── layout.tsx             # Root layout
│   │   ├── page.tsx               # Landing page
│   │   ├── dashboard/
│   │   │   └── page.tsx           # Dashboard
│   │   ├── design/
│   │   │   ├── page.tsx           # Design list
│   │   │   ├── [id]/
│   │   │   │   └── page.tsx       # Design detail & builder
│   │   │   └── new/
│   │   │       └── page.tsx       # New design form
│   │   ├── learn/
│   │   │   ├── page.tsx           # Topics list
│   │   │   └── [id]/
│   │   │       └── page.tsx       # Quiz interface
│   │   ├── analytics/
│   │   │   └── page.tsx           # User analytics
│   │   ├── api/
│   │   │   └── auth/
│   │   │       └── [...nextauth]/  # NextAuth.js API routes
│   │   └── globals.css            # Global styles
│   ├── components/
│   │   ├── ui/
│   │   │   ├── button.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── select.tsx
│   │   │   ├── tabs.tsx
│   │   │   ├── toast.tsx
│   │   │   └── progress.tsx
│   │   ├── layout/
│   │   │   ├── navbar.tsx
│   │   │   ├── sidebar.tsx
│   │   │   └── footer.tsx
│   │   ├── design/
│   │   │   ├── architecture-canvas.tsx
│   │   │   ├── node-explanation.tsx
│   │   │   ├── export-dialog.tsx
│   │   │   └── clarification-modal.tsx
│   │   ├── learn/
│   │   │   ├── quiz-interface.tsx
│   │   │   └── topic-card.tsx
│   │   └── analytics/
│   │       ├── stats-grid.tsx
│   │       └── quiz-history.tsx
│   ├── hooks/
│   │   ├── useDesign.ts           # Design generation hook
│   │   ├── useAuth.ts             # Authentication hook
│   │   └── useQuiz.ts             # Quiz interaction hook
│   ├── lib/
│   │   ├── api.ts                 # API client
│   │   ├── auth.ts                # Auth utilities
│   │   ├── types.ts               # TypeScript types
│   │   └── constants.ts           # Constants
│   ├── store/
│   │   ├── designStore.ts         # Design state (Zustand)
│   │   └── authStore.ts           # Auth state (Zustand)
│   ├── next.config.js
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   ├── package.json
│   ├── .env.local.example         # Environment template
│   └── README.md                  # Frontend documentation
│
├── docker/
│   ├── Dockerfile.backend         # Backend container
│   ├── Dockerfile.frontend        # Frontend container
│   └── docker-compose.yml         # Multi-container orchestration
│
├── research papers/               # 25 architecture pattern documents
├── Paper.md                       # Research paper (academic)
├── Blackbook.md                   # Project documentation (detailed)
├── Base_Papers.md                 # Literature references
├── working.md                     # Development notes
└── README.md                      # This file
```

---

## 🧠 How It Works: The Four-Stage Pipeline

### Stage 1: Requirement Extraction
**Agent**: GPT-4o (temperature=0)
**Input**: Natural language problem statement
**Output**: Structured requirements object
```json
{
  "functional_requirements": ["Real-time collaboration", "Persistence"],
  "non_functional_requirements": ["Supports 10M DAU", "P99 latency < 200ms"],
  "scale_metrics": {"daily_active_users": 10000000},
  "ambiguities": ["Definition of 'real-time'", "Geographic distribution?"]
}
```

### Stage 2: Ambiguity Clarification
**Agent**: GPT-4o (temperature=0)
**Condition**: Triggered if `ambiguities` list is non-empty
**Output**: 2-4 clarifying questions for the user
**User Input**: Answers to clarifying questions
**Impact**: Refines requirements for more accurate generation

### Stage 3: Retrieval-Augmented Generation
**Method**: FAISS semantic similarity search
**Input**: Extracted requirements + clarifications
**Process**:
1. Embed requirements using `text-embedding-ada-002`
2. Query FAISS index for top-3 most similar patterns
3. Retrieve full pattern documents
4. Concatenate patterns as `rag_context`

**Sample Patterns**: Netflix (microservices), Uber (real-time dispatch), Discord (WebSocket architecture), Twitter (feed generation), Airbnb (search), Dropbox (sync), Slack (messaging), etc.

### Stage 4: Architecture Synthesis
**Agent**: GPT-4o (temperature=0.2)
**Input**: Requirements + RAG context
**Output**: Complete architecture JSON
```json
{
  "summary": "A microservices-based real-time collaboration platform...",
  "nodes": [
    {
      "id": "client",
      "type": "client",
      "label": "Web Client",
      "technologies": ["React 18", "WebSocket client"]
    },
    {...}
  ],
  "edges": [
    {"source": "client", "target": "api_gateway", "label": "HTTPS"}
  ],
  "tech_stack": {
    "frontend": ["React", "WebSocket"],
    "backend": ["Node.js", "Kafka"],
    "database": ["PostgreSQL", "Redis"]
  }
}
```

---

## 🎓 Learning Module

The system provides 10 curated system design topics:

1. **Load Balancing Strategies** — Consistent hashing, sticky sessions, algorithms
2. **Database Design Patterns** — Sharding, replication, CQRS
3. **Caching Strategies** — Cache-aside, write-through, cache invalidation
4. **Message Queue Systems** — Pub-sub, FIFO, exactly-once delivery
5. **API Design** — REST vs gRPC, versioning, rate limiting
6. **Real-Time Systems** — WebSockets, Server-Sent Events, polling
7. **Microservices Architecture** — Service discovery, circuit breakers, saga patterns
8. **Data Consistency** — ACID vs BASE, eventual consistency
9. **Security in Distributed Systems** — JWT, mTLS, OAuth
10. **Monitoring & Observability** — Metrics, tracing, logging

Each topic includes:
- **Overview**: Key concepts and motivation
- **Adaptive Quizzes**: 3 difficulty levels (Beginner, Intermediate, Advanced)
- **Explanations**: Why each answer is correct/incorrect
- **References**: Links to deeper learning materials

---

## 🔐 Security Architecture

### Authentication Flow
```
User → Google OAuth 2.0 → NextAuth.js → HS256 JWT
                                              ↓
                              Stored in httpOnly cookie
                                              ↓
                           Sent with every API request
                                              ↓
                        FastAPI decodes & verifies JWT
                                              ↓
                        Fetches user from MongoDB
                                              ↓
                        Enforces role-based access
```

### Security Features

| Layer | Mechanism | Details |
|-------|-----------|---------|
| **Authentication** | Google OAuth 2.0 | Industry-standard identity provider |
| **Token** | HS256 JWT | HMAC-SHA256 signed, httpOnly cookie |
| **Authorization** | Role-Based Access Control | User, Moderator, Admin roles |
| **Data Isolation** | MongoDB `user_id` filters | Every query filtered by authenticated user |
| **Transport** | HTTPS/TLS | All production traffic encrypted |
| **CORS** | Whitelist origin | Prevents cross-origin attacks |
| **Input Validation** | Pydantic strict schemas | All inputs validated server-side |
| **Token Verification** | Never trust JWT claims | Role verified in MongoDB on every request |

---

## 📊 Evaluation Results

### Quantitative Metrics

**Architecture Completeness (RAG vs. Non-RAG)**

| Metric | RAG | Non-RAG | Improvement |
|--------|-----|---------|-------------|
| Average nodes per design | 8.2 | 6.1 | +34% |
| Avg tech stack items | 5.8 | 3.9 | +49% |
| Missing components | 1.2 | 3.1 | -61% |

**User Study (n=20)**

| Metric | StructAI | Manual Design | Improvement |
|--------|----------|---------------|-------------|
| Avg task time (minutes) | 4.2 | 46.8 | 11× faster |
| Task completion rate | 90% | 85% | +5% |
| User confidence (1-5) | 4.3 | 3.8 | +13% |
| Explanation quality (1-5) | 4.1 | N/A | — |
| Would recommend (%) | 85% | 60% | +42% |

**Performance Benchmarks**

| Operation | Target | Actual | Status |
|-----------|--------|--------|--------|
| FAISS retrieval latency | ≤100ms | 45ms | ✓ Pass |
| Design generation (no clarify) | ≤7s | 5.8s | ✓ Pass |
| Design generation (with clarify) | ≤12s | 10.2s | ✓ Pass |
| API response latency | ≤500ms | 280ms | ✓ Pass |

### Qualitative Feedback

**User Comments**:
- *"It saved me 45 minutes. I got a professional architecture without being an expert."*
- *"The explanations actually teach me why each component is important."*
- *"Much better than manually placing boxes in Lucidchart."*

**Limitations Identified**:
- Cannot generate architectures for embedded systems or HPC
- RAG corpus is limited to cloud-native, web-scale systems
- No real-time collaborative editing

---

## 🛠️ Configuration & Customization

### Adjusting Pipeline Temperature

Edit `backend/app/agents/*.py` to modify LLM creativity:

```python
# More deterministic (0 = deterministic, 1 = creative)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# For generation (slightly more creative)
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
```

### Adding New Architecture Patterns

1. Create pattern document: `backend/patterns/my_pattern.md`
2. Run initialization script:
   ```bash
   python backend/scripts/initialize_faiss.py
   ```
3. FAISS index automatically rebuilds with new patterns

### Customizing Quiz Topics

Edit `backend/app/data/topics.json`:
```json
{
  "id": "topic-11",
  "title": "Custom Topic",
  "description": "...",
  "difficulty_levels": {
    "beginner": "...",
    "intermediate": "...",
    "advanced": "..."
  }
}
```

---

## 🐳 Docker Deployment

### Build Images

```bash
# Backend
docker build -f docker/Dockerfile.backend -t structai-backend:latest .

# Frontend
docker build -f docker/Dockerfile.frontend -t structai-frontend:latest .
```

### Run with Docker Compose

```bash
docker-compose -f docker/docker-compose.yml up -d
```

### Environment Variables for Docker

Create `.env` in project root:
```env
OPENAI_API_KEY=sk-...
MONGODB_URI=mongodb+srv://...
JWT_SECRET_KEY=your-secret
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
NEXTAUTH_SECRET=...
```

---

## 🔄 CI/CD Pipeline

The project includes GitHub Actions workflows:

- `.github/workflows/test.yml` — Unit and integration tests
- `.github/workflows/lint.yml` — Code quality checks
- `.github/workflows/deploy.yml` — Production deployment

---

## 📚 Documentation

- **[Backend README](backend/README.md)** — API documentation, service details
- **[Frontend README](frontend/README.md)** — Component library, state management
- **[Paper.md](Paper.md)** — Full academic research paper (IEEE format)
- **[Blackbook.md](Blackbook.md)** — Detailed project report with figures and tables
- **[API Docs](http://localhost:8000/docs)** — Interactive Swagger UI (when running)

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Code Style

- **Python**: PEP 8 via Black formatter
- **TypeScript/JavaScript**: ESLint + Prettier
- **Commit messages**: Conventional Commits

### Testing

```bash
# Backend tests
cd backend
pytest tests/ -v --cov=app

# Frontend tests
cd frontend
npm test
```

---

## 🐛 Known Issues & Limitations

### Current Limitations

1. **Domain Scope**: Optimized for cloud-native, web-scale architectures only
2. **No Code Generation**: Produces architecture diagrams, not executable code
3. **Single Tenant**: No real-time multi-user collaboration
4. **RAG Corpus**: Limited to 25 patterns; expanding with user feedback
5. **LLM Dependency**: Requires OpenAI API key; cannot use local models

### Known Issues

- Large architectures (20+ nodes) may have overlapping labels in React Flow
- PDF export may have formatting issues with very long component names
- RAG retrieval may occasionally return patterns with marginal relevance

---

## 📈 Future Work

1. **Graph RAG**: Migrate from flat FAISS to knowledge graph for better pattern relationships
2. **Code Generation**: Add Infrastructure-as-Code (Terraform, Kubernetes manifests) output
3. **Real-Time Collaboration**: Multi-user concurrent editing
4. **Local LLM Support**: Ollama/Llama integration for offline use
5. **Mobile App**: React Native client for iOS/Android
6. **Expanded Domains**: Embedded systems, HPC, blockchain architectures
7. **Community Patterns**: User-contributed architecture patterns
8. **Conversation Mode**: Multi-turn chat for iterative architecture refinement

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) file for details.

---

## 👥 Authors

**Team Members**:
- **Akshat D. More**
- **Narendra B. Tekale**
- **Yash D. Thakare**
- **Neha B. Yengandul**

**Institution**:
Department of Artificial Intelligence and Machine Learning  
PES's Modern College of Engineering  
Savitribai Phule Pune University, India

**Academic Year**: 2025–2026

---

## 🙏 Acknowledgements

We thank:
- Our project guide and HoD for mentorship and infrastructure
- The open-source community: LangGraph, LangChain, FAISS, Next.js, FastAPI, React Flow
- OpenAI for the GPT-4o and embedding APIs
- Our 20 user study participants for valuable feedback

---

## 📧 Contact & Support

- **Email**: [structai26@gmail.com](mailto:structai26@gmail.com)
- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)

---

## 📖 Citation

If you use StructAI in your research, please cite:

```bibtex
@article{more2026structai,
  title={StructAI: An LLM-Powered Multi-Agent System for Automated Software Architecture Design and Education},
  author={More, Akshat D. and Tekale, Narendra B. and Thakare, Yash D. and Yengandul, Neha B.},
  journal={PES's Modern College of Engineering},
  year={2026}
}
```

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Production Ready
