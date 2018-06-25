# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:49:35 2017

@author: Preyas Shah
****************dataset.py******************
"""
import numpy as np
import pandas as pd
class Dataset():
    """*Defines a class Dataset, which contains the 2D Feature Matrix
    *Calculate the various parameters related to dataset; trainingExamples(rows),
    *Number of Features, Number of empty data-entry, covariance/correlation 
    *matrix as well as perform operations like replacing invalid entry with NaN     
    """
    #Constructor
    def __init__(self, datasetMatrix):
        self.featureMatrix2D = datasetMatrix
        self.numFeatures = np.shape(self.featureMatrix2D)[1]
        self.totalTrainingExamples = np.shape(self.featureMatrix2D)[0]
    #Total Number of Rows/Training Examples
    def getTotalTrainingExamples(self):
        """Total Number of Rows/Training Examples"""
        return self.totalTrainingExamples
    #Total Number of Features
    def getNumFeatures(self):
        """Total Number of Features"""
        return self.numFeatures
    #Replace the invalid val(like -1) with NaN
    def replaceInvalidWithNaN(self,invalidVal):
        self.featureMatrix2D[self.featureMatrix2D == float(invalidVal)] = float('NaN')
    #Total number of empty data in each feature
    #Useful to strip out the features with lot of missing data
    def getEmptyColCount(self):
        return np.nansum(self.featureMatrix2D, axis=1)
    #Total number of empty data
    def getTotalEmptyCount(self):
        return np.nansum(self.featureMatrix2D)
    #Covariance Matrix vs Correlation Matrix
    #Covariance Matrix -> Use when the features are on the similar scales and 
    #Variance needs to be retained
    #Correlation Matrix -> Use when the features are on the widely different 
    #scales and eliminate possibility of some features dominance over others
    
    #Covariance Matrix
    #Numpy Covariance matrix functions does not support the NaN values,
    #Therefore, a numpy array has to be converted to the panda array before
    #Calculating the Covariance Matrix
    def getCorrelationMatrix(self):
        df = pd.DataFrame(self.featureMatrix2D)
        corrFrame = df.corr()
        return corrFrame.as_matrix
    #Correlation Matrix
    #Numpy correlation matrix functions does not support the NaN values,
    #Therefore, a numpy array has to be converted to the panda array before
    #Calculating the Correlation Matrix
    def getCovarianceMatrix(self):
        df = pd.DataFrame(self.featureMatrix2D)
        covFrame = df.cov()
        return covFrame.as_matrix
        
    