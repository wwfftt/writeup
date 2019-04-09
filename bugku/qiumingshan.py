#!/usr/bin/env python
# coding=utf-8

import requests
import re

#serach
# url = 'http://123.206.87.240:8002/qiumingshan/'
# s = requests.Session()
# r = s.get(url)
# result = re.search(r'(\d+[+\-*])+(\d+)', r.text)
# post = {'value': eval(result.group())}
# print(s.post(url,data=post).text)


#findall
url = 'http://123.206.87.240:8002/qiumingshan/'
s = requests.Session()
r = s.get(url)
result = re.findall('<div>(.*?)=\?;</div>',r.content)
# print result
result = "".join(result)
data = {'value': eval(result)}
flag = s.post(url, data=data)
print flag.content

