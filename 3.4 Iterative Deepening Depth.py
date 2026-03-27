def dls(graph, node, target, limit, visited):
    if node == target:
        return True
    if limit <= 0:
        return False

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            # Recursively call DLS with a reduced limit
            if dls(graph, neighbor, target, limit - 1, visited):
                return True
    return False

def iddfs(graph, start_node, target, max_depth):
    for limit in range(max_depth + 1):
        print(f"Searching with Limit: {limit}")
        visited = set()
        if dls(graph, start_node, target, limit, visited):
            print(f"Target {target} found!")
            return True
    print("Target not found within max depth.")
    return False

# Example Graph
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

iddfs(graph, 'A', 'F', 3)
