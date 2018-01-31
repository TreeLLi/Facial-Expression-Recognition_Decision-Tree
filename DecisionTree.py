# Decision tree model class used to represent the structure of trained Decision Tree model, visualise and predict the emotion of given sample
from config import *

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

# Prediction

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
