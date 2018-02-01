# Data Processor works for loading and preprocessing, format and split etc.
import scipy.io #scipy: 0.17.0
import numpy as np #numpy: 1.11.0
import pickle #protocol version type:3.0
# Load data
def readDataFromMat(file_name):
    print("read data: " + file_name)
    raw_data_X = scipy.io.loadmat(file_name)['x'].tolist() #transfer data from mat table to list
    raw_data_Y = scipy.io.loadmat(file_name)['y'].tolist()
    num_of_rows = len(raw_data_Y)
    new_data_list_Y = np.zeros(num_of_rows, int)     #create a new 1*n list initilized with all zero
    # read every element of the two-dimensional list, and put it in 1*n list
    for row in range(new_data_list_Y.shape[0]):
        new_data_list_Y[row] = raw_data_Y[row][0]
    return (raw_data_X, new_data_list_Y.tolist())

# Split and divide
def crossValidation(dataset, fold, fold_num): # fold: current test fold no, fold_num: fold value
    fold_unit_amount = int(len(dataset[0]) / float(fold_num))
    start = (fold) * fold_unit_amount                     #the starting row based on fold no
    end = start + fold_unit_amount
    samples = dataset[0]
    labels = dataset[1]
    #categorize the train_list and test_list
    train_samples = samples[0:start] + samples[end:-1]
    train_labels = labels[0:start] + labels[end:-1]
    train_list = [train_samples, train_labels]
    test_list = [samples[start:end], labels[start:end]]
    return (train_list,test_list)

#make the subdataset based on given attribute
def subDataset(dataset, attr):
    sub_1 = [[], []]
    sub_0 = [[], []]
    # idx:index sample:element, reading through every row,
    #looking at specific attribute value based on the index 'attr'
    #find the corresponding label of that attr
    #if attribute value is 1, append to sub_1
    #if attribute value is 0, append to sub_0
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
# def saveObject(object):
#     emotion_label = object.emotion()
#     emotion_string = labelToStr(emotion_label)
#     filename = "dt_"+emotion_string +".pkl"
#     with open(filename, 'wb') as f:
#         pickle.dump(object,f)
#     # save single object into the binary file
#     # the name of binary file should be "dt_<specific emotion>.extension"
#     return
def saveObjects(objects):
    file_name = 'decision_tree.pkl'
    with open(file_name, 'wb') as f:
        pickle.dump(objects,f)
    return file_name

def retrieveObjects(file_name):
    # retrieve objects from the saved binary files
    with open(file_name,'rb') as f:
        objects = pickle.load(f)
    return objects

# x,y = readDataFromMat("cleandata_students.mat")
dataset = [[[1,1,1],[2,0,2],[3,1,3],[4,0,4],[5,1,5],[6,0,6]],[1,2,3,4,5,6]]
first, second = crossValidation(dataset, 2,4)
# first1, second1 = subDataset(dataset,2)
print(first, second)
# print(first1,second1)
