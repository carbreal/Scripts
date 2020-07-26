#!/usr/bin/python
import hashlib
import sys

finished=0
salt=sys.argv[1]
for i in xrange(int('00000', 16), int('100000', 16)):
	plaintxt=salt+hex(i)[2:].rjust(5, '0')
	#print plaintxt
	if bin(int(hashlib.sha1(plaintxt).hexdigest(),16))[-26:]=='11111111111111111111111111':
		print "Hash found "+plaintxt
		sys.exit(0)
	#print str(bin(int(hashlib.sha1(plaintxt).hexdigest(),16)))
