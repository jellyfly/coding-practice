class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if not prices:
			return 0
		length = len(prices)
		if length <= 1:
			return 0

		order_diff = {}
		mini = prices[0]
		max_profit = 0
		order_diff[0] = max_profit

		for i in range(1, length):
			if prices[i] > mini:
				diff = prices[i] - mini
				if diff > max_profit:
					max_profit = diff
				order_diff[i] = max_profit
			else:
				mini = prices[i]
				order_diff[i] = max_profit

		result = 0

		maxi = prices[-1]
		max_profit = 0
		i = length - 1
		while i >= 0:
			if prices[i] < maxi:
				diff = maxi - prices[i]
				if diff > max_profit:
					max_profit = diff
				profit = max_profit + order_diff[i]
				if profit > result:
					result = profit
			else:
				maxi = prices[i]
			i -= 1

		return result

if __name__ == "__main__":
	solution = Solution()
	print solution.maxProfit([1,2])
	print solution.maxProfit([2,1,2,0,1])
	print solution.maxProfit([6,1,3,2,4,7])