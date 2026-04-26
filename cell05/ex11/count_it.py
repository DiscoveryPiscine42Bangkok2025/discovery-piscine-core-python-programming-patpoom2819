#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    num_params = len(sys.argv) - 1
    print("parameters:", num_params)
    
    for i in range(1, len(sys.argv)):
        x = sys.argv[i]
        print(x + ":", len(x))