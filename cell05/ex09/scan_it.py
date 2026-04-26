#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("none")

else:
    keyword = sys.argv[1]
    sentence = sys.argv[2]
    count = sentence.count(keyword)

    if keyword in sentence:
        print(count)
    else:
        print("none")
