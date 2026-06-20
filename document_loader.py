import os
from pypdf import PdfReader

def extract_pdf(file_path):
    pages = []

    pdf = PdfReader(file_path)
    filename = os.path.basename(file_path)

    for page_no, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            pages.append({
                "text": text.strip(),
                "metadata": {
                    "source": filename,
                    "page": page_no
                }
            })

    return pages


def load_documents(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            documents.extend(extract_pdf(file_path))

    return documents