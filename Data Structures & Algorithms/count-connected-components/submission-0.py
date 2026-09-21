class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
         # Build an adjacency list for every node
        neighbors = {i: [] for i in range(n)}

        for a, b in edges:
            # Undirected edge: add both directions
            neighbors[a].append(b)
            neighbors[b].append(a)

        visited = set()

        def dfs(node):
            # Mark this node as visited
            visited.add(node)

            # Visit every unvisited neighbor
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        components = 0

        # Every unvisited node begins a new component
        for node in range(n):
            if node not in visited:
                # Count this component
                components += 1
                # Mark all nodes belonging to it
                dfs(node)

        return components
