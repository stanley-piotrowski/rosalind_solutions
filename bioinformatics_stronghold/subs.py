#!/usr/bin/env python3

#################
#### subs.py ####
#################

# Given two DNA strings, "s" and "t", return all locations of "t" that are a substring of "s"

####################
#### Pseudocode ####
####################

# Here is the strategy to solve the following problem:
# 1) Parse a file from the command line
# 2) Read in the first line as "s", stripping off the "\n"
# 3) Read in the second line as "t", stripping off the "\n"
# 4) Loop over "s" in windows of the length of "t"
# 5) If there's a match, append the location of "t" as a substring of "s" (the index) in a list
# 6) Loop over the list and print the locations, separated by spaces

##############
#### Code ####
##############

# Define argparse
import argparse
parser = argparse.ArgumentParser()

# Define argument
parser.add_argument("input", type = str, help = "Input file with sequence 's' and subsequence 't'")

# Execute argparse
args = parser.parse_args()

# Open file handle and push first line as 's' and second as 't'
input = args.input
input_handle = open(input, "r")
s = input_handle.readline().strip("\n")
t = input_handle.readline().strip("\n")

# Loop over the range of the length of the string "s"
# Slice up "s" from i to i + len(t) to make sure the window slides along at the same size and doesn't get smaller
# If the "s" slice == "t", append the index plus 1 (to include the starting position of "t")
subs_index = []
for i in range(0, len(s)):
	subs = s[i:i + len(t)]
	if subs == t:
		subs_index.append(i + 1)

# Map the str() method to each element of subs_index list and join them together
print(" ".join(map(str, subs_index)))

