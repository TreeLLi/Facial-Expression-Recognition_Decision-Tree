# Data Processor works for loading and preprocessing, format and split etc.


class DataProcessor:
    def __init__(self):
        print ("Data Processor\n")

# Load data
        
    def read(self, file_name):
        print ("read data: " + file_name)
        return [[1, 2, 3], [4, 5, 6]]

# Split and divide
    
    def crossValidation(self, dataset, folds):
        # return (train_list, test_list)
        # train_list is [[x-samples:N*45], [y-labels:1*N]]
        return ([[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [8, 9, 10]])

    def subDataset(self, dataset, attr):
        # split dataset based on the values of given attr
        # return sub-datasets with the same form of dataset
        # idx 0 for attr value 0, idx 1 for attr value 1
        return [dataset, dataset]

# Processing
    
    def majorityValue(self, labels):
        return 1
