# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:22:33 2017

@author: Preyas Shah
"""
import numpy as np
import matplotlib.pyplot as plt

class Feature():
    
    def __init__(self, valArray, name):
        self.valArray = valArray
        self.name = name
    def getValArray(self):
        return self.valArray
    def getName(self):
        return self.name
    def plot():
        pass

class BinFeature(Feature):
    def __init__(self, valArray, name='bin_feature'):
        Feature.__init__(self,valArray, name)
        self.noOfTrue = 0
        self.noOfFalse = 0
        self.noOfMissing = 0
        self.populateInformation()
    def populateInformation(self):
        featArray = self.getValArray()
        unique, counts = np.unique(featArray[~np.isnan(featArray)], return_counts=True)
        valMap = dict(zip(unique, counts))
        for key in sorted(valMap):
            if(int(key) == 0):
                self.noOfFalse = valMap[key]
            elif(int(key) != 0):
                self.noOfTrue = valMap[key]
        self.noOfMissing = np.count_nonzero(np.isnan(featArray))
    def plot(self):
        objects = ('True', 'False')
        y_pos = np.arange(len(objects))
        performance = [self.noOfTrue, self.noOfFalse]
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Count')
        plt.title(self.getName())
    def isBinary(self):
        return True
    def isCategory(self):
        return False
    def isContinuous(self):
        return False
    def toStr(self):
        strRep = "Name: "  + self.getName() + "\n" + \
              "Total: " + str(len(self.getValArray())) + "\n" + \
              "True: " + str(self.noOfTrue) + "\n" + \
              "False: " + str(self.noOfFalse) + "\n" + \
              "Missing: " + str(self.noOfMissing)
        return strRep
class CatFeature(Feature):
    def __init__(self, valArray, name='cat_feature'):
        Feature.__init__(self,valArray, name)
        self.noOfCategory = 0
        self.categoryCount = []
        self.categoryVals = []
        self.noOfMissing = 0
        self.populateInformation()
    def populateInformation(self):
        featArray = self.getValArray()
        unique, counts = np.unique(featArray[~np.isnan(featArray)], return_counts=True)
        valMap = dict(zip(unique, counts))
        self.noOfCategory = len(valMap)
        for key in sorted(valMap):
            self.categoryCount.append(valMap[key])
            self.categoryVals.append(int(key))
        self.noOfMissing = np.count_nonzero(np.isnan(featArray))
    def plot(self):
        y_pos = np.arange(len(self.categoryVals))
        performance = self.categoryCount
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, self.categoryVals)
        plt.ylabel('Count')
        plt.title(self.getName())
    def isBinary(self):
        return False
    def isCategory(self):
        return True
    def isContinuous(self):
        return False
    def toStr(self):
        strRep = "Name: " + self.getName() +  "\n" + \
              "Total: " + str(len(self.getValArray())) + "\n" + \
              "Category Values: "+ str(self.categoryVals) + "\n"+ \
              "Category Count: "+ str(self.categoryCount) + "\n"+ \
              "Missing: "+ str(self.noOfMissing)
        return strRep
class ContinuousFeature(Feature):
    def __init__(self, valArray, name='bin_feature'):
        Feature.__init__(self,valArray, name)
        self.mean = 0
        self.median = 0
        self.stddev = 0
        self.min = 0
        self.max = 0
        self.noOfMissing = 0
        self.populateInformation()
    def populateInformation(self):
        featArray = self.getValArray()
        self.mean = np.nanmean(featArray)
        self.median = np.nanmedian(featArray)
        self.stddev = np.nanstd(featArray)
        self.min = np.nanmin(featArray)
        self.max = np.nanmax(featArray)
        self.noOfMissing = np.count_nonzero(np.isnan(featArray))
    def plot(self):
        np.random.seed(19680801)
        x = self.mean + self.stddev * np.random.randn(10000)
        # the histogram of the data
        n, bins, patches = plt.hist(x, bins='auto', normed=1, color='g')
        plt.xlabel('Range')
        plt.ylabel(self.getName())
        plt.title('Histogram of '+ self.getName())
        #plt.text(self.mean - 2 * self.stddev, .15, r'$\mu=',str(self.mean),',\ \sigma=',str(self.stddev),'$')
        plt.axis([self.mean - 5 * self.stddev, self.mean + 5 * self.stddev, 0, 0.2])
        plt.show()
    def isBinary(self):
        return False
    def isCategory(self):
        return False
    def isContinuous(self):
        return True
    def toStr(self):
        strRep = "Name: "  + self.getName() + "\n" + \
              "Total: " + str(len(self.getValArray())) + "\n" + \
              "Minimum: " + str(self.min) + "\n" + \
              "Maximum: " + str(self.max) + "\n" + \
              "Mean: " + str(self.mean) + "\n" + \
              "Median: " + str(self.median) + "\n" + \
              "Standard Deviation: " + str(self.stddev) + "\n"+ \
              "Missing: " + str(self.noOfMissing)
        return strRep