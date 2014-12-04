from nose.tools import assert_true
from unittest import TestCase
import unittest

class ExampleTest(TestCase):

	def Setup(self):
		self.blah = False

	def test_blah(self):
		self.assertTrue(self.blah)

if __name__ == "__main__":
	unittest.main()
