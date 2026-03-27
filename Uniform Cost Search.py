import heapq

def ucs(graph, start_node, target):
    # Priority Queue stores: (total_cost, current_node, path_taken)
    # heapq always pops the item with the SMALLEST total_cost
    priority_queue = [(0, start_node, [start_node])]
    visited = set()

    while priority_queue:
        # Pop the node with the lowest cumulative cost
        (cost, current_node, path) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        
        # If we reached the goal, we found the cheapest path!
        if current_node == target:
            return path, cost

        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                total_cost = cost + weight
                heapq.heappush(priority_queue, (total_cost, neighbor, path + [neighbor]))

    return None, float('inf')

# Example Weighted Graph
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 10, 'E': 7},
    'C': {'F': 1},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

path, total_cost = ucs(graph, 'A', 'F')
print(f"Cheapest Path: {path} with Total Cost: {total_cost}")
