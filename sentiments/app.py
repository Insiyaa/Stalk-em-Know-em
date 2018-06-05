from flask import Flask, request, render_template, url_for, jsonify, flash
import tweepy
import json
import pandas as pd
from func import Process
from collections import Counter
import pygal

# Start flask app
app = Flask(__name__)
app.secret_key = 'some secret key'

# Set keys
consumer_key = 
consumer_secret = 
access_token = 
access_secret = 

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Index page
@app.route('/')
def index():
    return render_template("index.html")

# Displaying data
@app.route('/data', methods=['GET','POST'])
def data():
    # If requested via GET, go back to homepage
    if request.method == "GET":
        return render_template("index.html")
    else:
        try:
            name = request.form.get("tw_id")

            # Getting tweets and followers list for screen name entered
            publicTweets = tweepy.Cursor(api.user_timeline, id=name).items(50)
            followers = tweepy.Cursor(api.followers,id=name).items(100)

            # Getting data of the screen name entered
            user = api.get_user(name)
            screen_name =  user.screen_name
            des = user.description
            followers_c =  user.followers_count
            status_c = user.statuses_count

            tweet_text = []
            languages = []
            f_loc = []

            for x in publicTweets:
                tweet_text.append(x.text)
                languages.append(x.lang)
            for f in followers:
                if not f.location == '':
                    f_loc.append(f.location)

            # Cleaning and tockenizing
            process = Process()
            tweet_text = process.preprocess(tweet_text)

            analytics = process.analyze(tweet_text)

            # Plotting using pygal
            total = analytics[0] + analytics[1] + analytics[2]
            analytics = list(map(lambda x: x * (100/total),list(analytics)))
            pie_chart = pygal.Pie()
            pie_chart.title = 'Sentiments analysis (in %)'
            pie_chart.add('Positive', analytics[0])
            pie_chart.add('Negative', analytics[1])
            pie_chart.add('Swearing', analytics[2])
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
                if not e[0] == "und":
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
            chart3 = pie_chart.render_data_uri()
            return render_template("data.html", s_name = screen_name, des = des, f_c = followers_c, s_c = status_c, y = count_lang, z = count_loc, chart1 = chart1, chart2 = chart2, chart3 = chart3)
        except:
            # If missed get back to homepage
            flash("Oops! We missed somewhere or screen name doesn't exist. Try again later!")
            return render_template("index.html")

        


if __name__ == "__main__":
    app.run(debug=True)
