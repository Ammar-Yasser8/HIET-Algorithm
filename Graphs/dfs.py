"""
Depth-First Search (DFS)
Graph traversal algorithm that explores as far as possible along each branch.
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

def dfs(graph, start, visited=None):
    """
    Perform DFS traversal on graph.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
        visited: Set of visited vertices
    
    Returns:
        List of vertices in DFS order
    """
    if visited is None:
        visited = set()
    
    result = []
    
    if start not in visited:
        visited.add(start)
        result.append(start)
        
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                result.extend(dfs(graph, neighbor, visited))
    
    return result


if __name__ == "__main__":
    # Example usage
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    result = dfs(graph, 'A')
    print(f"DFS traversal starting from 'A': {result}")
