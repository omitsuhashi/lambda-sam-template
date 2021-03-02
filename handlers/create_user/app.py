import boto3
import json
from setting import session


def lambda_handler(event, context):
    params = json.loads(event['body'])
