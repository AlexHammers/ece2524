#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

if len(argv) != 3:
    stderr.write("Wrong number of arguments\n")
    exit(1)

for line in fileinput.input('-'):
    l = re.search(argv[1], line)
    if l:
	values = line.split(',')
	values[3] = argv[2]
	print ",".join(values)
    else:
	print line


