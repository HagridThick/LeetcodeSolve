# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth_left,depth_right = 0, 0
        if root.left:
            depth_left = self.maxDepth(root.left)
        if root.right:
            depth_right = self.maxDepth(root.right)
        return max(depth_left,depth_right) + 1
