import tweepy # used to access twitter API
import json
import pandas as pd  #provides fast, flexible, and expressive data structures 
from func import Process
from collections import Counter


#authentication
consumer_key = 'HSsfiqvQcqKKJh6aRl2YGAw7f'
consumer_secret = 'AHCKKukN4JAcOjlHarPsAf6MdVF3C1iwZaKUPo9RBBIEDzBAUz'
access_token = '3168794738-siQIS5uIGrEtW7n4gWNBdiqvIYjkmXBSZfcXHo9'
access_secret = 'ZSfyIBLlQVSwxp6RxZZG4ardokkH3HAMZyESJZjlM3FzK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

name = input("Enter the Screen Name: ")

publicTweets = tweepy.Cursor(api.user_timeline, id=name).items(50) #Collecting 50 tweets from the person's timeline
followers = tweepy.Cursor(api.followers,id=name).items(100) #Taking up 100 followers
# Cursor handles all the pagination work
tweet_text = []
languages = []
f_loc = []

for x in publicTweets:
    tweet_text.append(x.text)
    languages.append(x.lang)
for f in followers:
    if not f.location == '':
        f_loc.append(f.location)
print(len(tweet_text))
process = Process()
tweet_text = process.preprocess(tweet_text)

print(process.analyze(tweet_text))

count_lang = Counter()
count_lang.update(languages)
print(count_lang.most_common(5))

count_loc = Counter()
count_loc.update(f_loc)
print(count_loc.most_common(5))
del publicTweets
