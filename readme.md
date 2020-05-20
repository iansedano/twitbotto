# Twitter Wordcloud Generator

![](https://www.dropbox.com/s/gv1vsjwl6cztw3v/2020-05-20_python.png?raw=1)

Wordcloud generated on 2020-05-20 using the search term "python" made from 2123 unique tweets fetched from the date of the search and the 7 days previous.

---

A short script that connects to twitter (you would need your own API keys), and searches for as many tweets as it can for a search word, and makes a wordcloud using the python wordcloud library (https://amueller.github.io/word_cloud/)

### Excluded words
Words like "to", "the" and "a" are automatically excluded from the wordcloud generation. These for the most part automatically taken car of by the wordcloud library. I added `["https", "co", "ly", "&amp;", "amp", "re", "dr", "rt"]` also as they didn't carry any semantic meaning.

I removed all hyperlinks and @user mentions using regex in text_processing.py. These can be disabled there by commenting out the line.

Hashtags are included, the "#" is removed.

## Installation

I only have used this in windows, and to install wordcloud, this involved me downloading the wheel from here
https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

this solution for installation was found here
https://github.com/amueller/word_cloud/issues/134

On Linux I believe its as simple as running

```bash
pip install wordcloud
```

The tweepy library is also used `pip install tweepy`


You will need to get a twitter developer account and have these keys stored as variable in the src folder with filename `secret.py`
```
CONSUMER_KEY = "your key"
CONSUMER_SECRET = "your key"
ACCESS_TOKEN = "your key"
ACCESS_SECRET = "your key"
```

## Usage

In the main.py file there is a variable called `search_term`, fill this with whatever you want, though it should be a trending word, or at least something that will produce many tweets from the last 7 days (limit of twitter free API search).

```python
# ++++++++ SEARCH TERM +++++++++
search_term = "<your search term here>"
# ++++++++++++++++++++++++++++++
```

This can only run once in the space of 15 minutes, any more than that and you will run into the limit returning

```
tweepy.error.TweepError: Twitter error response: status code = 429
```

See the docs for wordcloud, twitter API, tweepy for more info. Or message me directly.

There is mysqlalchemy functionality written, but not finished or tested. At the moment it runs completely on json files.


## License
[MIT](https://choosealicense.com/licenses/mit/)
The wordcloud, tweepy and mysql libraries are MIT licenced.