# Dependencies required:

*   python2.7
*    numpy
*    pandas
*    sklearn
*    nltk

Input File:

> final.json


Command Line Arguments for running different Machine Learning Configurations:

- `countsNB` [Runs Naive Bayes Classifier with Word Counts]
- `tfidfNB` [Runs Naive Bayes Classifier with TF-IDF Vectors, Laplace Smoothing and N-Grams]
- `countsLR` [Runs Logistic Regression with Word Counts]
- `tfidfLR` [Runs Logistic Regression with TF-IDF Vectors, L1 Regularization and N-Grams]

Sample command to run from code from command line:

> python classifier_code.py `<path to final.json>` `<one of four values>`

# Example python command
> python classifier_code.py ../final.json tfidfLR