#!/bin/python3.8
import hashlib

# password: 'admin'
md5 = '21232f297a57a5a743894a0e4a801fc3'

file = open('wordlist.txt', 'r')
wordlist = file.readlines()

for word in wordlist:
	hashmd5 = hashlib.md5(word.strip().encode())
	digest = hashmd5.hexdigest()

	# This print is just for cosmetic porpourses
	print(f"{md5} <?> {digest} :: {word}\r\r", end='')

	if hashmd5.hexdigest() == md5:
		print("\033[32mHASH FOUND.", digest ,"::" , word, "\033[00m\n")
		break

file.close()