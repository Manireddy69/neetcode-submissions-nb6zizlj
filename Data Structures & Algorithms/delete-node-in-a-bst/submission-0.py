# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        ## if we want to take value from left subtree we take max(subtree)
        ## if we want to take value from right subtree we take min(subtree)
        def findmax(root):
            if not root:
                return None
            while root.right:
                root = root.right
            return root
        def findmin(root):
            while root:
                root = root.left
            return root
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            max_left = findmax(root.left) ## find the max(left subtree)
            root.val = max_left.val ## copy the val
            root.left = self.deleteNode(root.left, max_left.val)
        return root
            
