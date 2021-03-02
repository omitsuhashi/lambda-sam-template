import json


def respond(code: int, response: dict):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
