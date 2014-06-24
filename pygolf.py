#!/usr/bin/python
import sys
with open(sys.argv[1]) as f: print len(''.join(f.read().split()))
