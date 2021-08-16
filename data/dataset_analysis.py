import csv
import os

import emoji
import matplotlib.pyplot as plt
from nltk import TweetTokenizer
import numpy as np


from lexicon_app.Tweet import Tweet


def read_data(fpath):
    twt_list = []
    with open(fpath, 'rt', encoding="utf") as twt_file:
        reader = csv.reader(twt_file, delimiter="\t")
        for line in reader:
            if line[0] != "tweet_id":
                twt_list.append(Tweet(line[0], line[1], line[2], line[3]))
    return twt_list


def dataset_analysis(fpath):
    if fpath is None:
        print("No file given. Terminating")
        return

    tweets = read_data(fpath)
    num_tweets = len(tweets)
    num_emoji = sum([1 for x in tweets if any([1 for character in x.text if character in emoji.UNICODE_EMOJI['en']])])
    num_hashtag = sum([1 for x in tweets if '#' in x.text])
    num_user_mentions = sum([1 for x in tweets if '@' in x.text])
    num_url = sum([1 for x in tweets if 'http:/' in x.text or 'https:/' in x.text])
    tweet_tokenizer = TweetTokenizer()
    seq_lengths = [len(tweet_tokenizer.tokenize(x.text)) for x in tweets]
    fig, ax = plt.subplots(figsize=[12, 8])
    ax.hist(seq_lengths, bins=max(seq_lengths))
    ax.set_xlabel("Sequence Lengths")
    ax.set_ylabel("Count")
    plt.show()

    print("Percentage of tweets with an emoji = {}".format(num_emoji / num_tweets))
    print("Percentage of tweets with a hashtag = {}".format(num_hashtag / num_tweets))
    print("Percentage of tweets with a user mention = {}".format(num_user_mentions / num_tweets))
    print("Percentage of tweets with a hyperlink = {}".format(num_url / num_tweets))
    print("Mean number of tokens in tweet = {}".format(np.mean(seq_lengths)))
    print("Std. Dev. of number of tokens in tweet = {}".format(np.std(seq_lengths)))


if __name__ == "__main__":
    biocreative_train3_path = os.path.join("BioCreative_TrainTask3.tsv")
    biocreative_val3_path = os.path.join("BioCreative_ValTask3.tsv")

    print("Training data")
    dataset_analysis(biocreative_train3_path)
    print("Validation data")
    dataset_analysis(biocreative_val3_path)