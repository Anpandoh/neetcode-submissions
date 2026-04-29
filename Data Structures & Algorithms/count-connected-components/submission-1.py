from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #bfs through the graph
        #check if we have seen the starting node before, 
        #if there is a new starting node, that means there is a new component
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # print(graph)
        
        #bfs
        visitedIsland = defaultdict(set)
        allVisited = set()
        for node in graph.keys():
            q = [node]
            if node not in allVisited:
                while q:
                    currNode = q.pop(0)
                    if currNode not in visitedIsland[node]:
                        print("hey")
                        allVisited.add(currNode)
                        visitedIsland[node].add(currNode)
                        for nextNode in graph[currNode]:
                            q.append(nextNode)

        print(visitedIsland)
        return len(visitedIsland.keys()) + n - len(allVisited)


        