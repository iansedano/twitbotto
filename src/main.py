import os
import sys
import database
import json_functions
import text_processing
import twitter
from datetime import date, timedelta
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import wordcloud_functions


# max tweets can be 100
# no tweets older than 7 days will be found
# max 450 requests 15 mins
# max 300 requests per 3 hour window or 250 requests per month?

# lets do 28 searches per day for last 7 days
# = 196 requests
# have to go from 7 days to today

# ++++++++ SEARCH TERM +++++++++
search_term = "coding"
# ++++++++++++++++++++++++++++++

today = date.today()
json_filename = f"{today}_{search_term}.json"
wordcloud_filename = f"{today}_{search_term}.png"

# tweets = twitter.get_tweets(search_term)
tweets = twitter.get_week_tweets(search_term)

# record_list = json_functions.read_json("..\\jsons\\test.json")

record_list = database.make_basic_record_list(tweets)

json_functions.list_to_json(record_list, json_filename)

text_block = text_processing.make_text_block(record_list)

wordcloud_functions.make_wordcloud(text_block, wordcloud_filename, show=True)
