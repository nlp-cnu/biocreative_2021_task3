import os, csv
from Tweet import Tweet
from Dataset import Dataset

"""
@param data: "t0", "t1", or "val" - indicate which data file is being tested
@param lex: "Training", "RXNORM" or "Both" - indicate which lexicon to test with
@param stop_words_bool: include stop words (shot and pill) in search or not
@param subword_bool: include subwords ("pill" in "pillow") in search or not
@param pred_name: name of predictions file being written to
returns: string : "# of positive results: _ out of _"
"""


def implementation(data, lex, stop_words_bool, subwords_bool, pred_name):

    """
    Implementation script of lexicon approach to BioCreative Task 3
    Steps to Implement:
    1) Create list of Tweet objects from file reading, following parameters Tweet(twid, userid, created, text)
    """
    if data == "t0":
        fpath = os.path.join("data", "BioCreative_TrainTask3.tsv")
    elif data == "t1":
        fpath = os.path.join("data", "BioCreative_TrainTask3.1.tsv")
    elif data == "val":
        fpath = os.path.join("data", "BioCreative_ValTask3.tsv")
    else:
        print("Incorrect data: Use t0, t1, or val")
        return

    twt_list = []
    with open(fpath, 'rt', encoding=("utf")) as twt_file:
        reader = csv.reader(twt_file, delimiter="\t")
        for line in reader:
            if line[0] != "tweet_id":
                twt_list.append(Tweet(line[0], line[1], line[2], line[3]))

    """
    2) Create Dataset(tweets, lex_fpath, lex_delim) where
        tweets: list of Tweet objects
        lex_fpath: file path of lexicon file
        lex_delim: delimiter for reading lexicon file
    """

    #make directories
    if not os.path.isdir(os.path.join("lexicon_app", "test")):
         os.mkdir(os.path.join("lexicon_app", "test"))

    
    if lex == "Training":
        dict_file = os.path.join("lexicon_app", "Training_only.csv")
        pred_dir = os.path.join("lexicon_app", "test", "training_as_dict")
        if not os.path.isdir(pred_dir):
            os.mkdir(pred_dir)
    elif lex == "RXNORM":
        dict_file = os.path.join("lexicon_app", "RXNORM_only.csv")
        pred_dir = os.path.join("lexicon_app", "test", "rxnorm_as_dict")
        if not os.path.isdir(pred_dir):
            os.mkdir(pred_dir)
    elif lex == "Both":
        dict_file = os.path.join("lexicon_app", "Training_and_RXNORM.csv")
        pred_dir = os.path.join("lexicon_app", "test", "both_as_dict")
        if not os.path.isdir(pred_dir):
            os.mkdir(pred_dir)
    else:
        print("Incorrect dict file: Use Training, RXNORM or Both")
        return

    run = Dataset(twt_list, dict_file, '\n')
    """
    3) Call Dataset.check() to perform check on all tweets using lexicon, updating each
        positive result with necessary info, and setting tweet.contains_drug = True
        (*most time-consuming step*)
    """
    if stop_words_bool and subwords_bool:
        pred_dir = os.path.join(pred_dir, "Stopwords_and_Subwords")
    elif stop_words_bool:
        pred_dir = os.path.join(pred_dir, "Stopwords_only")
    elif subwords_bool:
        pred_dir = os.path.join(pred_dir, "Subwords_only")
    else:
        pred_dir = os.path.join(pred_dir, "No_Stopwords_or_Subwords")
    run.check(subwords_bool, stop_words_bool)
    """
    4) Call:
        - Dataset.get_tweets(): returns list of all tweets with positive results updated
        - Dataset.positive_only(): returns list of only positive result tweets
        - Dataset.write_results(fpath): with fpath as the desired file path, writes csv format
            of all tweets with positive results updated
    """
    if not os.path.isdir(pred_dir):
        os.mkdir(pred_dir)
    run.write_results(os.path.join(pred_dir, pred_name))

    return pred_name + "\t%s\t%r\t%r\t" %\
        (lex, stop_words_bool, subwords_bool) + run.results() + "\n"

    # with open(os.path.join("test", "Lexicon_Data.log"), "wt") as file:
    #     file.write("Data Log for Lexicon Results:")
    #     file.write("Training3.0 with Training as Dictionary:")
    #     file.write(run.print_results())
    #     file.close()
