import json
from lambda_common import respond
from models.user import Users


def lambda_handler(event, context):
    params = json.loads(event['body'])
    u = Users('test')
    return respond(200, {'greeting': f'hello {params["name"]}!'})
