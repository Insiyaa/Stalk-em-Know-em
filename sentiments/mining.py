from nltk.tokenize import TweetTokenizer
import preprocessor as p
from preprocessor.api import clean
import operator 
from collections import Counter
#import vincent
'''
import tweepy
import json
import pandas as pd
import matplotlib.pyplot as plt
#pip install nltk and install the package punkt of it. 
from nltk.tokenize import word_tokenize

# Consumer key and consumer secret are dummy. Add yours to make this work. I can't share mine publicily.

consumer_key = 'HSsfh6aRl2YGAw7f'
consumer_secret = 'AHCKKuwZaKUPo9RBBIEDzBAUz'
access_token = '316879473BdiqvIYjkmXBSZfcXHo9'
access_secret = 'ZSfyIBLZjlM3FzK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#tweet = "Playin around with tweepy!"
#try:
#    if api.update_status(status=tweet):
#        print("Posted")
#except tweepy.error.TweepError as e:
#    print(e)

tw_data = []
user = api.me()
print("Name:",user.name)
print("Location:", user.location)
print("Friends:",user.friends_count)

def process_or_store(tweet, here):   
    data = json.dumps(tweet._json)
    dt = json.loads(data)
    tw_data.append(dt)

publicTweets = tweepy.Cursor(api.home_timeline).items(5)

for tweet in publicTweets:
    process_or_store(tweet, "tweets")

#for friend in tweepy.Cursor(api.friends).items():
#    process_or_store(friend, "friends")
'''

tweet = b"@someone did you accomplish happy good check out this #superawesome!! it's very very cool \xF0\x9F\x98\x81 http://t.co/ydfY2".decode('utf-8')
p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.NUMBER)
tweet = p.clean(tweet)
tknz = TweetTokenizer()
tweet = tknz.tokenize(tweet)
print(tweet)
#count_all = Counter()
#terms_all = [term for term in tweet]
#count_all.update(terms_all)
#print(count_all.most_common(5))

positives = set()
negatives = set()

with open("positive-words.txt") as file:
    for line in file:
        if not line.startswith(";"):
            positives.add(line.strip('\n'))
    file.close()

with open("negative-words.txt") as file:
    for line in file:
        if not line.startswith(";"):
            negatives.add(line.strip('\n'))
    file.close()


score = 0
for word in tweet:
    if word in positives:
        score += 1
    elif word in negatives:
        score -= 1
print(score)
'''
word_freq = count_all.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')
'''

'''
with open(data_path, 'r') as f:
    for line in f:
        try:
            tw = json.loads(line)
            tw_data.append(tw)
        except:
            print("eroor")
            continue


print(len(tw_data))

tweets = pd.DataFrame()
tweets['text'] = map(lambda t : t['text'], tw_data)
tweets['lang'] = map(lambda t : t['lang'], tw_data)
tweets['country'] = map(lambda t : t['place']['country'] if t['place'] != None else None, tw_data)

#plotting
byLang = tweets['lang'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', label_size=15)
ax.tick_params(axis='y', label_size=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
byLang[:5].plot(ax=ax, kind='bar', color='red')

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()
'''