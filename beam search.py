def beam_search(graph, heuristics, start, goal, beam_width):
    # We start with just the initial node in our "beam"
    # Structure: [(heuristic, current_node, path)]
    current_beam = [(heuristics[start], start, [start])]
    
    while current_beam:
        candidates = []
        
        # 1. Expand all nodes in the current beam
        for _, current_node, path in current_beam:
            if current_node == goal:
                return path
            
            for neighbor in graph.get(current_node, []):
                if neighbor not in path: # Basic cycle check
                    new_path = path + [neighbor]
                    candidates.append((heuristics[neighbor], neighbor, new_path))
        
        # 2. Sort all potential next steps by heuristic (best first)
        candidates.sort()
        
        # 3. "The Beam": Only keep the top 'k' candidates for the next level
        current_beam = candidates[:beam_width]
        
        print(f"Current Beam: {[node for _, node, _ in current_beam]}")

    return None

# --- Data ---
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

heuristics = {
    'A': 10, 'B': 8, 'C': 3, 'D': 6, 'E': 5, 'F': 2, 'G': 1
}

# Try with a Beam Width of 2
result = beam_search(graph, heuristics, 'A', 'G', beam_width=2)
print(f"Path found: {result}")
