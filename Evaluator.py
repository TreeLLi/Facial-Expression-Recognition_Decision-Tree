# Evaluator used to evaluate the Decision Tree models

# Individual evaluation
def confusionMatrix(labels, predictions):
    row, coloum = 6, 6
    cf_matrix= [[0 for x in range(row)] for y in range(coloum)]
    for i in range(len(labels)):
        cf_matrix[labels[i][0]-1][predictions[i][0]-1]+=1
    print ("Confusion Matrix")
    return cf_matrix
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

def recallRate( emotion, cf_matrix):
    print ("Recall rate for " + emotion)
    tf_matrix=tfMatrix(emotion,cf_matrix)
    return tf_matrix[0][0]/(tf_matrix[0][0]+tf_matrix[0][1])

def precisionRate( emotion, cf_matrix):
    print ("Precision rate for " + emotion)
    tf_matrix=tfMatrix(emotion,cf_matrix)
    PrecisionRate = (tf_matrix[0][0] / (tf_matrix[0][0] + tf_matrix[1][0]))
    return PrecisionRate

def f1(recall, precision):
    print ("F1")
    return (2*recall* precision)/(recall+precision)

def classificationRate( emotion, labels, pdts):
    confusion_matrix=confusionMatrix(labels,pdts)
    sum=0
    for i in range(6):
        sum+=confusion_matrix[i][i]
    return sum/1004
    
def evaluate(labels, pdts):

    # return a tuple with such order
    # confusion, recall, precision, f1, classification
    confusion_matrix=confusionMatrix(labels, pdts)
    recall_rate=[]
    precision_rate=[]
    F1=[]
    emotions = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]
    for i in range(6):
        recall_rate.append(recallRate(emotions[i],confusion_matrix))
        print(recall_rate[i])
        precision_rate.append(precisionRate(emotions[i], confusion_matrix))
        F1.append(f1(recall_rate[i], precision_rate[i]))
    CR=classificationRate("a", labels, pdts)
    return (confusion_matrix, recall_rate, precision_rate,f1 ,CR )

