import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen
from pathlib import Path
import numpy as np
import wget
import scipy
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# Download the dataset
url = 'https://s3.amazonaws.com/amazon-reviews-pds/tsv/sample_us.tsv'
my_file = Path("sample_us.tsv")

if not my_file.is_file():
    wget.download(url)
# Read the dataset

data = pd.read_csv('sample_us.tsv',delimiter='\t',encoding='utf-8')
# total length of list, this number equals total number of products
print(len(data))

# first row of the list
print(data[data.star_rating == 3])
print(data.columns)
# Split the data into
df = data[["star_rating","review_body"]]

# extract feature vectors suitable for machine learning
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(df.review_body)
print(f" Shape of x: {X_train_counts.shape}")
print(f"Word frequency: {count_vect.vocabulary_.get(u'have')}")

# From occurrences to frequencies¶
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape
print(f" Shape of x: {X_train_tfidf.shape}")

# train a linear model to perform categorization
clf = MultinomialNB().fit(X_train_tfidf, df.star_rating)
docs_new = ['To keep together, had to use crazy  glue', 'I got these for my daughters for plane trip']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, df.star_rating[category]))
# use a grid search strategy to find a good configuration of both the feature extraction components and the classifier
# Building a pipeline
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', MultinomialNB()),])
text_clf.fit(df.review_body, df.star_rating)