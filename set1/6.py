#!/usr/bin/env python
from __future__ import division
from hammingdistance import calculate_hamming_distance
import binascii
import sys

# "main"
def break_repeating_key_xor():

	edit_dist_list = dict()
	chomped_input = ""
	block_pieces = list()
	with(open("6.txt", "r")) as input_file:
		for line in input_file:
			chomped_input += line
			for keysize in range(2, 41):
				# divide hamming distance results by key, then add to list
				# param 1: initial compared string for hamming distance
				# param 2: comparison string for hamming distance
				# params must be of equal length
				# params should be the first and second KEYSIZE worth of vals
				# in our input_file line
				# ?? how can we correlate our appended result with its key?
				# print "Numbah1: ", line[:keysize]
				# print "Numbah2: ", line[keysize:(2*keysize)], "\n"
				#
				# normalizing result
				edit_dist_list[keysize] = calculate_hamming_distance(line[:keysize], line[keysize:(2*keysize)])/keysize

			# iterate through keys
			for key in list(edit_dist_list.keys()):
				if edit_dist_list[key] == 0.0:
					del edit_dist_list[key]

		keysize = min(edit_dist_list, key=edit_dist_list.get)

	for i in range(0, len(chomped_input), keysize):
		block_pieces.append(chomped_input[i:i+keysize])

	# cipher broken up into chunks of size KEYSIZE
	print block_pieces




if __name__ == '__main__':
	assert(calculate_hamming_distance("this is a test".encode("ascii"),
									"wokka wokka!!!".encode("ascii")) == 37)

	print break_repeating_key_xor()

	# assert(break_repeating_key_xor() == "")