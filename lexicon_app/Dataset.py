
class Dataset(object):
    def __init__(self, tweets=None, lexicon=None):
        if tweets is None:
            tweets = []
        if lexicon is None:
            lexicon = {}
        self.tweets = tweets
        self.lexicon = lexicon

    def check(self):
        for tweet in self.tweets:
            for word in tweet: # TODO
                if word in self.lexicon: # TODO
                    pass # TODO tweet.pop(info)


    def get_tweets(self):
        return self.tweets

    def positive_only(self):
        final = []
        for tweet in self.tweets:
            if tweet.contains_drug:
                final.append(tweet)
        return final