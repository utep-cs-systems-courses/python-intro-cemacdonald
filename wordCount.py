#! /usr/bin/env python3

import os
import sys
import string

count = {}
with open(sys.argv[1], 'r') as f:
    words = f.read().split()
    for word in words:
        word = word.strip(string.punctuation).lower()
        count[word] = count.get(word, 0) + 1

sorted_count = sorted(count.items())

outp = os.open(sys.argv[2], os.O_WRONLY | os.O_TRUNC)
for key, value in sorted_count:
    string1 = f"{value} {key}\n"
    os.write(outp, string1.encode())

os.close(outp)

