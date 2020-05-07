import tweepy
import secret
import json
import database
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

today = date.today()
delta = timedelta(days=-1)


def get_tweets(search_term,
               type="popular",
               date=str(today),
               set_max_id='',
               set_since_id='',
               set_geocodes=''):
    tweets = tweepy.Cursor(api.search,
                           q=search_term,
                           lang="en",
                           result_type=type,
                           max_id=set_max_id,
                           since_id=set_since_id,
                           geocodes=set_geocodes,
                           tweet_mode="extended",
                           include_entities="false",
                           until=date).items(100)

    tweet_list = []
    for t in tweets:
        tweet_list.append(t._json)

    return tweet_list


def get_week_tweets(search_term):

    week = []
    for i in range(7):
        week.append(today - timedelta(days=i))

    lots_of_tweets = []

    for d in week:

        print(d)

        tweets_popular = get_tweets(
            search_term, "popular", str(d))
        for t in tweets_popular:
            lots_of_tweets.append(t)

        print(f"Running Total: {len(lots_of_tweets)}")

        least_id = 9999999999999999999
        tweets_recent = get_tweets(
            search_term, "recent", str(d))
        for t in tweets_recent:
            lots_of_tweets.append(t)
            if int(t['id_str']) < least_id:
                least_id = int(t['id_str'])

        print(f"Running Total: {len(lots_of_tweets)}")

        tweets_recent2 = get_tweets(
            search_term, "recent", str(d), least_id)
        for t in tweets_recent2:
            lots_of_tweets.append(t)
            if int(t['id_str']) < least_id:
                least_id = int(t['id_str'])

        print(f"Running Total: {len(lots_of_tweets)}")

    return lots_of_tweets
