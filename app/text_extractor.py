import fitz
from pathlib import Path
from docx import Document
def clean_text(text: str):
    text=text.replace("-\n","")
    text = text.replace("\r\n", "\n")
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)
def extract_pdf_text(file_path: str) -> str:
    doc = fitz.open(file_path)

    text = ""
    for page in doc:
        text += page.get_text()

    doc.close()

    return clean_text(text)


def extract_docx_text(file_path: str) -> str:
    doc = Document(file_path)

    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())

    return clean_text("\n".join(text))


def extract_text(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    raise ValueError("Unsupported file format")