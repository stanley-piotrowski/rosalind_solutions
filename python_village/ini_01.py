#!/usr/bin/env python3

################
#### ini_01 ####
################

# Take two integers as input, corresponding to the lengths of two sides of a triangle, and calculate the square of the hypotenuse of the right triangle
# Ex... given 3 and 5, the program should return 34

# To run this program, use the following example:
# ./ini_01.py <positional_argument_01> <position_argument_02>

##############
#### Code ####
##############

# Initialize parser and add required position arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("pos_arg_01", type = int, help = "A required first positional argument")
parser.add_argument("pos_arg_02", type = int, help = "A required second positional argument")
args = parser.parse_args()

# Calculate square of the hypotenuse
output = args.pos_arg_01**2 + args.pos_arg_02**2
print(output)
