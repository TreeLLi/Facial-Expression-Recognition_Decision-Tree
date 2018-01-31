# Individual evaluation

def confusionMatrix(labels, predictions):
    row, coloum = 6, 6
    # single_labels=[]
    # single_predictions=[]
    # for i in range(10):
    #     single_labels.append(labels[i])
    #     single_predictions.append(predictions[i])
    cf_matrix= [[[0 for x in range(row)] for y in range(coloum)] for i in range(10)]
    for i in range(10):
        for j in range(len(labels[i])):
            cf_matrix[i][labels[i][j]-1][predictions[i][j]-1]+=1
    return cf_matrix

def averageConfusionMatrix(cf_martix):
 ave_cf_matrix=[[0 for i in range(6)] for j in range(6)]
 for i in range(10):
     for row in range(6):
         for col in range(6):
             ave_cf_matrix[row][col]+=cf_martix[i][row][col]   #average?
 return ave_cf_matrix


def tfMatrix(emotion,confusionMarix):
    tf_matrix = [[0 for x in range(2)] for y in range(2)]
    emotions = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]
    for emotionIndex in range(6):
        if emotions[emotionIndex] == emotion:
            break
    for i in range(6):
        for j in range(6):
            if i==emotionIndex and j==emotionIndex:
                tf_matrix[0][0]=confusionMarix[i][j]
            elif i==emotionIndex and j!=emotionIndex:
                tf_matrix[0][1] += confusionMarix[i][j]
            elif i!=emotionIndex and j==emotionIndex:
                tf_matrix[1][0] += confusionMarix[i][j]
            else:
                tf_matrix[1][1] += confusionMarix[i][j]
    return tf_matrix

def recallRate(emotion, cf_matrix):
    # print ("Recall rate for " + emotion)
    tf_matrix=tfMatrix(emotion,cf_matrix)
    return tf_matrix[0][0]/(tf_matrix[0][0]+tf_matrix[0][1])

def precisionRate(emotion, cf_matrix):
    # print ("Precision rate for " + emotion)
    tf_matrix=tfMatrix(emotion,cf_matrix)
    precision_rate = (tf_matrix[0][0] / (tf_matrix[0][0] + tf_matrix[1][0]))
    return precision_rate

def f1(recall, precision):
    # print ("F1")
    return (2*recall* precision)/(recall+precision)

def classificationRate( emotion, labels, pdts):
    confusion_matrix=confusionMatrix(labels,pdts)
    ave_cf_matrix=averageConfusionMatrix(confusion_matrix)
    sum = 0
    for i in range(6):
        sum+=ave_cf_matrix[i][i]

    return sum/(len(labels)*len(labels[0]))


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
    emotions = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]
    for i in range(6):
        recall_rate.append(recallRate(emotions[i],ave_cf_matrix))
        precision_rate.append(precisionRate(emotions[i], ave_cf_matrix))
        f_1.append(f1(recall_rate[i], precision_rate[i]))
    c_r=classificationRate("a", labels, pdts)
    return (ave_cf_matrix, recall_rate, precision_rate,f_1 ,c_r )

