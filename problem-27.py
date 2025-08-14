# https://leetcode.com/problems/linked-list-cycle/

# Solution 1 - Use a set to track visited nodes
# Idea: Traverse the list and store each visited node in a set. If we see a node twice, there's a cycle.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def hasCycle(self, head):
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False


# Solution 2 - Slow and Fast Pointer (Floyd's cycle detection)
# Idea: Move one pointer at 1 step and another at 2 steps. If they meet, there's a cycle.
# Time Complexity: O(n)
# Space Complexity: O(1)
# class Solution:
#     def hasCycle(self, head):
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
