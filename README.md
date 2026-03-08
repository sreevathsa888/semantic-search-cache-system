![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![FAISS](https://img.shields.io/badge/FAISS-VectorSearch-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# Semantic Search Cache System

This project implements a **semantic document search system** using **text embeddings, vector databases, fuzzy clustering, and semantic caching**.

The system exposes its functionality through a **FastAPI backend API** and supports efficient document retrieval using **vector similarity search**.

---

# Dataset

The system uses the **20 Newsgroups Dataset**, which contains approximately **20,000 documents across 20 topics**, including:

* Technology
* Politics
* Science
* Sports
* Religion

Each document is treated as a searchable text document.

---

# System Architecture

```
                +------------------+
                |    User Query    |
                +------------------+
                         |
                         v
                +------------------+
                |   FastAPI Server |
                +------------------+
                         |
                         v
                +----------------------+
                | Query Embedding Model|
                | (SentenceTransformer)|
                +----------------------+
                         |
                         v
                +------------------+
                |   Semantic Cache |
                +------------------+
                    |          |
             Cache Hit      Cache Miss
                |              |
                v              v
       +----------------+   +----------------------+
       | Return Cached  |   |  Vector DB Search    |
       |     Result     |   |      (FAISS)         |
       +----------------+   +----------------------+
                                   |
                                   v
                        +-------------------------+
                        | Retrieve Similar Docs   |
                        +-------------------------+
                                   |
                                   v
                        +-------------------------+
                        | Store Result in Cache   |
                        +-------------------------+
                                   |
                                   v
                        +-------------------------+
                        | Return Response to User |
                        +-------------------------+
```

### Data Processing Pipeline

```
20 Newsgroups Dataset
        |
        v
Document Loader
        |
        v
SentenceTransformer Embeddings
        |
        +----------------------+
        |                      |
        v                      v
FAISS Vector Database   Fuzzy Clustering
```

---

# Technologies Used

* **Python**
* **FastAPI**
* **Sentence Transformers**
* **FAISS (Facebook AI Similarity Search)**
* **Scikit-learn**
* **Scikit-fuzzy**
* **NumPy**

---

# Key Features

## 1️⃣ Semantic Document Search

Documents are converted into vector embeddings using the model:

```
all-MiniLM-L6-v2
```

This allows the system to retrieve **semantically similar documents**, even if the exact words differ.

---

## 2️⃣ Vector Database

The system uses **FAISS** to store document embeddings and perform efficient similarity search.

---

## 3️⃣ Fuzzy Clustering

Documents are grouped using **Fuzzy C-Means clustering**, allowing a document to belong to multiple clusters with different membership strengths.

Example:

```
Document → Cluster A (0.6)
Document → Cluster B (0.4)
```

---

## 4️⃣ Semantic Cache

The system implements a **query cache using cosine similarity**.

If a new query is similar to a previous query:

```
Similarity > 0.85
```

the system returns cached results instead of performing a new search.

This significantly **improves response speed and reduces computation**.

---

# API Endpoints

### Query Search

```
POST /query
```

Example query:

```
space exploration
```

Example response:

```
{
  "cache_hit": false,
  "result": [...]
}
```

---

### Cache Statistics

```
GET /cache/stats
```

Example response:

```
{
  "total_entries": 3,
  "hit_count": 1,
  "miss_count": 2,
  "hit_rate": 0.33
}
```

---

### Clear Cache

```
DELETE /cache
```

Response:

```
Cache cleared
```

---
<img width="1919" height="1036" alt="image" src="https://github.com/user-attachments/assets/e6e1f361-80e9-4266-a393-0a4e02be743b" />

# Running the Project

## 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 2️⃣ Run the FastAPI Server

```
uvicorn api.main:app --reload
```

---

## 3️⃣ Open API Documentation

```
http://127.0.0.1:8000/docs
```

This opens the **FastAPI Swagger UI** where you can test the endpoints interactively.

---

# Example Query

```
space exploration and nasa missions
```

The system retrieves documents related to:

* NASA
* Satellites
* Space shuttle missions
* Astronomy discussions

---

# Project Structure

```
semantic-search-cache-system
│
├── api
│   └── main.py
│
├── cache
│   └── semantic_cache.py
│
├── clustering
│   └── fuzzy_cluster.py
│
├── data
│   └── load_data.py
│
├── embeddings
│   └── embedding_model.py
│
├── vectordb
│   └── vector_store.py
│
├── run_embeddings.py
├── run_vector_search.py
├── run_clustering.py
├── run_cache_test.py
│
├── Dockerfile
├── docker-compose.yml
│
├── requirements.txt
└── README.md
```

---

# Docker Setup (Optional)

Build the Docker image:

```
docker build -t semantic-search-api .
```

Run the container:

```
docker run -p 8000:8000 semantic-search-api
```

The API will be available at:

```
http://localhost:8000/docs
```

---

# Future Improvements

* Persistent vector storage
* Distributed semantic caching
* Interactive clustering visualization
* Scalable deployment with Kubernetes

---

# Author

**Sree Vathsa Oleti**
