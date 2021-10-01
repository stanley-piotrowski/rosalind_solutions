#!/usr/bin/env python3

################
#### dna.py ####
################

# Given a DNA string, return the counts of each of the four bases as integers separated by spaces 

# To run this program, save the string in an input file and type the following:
# ./dna.py <input>

# To print the help documentation, type one of the following:
# ./dna.py -h OR ./dna.py --help

# For example, given an input file with the DNA sequence: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Should return: 20 12 17 21

####################
#### Pseudocode ####
####################

# Here is my strategy for solving this problem, assuming the string is saved in a text file:
# 1) Parse the input file on the command-line
# 2) Since the DNA sequence will be a string on a single line, read that line, strip off the new line character, and split based on nothing so each character is an element in a list
# 3) Initialize an empty dictionary
# 4) Loop over each element in the list of bases, push the element as a key in the dictionary and the count of each element as a value
# 5) Loop over each item in the dictionary and print the value, separated by spaces

##############
#### Code ####
##############

# Initialize argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument 
parser.add_argument("input", type = str, help = "Input file containing DNA sequence (e.g., input_dna.txt)")

# Execute parser
args = parser.parse_args()

# Open file handle, read string from file, then loop through and push each element to a list
input = args.input
input_handle = open(input, "r")
dna = input_handle.readline().strip("\n")

dna_list = []
for i in dna:
	dna_list.append(i)

# Loop through each element of the list, push the element as a dict key and count as the dict value
dna_dict = {}
for i in dna_list:
	dna_dict[i] = dna_list.count(i)

# Print output
print(dna_dict["A"], dna_dict["C"], dna_dict["G"], dna_dict["T"], sep = " ")