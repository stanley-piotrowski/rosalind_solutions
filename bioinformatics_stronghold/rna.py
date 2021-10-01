#!/usr/bin/env python3

################
#### rna.py ####
################

# Given a DNA string as a coding strand, return the corresponding RNA strand, coverting "T" to "U"

# To use this program, place a DNA string in a file and type the following
# ./rna.py <input> 

# For help using this program, type one of the following:
# ./rna.py -h OR ./rna.py --help

# For example, given an input file with the following DNA string:
# GATGGAACTTGACTACGTAAATT

# This program will return the following:
# GAUGGAACUUGACUACGUAAAUU

####################
#### Pseudocode ####
####################

# Here is my basic strategy for solving this problem:
# 1) Parse the input file as a command-line argument
# 2) Use readline() to push the contents of the file to a list
# 3) Use the str.replace() method to replace "T" with "U"
# 4) Print the RNA string

##############
#### Code ####
##############

# Initialize argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument
parser.add_argument("input", type = str, help = "Input file with DNA string (e.g., input_rna.txt)")

# Execute parser
args = parser.parse_args()

# Open file handle, push string to a list
input = args.input
input_handle = open(input, "r")

# Replace "T" with "U" and print output
rna = input_handle.readline().strip("\n").replace("T", "U")
print(rna)