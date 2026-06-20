from query import ask_question

print("=" * 60)
print("📄 AI Document Q&A Chatbot")
print("=" * 60)

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer, docs = ask_question(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:\n")

    for doc in docs:
        print(
            f"{doc.metadata['source']} "
            f"(Page {doc.metadata['page']})"
        )