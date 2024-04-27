def dls(graph, current_node, goal_value, depth_limit, current_depth=0, visited=None):
    # Initialize visited set if not provided
    if visited is None:
        visited = []
    
    # Base case: if current node is the goal value, return it
    if current_node == goal_value:
        return current_node
    
    # Mark current node as visited
    visited.append(current_node)
    
    # Check if depth limit exceeded
    if current_depth >= depth_limit:
        return None
    
    # Recursive DLS for each neighbor of the current node
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            result = dls(graph, neighbor, goal_value, depth_limit, current_depth + 1, visited)
            if result:
                return result
    
    # If goal node is not found within depth limit, return None
    return None

# Example usage:
# Define the graph as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

# Set the depth limit
depth_limit = 2

# Perform DLS
goal_node = dls(graph, "A", "E", depth_limit)

# Check if goal node is found
if goal_node:
    print("Goal found within depth limit {}. Node with value: {}".format(depth_limit, goal_node))
else:
    print("Goal not found within depth limit {}.".format(depth_limit))
