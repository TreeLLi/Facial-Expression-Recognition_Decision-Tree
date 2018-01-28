# The main program trains and evaluates a Decision Tree model using ID3 algorithm

from DecisionTree import *
from DataProcessor import *
from Trainer import *
from Evaluator import *

from config import *

if __name__ == '__main__':
    print ('Main program:\n')

    emotions = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]    
    clean_dataset = readDataFromMat(CLEAN_DATASET)
    noisy_dataset = readDataFromMat(NOISY_DATASET)

    # train models on the entire clean datasetsets
    clean_entire_dts = []
    for emotion in emotions:
        dt = learnModel(emotion, clean_dataset)
        clean_entire_dts.append(dt)
        dt.visualise()
        dt.export()
    
    for dataset in [clean_dataset, noisy_dataset]:
        dts_matrix = []
        pdts_matrix = []
        labels_matrix = []
        # split dataset based on the 10-folds cross validation method
        for fold in range(CROSS_VALIDATION_FOLDS):
            train_dataset, test_dataset = crossValidation(dataset, fold, CROSS_VALIDATION_FOLDS)

            # learn the models for each emotion for each fold, i.e. 6*10 classifiers
            dts_row = []
            for emotion in emotions:
                dt = learnModel(emotion, train_dataset)
                dts_row.append(dt)
            dts_matrix.append(dts_row)

            # predict the emotions for samples of test dataset
            pdts_row = []
            for dt in dts_row:
                predictions = dt.predict(test_dataset)
                pdts_row.append(predictions)
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
        

        
        

        
        
