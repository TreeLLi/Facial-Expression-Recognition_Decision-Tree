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
    for string, number in __LABELS:
        if number == label:
            return string
    print ("Illegal emotion lable number")

YES = 1
NO = 0

# CROSS VALIDATION
CROSS_VALIDATION_FOLDS = 10
