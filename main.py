import os
import requests
import tweepy

# Get the API KEY from the environment variable
API_KEY = os.getenv("API")
API_SECRET_KEY = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_SECRET")

# Authentication
auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#---------------------


for tweet in tweepy.Cursor(api.search, q='TinkerHub').items(5):
    print("[*]",tweet.text)
