#!/usr/bin/env python
from score import score
from xor import xor_single_char_key
import sys

def decode_hex():
    bestStr = ""
    bestScore = 0

    with(open(sys.argv[1], "r")) as f:
	    for i in f:
		    for j in range(1, 256):
		        thisStr = xor_single_char_key(i.strip().decode("hex"), chr(j))
		        if score(thisStr) > bestScore:
		            bestScore = score(thisStr)
		            bestStr = thisStr

    return "Plaintext: {}".format(bestStr)

if __name__ == "__main__":
    assert(decode_hex() == "Plaintext: Now that the party is jumping\n")