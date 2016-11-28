from mlbase import MLBase
import configparser as cp
import matplotlib as mplot
import datetime as dt
import scipy as sp
import pandas as pd
import math
from sklearn import svm
from collections import Counter
from utils import MLUtilities as mlUtils
# First we import a function to determine the mode
from scipy.stats import mode

# todo 1. read data
# need a generalized readData function through which we can get the data
# from multiple sources and also different type of data like training, testing etc
# better create a utility function that can be called for this type of task
# code should be like a master piece
config = mlUtils.get_config_file()

# read data frame from csv file
train = mlUtils.read_csv_file(csv_file_path=config['mandatory']['train_csv_file_path'])

# read data frame, labels and features : should exist in params.ini file
label, features = mlUtils.get_labels_and_features(config)
print label
print features

# todo 2. process data
# how to deal with so many of the parameters
# deal with different type of parameters: int, float, factors
# deal with different type of values: date, NA,

# Find number of NA in the Columns
# axis=0 defines that function is to be applied on each column
print "Missing values per column:"
print train.apply(mlUtils.num_missing, axis=0)

# Find number of NA in the Rows
# axis=1 defines that function is to be applied on each row
print "Missing values per row:"
print train.apply(mlUtils.num_missing, axis=1).head(10)

print mode(train['GarageType']).mode[0]

print mlUtils.cross_tab(train, "SalePrice", "LotArea")

# Coding factors to numbers:
print 'Before Coding:'
print pd.value_counts(train["HouseStyle"])
train["HouseStyleCoded"] = mlUtils.coding(train["HouseStyle"],
                                          {'1.5Fin': 1, '1.5Unf': 2, '1Story': 3,
                                           '2.5Fin': 4, '2.5Unf': 5, '2Story': 6,
                                           'SFoyer': 7, 'SLvl': 8})
print '\nAfter Coding:'
print pd.value_counts(train["HouseStyleCoded"])




# todo 3. create final features and training set


# todo 4. fit the data set and find the classifier


# todo 5. apply the classifier on the test data and find the prediction
