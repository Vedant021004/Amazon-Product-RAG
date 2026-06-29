
# Amazon Product RAG Pipeline

An end-to-end Retrieval-Augmented Generation (RAG) application that enables semantic search over Amazon product data using vector embeddings and a local Large Language Model.

The project converts structured product data into vector embeddings, stores them in ChromaDB, retrieves the most relevant products for a user's query, and generates natural language answers using Llama 3.2 running locally through Ollama.

---

## Features

- Semantic product search using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Local LLM inference with Ollama (Llama 3.2)
- Persistent vector database using ChromaDB
- SentenceTransformer embeddings
- Interactive command-line chatbot
- Modular project structure for easy extension

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Processing | Pandas |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| LLM | Llama 3.2 |
| LLM Runtime | Ollama |
| HTTP Client | Requests |

---

## Project Structure

```
Amazon-Product-RAG/
│
├── amazon.csv
├── config.py
├── ingest.py
├── chat.py
├── requirements.txt
├── README.md
├── .gitignore
└── chroma_db/
```

---

## RAG Architecture

```
                  Amazon Dataset (CSV)
                           │
                           ▼
                 Convert Rows to Documents
                           │
                           ▼
                Sentence Transformer Model
                           │
                           ▼
                     Vector Embeddings
                           │
                           ▼
                      ChromaDB Storage
                           │
                           ▼
                     User Question
                           │
                           ▼
                 Query Embedding Generation
                           │
                           ▼
              Semantic Similarity Search
                           │
                           ▼
                Top Relevant Documents
                           │
                           ▼
                     Llama 3.2 (Ollama)
                           │
                           ▼
                   AI Generated Response
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/Amazon-Product-RAG.git

cd Amazon-Product-RAG
```

Create a virtual environment.

```bash
python -m venv myenv
```

Activate the environment.

### Windows

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
source myenv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama from:

https://ollama.com/download

Download the Llama model.

```bash
ollama pull llama3.2
```

Verify installation.

```bash
ollama run llama3.2
```

---

## Build the Vector Database

Run once.

```bash
python ingest.py
```

This will

- Read the dataset
- Create documents
- Generate embeddings
- Store vectors inside ChromaDB

---

## Start the Chatbot

```bash
python chat.py
```

Example

```
Ask your question:

Recommend a fast charging cable under ₹500
```

Output

```
The best option is the Wayona Nylon Braided USB Cable because it offers fast charging support, has a high customer rating, and fits within the specified budget.
```

---

## Example Questions

- Recommend a fast charging cable under ₹500
- Which headphones have the highest ratings?
- Suggest a Bluetooth speaker under ₹2000
- Find the best USB Type-C cable
- Recommend products with excellent customer reviews
- Which products offer the highest discount?

---

## Workflow

1. Read the CSV dataset.
2. Convert every product into a natural language document.
3. Generate embeddings using SentenceTransformers.
4. Store vectors in ChromaDB.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant documents.
7. Pass retrieved context to Llama 3.2.
8. Generate the final answer.

---

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embedding Models
- Semantic Search
- Prompt Engineering
- Large Language Models
- Local AI Deployment
- Python Development
- Data Processing
- Information Retrieval

---

## Future Improvements

- Web interface using Streamlit
- FastAPI backend
- Metadata filtering
- Hybrid search (BM25 + Vector Search)
- Conversation memory
- Docker support
- Cloud deployment
- Multi-dataset support
- Evaluation pipeline for retrieval quality

---

## Author

**Vedant Kapil**

GitHub: https://github.com/Vedant021004

LinkedIn: https://www.linkedin.com/in/vedant-kapil-8a786740a/
