import heapq

def ucs(graph, start_node, goal_node):
    frontier = [(0, start_node)]  # (path_cost, node)
    explored = []
    came_from = {}  # Dictionary to store parent nodes
    
    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        explored.append(current_node)
        
        # if current node is optimal cost so return the path 
        if current_node == goal_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from.get(current_node) #get the parent node
            path.reverse()
            return path
        
        # Step 5: Explore the selected node's neighbors
        for neighbor, neighbor_cost in graph[current_node].items():
            total_cost = current_cost + neighbor_cost
            
            if neighbor not in explored:
                heapq.heappush(frontier, (total_cost, neighbor))
                came_from[neighbor] = current_node  # Update parent node
    
     # Step 6: If goal node not found, return None
    return None

# Example usage:
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'D': 3, 'E': 6},
    'C': {'F': 4, 'G': 7},
    'D': {},
    'E': {'G': 2},
    'F': {},
    'G': {}
}

start_node = 'A'
goal_node = 'G'
path = ucs(graph, start_node, goal_node)

if path:
    print("Actual Path (Optimal Solution):", path)
else:
    print("Goal not reachable from the start node.")
