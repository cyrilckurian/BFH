#====MODULES=====#
import os
import requests
import tweepy
#================#

# Get the API KEY from the environment variable
API_KEY = os.getenv("API")
API_SECRET_KEY = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_SECRET")
#print(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


if __name__ == '__main__':
    # Authentication
    auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Getting Tweets and saving them to a txt file
    SEARCH_KEYWORD = "TinkerHub"
    OUT_FILE = "tweets.txt"
    fh = open(OUT_FILE, 'w')
    for tweet in tweepy.Cursor(api.search, q=SEARCH_KEYWORD).items(5):
        print("[*]",tweet.text)
        try:
            fh.write(tweet.text)
        except Exception as e:
            print(e)
    fh.close()
