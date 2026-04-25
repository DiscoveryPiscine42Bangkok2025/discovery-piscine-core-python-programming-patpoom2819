#!/usr/bin/env python3

number = "2 8 9 48 8 22 -12 2"

array = [int(x) for x in number.split() if int(x) > 5 ]
plus_two = [x + 2 for x in array]
print(set(plus_two))


