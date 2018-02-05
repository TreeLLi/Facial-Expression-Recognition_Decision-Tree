# Decision tree model class used to represent the structure of trained Decision Tree model, visualise and predict the emotion of given sample
from config import *

import random

class DecisionTree:

    def __init__(self, emotion, attr = -1):
        self.__rootAttribute = attr
        self.__emotion = emotion
        self.branchs = {1: None, 0: None}

# Accessing

    def op(self):
        return self.__rootAttribute

    def kids(self):
        kids = []
        for key in self.branchs.keys():
            if isinstance(self.branchs[key], DecisionTree):
                kids.append(self.branchs[key].op())
        return kids


    def classification(self):
        # substitue the name 'class' referred in the manual
        labels = []
        for key in self.branchs.keys():
            if not isinstance(self.branchs[key], DecisionTree):
                labels.append(self.branchs[key])
        return labels

    def emotion(self):
        return labelToNo(self.__emotion)


# Setting

    def newLeaf(self, key, value):
        self.branchs[key] = value
        return value

    def newSubtree(self, key, attr):
        sub_dt = DecisionTree(self.__emotion, attr)
        self.branchs[key] = sub_dt
        return sub_dt

    def setAttribute(self, attr):
        self.__rootAttribute = attr


# Visualisation and Export

    def visualise(self):
        print ("visualise tree " + self.__emotion)


    def export(self):
        print ("export tree" + self.__emotion)

# Single Tree Prediction

    # predict the emotion of single one sample
    def predictSample(self, sample):

        if not sample:
            return -1
        else:
            key = sample[self.__rootAttribute]
            if isinstance(self.branchs[key], DecisionTree):
                return self.branchs[key].predictSample(sample)
            else:
                return self.branchs[key]

    # predict the emotions of given samples
    def predict(self, samples):
        pdt = []
        for sample in samples:
            pdt.append(self.predictSample(sample))
        return pdt

# overall predictions

def testTrees(trees, samples):
    pdts_matrix = []
    for dt in trees:
        pdts_matrix.append(dt.predict(samples))

    predictions = combine(pdts_matrix)
    return predictions

def combine(pdts_matrix):
    activations = []
    for idx in range(len(pdts_matrix[0])):
        activation = []
        for emotion in range(EMOTION_AMOUNT):
            if pdts_matrix[emotion][idx] == 1:
                activation.append(emotion+1)
        activations.append(activation)
    return pick(activations)

# Random picking
# def pick(activations):
#     predictions = []
#     for activation in activations:
#         if activation:
#             # print ("random:" + str(len(activation)) + " ran: " + str(random.randint(0, len(activation)-1)))
#             picked = activation[random.randint(0, len(activation)-1)]
#             predictions.append(picked)
#         else:
#             predictions.append(1)
#     return predictions


# 1st Picking Algorithm
# def pick(activations):
#     predictions = []
#     for activation in activations:
#         if activation:
#             predictions.append(activation[0])
#         else:
#             predictions.append(1)
#     return predictions

# Recall & precision based picking
def pick(activations):
    predictions = []
    recalls = RECALLS
    precisions = PRECISIONS
    for activation in activations:
        ties = len(activation)
        if ties == 1:
            predictions.append(activation[0])
        elif ties == 0:
            mini_recall = recalls[0]
            emotion = 1
            for idx in range(EMOTION_AMOUNT):
                recall = recalls[idx]
                emotion = idx+1 if recall<mini_recall else emotion
            predictions.append(emotion)
        else:
            max_precision = precisions[activation[0]-1]
            emotion = activation[0]
            for activated in activation:
                precision = precisions[activated-1]
                emotion = activated if precision>max_precision else emotion
            predictions.append(emotion)
    return predictions
            
# F1 measure based picking

# def pick(activations):
#     predictions = []
#     f1s = F1s
#     for activation in activations:
#         ties = len(activation)
#         if ties == 1:
#             predictions.append(activation[0])
#         elif ties == 0:
#             max_f1 = f1s[0]
#             emotion = 0
#             for idx in range(EMOTION_AMOUNT):
#                 f1 = f1s[idx]
#                 emotion = idx+1 if f1>max_f1 else emotion
#             predictions.append(emotion)
#         else:
#             max_f1 = f1s[activation[0]-1]
#             emotion = activation[0]
#             for activated in activation:
#                 f1 = f1s[activated-1]
#                 emotion = activated if f1>max_f1 else emotion
#             predictions.append(emotion)

#     return predictions
