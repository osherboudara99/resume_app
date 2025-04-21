import os 
from sentence_transformers import SentenceTransformer
import chromadb


dir_path = os.getcwd()
resume_directory_path = os.path.join(dir_path, "resume")

VECTOR_DB_DIR = "db"

def load_documents():
    docs = []
    for filename in os.listdir(resume_directory_path):
        if filename.endswith(".md") or filename.endswith(".txt"):
            with open(os.path.join(resume_directory_path, filename), "r", encoding="utf-8") as f:
                docs.append({"id": filename, "content": f.read()})
    return docs

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def embed_and_store():
    docs = load_documents()
    texts, ids = [], []

    for doc in docs:
        chunks = chunk_text(doc["content"])
        texts.extend(chunks)
        ids.extend([f"{doc['id']}_chunk{i}" for i in range(len(chunks))])

    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedder.encode(texts).tolist()

    client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
    collection = client.get_or_create_collection("osher_docs")
    collection.add(documents=texts, ids=ids, embeddings=embeddings)

    print(f"Embedded {len(texts)} chunks.")

if __name__ == "__main__":
    embed_and_store()
