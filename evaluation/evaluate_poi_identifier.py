#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X_train, X_test, y_train, y_test = train_test_split(features, labels,test_size=0.3,random_state=42)

clf = DecisionTreeClassifier()

clf.fit(X_train,y_train)
# print(clf.score(X_test,y_test))

#for (i,y) in enumerate(clf.predict(X_test)):
#    print(y,"-",y_test[i])

# Number of poi's in test
# print(sum(y==1 for y in y_test))

y_pred = clf.predict(X_test)

from sklearn.metrics import precision_score, recall_score
print(precision_score(y_pred,y_test))
print(recall_score(y_pred,y_test))

