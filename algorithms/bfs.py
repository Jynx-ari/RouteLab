from collections import deque

def bfs(start, goal, walls, rows, cols):
    queue = deque([start])
    came_from = {start: None}
    visited = set()

    while queue: 
        current = queue.popleft()
        visited.add(current)

        yield current, visited, []

        if current == goal:
            path = []
            #path clear!

            while current != None:
                path.append(current)
                current = came_from[current]
            
            #time to look back
            path.reverse()
            yield None, visited, path
            return
        
        row, col = current

        following_neigbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col +1),
        ]
        for neighbor in following_neigbors:
            r, c = neighbor
            if not (0<=r<rows):
                continue
            if not (0<=c<cols):
                continue
            if neighbor in walls or neighbor in came_from:
                continue
            #Remember from neighbor to current so we can backtrack later
            came_from[neighbor] = current
            queue.append(neighbor)
    yield None, visited, []