import heapq

def a_star_search(graph, costs, heuristics, start, target):
    # Priority Queue stores: (f_score, current_node, current_g_score, path)
    # f_score = g_score (actual) + h_score (heuristic)
    priority_queue = [(heuristics[start], start, 0, [start])]
    visited = {} # Store node: best_g_score found so far

    while priority_queue:
        f, current_node, g, path = heapq.heappop(priority_queue)

        # If we've already found a cheaper way to this node, skip it
        if current_node in visited and visited[current_node] <= g:
            continue
        
        visited[current_node] = g

        # Goal Check
        if current_node == target:
            return path, g

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            new_g = g + weight
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(priority_queue, (new_f, neighbor, new_g, path + [neighbor]))

    return None, float('inf')

# --- Example Data ---
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 4},
    'F': {}
}

heuristics = {'A': 6, 'B': 4, 'C': 2, 'D': 1, 'E': 3, 'F': 0}

path, total_cost = a_star_search(graph, None, heuristics, 'A', 'F')
print(f"Optimal Path: {path} | Total Cost: {total_cost}")
