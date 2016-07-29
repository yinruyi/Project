#coding:utf-8
import os
import sys
import string
import codecs
import requests
import json
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

if __name__ == '__main__':
    productId = '10009683'
    pageNum = '1'
    comment_url = 'http://sclub.jd.com/productpage/p-'+productId+'-s-0-t-3-p-'+pageNum+'.html'
    # print comment_url  
    r = requests.get(comment_url)
    comment_set = json.loads(r.text)
    print comment_set['comments'],len(comment_set['comments'])

