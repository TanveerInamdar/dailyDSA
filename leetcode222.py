# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def lefth(root):

            if not root:
                return 0
            count = 1
            while root.left:
                count += 1
                root = root.left
            return count

        def righth(root):
            if not root:
                return 0
            count = 1
            while root.right:
                count += 1
                root = root.right
            return count

        x = lefth(root)
        y = righth(root)

        if x == y:
            return 2 ** x - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
