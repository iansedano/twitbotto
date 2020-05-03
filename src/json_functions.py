import json
import os


def list_to_json(list_to_convert, json_path):
	with open(json_path,'w') as fp:
		json.dump(list_to_convert, fp)

def read_json(path):
	with open(path) as json_file:
		data = json.load(json_file)
		for tweet in data:
			print(tweet['text'])

