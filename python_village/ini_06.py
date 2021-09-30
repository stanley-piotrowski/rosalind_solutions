#!/usr/bin/env python3

###################
#### ini_06.py ####
###################

# Give a string "s" of length at most 10,000 letters, return the number of occurrences of each word in "s" separated by spaces, where order does not matter

# To run this program, supply an input file and type the following:
# ./ini_06.py <input>

# To get help on this program, type one of the following:
# ./ini_06.py -h OR ./ini_06.py --help

# For example, given the following string as input: We tried list and we tried dicts also we tried Zen
# Should return:
# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1

####################
#### Pseudocode ####
####################

# My strategy for solving this problem, assuming the string was in a file, was to use the following steps:
# 1) Parse the input file from the command-line using the argparse module
# 2) Since we're just reading a single string, only read the first line of the file with readline()
# 3) Additionally, strip off the remaining new line character and split on white spaces to push each string in the line to a list
# 4) Initialize a dicitionary
# 5) Loop over each element in the list of strings, push the string as the key in the dictionary and the number of occurrences of that string as the associated value
# 6) Finally, for all items in the dictionary, print the key and value, separated by a space

##############
#### Code ####
##############

# Initialize argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument for input file
parser.add_argument("input", type = str, help = "Input file containing string (e.g., input_ini_06.txt)")

# Execute the parser
args = parser.parse_args()

# Open file handle and push the line to a list
input = args.input
input_handle = open(input, "r")
input_string = input_handle.readline().strip("\n").split(" ")

# Loop through each element in the list and count the number of occurrences
# Initialize a dictionary, push the string as a key and the number of occurrences as a value
string_dict = {}
for string in input_string:
	string_dict[string] = input_string.count(string)

# Loop over the dictionary items and print the key:value pairs
for key, value in string_dict.items():
	print(key, value, sep = " ")

