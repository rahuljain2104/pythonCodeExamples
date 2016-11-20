import scipy as sp
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np

try:
    numberClassifier = pickle.load(open("numberClassifier.pickle", "rb"))
except (OSError, IOError) as e:
    # read training data from the csv file
    df = pd.read_csv('D:\codes\datasets\kaggle\\numberClassification\\train.csv')

    # seperate  features('X') and label('y')
    y = sp.array(df[['label']])
    X = sp.array(df.drop(['label'], 1))

    # divide training, cross validation data
    X_train, X_cross_val, y_train, y_cross_val = train_test_split(X, y, test_size=0.0, random_state=0)

    # train the data and obtain the parameters/theta
    # this is multi class classification one versus all, so probably we want to obtain the
    # classification parameters for all the different digits and
    # Linear Equation goes like : y = theta*X
    numberClassifier = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train, y_train)

    # store data to some variable so that not every time needs to read file
    # its good to save the classifier because for every prediction  we do
    # not want to entire training process
    with open('numberClassifier.pickle', 'wb') as f:
        pickle.dump(numberClassifier, f)
        f.close()

    # predict the values on cross validation data
    y_predict = numberClassifier.predict(X_cross_val)

    # find error of prediction on cross validation data
    accuracy_score(y_cross_val, y_predict)

# load the classifier
# numberClassifier = pickle.load(numberClassifier)

# finally test the hypothesis on the test data
# find the percentage of correct classification
# check if particular digit is classified properly
df_X_test = pd.read_csv('D:\codes\datasets\kaggle\\numberClassification\\test.csv')

X_test = sp.array(df_X_test)
res = map(int, numberClassifier.predict(X_test))

result = sp.vstack((map(int, (range(1, len(res) + 1))), res)).T

with open("result.csv", "wb") as f:
    f.write(b'ImageId,Label\n')
    sp.savetxt(f, result.astype(int), fmt='%i', delimiter=",")
