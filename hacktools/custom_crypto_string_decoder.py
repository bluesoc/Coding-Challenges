#!/bin/python3
#
# This program was created to solve a challenge from pythonchallenge.com
#
# http://www.pythonchallenge.com/pc/def/map.html
#
# bluesoc (c) 2024
#

string_to_crack = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Premisses. We know that:
# 	K -> M
# 	O -> Q
# 	E -> G
#
# The actual brute force algorithm is a 
#  modification of the following code.

# Index 56 (Rotate by 56)
decoded_str = ''

for i in string_to_crack:
	if i.isalpha():

		# Calculate and correct the ASCII index
		value = ord(i) - 56

		if chr(value).isalpha() == False:
			value += 26

		value = chr(value)

		decoded_str += value
	else:
		decoded_str += i

print("\n", decoded_str)
