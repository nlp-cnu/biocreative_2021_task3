import os
import csv
from tsv_reader import tsv_reader


def positive_only(positive_tweets, total):
    fpath = os.path.join("data", "positive_only.tsv")
    # with open(fpath, 'wt', encoding='utf-8') as file:
    #     writer = csv.writer(file, delimiter='\t')
    #     writer.writerow([total])
    #     writer.writerow(['tweet_id', 'user_id', 'created_at', 'text', 'start', 'end', 'span', 'drug'])
    for tweet in positive_tweets:
        if tweet.contains_drug:
            print(tweet.list)


if __name__ == '__main__':
    pos_tweets = []
    t0 = "BioCreative_TrainTask3.tsv"
    t1 = "BioCreative_TrainTask3.1.tsv"
    val = "BioCreative_ValTask3.tsv"
    new = os.path.join("rxnorm_as_dict", "No_Stopwords_or_Subwords", "Train3.0.tsv")

    total = 0
    for tweet in tsv_reader(new):
        pos_tweets.append(tweet)
        total +=1
    # for tweet in tsv_reader(t1):
    #     pos_tweets.append(tweet)
    # for tweet in tsv_reader(val):
    #     pos_tweets.append(tweet)
    positive_only(pos_tweets, total)
