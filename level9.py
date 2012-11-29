# -*- coding: utf-8 -*-

import urllib2
import re
import bz2
import StringIO

from BeautifulSoup import BeautifulSoup
from PIL import Image
from PIL import ImageDraw

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
	print jpg.__class__
	print jpg.mode

	img = Image.new(jpg.mode, jpg.size)
	draw = ImageDraw.Draw(img)
	draw.line(first, 'green', 2)
	draw.line(second, 'red', 1)
	img.show()
	

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
