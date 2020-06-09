import requests
import os
from tweeter.graph_sentence_generator import *
from requests_oauthlib import OAuth1

POST_TWEET_URL = "https://api.twitter.com/1.1/statuses/update.json"

def tweet():
    tweet_msg = generate_sentence_string()
    params = {"status": tweet_msg}
    print(os.environ.get('CONSUMER_KEY'))
    print(os.environ.get('CONSUMER_SECRET_KEY'))
    print(os.environ.get('ACCESS_TOKEN'))
    print(os.environ.get('ACCESS_SECRET_TOKEN'))
    oauth = OAuth1(os.environ.get('CONSUMER_KEY'),
                   client_secret=os.environ.get('CONSUMER_SECRET_KEY'),
                   resource_owner_key=os.environ.get('ACCESS_TOKEN'),
                   resource_owner_secret=os.environ.get('ACCESS_SECRET_TOKEN'))
    response = requests.post(url=POST_TWEET_URL, auth=oauth, params=params)
    print("RESPONSE STATUS CODE: " + str(response.status_code))
    print("REPONSE BODY:\n" + response.text)
    return response
