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

with open("score_log.txt", "rt") as file:
    file.close()

#training as gold standard
training_goldstd = os.path.join("gold_std", "BioCreative_TrainTask3.tsv")
pred = os.path.join("test", "training_as_dict", "No_Stopwords_or_Subwords", "Train3.tsv")
score_task(pred, training_goldstd, "score_log.txt")
# score_task(os.path.join("test", "both_as_dict", "Subwords_only", "Val3.tsv"), training_goldstd, "score_log.txt")
# score_task(os.path.join("test", "both_as_dict", "Stopwords_only", "Val3.tsv"), training_goldstd, "score_log.txt")
# score_task(os.path.join("test", "both_as_dict", "Stopwords_and_Subwords", "Val3.tsv"), training_goldstd, "score_log.txt")
# with open(training_goldstd, "rt", encoding="utf") as goldstdfile:
#     reader1 = csv.reader(goldstdfile, delimiter="\t", lineterminator="\n")
#     with open(pred, "rt", encoding="utf") as predfile:
#         reader2 = csv.reader(predfile, delimiter="\t", lineterminator="\n")
#         num = 0
#         list1 = []
#         list2 = []
#         for line in reader1:
#             list1.append(line[3])
#         for line in reader2:
#             list2.append(line[3])
#         for i in range(len(list1)):
#                 item1 = list1[i]
#                 item2 = list2[i]
#
#                 if item1 == item2:
#                     print(item1, item2)
#                     print("mismatch at:", num)
#                 num+=1


