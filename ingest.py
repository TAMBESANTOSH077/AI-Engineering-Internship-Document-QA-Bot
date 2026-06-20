from document_loader import load_documents
from chunker import chunk_documents
from vector_store import get_vector_store

from langchain_core.documents import Document


def ingest():

    print("Loading documents...")

    docs = load_documents("data")

    print(f"Loaded {len(docs)} pages")

    chunks = chunk_documents(docs)

    print(f"Created {len(chunks)} chunks")

    documents = []

    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk["text"],
                metadata=chunk["metadata"]
            )
        )

    vector_store = get_vector_store()

    vector_store.add_documents(documents)

    print("\nDatabase Created Successfully!")
    print(f"Stored {len(documents)} chunks")


if __name__ == "__main__":
    ingest()