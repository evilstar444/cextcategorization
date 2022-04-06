import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import jieba as jb
import re
import pickle


def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  

def remove_punctuation(line):
    line = str(line)
    if line.strip()=='':
        return ''
    rule = re.compile(u"[^a-zA-Z0-9\u4E00-\u9FA5]")
    line = rule.sub('',line)
    return line


def myPredict(sec):
    format_sec=" ".join([w for w in list(jb.cut(remove_punctuation(sec))) if w not in stopwords])
    pred_cat_id=clf.predict(count_vect.transform([format_sec]))
    pre=id_to_cat[pred_cat_id[0]]
    print(id_to_cat[pred_cat_id[0]])
    return pre

with open('app/model/model1.pickle', 'rb') as f:
    clf= pickle.load(f)
with open('app/model/model2.pickle', 'rb') as f:
    count_vect= pickle.load(f)
id_to_cat={0:'政治',1:'體育',2:'財經',3:'軍事',4:'科技'}
stopwords = stopwordslist("app/model/not.txt")