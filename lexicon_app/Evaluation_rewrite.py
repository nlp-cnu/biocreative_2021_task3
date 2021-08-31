from lexicon_app.eval.Evaluation import score_task
import os
"""
def score_task(pred_file, gold_file, out_file):
    Score the predictions and print scores to files
    Arguments:
        pred_file {string} -- path to the predictions file
        gold_file {string} -- path to the gold annotation file
        out_file {string} -- path to the file to write results to
    
"""

with open("score_log.txt", "rt") as file:
    file.close()

#training as gold standard
training_goldstd = os.path.join("gold_std", "BioCreative_ValTask3")
score_task(os.path.join("test", "training_as_dict", "No_Stopwords_or_Subwords", "Train3.tsv"), training_goldstd, "score_log.txt")