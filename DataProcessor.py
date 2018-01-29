# Data Processor works for loading and preprocessing, format and split etc.
import scipy.io
import numpy as np
import math
import copy
# Load data
        
def readDataFromMat(file_name):
    print("read data: " + file_name)
    cleanDataX = scipy.io.loadmat(file_name)['x']
    cleanDataY = scipy.io.loadmat(file_name)['y']
    num_of_rows = len(cleanDataY)
    #print(num_of_rows)
    newcleandataY = np.zeros((num_of_rows,6),int)
    for row in range(newcleandataY.shape[0]):
        col  = cleanDataY[row]-1
        newcleandataY[row][col] = 1
    return (cleanDataX, newcleandataY)
# Split and divide

def crossValidation(dataset, fold, fold_num):
    set_length=len(dataset) / float(fold_num)
    n = int(math.ceil(set_length))
    set_no = (fold-1)*n
    train_list = copy.deepcopy(dataset[set_no:set_no+n])
    test_list = copy.deepcopy(dataset)
    del test_list[set_no:set_no+n]

    # return (train_list, test_list)
    # train_list is [[x-samples:N*45], [y-labels:1*N]]
    return (train_list,test_list)

def subDataset(dataset, attr):
    dataset_tmp = copy.deepcopy(dataset)
    dataset_tmp.sort( key=lambda attribute:attribute[attr-1])
    count = 0
    for i in dataset_tmp:
        if i[attr-1] == 1:
            break
        count = count+1
    zero_dataset = dataset_tmp[0:count]
    first_dataset = dataset_tmp[count:]
    return [zero_dataset, first_dataset]