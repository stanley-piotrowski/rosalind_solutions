#!/usr/bin/env python3

###################
#### ini_05.py ####
###################

# Take a file containing at most 1000 lines and return a file containing all the even-numbered lines from the original file, assuming a 1-based numbering of lines

# To run this program, type the following:
# ./ini_05.py <input_file> <output_file>

# For example, given an input file with the following lines:
# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin

# Should return:
# Yes, brave Sir Robin turned about

# To get help on the parameters, type one of the following:
# ./ini_05.py -h OR ./ini_05.py --help

##############
#### Code ####
##############

# Initialize argparse
import argparse
parser = argparse.ArgumentParser()

# Add arguments for input and output files
parser.add_argument("input", type = str, help = "Input file to read (e.g., input.txt)")
parser.add_argument("output", type = str, help = "Output file to write (e.g., output.txt)")

# Execute the parser
args = parser.parse_args()

# Open file handle, create empty list, and append the line stripped of the \n 
input_handle = open(args.input, "r")
input_list = []
for line in input_handle:
	input_list.append(line.strip("\n"))

# Loop over list and if the index is not zero and is even, subset the element with that index - 1
# This mimics the list having a 1-based indexing system
output_handle = open(args.output, "w")
for i in range(0, len(input_list) + 1):
	if (i != 0) & (i % 2 == 0):
		output_handle.write(input_list[i - 1] + "\n")




