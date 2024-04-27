import heapq

def astar(graph, start, goal, heuristic):
    # Initialize open list (priority queue) with start node
    open_list = [(0, start)]  # Priority queue sorted by f(n) = g(n) + h(n)
    heapq.heapify(open_list)
    # Initialize dictionaries to store g-values and parent nodes
    g_values = {node: float('inf') for node in graph}
    g_values[start] = 0
    parents = {start: None}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        # If current node is the goal, reconstruct and return the path
        if current_node == goal:
            return reconstruct_path(goal, parents)

        # Expand neighbors of current node
        for neighbor, cost in graph[current_node].items():
            # Calculate tentative g-value for neighbor
            tentative_g = g_values[current_node] + cost
            # Update if tentative g-value is lower than current g-value
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + euclidean_distance(neighbor, goal)
                # Add neighbor to open list if not already present
                heapq.heappush(open_list, (f_value, neighbor))
                # Update parent of neighbor
                parents[neighbor] = current_node

    # If goal node is not found, return an empty path
    return []

def reconstruct_path(goal, parents):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parents[goal]  # Move to parent node
    return path[::-1]  # Reverse path to start from start node

# Example usage:
# Define graph as an adjacency list with weighted edges
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 7, 'E': 3},
    'C': {'F': 12},
    'D': {'G': 15},
    'E': {'G': 8},
    'F': {'G': 10},
    'G': {}
}

# Define a heuristic function (e.g., Euclidean distance)
def euclidean_distance(node, goal):
    coordinates = {'A': (0, 0), 'B': (2, 3), 'C': (4, 1), 'D': (6, 5), 'E': (7, 2), 'F': (8, 4), 'G': (10, 0)}
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

start_node = 'A'
goal_node = 'G'

# Perform A* search
path = astar(graph, start_node, goal_node, euclidean_distance)

if path:
    print("Shortest path from {} to {}: {}".format(start_node, goal_node, path))
    print("Total cost:", sum(graph[node][path[index+1]] for index, node in enumerate(path[:-1])))
else:
    print("No path found from {} to {}.".format(start_node, goal_node))
