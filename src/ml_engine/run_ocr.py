import easyocr

def run_ai_ocr(image_path):
    print("Loading Neural Network weights...")
    # 'gpu=True' tells it to use your MacBook's GPU (MPS) we checked earlier
    reader = easyocr.Reader(['en'], gpu=True) 
    
    print("Analyzing Image (this may take a moment)...")
    result = reader.readtext(image_path)
    
    print("\n--- AI Extractions ---")
    for (bbox, text, prob) in result:
        # prob is the confidence score (0.0 to 1.0)
        print(f"Confidence: {prob:.2f} | Text: {text}")

if __name__ == "__main__":
    run_ai_ocr("assets/feereciept.jpeg")
