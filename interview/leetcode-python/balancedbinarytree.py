# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		if not root:
			return True # height = 0
		elif self.isBalanced(root.left) and self.isBalanced(root.right):
			return abs(self.height(root.left) - self.height(root.right)) <= 1
		else:
			return False

	def height(self, root):
		if not root:
			return -1
		return max(self.height(root.left), self.height(root.right)) + 1