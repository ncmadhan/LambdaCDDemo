import boto3
import json

def lambda_handler(event, context):
    response = {
	  "name": "John",
	  "age": 30,
	  "city": "New York"
	}

    return {"statusCode": 200, "body": json.dumps(response)}
