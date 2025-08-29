import json
from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_moderation_pipeline():
    """
    Initializes and returns a pre-trained text classification pipeline.
    Caches the model to avoid reloading on every invocation.
    """
    return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def lambda_handler(event, context):
    """
    AWS Lambda handler for content moderation.
    This function is triggered by API Gateway.
    """
    try:
        body = json.loads(event.get('body', '{}'))
        text_to_moderate = body.get('text')

        if not text_to_moderate:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No text provided for moderation.'})
            }

        moderation_pipeline = get_moderation_pipeline()
        result = moderation_pipeline(text_to_moderate)[0]

        response = {
            'label': result['label'],
            'score': result['score']
        }

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
