class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if not prices:
			return 0
		max_diff = 0
		mini = prices[0]

		for i in range(1, len(prices)):
			curr = prices[i]
			if curr < mini:
				mini = curr
			else:
				diff = curr - mini
				if diff > max_diff:
					max_diff = diff

		return max_diff
