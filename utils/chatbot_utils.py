import streamlit as st
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
import chromadb


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
    
    query_lower = query.lower().strip()

    # Check if the query matches any of the predefined general questions directly
    if query_lower in general_responses:
        return general_responses[query_lower]

    # Embed the query to get its embedding
    query_embedding = embedder.encode([query])[0].tolist()

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
        return "I'm sorry, I couldn't find any information on that topic. Please ask about Osher's resume or experiences."
    
    if "work" in query.lower() and "?" in query:
        return "Could you specify if you're asking about Osher's work at Cognizant, Hoffman Brothers Realty, or one of his personal projects?"
    
    context = "\n".join(docs)
    
    # Prepare the prompt with a clear instruction
    prompt = f"""
    You are Rebbe, a helpful assistant who answers questions about Osher Boudara using only the provided context. 
    Answer in a concise manner, with a focus on clarity and completeness. Below are sections about Osher Boudara and Osher Boudara's resume.

    -- For Cognizant-related queries --
    Please refer to the information in the **Cognizant** section when answering questions about Osher's work experience at Cognizant. Do not combine this with other work experiences or projects.

    -- For Hoffman Brothers Realty-related queries --
    Please refer to the information in the **Hoffman Brothers Realty** section when answering questions about Osher's work at Hoffman Brothers Realty. Do not include information about other work experiences or personal projects.

    -- For Personal Projects-related queries --
    Focus on the **Personal Projects** section when answering questions about Osher's personal projects. Do not mix them with work experience at Cognizant or other companies.

    Context:
    {context}

    Answer the user's question clearly, focusing only on the relevant section. (Provide a short and complete answer, summarizing the relevant details from the context.)
    """
    
    # Generate a response using the Llama model
    try:
        response = llm(prompt, max_tokens=250)
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return f"An error occurred while generating the response: {str(e)}"



def create_sidebar():
    with st.sidebar:
        st.markdown("### 💬 Chat with Rebbe!")
        st.markdown("Ask anything about Osher — resume, skills, projects, and more.")
        
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_input = st.chat_input("Ask a question about Osher...")
        if user_input:
            answer = retrieve_and_answer(user_input)
            st.session_state.chat_history.append(("User", user_input))
            st.session_state.chat_history.append(("Assistant", answer))

        for sender, msg in st.session_state.chat_history:
            with st.chat_message("user" if sender == "User" else "assistant"):
                st.markdown(msg)