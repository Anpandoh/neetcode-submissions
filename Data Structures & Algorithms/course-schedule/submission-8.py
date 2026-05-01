from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for course, prereq in prerequisites:
                graph[course].append(prereq)
        

        for key, val in graph.items():
            if self.dfs([key], val, graph) == False:
                return False
            print(key, val)

        
        return True





    def dfs(self, target, path, graph):
        if not path:
            return True
        elif set(target) & set(path):
            return False
        else:
            for node in path:
                if self.dfs(target + [node], graph.get(node, []), graph) == False:
                    return False
        

        