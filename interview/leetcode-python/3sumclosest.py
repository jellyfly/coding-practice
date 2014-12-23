class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):
		num.sort()
		length = len(num)
		result = num[0] + num[1] + num[2]

		for i in range(0, length - 1):
			index1 = i + 1
			index2 = length - 1

			while index1 < index2:
				temp = num[i] + num[index1] + num[index2]

				if temp == target:
					return temp
				elif temp < target:
					index1 += 1
				else:
					index2 -= 1

				if abs(temp - target) < abs(result - target):
					result = temp


		return result

if __name__ == "__main__":
	solution = Solution()
	S = [-1,2,1,-4]
	print solution.threeSumClosest(S, 1)
	T = [0,2,1,-3]
	print solution.threeSumClosest(T, 1)