from fastapi import FastAPI
from data.load_data import load_dataset
from embeddings.embedding_model import EmbeddingModel
from vectordb.vector_store import VectorStore
from cache.semantic_cache import SemanticCache

print("Starting system...")

# Load dataset
documents = load_dataset()

print("Documents loaded:", len(documents))

# Initialize embedding model
embedder = EmbeddingModel()

# Generate embeddings (use subset for speed)
doc_embeddings = embedder.encode_documents(documents[:3000])

dimension = len(doc_embeddings[0])

# Initialize vector database
vector_db = VectorStore(dimension)

vector_db.add_documents(doc_embeddings, documents[:3000])

# Initialize cache
cache = SemanticCache(threshold=0.85)

app = FastAPI()

# ----------------------------
# Query Endpoint
# ----------------------------

@app.post("/query")
def search(query: str):

    q_embedding = embedder.encode_query(query)

    cached_result, hit = cache.check_cache(q_embedding)

    if hit:
        return {
            "cache_hit": True,
            "result": cached_result
        }

    results = vector_db.search(q_embedding)

    cache.add_to_cache(query, q_embedding, results)

    return {
        "cache_hit": False,
        "result": results
    }


# ----------------------------
# Cache Stats
# ----------------------------

@app.get("/cache/stats")
def cache_stats():

    return cache.stats()


# ----------------------------
# Clear Cache
# ----------------------------

@app.delete("/cache")
def clear_cache():

    cache.clear()

    return {"message": "Cache cleared"}