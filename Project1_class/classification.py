#coding:utf-8
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import StratifiedKFold
from sklearn import cross_validation
import sys
import os
from scipy import interp
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()


def writeMatrix(dataset, Path, coding = "utf-8"):
    for i in xrange(len(dataset)):
        temp = dataset[i]
        temp = [str(temp[j]) for j in xrange(len(temp))]
        temp = ",".join(temp)
        dataset[i] = temp
    string = "\n".join(dataset)
    f = open(Path, "a+")
    line = f.write(string+"\n")
    f.close()

def getData():
    file = open("data.json",'r')
    data = json.loads(file.read())
    file.close()
    data = data['data']
    # print type(data)
    y = ["C000008","C000022","C000010","C000016","C000007","C000014","C000024",
                "C000013","C000020","C000023"]#things_tag
    # print y
    X = []#to cluster
    Tag = []
    # print data[0],type(data[0])
    for i in range(len(data)):
        temp = []
        for j in range(len(y)):
            if data[i].has_key(y[j]):
                temp.append(data[i][y[j]])
            else:
                temp.append(0)
        X.append(temp)
        Tag.append(data[i]["user_crc"])
    return np.array(X),Tag


if __name__ == '__main__':
    # X = np.random.randint(5, size=(6, 100))
    # y = np.array([1, 2, 3, 4, 5, 6])
    # print X,y
    # clf = MultinomialNB()
    # clf.fit(X, y)
    # print(clf.predict(X[2:3]))
    # print X[2:3]
    X,Tag = getData()
    kmeans_model = KMeans(n_clusters = 2).fit(X)
    y = kmeans_model.labels_
    # print X,y
    # print list(y),len(y)
    cv = StratifiedKFold(y, n_folds=2)
    clf = GaussianNB()

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []


    for i, (train, test) in enumerate(cv):
        probas_ = clf.fit(X[train], y[train]).predict_proba(X[test])
        # print probas_
        # print "train:", y[train],len(y[train]), "test:", y[test],len(y[test])
        fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
        print fpr,tpr
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0 
        roc_auc = auc(fpr, tpr)
        # print roc_auc
        plt.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
    mean_tpr /= len(cv)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    plt.plot(mean_fpr, mean_tpr, 'k--',
         label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()