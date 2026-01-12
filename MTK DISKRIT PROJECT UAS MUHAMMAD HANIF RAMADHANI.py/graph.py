class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # DFS Rekursif
    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    # DFS Iteratif
    def dfs_iterative(self, start):
        visited = [False] * self.V
        stack = []

        stack.append(start)
        visited[start] = True

        while stack:
            current = stack.pop()
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

    # BFS
    def bfs(self, start):
        visited = [False] * self.V
        queue = []

        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


# ===== MAIN PROGRAM =====
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Depth First Traversal (DFS):")
g.dfs(0, [False]*4)

print("\nBreadth First Traversal (BFS):")
g.bfs(0)