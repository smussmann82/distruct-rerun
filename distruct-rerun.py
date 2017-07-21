#!/usr/bin/python

from comline import ComLine
from distruct import Distruct
from clumpp import Clumpp

import sys



def main():
	input = ComLine(sys.argv[1:])

	c = Clumpp(input.args.directory, input.args.k)
	c.copyFiles()

main()

raise SystemExit
