#!/usr/bin/env python3

###################
#### ini_04.py ####
###################

# Take two positive integers as input, "a" and "b", and return the sum of all odd integers from "a" through "b" (inclusively) 

# To run this program, type the following:
# ./ini_04.py <positive_int_01> <positive_int_02>

# Example:
# a = 100, b = 200, should return 7500

# To get help on this program, type the following:
# ./ini_04.py -h OR ./ini_04.py -help OR ./ini_04.py --help

##############
#### Code #### 
##############

# Initialize parser
import argparse
parser = argparse.ArgumentParser(description = "Description: calculate the sum of odd integers between 'a' and 'b', inclusively")

# Define required arguments
parser.add_argument("a", type = int, help = "First required even integer")
parser.add_argument("b", type = int, help = "Second required even integer")

# Execute the parser
args = parser.parse_args()

# Loop and output result
a = args.a
b = args.b
output = 0
for i in range(a, (b + 1)):
	if i % 2 != 0:
		output += i

print(output)

