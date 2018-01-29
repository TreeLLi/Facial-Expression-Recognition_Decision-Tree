# Decision tree model class used to represent the structure of trained Decision Tree model, visualise and predict the emotion of given sample
from config import *

class DecisionTree:

    def __init__(self, emotion, attribute = -1):
        self.attribute = attribute
        self.__emotion = emotion
        self.tree = {1: None, 0: None}

# Accessing

    def op(self):
        return self.attribute

    def kids(self):

        self.kids = []
        for key in self.tree.keys():
            if isinstance(self.tree[key], DecisionTree):
                self.kids.append(self.tree[key].op())
        return self.kids


    def classification(self):
        # substitue the name 'class' referred in the manual
        self.labels = []
        for key in self.tree.keys():
            if not isinstance(self.tree[key], DecisionTree):
                self.labels.append(self.tree[key])
        return self.labels

    def emotion(self):
        return labelToNo(self.__emotion)


# Setting

    def newLeaf(self, key, value):
        self.tree[key] = value
        return value

    def newNode(self, key, attr):
        self.sub_dt = DecisionTree(self.__emotion, attr)
        self.tree[key] = self.sub_dt
        return self.sub_dt

    def setAttribute(self, attr):
        self.attr = attr


# Visualisation and Export

    def visualise(self):
        print ("visualise tree " + self.__emotion)


    def export(self):
        print ("export tree" + self.__emotion)

# Prediction

    # predict the emotion of single one sample
    def predict(self, sample):
        return True

    # predict the emotions of given samples
    def predict(self, samples):
        return [True, False]
