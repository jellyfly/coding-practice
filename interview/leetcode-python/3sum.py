class Solution:	
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(num):
		num.sort()
		results = []
		length = len(num)

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
					
					# can't use set, this is to work around
					while index1 < index2 and num[index1] == num[index1-1]:
						index1 += 1
					while index1 < index2 and num[index2] == num[index2+1]:
						index2 -= 1

		return results

if __name__ == "__main__":
	solution = Solution()
	S = [-1,0,1,2,-1,-4]
	print solution.threeSum(S)
	T = [0,0,0]
	print solution.threeSum(T)