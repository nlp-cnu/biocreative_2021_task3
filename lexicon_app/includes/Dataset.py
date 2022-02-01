import csv
import re

class Dataset(object):
    """
    A Dataset will include a lexicons, stored as a dictionary of drug terms, and a list of tweet objects
    to be searched using the lexicons
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
                    if i != "pill" and i != "shot" and i != "shots":
                        lexicon[i] = key
                key += 1
        self.lexicon = lexicon

    def check(self, subwords_bool, stop_words_bool):
        """
        runs lexicons search on tweets in list, call pop(start, end, span, drug) for positive drugs
        :return: none
        """
        if stop_words_bool:
            #self.lexicons["pill"] = len(self.lexicons) + 1
            #self.lexicons["shot"] = len(self.lexicons) + 1
            #self.lexicons["shots"] = len(self.lexicons) + 1
            if "pill" in self.lexicon:
                del(self.lexicon["pill"])
            if "shot" in self.lexicon:
                del(self.lexicon["shot"])
            if "shots" in self.lexicon:
                del(self.lexicon["shots"])

        tweet_num = 1
        num_tweets = len(self.tweets)
        for tweet in self.tweets:
            print ('running: ' + str(stop_words_bool) + ', ' + str(subwords_bool) + ', checking tweet # ' + str(tweet_num) + '/' + str(num_tweets))
            tweet_num+=1
            if subwords_bool:
                for drug in self.lexicon.keys():
                    start = tweet.text.find(drug)
                    if start != -1:
                        end = start + len(drug)
                        tweet.pop(start, end, tweet.text[start: end], drug)
            else:
                # if (' ' + drug + ' ') in (' ' + tweet.text + ' '):
                #     for match in re.finditer(drug, tweet.text):
                #         tweet.pop(match.start(), match.end(),
                #                   tweet.text[int(match.start()): int(match.end())], drug)
                for word in tweet.text.split():
                    if word in self.lexicon.keys():
                        start = tweet.text.find(word)
                        end = start + len(word)
                        tweet.pop(start, end, tweet.text[start: end], word)
    def get_tweets(self):
        final = []
        for tweet in self.tweets:
            final.append(tweet.list())
        return final

    def positive_only(self):
        final = []
        for tweet in self.tweets:
            if tweet.contains_drug:
                final.append(tweet.list())
        return final

    def write_results(self, fpath):
        with open(fpath, 'w', newline='', encoding="utf") as file:
            writer = csv.writer(file, delimiter="\t", quoting=csv.QUOTE_NONE)
            file.write('tweet_id\tuser_id\tcreated_at\ttext\tstart\tend\tspan\tdrug\n')
            writer.writerows(self.get_tweets())
            file.close()

    def results(self):
        return '# of positive results: %s/%s' % (len(self.positive_only()), len(self.tweets))

