# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inOrder(root):
            if root == None:
                return
            inOrder(root.left)
            l1.append(root)
            inOrder(root.right)

        l1 = []
        inOrder(root)
        x, y = None, None
        for i in range(len(l1) - 1):
            if l1[i].val > l1[i + 1].val:
                if x is None:
                    x = l1[i]
                    y = l1[i + 1]
                else:
                    y = l1[i + 1]
        x.val, y.val = y.val, x.val
