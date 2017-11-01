from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
import random
import csv
import numpy as np
import pickle

def loadDataset(filename, dataSet):
    # load the data and seperate it into train and test datasets seperately
    csvfile = open(filename, "r")
    lines = csv.reader(csvfile)
    dataTmp = list(lines)
    for x in range(len(dataTmp)-1):
        for y in range(4):
            dataTmp[x][y] = float(dataTmp[x][y])
        dataSet.append(dataTmp[x][:])



dataSet=[]
loadDataset("recording.csv",dataSet)
dataSet=np.array(dataSet)
X=dataSet[:,:-1]
y=dataSet[:,-1]
print(X)
N=(len(dataSet))
random.shuffle(dataSet)
clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2,random_state=0)
#scores = cross_val_score(clf, X, y)
#scores.mean()
#print('Avg Accuracy: ' + repr(scores.mean()))
clf.fit(X,y)
file1=open('model.data','w+')
pickle.dump(clf,file1)