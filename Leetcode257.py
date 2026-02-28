# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def paths(root, arr):

            if not root:
                return

            arr.append(root.val)
            if not root.right and not root.left:
                strin = ""
                for num in arr:
                    strin += str(num) + "->"
                res.append(strin[:-2])
            if root.left:
                paths(root.left, arr)

            if root.right:
                paths(root.right, arr)
            arr.pop()

        x = paths(root, [])
        return res