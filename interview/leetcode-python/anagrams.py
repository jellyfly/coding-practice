class Solution:
	# @param strs, a list of strings
	# @return a list of strings
	def anagrams(self, strs):
		results = []
		mapping = dict()

		for str_i in strs:
			str_sort = ''.join(sorted(str_i))
			if str_sort not in mapping:
				mapping[str_sort] = []
			mapping[str_sort].append(str_i)

		for str_sort in mapping:
			if len(mapping[str_sort]) > 1:
				results.extend(mapping[str_sort])

		return results

if __name__ == "__main__":
	solution = Solution()
	print solution.anagrams([""])