# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: Generally Linear O(N), but more specifically 
            O(N+E) or O(V+E), in which E is edges & V for vertices,
        Space Complexity: We're initializing 3 new data structures ->
            performance depends on the length of these sets, Linear O(N)
    """
    # guard-clause for an early-exit
    if not dislikes:
        return True

    queue = deque()
    visited = set()
    red = set()
    green = set()

    if dislikes[0]:
        start_node = 0
    else:
        start_node = 1
    
    queue.append(start_node)
    visited.add(start_node)
    red.add(start_node)

    while len(queue) != 0:
        current = queue.popleft()
        for neighbor in dislikes[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if current in red:
                    green.add(neighbor)
                else:
                    red.add(neighbor)
            elif neighbor in visited:
                if current in red and neighbor in red:
                    return False
                if current in green and neighbor in green:
                    return False

    return True
