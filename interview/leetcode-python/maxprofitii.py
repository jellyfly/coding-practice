class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if not prices:
			return 0
		diff = 0
		for i in range(0, len(prices) - 1):
			if prices[i+1] > prices[i]:
				diff = diff + prices[i+1] - prices[i]
				i += 1
		return diff