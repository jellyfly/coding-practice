class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		# use the math equation
		const = 5 ** 0.5
		return int((((1+const)/2) ** (n+1) - ((1-const)/2) **(n+1)) / const)

	def climbStairs_iter(self, n):
		if n < 0:
			return 0
		prev, curr = 0, 1
		for i in range(n):
			prev, curr = curr, curr + prev
		return curr

if __name__ == "__main__":
	solution = Solution()
	print solution.climbStairs_iter(0)
	print solution.climbStairs(0)
	assert solution.climbStairs(5) == solution.climbStairs_iter(5)