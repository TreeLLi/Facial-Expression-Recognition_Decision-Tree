from DecisionTree import *
from DataProcessor import *
import pickle

DATASET_PATH = './data/cleandata_students.mat' # change the path of the dataset

if __name__ == '__main__':

    dataset = readDataFromMat(DATASET_PATH) # load the dataset (this function returns both samples and labels)
    trees = retrieveObjects('decision_tree.pkl') # load the trained trees 

    preditions = testTrees(trees, dataset[0]) # test data on the trained trees (dataset[0] stores samples)
    print(preditions)
