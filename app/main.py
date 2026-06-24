from fastapi import FastAPI, UploadFile,File,HTTPException
import shutil
from pathlib import Path
from app.text_extractor import extract_text
from app.parser.parser import parse_resume
app=FastAPI()

UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
def root():
    return {"for Testing go to /docs also for now it is doing for pdf only"}
@app.post("/parse-resume")
async def upload_pdf(file:UploadFile=File(...)):
    extension=Path(file.filename).suffix.lower()
    if(extension) not in [".pdf",".docx"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format"
        )
    file_path=None
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
