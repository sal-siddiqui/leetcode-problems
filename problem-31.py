# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Brute Force using Array
# Idea: Store the values of the linked list in an array and check if the array is a palindrome.
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(n), for storing node values
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]


# Solution 2: Optimized Two-Pointer + Reverse Second Half
# Idea: Use slow and fast pointers to find the middle, reverse the second half, and compare both halves.
# Time Complexity: O(n), each node is visited at most twice
# Space Complexity: O(1), reversing in place requires no extra storage
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare first half and reversed second half
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
