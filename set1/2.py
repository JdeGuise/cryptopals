def xorStrings(hex_str, xor_val):

	return (int(hex_str, 16) ^ int(xor_val, 16))

if __name__ == '__main__':
	print hex(xorStrings('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))[2:-1]