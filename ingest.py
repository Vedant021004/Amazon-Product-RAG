import pandas as pd
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from config import *

df = pd.read_csv(CSV_PATH)

documents = []

for _, row in df.iterrows():

    doc = f"""
Product Name: {row['product_name']}

Category: {row['category']}

Discounted Price: {row['discounted_price']}

Actual Price: {row['actual_price']}

Discount Percentage: {row['discount_percentage']}

Rating: {row['rating']}

Rating Count: {row['rating_count']}

About Product:
{row['about_product']}

Review Title:
{row['review_title']}

Review:
{row['review_content']}
"""

    documents.append(doc)

model = SentenceTransformer(MODEL_NAME)

embeddings = model.encode(
    documents,
    show_progress_bar=True
)

client = chromadb.PersistentClient(path=DB_PATH)

try:
    client.delete_collection(COLLECTION_NAME)
except:
    pass

collection = client.create_collection(COLLECTION_NAME)

for i, (doc, embedding) in enumerate(zip(documents, embeddings)):
    collection.add(
        ids=[str(i)],
        documents=[doc],
        embeddings=[embedding.tolist()]
    )

print(f"\nStored {collection.count()} documents.")