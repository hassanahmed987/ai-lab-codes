import heapq

def best_first_search(graph, heuristics, start, target):
    # Priority Queue stores: (heuristic_value, current_node, path)
    # It sorts by the heuristic (the "guess" of distance to goal)
    priority_queue = [(heuristics[start], start, [start])]
    visited = set()

    while priority_queue:
        # Pop the node that "looks" closest to the goal
        _, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        if current_node == target:
            return path

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # We only care about the neighbor's heuristic value
                h_value = heuristics[neighbor]
                heapq.heappush(priority_queue, (h_value, neighbor, path + [neighbor]))

    return None

# Graph (Connections)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristics (Estimated distance to Goal 'F')
# These are "guesses" - lower means it looks closer to the target
heuristics = {
    'A': 10,
    'B': 8,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 0
}

path = best_first_search(graph, heuristics, 'A', 'F')
print(f"Path found by Best-First Search: {path}")
