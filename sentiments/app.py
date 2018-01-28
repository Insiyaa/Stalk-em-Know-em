from flask import Flask, request, render_template, url_for, jsonify
import tweepy
import json
import pandas as pd
from func import Process
from collections import Counter
import pygal

app = Flask(__name__)
#authentication
consumer_key = 'HSsfiqvQcqKKJh6aRl2YGAw7f'
consumer_secret = 'AHCKKukN4JAcOjlHarPsAf6MdVF3C1iwZaKUPo9RBBIEDzBAUz'
access_token = '3168794738-siQIS5uIGrEtW7n4gWNBdiqvIYjkmXBSZfcXHo9'
access_secret = 'ZSfyIBLlQVSwxp6RxZZG4ardokkH3HAMZyESJZjlM3FzK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#routing
@app.route('/')
def index():
    return render_template("layout.html")

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == "GET":
        return render_template("layout.html")
    else:
        name = request.form.get("tw_id")
        publicTweets = tweepy.Cursor(api.user_timeline, id=name).items(50)
        followers = tweepy.Cursor(api.followers,id=name).items(100)

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

        analytics = process.analyze(tweet_text)
        total = sum(analytics)
        analytics = list(map(lambda x: x * (total/100),list(analytics)))
        pie_chart = pygal.Pie()
        pie_chart.title = 'Sentiments analysis (in %)'
        pie_chart.add('Positive', analytics[0])
        pie_chart.add('Negative', analytics[1])
        pie_chart.add('Neutral', analytics[2])
        chart1 = pie_chart.render_data_uri()

        count_lang = Counter()
        count_lang.update(languages)
        count_lang = count_lang.most_common(8)
        sum = 0
        for e in count_lang:
            sum += e[1]

        pie_chart = pygal.Pie()
        pie_chart.title = 'Languages used (in %)'
        for e in count_lang:
            pie_chart.add(e[0], (e[1] * (100/sum)))
        chart2 = pie_chart.render_data_uri()

        count_loc = Counter()
        count_loc.update(f_loc)
        count_loc = count_loc.most_common(8)
        sum = 0
        for e in count_loc:
            sum += e[1]

        pie_chart = pygal.Pie()
        pie_chart.title = 'Location of followers(in %)'
        for e in count_loc:
            pie_chart.add(e[0], (e[1] * (100/sum)))
        chart2 = pie_chart.render_data_uri()

        return render_template("data.html", y = count_lang, z = count_loc, chart1 = chart1, chart2 = chart2)


if __name__ == "__main__":
    app.run(debug=True)