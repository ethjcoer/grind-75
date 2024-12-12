# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Solution info: https://www.youtube.com/watch?v=QfJsau0ItOY
        # Gemini for revisions (I got lazy)
        """
        Checks if a binary tree is balanced. A balanced tree
        is defined as a tree where the absolute difference
        in heights of left and right subtrees for each node
        is at most 1.
        """

        def dfs(root):
            """
            DFS helper function. Returns a tuple:
            - balanced: True if subtree is balanced, False otherwise
            - height: Height of the subtree
            """
            if not root:
                return True, 0
            left_bal, left_h = dfs(root.left)
            right_bal, right_h = dfs(root.right)
            return (
                left_bal and right_bal and abs(left_h - right_h) <= 1,
                max(left_h, right_h) + 1,
            )

        return dfs(root)[0]
