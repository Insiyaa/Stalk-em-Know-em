import tweepy

# Consumer key and consumer secret are dummy. Add yours to make this work. I can't share mine publicily.
consumer_key = 'HSsf2YGAw7f'
consumer_secret = 'AHCKKukN4RBBIEDzBAUz'
access_token = '3168794738-IhJujdhmAZ8mO'
access_secret = 'zrVSvnG5cohErrLTlp5bL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

publicTweets = tweepy.Cursor(api.user_timeline, id = "twitter").items(10)
for tweet in publicTweets:
    print(tweet.text)
