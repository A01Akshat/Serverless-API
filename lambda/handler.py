import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks')

def lambda_handler(event, context):

    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])

        task = {
            "id": str(uuid.uuid4()),
            "title": body['title'],
            "due_date": body['due_date']
        }

        table.put_item(Item=task)

        return {
            "statusCode": 201,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps(task)
        }

    if event['httpMethod'] == 'GET':
        response = table.scan()

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps(response['Items'])
        }
