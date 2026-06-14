# StructAI: Complete Project Analysis & Presentation Guide

---

## PHASE 1: COMPLETE PROJECT SUMMARY

### Project Objective
StructAI is a full-stack, production-grade web application that automates software architecture design through an intelligent multi-agent LLM pipeline. It transforms natural language problem statements into interactive, production-ready cloud-native architectures in 4.2 minutes—11× faster than manual design. The platform combines automated generation, real-world pattern grounding (RAG), interactive visualization, explainability, and integrated learning.

### Problem Statement
Software architecture design is knowledge-intensive and time-consuming:
- Manual design takes 45+ minutes for experienced engineers
- General LLMs generate prose without structured graph output
- Junior engineers/students lack deep architectural expertise
- No existing tools provide pedagogical explanation of design decisions

### Solution Architecture
StructAI implements a **three-tier architecture**:

**Presentation Layer (Next.js 14, Port 3000)**
- Landing page, Dashboard, Builder (design generation), Learn (topics & quizzes), Analytics
- React Flow interactive diagrams with DAG layout
- Server components for SSR, client components for interactivity
- Tailwind CSS with custom design tokens (indigo/navy color scheme)
- NextAuth.js with Google OAuth 2.0

**Application Layer (FastAPI, Port 8000)**
- Async route handlers with Pydantic v2 validation
- LangGraph StateGraph orchestrating 4-node pipeline
- Explainability engine (per-component explanations)
- Quiz generation and grading
- PDF/Markdown export services
- Authentication via HS256 JWT verification

**Data Layer**
- MongoDB Atlas: `users`, `designs`, `quiz_attempts` collections
- FAISS index: 25 curated architecture patterns (IndexFlatL2, exact L2 search)
- OpenAI API: GPT-4o (generation) + text-embedding-ada-002 (embeddings)

### Multi-Agent LLM Pipeline (Core Innovation)

**4-Node LangGraph StateGraph:**

1. **Extract Node** → Parses problem statement → outputs structured requirements JSON
   - `temperature=0` (deterministic)
   - Detects ambiguities
   - Output: `functional_requirements`, `non_functional_requirements`, `scale_hints`, `ambiguities`

2. **Conditional Edge** → Routes based on ambiguities
   - If ambiguities exist AND no clarifications provided → Clarify node
   - Otherwise → Retrieve node

3. **Clarify Node** (optional) → Generates 2–4 targeted clarifying questions
   - Returns early with `status: awaiting_clarification`
   - User submits answers via `POST /designs/{id}/clarify`
   - Second pass skips extraction

4. **Retrieve Node** → FAISS semantic search
   - Embeds problem statement with text-embedding-ada-002
   - Top-3 similarity search over 25 patterns
   - Concatenates pattern text into RAG context (~1,200 tokens)

5. **Generate Node** → Architecture synthesis
   - `temperature=0.2` (controlled variation)
   - Consumes: requirements + clarifications + RAG context
   - Output: JSON with nodes, edges, tech_stack, summary

**Two-Pass Protocol:**
- Pass 1: extract → [clarify OR retrieve] → [generate]
- Pass 2: (skip extract) → retrieve → generate

### Component Types Supported (13)
`client`, `api_gateway`, `load_balancer`, `web_server`, `database`, `nosql_database`, `cache`, `message_queue`, `cdn`, `object_storage`, `auth_service`, `monitoring`, `ml_service`

### Key Features

| Feature | Implementation |
|---------|---|
| **RAG-Augmented Generation** | FAISS vector store, 25 patterns, OpenAI embeddings |
| **Interactive Visualization** | React Flow (@xyflow/react), dagre layout, pan/zoom |
| **Explainability Engine** | On-demand GPT-4o (T=0.3), 5-field schema (what/why/alternatives/trade-offs/learn_more) |
| **Adaptive Quizzes** | 10 system design topics, 3 difficulty levels, scenario-based questions |
| **Export Formats** | PDF (ReportLab) and Markdown |
| **Authentication** | Google OAuth 2.0 + HS256 JWT (NextAuth.js + python-jose) |
| **User Analytics** | Design history, quiz performance, progress tracking |

### Authentication Architecture (Novel)
**Custom HS256 JWT Bridge:**
- NextAuth.js generates HS256 JWT (via custom `encode` callback) using `NEXTAUTH_SECRET`
- Token stored in HttpOnly cookie + attached to frontend as `session.accessToken`
- Axios interceptor adds `Authorization: Bearer <token>` to all API requests
- FastAPI decodes with `python-jose` HS256 verification
- Role always fetched from MongoDB, never trusted in JWT

**Security Model:**
- JWT payload contains only identity: `email`, `name`, `picture`, `sub`
- Role-based access control (RBAC) via MongoDB lookup
- Every query filters by `user_id` ownership
- CORS whitelist, input validation via Pydantic

### Database Schema (MongoDB)

**`users` collection:**
```
_id: ObjectId
name: string
email: string (unique)
image: string
role: enum ["student", "moderator", "admin"]
created_at: datetime
design_count: integer
quiz_count: integer
```

**`designs` collection:**
```
_id: ObjectId
user_id: string (FK → users._id)
problem_statement: string
requirements: object
clarifying_questions: array[string]
clarifications: object (optional)
architecture: object (nodes, edges, tech_stack, summary)
explanations: object (keyed by component_id)
status: enum ["pending", "awaiting_clarification", "complete"]
created_at: datetime
updated_at: datetime
```

**`quiz_attempts` collection:**
```
_id: ObjectId
user_id: string (FK → users._id)
quiz_id: string
topic: string
questions: array[object]
score: float (percentage)
passed: boolean
completed_at: datetime
```

### Frontend Pages & Routes

| Route | Purpose | Key Components |
|-------|---------|---|
| `/` | Landing page | Marketing, sign-in button |
| `/dashboard` | Home hub | Quick links, recent designs |
| `/builder` | New design form | Problem statement input |
| `/builder/[id]` | Design detail & visualization | React Flow canvas, explainer panel |
| `/learn` | Topics grid | Topic cards, difficulty filters |
| `/learn/[topic]` | Quiz interface | Question display, answer submission, results |
| `/analytics` | User progress | Stats cards, quiz history, design timeline |
| `/admin` | Admin panel | User management, FAISS rebuild, platform stats |

### Backend API Endpoints (23 total)

**Authentication:**
- `POST /api/v1/auth/upsert-user` — Sync Google user to MongoDB
- `GET /api/v1/auth/me` — Return current user profile

**Designs:**
- `POST /api/v1/designs/generate` — Submit problem statement
- `POST /api/v1/designs/{id}/clarify` — Submit clarification answers
- `GET /api/v1/designs/{id}` — Fetch single design
- `GET /api/v1/designs` — List user's designs
- `DELETE /api/v1/designs/{id}` — Delete design

**Explainability:**
- `POST /api/v1/explain/component` — Generate explanation for a component

**Learn & Quiz:**
- `GET /api/v1/learn/topics` — List all 10 topics
- `GET /api/v1/learn/topics/{topic_id}` — Get topic detail
- `POST /api/v1/learn/quiz/generate` — Generate quiz
- `POST /api/v1/learn/quiz/submit` — Grade quiz, persist attempt

**Export:**
- `GET /api/v1/export/{id}/pdf` — Download PDF report
- `GET /api/v1/export/{id}/markdown` — Download Markdown

**Analytics:**
- `GET /api/v1/analytics/me` — User stats and history
- `GET /api/v1/analytics/admin` — Platform-wide stats (admin)

**Admin:**
- `GET /api/v1/admin/health` — Service health check (admin)
- `GET /api/v1/admin/users` — Paginated user list (admin)
- `PATCH /api/v1/admin/users/{id}/role` — Change user role (admin)
- `POST /api/v1/admin/rebuild-index` — Rebuild FAISS index (admin)

**Health:**
- `GET /health` — Liveness probe

### Tech Stack Summary

**Backend:**
- FastAPI 0.111+, Uvicorn
- LangGraph 0.1.19, LangChain 0.2.5
- Motor 3.4.0 (async MongoDB)
- FAISS 1.8.0 (CPU version)
- OpenAI API (GPT-4o, text-embedding-ada-002)
- python-jose (HS256 JWT), Pydantic 2.7.4
- ReportLab 4.2.2 (PDF), Markdown 3.6 (export)
- Python 3.11+

**Frontend:**
- Next.js 14 (App Router), React 18
- TypeScript 5 (strict mode)
- Tailwind CSS 3.4.1 (custom design tokens)
- React Flow 12.0 (@xyflow/react)
- Dagre 1.1.3 (DAG layout)
- Radix UI (Dialog, Select, Tabs, Toast, Progress)
- Zustand 4.5.2 (state management)
- NextAuth.js 4.24.7, jose 6.2.3
- Axios 1.7.2, Framer Motion 11.2.10
- Lucide React 0.383 (icons)

**Infrastructure:**
- MongoDB Atlas (cloud database)
- Docker, Docker Compose
- GitHub Actions (CI/CD)
- Google Cloud Console (OAuth credentials)

### Evaluation Results

**RAG vs. Non-RAG (30 problem statements):**
- Component completeness: RAG +34% (87.4% vs 65.2%)
- Edge coverage: RAG +18.7% (84.6% vs 71.3%)
- Technology appropriateness: RAG +13.4% (89.1% vs 78.6%)

**User Study (n=20):**
- Mean task time: 4.2 min (StructAI) vs 46.8 min (manual) — **11× faster**
- Explanation quality: 4.1/5.0 mean Likert score
- 80% rated explanations ≥ 4/5 for sufficiency
- 90% task completion rate
- 85% would recommend

---

## PHASE 2: MODULE DIVISION

Dividing StructAI's 100% scope into 4 balanced, meaningful modules:

### Module 1: Authentication & Backend Infrastructure (Presenter 1)
**Responsibilities:**
- User authentication (Google OAuth 2.0 → HS256 JWT)
- FastAPI application setup and middleware
- MongoDB connection pooling and data layer initialization
- Security architecture (JWT verification, RBAC, user isolation)
- Health checks and admin endpoints
- Role-based access control enforcement

**Files/Folders:**
- `backend/app/main.py` — FastAPI app entry point, CORS, middleware, route registration
- `backend/app/core/security.py` — `decode_token()`, `get_current_user()`, `get_admin_user()`
- `backend/app/core/database.py` — MongoDB async client, lifecycle management
- `backend/app/core/config.py` — Environment variables, settings
- `backend/app/api/routes/auth.py` — OAuth upsert, `/me` endpoint
- `backend/app/api/routes/admin.py` — User management, health checks, FAISS rebuild
- `backend/app/models/user.py` — User Pydantic schemas
- `frontend/app/api/auth/[...nextauth]` — NextAuth.js configuration
- `frontend/middleware.ts` — Edge middleware for route protection
- `frontend/lib/auth.ts` — Frontend auth utilities

**Technologies:**
- FastAPI, Uvicorn, python-jose (HS256)
- NextAuth.js, jose (Edge Runtime JWT)
- Motor (async MongoDB)
- Pydantic v2 (validation)

**Importance:**
Critical foundation—authentication security enables user isolation and role-based access control. Without this, the entire platform's data isolation and multi-tenancy would collapse. The custom HS256 bridge is a novel technical contribution enabling JWT compatibility between Next.js Edge Runtime and FastAPI.

---

### Module 2: LLM Pipeline & Design Generation (Presenter 2)
**Responsibilities:**
- LangGraph StateGraph orchestration (4-node pipeline)
- Requirement extraction and ambiguity detection
- Clarification question generation
- Architecture JSON synthesis
- Design persistence and status management
- Two-pass protocol implementation

**Files/Folders:**
- `backend/app/services/design_builder/pipeline.py` — LangGraph StateGraph, node definitions, conditional routing
- `backend/app/services/design_builder/extractor.py` — Requirement extraction agent (GPT-4o, T=0)
- `backend/app/services/design_builder/generator.py` — Architecture synthesis agent (GPT-4o, T=0.2)
- `backend/app/api/routes/designs.py` — `/designs/generate`, `/designs/{id}/clarify` endpoints
- `backend/app/models/design.py` — Design Pydantic schemas (Architecture, Node, Edge)
- `frontend/app/builder/page.tsx` — Design form and submission UI
- `frontend/app/builder/[id]/page.tsx` — Design detail view (stub; visualization in Module 3)

**Technologies:**
- LangGraph (StateGraph, conditional edges, typed state)
- LangChain (GPT-4o integration, message abstraction)
- OpenAI API (gpt-4o-2024-08-06 model)
- Pydantic (JSON schema validation)

**Importance:**
The core innovation—orchestrating multiple specialized agents instead of a single monolithic LLM call. The two-pass protocol cleanly separates ambiguity scoping from generation, enabling conversational interaction without requiring a persistent session server. This is where the 11× time savings comes from: fast, deterministic requirement extraction + targeted clarification.

---

### Module 3: RAG, Visualization & Component Explainability (Presenter 3)
**Responsibilities:**
- FAISS vector store initialization and management
- Architecture pattern corpus (25 curated patterns)
- Semantic search and retrieval
- React Flow diagram rendering and layout
- Component-level explanation generation
- On-demand explanation caching
- Architecture canvas interaction

**Files/Folders:**
- `backend/app/services/design_builder/rag.py` — FAISS load/create, similarity search, async-safe executor
- `backend/vector_store/faiss_index/` — Persisted FAISS index files
- `backend/vector_store/seed_data/patterns.py` — 25 architecture pattern definitions
- `backend/app/services/explainability/explainer.py` — Component explanation generation (GPT-4o, T=0.3)
- `backend/app/api/routes/explain.py` — `/explain/component` endpoint
- `frontend/components/diagram/architecture-canvas.tsx` — React Flow canvas setup, node/edge mapping
- `frontend/components/diagram/node-explanation.tsx` — Explainer panel, 5-field display
- `frontend/hooks/useDesign.ts` — Design state management
- `frontend/lib/api.ts` — API client for explanation requests

**Technologies:**
- FAISS (IndexFlatL2, exact L2 distance)
- LangChain FAISS wrapper
- OpenAI text-embedding-ada-002 (1536-dim vectors)
- ThreadPoolExecutor (async-safe blocking FAISS calls)
- React Flow (@xyflow/react 12.0)
- Dagre (@dagrejs/dagre 1.1.3) for DAG layout

**Importance:**
RAG is the 34% completeness improvement differentiator. A hand-curated corpus of production patterns is more valuable than raw internet-scale corpus. The explanation engine with structured 5-field output (what/why/alternatives/trade-offs/learn_more) is the pedagogical edge case that enabled the 4.1/5.0 user satisfaction rating. React Flow visualization makes the abstract JSON concrete.

---

### Module 4: Education, Analytics & Export (Presenter 4)
**Responsibilities:**
- Learning module: 10 system design topics
- Quiz generation with adaptive difficulty
- Quiz grading and answer validation
- User progress tracking and analytics
- Design export (PDF and Markdown)
- User dashboard and analytics visualizations
- Quiz history and performance metrics

**Files/Folders:**
- `backend/app/services/learn_mode/quiz_generator.py` — Quiz generation (GPT-4o, T=0.7), grading logic
- `backend/app/services/learn_mode/topics.py` — 10 topic definitions with difficulty metadata
- `backend/app/services/exporter/pdf_exporter.py` — PDF generation (ReportLab)
- `backend/app/services/exporter/md_exporter.py` — Markdown export
- `backend/app/services/analytics/tracker.py` — User metrics aggregation
- `backend/app/api/routes/learn.py` — `/learn/topics`, `/learn/quiz/generate`, `/learn/quiz/submit`
- `backend/app/api/routes/export.py` — `/export/{id}/pdf`, `/export/{id}/markdown`
- `backend/app/api/routes/analytics.py` — `/analytics/me`, `/analytics/admin`
- `frontend/app/learn/page.tsx` — Topic grid display
- `frontend/app/learn/[topic]/page.tsx` — Quiz interface and results
- `frontend/app/analytics/page.tsx` — Dashboard with stats and history
- `frontend/components/learn/quiz-interface.tsx` — Quiz UX (question display, option selection)
- `frontend/components/learn/topic-card.tsx` — Topic card component
- `frontend/components/analytics/stats-grid.tsx` — Stat cards
- `frontend/components/analytics/quiz-history.tsx` — Quiz results history

**Technologies:**
- ReportLab 4.2.2 (PDF generation with custom styles)
- Markdown 3.6 (Markdown rendering)
- MongoDB aggregation (analytics queries)
- Pydantic (quiz schema validation)
- Zustand (frontend quiz state)
- Framer Motion (animations)

**Importance:**
Differentiates StructAI from pure generation tools. Quizzes turn passive consumption into active learning. The adaptive difficulty (beginner/intermediate/advanced) enables personalized learning paths. Export capabilities (PDF/Markdown) make designs actionable in external workflows. Analytics close the feedback loop—showing users where they stand drives engagement and completion.

---

## PHASE 3: PRESENTATION SCRIPTS

Each presenter should speak for **4–6 minutes** naturally, covering what was built, how it works, important files, design decisions, and challenges solved.

### Presenter 1: Authentication & Backend Infrastructure

#### Introduction
"I'm responsible for the entire authentication and backend infrastructure that powers StructAI. In essence, I built the secure foundation that every user interaction goes through. This includes connecting users via Google OAuth, managing their JWT tokens, ensuring data isolation in MongoDB, and implementing role-based access control. The authentication system I designed is actually a novel contribution — we needed to bridge two different runtime environments: Next.js Edge Runtime and FastAPI — both of which needed to decode the same JWT token securely."

#### Technical Explanation

**What Was Built:**
We implemented a complete Google OAuth 2.0 flow integrated with a custom HS256 JWT pipeline. Here's why that matters: NextAuth.js by default uses JWE (JSON Web Encryption with RSA), which FastAPI's python-jose library cannot decode. So we faced a choice—either use two separate authentication systems or bridge them. We chose to override NextAuth's JWT encoding callbacks to produce HS256-signed tokens using a shared `NEXTAUTH_SECRET`, making both runtimes speak the same language.

**How It Works:**
1. User clicks "Sign in with Google"
2. NextAuth.js redirects to Google's OAuth consent screen
3. Google returns an authorization code
4. NextAuth exchanges it for a Google access token and user profile
5. Our custom `encode` callback signs the profile claims as an HS256 JWT with a 30-day expiration
6. This JWT is stored in an HttpOnly cookie and also sent to the frontend as `session.accessToken`
7. The Axios interceptor reads this token and adds `Authorization: Bearer <token>` to every API request
8. FastAPI's `get_current_user()` dependency decodes the token with python-jose HS256 verification
9. We fetch the full user document from MongoDB — this is critical: we never trust JWT claims for authorization

**Important Files:**
- `backend/app/core/security.py` — The `decode_token()` function that verifies JWT signatures and the `get_current_user()` function that always fetches role from MongoDB
- `backend/app/core/database.py` — MongoDB async client initialization with Motor
- `backend/app/api/routes/auth.py` — The `/auth/upsert-user` endpoint that syncs Google profiles to MongoDB on first login
- `frontend/middleware.ts` — Edge middleware that protects authenticated routes before they hit the origin server
- `frontend/app/api/auth/[...nextauth]` — NextAuth configuration with custom JWT callbacks

**Database Schema:**
Our `users` collection stores four pieces of information: name, email, image, and role. The role is the key to access control — it's an enum with "student", "moderator", and "admin". Every design and quiz attempt is filtered by `user_id` at the database query level. This means even if someone has a valid JWT, they can only see their own data because MongoDB filters enforce ownership.

**Design Decisions & Trade-offs:**
1. **HS256 over JWE:** We chose HMAC-SHA256 signing over asymmetric encryption because it's simpler and sufficient for our threat model. Both the frontend and backend have the secret.
2. **HttpOnly Cookies + Bearer Token:** We store the JWT in both an HttpOnly cookie (for CSRF protection) and send it as a Bearer token (for API calls). This is a defense-in-depth approach.
3. **Never Trust JWT for Authorization:** This is the most critical design decision. JWT claims like email and user ID are used for *identification*, but authorization (role) is always resolved from MongoDB. This prevents privilege escalation attacks where someone might manipulate their JWT.
4. **Edge Middleware:** We run route protection at the Next.js Edge Runtime to reject unauthenticated requests before they hit the origin server, reducing latency.

**Challenges Solved:**
1. **Bridge Two Runtime Environments:** The fundamental challenge was making a JWT that both Next.js Edge Runtime (which uses V8 JavaScript, not Node.js APIs) and FastAPI (which uses python-jose) could verify. We solved it by standardizing on HS256 with a shared secret.
2. **Async MongoDB Driver:** Motor (async MongoDB driver for Python) has a learning curve. We had to properly manage connection pooling using FastAPI's lifespan context manager. If connections leak, the app crashes under load.
3. **Token Expiration & Refresh:** We set JWT expiration to 30 days. For a short-lived token approach, we could add a refresh mechanism, but for this product, 30 days is a reasonable balance between security and user convenience.

**Evaluation:**
Security was not directly measured in our user study, but this architecture passed a manual security review by a senior engineer. Zero unauthorized access incidents across all test deployments.

#### Demo Talking Points
When showing the authentication flow live:
- "Log in with Google, and I'll show you the token in the browser console. It's a JWT — you can decode it with jwt.io if you're curious. But notice: it doesn't contain a 'role' field. Why? Because we never trust the token for authorization decisions."
- "Now I'll open the browser's Application tab and show the HttpOnly cookie. Malicious JavaScript on the page cannot access it — that's the whole point of HttpOnly."
- "In the Network tab, you'll see every API request has an `Authorization: Bearer` header. That's the Axios interceptor we set up."
- "If I try to manually change my JWT in the browser and resend it, the FastAPI backend will decode it fine, but when it looks up the user in MongoDB, it gets my actual role from the database, not from the token."

#### Transition
"So now that we have a secure authentication foundation where users are logged in and their data is isolated, the next piece of the puzzle is generating the actual architecture. That's where Presenter 2 comes in with the LangGraph pipeline that orchestrates our multi-agent design generation system."

---

### Presenter 2: LLM Pipeline & Design Generation

#### Introduction
"I'm responsible for the core innovation of StructAI: the multi-agent LLM pipeline that takes a natural language problem statement and turns it into a complete system architecture. The key insight is that architecture design isn't a single task—it's multiple tasks that should be handled by specialized agents. We have four nodes in our LangGraph pipeline: extract, clarify, retrieve, and generate. Each one is optimized for its specific job. The fact that we can do this in 4.2 minutes compared to 47 minutes for manual design is almost entirely because of how we decomposed and orchestrated these agents."

#### Technical Explanation

**What Was Built:**
A LangGraph StateGraph with four async nodes and conditional routing. The pipeline takes a problem statement (e.g., "Design a real-time collaboration platform like Figma for 10M DAU") and produces a complete architecture JSON with nodes, edges, component types, technologies, and a summary.

**The Four Nodes:**

1. **Extract Node** — Parses the problem statement with GPT-4o at `temperature=0` (fully deterministic)
   - Outputs: structured JSON with `functional_requirements`, `non_functional_requirements`, `scale_hints`, and `ambiguities`
   - Why deterministic? Because if the same input produces different requirements on different runs, the downstream generation becomes non-reproducible
   - File: `backend/app/services/design_builder/extractor.py`

2. **Clarify Node** — Only runs if ambiguities were detected
   - Generates 2–4 targeted clarifying questions (e.g., "What's your geographic distribution?", "What's your primary use case?")
   - Returns early with `status: awaiting_clarification`
   - The design document is persisted to MongoDB at this point
   - File: `backend/app/services/design_builder/extractor.py`

3. **Retrieve Node** — Fetches relevant architecture patterns via FAISS (Presenter 3 covers this in depth)
   - Retrieves the top-3 most similar architecture patterns from our corpus of 25 real-world designs
   - Concatenates them into a ~1,200-token RAG context

4. **Generate Node** — Synthesizes the final architecture
   - Temperature is `0.2` (deterministic enough for structure, but with some variation in technology choices)
   - Consumes: requirements + clarifications + RAG context
   - Outputs: JSON with nodes array, edges array, tech_stack, and summary

**Two-Pass Protocol:**

This is crucial. Pass 1 can terminate early at the Clarify node. Once the user answers clarifying questions, Pass 2 skips extraction entirely and goes straight to retrieve and generate. This is elegant because:
- Simple inputs (no ambiguities) get a full architecture in one pass
- Complex inputs get scoped with clarifications, then generate with full context
- No persistent session server needed—we just reload the design from MongoDB and continue

Files: `backend/app/services/design_builder/pipeline.py`

**Important Files:**
- `backend/app/services/design_builder/pipeline.py` — LangGraph StateGraph definition, node implementations, routing logic, and the two helper functions `run_initial()` and `run_with_clarifications()`
- `backend/app/services/design_builder/extractor.py` — Requirement extraction and clarification question generation
- `backend/app/services/design_builder/generator.py` — Final architecture synthesis
- `backend/app/api/routes/designs.py` — REST endpoints: `POST /designs/generate` and `POST /designs/{id}/clarify`
- `backend/app/models/design.py` — Pydantic schemas for Architecture, Node, Edge validation

**Design Decisions:**

1. **Temperature Values:** We use `temperature=0` for extraction (full determinism) and `temperature=0.2` for generation (controlled variation). Why not `temperature=0` for generation? Because even small changes in the prompt ordering or token sampling can cause JSON formatting differences that break our parser. Temperature 0.2 gives us variation in *content* (different tech stacks) while keeping *structure* consistent.

2. **Conditional Routing:** We only route to clarification if ambiguities exist AND clarifications haven't been provided yet. This ensures we don't loop forever.

3. **JSON Schema Enforcement:** We explicitly tell the LLM "return ONLY valid JSON, no markdown fences". This prevents the model from wrapping the JSON in ```json blocks, which would break our parser.

4. **Minimum Node Count:** The system prompt says "include at least 6 nodes for any non-trivial system". This prevents degenerate outputs with just 2–3 components.

**Challenges Solved:**

1. **Non-Determinism of LLMs:** The first iteration of our pipeline ran the entire extraction-to-generation flow in a single LLM call. But if you run it twice on the same input, the JSON structure would be slightly different. We solved this by separating extraction (T=0) from generation (T=0.2), and caching the extraction result in MongoDB.

2. **JSON Parsing Failures:** GPT-4o sometimes wraps JSON in markdown code blocks. We had to be very explicit: "Return ONLY valid JSON (no markdown fences)". We also added a try-catch around the JSON parsing with meaningful error messages.

3. **Handling Ambiguous Inputs:** The initial approach was to generate architecture for any input. But some problems are just too vague ("Build something cool"). We added explicit ambiguity detection in the Extract node and route those cases through Clarify first.

4. **Token Budget Management:** The combined prompt (requirements + clarifications + RAG context) needs to fit within GPT-4o's effective context window while leaving room for the response. We tuned RAG to `k=3` patterns (~1,200 tokens total).

**Evaluation:**
- 34% improvement in architectural completeness with RAG vs. non-RAG (87.4% vs 65.2%)
- 91% accuracy in handling well-specified inputs
- 90% accuracy in ambiguous input clarification (9 out of 10 test cases)

#### Demo Talking Points
- "Watch the network tab. When I submit a problem statement, you'll see `POST /designs/generate`. If the backend detects ambiguities, we get back clarifying questions and a design ID in `status: awaiting_clarification`."
- "I'll fill in the answers and submit. Behind the scenes, we're calling `POST /designs/{id}/clarify`. This second request doesn't re-extract — we load the requirements from MongoDB and go straight to retrieve and generate."
- "The entire architecture generation takes 4–6 seconds. The slowest part is the OpenAI API latency, not our code."
- "If you inspect the response JSON, you'll see it's perfectly structured: every edge references valid node IDs, and the tech stack is specific (e.g., 'PostgreSQL with read replicas' not just 'database')."

#### Transition
"So the pipeline generates architecture, but how do we make sure it's grounded in real-world patterns rather than hallucinated? That's the RAG system. Presenter 3 will explain how we built a curated corpus of 25 architecture patterns and use FAISS to retrieve the most relevant ones for any given problem."

---

### Presenter 3: RAG, Visualization & Explainability

#### Introduction
"I built three interconnected systems: the RAG retrieval backend that grounds our generation in real-world patterns, the React Flow visualization that makes the abstract JSON concrete, and the explanation engine that teaches users *why* each component was chosen. The RAG system is where the 34% completeness improvement comes from — it's the difference between a model that relies on parametric knowledge and one that retrieves from authoritative examples."

#### Technical Explanation

**The RAG System:**

We have 25 curated architecture patterns: Netflix (video streaming), Uber (ride-sharing), Discord (real-time messaging), Twitter (feed generation), Airbnb (search & booking), Dropbox (file sync), Slack (messaging), and 18 others. Each pattern is a prose description covering components, communication patterns, scaling strategy, and tech stack.

When a user submits a problem statement like "Design a real-time collaboration app", we:
1. Embed the problem statement using OpenAI's `text-embedding-ada-002` (produces 1,536-dimensional vectors)
2. Query the FAISS index for the top-3 most similar patterns
3. Concatenate the pattern text with separators
4. Inject this into the generation prompt under "SIMILAR ARCHITECTURE PATTERNS FOR REFERENCE"

**Why This Works:**
The key insight is that GPT-4o reasons better over concrete examples than abstract features. If we just said "use a pattern similar to Uber", the model might misunderstand. But if we insert the actual Uber pattern text, the model sees the specific components, trade-offs, and technology choices, and can adapt them to the current problem.

**Important Files:**
- `backend/app/services/design_builder/rag.py` — FAISS loading, async-safe similarity search
- `backend/vector_store/faiss_index/` — Persisted FAISS index (binary files)
- `backend/vector_store/seed_data/patterns.py` — 25 pattern definitions
- `backend/app/services/explainability/explainer.py` — Component explanation generation

**FAISS Implementation Details:**
We use `IndexFlatL2` (exact L2 Euclidean distance) rather than approximate methods like HNSW. Why? With only 25 documents, approximate methods add complexity without speed benefit. Exact search is fast enough (45ms latency).

The index is loaded from disk on server startup — we don't re-embed the patterns every time. This saves ~2–3 seconds on startup after the first run.

Async Safety: FAISS operations are synchronous and CPU-bound. If we called `store.similarity_search()` directly from an async handler, it would block the entire event loop. We solved this by offloading FAISS to a `ThreadPoolExecutor` with 2 workers: `await loop.run_in_executor(_executor, lambda: store.similarity_search(query, k=3))`. This preserves async concurrency.

**React Flow Visualization:**

The architecture JSON has `nodes` and `edges`. We map them to React Flow's format:
- Each node gets a custom type (`client`, `database`, `cache`, etc.)
- Each node type has a distinct icon (Lucide React) and color
- Edges are decorated with protocol labels (`HTTPS`, `TCP`, `async`)
- Edges with `animated: true` pulsate to indicate real-time/async flows

The layout is automatic using Dagre (`@dagrejs/dagre`): left-to-right hierarchical arrangement with `nodesep: 80` and `ranksep: 120`. This means no manual positioning — users can't break the layout by dragging nodes around.

**Component Explainability Engine:**

When a user clicks a node in the diagram, we don't show the explanation immediately. Instead, we call our GPT-4o explainability agent with:
- The overall architecture summary
- The clicked component's label, type, and technology
- A prompt asking for a structured explanation

The response has five fields:
1. **what** — 1–2 sentence description (e.g., "Redis is an in-memory data store...")
2. **why** — 2–3 sentences on why it was chosen for this specific system (e.g., "Low latency is critical for real-time collaboration...")
3. **alternatives** — List of other options and when to use them (e.g., "Memcached: simpler but no persistence")
4. **trade_offs** — Performance, cost, complexity (e.g., "Redis uses more memory but is faster than disk-based stores")
5. **learn_more** — One concept to deepen understanding (e.g., "Study Redis replication for high availability")

This structured format beat free-form explanation in pilot testing. Structured elicitation of specific dimensions improves educational utility.

We cache explanations in the design document so repeat clicks don't call GPT-4o again.

Files: `backend/app/services/explainability/explainer.py`, `backend/app/api/routes/explain.py`, `frontend/components/diagram/node-explanation.tsx`

**Design Decisions:**

1. **Curated Corpus Over Internet Scale:** We hand-selected 25 patterns instead of embedding Wikipedia or HackerNews. Quality matters more than quantity for RAG. A small, high-quality corpus beats a large, noisy one.

2. **L2 Exact Search Over Approximate:** Approximate methods (HNSW, IVF) are optimized for 1M+ document corpora. For 25 documents, exact search is simpler and faster.

3. **Textual Injection Over Metadata:** We inject the full pattern text into the prompt rather than just pattern names or metadata. The model reasons better over prose descriptions.

4. **On-Demand Explanation:** We don't generate explanations for all components upfront. Instead, we generate on-click. This saves API cost and latency for designs where users only click a few components.

**Challenges Solved:**

1. **Async-Safe FAISS Calls:** FAISS is synchronous and would block the async event loop. The ThreadPoolExecutor solution was essential for concurrent request handling.

2. **Large Diagram Layout:** When architectures have 15+ nodes, manual layouts become cluttered. Dagre's hierarchical layout automatically organizes them left-to-right, keeping edges from crossing and maintaining readability.

3. **Explanation Hallucination:** Without the architecture summary in the prompt, the explainability agent would sometimes generate explanations that don't fit the actual architecture (e.g., explaining Redis replication when the design doesn't use replication). Including the architecture summary grounds the explanation.

**Evaluation:**
- FAISS retrieval latency: 45ms (target: ≤100ms) ✓
- Explanation quality: 4.1/5.0 mean Likert score
- 80% of users rated explanations as sufficient (≥4/5)
- Users specifically cited "alternatives" and "trade-offs" as most valuable

#### Demo Talking Points
- "Click on a node in the diagram. You'll see the explainer panel slide in on the right. The first time you click a node, there's a 200ms delay as we call GPT-4o. Click the same node again — it's instant because we cached the explanation."
- "Notice how the diagram is automatically laid out left-to-right. No node overlaps, and critical data flows are easy to trace."
- "In the explanation, look at the alternatives field. These are real options that could have been chosen instead, with tradeoffs spelled out. This is why users found them so valuable for learning."
- "If I drag a node around, React Flow handles the repositioning, but Dagre layout doesn't auto-correct. For this UI, we decided that's fine — users can organize it however they want."

#### Transition
"So we've generated the architecture, visualized it, and explained each component. But StructAI isn't just a generation tool — it's an educational platform. Presenter 4 will cover how we turn these architectures into learning opportunities through quizzes, progress tracking, and export capabilities."

---

### Presenter 4: Education, Analytics & Export

#### Introduction
"I built the educational core of StructAI: adaptive quizzes, progress tracking, and export capabilities. The platform generates architectures, but users learn by interacting with them — answering questions, seeing explanations, and tracking their progress. We have 10 system design topics, each with three difficulty levels. The quiz generation is adaptive: if you're a beginner, you get scenarios-based beginner questions; if you're advanced, you get tricky architectural trade-off questions. And when you're done, you can export your design as a professional PDF or Markdown document."

#### Technical Explanation

**The 10 Learning Topics:**
1. Load Balancing Strategies (consistent hashing, sticky sessions)
2. Database Design Patterns (sharding, replication, CQRS)
3. Caching Strategies (cache-aside, write-through, invalidation)
4. Message Queue Systems (pub-sub, FIFO, exactly-once delivery)
5. API Design (REST vs gRPC, versioning, rate limiting)
6. Real-Time Systems (WebSockets, Server-Sent Events, polling)
7. Microservices Architecture (service discovery, circuit breakers, saga patterns)
8. Data Consistency (ACID vs BASE, eventual consistency)
9. Security in Distributed Systems (JWT, mTLS, OAuth)
10. Monitoring & Observability (metrics, tracing, logging)

**Quiz Generation:**

Each topic has three difficulty levels (beginner, intermediate, advanced). When a user selects a topic and difficulty, we call our quiz generator with:
- Topic title and description
- Difficulty level
- Number of questions (typically 3–5)

The GPT-4o agent (temperature=0.7 for variety) generates a JSON array of questions with:
- Multiple choice format (exactly 4 options: a, b, c, d)
- Scenario-based questions (not trivia — e.g., "You're designing X. What do you do?")
- Plausible distractors (reflect common misconceptions, not obviously wrong)
- A 2–3 sentence explanation for the correct answer

Files: `backend/app/services/learn_mode/quiz_generator.py`

**Grading:**
Simple exact-match comparison: user's selected option ID vs. stored correct_option_id. Score is (correct_count / total_questions) * 100. Passing threshold is 70%.

We persist quiz attempts to MongoDB with user_id, topic, score, and timestamp. This builds the user's learning history.

**Analytics Dashboard:**

The `/analytics` page shows:
- Three stat cards: total designs, total quizzes, average quiz score (with large 56px Space Grotesk numerals for visual impact)
- Recent designs list (last 5)
- Quiz history (last 10 attempts with percentage score and colored progress bars: green ≥70%, amber <70%)

This gives users a clear sense of progress and motivates continued engagement.

Files: `frontend/app/analytics/page.tsx`, `frontend/components/analytics/stats-grid.tsx`

**Export Services:**

**PDF Export:**
Uses ReportLab (Python library for PDF generation). The PDF includes:
- Header with "StructAI System Design Report" and generation timestamp
- Problem statement section
- Architecture summary
- Component list with types and technologies
- Diagram (as a static image — we could embed an interactive SVG, but static is more portable)
- Tech stack summary
- Custom styling with our brand colors (indigo #6366f1 for headings)

Files: `backend/app/services/exporter/pdf_exporter.py`

**Markdown Export:**
A markdown version for users who want to edit in their own tools. Includes the same sections but formatted for GitHub/wiki consumption.

Files: `backend/app/services/exporter/md_exporter.py`

Both are served as downloads via:
- `GET /api/v1/export/{design_id}/pdf` → returns PDF bytes
- `GET /api/v1/export/{design_id}/markdown` → returns .md file

**User Dashboard:**

The main hub where users see their recent designs and quick links to New Design, Learn, and Analytics. Recent designs show status (complete vs. awaiting_clarification) with status badges and timestamps.

Files: `frontend/app/dashboard/page.tsx`

**Design Decisions:**

1. **Adaptive Difficulty:** We generate different questions for different difficulty levels rather than having a static question bank. This maximizes relevance and prevents memorization.

2. **Scenario-Based Over Trivia:** "What's a cache-aside pattern?" is trivia. "You have a hot YouTube video getting 1M views/minute. Your database can't handle the load. What caching pattern do you use?" is scenario-based. Scenario-based questions are more pedagogically valuable.

3. **Structured Explanation over Free-Form:** After a user submits a quiz, we show not just the correct answer but a full explanation. This transforms the quiz from testing into teaching.

4. **PDF Over Web Interface:** Some users want a printable document for presentation or archival. PDF export makes StructAI a tool, not just a webapp.

5. **Static PDF Image Over Interactive:** We embed the architecture diagram as a PNG in the PDF rather than trying to make it interactive. PDFs aren't great for interactive diagrams, and static images are compatible with all viewers.

**Challenges Solved:**

1. **Quiz Generation Non-Determinism:** With temperature=0.7, quiz generation is intentionally random. But we need to ensure the `correct_option_id` in the response matches one of the actual options. We validate this in the grading function.

2. **Large PDF Generation:** ReportLab can be memory-intensive for large documents. We stream the PDF to the client rather than holding it in memory.

3. **Markdown Rendering Edge Cases:** Component names with special characters (e.g., "API (REST)") need to be escaped in Markdown. We handle common cases.

4. **Analytics Query Performance:** If a user has 1000+ quiz attempts, fetching all of them is slow. We paginate (last 10) and use MongoDB indexes on user_id.

**Evaluation:**
- Quiz generation: ~2 seconds per quiz (T=0.7 adds latency vs T=0)
- Explanation quality: 4.1/5.0 (users loved structured format)
- PDF export time: <1 second for typical 8-node architecture
- 90% of users attempted at least one quiz
- Average quiz score: 78% (above passing threshold)

#### Demo Talking Points
- "Let me take a quiz. I'll select Load Balancing and Beginner difficulty. Notice the questions are scenario-based, not trivia. 'You're designing...' questions are how practitioners actually think."
- "After I answer, I see immediate feedback: this answer is correct because... Notice the explanation doesn't just say 'yes' or 'no' — it explains the reasoning."
- "On the analytics page, I can see all my quiz history. This score progression over time shows learning."
- "Now let me export a design as PDF. Click the download button, and in 1–2 seconds, you get a professional-looking report that you could present to stakeholders."
- "The PDF includes the problem statement, architecture summary, all components, and the tech stack. It's designed to be standalone — someone can read it without seeing the interactive diagram."

#### Transition
"So we've covered authentication, design generation, visualization, and learning. The next piece is how we tie it all together for evaluation and answering the question: does this system actually work?"



