# -*- coding: utf-8 -*-
"""MyMachineLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11YyHuCDetXp4_agN-wNpEn1XUuYMaFVK
"""



"""## **IMPORTANT: MUST ENABLE GPU -- Runtime->Change Runtime Type->Hardware Accelerator->GPU**

Install Dependencies (only needs to get run once)
"""

#pip install transformers

#!pip install tensorflow_addons
#!pip install keras_metrics

"""Set Up Drive and Mount Keras Examples"""


import sys
import csv

import transformers as tf
from keras_examples.Classifier import *
from keras_examples.Dataset import *
import pandas as pd
import tensorflow_addons as tfa

class NERDataset(Binary_Text_Classification_Dataset):

      def __init__(self, data_file_path, text_column_name=None, label_column_name=None, label_column_names=None, seed=SEED, validation_set_size=0):
        Dataset.__init__(self, seed=seed, validation_set_size=validation_set_size)

        # dataframe = pd.read_csv(data_file_path, delimiter="\t")

        # poplist = dataframe['start'].values.tolist()
        # labels = []
        # for i in poplist:
        #   if i != "-":
        #     labels.append(1)
        #   else:
        #     labels.append(0)


        data = []
        labels = []

        twt_list = []
        with open(data_file_path, 'rt', encoding=("utf")) as twt_file:
            reader = csv.reader(twt_file, delimiter="\t")
            for line in reader:
                if line[0] != "tweet_id":
                    data.append(line[3])
                    if line[4] != "-":
                      labels.append(1)
                    else:
                      labels.append(0)

        #data = np.array(data)
        print("type(data[0]) = " + str(type(data[0])))


        labels = np.array(labels)
        #print(str(data))
        #print(str(labels))
        print(len(data))
        print(labels.shape)
        self._training_validation_split(data, labels)
        self._determine_class_weights()

class My_Custom_Classifier(Binary_Text_Classifier):

    def __init__(self, language_model_name, num_classes, language_model_trainable=False, max_length=Classifier.MAX_LENGTH, learning_rate=Classifier.LEARNING_RATE, dropout_rate=Classifier.DROPOUT_RATE):
        
        Classifier.__init__(self, language_model_name, language_model_trainable=language_model_trainable, max_length=max_length, learning_rate=learning_rate, dropout_rate=dropout_rate)
        self._num_classes = num_classes
        
        #create the model
        #create the input layer, it contains the input ids (from tokenizer) and the
        # the padding mask (which masks padded values)
        input_ids = Input(shape=(None,), dtype=tf.int32, name="input_ids")
        input_padding_mask = Input(shape=(None,), dtype=tf.int32, name="input_padding_mask")
 
        # create the language model
        language_model = self.load_language_model()
        
        #create the embeddings - the 0th index is the last hidden layer
        embeddings = language_model(input_ids=input_ids, attention_mask=input_padding_mask)[0]
        sentence_representation = embeddings[:,0,:]
        
        #now, create some dense layers
        #dense
        dense1 = tf.keras.layers.Dense(64, activation='gelu')
        dropout1 = tf.keras.layers.Dropout(self._dropout_rate)
        output1 = dropout1(dense1(sentence_representation))

        #sigmoid layer
        sigmoid_layer = tf.keras.layers.Dense(self._num_classes, activation='sigmoid')
        final_output = sigmoid_layer(output1)
    
        #combine the language model with the classificaiton part
        self.model = Model(inputs=[input_ids, input_padding_mask], outputs=[final_output])
        
        #create the optimizer
        optimizer = tf.keras.optimizers.Adam(lr=self._learning_rate)
        metrics =[tfa.metrics.F1Score(1), tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]

        #compile the model
        self.model.compile(
            optimizer=optimizer,
            loss='binary_crossentropy',
            metrics=metrics
        )

"""Set up and run the experment"""
if __name__ == "__main__":
    # training parameters
    max_epoch = 100
    batch_size = 200
    early_stopping_patience = 5
    early_stopping_monitor = 'f1'

    # model hyperparameters
    learning_rate = 0.01
    dropout_rate = 0.8
    language_model_trainable = True

    # parameters to load and save a model
    model_in_file_name = "my_models/model_out_trainable_true" # to load a model, need to uncomment some code below
    model_out_file_name = "/content/drive/My Driver/NER_Colab/my_models/modelout" # to save a model, need to uncomment some code below

    #set up the language model
    # language_model_name = '/content/drive/My Drive/colab_stuff/models/NCBI_BERT_pubmed_mimic_uncased_L-12_H-768_A-12'
    language_model_name = 'bert-base-uncased'
    max_length = 512

    #load the dataset
    #data_filepath = '/content/drive/My Drive/Student_Research/Relationship_Extraction/i2b2_training_data/keras_converted_format/i2b2_converted_filtered.tsv'
    #data_filepath = '/content/drive/My Drive/colab_stuff/data/i2b2_relex/i2b2_converted.tsv'
    # data_filepath = '/content/drive/My Drive/NER_Colab/BioCreative_TrainTask3.tsv'
    data_filepath = '../data/BioCreative_TrainTask3.tsv'


    num_classes = 1
    data = NERDataset(data_filepath, validation_set_size=0.2)
    #data = i2b2Dataset(data_filepath)
    #exit()

    train_x, train_y = data.get_train_data()
    val_x, val_y = data.get_validation_data()

    #TODO @john - next, you need to do some hyperparameter tuning to optimize the performance of your model

    """
    Best F1 performance below:
 lr: 0.000100, dropout: 0.800000
    """

    # learning_rates = [0.000001, 0.00001,  0.0001, 0.001, 0.01, 0.1]
    learning_rates = [0.0001]
    # dropout_rates = [0.0, 0.4, 0.8]
    dropout_rates = [0.8]
    for lr in learning_rates:
      for dropout in dropout_rates:
        print("Classifier with lr = " + str(lr) + ", " + " dropout_rate = " + str(dropout))
    # .   classifier = create classifier   (pass in params)
        classifier = My_Custom_Classifier(language_model_name, num_classes,
                                            max_length=max_length,
                                            learning_rate=lr,
                                            language_model_trainable=language_model_trainable,
                                            dropout_rate=dropout)

        # # classifier.train(pass in params)
        # classifier.train(train_x, train_y,
        #             validation_data=(val_x, val_y),
        #             model_out_file_name=model_out_file_name,
        #             epochs=max_epoch)
        classifier.train(train_x, train_y,
                      validation_data=(val_x, val_y),
                      epochs=max_epoch,
                      batch_size=batch_size,
                      # model_out_file_name=model_out_file_name,
                      # early_stopping_patience=5,
                      # early_stopping_monitor=early_stopping_monitor,
                      class_weights=data.get_train_class_weights()
        )


    #create classifier and load data for a multiclass text classifier


    #load a model's weights from file, use this code
    #classifier.load_weights(model_in_file_name)

    # #get the training data
    # train_x, train_y = data.get_train_data()
    # val_x, val_y = data.get_validation_data()


    # #train the model
    # # If you want to save model weights, use below.
    # #classifier.train(train_x, train_y,
    # #                 validation_data=(val_x, val_y),
    # #                 model_out_file_name=model_out_file_name,
    # #                 epochs=max_epoch)
    # classifier.train(train_x, train_y,
    #                   validation_data=(val_x, val_y),
    #                   epochs=max_epoch,
    #                   batch_size=batch_size,
    #                   #model_out_file_name=model_out_file_name,
    #                   early_stopping_patience=5, early_stopping_monitor=early_stopping_monitor,
    #                   # class_weights=data.get_train_class_weights()
    # )
