import os
from includes.implementation import implementation
'''
src.py IS THE EXECUTION FILE FOR THE LEXICON APPROACH, RUN THIS FILE AFTER SETTING
APPROPRIATE RUN INSTANCES
'''
"""
implementation(data, lex, stop_words_bool, subwords_bool, pred_name):

@param data: "t0", "t1", or "val" - indicate which data file is being tested
@param lex: "Training", "RXNORM" or "Both" - indicate which lexicons to predictions with

"""
# training_as_dict = os.path.join("lexicon_app", "predictions", "training_as_dict")
# rxnorm_as_dict = os.path.join("lexicon_app", "predictions", "rxnorm_as_dict")
# both_as_dict = os.path.join("lexicon_app", "predictions", "both_as_dict")
# subdirs = ["Stopwords_and_Subwords", "Stopwords_only", "Subwords_only", "No_Stopwords_or_Subwords"]
# for i in subdirs:
#     os.mkdir(os.path.join(training_as_dict, i))
#     os.mkdir(os.path.join(rxnorm_as_dict, i))
#     os.mkdir(os.path.join(both_as_dict, i))
if __name__ == "__main__":
    log = "data_log.txt"
    with open(log, "r") as file:
        file.close()
    with open(log, "w") as file:
        file.write("NAME\tLEXICON\tSTOP WORDS\tSUBWORDS\tRESULTS\n")
        file.close()

    with open(log, "a") as file:
        # FOR REFERENCE: implementation(data, lex, stop_words_bool, subwords_bool, pred_name)

        for dict in ["Training", "RXNORM", "Both"]:
            file.write(implementation("t0", dict, False, False, "Train3.tsv"))
            file.write(implementation("t0", dict, False, True, "Train3.tsv"))
            file.write(implementation("t0", dict, True, False, "Train3.tsv"))
            file.write(implementation("t0", dict, True, True, "Train3.tsv"))

            file.write(implementation("val", dict, False, False, "Val3.tsv"))
            file.write(implementation("val", dict, False, True, "Val3.tsv"))
            file.write(implementation("val", dict, True, False, "Val3.tsv"))
            file.write(implementation("val", dict, True, True, "Val3.tsv"))



        # file.write(implementation("t0", "Training", False, False, "Train3.tsv"))
        # file.write(implementation("t0", "Training", True, False, "Train3.tsv"))
        #
        # file.write(implementation("val", "Training", False, False, "Val3.tsv"))
        # file.write(implementation("val", "Training", True, False, "Val3.tsv"))
        #
        # file.write(implementation("t0", "RXNORM", False, False, "Train3.tsv"))
        # file.write(implementation("t0", "RXNORM", True, False, "Train3.tsv"))
        #
        # file.write(implementation("val", "RXNORM", False, False, "Val3.tsv"))
        # file.write(implementation("val", "RXNORM", True, False, "Val3.tsv"))
        #
        # file.write(implementation("t0", "Both", False, False, "Train3.tsv"))
        # file.write(implementation("t0", "Both", True, False, "Train3.tsv"))
        #
        # file.write(implementation("val", "Both", False, False, "Val3.tsv"))
        # file.write(implementation("val", "Both", True, False, "Val3.tsv"))
        #
        #
        # #### Test with subword matching
        # file.write(implementation("t0", "Training", False, True, "Train3.tsv"))
        # file.write(implementation("t0", "Training", True, True, "Train3.tsv"))
        #
        # file.write(implementation("val", "Training", False, True, "Val3.tsv"))
        # file.write(implementation("val", "Training", True, True, "Val3.tsv"))
        #
        # file.write(implementation("t0", "RXNORM", False, True, "Train3.tsv"))
        # file.write(implementation("t0", "RXNORM", True, True, "Train3.tsv"))
        #
        # file.write(implementation("val", "RXNORM", False, True, "Val3.tsv"))
        # file.write(implementation("val", "RXNORM", True, True, "Val3.tsv"))
        #
        # file.write(implementation("t0", "Both", False, True, "Train3.tsv"))
        # file.write(implementation("t0", "Both", True, True, "Train3.tsv"))
        #
        # file.write(implementation("val", "Both", False, True, "Val3.tsv"))
        # file.write(implementation("val", "Both", True, True, "Val3.tsv"))


