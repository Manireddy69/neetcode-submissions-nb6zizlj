# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        num = TreeNode(val)
        if not root:
            return TreeNode(val)
        while curr:
            if curr.val < val:
                if curr.right is None:
                    curr.right = num
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = num
                    break
                else:
                    curr = curr.left
        return root