def dfs(graph, current_node, goal_value, visited=None):
    # Initialize visited set if not provided
    if visited is None:
        visited = []
    
    # Base case: if current node is the goal value, return it
    if current_node == goal_value:
        return current_node
    
    # Mark current node as visited
    visited.append(current_node)
    
    # Recursive DFS for each neighbor of the current node
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal_value, visited)
            if result:
                return result
    
    # If goal node is not found, return None
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

# Perform DFS
goal_node = dfs(graph, "A", "E")

# Check if goal node is found
if goal_node:
    print("Goal found. Node with value:", goal_node)
else:
    print("Goal not found.")
