import binascii

def calculateHammingDistance(s1, s2):
	a = int(bin(int(binascii.hexlify(s1), 16))[2:])
	b = int(bin(int(binascii.hexlify(s2), 16))[2:])

	count = 0
	for i in range(0, len(str(a))):
		if str(a)[i] != str(b)[i]:
			count += 1
	return count

if __name__ == '__main__':
	print calculateHammingDistance("this is a test", "wokka wokka!!!") # => 37