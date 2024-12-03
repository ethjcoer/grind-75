# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Solution using breadth-first search (BFS).
        # Python's deque object allows for efficient FIFO operations.
        # In LeetCode this is automatically imported for you.

        # Prepare a queue for nodes.
        queue = deque()
        # Insert the root node in the queue.
        queue.appendleft(root)

        # Traverse the tree in a breadth-first manner.
        while queue:
            # Remove and return the last node from the queue for processing.
            node = queue.pop()
            # Check if the node is not None (i.e., the node exists).
            # This ensures we don't try to process a None node.
            if node:
                # Swap left and right children of the current node.
                node.left, node.right = node.right, node.left
                # Add the children to the queue for further processing.
                queue.appendleft(node.right)
                queue.appendleft(node.left)

        # Return the root after the tree has been inverted.
        return root
