from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []

        self.adj[v].append(w)

        if w not in self.adj:
            self.adj[w] = []

    def BFS(self, start, goal):
        visited = [start]
        queue = deque([start])

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node == goal:
                print("\nGoal Found!")
                return True

            for i in self.adj[node]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        print("\nGoal not found")
        return False


g = Graph()

g.addEdge('A','B')
g.addEdge('A','F')
g.addEdge('A','D')
g.addEdge('A','E')
g.addEdge('B','A')
g.addEdge('B','K')
g.addEdge('B','J')
g.addEdge('K','B')
g.addEdge('K','N')
g.addEdge('K','M')
g.addEdge('F','A')
g.addEdge('D','A')
g.addEdge('D','G')
g.addEdge('G','D')
g.addEdge('E','A')
g.addEdge('E','C')
g.addEdge('C','E')
g.addEdge('E','H')
g.addEdge('H','E')
g.addEdge('E','I')
g.addEdge('I','E')
g.addEdge('I','L')
g.addEdge('L','I')


print("BFS Traversal:")
go=input("Enter goal: ")

g.BFS('A', go)