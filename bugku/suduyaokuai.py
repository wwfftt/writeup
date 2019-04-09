#!/usr/bin/env python
# coding = utf-8

import requests
import base64

url = 'http://123.206.87.240:8002/web6/'
s = requests.Session()
headers = s.get(url).headers

mid = base64.b64decode(headers['flag'])   #获取响应头里的flag
mid = repr(mid)     #将obj转化为str

flag = base64.b64decode(mid.split(':')[1])
data = {'margin':flag}

text = s.post(url,data=data).text

print text