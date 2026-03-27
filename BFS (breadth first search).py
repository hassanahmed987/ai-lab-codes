from collections import deque

def bfs(graph, start_node):
    # Keep track of visited nodes to avoid infinite loops
    visited = set()
    # Create a queue and enqueue the starting node
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        # Remove the first node added to the queue
        current_node = queue.popleft()
        print(current_node, end=" ") 

        # Check all neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example Graph
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

print("BFS Traversal starting from node A:")
bfs(graph, 'A')
