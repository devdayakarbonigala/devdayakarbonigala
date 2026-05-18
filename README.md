## Document Intelligence & Text Extraction Engine

Currently leveraging PyTorch (MPS) to build an end-to-end processing pipeline engineered to ingest unstructured documents, clean image artifacts, execute high-fidelity text recognition, and structure data into schema-compliant JSON payloads. Designed with production-ready architecture rather than loose experimental scripts.

## System Architecture
The engine splits tasks across a modular processing chain inside `src/ml_engine/`:
1. **`process_image.py`**: Handles asset preprocessing, scaling, and noise-filtering.
2. **`run_ocr.py`**: Executes core text recognition pipelines.
3. **`structure_data.py`**: Standardizes raw text into predictable, structured schemas.
4. **`app.py`**: Wraps the entire engine inside a high-performance **FastAPI** web service.

# Local Deployment & Execution

### Option 1: Native Python
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
