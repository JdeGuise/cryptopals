#!/usr/bin/env python
from xor import xor_single_char_key
from score import score

def decode_hex(inputStr):
    bestStr = ""
    bestScore = 0

    # bruteforce all possible values
    for i in range(1, 256):
        thisStr = xor_single_char_key(inputStr.decode("hex"), chr(i))
        if score(thisStr) > bestScore:
            bestScore = score(thisStr)
            bestStr = thisStr

    return "Plaintext: {}".format(bestStr)

if __name__ == "__main__":

    assert(decode_hex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736") == "Plaintext: Cooking MC's like a pound of bacon")