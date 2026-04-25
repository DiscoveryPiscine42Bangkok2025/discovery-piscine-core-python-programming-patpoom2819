#!/usr/bin/env python3

number = float(input("Give me a number: "))
rounded = int(number) + (1 if number != int(number) else 0)
print(rounded)


