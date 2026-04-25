#!/usr/bin/env python3

print("Enter a number less than 25")
number =  int(input())
i = number

if number >25 :
    print("ERROR")
else:
    while i < 26:
        print("Inside the loop, my variable is", i)
        i += 1
 