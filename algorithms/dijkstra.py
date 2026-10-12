import heapq

def dijkstra(start, goal, walls, rows, cols, terrain_costs=None):
    if terrain_costs is None:
        terrain_costs={}
        print("no costs")

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

            path.reverse()
            yield None, visited, path
            return

        row, col = current

        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 2),
        ]

        for neighbor in neighbors:
            r, c = neighbor
            if not ( 0<= r <rows and 0 <=c < cols):
                continue

            if neighbor in walls:
                continue

            step_cost = terrain_costs.get(neighbor, 1)
            new_cost = current_cost + step_cost


            if new_cost> costs.get(neighbor, float("inf")):
                costs[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor),
                )
                
    yield None, visited, []