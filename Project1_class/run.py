#coding:utf-8
import json
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

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

def clustering_drawing():
    X,Tag = getData()

    n = 3
    kmeans_model = KMeans(n_clusters = n).fit(X)
    labels = kmeans_model.labels_
    score = metrics.silhouette_score(X, labels, metric='euclidean')

    scoreList = [score] 
    nList = [3,4,5,6,7,8,9]

    for i in range(4,10):# 聚类4-10类循环
        # print i
        kmeans_model_temp = KMeans(n_clusters=i).fit(X)
        labels_temp = kmeans_model_temp.labels_
        score_temp = metrics.silhouette_score(X, labels_temp, metric='euclidean')
        print i,score_temp
        scoreList.append(float(score_temp))
        if float(score_temp) > score:
        	kmeans_model = kmeans_model_temp
        	labels = labels_temp
        	n = i
    print n,labels
    plt.axis([3,9,0.8,1.0])
    plt.plot(nList, scoreList, 'r--')
    plt.show()	

def clustering_result():
    X,Tag = getData()

    n = 4# 四类
    kmeans_model = KMeans(n_clusters = n).fit(X)
    labels = kmeans_model.labels_	
    print labels

if __name__ == '__main__':
	clustering_result()
    


