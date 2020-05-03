import os
import tweepy
import secret
import json
import sqlalchemy
import sys
from datetime import date, timedelta
from pprint import pprint
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

#max tweets can be 100
#no tweets older than 7 days will be found
#max 450 requests 15 mins
#max 300 requests per 3 hour window or 250 requests per month?

# lets do 28 searches per day for last 7 days 
# = 196 requests
# have to go from 7 days to today
# 

today = date.today()
delta = timedelta(days=-1)

def get_tweets(search_term, json_path, type, date):
	tweets = tweepy.Cursor(api.search,
		q=search_term,
		lang="en",
		result_type=type, # maybe alternate between recent and popular
		# maybe include a max_id and since_id here based on the tweets received, so as to get more tweets.
		# maybe include certain geocodes (most popular tweeting cities?) latitude,longitude,radius (radius in mi), i.e "37.781157 -122.398720 1mi"
		include_entities="false",
		since=date).items(100)

	mylist =[]
	for t in tweets:
		mylist.append(t._json)

	with open(json_path,'w') as fp:
		json.dump(mylist, fp)

# testing

get_tweets("coronavirus", "jsons\\test.json", "recent", str(today))



def read_json(path):
	with open(path) as json_file:
		data = json.load(json_file)
		for tweet in data:
			print(tweet['text'])

read_json("jsons\\test.json")

def json_to_db(json_path):
	

	engine = sqlalchemy.create_engine(
    	'mysql+pymysql://root:cO2rm2JY9mHNPqkr0GSs@localhost/twitbotto')

	connection = engine.connect()
	metadata = sqlalchemy.MetaData()
	tweets = sqlalchemy.Table(
	    'tweets', metadata, autoload=True, autoload_with=engine)
	searches = sqlalchemy.Table(
	    'searches', metadata, autoload=True, autoload_with=engine)
	hashtags = sqlalchemy.Table(
	    'hashtags', metadata, autoload=True, autoload_with=engine)
	users = sqlalchemy.Table(
	    'users', metadata, autoload=True, autoload_with=engine)



	query = sqlalchemy.insert(newTable).values(
	    id=1,
	    name='Software Ninjaneer',
	    salary=60000.00,
	    active=True)

	result_proxy = connection.execute(query)

	query = sqlalchemy.insert(newTable)

	new_records = [{'id': '2', 'name': 'record1', 'salary': 80000, 'active': False},
	               {'id': '3', 'name': 'record2', 'salary': 70000, 'active': True}]

	result_proxy = connection.execute(query, new_records)
