# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Optimized In-Place Iterative Merge
# Idea: Use two pointers to traverse both lists, append the smaller node to the merged list, and continue until both lists are exhausted.
# Time Complexity: O(n + m), each node is visited once
# Space Complexity: O(1), only pointers used, no extra storage
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next
