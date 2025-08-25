# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def binary(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return binary(p.left, q.left) and binary(p.right, q.right)

        def find(p, q):
            if p and q:
                if p.val != q.val:
                    return find(p.left, q) or find(p.right, q)
                elif p.val == q.val:
                    return binary(p, q) or find(p.left, q) or find(p.right, q)
            else:
                return False

        return find(root, subRoot)

