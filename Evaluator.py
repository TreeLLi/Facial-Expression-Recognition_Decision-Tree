# Individual evaluation
from config import *
import time

def confusionMatrix(labels, predictions):
    cf_matrix= [[[0 for x in range(EMOTION_AMOUNT)] for y in range(EMOTION_AMOUNT)] for i in range(CROSS_VALIDATION_FOLDS)]
    for fold in range(CROSS_VALIDATION_FOLDS):
        for exp_num in range(len(labels[fold])):
            cf_matrix[fold][labels[fold][exp_num]-1][predictions[fold][exp_num]-1]+=1
    return cf_matrix

# calculate the average confusion matrix of ten datasets
def averageConfusionMatrix(cf_martix):
 ave_cf_matrix=[[0 for col in range(EMOTION_AMOUNT)] for row in range(EMOTION_AMOUNT)]
 for fold in range(CROSS_VALIDATION_FOLDS):
     for row in range(EMOTION_AMOUNT):
         for col in range(EMOTION_AMOUNT):
             ave_cf_matrix[row][col]+=cf_martix[fold][row][col]/CROSS_VALIDATION_FOLDS   # average?
 return ave_cf_matrix

def tfMatrix(emotion,confusionMarix):
    tf_matrix = [[0 for x in range(2)] for y in range(2)]   # tf_matrix is a 2*2 list
    for emotion_index in range(len(confusionMarix)):  # this loop find the emotion_index of the passed emotion
        if EMOTIONS[emotion_index]==emotion:
            break
    for i in range(len(confusionMarix)):
        for j in range(len(confusionMarix)):
            if i==emotion_index and j==emotion_index:
                tf_matrix[0][0]=confusionMarix[i][j]
            elif i==emotion_index and j!=emotion_index:
                tf_matrix[0][1]+=confusionMarix[i][j]
            elif i!=emotion_index and j==emotion_index:
                tf_matrix[1][0]+=confusionMarix[i][j]
            else:
                tf_matrix[1][1]+=confusionMarix[i][j]
    return tf_matrix

def recallRate(emotion, cf_matrix):
    # print ("Recall rate for " + emotion)
    tf_matrix=tfMatrix(emotion,cf_matrix)
    return tf_matrix[0][0]/(tf_matrix[0][0]+tf_matrix[0][1])

def precisionRate(emotion, cf_matrix):
    # print ("Precision rate for " + emotion)
    tf_matrix=tfMatrix(emotion,cf_matrix)
    precision_rate=(tf_matrix[0][0]/(tf_matrix[0][0]+tf_matrix[1][0]))
    return precision_rate

def f1(recall, precision):
    # print ("F1")
    return (2*recall* precision)/(recall+precision)

def classificationRate( emotion, labels, pdts):
    confusion_matrix=confusionMatrix(labels,pdts)
    ave_cf_matrix=averageConfusionMatrix(confusion_matrix)
    sum = 0
    for i in range(EMOTION_AMOUNT):
        sum+=ave_cf_matrix[i][i]
    return sum/((len(labels)*len(labels[0]))/CROSS_VALIDATION_FOLDS)
   # print ("Classficiation Rate for emotion " + emotion)

# Summary evaluation

def evaluate(labels, pdts):
    # return a tuple with such order
    # confusion, recall, precision, f1, classification
    confusion_matrix=confusionMatrix(labels, pdts)
    ave_cf_matrix=averageConfusionMatrix(confusion_matrix)
    recall_rate=[]
    precision_rate=[]
    f_1=[]
    for i in range(6):
        recall_rate.append(recallRate(EMOTIONS[i],ave_cf_matrix))
        precision_rate.append(precisionRate(EMOTIONS[i], ave_cf_matrix))
        f_1.append(f1(recall_rate[i], precision_rate[i]))
    c_r=classificationRate("a",labels,pdts)
    argument = [ave_cf_matrix, recall_rate, precision_rate, f_1, c_r]
    return (ave_cf_matrix,recall_rate,precision_rate,f_1 ,c_r )

# Save results into files
TITLE=['Recall rate:','Precision rate:','F1:','Classification rate:']
def saveEvaluations(file_name,evaluations):
    # able to detect the data structures of passed evaluations
    # the write them into a single file with given file name automatically
    file=open(file_name,'w')
    file.write('Confusion Matrix:\n')
    for argument_index in range(len(evaluations)):
        for index in range(len(evaluations[argument_index])):
            if type(evaluations[argument_index][index]) is list:
                for value in evaluations[argument_index][index]:
                    file.write(str(value))
                    file.write(' ')
                file.write('\n')
            else:
                file.write(TITLE[argument_index-1]+'\n')
                for value in evaluations[argument_index]:
                    file.write(str(value))
                    file.write(' ')
                file.write('\n')
                break
    localtime = time.asctime(time.localtime(time.time()))
    file.write('\n'+"Time: " + localtime)
    file.close

