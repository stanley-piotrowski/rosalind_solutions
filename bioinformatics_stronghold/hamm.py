#!/usr/bin/env python3

#################
#### hamm.py ####
#################

# Take two strings of equal length and return the hamming distance- the number of differences after both sequences are aligned

# To run this program, place two DNA sequences in a file and type the following:
# ./hamm.py <input> 

# To get help on this program, type one of the following:
# ./hamm.py -h OR ./hamm.py --help

# For example, given a file with two input strings:
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Should produce the following output: 7

####################
#### Pseudocode ####
####################

# Here is the strategy for solving this problem:
# 1) Parse the file from the command line
# 2) Read both strings as separate lists
# 3) Initialize a counter, zip two lists together, and iterate over both simultaneously
# 4) If the strings don't match, add 1 to the counter
# 5) Print the resulting hamming distance

##############
#### Code ####
##############

# Define argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument
parser.add_argument("input", type = str, help = "Input file containing two DNA sequences (e.g., input_hamm.txt)")

# Execute parser
args = parser.parse_args()

# Open file handle and push two DNA sequences to lists
input = args.input
input_handle = open(input, "r")
seq1 = input_handle.readline().strip("\n")
seq2 = input_handle.readline().strip("\n")

# Use zip to iterate over two lists and print output
hamm_dist = 0
for (i, j) in zip(seq1, seq2):
	if i != j:
		hamm_dist += 1
print(hamm_dist)

# Close file handle
input_handle.close()
