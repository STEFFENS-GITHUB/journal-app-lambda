import requests


def lambda_handler(event, context):
    response = requests.get("https://dev.steffenaws.com/api/user/1")
    return {
        "statusCode": 200,
        "body": response.text
    }
