#!/usr/bin/env python

first_number =  int(input("Enter the first number: "))
last_number = int(input("Enter the second number: "))
total = first_number * last_number
print(total)

if total > 0:
    print("The result is positive")
if total < 0:
    print("The result is negative")
if total == 0:
    print("The result is proitive and negative")