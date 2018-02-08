# Decision tree trainer dedicated to determine the best entry feature and update the tree structure

from DecisionTree import *
from DataProcessor import subDataset
from config import *

from math import log

def areLabelsSame(emotion, labels):
    pos = 0
    neg = 0
    for label in labels:
        if label[emotion-1] == 1:
            pos += 1
        else:
            neg += 1

        if pos*neg != 0:
            return False
    return True

def areAttributesSame(samples, attribute):
    base = samples[0][attribute]
    for sample in samples:
        if base != sample[attribute]:
            return False
    return True

def majorityValue(emotion, labels):
    # index 0 for positive samples
    # index 1 for negative sampels
    counts = [0, 0]
    for label in labels:
        if label[emotion-1] == 1:
            counts[0] += 1
        else:
            counts[1] += 1

    if counts[0] > counts[1]:
        return YES
    else:
        return NO

def entropy(p, n):
    if p==0.0 and n==0.0:
        return 0.0
    
    first = p / (p+n)
    if first != 0.0:
        first = -1 * first * log(first, 2)
    second = n / (p+n)
    if second != 0.0:
        second = -1 * second * log(second, 2)
    return first + second

def remainder(p, n, p0, p1, n0, n1):
    first = (p0+n0)/(p+n) * entropy(p0, n0)
    second = (p1+n1)/(p+n) * entropy(p1, n1)
    return first + second

def areIGSame(igs):
    init = igs[0]
    for ig in igs:
        if ig != init:
            return False
    return True

def selectBestAttr(samples, labels, emotion, attributes):
    igs = []
    for attribute in attributes:
        p, p0, p1, n, n0, n1 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        for idx, sample in enumerate(samples):
            attr_value = sample[attribute]
            label_value = labels[idx][emotion-1]
            p += 1 if label_value==1 else 0
            n += 1 if label_value==0 else 0
            p0 += 1 if (label_value==1 and attr_value==0) else 0
            p1 += 1 if (label_value==1 and attr_value==1) else 0
            n0 += 1 if (label_value==0 and attr_value==0) else 0
            n1 += 1 if (label_value==0 and attr_value==1) else 0
        # print ("ig {6} p:{0} n:{1} p0:{2} p1:{3} n0:{4} n1:{5}".format(p, n, p0, p1, n0, n1, attribute))
        ig = entropy(p, n) - remainder(p, n, p0, p1, n0, n1)
        igs.append(ig)

    if areIGSame(igs):
        return -1
    else:
        max_idx = 0
        for idx, ig in enumerate(igs):
            max_idx= idx if ig>igs[max_idx] else max_idx
        return attributes[max_idx]
    
def learn(dt, dataset, attributes):
    samples = dataset[0]
    labels = dataset[1]
    emotion = dt.emotion()
    root_attr = dt.op()
    branch = samples[0][root_attr]
    leaf_value = majorityValue(emotion, labels)
    
    if areLabelsSame(emotion, labels):
        # all samples share the same emotion
        leaf_value = YES if labels[0][emotion-1]==1 else NO
        if root_attr == -1:
            dt.newLeaf(YES, leaf_value)
            dt.newLeaf(NO, leaf_value)
        elif areAttributesSame(samples, root_attr):
            dt.newLeaf(branch, leaf_value)
            # print ("New leaf {0} for the branch {1} of parent node {2} same value".format(leaf_value, branch, dt.op()))
    elif not attributes:
        # all features have been used
        dt.newLeaf(branch, leaf_value)
        # print ("New leaf {0} for the branch {1} of parent node {2} no attribute".format(leaf_value, branch, dt.op()))
    else:
        best_attr = selectBestAttr(samples, labels, emotion, attributes)
        if best_attr == -1:
            dt.newLeaf(branch, leaf_value)
            return 
        branched_dt = dt
        if root_attr == -1:
            dt.setAttribute(best_attr)
            print ("The root:" + str(dt.op()))
        else:
            branched_dt = dt.newSubtree(branch, best_attr)
            # print ("New node {0} for the branch {1} of parent node {2}".format(branched_dt.op(), branch, dt.op()))

        if attributes.count(best_attr) > 0:
            sub_attrs = list(attributes)
            sub_attrs.remove(best_attr)
        
        for branch in (NO, YES):
            sub_dataset = subDataset(dataset, best_attr)[branch]
            
            if not sub_dataset[0]:
                branched_dt.newLeaf(branch, leaf_value)
                # print ("New leaf {0} for the branch {1} of parent node {2} no data".format(leaf_value, branch, branched_dt.op()))
            else:
                learn(branched_dt, sub_dataset, sub_attrs)
        

def learnModel(emotion, dataset):
    dt = DecisionTree(emotion)
    attributes = list(range(0, 44))

    learn(dt, dataset, attributes)
    return dt


