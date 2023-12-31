# -*- coding: utf-8 -*-


import sys

#n-gram的n值
n = int(sys.argv[1])
print("n = ", n)

import pandas as pd

origin = pd.read_csv("data.csv")
#origin = pd.read_csv("test.csv")

from infrastructure.mydict import MyDict

mdict = MyDict()

feature = origin["Feature"].str.split("|")
total = len(feature)
for i, code in enumerate(feature):
    mdict.newLayer()
    if not type(code) == list:
        continue
    for method in code:
        length = len(method)
        if length < n:
            continue
        for start in range(length - (n - 1)):
            end = start + n
            mdict.mark(method[start:end])
    print("已完成", i, "个应用，百分比如下：")
    print((i + 1) * 100 / total, "%")
            
result = mdict.dict
pd.DataFrame(result, index=origin.index)\
               .to_csv("./" + str(n) + "_gram.csv", index=False)
            
        
        
        

