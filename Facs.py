# The main program trains and evaluates a Decision Tree model using ID3 algorithm

from DecisionTree import *
from DataProcessor import *
from Trainer import *
from Evaluator import *

from config import *

def predict_overall(tree_pdts):
    overall_pdts = []
    for idx in range(len(tree_pdts[0])):
        for emotion in range(EMOTION_AMOUNT):
            if tree_pdts[emotion][idx] == 1:
                overall_pdts.append(emotion+1)
                break
            if emotion == EMOTION_AMOUNT-1:
                overall_pdts.append(1)
    return overall_pdts

if __name__ == '__main__':
    print ('Main program:\n')

    clean_dataset = readDataFromMat(CLEAN_DATASET)
    noisy_dataset = readDataFromMat(NOISY_DATASET)

    # train models on the entire clean datasetsets
    clean_entire_dts = []
    for emotion in EMOTIONS:
        print ("\n")
        print ("Training " + emotion + " tree on the clean dataset:")
        dt = learnModel(emotion, clean_dataset)
        clean_entire_dts.append(dt)
        # dt.visualise()
        # dt.export()
    
    for dataset in [clean_dataset, noisy_dataset]:
        dts_matrix = []
        pdts_matrix = []
        labels_matrix = []

        # split dataset based on the 10-folds cross validation method
        for fold in range(CROSS_VALIDATION_FOLDS):
            train_dataset, test_dataset = crossValidation(dataset, fold, CROSS_VALIDATION_FOLDS)
            # learn the models for each emotion for each fold, i.e. 6*10 classifiers
            dts_row = []
            for emotion in EMOTIONS:
                if dataset is clean_dataset:
                    print ("Training {0} tree for {1} fold of clean dataset:".format(emotion, fold))
                else:
                    print ("Training {0} tree for {1} fold of noisy dataset:".format(emotion, fold))

                dt = learnModel(emotion, train_dataset)
                dts_row.append(dt)
            dts_matrix.append(dts_row)

            # predict the emotions for samples of test dataset
            tree_pdts = []
            for dt in dts_row:
                predictions = dt.predict(test_dataset[0])
                tree_pdts.append(predictions)

            pdts_row = predict_overall(tree_pdts)
            
            pdts_matrix.append(pdts_row)
            labels_matrix.append(test_dataset[1])

        # evaluate the results of predictions
        cf_matrix, recalls, precisions, f1s, classifications = evaluate(labels_matrix, pdts_matrix)
        if dataset is clean_dataset:
            print ("The evaluation for the clean dataset:\n")
        else:
            print ("The evaluation for the noisy dataset:\n")
            
        print ("Confusion Matrix: ")
        print (cf_matrix)
            
        print ("Recall rates: ")
        print (recalls)

        print ("Precision rates: ")
        print (precisions)

        print ("F1 measurements: ")
        print (f1s)
                
        print ("Classification rates: ")
        print (classifications)

        # results = evaluate(labels_matrix, pdts_matrix)
        # if dataset is clean_dataset:
        #     file_name = "clean_evaluations"
        # else:
        #     file_name = "noisy_evaluations"
        # saveEvaluations(file_name, results)
