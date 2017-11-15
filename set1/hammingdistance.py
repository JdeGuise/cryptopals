# @ s1: string 1 in edit distance calculation -> first 'key' bytes
# @ s2: string 2 in edit distance calculation -> second block of 'key' bytes
def calculateHammingDistance(s1, s2):
	assert(len(s1) == len(s2))

	a = bin(int(binascii.hexlify(s1), 16))[2:]
	b = bin(int(binascii.hexlify(s2), 16))[2:]

	dist = 0
	for i in range(0, len(str(a))):
		try:
			if str(a)[i] != str(b)[i]:
				dist += 1
		except:
			return dist

	return dist


if __name__ == '__main__':
	assert(calculateHammingDistance("this is a test".encode("ascii"),
									"wokka wokka!!!".encode("ascii")) == 37)