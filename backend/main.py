from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Content(BaseModel):
    text: str

@app.post("/moderate/")
async def moderate_content(content: Content):
    """
    This endpoint receives text content and returns a moderation decision.
    Replace this with your actual NLP model pipeline.
    """
    # Placeholder for BiLSTM/BERT model inference
    is_harmful = "harmful" in content.text.lower() # Simple keyword check
    
    return {
        "content": content.text,
        "is_harmful": is_harmful,
        "confidence_score": 0.95 if is_harmful else 0.05
    }

@app.get("/")
async def root():
    return {"message": "SafeLens NLP Moderation API is running."}

# To run this app:
# 1. Install FastAPI and uvicorn: pip install fastapi uvicorn
# 2. Run from your terminal: uvicorn main:app --reload
