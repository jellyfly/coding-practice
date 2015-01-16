#!/usr/bin/python


def cal_sep(x, y, n):
	
	a = x / (10 ** (n/2))
	b = x - a * (10 ** (n/2))
	c = y / (10 ** (n/2))
	d = y - c * (10 ** (n/2))

	return (a, b, c, d)

def cal_recur(tup):
	
	(a, b, c, d) = tup

	ac = a * c
	bd = b * d
	bc = b * c
	ad = a * d
	
	second = ad + bc

	return (ac, bd, second)
	
def cal_kara(tup):
	
	(a, b, c, d) = tup
	
	ac = a * c
	bd = b * d
	abcd = (a + b) * (c + d)
	
	second = abcd - ac - bd

	return (ac, bd, second)
	
def cal_final(tup, n):

	(ac, bd, second) = tup
	
	result = (10 ** n) * ac + (10 ** (n / 2)) * second + bd

	return result
	 

def recur(x, y):
	
	n = len(str(x))
	print cal_final(cal_recur(cal_sep(x,y,n)), n)

def kara(x, y):

	n = len(str(x))
	print cal_final(cal_recur(cal_sep(x,y,n)), n)

def main(x, y):

	if (len(str(x)) == len(str(y))):
		recur(x,y)
		kara(x,y)
	else:
		print "not the same length"

if __name__ == "__main__":
	x = 1234
	y = 5678
	main(x, y)
