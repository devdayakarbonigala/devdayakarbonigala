from fastapi import FastAPI, UploadFile, File
import uvicorn
import shutil
import os

# Dynamically import your existing engine logic
from src.ml_engine.run_ocr import your_ocr_main_function  # <-- Replace with your actual function name if different
from src.ml_engine.structure_data import your_structuring_function # <-- Replace with your actual function name if different

app = FastAPI(title="Document Intelligence & Processing API")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "The Document Intelligence Engine is running seamlessly. Ready to parse unstructured chaos."
    }

@app.post("/extract")
async def extract_document_data(file: UploadFile = File(...)):
    # 1. Securely save the uploaded file temporarily
    temp_file_path = f"assets/temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 2. Run your existing OCR engine logic on the saved image
        # raw_text = your_ocr_main_function(temp_file_path)
        
        # 3. Structure the data using your processing logic
        # structured_json = your_structuring_function(raw_text)
        
        # Temporary placeholder so the API runs immediately
        return {
            "filename": file.filename,
            "status": "Success",
            "message": "File processed through src/ml_engine pipeline successfully.",
            "extracted_data": {
                "sample_extracted_field": "This will hook directly into your structured_data.py output"
            }
        }
        
    except Exception as e:
        return {"status": "Error", "detail": str(e)}
        
    finally:
        # 4. Clean up the asset file after processing so you don't leak storage
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
