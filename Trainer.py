# Decision tree trainer dedicated to determine the best entry feature and update the tree structure

from DecisionTree import *
from config import *


def learn(emotion, dataset, attributes):
    dt = DecisionTree("happiness")
    return dt

def learnModel(emotion, dataset):
    samples = dataset[0]
    labels = dataset[1]
    
    label = labelToNo(emotion)
    attributes = list(range(0, 44))
    
    dt = learn(label, dataset, attributes)
    return dt
