#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
智能机顶盒用户id
'''
import os

import MySQLdb
from  MySQLdb.cursors import DictCursor

fileSuffix = '.log'
def getUserIdsFromDB(date=201501):  # @DontTrace
        try:
                # conn=MySQLdb.connect(host='localhost',port=3304,user='root',passwd='xuwuqiang',db='kytv_user')
                conn=MySQLdb.connect(host='172.21.19.72',port=3313,user='kytv_au',passwd='58LQMRlCeT',db='kytv_audio')
                cur=conn.cursor(DictCursor)
                sql= "SELECT certificate_code FROM tvlogo_certificatecode WHERE vendor_id = 'konka' AND DATE_FORMAT(create_time, '%Y%m') = "+str(date)
                print "connected ! and sql is :" + sql
                cur.execute(sql)
                userIds = set([])
                for item in cur:
                    userIds.add(str(item['certificate_code']))
                cur.close()
                conn.close()
                return userIds
        except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def dealLogs(productId):
    cmd = "find /ky/shark/hive/warehouse/uniqsocketboxsubscribe -type f -mtime -180 -name 'uniqsocketboxsubscribe*' | xargs cat | awk -F '|' '$1==" + str(productId) + "{print $2}' | sort | uniq > /ky/data/tvstat/temp/" + str(productId) + fileSuffix
    os.system(cmd)
    
def readFile(path = '/Users/xuwuqiang/Downloads/',name='test.log'):

    rowlist = [line.strip() for line in open(path + name).readlines() if line != '\n']

    return set(rowlist)


if __name__ == "__main__":
        
    
#         get ids from logs
        all = readFile(name='2015最近六个月有激活')
        a1 = readFile(name='201501注册')
        # a2 = readFile(name='201502注册')
        # a3 = readFile(name='201503注册')
        # a4 = readFile(name='201504注册')
        # a5 = readFile(name='201505注册')
        # a6 = readFile(name='201506注册')
        # a7 = readFile(name='201507注册')
        # a8 = readFile(name='201508注册')
        # a9 = readFile(name='201509注册')
        # a10 = readFile(name='201510注册')
        # a11 = readFile(name='201511注册')
        # a12 = readFile(name='201512注册')
#         query UserIds from db
        
#         print 'result:' + str(a1 - all)
        print '2015-01:' + str(len((a1 - all)))
        # print '2015-02:' + str(len((a2 - all)))
        # print '2015-03:' + str(len((a3 - all)))
        # print '2015-04:' + str(len((a4 - all)))
        # print '2015-05:' + str(len((a5 - all)))
        # print '2015-06:' + str(len((a6 - all)))
        # print '2015-07:' + str(len((a7 - all)))
        # print '2015-08:' + str(len((a8 - all)))
        # print '2015-09:' + str(len((a9 - all)))
        # print '2015-10:' + str(len((a10 - all)))
        # print '2015-11:' + str(len((a11 - all)))
        # print '2015-12:' + str(len((a12 - all)))
        
        
        
#        如何知道方法参数的传入 