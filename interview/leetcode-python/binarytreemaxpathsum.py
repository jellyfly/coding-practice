# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxPathSum(self, root):
		self.max_sum = None
		self.findMax(root)
		return self.max_sum

	def findMax(self,root):
		if not root:
			return 0
		else:
			left = self.findMax(root.left)
			right = self.findMax(root.right)

			max_path = max(max(left, right) + root.val, root.val)
			max_result = max()
			self.max_sum = max(self.max_sum, max_path, left + right + root.val)			
			return max_path

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

if __name__ == "__main__":
	x = TreeNode(-2)
	y = TreeNode(1)
	x.left = y
	solution = Solution()
	print solution.maxPathSum(x)