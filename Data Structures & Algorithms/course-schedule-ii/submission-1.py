class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = defaultdict(list)
        for prereqs in prerequisites:
            adjList[prereqs[0]].append(prereqs[1])

        visited = []
        cycle = set()
        def dfs(root):
            if root in visited:
                return visited
            if root in cycle:
                return []
            cycle.add(root)
            for node in adjList[root]:
                if not dfs(node):
                    return []
            cycle.remove(root)
            visited.append(root)
            return visited



        for i in range(numCourses):
            curr = dfs(i)
            if not curr:
                return []

        return curr
        