from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_moderation_pipeline():
    """
    Initializes and returns a pre-trained text classification pipeline
    for content moderation. This uses a DistilBERT model fine-tuned
    on a toxicity dataset.
    The model is cached to avoid reloading it on every request.
    """
    # You can replace this with any other model from the Hugging Face Hub
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    return pipeline("text-classification", model=model_name)

def moderate_text(text: str):
    """
    Performs content moderation on the input text.
    Returns the predicted label and confidence score.
    """
    moderation_pipeline = get_moderation_pipeline()
    results = moderation_pipeline(text)
    # The model returns a list of results, we take the first one
    result = results[0]
    return {"label": result["label"], "score": result["score"]}
