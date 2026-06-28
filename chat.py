import requests
import chromadb
from sentence_transformers import SentenceTransformer
from config import *

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection(COLLECTION_NAME)

model = SentenceTransformer(MODEL_NAME)

while True:

    question = input("\nAsk your question (type exit to quit): ")

    if question.lower() == "exit":
        break

    query_embedding = model.encode(question)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are an Amazon Product Assistant.

Answer only from the given context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    print("\n")
    print("=" * 80)
    print(response.json()["response"])
    print("=" * 80)