# -*- coding: utf-8 -*-

import Image
import re

def answer1():
	im = Image.open("./oxygen.png")
	pixels = [im.getpixel((x, im.size[1]/2)) for x in range(0, im.size[0], 7)]
	print pixels
	same_rgb = [r for r,g,b,a in pixels if r==g==b]
	print same_rgb
	answer = "".join(map(chr, same_rgb))
	print answer
	result = "".join(map(chr, map(int, re.findall(r"\d+", answer))))
	print result
	return

def main():
	answer1()

if __name__=="__main__":
	main()

