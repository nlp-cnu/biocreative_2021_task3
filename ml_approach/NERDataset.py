from keras_examples.Dataset import *
import csv
import random


class NERDataset(Binary_Text_Classification_Dataset):

    def __init__(self, data_file_path, text_column_name=None, label_column_name=None, label_column_names=None,
                 seed=SEED, validation_set_size=0, pre_undersample=False):
        Dataset.__init__(self, seed=seed, validation_set_size=validation_set_size)

        data = []
        labels = []

        with open(data_file_path, 'rt', encoding=("utf")) as twt_file:
            reader = csv.reader(twt_file, delimiter="\t")
            for line in reader:
                if line[0] != "tweet_id":
                    data.append(line[3])
                    if line[4] != "-":
                        labels.append(1)
                    else:
                        labels.append(0)

        if pre_undersample:
            #code that deletes negative tweets at random
            pos_ct = 0
            for i in labels:
                pos_ct += i

            while len(data) > 2*pos_ct:
                r = random.randrange(len(data))
                if labels[r] == 0:
                    data.pop(r)
                    labels.pop(r)

        # print(pos_ct)
        # print("type(data[0]) = " + str(type(data[0])))
        # print(data)
        # print(labels)
        #
        # # print(str(data))
        # # print(str(labels))
        # # print(len(data))

        labels = np.array(labels)
        print(labels.shape)
        self._training_validation_split(data, labels)
        self._determine_class_weights()


if __name__ == "__main__":
    data = NERDataset('../data/BioCreative_TrainTask3.tsv', validation_set_size=0.2, pre_undersample=True)
