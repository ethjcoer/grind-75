# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Initialize a pointer that defaults to root.
        cur = root

        # Traverse the tree until the LCA is found.
        while cur:
            # Both q and p are greater than cur;
            # LCA must be in the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # Both q and p are less than cur;
            # LCA must be in the left subtree.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # Either q and p sits on opposite sides of cur,
            # or one of them is cur.
            # Then cur must be the LCA.
            else:
                return cur
