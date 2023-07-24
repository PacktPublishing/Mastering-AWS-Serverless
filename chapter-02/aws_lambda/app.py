import json

def lambda_handler(event, context):
    
    # print out the event information
    print(f'event: {event}')
    # print out the context information
    print(f'context: {context}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Mastering AWS Serverless!')
    }
