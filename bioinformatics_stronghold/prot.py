#!/usr/bin/env python3

#################
#### prot.py ####
#################

# Given a file with a mRNA string, return the translated amino acid sequence

# To run this program, place a mRNA sequence into a file, place a RNA codon table into the directory and type the following:
# ./prot.py <input_mrna_file> <rna_codon_table>

# To find help for this program, type one of the following:
# ./prot.py -h OR ./prot.py --help

# Example: give a file with the following mRNA:
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

# Should return the following amino acid sequence:
# MAMAPRTEINSTRING

####################
#### Pseudocode ####
####################

# Here is the strategy for solving the following problem:
# 1) Parse input files containing mRNA sequence and the RNA condon table from the command line
# 2) Readline the mRNA sequence into a list
# 3) For each line in the codon table, strip the new line character and split on the tab character, then push to a dictionary
# 4) Walk along the the mRNA sequence in slices of 3 to identify codons- if the codon is in the dictionary keys, append the value to a new amino acid list
# 5) Print the final output as a string

##############
#### Code ####
##############

# Define argparse
import argparse
parser = argparse.ArgumentParser()

# Define arguments
parser.add_argument("input", type = str, help = "Input file containing mRNA sequence to translate (e.g., input_prot.txt")
parser.add_argument("codon_table", type = str, help = "Table linking RNA codons to amino acids (e.g., codon_table.txt")

# Execute argparse
args = parser.parse_args()

# Read mRNA sequence
input = args.input
input_handle = open(input, "r")
input = input_handle.readline().strip("\n")

# Read codon table and push to a dictionary, codons are keys and amino acids are the values
codon_table = args.codon_table
codon_handle = open(codon_table, "r")

codon_dict = {}
for line in codon_handle:
	line = line.strip("\n").split("\t")
	codon_dict[line[0]] = line[1]

# Slice up the mRNA sequence into codons using C-style loop
# If the codon is in the keys of the codon dictionary, append the value to the amino acid sequence list
aa_seq = []
for i in range(0, len(input), 3):
	codon = input[i:i+3]
	if codon in codon_dict.keys():
		if codon != "UGA":
			aa_seq.append(codon_dict[codon])

# Print output as a string
print("".join(aa_seq))





