import tweepy
import json
import re
#pip install nltk and install the package punkt of it. 
from nltk.tokenize import word_tokenize

# Consumer key and consumer secret are dummy. Add yours to make this work. I can't share mine publicily.
consumer_key = 'HSsAw7f'
consumer_secret = 'AHCKKukzBAUz'
access_token = '31687947kmXBSZfcXHo9'
access_secret = 'ZSfjlM3FzK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

'''
tweet = "Playin around with tweepy!"
try:
    if api.update_status(status=tweet):
        print("Posted")
except tweepy.error.TweepError as e:
    print(e)
'''

user = api.me()
print("Name:",user.name)
print("Location:", user.location)
print("Friends:",user.friends_count)

def process_or_store(tweet, here):
    data = json.dumps(tweet._json)
    with open("DATA/"+ here + ".json","a") as f:
        f.write(data)


publicTweets = tweepy.Cursor(api.home_timeline).items(10)

for tweet in publicTweets:
    process_or_store(tweet, "tweets")

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend, "friends")

tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(tweet))


