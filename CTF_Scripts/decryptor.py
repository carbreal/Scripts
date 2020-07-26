#!/usr/bin/python
import sys
import itertools
import crypt

try:
	salt=sys.argv[1]
	hasher=sys.argv[2]
	length=sys.argv[3]
except:
	print "[-] USAGE: ./decryptor [SALT] [HASH] [LENGTH]"
	sys.exit(0)

base="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$%&/=+@#"
gen = itertools.product(base,repeat=int(length))

print "\nPASSWORD CRACKER\n"
print "[+] Hash: "+hasher
print "[+] Salt: "+salt
print "[+] Length: "+length
print "\n[+] Cracking password..."

for comb in gen:
	key=''.join(comb)
	if crypt.crypt(key,salt) == hasher:
		print "[+] Password found: "+str(key)
		sys.exit(0)

print "[-] Password not found."
