#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    list = line.split(',')
    print list[1] + "\t" + list[5]
