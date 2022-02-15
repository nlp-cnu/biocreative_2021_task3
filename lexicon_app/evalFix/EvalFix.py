import csv

from eval.Evaluation import score_task
import os
"""
def score_task(pred_file, gold_file, out_file):
    Score the predictions and print scores to files
    Arguments:
        pred_file {string} -- path to the predictions file
        gold_file {string} -- path to the gold annotation file
        out_file {string} -- path to the file to write results to
    
"""

with open("evalFix/score_log.txt", "wt") as file:
    file.close()

SCORE_LOG = "evalFix/score_log.txt"
training_goldstd = "gold_std/BioCreative_TrainTask3.tsv"
val_goldstd = "gold_std/BioCreative_ValTask3.tsv"

files = ["Train3.tsv", "Val3.tsv"]
predictions = ["training_as_dict", "rxnorm_as_dict", "both_as_dict"]
params = ["No_Stopwords_or_Subwords", "Stopwords_and_Subwords", "Stopwords_only", "Subwords_only"]




#EVALUATING TRAINING FILES
open(SCORE_LOG, "at").write("-------------------\nTRAINING FILES EVALUATIONS\n")
for prediction in predictions:
    open(SCORE_LOG, "at").write("\n" + prediction + "\n")
    for param in params:
        open(SCORE_LOG, "at").write(param+ "\n")
        score_task(os.path.join("predictions", prediction, param, files[0]), training_goldstd, SCORE_LOG)

#EVALUATING VAL FILES
open(SCORE_LOG, "at").write("\n\n-------------------\nVAL FILES EVALUATIONS\n")
for prediction in predictions:
    open(SCORE_LOG, "at").write("\n" + prediction+ "\n")
    for param in params:
        open(SCORE_LOG, "at").write(param+ "\n")
        score_task(os.path.join("predictions", prediction, param, files[1]), val_goldstd, SCORE_LOG)



