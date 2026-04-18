# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_sex):
            if not root:
                return 0
            good = 1 if root.val >= max_sex else 0

            new_max = max(max_sex, root.val)

            good += dfs(root.left, new_max)
            good += dfs(root.right, new_max)

            return good
        return dfs(root, float('-inf'))