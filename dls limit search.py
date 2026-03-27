def dls(graph, node, limit, visited=None):
    if visited is None:
        visited = set()

    # If limit is 0, we can't go any deeper
    if limit < 0:
        return

    print(node, end=" ")
    visited.add(node)

    # Stop exploring neighbors if we've reached the limit
    if limit > 0:
        for neighbor in graph[node]:
            if neighbor not in visited:
                dls(graph, neighbor, limit - 1, visited)

# Example Graph
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

print("DLS Traversal (Limit = 1):")
dls(graph, 'A', 1) 
# Output: A B C (It stops before reaching D, E, or F)

print("\nDLS Traversal (Limit = 2):")
dls(graph, 'A', 2)
# Output: A B D E C F
