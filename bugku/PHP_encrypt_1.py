#!/usr/bin/env python
# coding=utf-8

import hashlib
import base64

def eccrypt(data):
	key = hashlib.md5('ISCC').hexdigest()
	x = 0
	char = ''
	data_len = len(data)
	key_len = len(key)
	for i in range(data_len):
		if x == key_len:
			x = 0
		char += key[x]
		x += 1

	for i in range(data_len):
		flag += chr((ord(data[i]) + ord(char[i])) % 128)

	return base64.b64encode(flag)


def decrypt(b64):
	int_b64 = []
	b64ed = base64.b64decode(b64)
	for i in range(len(b64ed)):
		int_b64.append(ord(b64ed[i]))
	key = '729623334f0aa2784a1599fd374c120d729623'
	int_key = []
	for i in range(len(key)):
		int_key.append(ord(key[i]))
	flag = ''
	for i in range(len(int_b64)):
		flag += chr((int_b64[i]-int_key[i]+128)%128)
	print flag


if __name__ == '__main__':
	str_b64 = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='
	decrypt(str_b64)

