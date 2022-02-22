import os
import csv
from tsv_reader import tsv_reader


def positive_only(positive_tweets):
    fpath = os.path.join("../../data", "positive_only.tsv")
    # with open(fpath, 'wt', encoding='utf-8') as file:
    #     writer = csv.writer(file, delimiter='\t')
    #     writer.writerow([total])
    #     writer.writerow(['tweet_id', 'user_id', 'created_at', 'text', 'start', 'end', 'span', 'drug'])
    final = 0
    for tweet in positive_tweets:
        if tweet.contains_drug:
            final += 1
    return final


if __name__ == '__main__':
    pos_tweets = []
    t0 = os.path.join("..", "gold_std", "BioCreative_TrainTask3.tsv")
    t1 = "BioCreative_TrainTask3.1.tsv"
    val = "BioCreative_ValTask3.tsv"
    new = os.path.join("rxnorm_as_dict", "No_Stopwords_or_Subwords", "Train3.0.tsv")

    total = 0
    # print(tsv_reader(t0))
    print(os.path.isdir(t0))