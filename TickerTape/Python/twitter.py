import yfinance as yf
import pandas as pd
import os
import tweepy as tw
from pandasql import sqldf, load_meat, load_births
from get_all_tickers import get_tickers as gt
pysqldf = lambda q: sqldf(q, globals())
import re
import itertools
import collections
import matplotlib.pyplot as plt

consumer_key= 'Q92s7dhjVRa8gnQUnIGoGJSwU'
consumer_secret= 'cb0U78LHxF6QFMP7nmgSXbPgvMk1icwjq4tllw4hR6t4TPqeUr'
access_token= '1272935157788368896-3d9y1pYdiEVnxjjgrExcLjaONGpPeP'
access_token_secret= '1scxnqxrLIAu82tBXn39QB4M6R7FE6sgK5cR9zHoY9eWV'

def remove_url(txt):

    return ' '.join(re.sub('([^0-9A-Za-z \t])|(\w+:\/\/\S+)', '', txt).split())

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit = True)

#symbols = pd.DataFrame(gt.get_tickers_filtered(mktcap_min=500000))

tweets = tw.Cursor(api.search,q='$tsla -filter:retweets',lang='en',since='2020-06-15').items(1000)

all_tweets = [tweet.text for tweet in tweets]

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]

words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]

all_words_no_urls = list(itertools.chain(*words_in_tweet))

counts_no_urls = collections.Counter(all_words_no_urls)

clean_tweets_no_urls = pd.DataFrame(counts_no_urls.most_common(15),columns=['words', 'count'])

fig, ax = plt.subplots(figsize=(8, 8))

clean_tweets_no_urls.sort_values(by='count').plot.barh(x='words',y='count', ax=ax, color="purple")

ax.set_title("Common Words Found in Tweets (Including All Words)")

plt.show()

#print(clean_tweets_no_urls.head())


