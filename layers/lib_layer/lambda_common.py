import json
from typing import Optional


def respond(
        code: int,
        response: Optional[dict],
        err: Optional[Exception] = None):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response) if response else {
            'error': err
        }
    }
