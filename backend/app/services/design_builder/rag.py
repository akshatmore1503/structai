"""FAISS-backed RAG for architecture pattern retrieval."""
import os
import asyncio
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.core.config import settings

FAISS_INDEX_PATH = os.path.join(os.path.dirname(__file__), "../../../vector_store/faiss_index")
_executor = ThreadPoolExecutor(max_workers=2)
_vector_store: FAISS | None = None


def _load_or_create_store(embeddings: OpenAIEmbeddings) -> FAISS:
    if os.path.exists(FAISS_INDEX_PATH):
        return FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

    from vector_store.seed_data.patterns import ARCHITECTURE_PATTERNS
    texts = [p["text"] for p in ARCHITECTURE_PATTERNS]
    metadatas = [{"name": p["name"], "tags": p["tags"]} for p in ARCHITECTURE_PATTERNS]
    store = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    os.makedirs(FAISS_INDEX_PATH, exist_ok=True)
    store.save_local(FAISS_INDEX_PATH)
    return store


async def get_vector_store() -> FAISS:
    global _vector_store
    if _vector_store is None:
        embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        loop = asyncio.get_event_loop()
        _vector_store = await loop.run_in_executor(_executor, _load_or_create_store, embeddings)
    return _vector_store


async def retrieve_similar_patterns(query: str, k: int = 3) -> str:
    """Return concatenated text of the k most similar architecture patterns."""
    store = await get_vector_store()
    loop = asyncio.get_event_loop()
    docs = await loop.run_in_executor(_executor, lambda: store.similarity_search(query, k=k))
    return "\n\n---\n\n".join(d.page_content for d in docs)
