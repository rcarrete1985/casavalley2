"""
March 26th, 2019, module creates a linear regression machine learning model  that is saved as a .pkl file
for importing into other modules. Currently has an r2 coefficient of ~71%.
"""

# imports
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn import linear_model

# connect database
dat = sqlite3.connect('db.sqlite3')

# create pandas data frame from database data
df = pd.read_sql_query("SELECT valuesCAD, zestimate, finalBid FROM properties_property", dat)

# create X,y and split for testing/training
X = df.iloc[:, :-1].values
y = df.iloc[:, 2].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# create model and fit
clf = linear_model.LinearRegression()
clf.fit(X, y)

# create pkl of model to make it portable to other modules
joblib.dump(clf, 'cvestimate.pkl', compress=9)
