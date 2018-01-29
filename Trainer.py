# Decision tree trainer dedicated to determine the best entry feature and update the tree structure

from DecisionTree import *
from config import *

from math import log

def isSameValues(labels):
    base = labels[0]
    for label in labels:
        if base != label:
            return False
    return True

def majorityValue(emotion, labels):
    counts = (0, 0)
    for label in labels:
        if label == emotion:
            counts[0] += 1
        else:
            counts[1] += 1

    if counts[0] >= counts[1]:
        return True
    else:
        return False

def entropy(p, n):
    first = p / (p+n)
    first = -1 * first * log(first, 2)
    second = n / (p+n)
    second = -1 * second * log(second, 2)
    return first + second

def remainder(p, n, p0, p1, n0, n1):
    first = (p0+n0)/(p+n) * entropy(p0, n0)
    second = (p1+n1)/(p+n) * entropy(p1, n1)
    return first + second
    
def selectBestAttr(samples, labels, emotion, attributes):
    igs = []
    for attribute in attributes:
        p, p0, p1, n, n0, n1 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        for idx, sample in enumerate(samples):
            attr_value = sample[attribute]
            label = labels[idx]
            #print (label)
            p += 1 if label==emotion else 0
            n += 1 if label!=emotion else 0
            p0 += 1 if (label==emotion and attr_value==0) else 0
            p1 += 1 if (label==emotion and attr_value==1) else 0
            n0 += 1 if (label!=emotion and attr_value==0) else 0
            n1 += 1 if (label!=emotion and attr_value==1) else 0
        ig = entropy(p, n) - remainder(p, n, p0, p1, n0, n1)
        igs.append(ig)
    
def learn(dt, dataset, attributes):
    samples = dataset[0]
    labels = dataset[1]
    #emotion = dt.emotion
    emotion = 1

    if isSameValues(labels):
        # all samples share the same emotion
        leaf_value = True if emotion==labels[0] else False
        dt.newLeaf(leaf_value)
    elif not attributes:
        # all features have been used
        leaf_value = majorityValue(emotion, labels)
        dt.newLeaf(leaf_value)
    else:
        best_attr = selectBestAttr(samples, labels, emotion, attributes)
    

def learnModel(emotion, dataset):
    dt = DecisionTree(emotion)
    attributes = list(range(0, 44))

    # print (dataset[0][0])
    # print (dataset[1][0])
    
    learn(dt, dataset, attributes)
    return dt


