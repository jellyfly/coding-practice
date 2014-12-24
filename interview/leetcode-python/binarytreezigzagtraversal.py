# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def zigzagLevelOrder(self, root):
		if not root:
			return []
		results = []

		queue = []
		visited_level = []
		flag = False

		queue.append(root)
		queue.append(None)

		while queue:
			node = queue.pop(0)
			if not node:
				if queue:
					queue.append(None)
				results.append(visited_level)
				visited_level = []
				flag = not flag
			else:
				if flag:
					visited_level.insert(0, node.val)
				else:
					visited_level.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

		return results


