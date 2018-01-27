# Decision tree model class used to represent the structure of trained Decision Tree model, visualise and predict the emotion of given sample
class DecisionTree:
    def __init__(self, emotion):
        self.emotion = emotion
        print ("DecisionTree " + self.emotion)

# Accessing

    def op(self):
        return "the attribute number"

    def kids(self):
        return []

    def classification(self):
        # substitue the name 'class' referred in the manual
        return 1
        
# Setting

    def newLeaf(self, value):
        return value

    def newNode(self, attr):
        sub_dt = DecisionTree(self.emotion)
        return sub_dt

# Visualisation and Export
        
    def visualise(self):
        print ("visualise tree " + self.emotion)

    def export(self):
        print ("export tree " + self.emotion)

# Prediction

    # predict the emotion of single one sample
    def predict(self, sample):
        return True

    # predict the emotions of given samples
    def predict(self, samples):
        return [True, False]
