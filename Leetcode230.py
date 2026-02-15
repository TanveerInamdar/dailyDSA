# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inorder(root):
            nonlocal count
            if not root:
                return

            left = inorder(root.left)
            if left is not None: return left

            count += 1
            if count == k:
                return root.val

            right = inorder(root.right)
            return right

        return inorder(root)
