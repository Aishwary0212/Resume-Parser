from fastapi import FastAPI, UploadFile,File
import shutil
from pathlib import Path
from app.pdf_extractor import extract_text
from app.parser.parser import parse_resume
app=FastAPI()

UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
@app.post("/parse-resume")
async def upload_pdf(file:UploadFile=File(...)):
    file_path-None
    try:
        file_path=UPLOAD_DIR/file.filename
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        text = extract_text(str(file_path))
        parsed_data=parse_resume(text)
        return {
            "message":"Resume received successfully",
            "file_name":file.filename,
            "parsed_data":parsed_data
        }
    finally:
        if file_path and file_path.exists():
            file_path.unlink()
