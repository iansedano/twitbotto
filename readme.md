# Twitter Wordcloud Generator

A short script that connects to twitter (you would need your own API keys), and searches for as many tweets as it can for a search word, and makes a wordcloud using the python wordcloud library (https://amueller.github.io/word_cloud/)

## Installation

I am on Windows, for wordcloud, this involved me downloading the wheel from here
https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
solution found here
https://github.com/amueller/word_cloud/issues/134

On Linux I believe its as simple as running

```bash
pip install wordcloud
```

The tweepy library is also used `pip install tweepy`

## Usage

in the main.py file there is a variable called search term, fill this with whatever you want, though it should be a trending word, or at least something that will produce many tweets from the last 7 days (limit of twitter free API search).
```python
# ++++++++ SEARCH TERM +++++++++
search_term = ""
# ++++++++++++++++++++++++++++++
```
This can only run once in the space of 15 minutes, any more than that and you will run into the limit returning
```
tweepy.error.TweepError: Twitter error response: status code = 429
```

See the docs for wordcloud, twitter API, tweepy for more info. Or message me directly.

There is mysqlalchemy functionality written, but not finished or tested. At the moment it runs completely on json files.

## Contributing
This is a small project made for a coding course, but I am open to collaborating to extend its functionality.

## License
[MIT](https://choosealicense.com/licenses/mit/)
The wordcloud, tweepy and mysql libraries are MIT licenced.