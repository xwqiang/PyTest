#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
重庆用户注册时间
'''
import sys

from dcrt.log import log

@log('execute')
def readFile(path = '/Users/xuwuqiang/Downloads/',name='chongqingxls'):
    with open(path + name,'r') as logfile:
        rowlist = [line.strip() for line in logfile.readlines()]

    return set(rowlist)

@log('execute')
def readFileMap(path = '/Users/xuwuqiang/Downloads/',name='chongqingUser'):
    d = {}
    with open(path + name,'r') as logfile:
        for line in map(lambda x : x.strip(),logfile.readlines()):
            
            if(len(line.split('\t')) != 2):
                continue
            line = line.split('\t')
            d[line[0]] = line[1]

    return d


if __name__ == "__main__":

        chongqingxls = readFile()
        allMap = readFileMap()

        print map(lambda y :  str(y) + ' : ' + str(allMap[y]) ,filter(lambda x : allMap.has_key(x),chongqingxls))







        # for line in chongqingxls :

        #     if allMap.has_key(line) :
        #         print line,allMap[line]
        #     else:
        #         print line
