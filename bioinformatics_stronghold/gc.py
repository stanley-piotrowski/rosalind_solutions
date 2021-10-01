#!/usr/bin/env python3

###############
#### gc.py ####
###############

# Given a list of DNA sequences and headers in FASTA format, calculate the GC content of each and output the sequence and header with the highest GC content

# To run this program, place FASTA formatted DNA sequences in a file and type the following:
# ./gc.py <input>

# To get help for this program, type one of the following:
# ./gc.py -h OR ./gc.py --help

####################
#### Pseudocode ####
####################

# Here is my strategy to solve this problem:
# 1) Parse the input file from the command-line
# 2) Initialize an empty dictionary and for each 

##############
#### Code ####
##############

# Define argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument
parser.add_argument("input", type = str, help = "Input file containing DNA sequences in FASTA format (e.g., input_gc.txt)")

# Execute parser
args = parser.parse_args()

# Read lines and if the lines don't include a ">" character, strip the "\n"
input = args.input
input_handle = open(input, "r")

# Populate lists of FASTA header and DNA sequences
fasta_dict = {}
for line in input_handle:
	if line.startswith(">"):
		header = line.strip("\n").replace(">", "")
		fasta_dict[header] = ""
	else: 
		fasta_dict[header] = line.strip("\n") + line.strip("\n")

# Calculate GC content
gc_dict = {}
for key, value in fasta_dict.items():
	gc_content = (value.count("G") + value.count("C")) / len(value) 
	gc_content = gc_content * 100
	gc_dict[key] = gc_content

# Push sorted dictionary to a list
for key, value in sorted (gc_dict.items()):
	gc_list = list(gc_dict.items())

# Grab the last entry (highest GC content)
top_gc = gc_list[-1]
print(top_gc[0], top_gc[1], sep = "\n")

# Close file handle
input_handle.close()
	