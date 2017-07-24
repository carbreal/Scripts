#!/usr/bin/python
import sys
import itertools

base = "0123456789abcdefghijklmnopqrstuvwxyz";
n = 4294967297;
f=[" "]*36
#key=sys.argv[1]
code=0

for x in range(36):
	y=1+(x<<8)
	f[x]=(y*y*y)%n

for i in range(7):
	gen = itertools.product(base,repeat=i)	
	for comb in gen:
		key=''.join(comb)
		#print key
		code=0
		for y in range(len(key)):
			for x in range(36):
				if key[y]==base[x]:
					code+=f[x];
					code*=(y+1);
		#print code
		if code==425581634525:
			print "Pass found, key: "+str(key)+" code: "+str(code)
			sys.exit(0)

