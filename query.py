from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

# -----------------------------
# Embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Vector Store
# -----------------------------
vector_store = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)

generator = None


def get_generator():
    global generator

    if generator is None:
        generator = pipeline(
    task="text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)
    return generator


def ask_question(question):

    docs = vector_store.similarity_search(question, k=3)

    if not docs:
        return "No relevant documents found.", []

    context = "\n\n".join(
        doc.page_content[:500] for doc in docs
    )

    prompt = f"""
Use ONLY the context below to answer.

If the answer is not available in the context, reply:

I couldn't find the answer in the provided documents.

Context:
{context}

Question:
{question}

Answer:
"""

    model = get_generator()

    result = model(
        prompt,
        max_new_tokens=128
    )

    answer = result[0]["generated_text"]

    return answer, docs