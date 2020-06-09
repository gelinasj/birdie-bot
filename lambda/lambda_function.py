import json
import requests

def lambda_handler(event, context):
    response = requests.post("https://michael-gary-bot.herokuapp.com/tweet/")
    return {
        'statusCode': response.status_code,
        'body': json.dumps(response.text)
    }

