import tweepy
import json
import pandas as pd
import matplotlib.pyplot as plt
import preprocessor as p
from nltk.tokenize import TweetTokenizer
import preprocessor as p
from preprocessor.api import clean

#authentication
consumer_key = 'HSsfiqvQcqKKJh6aRl2YGAw7f'
consumer_secret = 'AHCKKukN4JAcOjlHarPsAf6MdVF3C1iwZaKUPo9RBBIEDzBAUz'
access_token = '3168794738-siQIS5uIGrEtW7n4gWNBdiqvIYjkmXBSZfcXHo9'
access_secret = 'ZSfyIBLlQVSwxp6RxZZG4ardokkH3HAMZyESJZjlM3FzK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

name = input("Enter the Screen Name: ")

publicTweets = tweepy.Cursor(api.user_timeline, id=name).items(10)

'''
twt = ''
for x in publicTweets:
    twt = x.text

p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.NUMBER)
twt = p.clean(twt)
tknz = TweetTokenizer()
twt = tknz.tokenize(twt)
print(twt)
'''

tw_data = []
for tweet in publicTweets:
    data = (tweet._json)
    #dt = json.loads(data)
    tw_data.append(data)

del publicTweets
tweets = pd.DataFrame()
tweets['lang'] = map(lambda t: t['lang'], tw_data)
tweets['country'] = map(lambda t : t['place']['country'] if t['place'] != None else None, tw_data)
byLang = tweets['lang'].value_counts()
byCountry = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
byLang[:5].plot(ax=ax, kind='barh', color='red')
plt.show()

fig, ax = plt.subplots()
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 Countries', fontsize=15, fontweight='bold')
byCountry[:5].plot(ax=ax, kind='barh', color='b')
plt.show()