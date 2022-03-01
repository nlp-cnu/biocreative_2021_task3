from includes.implementation import implementation
from eval.Evaluation import score_task
import os

#TODO - Fix the stopwords param in the implementation code

"""
CONFIG - Modifying the program using test cases to achieve better scores

GOLD STD: BioCreative_TrainTask3.tsv
Generated file ConfigPred.tsv with predictions from implementation.py
"""
"""
implementation(data, lex, stop_words_bool, subwords_bool, pred_name):

@param data: "t0", "t1", or "val" - indicate which data file is being tested
@param lex: "Training", "RXNORM" or "Both" - indicate which lexicons to predictions with

"""
"""
**For the sake of this configuration, and since I don't have the original data files available,
implementation step 1 has been altered to just accept a file path as the first parameter to analyze

"""

with open("log.txt", "w") as log:
    log.write(implementation("Train3.tsv", "Training", False, False, "ConfigPred.tsv"))
    log.write(implementation("Train3.tsv", "Training", False, True, "ConfigPred.tsv"))
    log.write(implementation("Train3.tsv", "Training", True, False, "ConfigPred.tsv"))
    log.write(implementation("Train3.tsv", "Training", True, True, "ConfigPred.tsv"))
    log.close()

"""
def score_task(pred_file, gold_file, out_file):
    Score the predictions and print scores to files
    Arguments:
        pred_file {string} -- path to the predictions file
        gold_file {string} -- path to the gold annotation file
        out_file {string} -- path to the file to write results to

"""
score_task("../predictions/training_as_dict/No_Stopwords_or_Subwords/ConfigPred.tsv", "BioCreative_TrainTask3.tsv", "log.txt")
score_task("../predictions/training_as_dict/Stopwords_only/ConfigPred.tsv", "BioCreative_TrainTask3.tsv", "log.txt")
score_task("../predictions/training_as_dict/Subwords_only/ConfigPred.tsv", "BioCreative_TrainTask3.tsv", "log.txt")
score_task("../predictions/training_as_dict/Stopwords_and_Subwords/ConfigPred.tsv", "BioCreative_TrainTask3.tsv", "log.txt")




