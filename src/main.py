import os
import sys
import database
import json_functions
import text_processing
import twitter
from datetime import date, timedelta, datetime
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import wordcloud_functions


# Place search term below
# Will attempt to return maximum 2800 tweets
# from last 7 days.
# Maximum unique tweets retrieved in one operation
# while testing was around 2400.

# ++++++++ SEARCH TERM +++++++++
search_term = "python"
# ++++++++++++++++++++++++++++++

today = date.today()
json_filename = f"{today}_{search_term}.json"
wordcloud_filename = f"{today}_{search_term}.png"

# Getting tweets
tweets = twitter.get_week_tweets(search_term)

# FOR TESTING - comment out the line that gets tweets and uncomment line below
#               so as not to call twitter API every time you want to run a test
#               replace the path to a suitable json file
#               (i.e. one from a previous execution)
# record_list = json_functions.read_json("..\\jsons\\2020-05-06_coding.json")

# Summarizing tweets
record_list = database.make_basic_record_list(tweets)

# ++++ REMOVING +++++
print(f"total tweets retrieved: {len(record_list)}")

# Creating dictionary to get uniques
record_dict = {}
for r in record_list:
    record_dict[r['id_str']] = {
        'created_at': r['created_at'],
        'user_id': r['user_id'],
        'text': r['text'],
    }

print(f"total unqiue tweets: {len(record_dict)}")

# Converting back to json friendly format
record_list = []
for r in record_dict.keys():
    record = {'id_str': r,
              'created_at': record_dict[r]['created_at'],
              'user_id': record_dict[r]['user_id'],
              'text': record_dict[r]['text']}
    record_list.append(record)

# Export to json
json_functions.list_to_json(record_list, json_filename)

# Creating text block to use as Wordcloud input
text_block = text_processing.make_text_block(record_list)

# Creating wordcloud
wordcloud_functions.make_wordcloud(text_block, wordcloud_filename, show=True)

# Print current time so know when 15 mins have passed.
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
