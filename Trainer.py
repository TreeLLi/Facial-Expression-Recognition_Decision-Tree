# Decision tree trainer dedicated to determine the best entry feature and update the tree structure

from DecisionTree import *
from config import *

class Trainer:
    def __init__(self):
        print ("Decision Tree Trainer is created.")

    def learnModel(self, emotion, data):
        print ("Training model of " + emotion + " " + str(labelToNo(emotion)))
        dt = DecisionTree(emotion)
        return dt
