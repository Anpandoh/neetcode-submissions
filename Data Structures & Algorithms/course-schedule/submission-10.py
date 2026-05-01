from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for course, prereq in prerequisites:
                graph[course].append(prereq)
        
        memo: Dict[int, bool] = {}

        for i in range(numCourses):
            if self.dfs([i], graph.get(i, []), graph, memo) == False:
                return False

        
        return True





    def dfs(self, target, path, graph, memo):
        if not path:
            return True
        for node in path:
            if node in memo:
                if memo[node] == False:
                    return False
                continue
        if set(target) & set(path):
            return False
        for node in path:
            if self.dfs(target + [node], graph.get(node, []), graph, memo) == False:
                memo[node] = False
                return False
            memo[node] = True
        
        return True
        

        