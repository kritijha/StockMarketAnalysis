#!/usr/bin/env python

from operator import itemgetter
import sys

current_sym = "A"
current_count = 0
x=0
sym = None

for line in sys.stdin:
    line = line.strip()
    sym,cls = line.split('\t')
    if sym == current_sym:
	if x==0:
    	    perc=0
    	else:
    	    perc=((float(cls)-x)/x)*100
    	current_count += 1
	cdf =float( float(current_count)/ 240)
    else:
        current_count = 1
        current_sym = sym
	perc = 0
	cdf =float( float(current_count)/ 240)
    x=float(cls)
    print '%s,%.2f,%.3f' % (current_sym, perc,cdf)
