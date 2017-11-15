from hammingdistance import calculateHammingDistance

# XOR key against every char in input_str, concat and return result
def xor_repeating_key(input_str):
    result_str = ""

    for i in range(0, len(input_str)):
        try:
            result_str += chr(ord(input_str[i*3]) ^ ord("I"))
            result_str += chr(ord(input_str[i*3 + 1]) ^ ord("C"))
            result_str += chr(ord(input_str[i*3 + 2]) ^ ord("E"))
        except:
            return result_str.encode("hex")

    return result_str.encode("hex")


# XOR key against every char in input_str, concat and return result
def xor_single_char_key(input_str, xor_key):
    result_str = ""
    for i in range(0, len(input_str)):
        result_str += chr(ord(input_str[i]) ^ ord(xor_key[i%len(xor_key)]))

    return result_str

def xor_strings(hex_str, xor_val):
	assert(len(hex_str) == len(xor_val))
	return (int(hex_str, 16) ^ int(xor_val, 16))