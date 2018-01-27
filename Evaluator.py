# Evaluator used to evaluate the Decision Tree models

class Evaluator:
    def __init__(self):
        print ("Evaluator is created")

# Individual evaluation

    def confusionMatrix(self, labels, predictions):
        print ("Confusion Matrix")

    def recallRate(self, emotion, cf_matrix):
        print ("Recall rate for " + emotion)

    def precisionRate(self, emotion, cf_matrix):
        print ("Precision rate for " + emotion)

    def f1(self, recall, precision):
        print ("F1")

    def classificationRate(self, emotion, labels, pdts):
        print ("Classficiation Rate for emotion " + emotion)

# Summary evaluation

    def evaluate(self, labels, pdts):
        # return a tuple with such order
        # confusion, recall, precision, f1, classification
        return ([], [], [], [], [])
