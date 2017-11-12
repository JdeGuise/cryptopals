#!/usr/bin/env python

import sys

def score(xor_string):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    score = 0
    for i in xor_string:
        if i in charset or i == ' ' or i == '\'':
            score += 1
    return score

# XOR key against every char in input_str, concat and return result
def xor(input_str, xor_key):
    result_str = ""
    for i in range(0, len(input_str)):
        result_str += chr(ord(input_str[i]) ^ ord(xor_key[i%len(xor_key)]))

    return result_str

def decodeHex():
    best_str = ""
    best_score = 0

    with(open(sys.argv[1], "r")) as f:
	    for i in f:
		    for j in range(1, 256):
		        this_str = xor(i.strip().decode("hex"), chr(j))
		        if score(this_str) > best_score:
		            best_score = score(this_str)
		            best_str = this_str

    print "Plaintext: {}".format(best_str)

if __name__ == "__main__":
	decodeHex()