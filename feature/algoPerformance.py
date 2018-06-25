# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:19:49 2017

@author: Preyas Shah
*************algoPerformance.py*****************
*This file contains the function to execute the
*baseline algorithms over the dataset and find the 
*performance parameters, such as precision, recall
*and F1 Score. 
"""

#*********Import Statements***************
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

#A Class that defines the Performance Metrics
#Defines the methods to get the various performance metrics on algorithms
class PerformanceMetrics:
    #Constructor
    def __init__(self,precision,recall):
        """Constructor of the class Performance Matrix
        Initialize it as: PerformanceMetrics(precision,recall)"""
        self.precision = precision
        self.recall = recall
        self.F1 = 2 * precision * recall / (precision + recall)
    #Precision
    def precision(self):
        """Returns the precision of the algorithm"""
        return self.precision
    #Recall
    def recall(self):
        """Returns the recall of the algorithm"""
        return self.recall
    #F1 Score
    def F1Score(self):
        """Returns the F1 Score of the algorithm"""
        #If precision or recall is 0, F1 score is 0
        if(self.precision == 0 or self.recall == 0):
            return 0
        else:    
            return 2 * self.precision * self.recall / (self.precision + self.recall)
        
#Apply the classifier to the training dataset
#Test the performance of the classifier using the test dataset
def applyClassifier(Xtrain,Ytrain,Xtest,Ytest,classifier_type, n_knnr=3):
    """Apply the classifier on training set and calculate the performance
    metrics ove the test set. 
    applyClassifier(Xtrain,Ytrain,Xtest,Ytest,classifier_type, n_knnr=3)
    Xtrain -> Input Training Set
    Ytrain -> Output Training Set
    Xtest  -> Input Test Set
    Ytest  -> Output Test Set
    classifier_type -> Has to be one of the Bayesian, Decision Tree, K-NNR
    n_knnr -> Only required for k nearest neighbor classifier (Default -> 3)"""
    if(classifier_type == "Bayesian"):
        print ("Applying Naive Bayes Classifier")
        clf = GaussianNB()
    elif(classifier_type == "Decision Tree"):
        print ("Applying Decision Tree")
        clf = tree.DecisionTreeClassifier()
    elif(classifier_type == "K-NNR"):
        print ("Applying K Nearest Neighbor Classification")
        clf = KNeighborsClassifier(n_neighbors=n_knnr)
    else:
        print ("Invalid Classifier")
        print (applyClassifier.__doc__)
        return
    #Fit the classifier over the training data
    clf.fit(Xtrain,Ytrain)
    rng = np.shape(Xtest)[0]
    #Now, calculate the true_positives, true_negatives,
    #false_postitives and false negatives
    #Calculate the performance parameters over them
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0    
    for i in range(rng):
        prediction = clf.predict(Xtest[i].reshape(1,-1))
        if(prediction[0] == int(Ytest[i])):
            if(prediction[0] == 0):
                true_negatives = true_negatives + 1
            else:
                true_positives = true_positives + 1
        else:
             if(prediction[0] == 0):
                false_negatives = false_negatives + 1
             else:
                false_positives = false_positives + 1
    try:        
        precision = float(true_positives)/(true_positives + false_positives)
        recall    = float(true_positives)/(true_positives + false_negatives)
    except: 
        precision = 0
        recall = 0
    algoPerformData = PerformanceMetrics(precision,recall)
    return algoPerformData
    
