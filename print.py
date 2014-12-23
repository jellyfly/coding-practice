#!/usr/bin/python

import codecs

infile = codecs.open("file.txt", "r", encoding = "utf-8")
lines = infile.read().split("\n")
print len(lines)
for line in lines:
	print len(line.split(","))
	print line
