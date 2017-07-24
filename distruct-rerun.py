#!/usr/bin/python

from comline import ComLine
from distruct import Distruct
from clumpp import Clumpp

import sys



def main():
	input = ComLine(sys.argv[1:])

	for k in xrange(int(input.args.mink),int(input.args.maxk)+1):
		drawp = "drawparams." + str(k)
		outfile = "K" + str(k) + ".ps"

		c = Clumpp(input.args.directory, str(k))
		c.copyFiles()

		d = Distruct(input.args.directory)
		d.copyFiles()
		d.writeDrawparams(drawp, c.oldpop, c.oldind, str(k), outfile, c.pops, c.inds)

main()

raise SystemExit
