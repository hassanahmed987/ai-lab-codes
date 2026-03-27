def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited and print it
    visited.add(node)
    print(node, end=" ")

    # Recur for all the neighbors that haven't been visited
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example Graph
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

print("DFS Traversal starting from node A:")
dfs(graph, 'A')
