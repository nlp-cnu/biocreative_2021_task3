from tsv_reader import tsv_reader
import csv
import os

def wrong_annotations_creator(wrong_list, fname):
    fpath = os.path.join("data", fname)
    with open(fpath, 'wt') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['start', 'end', 'length', 'span', 'drug'])
        for example in wrong_list:
            writer.writerow(example)
        file.close()


if __name__ == "__main__":
    t0 = "BioCreative_TrainTask3.tsv"
    t1 = "BioCreative_TrainTask3.1.tsv"
    val = "BioCreative_ValTask3.tsv"

    anno = []
    for i in tsv_reader(t0):
        anno.append(i)
    for i in tsv_reader(t1):
        anno.append(i)
    for i in tsv_reader(val):
        anno.append(i)
    wrong_annotations_creator(anno, "wrong_annotations")

