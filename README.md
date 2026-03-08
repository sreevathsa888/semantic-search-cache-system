# Semantic Search Cache System

This project implements a **semantic document search system** using embeddings, vector databases, fuzzy clustering, and semantic caching.  
The system exposes its functionality through a **FastAPI backend API**.

---

## Dataset

The system uses the **20 Newsgroups Dataset**, which contains approximately **20,000 documents across 20 topics**, including:

- Technology
- Politics
- Science
- Sports
- Religion

Each document is treated as a searchable text document.

---

## System Architecture

```mermaid
flowchart TD

A[User Query] --> B[FastAPI Server]

B --> C[Query Embedding Model]

C --> D{Semantic Cache}

D -->|Cache Hit| E[Return Cached Result]

D -->|Cache Miss| F[Vector Database Search]

F --> G[Retrieve Similar Documents]

G --> H[Store Result in Cache]

H --> I[Return Result to User]

subgraph Data Pipeline
J[20 Newsgroups Dataset] --> K[Document Loader]
K --> L[SentenceTransformer Embeddings]
L --> M[FAISS Vector Database]
L --> N[Fuzzy Clustering]
end

## Technologies Used

- Python
- FastAPI
- Sentence Transformers
- FAISS (Facebook AI Similarity Search)
- Scikit-learn
- Scikit-fuzzy
- NumPy

---

## Key Features

### 1. Semantic Document Search
Documents are converted into vector embeddings using:

all-MiniLM-L6-v2

This allows the system to retrieve **semantically similar documents**, even if the words are different.

---

### 2. Vector Database

The system uses **FAISS** to store document embeddings and perform efficient similarity search.

---

### 3. Fuzzy Clustering

Documents are grouped using **Fuzzy C-Means clustering**, allowing a document to belong to multiple clusters with different membership strengths.

Example:
Document → Cluster A (0.6)
Document → Cluster B (0.4)


---

### 4. Semantic Cache

The system implements a **query cache using cosine similarity**.

If a new query is similar to a previous query:

Similarity > 0.85

the system returns cached results instead of performing a new search.

This improves response speed.

---

## API Endpoints

### Query Search

POST /query


Example:


space exploration


Response:


{
"cache_hit": false,
"result": [...]
}


---

### Cache Statistics


GET /cache/stats


Example response:


{
"total_entries": 3,
"hit_count": 1,
"miss_count": 2,
"hit_rate": 0.33
}


---

### Clear Cache


DELETE /cache


Response:


Cache cleared


---

## Running the Project

### Install dependencies


pip install -r requirements.txt


---

### Run the API


uvicorn api.main:app --reload


---

### Open API documentation


http://127.0.0.1:8000/docs


This opens the **FastAPI Swagger UI** for testing endpoints.

---

## Example Query


space exploration and nasa missions


The system retrieves documents related to:

- NASA
- satellites
- space shuttle
- astronomy discussions

---

## Project Structure
semantic-search-cache-system
│
├── api
│ └── main.py
│
├── cache
│ └── semantic_cache.py
│
├── clustering
│ └── fuzzy_cluster.py
│
├── data
│ └── load_data.py
│
├── embeddings
│ └── embedding_model.py
│
├── vectordb
│ └── vector_store.py
│
├── run_embeddings.py
├── run_vector_search.py
├── run_clustering.py
├── run_cache_test.py
│
├── requirements.txt
└── README.md


---

## Future Improvements

- Add Docker containerization
- Add persistent vector storage
- Improve clustering visualization
- Implement distributed caching

---

## Author

Sreevathsa Oleti
