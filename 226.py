# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        save = root.left
        root.left = root.right
        root.right = save
        return root