#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import pickle

def savebypickle(res,file):
    f = open(file, 'wb')
    pickle.dump(res, f)
    f.close()

def getbypickle(file):
    f=open(file,'rb')
    res=pickle.load(f)
    f.close()
    return res
