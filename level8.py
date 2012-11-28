# -*- coding: utf-8 -*-

import Image
import urllib2
import re
import bz2

from BeautifulSoup import BeautifulSoup

def answer1():
	url = "http://www.pythonchallenge.com/pc/def/integrity.html"
	print url
	response = urllib2.urlopen(url)
	raw = response.read()
	soup = BeautifulSoup(raw)
	comment = soup.find(text=re.compile("un"))
	print comment.__class__
	l = comment.split("\n")
	un = l[1].split(":")[1]
	pw = l[2].split(":")[1]
	print un, pw
	print "un: %s" % bz2.decompress(eval(un))
	print "pw: %s" % bz2.decompress(eval(pw))

def main():
	answer1()

if __name__=="__main__":
	main()

