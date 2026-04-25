#!/usr/bin/env python3

number = "2 8 9 48 8 22 -12 2"

array = [int(x) for x in number.split()]
print("Original array:", array)

plus_array = [int(x)+ 2 for x in number.split()]
print("New array:", plus_array)

