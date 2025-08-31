# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        def post(root):
            if not root:
                return
            left = post(root.left)
            right = post(root.right)
            res.append(root.val)
            return res

        return post(root)