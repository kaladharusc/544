import sys
import json
import csv
import numpy as np
import pandas as pd
import re
import nltk
import time
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import warnings
from pandas import Series
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.metrics import classification_report, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def countsNB(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['data'])
    X_train, X_test, y_train, y_test = train_test_split(X.toarray(), df['label'], test_size=0.25, stratify=df['label'])

    parameters = {}
    model = MultinomialNB()
    clf = GridSearchCV(model, parameters, cv=5, scoring='f1_weighted')
    clf.fit(X_train, y_train)
    print("\n")
    print("Cross Validation Weighted F1 Score: {}".format(clf.best_score_))
    y_pred = clf.predict(X_test)

    print("\n\n")
    print("Classification Report:")
    print(classification_report(y_pred=y_pred, y_true=y_test))

def tfidfNB(df):
    tfidf = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'[a-z]{3,}',
    stop_words='english',
    ngram_range=(1, 2),
    max_features=500)

    tfidf.fit(df['data'])
    X = tfidf.transform(df['data'])
    X_train, X_test, y_train, y_test = train_test_split(X.toarray(), df['label'], test_size=0.25, stratify=df['label'])

    parameters = {'alpha':[0.1,0.2,0.5,0.7,1.0]}
    model = MultinomialNB()
    clf = GridSearchCV(model, parameters, cv=5, scoring='f1_weighted')
    clf.fit(X_train, y_train)
    print("\n")
    print("Cross Validation Weighted F1 Score: {}".format(clf.best_score_))
    y_pred = clf.predict(X_test)

    print("\n\n")
    print("Classification Report:")
    print(classification_report(y_pred=y_pred, y_true=y_test))

def countsLR(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['data'])
    X_train, X_test, y_train, y_test = train_test_split(X.toarray(), df['label'], test_size=0.25, stratify=df['label'])

    parameters = {'C':[0.01,0.1,1,10]}
    model = LogisticRegression(penalty='l1')
    clf = GridSearchCV(model, parameters, cv=3, scoring='f1_weighted')
    clf.fit(X_train, y_train)
    print("\n")
    print("Cross Validation Weighted F1 Score: {}".format(clf.best_score_))
    y_pred = clf.predict(X_test)

    print("\n\n")
    print("Classification Report:")
    print(classification_report(y_pred=y_pred, y_true=y_test))

def tfidfLR(df):
    tfidf = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'[a-z]{3,}',
    stop_words='english',
    ngram_range=(1, 3),
    max_features=500)

    tfidf.fit(df['data'])
    X = tfidf.transform(df['data'])
    X_train, X_test, y_train, y_test = train_test_split(X.toarray(), df['label'], test_size=0.25, stratify=df['label'])

    parameters = {'C':[0.01,0.1,1,10]}
    model = LogisticRegression(penalty='l1')
    clf = GridSearchCV(model, parameters, cv=3, scoring='f1_weighted')
    clf.fit(X_train, y_train)
    print("\n")
    print("Cross Validation Weighted F1 Score: {}".format(clf.best_score_))
    y_pred = clf.predict(X_test)

    print("\n\n")
    print("Classification Report:")
    print(classification_report(y_pred=y_pred, y_true=y_test))

if __name__ == "__main__":
    filename = sys.argv[1]
    _code = sys.argv[2]
    
    warnings.filterwarnings('ignore')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')
    
    with open(sys.argv[1], "r") as json_data:
        json = json.load(json_data)

    df = pd.DataFrame(columns=['data', 'label'])

    for x in json['corpus']:
        df = df.append(pd.DataFrame([[x['data'], x['label']]], columns=['data', 'label']))
    df.reset_index(drop=True, inplace=True)

    df = df[df.label != '#']

    df.reset_index(drop=True, inplace=True)

    print("\n\n")
    print("Class Distribution:")
    print(np.round(df.label.value_counts()/(float(df.label.value_counts().sum())/100), 2))
    
    if _code == 'countsNB':
        print("\n")
        print("Running Naive Bayes Classifier with Word Counts")
        countsNB(df)
    elif _code == 'tfidfNB':
        print("\n")
        print("Running Naive Bayes Classifier with TF-IDF Vectors, Laplace Smoothing and N-Grams")
        tfidfNB(df)
    elif _code == 'countsLR':
        print("\n")
        print("Running Logistic Regression with Word Counts")
        countsLR(df)
    elif _code == 'tfidfLR':
        print("\n")
        print("Running Logistic Regression with TF-IDF Vectors, L1 Regularization and N-Grams")
        tfidfLR(df)