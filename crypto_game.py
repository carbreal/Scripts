#!/usr/bin/python

import random
import base64
import sys

####ENCRIPTION
rng=random.randint(1000,9999)
random.seed(rng)
#flag="flag{$0y0ul1k3crypt0?}"
flag=sys.argv[1]
enc=""
for i in flag:
	ciph=ord(i)^random.randint(1,99)
	random.randint(1,99)
	ln=len(str(ciph))
	it=str(ln)+str(ciph)
	enc=enc+it

enc=enc+str(rng)
print enc
enc=base64.b64encode(enc)
print enc

####DECRIPTION
enc=base64.b64decode(enc)
rng2=enc[-4:]
enc_new=enc[:-4]

random.seed(int(rng2))
finished=0
sol=""
while(finished==0):
	lngf=enc_new[:1]
	enc_new=enc_new[1:]
	num=enc_new[:int(lngf)]
	enc_new=enc_new[int(lngf):]
	sol=sol+str(chr(int(num)^random.randint(1,99)))
	random.randint(1,99)
	if len(enc_new)<2:
		finished=1
	
print sol
