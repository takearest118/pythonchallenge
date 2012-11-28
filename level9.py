# -*- coding: utf-8 -*-

import Image
import urllib2
import re
import bz2
import StringIO

from BeautifulSoup import BeautifulSoup

def answer1():
	url = "http://www.pythonchallenge.com/pc/return/good.html"
	username = "huge"
	password = "file"
	raw = _request_auth(url, username, password)
	soup = BeautifulSoup(raw)
	comment = soup.find(text = re.compile("first"))
	first = map(int, comment.split("second")[1].replace("\n", "").replace("=?first:", "").split(","))
	second = map(int, comment.split("second")[2].replace("\n", "").replace(":", "").split(","))
	print first
	print second
	img_url = "http://www.pythonchallenge.com/pc/return/good.jpg"
	raw = _request_auth(img_url, username, password)
	jpg = Image.open(StringIO.StringIO(raw))
	print jpg
	print jpg.size
	print dir(jpg)
	jpg.show()

def _request_auth(url, username, password):
	p = urllib2.HTTPPasswordMgrWithDefaultRealm()
	p.add_password(None, url, username, password)
	handler = urllib2.HTTPBasicAuthHandler(p)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	response = urllib2.urlopen(url)
	return response.read()

def main():
	answer1()

if __name__=="__main__":
	main()
