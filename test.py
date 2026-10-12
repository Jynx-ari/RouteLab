
from algorithms.dijkstra import dijkstra

start = (1, 0)
goal = (1, 2)

walls = set()

# The direct middle cell is expensive.
terrain_costs = {
    (1, 1): 10,
}

steps = dijkstra(
    start,
    goal,
    walls,
    rows=3,
    cols=4,
    terrain_costs=terrain_costs,
)

visited = set()
path = []

for current, explored, result in steps:
    visited = explored
    if current is None:
        path = result

total_cost = sum(
    terrain_costs.get(cell, 1)
    for cell in path[1:]
)

print("Path:", path)
print("Moves:", len(path) - 1 if path else 0)
print("Total cost:", total_cost)
print("Expected total cost: 4")

assert path, "Dijkstra should find a route."
assert (1, 1) not in path, "It should avoid the expensive cell."
assert total_cost == 4, "The cheapest route should cost 4."

print("All Dijkstra tests passed!")
