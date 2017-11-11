#!/usr/bin/env python

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

def decodeHex(input_str):
    best_str = ""
    best_score = 0

    # bruteforce all possible values
    for i in range(1, 256):
        this_str = xor(input_str.decode("hex"), chr(i))
        if score(this_str) > best_score:
            best_score = score(this_str)
            best_str = this_str

    print "Plaintext: {}".format(best_str)

if __name__ == "__main__":
    decodeHex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")