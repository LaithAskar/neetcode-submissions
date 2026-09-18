class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # For a graph to be a valid tree, it must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build an adjacency list for nodes 0 through n - 1
        neighbors = {i: [] for i in range(n)}

        for a, b in edges:
            # Add the undirected edge in both directions
            neighbors[a].append(b)
            neighbors[b].append(a)

        visited = set()

        def dfs(node, parent):
            # Mark the current node as visited
            visited.add(node)

            for neighbor in neighbors[node]:
                # Ignore the edge we used to arrive here
                if neighbor == parent:
                    continue

                # A visited non-parent neighbor means a cycle
                if neighbor in visited:
                    return False

                # Recursively inspect an unvisited neighbor
                if not dfs(neighbor, node):
                    return False

            # No cycle found through this node
            return True

        # Require both:
        # 1. DFS found no cycle
        # 2. DFS reached all n nodes
        return dfs(0, -1) and len(visited) == n