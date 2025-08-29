import json

def lambda_handler(event, context):
    """
    AWS Lambda handler for SafeLens content moderation.
    
    This function is triggered by an API Gateway, S3 event, or other AWS service.
    It processes the input content and returns a moderation result.
    """
    
    # 1. Parse input from the event object
    # Example: For API Gateway, the content might be in event['body']
    try:
        body = json.loads(event.get('body', '{}'))
        content_to_moderate = body.get('text', '')
    except (json.JSONDecodeError, AttributeError):
        content_to_moderate = ''

    if not content_to_moderate:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No text provided for moderation.'})
        }

    # 2. Perform moderation (placeholder logic)
    # In a real application, you would invoke a SageMaker endpoint,
    # use AWS Comprehend, or run a model packaged with the Lambda function.
    is_harmful = "harmful" in content_to_moderate.lower()
    confidence_score = 0.95 if is_harmful else 0.05

    # 3. Format the response
    response = {
        'content': content_to_moderate,
        'is_harmful': is_harmful,
        'confidence_score': confidence_score
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*' # For CORS
        },
        'body': json.dumps(response)
    }

# Example event for testing:
# {
#   "body": "{\"text\": \"This is some harmful content.\"}"
# }
