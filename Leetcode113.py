# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def hasPathSum(root: Optional[TreeNode], targetSum: int, path) -> bool:

            if not root:
                return
            path.append(root.val)

            if not root.left and not root.right:
                if root.val == targetSum:
                    res.append(path[:])
            else:
                x = hasPathSum(root.left, targetSum - root.val, path) or hasPathSum(root.right, targetSum - root.val,
                                                                                    path)
            path.pop()

        hasPathSum(root, targetSum, path)
        return res