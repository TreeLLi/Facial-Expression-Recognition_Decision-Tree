# configurations of program

# DATASET
CLEAN_DATASET = "cleandata_students.mat"
NOISY_DATASET = "noisydata_students.mat"

# EMOTHIONS LABELS
EMOTIONS = ["anger", "disgust", "fear", "happiness", "sadness", "surprise"]
__LABELS = {"anger" : 1,
            "disgust" : 2,
            "fear" : 3,
            "happiness" : 4,
            "sadness" : 5,
            "surprise" : 6}

EMOTION_AMOUNT = len(__LABELS)

def labelToNo(label):
    return __LABELS[label]

def labelToStr(label):
    for string, number in __LABELS.items():
        if number == label:
            return string
    print ("Illegal emotion lable number")

def encodeLabel(label):
    encoded = [ 0 for i in range(6)]
    encoded[label-1] = 1
    return encoded

def decodeLabel(label):
    for idx, value in enumerate(label):
        if value == 1:
            return idx+1

    return -1

YES = 1
NO = 0

# CROSS VALIDATION
CROSS_VALIDATION_FOLDS = 10

# HISTORY TEST PERFORMANCE
RECALLS = [0.786, 0.672, 0.695, 0.786, 0.538, 0.786]
PRECISIONS = [0.438, 0.773, 0.796, 0.871, 0.676, 0.848]
F1s = [0.563, 0.719, 0.742, 0.826, 0.599, 0.816]

# RECALLS = [0.534, 0.686, 0.694, 0.846, 0.689, 0.815]
# PRECISIONS = [0.791, 0.716, 0.861, 0.790, 0.484, 0.765]

# FILE INDEX TITLE
TITLE = ['Recall rate:', 'Precision rate:', 'F1:', 'Classification rate:']
