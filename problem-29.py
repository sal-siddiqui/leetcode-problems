# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Brute Force with Dummy Node
# Idea: Use a dummy node to handle edge cases and iterate through the list, skipping nodes with the target value.
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(1), no extra space besides dummy node
def removeElements(self, head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next


# Solution 3: Iterative without Dummy Node
# Idea: First, skip all leading nodes with the target value, then iterate through the remaining list and remove matching nodes.
# Time Complexity: O(n), each node is visited once
# Space Complexity: O(1), no extra space used
def removeElements(self, head, val):
    # Skip leading nodes with target value
    while head and head.val == val:
        head = head.next

    current = head
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return head
