#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016年7月3日

@author: xuwuqiang
'''

import requests

from db.SendMail import sendMail
import simplejson as json


def requestMeetingRoom():
    url = 'http://oa.kuyun.com/oaapi/showRoomList?userId=637'
    response = requests.get(url)
    print response
    if response.status_code != 200:
        print 'error in url ' + url
    content = response.content
    cJson = json.loads(content, "utf-8")
    cmd = cJson['cmd']
    result_code = cJson['result-code']
    if result_code != '0' :
        sendMail('OA 接口异常','error in request '+cmd)
if __name__ == '__main__':
    requestMeetingRoom()