# Data Processor works for loading and preprocessing, format and split etc.

import scipy.io
import numpy as np
import pickle

from config import encodeLabel
from config import EMOTION_AMOUNT

# Load data from .mat datafile
def readDataFromMat(file_name):
    print("read data: " + file_name)
    raw_data_X = scipy.io.loadmat(file_name)['x'].tolist()
    raw_data_Y = scipy.io.loadmat(file_name)['y'].tolist()

    # transfer the y(label) date into one hot encoding, i.e. 1*6 list
    num_of_rows = len(raw_data_Y)
    new_data_list_Y = np.zeros((num_of_rows, EMOTION_AMOUNT), int)
    for row in range(new_data_list_Y.shape[0]):
        new_data_list_Y[row] = encodeLabel(raw_data_Y[row][0])
        
    return (raw_data_X, new_data_list_Y.tolist())

# Split and divide
# return the dataset corresponding to the given param 'fold' index
# of the total number of division 'fold_num'
def crossValidation(dataset, fold, fold_num):
    samples = dataset[0]
    labels = dataset[1]

    fold_unit_amount = int(len(dataset[0]) / float(fold_num))
    start = (fold) * fold_unit_amount
    end = start + fold_unit_amount
    
    train_samples = samples[0:start] + samples[end:-1]
    train_labels = labels[0:start] + labels[end:-1]
    train_list = [train_samples, train_labels]
    
    test_list = [samples[start:end], labels[start:end]]
    return (train_list,test_list)

#make the subdataset based on the states of given attribute
def subDataset(dataset, attr):
    # store the samples for attribute with value 1
    sub_1 = [[], []]
    # store the samples for attribute with value 0
    sub_0 = [[], []]
    for idx, sample in enumerate(dataset[0]):
        attr_value = sample[attr]
        label = dataset[1][idx]
        if attr_value == 1:
            sub_1[0].append(sample)
            sub_1[1].append(label)
        else:
            sub_0[0].append(sample)
            sub_0[1].append(label)

    return (sub_0, sub_1)

#save objects to a binary file
def saveObjects(objects):
    file_name = 'decision_tree.pkl'
    with open(file_name, 'wb') as f:
        pickle.dump(objects,f)
    return file_name

#retrive objects from a binary file
def retrieveObjects(file_name):
    # retrieve objects from the saved binary files
    with open(file_name,'rb') as f:
        objects = pickle.load(f)
    return objects
