# https://leetcode.com/problems/reverse-linked-list/

# Solution 1: Brute Force / Iterative with Extra List
# Idea: Traverse the linked list, store all nodes in a list/array, then reconstruct the list in reverse order.
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(n), for storing nodes in a list
class Solution:
    def reverse_list(self):
        if not self.head:
            return None

        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]
        nodes[0].next = None
        return nodes[-1]


# Solution 2: Optimized In-Place Iterative
# Idea: Use two pointers (prev and curr) to reverse the links one by one while traversing the list.
# Time Complexity: O(n), each node is visited once
# Space Complexity: O(1), no extra space used
# class Solution:
#     def reverse_list(self):
#         prev = None
#         curr = self.head
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         self.head = prev
#         return self.head


# Solution 3: Recursive Approach
# Idea: Recursively reverse the rest of the list, then set the next node's next pointer to the current node.
# Time Complexity: O(n), each node is visited once
# Space Complexity: O(n), due to recursion call stack
# class Solution:
#     def revesse_list(self):
#         if not self.head or not self.head.next:
#             return self.head
#         new_head = self.reverseList(self.head.next)
#         self.head.next.next = self.head
#         self.head.next = None
#         return new_head
