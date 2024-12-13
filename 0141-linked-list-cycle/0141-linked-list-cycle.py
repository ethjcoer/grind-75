# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Solution explanation: https://www.youtube.com/watch?v=gBTe7lFR3vc
        # This function detects whether a linked list has a cycle.

        # Initialize two pointers: slow and fast. Both start at the head of the list.
        slow, fast = head, head

        # Traverse the list with the two pointers
        while fast and fast.next:
            # Move the slow pointer one step at a time
            slow = slow.next
            # Move the fast pointer two steps at a time
            fast = fast.next.next

            # If the slow pointer meets the fast pointer, a cycle exists
            if slow == fast:
                return True

        # If fast reaches the end of the list without meeting slow, there's no cycle
        return False
