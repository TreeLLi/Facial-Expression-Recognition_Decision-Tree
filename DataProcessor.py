# Data Processor works for loading and preprocessing, format and split etc.

import scipy.io
import numpy as np

# Load data
        
def readDataFromMat(file_name):
    print("read data: " + file_name)
    raw_data_X = scipy.io.loadmat(file_name)['x'].tolist() #transfer data from first mat table to list
    raw_data_Y = scipy.io.loadmat(file_name)['y'].tolist() #transfer data from second mat table to list
    num_of_rows = len(raw_data_Y)                          #calculate number of rows
    new_data_list_Y = np.zeros(num_of_rows, int)             #create a new 1*n list initilized with all zero
    for row in range(new_data_list_Y.shape[0]): #read every element of the two-dimensional list, and put it in a 1*n list
        new_data_list_Y[row] = raw_data_Y[row][0]
    return (raw_data_X, new_data_list_Y.tolist())

# Split and divide
def crossValidation(dataset, fold, fold_num): # fold: current test fold no, fold_num: fold value
    fold_unit_amount = int(len(dataset[0]) / float(fold_num))#total length of dataset X divided by the fold value
    start = (fold-1) * fold_unit_amount                         #the starting row based on fold no
    end = start + fold_unit_amount                          #starting row + unit length
    samples = dataset[0]
    labels = dataset[1]
    train_samples = samples[0:start] + samples[end:-1]      #combine other rows of data except the folding rows
    train_labels = labels[0:start] + labels[end:-1]
    train_list = [train_samples, train_labels]            #combine folding samples list and labels list as a traing list
    test_list = [samples[start:end], labels[start:end]]   #combine rest lists as a testing list
    return (train_list,test_list)


def subDataset(dataset, attr):
    sub_1 = [[], []]
    sub_0 = [[], []]
    for idx, sample in enumerate(dataset[0]): #idx:index sample:element, reading through every row
        attr_value = sample[attr-1] #look at specific attribute value based on the index 'attr'
        label = dataset[1][idx]     #find the corresponding label of that attr
        if attr_value == 1:         #if attribute value is 1, append to sub_1
            sub_1[0].append(sample)
            sub_1[1].append(label)
        else:                       #if attribute value is 0, append to sub_0
            sub_0[0].append(sample)
            sub_0[1].append(label)

    return (sub_0, sub_1)
