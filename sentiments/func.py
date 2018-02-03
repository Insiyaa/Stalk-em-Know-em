from nltk.tokenize import TweetTokenizer
import preprocessor as p
from preprocessor.api import clean

class Process():

    def __init__(self):
        self.positive = set()
        self.negative = set()
        self.swears = set()
        with open("positive-words.txt") as file:
            for line in file:
                if not line.startswith(";"):
                    self.positive.add(line.strip('\n'))
            file.close()

        with open("negative-words.txt") as file:
            for line in file:
                if not line.startswith(";"):
                    self.negative.add(line.strip('\n'))
            file.close()
        
        with open("badwords.txt") as file:
            for line in file:
                self.swears.add(line.strip('\n'))
            file.close()

    def preprocess(self, tweet_text):
        processed = []
        for twt in tweet_text:
            p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.NUMBER)
            twt = p.clean(twt)
            tknz = TweetTokenizer()
            twt = tknz.tokenize(twt)
            processed.extend(twt)
        return processed

    def analyze(self, tokenList):
        pos = 0
        neg = 0
        swear = 0
        for word in tokenList:
            if word in self.positive:
                pos += 1
            elif word in self.negative:
                neg += 1
            elif word in self.swears:
                swear += 1
        return (pos,neg,swear)
