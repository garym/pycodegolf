#!/usr/bin/python
import sys
print sum(len(l) for l in (''.join(s.split()) for s in open(sys.argv[1]).readlines()) if l[0] != '#')
