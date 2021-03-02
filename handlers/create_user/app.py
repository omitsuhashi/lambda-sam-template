import json
from lambda_common import respond


def lambda_handler(event, context):
    params = json.loads(event['body'])
    return respond(200, {'greeting': f'hello {params["name"]}!'})
