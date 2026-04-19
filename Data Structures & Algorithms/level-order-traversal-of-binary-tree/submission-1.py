# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #bfs

        q = []
        if root:
            q.append((root, 0))
        res = []
        while q:
            currNode, currLevel = q.pop(0)
            if len(res) - 1 == currLevel:
                res[currLevel].append(currNode.val)
            else:
                res.append([currNode.val])

            if currNode.left:
                q.append((currNode.left, currLevel + 1))
            if currNode.right:
                q.append((currNode.right, currLevel + 1))

        return res

