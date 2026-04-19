class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        #adj list
        adjList = defaultdict(list)
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])
        
        #detect loops if there are any repeats (then false), go through all nodes and check
        visited = set()
        cycle = set()
        def dfs(root: int):
            if root in cycle:
                return False
            if root in visited: #visited everything in graph
                return True
            cycle.add(root)
            for node in adjList[root]:
                if not dfs(node):
                    return False
            cycle.remove(root)
            visited.add(root)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
 


        
        