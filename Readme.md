# Facial Expression Recognition System(Simplified) Based on the AUs

## Running Instructions
In order to test the performance of the trained decision trees on new dataset, please load the trained trees from `decision_tree.pkl`, which returns a list of **6** trained trees, and import `DecisionTree.py` in your test file. You can use standard way of loading pickle file to load the `decision_tree.pkl` or simply use the `retrieveObjects` function in `DataProcessor.py`. The running environment should be **Linux** and **python 3**. Invoke the function `testTrees(trees, samples)` to start your testing. The first parameter of the `testTrees` function is the loaded **6** decision trees, and the second parameter is the new samples. This function returns a list of predictions ranging from **1** to **6**. We have provided an example test file `bootstrap.py` as a reference to test the trained decision trees.



## Dependencies

Kindly please **add any external libraries you're using but not in this list** into here so that others can know what he/she should prepare:

* scipy.io (version:0.17.0)
* numpy (version:1.11.0)
* pickle (version:3.0)
* matplotlib (version:1.5.1)

## Retrain the decision trees
If you want to retrain the decision trees, please run the `Facs.py`. **Although it is rare that the program starts running slowly, if it happens, please wait a moment**. It may take a moment to cache some fonts. 

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
