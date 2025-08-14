# https://leetcode.com/problems/middle-of-the-linked-list/

# Solution 1 - Convert to array and return middle
# Idea: Store all nodes in a list, then directly access the middle index.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def middleNode(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes[len(nodes) // 2]


# Solution 2 - Slow and Fast Pointer
# Idea: Move one pointer at 1 step, another at 2 steps. When fast reaches the end, slow is at the middle.
# Time Complexity: O(n)
# Space Complexity: O(1)
# class Solution:
#     def middleNode(self, head):
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
