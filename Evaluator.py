# Evaluator used to evaluate the Decision Tree models

# Individual evaluation

def confusionMatrix(labels, predictions):
    print ("Confusion Matrix")
    
def recallRate(emotion, cf_matrix):
    print ("Recall rate for " + emotion)
    
def precisionRate(emotion, cf_matrix):
    print ("Precision rate for " + emotion)

def f1(recall, precision):
    print ("F1")

def classificationRate(emotion, labels, pdts):
    print ("Classficiation Rate for emotion " + emotion)

# Summary evaluation

def evaluate(labels, pdts):
    # return a tuple with such order
    # confusion, recall, precision, f1, classification
    return ([], [], [], [], [])
