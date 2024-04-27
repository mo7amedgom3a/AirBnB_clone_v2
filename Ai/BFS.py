from collections import deque

def bfs(graph, start_node, goal_value):
    # Initialize a queue to keep track of nodes to be explored
    queue = []
    
    # Initialize a list to keep track of visited nodes
    visited = []
    
    # Enqueue the start node root node
    queue.append(start_node)
    
    # Mark start node as visited
    visited.append(start_node)
    
    # While there are nodes to explore in the queue
    while queue:
        # Dequeue a node from the front of the queue
        current_node = queue.pop(0)
        
        # If current node contains the goal value, return success
        if current_node == goal_value:
            return current_node
        
        # For each neighbor of the current node for each child in expand(problem, current node)
        for neighbor in graph[current_node]:
            # If neighbor has not been visited
            if neighbor not in visited:
                # Mark neighbor as visited
                visited.append(neighbor)
                
                # Enqueue neighbor for exploration
                queue.append(neighbor)
    
    # If goal node is not found, return None
    return None

# Example usage:
# Define the graph as a dictionary

if __name__ == "__main__":

    graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
    }
    # Perform BFS
    print("please enter the first node and the goal node to apply BFS from this graph")
    print("*" * 50)
    for i in graph:
        print(f"{i} ==> conncted to {graph[i]}")
    print("*" * 50)

    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    goal_node = bfs(graph, start_node, goal_node )

    # Check if goal node is found
    if goal_node:
        print("Goal found. Node with value:", goal_node)
    else:
        print("Goal not found.")
