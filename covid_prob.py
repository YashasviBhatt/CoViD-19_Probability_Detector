# importing libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


# reading data
dF = pd.read_csv('data.csv')
X = dF.iloc[0:,0:5]                                 # extracting features
Y = dF.iloc[0:,5]                                   # extracting label

# splitting data into training and testing
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3)

# converting dataframes to numpy array
train_X = train_X.to_numpy()
test_X = test_X.to_numpy()
train_Y = train_Y.to_numpy().reshape(699,)          # reshaping to rows
test_Y = test_Y.to_numpy().reshape(300,)            # reshaping to rows

# training model using logistic regression
clf = LogisticRegression()
clf.fit(train_X, train_Y)

# saving trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

# testing model on a dummy model
input_features = [100, 1, 22, 1, 1]
print(clf.predict_proba([input_features]))
print(clf.predict_proba([input_features])[0])
infProb = clf.predict_proba([input_features])[0][1]
print(infProb)