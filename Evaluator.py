# Individual evaluation
from config import *
import time
import numpy as np

def confusionMatrix(labels, predictions):
    cf_matrix = np.zeros((CROSS_VALIDATION_FOLDS, EMOTION_AMOUNT, EMOTION_AMOUNT), dtype=int).tolist()
    for fold in range(CROSS_VALIDATION_FOLDS):
        len_fold_labels = len(labels[fold])
        for exp_num in range(len_fold_labels):
            matrix_correspond_row = decodeLabel(labels[fold][exp_num]) - 1
            matrix_correspond_column = predictions[fold][exp_num] - 1
            cf_matrix[fold][matrix_correspond_row][matrix_correspond_column] += 1
    return cf_matrix


def averageConfusionMatrix(cf_matrix):
    ave_cf_matrix = [[0 for col in range(EMOTION_AMOUNT)] for row in range(EMOTION_AMOUNT)]
    for fold in range(CROSS_VALIDATION_FOLDS):
        for row in range(EMOTION_AMOUNT):
            for col in range(EMOTION_AMOUNT):
                ave_cf_matrix[row][col] += cf_matrix[fold][row][col] / CROSS_VALIDATION_FOLDS
    return ave_cf_matrix


def absoluteConfusionMatrix(cf_matrix):
    abs_cf_matrix = np.zeros((EMOTION_AMOUNT, EMOTION_AMOUNT), dtype=int).tolist()
    for fold in range(CROSS_VALIDATION_FOLDS):
        for row in range(EMOTION_AMOUNT):
            for col in range(EMOTION_AMOUNT):
                abs_cf_matrix[row][col] += cf_matrix[fold][row][col]
    return abs_cf_matrix


def nomalConfusionMatrix(cf_matrix):
    abs_cf_matrix = np.zeros((EMOTION_AMOUNT, EMOTION_AMOUNT), dtype=int).tolist()
    nom_cf_matrix = np.zeros((EMOTION_AMOUNT, EMOTION_AMOUNT), dtype=int).tolist()
    abs_cf_matrix = absoluteConfusionMatrix(cf_matrix)
    for row in range(EMOTION_AMOUNT):
        for col in range(EMOTION_AMOUNT):
            nom_cf_matrix[row][col] += abs_cf_matrix[row][col] / sum(abs_cf_matrix[row])
    return nom_cf_matrix


def tfMatrix(emotion, confusionMarix):
    tf_matrix = [[0 for x in range(2)] for y in range(2)]  # tf_matrix is a 2*2 list
    for emotion_index in range(len(confusionMarix)):
        if EMOTIONS[emotion_index] == emotion:
            break
    for i in range(len(confusionMarix)):
        for j in range(len(confusionMarix)):
            if i == emotion_index and j == emotion_index:
                tf_matrix[0][0] = confusionMarix[i][j]
            elif i == emotion_index and j != emotion_index:
                tf_matrix[0][1] += confusionMarix[i][j]
            elif i != emotion_index and j == emotion_index:
                tf_matrix[1][0] += confusionMarix[i][j]
            else:
                tf_matrix[1][1] += confusionMarix[i][j]
    return tf_matrix


def recallRate(emotion, cf_matrix):
    tf_matrix = tfMatrix(emotion, cf_matrix)
    return tf_matrix[0][0] / (tf_matrix[0][0] + tf_matrix[0][1])


def precisionRate(emotion, cf_matrix):
    tf_matrix = tfMatrix(emotion, cf_matrix)
    if (tf_matrix[0][0] + tf_matrix[1][0] == 0):
        print("There is no " + emotion + "example")
    precision_rate = (tf_matrix[0][0] / (tf_matrix[0][0] + tf_matrix[1][0]))
    return precision_rate


def f1(recall, precision):
    return (2 * recall * precision) / (recall + precision)


def classificationRate(cf_matrix):
    accuracy = 0
    for i in range(EMOTION_AMOUNT):
        accuracy += cf_matrix[i][i]
    total_amount = 0.0
    for row in cf_matrix:
        for column in row:
            total_amount += column
    
    return accuracy / total_amount


# summary evaluation

def evaluate(labels, pdts):
    # return a tuple with such order
    # confusion, recall, precision, f1, classification
    confusion_matrix = confusionMatrix(labels, pdts)
    ave_cf_matrix = averageConfusionMatrix(confusion_matrix)
    nom_cf_matrix = nomalConfusionMatrix(confusion_matrix)
    abs_cf_matrix = absoluteConfusionMatrix(confusion_matrix)
    recall_rate = []
    precision_rate = []
    f_1 = []
    for i in range(EMOTION_AMOUNT):
        # recall_rate.append(recallRate(EMOTIONS[i], ave_cf_matrix))
        # precision_rate.append(precisionRate(EMOTIONS[i], ave_cf_matrix))
        # recall_rate.append(recallRate(EMOTIONS[i], abs_cf_matrix))
        # precision_rate.append(precisionRate(EMOTIONS[i], abs_cf_matrix))
        recall_rate.append(recallRate(EMOTIONS[i], nom_cf_matrix))
        precision_rate.append(precisionRate(EMOTIONS[i], nom_cf_matrix))
        f_1.append(f1(recall_rate[i], precision_rate[i]))
    c_r = [classificationRate(nom_cf_matrix)]
    # return (ave_cf_matrix, recall_rate, precision_rate, f_1, c_r)
    # return (abs_cf_matrix, recall_rate, precision_rate, f_1, c_r)
    return (nom_cf_matrix, recall_rate, precision_rate, f_1, c_r)


def saveEvaluations(file_name, evaluations):
    # able to detect the data structures of passed evaluations
    # the write them into a single file with given file name automatically
    file = open("./evaluations/"+file_name, 'w')
    file.write('Confusion Matrix:\n')
    for argument_index in range(len(evaluations)):
        for index in range(len(evaluations[argument_index])):
            if type(evaluations[argument_index][index]) is list:
                for value in evaluations[argument_index][index]:
                    file.write(str('%.3f' % value))
                    file.write(' ')
                file.write('\n')
            else:
                file.write(TITLE[argument_index - 1] + '\n')
                for value in evaluations[argument_index]:
                    file.write(str('%.3f' % value))
                    file.write(' ')
                file.write('\n')
                break
    localtime = time.asctime(time.localtime(time.time()))
    file.write('\n' + "Time: " + localtime)
    file.close
