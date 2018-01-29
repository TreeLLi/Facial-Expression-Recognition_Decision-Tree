# Data Processor works for loading and preprocessing, format and split etc.

import scipy.io
import numpy as np
import math
import copy
# Load data
        
def readDataFromMat(file_name):
    print("read data: " + file_name)
    cleanDataX = scipy.io.loadmat(file_name)['x'].tolist()
    cleanDataY = scipy.io.loadmat(file_name)['y'].tolist()
    num_of_rows = len(cleanDataY)
    #print(num_of_rows)
    newcleandataY = np.zeros(num_of_rows,int)
    for row in range(newcleandataY.shape[0]):
        newcleandataY[row] = cleanDataY[row][0]
    return (cleanDataX, newcleandataY.tolist())
# Split and divide

def crossValidation(dataset, fold, fold_num):
    # set_length=len(dataset) / float(fold_num)
    # n = int(math.ceil(set_length))
    # set_no = (fold-1)*n
    # train_list = copy.deepcopy(dataset[set_no:set_no+n])
    # test_list = copy.deepcopy(dataset)
    # del test_list[0][set_no:set_no+n]
    # del test_list[1][set_no:set_no+n]

    fold_unit_amount = int(len(dataset[0]) / float(fold_num))
    start = fold * fold_unit_amount
    end = start + fold_unit_amount
    samples = dataset[0]
    labels = dataset[1]
    train_samples = samples[0:start] + samples[end:-1]
    train_labels = labels[0:start] + labels[end:-1]
    train_list = [train_samples, train_labels]
    test_list = [samples[start:end], labels[start:end]]
    
    # return (train_list, test_list)
    # train_list is [[x-samples:N*45], [y-labels:1*N]]
    return (train_list,test_list)

def subDataset(dataset, attr):
    # dataset_tmp = copy.deepcopy(dataset)
    # dataset_tmp.sort( key=lambda attribute:attribute[attr-1])
    # count = 0
    # for i in dataset_tmp:
    #     if i[attr] == 1:
    #         break
    #     count = count+1
    # zero_dataset = dataset_tmp[0:count]
    # first_dataset = dataset_tmp[count:]
    sub_1 = []
    sub_0 = []
    for idx, sample in dataset[0]:
        
    return [zero_dataset, first_dataset]
