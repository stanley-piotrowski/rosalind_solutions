#!/usr/bin/env python3

#################
#### revc.py ####
#################

# Given a DNA string, return the reverse complement

# To run this program, place a DNA string in an input file and type the following:
# ./revc.py <input>

# To print help documentation on this program, type one of the following:
# ./revc.py -h OR ./revc.py --help

# For example, an input file with the following DNA string: AAAACCCGGT
# Should return: ACCGGGTTTT

####################
#### Pseudocode ####
####################

# Here is the basic strategy to solve this problem:
# 1) Parse an input file from the command-line
# 2) Read the first line in the file and strip off the new line character
# 3) Replace "A" with "T", "T" with "A", "C" with "G" and "G" with "C"
# 4) Reverse the compliment using extended slice syntax [::-1] (all values, starting with the last index)
# 5) Print the output

##############
#### Code ####
##############

# Define argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument
parser.add_argument("input", type = str, help = "Input file containing DNA sequence (e.g., input_revc.txt")

# Execute parser
args = parser.parse_args()

# Open file handle, read line into a list and strip off new line
input = args.input
input_handle = open(input, "r")
dna = input_handle.readline().strip("\n")

# Generate complement
dna_comp = []
for i in dna:
	if i == "A":
		dna_comp.append("T")
	elif i == "T":
		dna_comp.append("A")
	elif i == "C":
		dna_comp.append("G")
	elif i == "G":
		dna_comp.append("C")

# Print reverse complement
rev_comp = "".join(dna_comp)[::-1]
print(rev_comp)