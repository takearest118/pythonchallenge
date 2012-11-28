# -*- coding: utf-8 -*-

import math

def answer1():
	return 2**38

def answer2():
	return pow(2, 38)

def main():
	print "answer1 is\n\"%s\"" % answer1()
	print "answer2 is\n\"%s\"" % answer2()
	print "go to the following url\n\"%s.html\"" % answer2()

if __name__=="__main__":
	main()
