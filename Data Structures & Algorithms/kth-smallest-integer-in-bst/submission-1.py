# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #(recurs)
        #go all the way to the left, saving nodes

        #iterate backwards through save nodes, for each nodes, iterate all the way again left to right using dfs, keep a count
        # in order traversal
        ans = 0
        def recurs(currNode):
            nonlocal k, ans
            if not currNode:
                return
            recurs(currNode.left)
            k -= 1
            if k == 0:
                ans = currNode.val
            recurs(currNode.right)

        recurs(root)
        return ans
        # return arr[k-1]
            
