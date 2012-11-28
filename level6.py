# -*- coding: utf-8 -*-

import re
import zipfile
import StringIO
import urllib

def answer1():
	ret = ""
	z = StringIO.StringIO()
	z.write(urllib.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip").read())
	zf = zipfile.ZipFile(z)
	start = ["90052"]
	next = start
	while True:
		desc = zf.read("%s.txt" % next[0])
		info = zf.getinfo("%s.txt" % next[0])
		next = re.findall(r"[0-9]+", desc)
		if len(next) == 0:
			break
		else:
			ret += info.comment
	return ret

def main():
	print "answer1 is\n\"%s\"" % answer1()

if __name__=="__main__":
	main()
