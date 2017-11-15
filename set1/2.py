#!/usr/bin/env python
from xor import xor_strings

if __name__ == '__main__':

	assert(hex(xor_strings('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))[2:-1] == "746865206b696420646f6e277420706c6179")