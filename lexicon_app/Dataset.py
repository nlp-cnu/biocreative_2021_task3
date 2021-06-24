import csv
import re

class Dataset(object):
    """
    A Dataset will include a lexicon, stored as a dictionary of drug terms, and a list of tweet objects
    to be searched using the lexicon
    """
    def __init__(self, tweets=None, lex_fpath=None, lex_delim=""):
        if tweets is None:
            tweets = []
        if lex_fpath is None:
            self.lexicon = {}

        self.tweets = tweets

        with open(lex_fpath, 'rt') as lex_file:
            reader = csv.reader(lex_file, lineterminator=lex_delim)
            lexicon = {}
            key = 0
            for item in reader:
                for i in item:
                    lexicon[key] = i
                key += 1
        self.lexicon = lexicon

    def check(self):
        """
        runs lexicon search on tweets in list, call pop(start, end, span, drug) for positive drugs
        :return: none
        """
        for tweet in self.tweets:
            for drug in self.lexicon.values():
                for match in re.finditer(drug, tweet.text):
                    tweet.pop(match.start(), match.end(),
                              tweet.text[int(match.start()): int(match.end())], drug)

    def get_tweets(self):
        return self.tweets

    def positive_only(self):
        final = []
        for tweet in self.tweets:
            if tweet.contains_drug:
                final.append(tweet.list())
        return final

    def write_results(self, fpath):
        with open(fpath, 'wt', encoding="utf") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(['tweet_id', 'text', 'start', 'end', 'span', 'drug'])
            for tweet in self.tweets:
                writer.writerow(tweet.list())
            file.close()

