#!/usr/bin/env python3

#################
#### cons.py ####
#################

# Given a collection of at most 10 DNA strings of equal length in FASTA format, return a consensus string and a profile matrix for the collection
# Note, if several possible consensus strings exist, the function may return any of them

# To run this program, place at most 10 equal-length DNA strings in FASTA format into a file and type the following
# ./cons.py <input>

# For help using this program, type one of the following:
# ./cons.py -h OR ./cons.py --help

# Example:
# Given a file with the following sequences:
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Should produce the following consensus string and profile matrix:
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

####################
#### Pseudocode ####
####################

# Here is my strategy to solve this problem:
# 1) Parse input file from the command line
# 2) Create an input file handle and a set of empty lists to hold each sequence
# 3) For each line in the file, if the line doesn't start with ">", push to a new list
# 4) Zip all of the sequence lists together
# 5) For each element in each list, count the number of nucleotides as A, C, G, and T, and push to a dictionary, then into a list of dictionaries
# 6) For each element in the list of counts per position dictionaries, sort the values, identify the max, then output the key into a new output list
# 7) To print the output string, join all of the elements of the output list

# Modules
import argparse
import string

# Define argparse
parser = argparse.ArgumentParser()

# Define arguments
parser.add_argument("input", type = str, help = "Input file containing equal-length DNA sequences in FASTA format (e.g., input_fasta.txt)")

# Execute the parser
args = parser.parse_args()

# Read lines and push to dicitionary (header as key, sequence as value)
input = args.input
input_handle = open(input, "r")
seq_dict = {}
for line in input_handle:
	if line.startswith(">"):
		header = line.strip("\n")
		seq_dict[header] = ""
	else:
		seq_dict[header] = line.strip("\n")

# Loop over values of sequence dictionary and zip 
zip_seq = zip(*seq_dict.values())

# Loop through zipped iterator, count the number of each base, push to dictionary for each position
# Then store all dictionaries in a single list
base_count_list = []
for (a, b, c, d, e, f, g) in zip_seq:
	base_count = {}
	base_count["A"] = a.count("A") + b.count("A") + c.count("A") + d.count("A") + e.count("A") + f.count("A") + g.count("A")
	base_count["C"] = a.count("C") + b.count("C") + c.count("C") + d.count("C") + e.count("C") + f.count("C") + g.count("C") 
	base_count["G"] = a.count("G") + b.count("G") + c.count("G") + d.count("G") + e.count("G") + f.count("G") + g.count("G") 
	base_count["T"] = a.count("T") + b.count("T") + c.count("T") + d.count("T") + e.count("T") + f.count("T") + g.count("T")
	base_count_list.append(base_count)

# Call consensus sequence 
# Sort the dictionary items by the value (index 1), which will return a list
# I want to grab the last element (corresponding to the highest counts)
# From that element, grab the base (i.e, the key in the dictionary at index 0)
consensus = []
for i in base_count_list:
	consensus.append(sorted(i.items(), key = lambda item: item[1])[-1][0])

# Print profile matrix
# Initialize empty lists for counts of each base
count_A = []
count_C = []
count_G = []
count_T = []

# Loop over the list of dictionaries and iterate over each key:value pair in each dictionary
# If the base is A, append the count to the A list, etc.
for i in base_count_list:
	for base, count in i.items():
		if base == "A":
			count_A.append(count)
		elif base == "C":
			count_C.append(count)
		elif base == "G":
			count_G.append(count)
		elif base == "T": 
			count_T.append(count)

# Print consensus 
print("".join(consensus))

# Print profile matrix
# Note- map the str() method to each element 
print("A:", " ".join(map(str, count_A)), sep = " ")
print("C:", " ".join(map(str, count_C)), sep = " ")
print("G:", " ".join(map(str, count_G)), sep = " ")
print("T:", " ".join(map(str, count_T)), sep = " ")




