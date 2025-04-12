import urllib3
import json
import os


def lambda_handler(event, context):
    if "issue" not in event:
        return

    if "html_url" not in event["issue"]:
        return

    session = urllib3.PoolManager()

    payload = {
        "text": f"Issue Created {event["issue"]["html_url"]}"
    }

    headers = {"Content-Type": "application/json"}

    result = session.request('POST', os.environ["SLACK_URL"], headers=headers, body=json.dumps(payload))

    return result.read()
