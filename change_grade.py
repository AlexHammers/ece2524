#!/usr/bin/env python

import re
import fileinput

def change_grade(searchStr, grade, data):
    lines=[]
    for line in fileinput.input(data):
    	l = re.search(searchStr, line)
    	if l:
	    values = line.split(',')
	    values[3] = grade
	    lines.append(",".join(values))
    	else:
	    lines.append(line)
    return (lines)

if __name__=='__main__':
    from sys import stderr,stdout,argv,exit
    if len(argv) != 3:
    	stderr.write("Wrong number of arguments\n")
    	exit(1)
    (lines) = change_grade(argv[1], argv[2], stdin)
    for line in lines:
	stderr.write(line)






