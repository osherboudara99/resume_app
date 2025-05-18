import os
import re
import logging
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
import chromadb

# Configure logging to display information and errors
logging.basicConfig(level=logging.INFO)

# Define paths and constants
dir_path = os.getcwd()  # Get the current working directory
resume_directory_path = os.path.join(dir_path, "resume")  # Path to the resume folder
VECTOR_DB_DIR = "db"  # Directory to store the vector database
MODEL_NAME = "all-MiniLM-L6-v2"  # Name of the embedding model

def preprocess_text(text):
    """
    Preprocesses the input text by:
    - Converting it to lowercase
    - Removing special characters (except markdown syntax)
    - Stripping extra whitespace
    Args:
        text (str): The input text to preprocess
    Returns:
        str: The cleaned and normalized text
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s\*\-\_\[\]\(\)\:\/\.]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def parse_and_clean_resume(file_path):
    """
    Reads and cleans a markdown file by:
    - Removing unnecessary tags (e.g., \[\[BR\]\])
    - Simplifying link formatting
    - Adding a personal GitHub link if not already present
    Args:
        file_path (str): Path to the markdown file
    Returns:
        str: The cleaned and simplified content of the file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    cleaned_content = []
    for line in content:
        # Remove [[BR]] tags and preprocess the line
        line = line.replace(r"\[\[BR\]\]", "").strip()
        line = line.replace(r"\-", "-")
        line = line.replace("** ", "**\n")
        line = preprocess_text(line)

        # Simplify link formatting for LinkedIn and GitHub links
        if "www.linkedin.com" in line or "www.github.com" in line:
            start = line.find("http")
            if start != -1:
                link = line[start:].split(" ")[0]  # Extract the link
                if "linkedin" in link:
                    line = f"[LinkedIn]({link})"
                elif "github" in link:
                    line = f"[GitHub]({link})"
            else:
                line = ""  # Remove malformed links

        # Add the cleaned line to the list if it's not empty
        if line:
            cleaned_content.append(line)

    # Ensure the personal GitHub link is included
    if "[Personal GitHub](https://github.com/osherboudara99)" not in cleaned_content:
        cleaned_content.append("[Personal GitHub](https://github.com/osherboudara99)")

    # Return the cleaned content as a single string
    return "\n".join(cleaned_content)

def load_documents():
    """
    Loads text and markdown files from the resume directory.
    - For .txt files (only aboutme.txt currently): Reads the content directly.
    - For .md files (only resume.md file): Cleans and parses the content using `parse_and_clean_resume`.
    Returns:
        list: A list of dictionaries, each containing the file ID and its content
    """
    docs = []
    for filename in os.listdir(resume_directory_path):
        file_path = os.path.join(resume_directory_path, filename)
        try:
            if filename.endswith(".txt"):
                # Read plain text files
                with open(file_path, "r", encoding="utf-8") as f:
                    content = preprocess_text(f.read())
                    docs.append({"id": filename, "content": content})
            elif filename.endswith(".md"):
                # Parse and clean markdown files
                mk_str = parse_and_clean_resume(file_path)
                docs.append({"id": filename, "content": mk_str})
            logging.info(f"Loaded document: {filename}")
        except Exception as e:
            logging.error(f"Failed to load document {filename}: {e}")
    return docs

def chunk_text(text, chunk_size=500, overlap=100):
    """
    Splits a large text into smaller chunks of a specified size with overlap.
    Args:
        text (str): The input text to be chunked
        chunk_size (int): The maximum size of each chunk
        overlap (int): The number of overlapping characters between chunks
    Returns:
        list: A list of text chunks
    """
    sentences = sent_tokenize(text)  # Split text into sentences
    chunks, current_chunk = [], []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence)
        # If adding the sentence exceeds the chunk size, finalize the current chunk
        if current_length + sentence_length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]  # Retain overlap
            current_length = sum(len(s) for s in current_chunk)
        current_chunk.append(sentence)
        current_length += sentence_length

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def embed_and_store(test_mode=False):
    """
    Embeds the documents and stores them in a persistent vector database.
    - Loads documents from the resume directory
    - Splits each document into chunks
    - Encodes the chunks into embeddings using a SentenceTransformer model
    - Stores the embeddings, chunk texts, and IDs in a ChromaDB collection
    Args:
        test_mode (bool): If True, processes only the first two documents for testing
    """
    # Load documents from the resume directory
    docs = load_documents()
    if test_mode:
        docs = docs[:2]  # Process only the first two documents in test mode

    texts, ids = [], []

    # Chunk each document and prepare for embedding
    for doc in docs:
        try:
            chunks = chunk_text(doc["content"])
            texts.extend(chunks)
            ids.extend([f"{doc['id']}_chunk{i}" for i in range(len(chunks))])
        except Exception as e:
            logging.error(f"Failed to process document {doc['id']}: {e}")

    try:
        # Initialize the embedding model
        embedder = SentenceTransformer(MODEL_NAME)

        # Generate embeddings for the text chunks
        embeddings = embedder.encode(texts).tolist()

        # Initialize the ChromaDB client and collection
        client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
        collection = client.get_or_create_collection("osher_docs")

        # Add the embeddings, texts, and IDs to the collection
        collection.add(documents=texts, ids=ids, embeddings=embeddings)

        logging.info(f"Embedded {len(texts)} chunks.")
    except Exception as e:
        logging.error(f"Failed to embed or store documents: {e}")

if __name__ == "__main__":
    # Embed and store the documents in vector db
    embed_and_store()