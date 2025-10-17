"""
Breadth-First Search (BFS)
Graph traversal algorithm that explores vertices level by level.
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque

def bfs(graph, start):
    """
    Perform BFS traversal on graph.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
    
    Returns:
        List of vertices in BFS order
    """
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
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
    
    result = bfs(graph, 'A')
    print(f"BFS traversal starting from 'A': {result}")
