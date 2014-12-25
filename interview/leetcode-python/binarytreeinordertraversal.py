# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):

		results = []
		if not root:
			return results

		queue = []

		while queue or root:
			if root:
				queue.append(root)
				root = root.left
			else:
				root = queue.pop()
				results.append(root.val)
				root = root.right

		return results