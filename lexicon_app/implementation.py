import os, csv
from Tweet import Tweet
from Dataset import Dataset
"""
Implementation script of lexicon approach to BioCreative Task 3
Steps to Implement:
1) Create list of Tweet objects from file reading, following parameters Tweet(twid, userid, created, text)
"""
t0 = os.path.join("data", "BioCreative_TrainTask3.0.tsv")
t1 = os.path.join("data", "BioCreative_TrainTask3.1.tsv")
val = os.path.join("data", "BioCreative_ValTask3.tsv")


twt_list = []
with open(val, 'rt', encoding=("utf")) as twt_file:
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
t_only = os.path.join("lexicon_app", "Training_only.csv")
run = Dataset(twt_list, t_only, '\n')
"""
3) Call Dataset.check() to perform check on all tweets using lexicon, updating each
    positive result with necessary info, and setting tweet.contains_drug = True
    (*most time-consuming step*)
"""
run.check()
"""
4) Call:
    - Dataset.get_tweets(): returns list of all tweets with positive results updated
    - Dataset.positive_only(): returns list of only positive result tweets
    - Dataset.write_results(fpath): with fpath as the desired file path, writes csv format
        of all tweets with positive results updated
"""
run.write_results(os.path.join("lexicon_app", "test", "ValTask3.0_UsingTrainingOnly.tsv"))
run.print_results()
# with open(os.path.join("test", "Lexicon_Data.log"), "wt") as file:
#     file.write("Data Log for Lexicon Results:")
#     file.write("Training as Dictionary:")
#     file.write(run.print_results())
#     file.close()