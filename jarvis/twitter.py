import os
from nltk import word_tokenize,sent_tokenize
import numpy as np
import nltk
import pandas as pd
nltk.download('punkt')
from nltk import pos_tag

training_data=pd.read_csv("C:\\Users\\Naman Crist\\Desktop\\machine learning\\training_twitter_x_y_train.csv")
training_data["text"][1:15]

testing_data=pd.read_csv("C:\\Users\\Naman Crist\\Desktop\\machine learning\\test_twitter_x_test.csv")
testing_data["text"][1:15]

xtrain=training_data["text"]
type(xtrain)

xtest=testing_data["text"]
xtest=np.array(xtest)
xtest=xtest.reshape(len(xtest),1)
xtest.shape

ytrain=training_data['airline_sentiment']
x_train=np.array(xtrain)
y_train=np.array(ytrain)
x_train=x_train.reshape(len(x_train),1)
y_train=y_train.reshape(len(y_train),1)
x_train.shape,y_train.shape

train=np.append(x_train,y_train,axis=1)
test=xtest

documents = []
c=0
for text,category in train:
    c+=1
    documents.append((word_tokenize(text), category))
documents[0:5]

test_documents = []
c=0
for text in test:
    c+=1
    test_documents.append(word_tokenize(str(text)))
test_documents[0:5]

import random
random.shuffle(documents)
documents[0:5]

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from nltk.corpus import wordnet
def get_simple_pos(tag):
    
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

from nltk.corpus import stopwords
import string
stops = set(stopwords.words('english'))
punctuations = list(string.punctuation)
stops.update(punctuations)
#stops, string.punctuation

def clean_review(words):
    output_words = []
    for w in words:
        if w.lower() not in stops:
            pos = pos_tag([w])
            clean_word = lemmatizer.lemmatize(w, pos = get_simple_pos(pos[0][1]))
            output_words.append(clean_word.lower())
    return output_words



documents = [(clean_review(document), category) for document, category in documents]
test_documents = [clean_review(document) for document in test_documents]
training_documents=documents
testing_documents=test_documents
all_words= []
for doc in training_documents:
    all_words += doc[0]
freq=nltk.FreqDist(all_words)
common = freq.most_common(1000)
features = [i[0] for i in common]
def get_feature_dict(words):
    current_feature={}
    word_set=set(words)
    for w in features:
        current_feature[w]=w in word_set
    return current_feature
output=get_feature_dict(training_documents[0][0])
training_data = [(get_feature_dict(doc), category) for doc, category in documents]
testing_data = [get_feature_dict(doc) for doc in testing_documents]
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
classifier_sklearn1 = SklearnClassifier(rfc)
classifier_sklearn1.train(training_data)
randomforest=classifier_sklearn1.classify_many(testing_data)
randomforest=np.array(randomforest)
np.savetxt("randomforestabc.csv",randomforest, fmt='%s',encoding=None)