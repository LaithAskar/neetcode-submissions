# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a, b):
            if not a and not b:
                return True# Both missing
            if not a or not b:
                return False# Only one missing
            if a.val != b.val:
                return False# Values differ    
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)# Compare both corresponding child pairs

        # The larger search tree is exhausted
        if not subRoot:
            return True
        if not root:
            return False

        # Check the current position, then search left and right
        return (
            sameTree(root, subRoot)# match here
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)# OR search root.left
            # OR search root.right
        )
