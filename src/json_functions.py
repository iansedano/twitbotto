import json
import os


def list_to_json(list, json_path):
	with open(json_path,'w') as fp:
		json.dump(mylist, fp)

def read_json(path):
	with open(path) as json_file:
		data = json.load(json_file)
		for tweet in data:
			print(tweet['text'])

