import os
import csv
from tsv_reader import tsv_reader


def positive_only(positive_tweets):
    fpath = os.path.join("data", "positive_only.tsv")
    with open(fpath, 'wt', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['tweet_id', 'user_id', 'created_at', 'text', 'start', 'end', 'span', 'drug'])
        for tweet in positive_tweets:
            writer.writerow(tweet)


if __name__ == '__main__':
    pos_tweets = []
    t0 = "BioCreative_TrainTask3.0.tsv"
    t1 = "BioCreative_TrainTask3.1.tsv"
    for tweet in tsv_reader(t0):
        pos_tweets.append(tweet)
    for tweet in tsv_reader(t1):
        pos_tweets.append(tweet)
    positive_only(pos_tweets)