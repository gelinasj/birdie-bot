import requests
import os
import json
from graph_sentence_generator import *
from requests_oauthlib import OAuth1

POST_TWEET_URL = "https://api.twitter.com/1.1/statuses/update.json"
BASE_DIR = "/var/task/"

def lambda_handler(event, context):
    os.chdir(BASE_DIR)
    tweet_msg = generate_sentence_string()
    params = {"status": tweet_msg}
    oauth = OAuth1(os.environ.get('CONSUMER_KEY'),
                   client_secret=os.environ.get('CONSUMER_SECRET_KEY'),
                   resource_owner_key=os.environ.get('ACCESS_TOKEN'),
                   resource_owner_secret=os.environ.get('ACCESS_SECRET_TOKEN'))
    response = requests.post(url=POST_TWEET_URL, auth=oauth, params=params)
    print("RESPONSE STATUS CODE: " + str(response.status_code))
    print("REPONSE BODY:\n" + response.text)
    return {
        'statusCode': response.status_code,
        'body': json.dumps(response.text)
    }
