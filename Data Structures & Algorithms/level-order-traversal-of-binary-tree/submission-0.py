# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # #bfs
        res = []
        queue = []
        if root:
            queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                currNode = queue.pop(0)
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(level)

        return res
        #dfs
        # res = []
        # def dfs(currNode, level):
        #     if not currNode:
        #         return
        #     res[level] += [currNode]
        #     print(res)
        #     dfs(currNode.left, level + 1)
        #     dfs(currNode.right, level + 1)

        # dfs(root, 0)
        # return res
            

