import os, csv


def tsv_reader(fname):
    fpath = os.path.join("data", fname)
    print("path:", fpath)
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
                    wrong_annotations.append("'%s' becomes '%s'" % (span, drug))

        file.close()
        return pos_tweets


def write_drugs(fname, drugs_list):
    fpath = os.path.join("data", fname)
    with open(fpath, 'wt') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        drugs_list.sort()
        drugs_nd = []
        [drugs_nd.append(x) for x in drugs_list if x not in drugs_nd]
        writer.writerow(drugs_nd)


# if __name__ == "__main__":
#     t0 = "BioCreative_TrainTask3.0.tsv"
#     t1 = "BioCreative_TrainTask3.1.tsv"
#     val = "BioCreative_ValTask3.tsv"
#
#     drugs_train0 = tsv_reader(t0)
#     drugs_train1 = tsv_reader(t1)
#     drugs = []
#
#     for i in drugs_train0:
#         drugs.append(i)
#
#     for j in drugs_train1:
#         if j not in drugs:
#             drugs.append(j)
#
#     write_drugs("Drugs_Database", drugs)
#
#     tsv_reader(t0)
