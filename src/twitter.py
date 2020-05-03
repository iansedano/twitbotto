import tweepy
import secret
import json
import sys
from datetime import date, timedelta
from io import TextIOWrapper


sys.stdout = TextIOWrapper(
    sys.stdout.buffer, encoding='utf-8', errors='replace')

CONSUMER_KEY = secret.CONSUMER_KEY
CONSUMER_SECRET = secret.CONSUMER_SECRET
ACCESS_TOKEN = secret.ACCESS_TOKEN
ACCESS_SECRET = secret.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

search_term = "python"

today = date.today()
delta = timedelta(days=-1)


def get_tweets(search_term, type="popular", date=str(today), set_max_id='',set_since_id='',set_geocodes=''):

	tweets = tweepy.Cursor(api.search,
		q=search_term,
		lang="en",
		result_type=type,
		max_id=set_max_id,
		since_id=set_since_id,
		geocodes=set_geocodes,
		tweet_mode="extended",
		include_entities="false",
		since=date).items(100)

	tweet_list =[]
	for t in tweets:
		tweet_list.append(t._json)

	return tweet_list



