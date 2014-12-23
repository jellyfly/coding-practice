class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum_recursion(self, num, target):
		num.sort()
		return self.k_sum(4, num, target)

	def k_sum(self, k, num, target):
		'''suitable for k > = 3'''
		length = len(num)

		if k == 2:
			results = []
			for i in range(0, length - 1):
				if i>0 and num[i] != num[i-1]:
					next
					
				target = - num[i]
				index1 = i + 1
				index2 = length - 1

				while index1 < index2:

					temp = num[index1] + num[index2]

					if temp < target:
						index1 += 1
					elif temp > target:
						index2 -= 1
					else:
						results.append([num[i], num[index1], num[index2]])
						index1 += 1
						index2 -= 1

						while index1 < index2 and num[index1] == num[index1-1]:
							index1 += 1
						while index1 < index2 and num[index2] == num[index2+1]:
							index2 -= 1
			return results
		else:
			results = []
			for i in range(0, length): 
				next_target = target - num[i]
				for array in self.k_sum(k-1, num, target):
					results.append(array + [num[i]])

			return results

	def fourSum_naive(self, num,target):
		num.sort()
		length = len(num)
		results = []

		for i in range(0, length - 2):
			if i>0 and num[i] != num[i-1]:
				next

			for index1 in range(i+1, length - 1):
				if  index1 > i+1 and num[index1] != num[index1 - 1]:
					next

				index2 = index1 + 1
				index3 = length - 1

				while index2 < index3:
					temp = num[i] + num[index1] + num[index2] + num[index3]

					if temp == target:
						results.append([num[i], num[index1], num[index2], num[index3]])
						index2 += 1
						index3 -= 1
						
						while index2 < index3 and num[index2] == num[index2-1]:
							index2 += 1
						while index2 < index3 and num[index3] == num[index3+1]:
							index3 -= 1
						
					elif temp > target:
						index3 -= 1
					else:
						index2 += 1
							
		return results

	def fourSum_set(self, num,target):
		num.sort()
		length = len(num)
		results = set()

		for i in range(0, length - 2):
			for index1 in range(i+1, length - 1):
				index2 = index1 + 1
				index3 = length - 1

				while index2 < index3:
					temp = num[i] + num[index1] + num[index2] + num[index3]

					if temp == target:
						results.add((num[i], num[index1], num[index2], num[index3]))
						index2 += 1
						index3 -= 1
						
					elif temp > target:
						index3 -= 1
					else:
						index2 += 1
				
		results = list(results)		

		return results


if __name__ == "__main__":
	solution = Solution()
	S = [1, 0, -1, 0, -2, 2]
	print solution.fourSum_set(S, 0)
	solution.fourSum_set([-6,-8,-4,1,9,7,1,-10,5,-9,-1,3,0,7,3], -25)
	#solution.fourSum_naive([-6,-8,-4,1,9,7,1,-10,5,-9,-1,3,0,7,3], -25)