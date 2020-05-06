import json
import os


def list_to_json(list_to_convert, json_file_name):
    path = "..\\jsons\\" + json_file_name
    with open(path, 'w') as fp:
        json.dump(list_to_convert, fp)


def read_json(path):
    with open(path) as json_file:
        return json.load(json_file)
