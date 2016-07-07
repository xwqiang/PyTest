#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendMail(subject,content,sendTo='xu.wuqiang@kuyun.com'):
	# 第三方 SMTP 服务
	mail_host="smtp.exmail.qq.com"  #设置服务器
	mail_user="oa@kuyun.com"	#用户名
	mail_pass="Tenfen1234"   #口令 

	sender = 'oa@kuyun.com'
	receivers = [sendTo]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

	message = MIMEText(content, 'plain', 'utf-8')
	message['From'] = Header("oa预警", 'utf-8')
	message['To'] =  Header(sendTo, 'utf-8')

	message['Subject'] = Header(subject, 'utf-8')


	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)	# 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)  
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"

if __name__ == "__main__":
	sendMail('mysubject','mycontent')
