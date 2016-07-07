'''
@author: xuwuqiang
'''
# import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
# fig = plt.figure()  
# ax = fig.add_subplot(1,1,1)
def PlotDemo1():
#     fig  = plt.figure()
#     ax = fig.add_subplot(1,1,1)
    x = []
    y = []
    f = open('/Users/xuwuqiang/Documents/backyard/datas/teminalSum.csv')
    for item in f:
        value = item.split('\t')
        print value
#         x.append(value[0])
#         y.append(value[1])
    print x
    print y 
#     ax.plot([],[2,3,4,5,6])
#     plt.show()
    
if __name__ == "__main__":
    PlotDemo1()