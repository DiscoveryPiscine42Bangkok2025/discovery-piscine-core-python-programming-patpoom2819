#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for arg in range(int(sys.argv[1]), int(sys.argv[2])):
        print(arg)