# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):

		carry = 0
		begin_node = None
		end_node = None

		while l1 != None or l2 != None or carry == 1:

			value = 0

			if l1 != None:
				value += l1.val
				l1 = l1.next

			if l2 != None:
				value += l2.val
				l2 = l2.next

			value += carry
			value_dec = value%10
			carry = value/10

			if begin_node == None:
				begin_node = ListNode(value_dec)
				end_node = begin_node
			else:
				end_node.next = ListNode(value_dec)
				end_node = end_node.next

		return begin_node


if __name__ == "__main__":
	solution = Solution()
	solution.addTwoNumbers()