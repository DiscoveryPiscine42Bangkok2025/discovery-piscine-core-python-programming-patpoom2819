#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    text = sys.argv[1]

    z_count = text.count('z')
    print('z' * z_count)
