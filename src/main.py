import os
import sys
import database
import json_functions
import text_processing
import twitter
import wordcloud_functions


#max tweets can be 100
#no tweets older than 7 days will be found
#max 450 requests 15 mins
#max 300 requests per 3 hour window or 250 requests per month?

# lets do 28 searches per day for last 7 days 
# = 196 requests
# have to go from 7 days to today
# 


# testing

tweets = twitter.get_tweets("trump")

# json_functions.list_to_json(tweets, "..\\jsons\\test.json")


record_list = database.make_basic_record_list(tweets)

print(record_list)

# read_json("..\\jsons\\test.json")
