# Decision tree model class used to represent the structure of trained Decision Tree model, visualise and predict the emotion of given sample

from config import *
import TreeVisualization as TV
import random
import matplotlib.pyplot as plt

class DecisionTree:

    def __init__(self, emotion, attr = -1, ig=0):
        self.__rootAttribute = attr
        self.__emotion = emotion
        self.branchs = {1: None, 0: None}
        self.__ig = ig

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

    def width(self):
        width = 0
        for key in self.branchs.keys():
            if isinstance(self.branchs[key], DecisionTree):
                width += self.branchs[key].width()
            else:
                width += 1
        return width

    def depth(self):
        maxDepth = 0
        for key in self.branchs.keys():
            if isinstance(self.branchs[key], DecisionTree):
                depth = self.branchs[key].depth() + 1
            else:
                depth = 1
            if depth > maxDepth:
                maxDepth = depth
        return maxDepth


# Setting

    def newLeaf(self, key, value):
        self.branchs[key] = value
        return value

    def newSubtree(self, key, attr_ig):
        attr = attr_ig[0]
        ig = attr_ig[1]
        sub_dt = DecisionTree(self.__emotion, attr, ig)
        self.branchs[key] = sub_dt
        return sub_dt

    def setAttribute(self, attr_ig):
        attr = attr_ig[0]
        ig = attr_ig[1]
        self.__rootAttribute = attr
        self.__ig = ig


# Visualisation and Export

    def visualisation(self):
        # please adjust the figsize in TreeVisualization class if overlap occurs
        # and then zoom in to observe the tree structure
        TV.visualise(self)
        print ("visualise tree " + self.__emotion)

# Tree Prediction
    
    def predictSample(self, sample, depth=0, ig=0):
        key = sample[self.__rootAttribute]
        if isinstance(self.branchs[key], DecisionTree):
            return self.branchs[key].predictSample(sample, depth+1, ig+self.__ig)
        else:
            return [self.branchs[key], depth+1, ig+self.__ig]

    # predict the emotions of given samples
    def predict(self, samples):
        pdt = []
        for sample in samples:
            results = self.predictSample(sample)
            results[1] = results[1] / float(self.depth())
            pdt.append(results)
        return pdt

# overall predictions

def testTrees(trees, samples):
    pdts_matrix = []
    for dt in trees:
        pdts_matrix.append(dt.predict(samples))

    predictions = combine(trees, pdts_matrix)
    return predictions

def combine(trees, pdts_matrix):
    activations = []
    combinations = []
    for idx in range(len(pdts_matrix[0])):
        activation = []
        for emotion in range(EMOTION_AMOUNT):
            if pdts_matrix[emotion][idx][0] == 1:
                activation.append((emotion+1, pdts_matrix[emotion][idx][2]))
        activations.append(activation)

        ties = len(activation)
        if ties == 0:
            max_idx = 0
            max = pdts_matrix[max_idx][idx][2]
            for emotion in range(EMOTION_AMOUNT):
                max_idx = emotion if pdts_matrix[emotion][idx][2]>max else max_idx
                max = pdts_matrix[max_idx][idx][2]
            combinations.append(max_idx+1)
        elif ties > 1:
            min_idx = 0
            min = activation[min_idx][1]
            for emotion in range(len(activation)):
                min_idx = emotion if activation[emotion][1]<min else min_idx
                min = activation[min_idx][1]
            combinations.append(activation[min_idx][0])
        else:
            combinations.append(activation[0][0])

    return combinations


# def testTrees(trees, samples):
#     pdts_matrix = []
#     for dt in trees:
#         pdts_matrix.append(dt.predict(samples))

#     predictions = combine(trees, pdts_matrix)
#     return predictions

# def combine(trees, pdts_matrix):
#     activations = []
#     for idx in range(len(pdts_matrix[0])):
#         activation = []
#         for emotion in range(EMOTION_AMOUNT):
#             if pdts_matrix[emotion][idx] == 1:
#                 activation.append(emotion+1)
#         activations.append(activation)
#     combinations = pick(trees, activations)

#     predictions = []
#     for prediction in combinations:
#         predictions.append(encodeLabel(prediction))

#     return predictions


# Random picking
# def pick(trees, activations):
#     predictions = []
#     for activation in activations:
#         if activation:
#             # print ("random:" + str(len(activation)) + " ran: " + str(random.randint(0, len(activation)-1)))
#             picked = activation[random.randint(0, len(activation)-1)]
#             predictions.append(picked)
#         else:
#             predictions.append(1)
#     return predictions


# Recall & precision based picking
# def pick(trees, activations):
#     predictions = []
#     recalls = RECALLS
#     precisions = PRECISIONS
#     for activation in activations:
#         ties = len(activation)
#         if ties == 1:
#             predictions.append(activation[0])
#         elif ties == 0:
#             # mini_recall = recalls[0]
#             # emotion = 1
#             # for idx in range(EMOTION_AMOUNT):
#             #     recall = recalls[idx]
#             #     emotion = idx+1 if recall<mini_recall else emotion
#             #     mini_recall = recalls[emotion-1]
#             # predictions.append(emotion)

#             predictions.append(emotionMax(range(1, 6), recalls))
#         else:
#             predictions.append(emotionMax(activation, precisions))
#     return predictions
            
# F1 measure based picking
# def pick(trees, activations):
#     predictions = []
#     f1s = F1s
#     for activation in activations:
#         ties = len(activation)
#         if ties == 1:
#             predictions.append(activation[0])
#         elif ties == 0:
#             predictions.append(emotionMax(range(1, 6), f1s))
#         else:
#             predictions.append(emotionMax(activation, f1s))
#     return predictions

# depth first
# def pick(trees, activations):
#     predictions = []
#     depths = []
#     for tree in trees:
#         depths.append(tree.depth())

#     for activation in activations:
#         ties = len(activation)
#         if ties == 1:
#             predictions.append(activation[0])
#         elif ties > 1:
#             predictions.append(emotionMax(activation, depths))
#         else:
#             predictions.append(emotionMax(range(1, 6), depths))
#     return predictions

# def emotionMax(emotions, values):
#     max_emotion = emotions[0]
#     max_value = values[max_emotion-1]
#     for emotion in emotions:
#         max_emotion = emotion if values[emotion-1]>max_value else max_emotion
#         max_value = values[max_emotion-1]
#     return max_emotion
