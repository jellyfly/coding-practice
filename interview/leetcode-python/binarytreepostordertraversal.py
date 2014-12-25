# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		
		results = []
		if not root:
			return results

		queue = []
		queue.append(root)

		while queue:
			root = queue.pop()
			results.insert(0, root.val)
			if root.left:
				queue.append(root.left)
			if root.right:
				queue.append(root.right)

		return results