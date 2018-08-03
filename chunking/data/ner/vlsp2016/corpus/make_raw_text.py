from __future__ import print_function

import os 

with open("test.txt", "r") as f:
	# raw_data = [[line.split("\t")[0] for sentence in f.read().split('\n\n') for line in sentence.split("\n")]]
	sentences = [sentence.split("\n") for sentence in f.read().split("\n\n")]
	raw_data = [[line.split("\t")[0] for line in sentence] for sentence in sentences]

for xxx in raw_data:
	print(" ".join(xxx))
