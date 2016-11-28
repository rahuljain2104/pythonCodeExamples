from mlbase import MLBase
import configparser as cp
import matplotlib as mplot
import datetime as dt
import scipy as sp
import pandas as pd
import math
from sklearn import svm

from collections import Counter


class TitanicDisaster(MLBase):
    def get_data(self, file_path):
        ml = MLBase()
        data = ml.read_csv_data(file_path)
        return data

    # # mutual information : to find how much variables are interdependent
    # def mutual_information(self,var1,var2):
    #
    #
    #
    #     # probability distribution of var1 and var2
    #
    #     # need to find joint probability distribution

    # def entropy(self, labels):
    #     """ Computes entropy of 0-1 vector. """
    #     n_labels = len(labels)
    #
    #     if n_labels <= 1:
    #         return 0
    #
    #     counts = sp.bincount(map(int, labels))
    #     myList = map(float, counts)
    #     probs = [x / n_labels for x in myList]
    #     n_classes = len(probs)
    #
    #     if n_classes <= 1:
    #         return 0
    #     return - sp.sum(probs * sp.log(probs)) / sp.log(n_classes)

    def eta(self, data, unit='natural'):
        base = {
            'shannon': 2.,
            'natural': math.exp(1),
            'hartley': 10.
        }

        if len(data) <= 1:
            return 0

        counts = Counter()

        for d in data:
            counts[d] += 1

        probs = [float(c) / len(data) for c in counts.values()]
        probs = [p for p in probs if p > 0.]

        ent = 0

        for p in probs:
            if p > 0.:
                ent -= p * math.log(p, base[unit])

        return ent


config = cp.ConfigParser()
config.read("params.ini")
train_csv_file_path = config['mandatory']['train_csv_file_path']
test_csv_file_path = config['mandatory']['test_csv_file_path']

ship = TitanicDisaster()

# data reading from csv file as a data frame
ship_data = ship.get_data(train_csv_file_path)

# prepare X and y variable
family_members = ship_data['Parch'] + ship_data['SibSp']

X = ship_data[['Survived', 'Sex', 'Pclass', 'Age', 'Embarked']]
X['family'] = pd.Series(family_members, index=X.index)
X = X.dropna()

from sklearn import preprocessing
import pickle

# processing data columns so can be used to fit the classifier
le_sex = preprocessing.LabelEncoder()
# to convert into numbers
X.Sex = le_sex.fit_transform(X.Sex)
# pickle.dump(le_sex)

le_embarked = preprocessing.LabelEncoder()
# to convert into numbers
X.Embarked = le_embarked.fit_transform(X.Embarked)

# to convert back
# X.Sex = le_sex.inverse_transform(X.Sex)

X = X.dropna()

y = X['Survived']

X = sp.array(X.drop(['Survived'], 1))

clf = svm.SVC()
clf.fit(X, y)

#################################
# Now need to test the data and check the hypothesis
ship_test_data = ship.get_data(test_csv_file_path)

# prepare X and y variable
family_members = ship_test_data['Parch'] + ship_test_data['SibSp']

X_test = ship_test_data[['Sex', 'Pclass', 'Age', 'Embarked']]
X_test['family'] = pd.Series(family_members, index=X_test.index)

le_sex = preprocessing.LabelEncoder()
# to convert into numbers
X_test.Sex = le_sex.fit_transform(X_test.Sex)

le_embarked = preprocessing.LabelEncoder()
# to convert into numbers
X_test.Embarked = le_embarked.fit_transform(X_test.Embarked)

accuracy = clf.predict(X_test.dropna())

print accuracy
