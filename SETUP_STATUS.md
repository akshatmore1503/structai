# StructAI Setup Status

## ✅ Completed Setup

### Backend (FastAPI)
- ✅ Python 3.12 detected
- ✅ Virtual environment created at `backend/.venv`
- ✅ All dependencies installed from requirements.txt:
  - FastAPI 0.111.0
  - Uvicorn 0.30.1
  - LangChain & LangGraph (LLM orchestration)
  - Motor 3.4.0 (async MongoDB driver)
  - FAISS (vector store for RAG)
  - OpenAI client library
  - All other dependencies

### Frontend (Next.js)
- ✅ Node.js 20+ available
- ✅ npm dependencies installed (612 packages)
- ✅ Configuration files created

### Environment Files
- ✅ Created `backend/.env` (template)
- ✅ Created `frontend/.env.local` (template)

---

## ⚠️ What's Needed to Run (Missing Credentials)

The application requires the following to fully function:

### 1. **MongoDB Atlas Connection**
```env
# backend/.env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/structai?retryWrites=true&w=majority
```
- Get from: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Free tier available (M0)

### 2. **OpenAI API Key**
```env
# backend/.env
OPENAI_API_KEY=sk-...
```
- Get from: [OpenAI API Keys](https://platform.openai.com/api-keys)
- Required for GPT-4o model and embeddings (text-embedding-ada-002)

### 3. **Google OAuth Credentials**
```env
# backend/.env & frontend/.env.local
GOOGLE_CLIENT_ID=...apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=...
```
- Get from: [Google Cloud Console](https://console.cloud.google.com)
- Create an OAuth 2.0 Application

### 4. **JWT Secrets** (Already in env files, but can be regenerated)
```bash
# Generate secure secrets:
openssl rand -base64 32
```

---

## 🚀 Quick Start (Once Credentials Are Added)

### Step 1: Configure Backend
```bash
cd backend
# Edit .env with your credentials
# MONGODB_URI
# OPENAI_API_KEY
# NEXTAUTH_SECRET (or keep existing one if matching frontend)
```

### Step 2: Start Backend
```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Step 3: Configure Frontend
```bash
cd frontend
# Edit .env.local with credentials and backend URL
# GOOGLE_CLIENT_ID
# GOOGLE_CLIENT_SECRET
# NEXTAUTH_SECRET (must match backend!)
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Step 4: Start Frontend
```bash
cd frontend
npm run dev
```
The UI will be available at: `http://localhost:3000` (or 3001 if 3000 is in use)

---

## 📊 Current Server Status

| Component | Port | Status | Notes |
|-----------|------|--------|-------|
| Backend (FastAPI) | 8000 | ❌ Fails on startup | Needs MONGODB_URI |
| Frontend (Next.js) | 3000/3001 | ✅ Ready to start | Just needs credentials to connect |

---

## 🧪 Testing After Setup

### Backend Health Check
```bash
curl http://localhost:8000/docs
```

### Frontend Access
Open browser to `http://localhost:3000`

### Design Generation (once running)
```bash
curl -X POST http://localhost:8000/api/v1/designs/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"problem_statement": "Build a real-time collaboration platform like Figma"}'
```

---

## 📁 Project Structure

```
structai/
├── backend/          # FastAPI application
│   ├── .venv/        # ✅ Virtual environment (installed)
│   ├── app/          # Application code
│   ├── .env          # ✅ Created (needs credentials)
│   └── requirements.txt
│
├── frontend/         # Next.js application
│   ├── node_modules/ # ✅ Installed (612 packages)
│   ├── app/          # Pages and routes
│   ├── .env.local    # ✅ Created (needs credentials)
│   └── package.json
│
├── docker/           # Dockerfiles for deployment
└── README.md         # Full project documentation
```

---

## 🔑 Key Features to Test Once Running

1. **Design Generation**
   - Enter a problem statement (e.g., "Build Netflix")
   - System generates architecture diagram
   - View component explanations

2. **Interactive Visualization**
   - React Flow diagram with drag, zoom, pan
   - Click components to see detailed explanations

3. **Learning Module**
   - 10 system design topics
   - Adaptive quizzes (3 difficulty levels)
   - Progress tracking

4. **Export**
   - PDF and Markdown export
   - Shareable architecture documents

---

## 🆘 Troubleshooting

### Backend won't start: "DNS query name does not exist"
- Solution: Update `MONGODB_URI` in `backend/.env`

### Backend won't connect to OpenAI
- Solution: Verify `OPENAI_API_KEY` is set and valid

### Frontend can't connect to backend
- Solution: Verify `NEXT_PUBLIC_API_URL=http://localhost:8000` in `frontend/.env.local`

### Port already in use
- Backend: `lsof -i :8000` and kill the process, or use a different port
- Frontend: Next.js will automatically try port 3001 if 3000 is in use

---

## 📚 Additional Resources

- **Project README**: [README.md](README.md)
- **Backend Docs**: [backend/README.md](backend/README.md)
- **Frontend Docs**: [frontend/README.md](frontend/README.md)
- **Research Paper**: [Paper.md](Paper.md)
- **Project Details**: [Blackbook.md](Blackbook.md)

---

**Last Updated**: June 15, 2026
**Setup Status**: Infrastructure Ready ✅ | Credentials Pending ⏳
