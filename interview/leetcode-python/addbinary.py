class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		value_a = int(a, 2)
		value_b = int(b, 2)
		value_c = value_a + value_b
		return str(bin(value_c))[2:]

	def addBinary_naive(self, a, b):
		list_a = [int(i) for i in a]
		list_b = [int(i) for i in b]
		
		length_a = len(list_a)
		length_b = len(list_b)

		value_a = 0
		for i in range(0, length_a):
			value_a = value_a + list_a[length_a - i - 1] * (2 ** i)

		value_b = 0
		for i in range(0, length_b):
			value_b = value_b + list_b[length_b - i - 1] * (2 ** i)

		value_c = value_a + value_b

		return str(bin(value_c))[2:]


if __name__ == "__main__":
	solution = Solution()
	print solution.addBinary("1111", "0101")