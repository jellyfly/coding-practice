# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderBottom(self, root):
		if not root:
			return []
		results = []

		queue = []
		visited_level = []
		queue.append(root)
		queue.append(None)

		while queue:
			root = queue.pop(0)
			if not root:
				if queue:
					queue.append(None)
				results.insert(0, visited_level)
				visited_level = []
			else:
				visited_level.append(root.val)
				if root.left:
					queue.append(root.left)
				if root.right:
					queue.append(root.right)

		return results