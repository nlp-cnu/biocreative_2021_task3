import os, csv

def tsv_reader(fname):
    fpath = os.path.join("data", fname)
    if not os.path.exists(fpath):
        print("file not found")
        return

    usr_id=[]
    twt_id=[]
    txt=[]
    num_positives = 0
    drugs=[]
    wrong_annotations = []
    pos_tweets = []

    with open(fpath, 'rt', encoding=("utf")) as file:
        reader = csv.reader(file, delimiter="\t")
        for line in reader:
            usr_id.append((line[0]))
            twt_id.append((line[1]))
            txt.append((line[2]))

            if line[0] != "tweet_id" and line[7] != "-":
                pos_tweets.append(line)
                drug = line[7]
                span = line[6]
                drugs.append(drug)
                num_positives += 1
                length = int(line[5]) - int(line[4])
                if length != len(str(drug)):
                    wrong_annotations.append([int(line[4]), int(line[5]), length, span, drug])
                                            #start, end, length, span, drug

        file.close()
        return pos_tweets


def read_rxnorm():
    """
    Reads drug listings from provided RXNORM file and returns them in a list
    :return:
    """
    with open("data\RXNORM.RRF", "rt") as rxfile:
        reader = csv.reader(rxfile, delimiter='|', lineterminator='\n')
        drugs_list = []
        for line in reader:
            drugs_list.append(line[14])
        rxfile.close()
    return drugs_list


def write_drugs(fname, drugs_list):
    """
    takes a list of drugs and writes them to a file for reference
    :param fname:
    :param drugs_list:
    :return:
    """
    fpath = os.path.join("lexicon_app", fname)
    with open(fpath, 'wt') as file:
        writer = csv.writer(file, delimiter="\n", quoting=csv.QUOTE_ALL)
        # drugs_list.sort()
        writer.writerow(drugs_list)


if __name__ == "__main__":
    t0 = "BioCreative_TrainTask3.tsv"
    t1 = "BioCreative_TrainTask3.1.tsv"
    val = "BioCreative_ValTask3.tsv"

    drugs_train0 = tsv_reader(t0)
    drugs_train1 = tsv_reader(t1)
    drugs_rxnorm = read_rxnorm()
    drugs = []

    # for i in drugs_train0:
    #     drugs.append(i)
    #
    # for j in drugs_train1:
    #     if j not in drugs:
    #         drugs.append(j)
    #
    # # for x in drugs_rxnorm:
    # #     # if x not in drugs:
    # #     drugs.append(x)
    #
    #
    # write_drugs("Training_only.csv", drugs)

