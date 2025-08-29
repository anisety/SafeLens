from pydantic import BaseModel

class ModerationRequest(BaseModel):
    text: str

class ModerationResponse(BaseModel):
    label: str
    score: float
