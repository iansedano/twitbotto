import json
import sys
from io import TextIOWrapper
sys.stdout = TextIOWrapper(
    sys.stdout.buffer, encoding='utf-8', errors='replace')

with open('result.json') as json_file:
    data = json.load(json_file)


lengths = []
texts = []
followers_list = []

for t in data:
    texts.append(t['text'])
    followers_list.append(t["user"]["followers_count"])

for t in texts:
    tweet = t.split(" ")
    lengths.append(len(tweet))

sum = 0
for l in lengths:
    sum += l

average_length = sum / len(lengths)

print(f"average length {average_length}")

longest_word = ""
longest_word_length = 0
for t in texts:
    tweet = t.split()
    for w in tweet:
        if len(w) > longest_word_length:
            longest_word = w
            longest_word_length = len(w)

print(f"longest word {longest_word}")

sum_followers = 0

for n in followers_list:
    sum_followers += n

average_followers = sum_followers / len(followers_list)

print(f"average followers {average_followers}")
