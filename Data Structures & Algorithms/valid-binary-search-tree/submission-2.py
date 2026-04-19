# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(currNode, left, right):
            if not currNode:
                return True
            if not (left.val < currNode.val < right.val):
                return False
            return dfs(currNode.left, left, currNode) and dfs(currNode.right, currNode, right)


        return dfs(root, TreeNode(float("-inf")), TreeNode(float("inf")))
        