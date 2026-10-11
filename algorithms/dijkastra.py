import heapq

def dijkstra(start, goal, walls, rows, cols, terrain_costs=None):
    if terrain_costs is None:
        terrain_costs={}

    priority_queue = [(0, start)]
    costs = {start: 0}
    came_from = {start: None}
    visited = set()

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)

        if current_cost != costs[current]:
            continue

        visited.add(current)
        yield current, visited, []

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            
