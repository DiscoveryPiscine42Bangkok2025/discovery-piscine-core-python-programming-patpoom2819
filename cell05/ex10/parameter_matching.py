#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    secret_word = sys.argv[1]
    user_anwer = input("What is the secret?")

    if user_anwer == secret_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
