# following packages needs to be preinstalled in the machine to run this file
# scipy, numpy, pandas, skearn packages inside python

# get the data from https://www.kaggle.com/c/digit-recognizer/data and store the csv file
# in local. Provide the same path in main method

# please reach out to rahuljain2104@gmail.com in case of difficulty

class DataProcessing:
    def __init__(self, file_path):
        self.csv_file_path = file_path
        self.data_frame = None
        self.features = None
        self.label = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def get_data_from_csv(self):
        # get the data
        import pandas
        self.data_frame = pandas.read_csv(self.csv_file_path)

    def get_features_and_label(self):
        # get the features and label
        import numpy
        self.label = numpy.array(self.data_frame["label"])
        self.features = numpy.array(self.data_frame.drop(["label"], 1))

    def do_scaling(self):
        # do the processing on the features
        from sklearn.preprocessing import scale
        self.features = scale(self.features)

    def split_train_and_test_data(self):
        # split the train and test data
        from sklearn.model_selection import train_test_split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.features, self.label, test_size=0.3)


class ClassificationAlgorithms:
    def __init__(self):
        self.classifier = None

    def get_classifier(self, classifier_type, X_train, y_train):
        # get/train the classifier
        if classifier_type == 'ovr':
            from sklearn.multiclass import OneVsRestClassifier
            from sklearn.svm import LinearSVC
            self.classifier = OneVsRestClassifier(LinearSVC()).fit(X_train, y_train)

        if classifier_type == 'knn':
            from sklearn import neighbors
            self.classifier = neighbors.KNeighborsClassifier().fit(X_train, y_train)

        if classifier_type == 'lr':
            from sklearn import linear_model
            self.classifier = linear_model.LogisticRegression().fit(X_train,y_train)

    def calculate_score(self, X_test, y_test):
        # calculate the classifier
        print(self.classifier.score(X_test, y_test))


def main():
    # get the data from https://www.kaggle.com/c/digit-recognizer/data and store the csv file
    # in local. Provide the same path in below line
    dp = DataProcessing("{path for train.csv}")
    dp.get_data_from_csv()
    dp.get_features_and_label()
    dp.do_scaling()
    dp.split_train_and_test_data()

    classification_obj = ClassificationAlgorithms()
    classification_obj.get_classifier('ovr', dp.X_train, dp.y_train)
    classification_obj.calculate_score(dp.X_test, dp.y_test)

    classification_obj.get_classifier('knn', dp.X_train, dp.y_train)
    classification_obj.calculate_score(dp.X_test, dp.y_test)

    classification_obj.get_classifier('lr', dp.X_train, dp.y_train)
    classification_obj.calculate_score(dp.X_test, dp.y_test)

main()