class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		indice = {}
		for i in range(0, len(num)):
			if (target - num[i]) in indice:
				return (indice[target-num[i]] + 1, i + 1)
			else:
				indice[num[i]]=i

if __name__ == "__main__":
	solution = Solution()
	S = [1, 0, -1, 0, -2, 2]
	print solution.twoSum(S, 1)