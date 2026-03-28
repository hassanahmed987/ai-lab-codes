def hill_climbing(graph, heuristics, start, goal):
    current_node = start
    path = [start]

    while current_node != goal:
        neighbors = graph.get(current_node, [])
        
        if not neighbors:
            print("Reached a dead end (no neighbors).")
            break

        # 1. Look at all neighbors and find the "best" one
        # We want the one with the SMALLEST heuristic value
        best_neighbor = None
        best_h = heuristics[current_node]

        for neighbor in neighbors:
            if heuristics[neighbor] < best_h:
                best_h = heuristics[neighbor]
                best_neighbor = neighbor

        # 2. If we found a neighbor better than our current spot, move there
        if best_neighbor:
            current_node = best_neighbor
            path.append(current_node)
            print(f"Moving to {current_node} (h={best_h})")
        else:
            # 3. If no neighbor is better, we are at a "Peak" (Local Optimum)
            print(f"Stuck at {current_node}. No neighbors are better.")
            break

    return path if current_node == goal else None

# --- Data ---
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
# Note: For Hill Climbing to work, heuristics must strictly decrease toward the goal
heuristics = {'A': 10, 'B': 8, 'C': 5, 'D': 9, 'E': 7, 'F': 6, 'G': 0}

result = hill_climbing(graph, heuristics, 'A', 'G')
print(f"Final Path: {result}")
