#coding:utf-8
import os
import sys
import string
import codecs
import requests
import json
import time
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from multiprocessing.dummy import Pool as ThreadPool

def writeMatrix(dataset, Path, coding = "utf-8"):
    for i in xrange(len(dataset)):
        temp = dataset[i]
        temp = [str(temp[j]) for j in xrange(len(temp))]
        temp = "***".join(temp)
        dataset[i] = temp
    string = "\n".join(dataset)
    f = open(Path, "a+")
    line = f.write(string+"\n")
    f.close()

def write_comments(comments):
    comments_to_write = []
    for i in range(len(comments)):
        comment = comments[i]
        comments_to_write.append([comment['id'],comment['content']])
    writeMatrix(comments_to_write, 'test.txt')

def comments_pageNum(productId):
    test_url = 'http://sclub.jd.com/productpage/p-'+ productId +'-s-0-t-3-p-0.html'
    r = requests.get(test_url)
    comment_set = json.loads(r.text)
    pageNum = int(comment_set['productCommentSummary']['commentCount']*1.0/10)+1
    return pageNum

def spider_comments(productId):
    pageNum = comments_pageNum(productId)
    comments = []
    for i in range(pageNum):
        comment_url = 'http://sclub.jd.com/productpage/p-'+productId+'-s-0-t-3-p-'+str(i)+'.html'
        r = requests.get(comment_url)
        time.sleep(20)
        try:
            comment_set = json.loads(r.text)
            # comments.append(comment_set['comments'])
            write_comments(comment_set['comments'])
        except:
            print i

    print len(comments)


if __name__ == '__main__':
    # productId = '10009683'
    # spider_comments(productId)
    url = 'http://127.0.0.1:5000/'
    r = requests.get(url, proxies={'http':'http://60.251.55.158:8088'}, timeout=10) 
    # r = requests.get(url, timeout=10)
    print r.status_code

