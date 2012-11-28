# -*- coding: utf-8 -*-

from string import maketrans

q1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

from_table = "abcdefghijklmnopqrstuvwxyz"
to_table = "cdefghijklmnopqrstuvwxyzab"

def answer1():
	ret = ""
	for c in q1:
		if c == " " or c == "'" or c == "(" or c ==")" or c == "." or c ==",":
			ret += c
		elif c == 'y':
			ret += 'a'
		elif c == 'z':
			ret += 'b'
		else:
			ret += chr(ord(c)+2)
	return ret

def answer2():
	temp = maketrans(from_table, to_table)
	return q1.translate(temp)

def goToUrl():
	temp = maketrans(from_table, to_table)
	return "map".translate(temp)

def main():
	print "answer1 is\n\"%s\"" % answer1()
	print "answer2 is\n\"%s\"" % answer2()
	print "go to the following url\n\"%s.html\"" % goToUrl()

if __name__=="__main__":
	main()
