# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv,codecs
from matplotlib import cm
import pandas
#for python3
def open_with_pandas(filename):
    df = pandas.read_csv(filename)
    header = df.columns.values.tolist()
    data = df.values
    return df, header, data

df, header, data = open_with_pandas('./trans.csv')


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
count=0
count_kanto=0
count_kansai=0
num=len(data)
for d in data:
    count+=1
    
    if count>=11 and count<=14:
        c_k = cm.winter(float(count_kanto) / 4)
        count_kanto+=1
        ax.scatter(d[1],d[2], color=c_k, label=d[0])
    elif count>=23 and count<=30:
        c_ks= cm.hot(float(count_kansai) / 8)
        count_kansai+=1
        ax.scatter(d[1],d[2], color=c_ks, label=d[0])
    else:
        c = cm.hsv(float(count) / num)
        ax.scatter(d[1],d[2], color=c, label=d[0])
    '''
    if count==13:
        c = cm.hsv(float(count) / num)
        ax.scatter(d[1],d[2], color="red", label=unicode(d[0],'utf-8'))
    '''

ax.set_title('transportation')
ax.set_xlabel(header[1])
ax.set_ylabel(header[2])

ax.grid(True)

ax.legend(bbox_to_anchor=(1.05, 1),loc='upper left', ncol=3)
plt.savefig('trans.png', bbox_inches='tight')
