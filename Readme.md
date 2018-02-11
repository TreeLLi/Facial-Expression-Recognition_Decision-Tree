# Facial Expression Recognition System(Simplified) Based on the AUs

## Running Instructions
In order to test the performance of the trained decision trees on new dataset, please load the trained trees from `decision_tree.pkl`, which returns a list of `6` trained trees, and import `DecisionTree.py` in your test file. The running environment should be `Linux` and `python 3`. Invoke the function `testTrees(trees, dataset)` to start your testing. The first parameter of the `testTrees` function is the loaded `6` decision trees, and the second parameter is the new dataset with the same format as the `cleandata_students.mat` and `noisydata_students`. This function returns a list of predictions ranging from `1` to `6`. 

## File Architecture
### Facs.py
the main program, i.e. the starting point  `__name__=="main"` of program, describes the complete working flows including data reading, preprocessing, model learning, predicting and evaluating.

### config.py
this file contains all pre-defined global configurations, like data files' names, cross-validation's folds and the mapping between emotions and its corresponding number in the data files.

### makefile
Basically, there're two methods to compile/run the python script. Writing and using makefile is just a **personal, i.e. Lin's, preference** out of a consideration to run it more smoothly on the emacs editor and make a full use of some auto-script like clean. Therefore, if dislike, you can still run the program by using `python Facs.py` in the terminal.

### .gitignore
These files, currently `*.pyc` and `__pycache__`, have already been blocked to be included in the git.s

## Terms Clarification
* **dataset**: a list of two lists, samples and labels respectively
* **datasets**: a list of N datasets
* **sample**: one single observation of dataset containing normally 45 boolean values representing states of 45 AUs witout corresponding label
* **label(s)**: the single value(list) of emotion's number(s)
* **matrix**: alias of multi-dimension list
* **row**: single(one) dimension list embeded in the matrix

## Dependencies

Kindly please **add any external libraries you're using but not in this list** into here so that others can know what he/she should prepare:

* import scipy.io (version:0.17.0)
* import numpy as np (version:1.11.0)
* import pickle (version:3.0)
* import time (version:3.5.2)
