# questions that will probably end up fucking me up:
#
# 	does the encryption include new lines?
#		we get to figure it out! hooray!


#instead of iterating over the hexadecimal string, decoding the string to bytecode, then iterating over with a single character and de-XORing each character, appending, and returning the result, we need to do the opposite:
#
# iterate over our string, three chars at a time.
# foreach of the 3, XOR against I, C, or E, and append to string




import sys

def score(xor_string):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    score = 0
    for i in xor_string:
        if i in charset or i == ' ' or i == '\'':
            score += 1
    return score

# XOR key against every char in input_str, concat and return result
def xor(input_str):
    result_str = ""

    for i in range(0, len(input_str)/2):
        try:
            result_str += chr(ord(input_str[i*3]) ^ ord("I"))
            result_str += chr(ord(input_str[i*3 + 1]) ^ ord("C"))
            result_str += chr(ord(input_str[i*3 + 2]) ^ ord("E"))
        except:
            return result_str.encode("hex")

    return result_str.encode("hex")

def decodeHex(param):
    best_str = ""
    best_score = 0

    this_str = xor(param)

    if score(this_str) > best_score:
        best_score = score(this_str)
        best_str = this_str

    print "Plaintext: {}".format(best_str)

if __name__ == "__main__":
	decodeHex("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")

# iterate every 3 elements
# for i * 3 in range(0, endresult):
# 	I => array[i]
# 	C => array[i+1]
# 	E => array[1+2]