# Data Processor works for loading and preprocessing, format and split etc.

class DataProcessor:
    def __init__(self):
        print ("Data Processor\n")

    def read(self, file_name):
        print ("read data: " + file_name)
        return [[1, 2, 3], [4, 5, 6]]

    def crossValidation(self, data, folds):
        # (train_list, test_list)
        return ([[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [8, 9, 10]])
