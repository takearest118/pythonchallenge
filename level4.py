# -*- coding: utf-8 -*-

import re
import urllib


def answer():
	nothing = "12345"
	for i in range(400):
		text = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing).read()
		print i, text
		nothing = ""
		for n in re.findall(r"[0-9]+", text):
			nothing += n
		print nothing

def main():
	answer()
	pass

if __name__=="__main__":
	main()
