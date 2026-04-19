# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #dfs

        def dfs(currNode, depth):
            if not currNode:
                return depth
            return max(dfs(currNode.left, depth + 1), dfs(currNode.right, depth + 1))

        return dfs(root, 0)
        