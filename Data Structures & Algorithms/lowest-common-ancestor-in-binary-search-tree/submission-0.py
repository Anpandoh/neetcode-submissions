# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(currNode):
            if currNode.val == p.val or currNode.val == q.val:
                return currNode
            if currNode.val > p.val and currNode.val < q.val:
                return currNode
            if currNode.val < p.val and currNode.val > q.val:
                return currNode
            if currNode.val < p.val and currNode.val < q.val:
                return dfs(currNode.right)
            if currNode.val > p.val and currNode.val > q.val:
                return dfs(currNode.left)
        
        return dfs(root)