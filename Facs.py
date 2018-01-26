# The main program trains and evaluates a Decision Tree model using ID3 algorithm

from DecisionTree import *
from DataProcessor import *

CLEAN_DATA = "cleandata_students.mat"
NOISY_DATA = "noisydata_students.mat"

if __name__ == '__main__':
    print ('Main program:\n')

    processor = DataProcessor()
    clean_data = processor.read(CLEAN_DATA)
    noisy_data = processor.read(NOISY_DATA)

    for data in [clean_data, noisy_data]:
        
    dt = DecisionTree()
    
