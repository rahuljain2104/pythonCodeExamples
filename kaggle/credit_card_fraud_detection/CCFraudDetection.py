from utils import MLUtilities as util
import scipy as sp
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# read data
params = util.get_config_file()
df = util.read_csv_file(params['mandatory']['train_csv_file_path'])

# lets see the some sample data
print(df.head())

# analyze data
print("Missing values per column:")
is_null = df.apply(util.num_missing, axis=0)
print(sp.transpose(is_null))

# preparing features and labels
y = sp.array(df[[-1]])
X = sp.array(df.drop(['Class', 'Time'], 1))

# appearently there is no null value in the data frame, and all the values looks good
# divide training and test set and check no. of positives and negatives example percentage in each case
# crossvalidation and training data should contain balanced number of positive and negative examples

# divide training, cross validation data
# create training and test sets
X_train, X_cross_val, y_train, y_cross_val = train_test_split(X, y, test_size=0.3, random_state=0)

# need to find the number of 0's and 1's in
temp = 0
for y1 in y_train:
    if y1 == 1:
        temp += 1

print("number of ones in y_train : ")
print(temp)

# need to find the number of 0's and 1's in
temp = 0
for y1 in y_cross_val:
    if y1 == 1:
        temp += 1

print("number of ones in y_cross_val : ")
print(temp)

# perform classification and predict the test set
clf = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train, y_train)

# predict the values on cross validation data
y_predict = clf.predict(X_cross_val)

# find error of prediction on cross validation data
print("Accuracy :")
accuracy_score(y_cross_val, y_predict)

# lets check the false positive and false negative predictions
# absolute values will be much more helpful
false_positive = 0
false_negative = 0
for i in range(1, len(y_cross_val)):
    if y_cross_val[i] - y_predict[i] == -1:
        false_negative += 1
    if y_cross_val[i] - y_predict[i] == 1:
        false_positive += 1
print("false positive : ")
print(false_positive)

print("false negative : ")
print(false_negative)
