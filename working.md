# StructAI — Complete Working Document

> **Document Purpose:** This document provides an exhaustive, line-by-line explanation of every component in the StructAI project. Any reader — human or AI — can fully understand the architecture, data flow, engineering decisions, and edge-case handling without needing access to the source code.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Why These Tech Stacks?](#2-why-these-tech-stacks)
3. [Full Tech Stack](#3-full-tech-stack)
4. [System Architecture](#4-system-architecture)
5. [Setup & Configuration](#5-setup--configuration)
6. [User Authentication & Session Flow](#6-user-authentication--session-flow)
7. [LangGraph Pipeline — Node-by-Node Deep Dive](#7-langgraph-pipeline--node-by-node-deep-dive)
8. [RAG System (FAISS Vector Store)](#8-rag-system-faiss-vector-store)
9. [Explainability Engine](#9-explainability-engine)
10. [Learn Mode & Quiz Engine](#10-learn-mode--quiz-engine)
11. [Export System](#11-export-system)
12. [Analytics System](#12-analytics-system)
13. [Admin System](#13-admin-system)
14. [Frontend Architecture](#14-frontend-architecture)
15. [Data Models](#15-data-models)
16. [API Endpoints — Complete Reference](#16-api-endpoints--complete-reference)
17. [Privacy & Security](#17-privacy--security)
18. [Repository Structure](#18-repository-structure)
19. [Environment Variables](#19-environment-variables)
20. [Hardware Requirements & Performance](#20-hardware-requirements--performance)
21. [Prompt Engineering](#21-prompt-engineering)
22. [All Edge Cases & Rules](#22-all-edge-cases--rules)

---

## 1. Project Overview

StructAI is a full-stack AI-powered system design platform. A user types a free-text problem statement (e.g., "Design a food delivery platform like DoorDash") and the system:

1. **Extracts** structured requirements using GPT-4o
2. **Detects** ambiguities and asks clarifying questions (optional step)
3. **Retrieves** similar real-world architecture patterns from a FAISS vector store (RAG)
4. **Generates** a complete, production-grade architecture as a JSON graph (nodes + edges)
5. **Renders** the graph interactively using React Flow with dagre auto-layout
6. **Explains** any component on click via a second GPT-4o call
7. **Teaches** system design concepts via a static topic catalog + AI-generated quizzes
8. **Exports** designs as downloadable PDF or Markdown reports
9. **Tracks** personal analytics: design count, quiz scores, history

The platform is designed for software engineers preparing for system design interviews and for students learning distributed systems concepts.

---

## 2. Why These Tech Stacks?

### Why Next.js 14 (App Router)?
- Server components reduce JavaScript bundle size; client components handle interactivity
- App Router file-system routing maps cleanly to the feature structure (builder, learn, analytics)
- Built-in image optimization for Google profile pictures via `next/image`
- `next-auth` integrates deeply with the framework for OAuth + session management
- Edge-runtime middleware enables route protection at the CDN layer without a Node.js cold start

### Why FastAPI?
- Async-native: the LangChain/LangGraph `ainvoke` calls are awaitable without any thread-pool bridging overhead
- Automatic OpenAPI docs (`/docs`) for rapid API testing during development
- Pydantic v2 models provide automatic request validation and serialization
- `lifespan` context manager handles MongoDB connection setup/teardown cleanly

### Why LangGraph?
- State machine approach makes the two-pass pipeline (extract → clarify OR extract → retrieve → generate) explicit and debuggable
- Each node is an async function with a typed `DesignState` dict, making unit testing straightforward
- Conditional edges encode the "should we clarify or generate immediately?" branching logic declaratively
- Can be extended with human-in-the-loop nodes or memory nodes without restructuring

### Why FAISS?
- Local, zero-latency vector similarity search with no external API calls after the index is built
- `save_local` / `load_local` makes the index persistent across server restarts
- `lru_cache` and a `ThreadPoolExecutor` prevent blocking the async event loop during similarity search (FAISS is CPU-bound and synchronous)
- Supports `text-embedding-ada-002` embeddings via LangChain's `OpenAIEmbeddings`

### Why MongoDB Atlas?
- Document model fits perfectly: each `design` document embeds its `architecture` JSON (nodes + edges) without requiring a relational join
- Motor (`AsyncIOMotorClient`) gives non-blocking database access compatible with FastAPI's async event loop
- Atlas free tier is sufficient for development; scales horizontally if needed
- `ObjectId` as primary key avoids sequential ID enumeration attacks

### Why NextAuth.js with custom HS256 JWT?
- NextAuth handles the entire Google OAuth dance (redirect → callback → session)
- Default NextAuth uses JWE (JSON Web Encryption), but FastAPI's `python-jose` library needs HS256 (JSON Web Signature) for straightforward decoding
- The custom `encode`/`decode` callbacks in `lib/auth.ts` rewrite the session cookie as HS256, making it readable by both the Next.js middleware and the FastAPI backend with a shared secret
- `jose` (not `jsonwebtoken`) is used because it runs in the Edge Runtime (Vercel Edge Functions, Next.js middleware)

### Why React Flow + dagre?
- React Flow is the de-facto standard for node graph rendering in React; supports custom node components, handles pan/zoom, edge routing natively
- `@dagrejs/dagre` computes a hierarchical layout (left-to-right, rank-separated) automatically from the JSON graph without requiring manual coordinate assignment
- Custom node components in `components/diagram/nodes/index.tsx` render per-type colors, icons, and connection handles

---

## 3. Full Tech Stack

| Layer | Technology | Version / Notes |
|---|---|---|
| Frontend framework | Next.js | 14, App Router |
| Frontend language | TypeScript | Strict mode |
| Styling | Tailwind CSS | 3.x, custom `navy` + `brand` color tokens |
| Auth | NextAuth.js | v4, Google provider, custom HS256 JWT |
| JWT (frontend) | `jose` | Edge Runtime compatible |
| HTTP client | Axios | With request interceptor for Bearer token |
| Diagram rendering | React Flow (`@xyflow/react`) | Custom node types |
| Graph layout | `@dagrejs/dagre` | Left-to-right hierarchical layout |
| Backend framework | FastAPI | Python 3.11+ |
| Backend language | Python | Async/await throughout |
| LLM orchestration | LangGraph + LangChain | StateGraph, async nodes |
| LLM model | OpenAI GPT-4o | `temperature=0` for extraction, `0.2` for generation, `0.3` for explanation, `0.7` for quizzes |
| Embeddings | OpenAI `text-embedding-ada-002` | Via `langchain_openai.OpenAIEmbeddings` |
| Vector store | FAISS (local) | Persisted at `vector_store/faiss_index/` |
| Database | MongoDB Atlas | Motor (async driver) |
| PDF generation | `reportlab` or `fpdf` | Via `pdf_exporter.py` |
| Settings | `pydantic-settings` | Reads from `.env` |
| Token validation | `python-jose` | HS256, shared NEXTAUTH_SECRET |
| Fonts | Space Grotesk, Inter | Google Fonts |
| Icons | Lucide React | Throughout UI |

---

## 4. System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER BROWSER                         │
│  Next.js 14 App (localhost:3000)                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ Landing  │ │Dashboard │ │ Builder  │ │  Learn   │  │
│  │ /        │ │/dashboard│ │/builder  │ │  /learn  │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│         │            │            │            │        │
│         └────────────┴────────────┴────────────┘       │
│                       Axios (lib/api.ts)                │
│              Bearer: HS256 JWT (from session)           │
└─────────────────────────────────────────────────────────┘
                           │ HTTP/REST
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  FastAPI Backend                         │
│                  (localhost:8000)                        │
│                                                         │
│  /api/v1/auth      /api/v1/designs    /api/v1/learn     │
│  /api/v1/explain   /api/v1/export     /api/v1/analytics │
│  /api/v1/admin                                          │
│                                                         │
│  Security Layer: decode_token() → get_current_user()    │
│  (python-jose HS256, shared NEXTAUTH_SECRET)            │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │           LangGraph Pipeline                    │   │
│  │  extract → [clarify?] → retrieve → generate    │   │
│  └─────────────────────────────────────────────────┘   │
│                      │                                  │
│          ┌───────────┴────────────┐                     │
│          │                        │                     │
│     GPT-4o API              FAISS Index                 │
│     (OpenAI)          (vector_store/faiss_index/)       │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │           MongoDB Atlas                         │   │
│  │  collections: users, designs, quiz_attempts     │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Request lifecycle (design generation):
1. User types problem statement → clicks Generate
2. Frontend calls `POST /api/v1/designs/generate` with `Authorization: Bearer <hs256_jwt>`
3. FastAPI middleware: `get_current_user()` decodes the HS256 JWT using `NEXTAUTH_SECRET`, extracts `email`, fetches user from MongoDB
4. `run_initial(problem_statement)` invokes the LangGraph pipeline
5. Pipeline: `node_extract` → conditional → `node_clarify` OR `node_retrieve` → `node_generate`
6. If clarification needed: API returns `{status: "awaiting_clarification", clarifying_questions: [...]}`; frontend shows the Q&A form
7. User submits answers → `POST /api/v1/designs/{id}/clarify` → `run_with_clarifications()` skips extract, goes straight to retrieve → generate
8. Architecture JSON stored in MongoDB; `design_count` incremented on the user document
9. Frontend receives architecture → navigates to `/builder/{design_id}` → React Flow renders the graph

---

## 5. Setup & Configuration

### Frontend setup (`frontend/`)
```bash
npm install
# Required env: NEXTAUTH_SECRET, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
# Optional:     NEXT_PUBLIC_API_URL (defaults to http://localhost:8000)
npm run dev     # localhost:3000
```

### Backend setup (`backend/`)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Required env in .env:
#   MONGODB_URI, OPENAI_API_KEY, NEXTAUTH_SECRET, ENVIRONMENT, BACKEND_CORS_ORIGINS
uvicorn app.main:app --reload --port 8000
```

### FAISS index initialization
- On first startup, if `vector_store/faiss_index/` does not exist, `rag.py` calls `_load_or_create_store()`
- This reads `ARCHITECTURE_PATTERNS` from `vector_store/seed_data/patterns.py` (25+ real-world patterns)
- Calls `OpenAIEmbeddings` to embed each pattern text (one API call per pattern, ~1–2 seconds total)
- Saves the index to disk with `FAISS.save_local()`
- Subsequent server restarts load the pre-built index from disk (no embedding API calls)

### Critical shared secret
- `NEXTAUTH_SECRET` must be identical in both `.env.local` (frontend) and `.env` (backend)
- Frontend uses it to sign/verify JWT cookies via `jose`
- Backend uses it to verify the same tokens via `python-jose`
- A mismatch causes every API request to return `401 Unauthorized`

---

## 6. User Authentication & Session Flow

### Step 1 — Google OAuth Initiation
- User clicks "Continue with Google" on landing page or login page
- `signIn("google", { callbackUrl: "/dashboard" })` is called
- NextAuth redirects to `https://accounts.google.com/o/oauth2/auth` with the app's `GOOGLE_CLIENT_ID`

### Step 2 — Google callback
- Google redirects back to `http://localhost:3000/api/auth/callback/google` with a code
- NextAuth exchanges the code for a Google access token and fetches the user's profile (name, email, image)

### Step 3 — Custom JWT encoding (`lib/auth.ts`)
NextAuth normally creates a JWE-encrypted cookie. StructAI overrides both `encode` and `decode`:

```typescript
// encode: called when setting the session cookie
encode: async ({ token }) => {
  const { exp, iat, jti, ...rest } = token as Record<string, unknown>;
  return new SignJWT(rest)           // rest = { email, name, picture, sub }
    .setProtectedHeader({ alg: "HS256" })
    .setExpirationTime("30d")
    .sign(secret());                 // secret = TextEncoder(NEXTAUTH_SECRET)
}

// decode: called when reading the session cookie
decode: async ({ token }) => {
  if (!token) return null;
  try {
    const { payload } = await jwtVerify(token, secret());
    return payload as Record<string, unknown>;
  } catch { return null; }
}
```

**Why strip `exp`, `iat`, `jti`?** These are standard JWT claims. The `jose` `SignJWT` builder sets its own `exp` via `setExpirationTime("30d")`. Passing them in the payload would create duplicates in the JWT.

### Step 4 — Session callback (`lib/auth.ts`)
After the JWT is created, the `session` callback fires to build the client-visible session object:

```typescript
async session({ session, token }) {
  // Copy profile fields into session.user
  session.user.email = token.email as string;
  session.user.name = token.name as string;
  session.user.image = token.picture as string;

  // Re-encode the token as a JWT string for FastAPI
  const { exp, iat, jti, ...rest } = token as Record<string, unknown>;
  const accessToken = await new SignJWT(rest)
    .setProtectedHeader({ alg: "HS256" })
    .setExpirationTime("30d")
    .sign(secret());

  (session as unknown as Record<string, unknown>).accessToken = accessToken;
  return session;
}
```

**Why re-encode?** The `token` object passed into `session()` is the decoded payload (a plain JS object), not the JWT string. The frontend needs the raw JWT string to send as a Bearer token to FastAPI. Re-encoding produces that string.

### Step 5 — User upsert to MongoDB
On first page load after login, `dashboard/page.tsx` calls `upsertUser()`:
```typescript
upsertUser({ name, email, image })  // POST /api/v1/auth/upsert-user
```
The backend's `upsert_user` route checks if the email exists in MongoDB:
- **Exists:** returns existing user document (idempotent)
- **New user:** creates document with `role: "student"`, `design_count: 0`, `quiz_count: 0`

**Note:** `upsert-user` does NOT require a Bearer token — it is the one unprotected write endpoint because at the time of calling, the user is authenticated via Google but hasn't been synced to the backend yet.

### Step 6 — Route protection via Next.js middleware (`middleware.ts`)
```typescript
export async function middleware(req: NextRequest) {
  const token = await getToken({
    req,
    secret: process.env.NEXTAUTH_SECRET!,
    decode: async ({ token: raw }) => {
      if (!raw) return null;
      try {
        const { payload } = await jwtVerify(raw, secret());
        return payload as Record<string, unknown>;
      } catch { return null; }
    },
  });
  if (!token) return NextResponse.redirect(new URL("/login", req.url));
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/builder/:path*", "/learn/:path*", "/analytics/:path*", "/admin/:path*"],
};
```

- Runs in the **Edge Runtime** (not Node.js) — this is why `jsonwebtoken` cannot be used (it's Node-only)
- `getToken()` reads the `next-auth.session-token` cookie and uses the custom `decode` function to verify it
- If verification fails or the cookie is absent, the user is redirected to `/login`
- The matcher excludes `/`, `/login`, and `/api/auth/*` (these are public)

### Step 7 — API requests from frontend (`lib/api.ts`)
```typescript
api.interceptors.request.use(async (config) => {
  const session = await getSession();
  const token = (session as Record<string, unknown> | null)?.accessToken;
  if (token && typeof token === "string") {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```
- `getSession()` fetches the current session from the NextAuth session endpoint
- `session.accessToken` is the HS256 JWT string embedded by the `session` callback above
- Every API call to FastAPI carries this Bearer token

### Step 8 — FastAPI token verification (`core/security.py`)
```python
def decode_token(token: str) -> dict:
    payload = jwt.decode(token, settings.NEXTAUTH_SECRET, algorithms=["HS256"])
    return payload

async def get_current_user(credentials, db) -> dict:
    payload = decode_token(credentials.credentials)
    email = payload.get("email")
    user = await db.users.find_one({"email": email})
    if not user: raise HTTPException(status_code=404)
    return user
```
- Uses `python-jose` to decode the HS256 JWT with the shared `NEXTAUTH_SECRET`
- Extracts `email` from the payload (set during Google OAuth)
- Fetches the full user document from MongoDB to attach to the request

---

## 7. LangGraph Pipeline — Node-by-Node Deep Dive

### State definition (`pipeline.py`)
```python
class DesignState(TypedDict):
    problem_statement: str      # original user input
    requirements: dict          # output of extract node
    clarifying_questions: list  # output of clarify node
    clarifications: Optional[dict]  # user answers (second pass only)
    rag_context: str            # concatenated pattern texts from FAISS
    architecture: Optional[dict]    # final JSON graph
    error: Optional[str]        # propagated exception message
```

All nodes receive the full state and return a partial dict of updated keys (LangGraph merges them).

---

### Node 1: `node_extract` — Requirements Extraction

**File:** `services/design_builder/extractor.py`  
**LLM config:** `temperature=0` (deterministic, structured output required)

**What it does:**
Sends the raw problem statement to GPT-4o with a system prompt instructing it to return a structured JSON object containing:
- `functional_requirements`: list of concrete features (e.g., "Users can upload images up to 10MB")
- `non_functional_requirements`: list of quality attributes (e.g., "99.99% uptime", "< 200ms P95 latency")
- `scale_hints`: object with estimates for users, reads/sec, writes/sec, data size
- `ambiguities`: list of unclear aspects that would benefit from clarification

**System prompt (verbatim):**
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

**Error handling:** If GPT-4o returns malformed JSON or the call fails, the exception is caught and `{"error": str(e)}` is set in the state. The `designs/generate` route checks for this and returns HTTP 500.

---

### Conditional edge: `should_clarify`

```python
def should_clarify(state: DesignState) -> str:
    has_ambiguities = bool(state["requirements"].get("ambiguities"))
    already_clarified = bool(state.get("clarifications"))
    return "clarify" if has_ambiguities and not already_clarified else "retrieve"
```

**Two cases:**
- `ambiguities` list is non-empty AND `clarifications` is `None` → route to `clarify` node
- Otherwise (no ambiguities OR second pass with answers) → route directly to `retrieve` node

**Why skip clarification on second pass?** When `run_with_clarifications()` is called, it doesn't go through the graph at all — it calls `retrieve_similar_patterns` and `generate_architecture` directly. The conditional edge only matters during `run_initial()`.

---

### Node 2: `node_clarify` — Question Generation

**File:** `services/design_builder/extractor.py`  
**LLM config:** `temperature=0` (consistent question generation)

**What it does:**
Takes the extracted `requirements` dict (including the `ambiguities` list) and asks GPT-4o to generate 2–4 concise clarifying questions.

**System prompt (verbatim):**
```
You are a senior system design architect conducting a scoping session.
Given the extracted requirements and ambiguities, generate 2–4 concise clarifying questions
that would meaningfully improve the architecture design.

Return ONLY valid JSON (no markdown fences):
{"questions": ["<question>", ...]}
```

**After this node:** The LangGraph graph reaches `END`. The API route returns `{status: "awaiting_clarification", clarifying_questions: [...]}`. The design document is persisted in MongoDB with `status: "awaiting_clarification"` and the `clarifying_questions` array stored for the second pass.

**Frontend behavior:** Renders a Q&A form where each question gets a textarea. The user can leave answers blank (defaults to "No preference"). On submit, calls `POST /api/v1/designs/{id}/clarify`.

---

### Node 3: `node_retrieve` — RAG Pattern Retrieval

**File:** `services/design_builder/rag.py`

**What it does:**
- Calls `retrieve_similar_patterns(problem_statement, k=3)`
- Loads (or lazily initializes) the FAISS vector store
- Embeds the problem statement using `text-embedding-ada-002`
- Performs cosine similarity search against 25+ pre-embedded architecture patterns
- Returns the text of the top-3 most similar patterns, joined by `---` separators
- This becomes `rag_context` in the state

**Why k=3?** Balances context richness with token budget. Three patterns at ~300 words each ≈ 900 words ≈ ~1200 tokens — well within GPT-4o's context window, leaves plenty of room for the requirements JSON and system prompt.

---

### Node 4: `node_generate` — Architecture Generation

**File:** `services/design_builder/generator.py`  
**LLM config:** `temperature=0.2` (slight creativity allowed for tech stack diversity)

**What it does:**
Sends a combined prompt to GPT-4o containing:
1. The structured `requirements` JSON
2. The `clarifications` dict (if second pass, otherwise empty `{}`)
3. The `rag_context` (top-3 similar patterns from FAISS)

**System prompt (verbatim):**
```
You are a world-class system design architect.
Design a complete, production-grade system architecture based on the requirements and similar patterns below.

Return ONLY valid JSON (no markdown fences) matching this exact schema:
{
  "nodes": [
    {
      "id": "<kebab-case unique id>",
      "type": "<one of: client|api_gateway|load_balancer|web_server|database|nosql_database|cache|message_queue|cdn|object_storage|auth_service|monitoring|ml_service>",
      "label": "<display name>",
      "description": "<one-line description>",
      "tech": "<recommended technology, e.g. Redis, PostgreSQL, Nginx>"
    }
  ],
  "edges": [
    {
      "id": "<unique id>",
      "source": "<node id>",
      "target": "<node id>",
      "label": "<protocol or relationship, e.g. HTTPS, TCP, async>",
      "animated": <true for real-time or async flows, false otherwise>
    }
  ],
  "tech_stack": ["<technology>", ...],
  "summary": "<2–3 sentence architecture overview>"
}

Rules:
- Include all components needed for a production system (auth, monitoring, caching, etc.)
- Every edge must reference valid node ids
- Prefer battle-tested technologies unless the requirements suggest otherwise
- Include at least 6 nodes for any non-trivial system
```

**Valid node types (13 total):**
`client`, `api_gateway`, `load_balancer`, `web_server`, `database`, `nosql_database`, `cache`, `message_queue`, `cdn`, `object_storage`, `auth_service`, `monitoring`, `ml_service`

Each type maps to a unique icon and color in the frontend's `NODE_CONFIG` object.

**Edge `animated` field:** Set to `true` by GPT-4o for async/real-time flows (e.g., Kafka message passing, WebSocket connections). React Flow renders animated dashed edges for these.

---

### Two-pass flow summary

```
First call (run_initial):
  problem_statement → extract → [has ambiguities?]
                                   YES → clarify → END (return questions)
                                   NO  → retrieve → generate → END (return arch)

Second call (run_with_clarifications):
  [skips LangGraph graph entirely]
  retrieve_similar_patterns(problem_statement)
  generate_architecture(requirements, clarifications, rag_context)
  → returns complete architecture
```

---

## 8. RAG System (FAISS Vector Store)

### Seed data (`vector_store/seed_data/patterns.py`)
- 25+ real-world architecture patterns pre-written as descriptive text blocks
- Examples: Netflix video streaming, Uber ride-sharing, Discord messaging, Twitter timeline, Airbnb search, Dropbox file storage, etc.
- Each pattern has a `name`, `tags` (list of relevant concepts), and `text` (full description)

### Index lifecycle
```python
# Lazy initialization on first request
async def get_vector_store() -> FAISS:
    global _vector_store
    if _vector_store is None:
        embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        loop = asyncio.get_event_loop()
        _vector_store = await loop.run_in_executor(
            _executor,           # ThreadPoolExecutor(max_workers=2)
            _load_or_create_store,
            embeddings
        )
    return _vector_store
```

**Why `run_in_executor`?** FAISS operations (`save_local`, `load_local`, `similarity_search`) are synchronous and CPU-bound. Running them on the async event loop would block all other requests. The ThreadPoolExecutor offloads this work to a worker thread, keeping the event loop free.

**Why `lru_cache` pattern (global `_vector_store`)?** The FAISS index is loaded once per process lifetime. Loading it on every request would be prohibitively slow (~2–3 seconds per request).

### Retrieval
```python
async def retrieve_similar_patterns(query: str, k: int = 3) -> str:
    store = await get_vector_store()
    loop = asyncio.get_event_loop()
    docs = await loop.run_in_executor(_executor, lambda: store.similarity_search(query, k=k))
    return "\n\n---\n\n".join(d.page_content for d in docs)
```

- `similarity_search` embeds the query and finds the k nearest documents by cosine similarity
- Returns page content (the pattern text) concatenated with `---` separators
- This string is injected verbatim into the generation prompt as `SIMILAR ARCHITECTURE PATTERNS FOR REFERENCE:`

---

## 9. Explainability Engine

**File:** `services/explainability/explainer.py`  
**Route:** `POST /api/v1/explain/component`  
**LLM config:** `temperature=0.3` (slightly creative for educational prose)

### Trigger
User clicks any node in the React Flow diagram. The `ExplainerPanel` component calls `explainComponent(designId, componentId)`.

### What it does
Sends a prompt to GPT-4o containing:
- The architecture's `summary` (2–3 sentences giving context)
- The specific node's: `id`, `label`, `type`, `tech`

**System prompt (verbatim):**
```
You are a senior system design mentor explaining architecture decisions to a student or developer.
Given an architecture component, explain it clearly and concisely.

Return ONLY valid JSON (no markdown fences):
{
  "what": "<1–2 sentence description of what this component is>",
  "why": "<2–3 sentences on why it was chosen for this specific system>",
  "alternatives": ["<alternative tech or pattern>", "<another>"],
  "trade_offs": "<2–3 sentences on key trade-offs: performance, cost, complexity>",
  "learn_more": "<one key concept the user should study to go deeper>"
}
```

### Caching behavior
Explanations are stored in the design's MongoDB document under `explanations[component_id]`. On subsequent clicks of the same component, the stored explanation is returned immediately without a new GPT-4o call.

The `ExplainerPanel` (frontend) receives and displays all five fields with different typography weights — `what` as a lead sentence, `why` as body text, `alternatives` as pills, `trade_offs` as italicized caution text, `learn_more` as a linked call-to-action.

---

## 10. Learn Mode & Quiz Engine

### Topic catalog (`services/learn_mode/topics.py`)
10 static topics, hardcoded as Python dicts:

| ID | Title | Difficulty | Est. Minutes |
|---|---|---|---|
| `load-balancing` | Load Balancing | beginner | 10 |
| `caching` | Caching Strategies | beginner | 12 |
| `databases-sql-vs-nosql` | SQL vs NoSQL | beginner | 15 |
| `message-queues` | Message Queues & Event Streaming | intermediate | 15 |
| `cap-theorem` | CAP Theorem | intermediate | 10 |
| `api-design` | API Design & Rate Limiting | intermediate | 12 |
| `database-sharding` | Database Sharding & Replication | advanced | 20 |
| `microservices` | Microservices Architecture | advanced | 20 |
| `cdn-object-storage` | CDN & Object Storage | beginner | 10 |
| `distributed-consensus` | Distributed Consensus | advanced | 25 |

`GET /api/v1/learn/topics` returns all 10.  
`GET /api/v1/learn/topics/{topic_id}` returns a single topic or 404.

### Quiz generation (`services/learn_mode/quiz_generator.py`)
**LLM config:** `temperature=0.7` (high variation so each quiz attempt feels different)

**Request:** `POST /api/v1/learn/quiz/generate`
```json
{ "topic": "Load Balancing", "difficulty": "beginner", "num_questions": 5 }
```

**System prompt enforces:**
- Multiple choice with exactly 4 options (a, b, c, d)
- Scenario-based questions, not trivia
- Plausible distractors (common misconceptions)
- 2–3 sentence explanation per correct answer

**Quiz cache:** Questions are stored in a Python process-level dict `_quiz_cache: dict[str, list]` keyed by `quiz_id` (UUID). This is intentional for local development. **In production this should be Redis** (noted in code comment). The cache ensures that when the user submits answers, the backend can grade them against the original questions without re-generating.

### Quiz grading (`grade_quiz`)
```python
def grade_quiz(questions: list[dict], answers: list[dict]) -> dict:
    answer_map = {a["question_id"]: a["selected_option_id"] for a in answers}
    correct_count = sum(1 for q in questions if answer_map.get(q["id"]) == q["correct_option_id"])
    score = round((correct_count / len(questions)) * 100, 1)
    return {
        "score": score,
        "results": [...],  # per-question: correct bool + explanation
        "passed": score >= 70,
    }
```

**Passing threshold:** 70%. This is hardcoded. A score ≥ 70 is shown in green (`#059669`), below 70 in amber (`#D97706`).

### Post-submission persistence
After grading:
1. A `quiz_attempt` document is inserted into MongoDB with: `user_id`, `quiz_id`, `topic`, `score`, `passed`, `completed_at`
2. `users.quiz_count` is incremented by 1
3. The quiz is removed from `_quiz_cache` to free memory

### Frontend quiz engine (`components/learn/QuizEngine.tsx`)
- Shows one question at a time or all questions (depends on implementation)
- Each option is a radio-style button; selection is highlighted
- On submit: calls `submitQuiz(quizId, topic, answers)` → displays results with per-question explanations

---

## 11. Export System

**Routes:** `GET /api/v1/export/{design_id}/pdf` and `GET /api/v1/export/{design_id}/markdown`

Both routes:
1. Fetch the design document from MongoDB, verifying `user_id` ownership
2. Check that `architecture` is not null (design must be `status: "complete"`)
3. Pass `problem_statement`, `architecture` dict, and `explanations` dict to the generator
4. Return a binary response with appropriate `Content-Disposition: attachment` headers

### Markdown export (`services/exporter/md_exporter.py`)
Produces a structured Markdown document:
```markdown
# System Design: {problem_statement}
*Generated by StructAI on {datetime}*
---
## Overview
{summary}

## Tech Stack
- Redis
- PostgreSQL
- ...

## Architecture Components
### {node_label} (`{node_type}`)
**Technology:** {tech}
{description}
**Why chosen:** {explanation.why}        ← only if component was clicked/explained
**Alternatives:** {alt1}, {alt2}
**Trade-offs:** {trade_offs}

## Data Flow
- **{source_label}** → **{target_label}** (HTTPS)
- ...
```

### PDF export (`services/exporter/pdf_exporter.py`)
Generates a styled PDF using a Python PDF library. Mirrors the Markdown structure but with formatted sections, font sizes, and page layout.

### Frontend download trigger (`lib/api.ts`)
```typescript
export const downloadPdf = async (designId: string) => {
  const res = await api.get(`/export/${designId}/pdf`, { responseType: "blob" });
  const url = URL.createObjectURL(res.data);
  const a = document.createElement("a");
  a.href = url; a.download = `structai-${designId.slice(0, 8)}.pdf`;
  a.click();
  URL.revokeObjectURL(url);
};
```
Creates a temporary object URL from the blob, triggers a programmatic click on a hidden anchor, then revokes the URL immediately to free memory.

---

## 12. Analytics System

### User stats (`GET /api/v1/analytics/me`)
**File:** `services/analytics/tracker.py → get_user_stats(user_id)`

Runs 3 MongoDB queries:
1. `count_documents({user_id})` on `designs` collection → `total_designs`
2. `count_documents({user_id})` on `quiz_attempts` collection → `total_quizzes`
3. `find` on `designs`, sorted by `created_at` desc, limit 5 → `recent_designs`
4. `find` on `quiz_attempts`, sorted by `completed_at` desc, limit 10 → `quiz_history`

Computes `avg_quiz_score` in Python: `sum(scores) / len(scores)`, rounded to 1 decimal. Returns 0 if no quizzes taken.

**Edge case:** If `quiz_history` is empty, `avg_score = 0` (not `None` or a division error).

### Admin stats (`GET /api/v1/analytics/admin`)
**Access:** Requires `role: "admin"` in the user's MongoDB document.

Runs:
- `count_documents({})` on all three collections
- `distinct("user_id", {created_at: {$gte: week_ago}})` → unique users active in last 7 days
- MongoDB aggregation pipeline: group by date string, count designs per day for last 7 days

### Frontend Analytics page
Displays:
- 3 stat cards with huge Space Grotesk 56px numbers (Bungee-style)
- Recent designs list (last 5, from `recent_designs`)
- Quiz history with score bar + percentage (last 10)

Pass/fail threshold for color: `score >= 70` → green `#059669`, else amber `#D97706`

---

## 13. Admin System

**Route prefix:** `/api/v1/admin`  
**Access:** All endpoints require `get_admin_user` dependency (checks `role === "admin"` in MongoDB)

### Endpoints
- `GET /admin/health` — returns service status, DB connection state, index info
- `GET /admin/users` — paginated list of all users with design/quiz counts
- `PATCH /admin/users/{user_id}/role?role=admin` — promote a user to admin
- `POST /admin/rebuild-index` — drops and rebuilds the FAISS index from seed data (useful when patterns are updated)

### Role promotion
The only way to create an admin is via this endpoint (called with an existing admin account) or by direct MongoDB modification. There is no self-service admin signup.

---

## 14. Frontend Architecture

### Routing structure
```
app/
├── page.tsx                    → / (landing, public)
├── (auth)/login/page.tsx       → /login (public)
├── dashboard/
│   ├── layout.tsx              → wraps with NavBar
│   └── page.tsx                → dashboard page
├── builder/
│   ├── layout.tsx              → wraps with NavBar
│   ├── page.tsx                → problem statement input
│   └── [designId]/page.tsx     → React Flow diagram view
├── learn/
│   ├── layout.tsx
│   ├── page.tsx                → topic grid
│   └── [topic]/page.tsx        → topic detail + quiz
└── analytics/
    ├── layout.tsx
    └── page.tsx                → stats + history
```

### Middleware (`middleware.ts`)
Protects all routes matching `/dashboard/:path*`, `/builder/:path*`, `/learn/:path*`, `/analytics/:path*`, `/admin/:path*`. Runs at the Edge Runtime.

### Providers (`app/providers.tsx`)
Wraps the entire app with `SessionProvider` from `next-auth/react`. This enables `useSession()` in any client component.

### NavBar (`components/ui/NavBar.tsx`)
- Fixed sidebar `w-60` on the left
- Background: `#0A0E2E` (dark navy)
- Active route detection: exact match for `/dashboard`, `startsWith` for all others
- Active state: indigo left border indicator + `rgba(99,102,241,0.18)` background + lighter text
- User section at bottom: avatar (from Google), name, email, sign-out button

### Diagram view (`app/builder/[designId]/page.tsx`)
On mount: fetches the design from `GET /api/v1/designs/{id}`. Passes `architecture` to `ArchitectureCanvas`.

**`ArchitectureCanvas` (`components/diagram/ArchitectureCanvas.tsx`):**
1. Receives `architecture` (nodes + edges) as props
2. Maps API nodes → React Flow `Node` objects with `position: {x: 0, y: 0}` (dagre will set real positions)
3. Maps API edges → React Flow `Edge` objects with arrow markers and label styles
4. Calls `applyDagreLayout(nodes, edges)` which runs dagre's `LR` (left-to-right) layout algorithm
5. Calls `setNodes(layouted)` and `setEdges(rawEdges)` to trigger render
6. On node click → calls `onNodeClick(node)` → parent renders `ExplainerPanel`

**`applyDagreLayout`:** Sets a shared global `DAGRE_GRAPH` object (note: this is a module-level singleton, which works fine because the graph is reset on each layout call via `setGraph()`). Node dimensions: `width: 180, height: 80`. Spacing: `nodesep: 80, ranksep: 120`.

**Custom node rendering (`components/diagram/nodes/index.tsx`):**
- `NODE_CONFIG` maps each of the 13 node types to a `{ color, bg, border, dot, Icon }` config
- `Gateway = Shield` (lucide-react `Shield` icon used for API Gateway)
- `Scale` is a custom SVG component (balance scale, since lucide-react's `Scale` has a conflicting prop type for `size` as `string | number` vs the expected `number`)
- Each node renders: a colored icon background circle, the icon, node label, tech name, and connection handles (source/target dots)
- Selected node gets a brighter ring/highlight

### Design system (globals.css + tailwind.config.ts)

**Body:** `background: #F8F9FB` (light gray), `color: #0A0E2E` (dark navy text)

**Card:** White `#FFFFFF`, `1px solid #E8E9F0` border, hover shadow

**Button primary (`.btn-primary`):** `background: #4F46E5` (indigo), white text, hover darkens to `#4338CA`

**Button ghost (`.btn-ghost`):** `background: #F3F4F6`, `color: #4B5563`, hover to `#E9EAEF`

**Input (`.input`):** White background, `1px solid #E5E7EB`, focus ring `rgba(99,102,241,0.1)`

**Section labels (`.section-label`):** `10px`, `700 weight`, `0.12em letter-spacing`, uppercase, `color: #9CA3AF`

**`.gradient-text`:** `background: linear-gradient(135deg, #6366F1, #8B5CF6, #A78BFA)` with `animation: gradientShift 4s ease infinite`

**Tailwind custom tokens:**
```
brand: { 50, 100, 300, 400, 500, 600, 700, 900 }  ← indigo/violet scale
navy:  { 950: #04050F, 900: #06071A, 800: #0C0E24, 700: #12143A }
fonts: display (Space Grotesk), sans (Inter), mono (JetBrains Mono / Fira Code)
animations: fade-up, fade-in, slide-in, gradient
```

### Landing page (`app/page.tsx`)
- Full-screen `linear-gradient(160deg, #EEF2FF, #EDE8FF, #F3EEFF, #EDF2FF)` background
- Redirects to `/dashboard` if session exists (`useEffect` + `useSession`)
- Hero heading: "DESIGN" (filled `#0A0E2E`) + "SYSTEMS" (stroke only, `WebkitTextStroke: "2.5px #7c3aed"`)
- Font size: `clamp(68px, 10.5vw, 148px)` — scales responsively
- 4-item numbered feature list (01–04) instead of heavy cards
- CTA: dark navy button with Google icon SVG

---

## 15. Data Models

### MongoDB Collections

#### `users`
```json
{
  "_id": ObjectId,
  "name": "Akshat More",
  "email": "technospy674589@gmail.com",
  "image": "https://lh3.googleusercontent.com/...",
  "role": "student",        // or "admin"
  "created_at": ISODate,
  "design_count": 12,       // incremented on design creation, decremented on delete
  "quiz_count": 5           // incremented on quiz submission
}
```

#### `designs`
```json
{
  "_id": ObjectId,
  "user_id": "string(ObjectId)",    // owner; used for all authorization checks
  "problem_statement": "Design a food delivery app like DoorDash",
  "requirements": {
    "functional_requirements": ["..."],
    "non_functional_requirements": ["..."],
    "scale_hints": { "users": "...", ... },
    "ambiguities": ["..."]
  },
  "clarifying_questions": ["What is the expected delivery radius?"],  // only if step 1 returned questions
  "clarifications": { "What is...": "City-wide, 20km radius" },      // only after step 2
  "architecture": {
    "nodes": [{ "id": "client", "type": "client", "label": "Mobile App", "description": "...", "tech": "React Native" }],
    "edges": [{ "id": "e1", "source": "client", "target": "api-gateway", "label": "HTTPS", "animated": false }],
    "tech_stack": ["React Native", "FastAPI", "PostgreSQL", "Redis"],
    "summary": "A microservices-based food delivery platform..."
  },
  "explanations": {
    "api-gateway": { "what": "...", "why": "...", "alternatives": ["..."], "trade_offs": "...", "learn_more": "..." }
  },
  "status": "complete",    // "pending" | "awaiting_clarification" | "complete"
  "created_at": ISODate,
  "updated_at": ISODate
}
```

#### `quiz_attempts`
```json
{
  "_id": ObjectId,
  "user_id": "string(ObjectId)",
  "quiz_id": "uuid-string",
  "topic": "Load Balancing",
  "score": 80.0,
  "passed": true,
  "completed_at": ISODate
}
```

### Frontend TypeScript types (`types/index.ts`)
All interfaces match the backend JSON exactly:
- `AppUser`, `ArchNode`, `ArchEdge`, `Architecture`, `Design`, `DesignListItem`, `GenerateResponse`
- `ComponentExplanation`, `Topic`, `QuizQuestion`, `QuizOption`, `QuizResult`, `QuizSubmitResponse`
- `UserStats`, `AdminStats`

---

## 16. API Endpoints — Complete Reference

All endpoints are prefixed with `/api/v1`. Auth endpoints marked with 🔓 are unauthenticated; all others require `Authorization: Bearer <hs256_jwt>`.

### Auth
| Method | Path | Description |
|---|---|---|
| POST 🔓 | `/auth/upsert-user` | Sync Google user to MongoDB on first login |
| GET | `/auth/me` | Return current user profile |

### Designs
| Method | Path | Description |
|---|---|---|
| POST | `/designs/generate` | Submit problem statement; starts LangGraph pipeline |
| POST | `/designs/{id}/clarify` | Submit answers to clarifying questions |
| GET | `/designs/{id}` | Fetch a single design (full document) |
| GET | `/designs/` | List user's designs (last 20, problem + status + created_at only) |
| DELETE | `/designs/{id}` | Delete a design; decrements `design_count` |

### Explainability
| Method | Path | Description |
|---|---|---|
| POST | `/explain/component` | Generate explanation for a clicked node |

### Learn Mode
| Method | Path | Description |
|---|---|---|
| GET 🔓 | `/learn/topics` | List all 10 topics |
| GET 🔓 | `/learn/topics/{topic_id}` | Get single topic detail |
| POST | `/learn/quiz/generate` | Generate a quiz for a topic |
| POST | `/learn/quiz/submit` | Grade submitted answers; persist attempt |

### Export
| Method | Path | Description |
|---|---|---|
| GET | `/export/{design_id}/pdf` | Download design as PDF |
| GET | `/export/{design_id}/markdown` | Download design as Markdown |

### Analytics
| Method | Path | Description |
|---|---|---|
| GET | `/analytics/me` | Current user's stats |
| GET | `/analytics/admin` | Platform-wide stats (admin only) |

### Admin
| Method | Path | Description |
|---|---|---|
| GET | `/admin/health` | Service health check |
| GET | `/admin/users` | List all users |
| PATCH | `/admin/users/{id}/role` | Change user role |
| POST | `/admin/rebuild-index` | Rebuild FAISS vector store |

### Health (public)
| Method | Path | Description |
|---|---|---|
| GET 🔓 | `/health` | `{"status": "ok", "service": "structai-api"}` |

---

## 17. Privacy & Security

### JWT security
- `NEXTAUTH_SECRET` is the single shared secret between frontend and backend — it is the linchpin of the entire auth system. Must be a long random string (32+ characters)
- Tokens expire in 30 days (`setExpirationTime("30d")`)
- Tokens are stored in HttpOnly cookies by NextAuth — JavaScript on the page cannot read them directly
- The `accessToken` on `session` is a re-encoded JWT string (not a cookie) — it is readable by JavaScript but is signed and cannot be tampered with without knowing the secret

### Authorization model
- Every route that touches user data uses `get_current_user()` which verifies the token AND fetches the user from MongoDB
- Design ownership is enforced by including `user_id: str(current_user["_id"])` in all MongoDB queries — a user cannot access another user's designs even if they know the `ObjectId`
- Admin routes use `get_admin_user()` which calls `get_current_user()` first, then checks `role === "admin"` in the MongoDB document — the role cannot be elevated via a JWT claim (it is always read from the database)

### CORS configuration
- `BACKEND_CORS_ORIGINS` env var (JSON string) controls which origins can call the API
- Default: `["http://localhost:3000"]`
- `allow_credentials: True` is required for the browser to send cookies/headers on cross-origin requests

### Input validation
- All request bodies are validated by Pydantic models before reaching route handlers
- MongoDB `ObjectId` conversion (`ObjectId(design_id)`) raises a `bson.errors.InvalidId` exception for malformed IDs — this should ideally be caught and returned as 400, not 500 (current edge case)

### No sensitive data in JWT payload
The JWT payload contains only: `email`, `name`, `picture`, `sub` (Google user ID). No role claims are in the JWT — roles are always read from MongoDB to prevent privilege escalation via token manipulation.

---

## 18. Repository Structure

```
StructAI/
├── frontend/
│   ├── app/
│   │   ├── (auth)/login/page.tsx           Public login page
│   │   ├── admin/layout.tsx + page.tsx      Admin dashboard
│   │   ├── analytics/layout.tsx + page.tsx  Analytics
│   │   ├── builder/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx                     Problem statement input
│   │   │   └── [designId]/page.tsx          React Flow diagram
│   │   ├── dashboard/layout.tsx + page.tsx  Main dashboard
│   │   ├── learn/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx                     Topic grid
│   │   │   └── [topic]/page.tsx             Topic detail + quiz
│   │   ├── globals.css                      Design system (light theme)
│   │   ├── layout.tsx                       Root: Google Fonts, SessionProvider
│   │   ├── page.tsx                         Landing page
│   │   └── providers.tsx                    NextAuth SessionProvider wrapper
│   ├── components/
│   │   ├── diagram/
│   │   │   ├── ArchitectureCanvas.tsx        React Flow canvas + dagre layout
│   │   │   ├── ExplainerPanel.tsx            Slide-in component explanation panel
│   │   │   └── nodes/index.tsx              13 node type renderers + NODE_CONFIG
│   │   ├── learn/
│   │   │   ├── QuizEngine.tsx               Quiz question UI + grading display
│   │   │   └── TopicCard.tsx                Topic card (white, light theme)
│   │   └── ui/
│   │       ├── NavBar.tsx                   Dark sidebar navigation
│   │       └── Spinner.tsx                  Loading indicator
│   ├── lib/
│   │   ├── api.ts                           Axios client + all API functions
│   │   └── auth.ts                          NextAuth config (custom HS256 JWT)
│   ├── middleware.ts                         Edge Runtime route protection
│   ├── types/index.ts                        All TypeScript interfaces
│   ├── tailwind.config.ts                    Custom tokens
│   └── next.config.mjs                      next/image remote patterns
│
└── backend/
    ├── app/
    │   ├── main.py                           FastAPI app, CORS, router registration
    │   ├── api/routes/
    │   │   ├── auth.py                       upsert-user, /me
    │   │   ├── designs.py                    generate, clarify, get, list, delete
    │   │   ├── explain.py                    component explanation
    │   │   ├── learn.py                      topics, quiz generate/submit
    │   │   ├── export.py                     PDF, Markdown download
    │   │   ├── analytics.py                  /me stats, /admin stats
    │   │   └── admin.py                      health, users, role, rebuild-index
    │   ├── core/
    │   │   ├── config.py                     pydantic-settings (env vars)
    │   │   ├── database.py                   Motor MongoDB client, connect/close/get
    │   │   └── security.py                   decode_token, get_current_user, get_admin_user
    │   ├── models/
    │   │   ├── design.py                     DesignCreate, Architecture, etc.
    │   │   ├── quiz.py                       QuizGenerateRequest, QuizSubmitRequest
    │   │   └── user.py                       UserCreate, UserResponse
    │   └── services/
    │       ├── design_builder/
    │       │   ├── pipeline.py               LangGraph graph + run_initial/run_with_clarifications
    │       │   ├── extractor.py              extract_requirements, generate_clarifying_questions
    │       │   ├── generator.py              generate_architecture (GPT-4o)
    │       │   └── rag.py                    FAISS retrieval
    │       ├── explainability/
    │       │   └── explainer.py              explain_component (GPT-4o)
    │       ├── learn_mode/
    │       │   ├── topics.py                 TOPICS list + get_topic()
    │       │   └── quiz_generator.py         generate_quiz, grade_quiz
    │       ├── exporter/
    │       │   ├── md_exporter.py            generate_markdown()
    │       │   └── pdf_exporter.py           generate_pdf()
    │       └── analytics/
    │           └── tracker.py                get_user_stats, get_admin_stats
    └── vector_store/
        ├── faiss_index/                      Persisted FAISS index (auto-created)
        └── seed_data/
            └── patterns.py                   25+ architecture pattern texts
```

---

## 19. Environment Variables

### Frontend (`.env.local`)
| Variable | Required | Description |
|---|---|---|
| `NEXTAUTH_SECRET` | ✅ | Shared HS256 signing secret (must match backend) |
| `GOOGLE_CLIENT_ID` | ✅ | Google OAuth app client ID |
| `GOOGLE_CLIENT_SECRET` | ✅ | Google OAuth app client secret |
| `NEXTAUTH_URL` | ✅ (prod) | Full URL of the Next.js app (e.g., `http://localhost:3000`) |
| `NEXT_PUBLIC_API_URL` | ❌ | Backend URL, defaults to `http://localhost:8000` |

### Backend (`.env`)
| Variable | Required | Description |
|---|---|---|
| `MONGODB_URI` | ✅ | MongoDB Atlas connection string |
| `OPENAI_API_KEY` | ✅ | OpenAI API key (GPT-4o + embeddings) |
| `NEXTAUTH_SECRET` | ✅ | Must be identical to frontend value |
| `ENVIRONMENT` | ❌ | `"development"` or `"production"`, defaults to `"development"` |
| `BACKEND_CORS_ORIGINS` | ❌ | JSON array string of allowed origins, defaults to `["http://localhost:3000"]` |

---

## 20. Hardware Requirements & Performance

### Development (local)
- **CPU:** Any modern x86-64 or Apple Silicon
- **RAM:** 4GB minimum; FAISS index for 25 patterns is ~10MB in memory
- **Disk:** ~500MB for Python venv + Node modules; FAISS index ~5MB
- **Network:** Requires internet for OpenAI API calls and MongoDB Atlas

### LLM latency breakdown (per design generation)
| Step | Model | Avg time |
|---|---|---|
| Requirements extraction | GPT-4o | ~1.5s |
| Clarifying question generation (if needed) | GPT-4o | ~1.5s |
| FAISS similarity search | Local (CPU) | ~50ms |
| Architecture generation | GPT-4o | ~3–5s |
| **Total (no clarification)** | — | **~5–7s** |
| **Total (with clarification)** | — | **~10–12s** |

### Component explanation
- First click: ~2s (GPT-4o call)
- Subsequent clicks (same component): ~0ms (served from MongoDB cache)

### FAISS index operations
- First request (create + embed 25 patterns): ~15–30s (one-time)
- Subsequent server starts (load from disk): ~200ms
- Per-query similarity search: ~50ms

---

## 21. Prompt Engineering

### Design principles used across all prompts

**1. Schema-first output:**
Every prompt ends with `Return ONLY valid JSON (no markdown fences) matching this schema:`. This prevents GPT-4o from wrapping the output in triple-backtick code blocks, which would break `json.loads()`.

**2. Persona priming:**
Each system prompt opens with a role statement:
- Extractor: "You are a senior system design architect."
- Generator: "You are a world-class system design architect."
- Explainer: "You are a senior system design mentor explaining architecture decisions to a student or developer."
- Quiz: "You are a system design instructor creating quiz questions."
- Clarifier: "You are a senior system design architect conducting a scoping session."

**3. Temperature tuning:**
- `0` for extraction and clarification (consistency, structured output)
- `0.2` for generation (slight variety in tech choices while remaining production-appropriate)
- `0.3` for explanation (natural educational prose)
- `0.7` for quizzes (high variety so retakes feel different)

**4. Explicit rules:**
The generation prompt lists hard rules:
- "Every edge must reference valid node ids" (prevents dangling edges)
- "Include at least 6 nodes for any non-trivial system" (prevents minimal/incomplete architectures)
- "Prefer battle-tested technologies" (prevents exotic/experimental tech suggestions)
- "Include auth, monitoring, caching, etc." (ensures completeness)

**5. Context injection:**
RAG patterns are injected under the label `SIMILAR ARCHITECTURE PATTERNS FOR REFERENCE:` — the word "reference" signals the model to use them as inspiration, not copy them verbatim.

**6. Quiz quality rules:**
- "Questions must be practical and scenario-based, not trivia" (prevents "what does CAP stand for?")
- "Distractors must be plausible (common misconceptions, not obviously wrong)" (prevents trivially easy quizzes)
- "Explanations must be educational, not just restate the answer" (ensures learning value)

---

## 22. All Edge Cases & Rules

### Authentication
- If `NEXTAUTH_SECRET` differs between frontend and backend → all API calls return 401. **Fix:** ensure both `.env.local` and `.env` have identical values.
- If the session cookie expires (30 days) → middleware redirects to `/login`. NextAuth handles refresh automatically if configured.
- If a user visits a protected route without a cookie → middleware redirects to `/login` (not 401, a redirect).
- If Google OAuth credentials are revoked → `getSession()` returns null → Bearer token is absent → all API calls silently skip the Authorization header → backend returns 401.

### Design generation
- If GPT-4o returns invalid JSON (markdown fences, extra text) → `json.loads()` raises `JSONDecodeError` → caught, sets `state["error"]` → route returns HTTP 500 with error message.
- If GPT-4o returns an edge with a `source` or `target` that doesn't exist in `nodes` → React Flow renders the edge but cannot connect it to a node (dangling edge). The prompt instructs against this but it can happen on complex designs.
- If the user submits clarifications for a design that belongs to another user → `find_one({_id, user_id})` returns null → 404 Not Found.
- If the user deletes a design and then navigates to `/builder/{id}` → `getDesign()` returns 404 → frontend should handle this (show error state).
- `run_with_clarifications()` skips the LangGraph state machine entirely and calls `retrieve_similar_patterns` and `generate_architecture` directly. The `requirements` dict used is the one stored in MongoDB from the first pass (not re-extracted).

### FAISS / RAG
- If `vector_store/faiss_index/` is deleted → `_load_or_create_store()` recreates it from seed data on the next request (automatic recovery).
- If OpenAI API key is invalid when the index is being created → embedding call fails → `get_vector_store()` raises an exception → the first design generation request fails with 500. The global `_vector_store` remains `None` so subsequent requests retry.
- The `ThreadPoolExecutor(max_workers=2)` limits concurrent FAISS operations. Under high load, additional requests queue. This is acceptable for local dev.

### Quiz system
- Quiz cache (`_quiz_cache`) is process-local. If the server restarts between quiz generation and submission → quiz not found → 404 "Quiz session expired or not found". **Production fix:** use Redis with TTL.
- If the user submits answers for a non-existent `quiz_id` (e.g., typed manually) → 404.
- If `num_questions` in the generate request is 0 → GPT-4o behavior is undefined (may return 0 or 1 questions). Pydantic model should enforce a minimum of 1 (current gap).
- Passing threshold is hardcoded at 70%. There is no per-topic or per-difficulty adjustment.

### Export
- Export requires `architecture` to be non-null. Exporting a design with `status: "awaiting_clarification"` → 400 "Design not yet complete".
- PDF/Markdown include `explanations` only for nodes that the user has clicked. Unclicked nodes appear without the "Why chosen / Alternatives / Trade-offs" section.

### Analytics
- `avg_quiz_score` computed in Python from the last 10 attempts (not all-time). If the user has taken > 10 quizzes, older attempts are excluded from the average.
- `design_count` and `quiz_count` on the user document are counter-cache fields incremented/decremented at write time. They can drift from the actual counts if exceptions occur mid-operation. The analytics queries (`count_documents`) always hit MongoDB directly and are authoritative.

### Frontend / UI
- `useNodesState<Node>([])` and `useEdgesState<Edge>([])` require explicit type parameters — without them, TypeScript infers `never[]` and `setNodes(layouted)` fails compilation.
- `Icon: React.ComponentType<any>` in `NODE_CONFIG` — Lucide icons have `size?: string | number` but the component interface expected `size?: number`. The `any` cast resolves the type mismatch without runtime consequences.
- The landing page uses `min-height: 100vh` with inline `background` style to override the body's `#F8F9FB`. This ensures the light ice-blue gradient covers the full viewport even before JavaScript hydrates.
- The NavBar uses `pathname.startsWith(href)` for non-dashboard routes to keep the active state correct when on sub-routes like `/builder/abc123`. Dashboard uses exact match (`pathname === href`) to prevent it from staying active on all routes.
- `getSession()` in the Axios interceptor is called on every request. It reads from the NextAuth session cache (not a network call each time), so there is no significant performance overhead.

### MongoDB
- All design queries include `user_id` in the filter. This is the ownership check — without it, any authenticated user could read any design by guessing an ObjectId.
- `design_count` is decremented on delete with `$inc: {"design_count": -1}`. If this goes below 0 (due to a bug), it should be treated as 0 on display (current gap — no floor check).
- MongoDB Atlas free tier has a 512MB storage limit and 100 connection limit. Motor uses connection pooling by default (100 connections shared across all requests).

---

*Document generated from full source code analysis of StructAI v1.0 — May 2026*
