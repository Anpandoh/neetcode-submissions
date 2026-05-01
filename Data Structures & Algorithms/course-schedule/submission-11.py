from collections import defaultdict
from typing import List, Dict, Set

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: Dict[int, List[int]] = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        memo: Dict[int, bool] = {}
        visiting: Set[int] = set()

        for i in range(numCourses):
            if self.dfs(i, graph, memo, visiting) == False:
                return False

        return True

    def dfs(self, node: int, graph: Dict[int, List[int]], memo: Dict[int, bool], visiting: Set[int]) -> bool:
        if node in memo:
            return memo[node]

        if node in visiting:
            return False

        visiting.add(node)

        for neighbor in graph.get(node, []):
            if self.dfs(neighbor, graph, memo, visiting) == False:
                memo[node] = False
                visiting.remove(node)
                return False

        visiting.remove(node)
        memo[node] = True
        return True