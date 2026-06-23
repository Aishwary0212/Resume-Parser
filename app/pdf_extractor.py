import fitz
def extract_text(pdf_path:str)->str:
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text