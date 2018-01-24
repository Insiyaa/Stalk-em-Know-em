import tweepy
import json
import pandas as pd
import matplotlib.pyplot as plt

#authentication
consumer_key = 'HSsfiqvQcqKKJh6aRl2YGAw7f'
consumer_secret = 'AHCKKukN4JAcOjlHarPsAf6MdVF3C1iwZaKUPo9RBBIEDzBAUz'
access_token = '3168794738-siQIS5uIGrEtW7n4gWNBdiqvIYjkmXBSZfcXHo9'
access_secret = 'ZSfyIBLlQVSwxp6RxZZG4ardokkH3HAMZyESJZjlM3FzK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

name = input("Enter the Screen Name: ")

publicTweets = tweepy.Cursor(api.user_timeline, id=name).items(5)


tw_data = []
for tweet in publicTweets:
    data = json.dumps(tweet._json)
    dt = json.loads(data)
    tw_data.append(dt)

del publicTweets
tweets = pd.DataFrame()
tweets['lang'] = map(lambda t: t['lang'], tw_data)

#plotting

