# -*- coding: utf-8 -*-

import pickle
import urllib
import os

def answer1():
	ret = ""
	banner_obj = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
	for line in banner_obj:
		ret += "".join(map(lambda pair: pair[0]*pair[1], line))
		ret += os.linesep
	return ret

def answer2():
	ret = ""
	banner_obj = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
	for line in banner_obj:
		ret += "".join([ch*count for ch, count in line])
		ret += os.linesep
	return ret

def answer3():
	banner_obj = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
	return os.linesep.join(["".join([ch*count for ch, count in line]) for line in banner_obj])

def main():
	print "answer1 is\n\"%s\"" % answer1()
	print "answer2 is\n\"%s\"" % answer2()
	print "answer3 is\n\"%s\"" % answer3()

if __name__=="__main__":
	main()
