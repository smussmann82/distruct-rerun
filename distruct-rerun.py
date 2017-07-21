#!/usr/bin/python

from comline import ComLine
from distruct import Distruct
from clumpp import Clumpp

import sys



def main():
	input = ComLine(sys.argv[1:])

	drawp = "drawparams." + input.args.k
	outfile = "K" + input.args.k + ".ps"

	c = Clumpp(input.args.directory, input.args.k)
	c.copyFiles()

	d = Distruct(input.args.directory)
	d.copyFiles()
	d.writeDrawparams(drawp, c.oldpop, c.oldind, input.args.k, outfile, c.pops, c.inds)

main()

raise SystemExit
