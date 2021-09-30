#!/usr/bin/env python3

###################
#### ini_03.py ####
###################

# Given a string of length <= 200 and four integers (a-d), slice the string between a-b and c-d, separated by space
# Importantly, the sliced strings a-b and c-d should be inclusive to include both b and d

# Use this program by providing a string as the first position argument, followed by four integer positional arguments
# For example:
# ./ini_03.py <string> <index_01> <index_02> <index_03> <index_04>

# <string> = HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain

# With the following position arguments: 22 27 97 102
# Should return "Humpty Dumpty"

##############
#### Code ####
##############

# Initialize parser
import argparse
parser = argparse.ArgumentParser()

# Define arguments
parser.add_argument("string", type = str, help = "required string argument")
parser.add_argument("slice01_start", type = int, help = "starting index of sliced string #1")
parser.add_argument("slice01_end", type = int, help = "ending index of sliced string #1")
parser.add_argument("slice02_start", type = int, help = "starting index of sliced string #2")
parser.add_argument("slice02_end", type = int, help = "ending index of sliced string #2")
args = parser.parse_args()

# Slice the strings
string01 = args.string[args.slice01_start:args.slice01_end + 1]
string02 = args.string[args.slice02_start:args.slice02_end + 1]

# Output
print(string01, string02, sep = " ")
