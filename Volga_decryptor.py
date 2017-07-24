#!/usr/bin/python
import re
from itertools import izip, cycle

def xor_strings(xs, ys):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in izip(xs, cycle(ys)))

#primeras letras de la flag: VolgaCTF{
#regla del mundo del xor
#flag="VolgaCTF{"




prikey="\x94\xff\x63\xa3\x8d\x75\xd8\xc4\x1a\xc1\xca\x24\x1e\x66\x0c\x1f\xc6\xe2\xcc\xea"

enc=open("flag.enc","rb").read()
reg=re.compile("[\x20-\x7E]{119}")

test=""
#Get de prikey
'''
for i in range(20):
	for j in range(255):
		for h in range(120):
			test+=chr(ord(enc[i+20*h])^j)	
		if reg.match(test):
			print "Posible key from "+str(i)+" is "+str(j)+". Result: "+test
			test=""
		else:
			test=""

'''

print xor_strings(enc, prikey)
