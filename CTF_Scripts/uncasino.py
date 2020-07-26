#!/usr/bin/python

import random
import sys

first_10=sys.argv[1]
inp=first_10.split(',')
vector=[]
for j in inp:
	vector.append(int(j))
print "Entrada: "+str(first_10)

for i in xrange(1,99999):
	count=0
	random.seed(i)
	numb = int(random.randint(1,99))
	if str(numb) == str(vector[0]):
		count+=1
		for j in range(len(vector)-1):
			numb = int(random.randint(1,99))
			if str(numb) == str(vector[j+1]):
				count+=1

	if count > len(vector)-1:
		print "We've got the seed: "+str(i)+" . PEDRO, FUCK YOU!"	
		for z in range(10):
			rand_num = int(random.randint(1,99))
			print "Next Number: "+str(rand_num)
			
		exit(0)




