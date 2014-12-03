import unittest

# Here's our "unit".
'''this is before odd'''
def IsOdd(n):
	'''this is odd'''
	return n % 2 == 1
	print(IsOdd.__doc__)
    

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
