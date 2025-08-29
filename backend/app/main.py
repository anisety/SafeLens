from fastapi import FastAPI
from .models import ModerationRequest, ModerationResponse
from .services import moderate_text

app = FastAPI(
    title="SafeLens API",
    description="API for real-time content moderation.",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    """
    On startup, this will preload the model to ensure the first
    request is fast.
    """
    from .services import get_moderation_pipeline
    get_moderation_pipeline()

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Welcome to the SafeLens API"}

@app.post("/moderate", response_model=ModerationResponse, tags=["Moderation"])
def moderate(request: ModerationRequest):
    """
    Analyzes the provided text for harmful content.
    
    - **text**: The text to be analyzed.
    
    Returns a moderation decision with a label and a confidence score.
    """
    result = moderate_text(request.text)
    return ModerationResponse(label=result['label'], score=result['score'])
