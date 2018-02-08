# Decision tree model class used to represent the structure of trained Decision Tree model, visualise and predict the emotion of given sample
from config import *
import TreeVisualization as TV
import random
import matplotlib.pyplot as plt

class DecisionTree:

    def __init__(self, emotion, attr = -1):
        self.__rootAttribute = attr
        self.__emotion = emotion
        self.branchs = {1: None, 0: None}
        self.maxDepth = 0

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
                width += self.branchs[key].getTreeWidth()
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

    def newSubtree(self, key, attr):
        sub_dt = DecisionTree(self.__emotion, attr)
        self.branchs[key] = sub_dt
        return sub_dt

    def setAttribute(self, attr):
        self.__rootAttribute = attr


# Visualisation and Export

    def visualisation(self):
        # please adjust the figsize in TreeVisualization class if overlap occurs, and then zoom in to observe the tree structure
        TV.visualise(self)
        print ("visualise tree " + self.__emotion)

    #
    #
    # def export(self):
    #     print ("export tree" + self.__emotion)

# Tree Prediction

    # predict the emotion of single one sample
    # def predictSample(self, sample):
    #     if not sample:
    #         return -1
    #     else:
    #         key = sample[self.__rootAttribute]
    #         if isinstance(self.branchs[key], DecisionTree):
    #             return self.branchs[key].predictSample(sample)
    #         else:
    #             return self.branchs[key]

    # predict the emotions of given samples
    # def predict(self, samples):
    #     pdt = []
    #     for sample in samples:
    #         pdt.append(self.predictSample(sample))
    #     return pdt
    
    # TEST
    def predictSample(self, sample, depth):
        key = sample[self.__rootAttribute]
        if isinstance(self.branchs[key], DecisionTree):
            return self.branchs[key].predictSample(sample, depth+1)
        else:
            return (self.branchs[key], depth+1)

    # predict the emotions of given samples
    def predict(self, samples):
        pdt = []
        for sample in samples:
            pdt.append(self.predictSample(sample, 0))
        return pdt

# overall predictions

# def testCombine(trees, dataset):
#     samples = dataset[0]
#     labels = dataset[1]
#     pdts_matrix = []
#     for dt in trees:
#         pdts_matrix.append(dt.predict(samples))

#     return combineTest(pdts_matrix, labels)

# def combineTest(pdts_matrix, labels):
#     predictions = []
#     ties_0_amount = 0
#     ties_2_amount = 0
#     for idx in range(len(pdts_matrix[0])):
#         activation = []
#         for emotion in range(EMOTION_AMOUNT):
#             if pdts_matrix[emotion][idx] == 1:
#                 activation.append(emotion+1)
#         ties = len(activation)
#         if ties==0 or ties>1:
#             ties_0_amount += 1 if ties>1 else 0
#             ties_2_amount += 1 if ties==0 else 0
#             label = decodeLabel(labels[idx])
#             if activation.count(label)==1:
#                 predictions.append(labels[idx])
#             else:
#                 predictions.append(encodeLabel(label+1 if label!=6 else 5))
#         else:
#             predictions.append(encodeLabel(activation[0]))

#     print ("Ties == 0:" + str(ties_0_amount) + "      >2: " + str(ties_2_amount))
#     print ("Ties proportion: " + str((ties_0_amount+ties_2_amount)/float(len(pdts_matrix[0]))))
#     return predictions

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

# TEST
# def testTrees(trees, dataset):
#     samples = dataset[0]
#     labels = dataset[1]
#     pdts_matrix = []
#     for dt in trees:
#         pdts_matrix.append(dt.predict(samples))

#     predictions = combine(trees, pdts_matrix, labels)
#     return predictions

# def combine(trees, pdts_matrix, labels):
#     activations = []
#     for idx in range(len(pdts_matrix[0])):
#         activation = []
#         for emotion in range(EMOTION_AMOUNT):
#             if pdts_matrix[emotion][idx] == 1:
#                 activation.append(emotion+1)
#         activations.append(activation)
#     combinations = pick(trees, activations)

#     predictions = []
#     ties_0_amount = 0
#     ties_2_amount = 0
#     ties_0_right = 0
#     ties_2_right = 0
#     for idx, prediction in enumerate(combinations):
#         predictions.append(encodeLabel(prediction))
#         ties = len(activations[idx])
#         label = decodeLabel(labels[idx])
#         ties_0_amount += 1 if ties==0 else 0
#         ties_2_amount += 1 if ties>1 else 0
#         ties_0_right += 1 if ties==0 and label==prediction else 0
#         ties_2_right += 1 if ties>1 and label==prediction else 0

#     print ("Ties == 0:" + str(ties_0_amount) + "      right: " + str(ties_0_right))
#     print ("Ties > 1:" + str(ties_2_amount) + "      right: " + str(ties_2_right))
#     return predictions

# TEST depth
def testTrees(trees, dataset):
    samples = dataset[0]
    labels = dataset[1]
    pdts_matrix = []
    for dt in trees:
        pdts_matrix.append(dt.predict(samples))

    predictions = combine(trees, pdts_matrix, labels)
    return predictions

def combine(trees, pdts_matrix, labels):
    activations = []
    combinations = []
    for idx in range(len(pdts_matrix[0])):
        activation = []
        for emotion in range(EMOTION_AMOUNT):
            if pdts_matrix[emotion][idx][0] == 1:
                activation.append((emotion+1, pdts_matrix[emotion][idx][1]))
        activations.append(activation)

        ties = len(activation)
        if ties == 0:
            max_idx = 0
            max = pdts_matrix[max_idx][idx][1]
            for emotion in range(EMOTION_AMOUNT):
                max_idx = emotion if pdts_matrix[emotion][idx][1]>max else max_idx
                max = pdts_matrix[max_idx][idx][1]
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

    predictions = []
    ties_0_amount = 0
    ties_2_amount = 0
    ties_0_right = 0
    ties_2_right = 0
    for idx, prediction in enumerate(combinations):
        predictions.append(encodeLabel(prediction))
        ties = len(activations[idx])
        label = decodeLabel(labels[idx])
        ties_0_amount += 1 if ties==0 else 0
        ties_2_amount += 1 if ties>1 else 0
        ties_0_right += 1 if ties==0 and label==prediction else 0
        ties_2_right += 1 if ties>1 and label==prediction else 0

    print ("Ties == 0:" + str(ties_0_amount) + "   right: " + str(ties_0_right) + " - " + str(ties_0_right/float(ties_0_amount)))
    print ("Ties > 1:" + str(ties_2_amount) + "   right: " + str(ties_2_right) + " - " + str(ties_2_right/float(ties_2_amount)))
    return predictions
                

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


# 1st Picking Algorithm
# def pick(trees, activations):
#     predictions = []
#     for activation in activations:
#         if activation:
#             predictions.append(activation[0])
#         else:
#             predictions.append(1)
#     return predictions

# Recall & precision based picking
def pick(trees, activations):
    predictions = []
    recalls = RECALLS
    precisions = PRECISIONS
    for activation in activations:
        ties = len(activation)
        if ties == 1:
            predictions.append(activation[0])
        elif ties == 0:
            # mini_recall = recalls[0]
            # emotion = 1
            # for idx in range(EMOTION_AMOUNT):
            #     recall = recalls[idx]
            #     emotion = idx+1 if recall<mini_recall else emotion
            #     mini_recall = recalls[emotion-1]
            # predictions.append(emotion)

            predictions.append(emotionMax(range(1, 6), recalls))
        else:
            predictions.append(emotionMax(activation, precisions))
    return predictions
            
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

def emotionMax(emotions, values):
    max_emotion = emotions[0]
    max_value = values[max_emotion-1]
    for emotion in emotions:
        max_emotion = emotion if values[emotion-1]>max_value else max_emotion
        max_value = values[max_emotion-1]
    return max_emotion
