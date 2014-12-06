#!/usr/bin/python

import sys
sys.path.append("../exp_assist")
print sys.path
from data import fn_timer


@fn_timer
def run_timetest():
	print "testsss"

if __name__ == "__main__":
	run_timetest()
