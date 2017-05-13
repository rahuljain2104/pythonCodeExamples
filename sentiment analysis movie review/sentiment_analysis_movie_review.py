# to run this file following libraries needs to be installed
# pandas, numpy, scipy, unicodedata, nltk, sklearn, re, bs4

# get the data set - csv
import pandas as pd
df = pd.read_csv("movie_reviews_small.csv", encoding="ISO-8859-1")

# prepare data for training and testing
import numpy as np
X = np.array(df["review"]) # features
y = np.array(df["sentiment"]) # label

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

import unicodedata
from bs4 import BeautifulSoup
from normalization import expand_contractions, CONTRACTION_MAP, lemmatize_text, remove_special_characters, keep_text_characters, remove_stopwords

# normalization on data
def normalize_documents(documents):
    normalized_doc_list = []
    for doc in documents:
        # convert to ascii
        doc1 = unicodedata.normalize('NFKD', doc).encode('ascii', 'ignore')

        # remove tags and escape characters
        doc2 = BeautifulSoup(doc1, 'html.parser').get_text()

        # expand contractions
        doc3 = expand_contractions(doc2, CONTRACTION_MAP)

        # lemmatize of text
        doc4 = lemmatize_text(doc3)

        # remove special characters
        doc5 = remove_special_characters(doc4)

        # keep text characters
        doc6 = keep_text_characters(doc5)

        # remove stopwords
        doc7 = remove_stopwords(doc6)
        normalized_doc_list.append(doc7)
    return normalized_doc_list

# feature extraction
X_train_normalized = normalize_documents(X_train)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df=1.0, min_df=0.0, ngram_range=(1, 1))
X_train_features = tfidf_vectorizer.fit_transform(X_train_normalized)

# training the classifier
from sklearn.linear_model import SGDClassifier
# get the classifier
sgd_classifier = SGDClassifier(loss='hinge', n_iter=500).fit(X_train_features, y_train)

# validation on test set
y_predicted = sgd_classifier.predict(tfidf_vectorizer.transform(normalize_documents(X_test)))

# stats - confusion matrix, accuracy, precision and recall
from sklearn import metrics
print('{}'.format(metrics.confusion_matrix(y_true=y_test, y_pred=y_predicted)))
print('Accuracy = {}'.format(metrics.accuracy_score(y_true=y_test, y_pred=y_predicted)))
print('Precision(positive) = {}'.format(metrics.precision_score(y_true=y_test, y_pred=y_predicted, pos_label='positive')))
