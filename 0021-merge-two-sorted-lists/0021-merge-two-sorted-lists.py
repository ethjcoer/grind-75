# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Explanation video: https://www.youtube.com/watch?v=5Rec4JS9H5o

        # Create a dummy node to start the output list.
        # <dummy node> -> <...other nodes>
        # At the end, return just the <other nodes>.
        dummy = ListNode()
        # Create a pointer to keep track of the tail.
        pointer = dummy

        # Compare the heads of both lists until one becomes empty.
        while list1 and list2:

            # Append the node with the smaller value to the dummy node,
            # then unlink it from its original list.
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next

            # Move the pointer to the newly appended node.
            pointer = pointer.next

        # If one list becomes empty (or was empty from the start),
        # append the remaining nodes of the other list.
        pointer.next = list1 if list1 else list2

        # Return the merged list starting from the node after the dummy node.
        return dummy.next
