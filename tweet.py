import requests
from graph_sentence_generator import *
from requests_oauthlib import OAuth1

CONSUMER_KEY = "31JbVNzBE6Y4PC6H3OqT8MlzS"
CONSUMER_SECRET_KEY = "OKvm5MhM0D6mlfTitdeppbl5ZIAaG0P0SPdfrYIhtcA0bslql0"
ACCESS_TOKEN = "1263665819000733698-uugqwqRNvDde2rmFtyYmq8gcYRTyQQ"
ACCESS_SECRET_TOKEN = "Ysyrz93W9wZc8zaO6GYFZM9iP7asPqIVhBLWrTSlUj4Sf"
POST_TWEET_URL = "https://api.twitter.com/1.1/statuses/update.json"

def tweet():
    tweet_msg = generate_sentence_string()
    params = {"status": tweet_msg}
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET_KEY,
                   resource_owner_key=ACCESS_TOKEN,
                   resource_owner_secret=ACCESS_SECRET_TOKEN)
    response = requests.post(url=POST_TWEET_URL, auth=oauth, params=params)
    print("RESPONSE STATUS CODE: " + str(response.status_code))
    print("REPONSE BODY:\n" + response.text)

tweet()
