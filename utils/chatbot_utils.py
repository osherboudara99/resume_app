import streamlit as st
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
import chromadb
import logging


MODEL_PATH = "C:\\Users\\Osher N Boudara\\.cache\\gpt4all\\Phi-3-mini-4k-instruct.Q4_0.gguf"
VECTOR_DB_DIR = "db"

# Load model
@st.cache_resource
def load_llm():
    return Llama(
        model_path=MODEL_PATH,
        n_ctx=4096,
        n_threads=6,
        n_gpu_layers=35,
        temperature=0.7,
        stop=["User:", "Assistant:"]
    )
@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def load_vectorstore():
    client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
    return client.get_or_create_collection("osher_docs")

llm = load_llm()
embedder = load_embedder()
vectorstore = load_vectorstore()

def retrieve_and_answer(query):
    # Define a set of simple, predefined responses for general questions
    general_responses = {
        "hi how are you": "I'm doing well, thank you for asking! How can I help you today?",
        "hello how are you": "I'm doing well, thank you for asking! How can I help you today?",
        "hi how are you?": "I'm doing well, thank you for asking! How can I help you today?",
        "hello how are you?": "I'm doing well, thank you for asking! How can I help you today?",
        "how are you": "I'm doing well, thank you for asking! How can I help you today?",
        "what is the weather like": "I’m unable to provide real-time weather information, but you can check your local weather service for the latest updates!",
        "who are you": "I am Rebbe, an AI assistant here to answer questions about Osher Boudara based on the provided context.",
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! How can I assist you today?",
        "good morning": "Good morning! How can I assist you today?",
        "good evening": "Good evening! How can I assist you today?"
    }

    # Convert the query to lowercase and strip whitespace
    query_lower = query.lower().strip()

    # Check if the query matches any of the predefined general questions directly
    if query_lower in general_responses:
        return general_responses[query_lower]

    # Embed the query to get its embedding
    try:
        query_embedding = embedder.encode([query_lower])[0].tolist()
        logging.info("Query embedding generated successfully.")
    except Exception as e:
        logging.error(f"Error generating query embedding: {e}")
        return "An error occurred while processing your query."

    # Query the vector store to find the most relevant documents
    try:
        results = vectorstore.query(query_embeddings=[query_embedding], n_results=3)
    except Exception as e:
        return f"An error occurred while querying the database: {str(e)}"

    # Get the retrieved documents
    docs = results.get("documents", [])

    # Flatten documents list in case of nested lists
    docs = [doc for sublist in docs for doc in (sublist if isinstance(sublist, list) else [sublist])]

    # If no documents are found
    if not docs:
        return "I'm sorry, I can only answer questions about Osher Boudara or general small talk."

    # Combine the retrieved documents into a single context
    context = "\n".join(docs)

    # Prepare the prompt with a clear instruction
    prompt = f"""
    You are Rebbe, a helpful assistant who answers questions about Osher Boudara using only the provided context. 
    Do not make up information or answer questions unrelated to Osher Boudara. If the question is unrelated, respond with:
    "I'm sorry, I can only answer questions about Osher Boudara or general small talk."

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    # Generate a response using the Llama model
    try:
        response = llm(prompt, max_tokens=250)
        return response["choices"][0]["text"].strip()
    except Exception as e:
        logging.error(f"Error generating response from Llama model: {e}")
        return "I'm sorry, I couldn't generate a response. Please try again later."



def create_sidebar():
    with st.sidebar:
        st.markdown("### 💬 Chat with Rebbe!")
        st.markdown("Ask anything about Osher — resume, skills, projects, and more.")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_input = st.chat_input("Ask a question about Osher...")
        if user_input:
            with st.spinner("Rebbe is thinking..."):
                answer = retrieve_and_answer(user_input)
            st.session_state.chat_history.append(("User", user_input))
            st.session_state.chat_history.append(("Assistant", answer))

        for sender, msg in st.session_state.chat_history:
            with st.chat_message("user" if sender == "User" else "assistant"):
                st.markdown(msg)