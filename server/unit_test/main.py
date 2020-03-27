# -*- coding: utf-8 -*-
# desc: unit test entry
import os
import sys

def main():
	sys.path.append('../')
	import test
	for testCls in test.TestBase.__subclasses__():
		if sys.argv[1] == 'all' or sys.argv[1] in testCls.__name__:
			testInst = testCls()
			testInst.run()

if __name__ == '__main__':
	main()