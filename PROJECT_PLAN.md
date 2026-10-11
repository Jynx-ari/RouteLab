# RouteLab — Full Project Plan

> **Project:** RouteLab  
> **Purpose:** A beginner-friendly, offline pathfinding laboratory built with Python and Pygame.  
> **Main direction:** Start with a reliable visual BFS maze, then add weighted terrain and Dijkstra so users can explore how the meaning of a “best route” changes when movement has different costs.  
> **Working rule:** Build one small phase at a time, test it, understand it, and commit it before moving on.

---

## 1. Project vision

RouteLab is an interactive grid where users can create a maze, choose a start and destination, and watch pathfinding algorithms search for a route.

It should teach pathfinding by making the algorithm's decisions visible. The user should be able to compare routes and understand the difference between:

- **Shortest route:** the fewest moves.
- **Lowest-cost route:** the smallest sum of movement costs.

RouteLab is a learning tool and a foundation for exploring routing concepts. It is not a GPS app and does not need online services, real maps, or location tracking.

## 2. Project goals

- [x] Draw and edit a grid maze.
- [x] Place a start cell and a goal cell.
- [x] Draw and erase walls.
- [x] Animate BFS exploration.
- [x] Reveal the resulting route with an animation.
- [x] Reset search state when the maze changes.
- [ ] Make the core behavior reliable across important edge cases.
- [ ] Add editable terrain types with different movement costs.
- [ ] Implement Dijkstra's algorithm for minimum-cost routes.
- [ ] Show route length and total route cost as separate results.
- [ ] Improve the interface and explain the visual legend clearly.
- [ ] Document, demonstrate, and release a stable version.

## 3. Current project status

The current app uses Python and Pygame. The main application is in `main.py`, and BFS is in `algorithms/bfs.py`.

Known existing behavior:

- The user can draw and erase walls.
- The user can reposition the start and goal.
- Enter starts the animated BFS search; pressing Enter while it is running stops it.
- Explored cells and the final path are animated.
- Pressing N generates a noisy/random wall layout.
- Search reset behavior has recently been corrected and manually tested.

Keep the working BFS version usable throughout development. New features should not require throwing away the current implementation.

## 4. Scope and priorities

### Must-have for the next complete milestone

1. Reliable existing maze editing and BFS behavior.
2. Terrain data and terrain-painting controls.
3. Dijkstra's algorithm for weighted movement.
4. Animated search and final route for Dijkstra.
5. Results that distinguish move count from total cost.
6. Edge-case tests and clear README instructions.

### Nice to have after the core works

- A* search that accounts for terrain costs.
- A simple algorithm selector and repeatable comparisons.
- Saved maze presets or a few example scenarios.
- Better visual styling, keyboard shortcuts, and clearer controls.
- A demo recording and screenshots for the README.

### Not part of the current scope

- GPS, live location, or a full offline navigation app.
- Downloading or processing real-world map data.
- Online accounts, servers, multiplayer, or collaboration.
- 3D graphics, traffic simulation, road rules, or complex terrain physics.
- Many algorithms added just for the sake of having more algorithms.
- Plugin systems or user-written scripts.

---

## 5. Concepts and behavior

### Grid and movement

- The grid is made of rows and columns.
- Movement is allowed in four directions: up, down, left, and right.
- Walls cannot be entered.
- The start and goal must always occupy valid, traversable cells.
- Editing the maze or terrain clears any stale search result and animation.

### Terrain and costs

Use a simple initial set of terrain types. The exact costs and colors can be tuned during implementation.

| Cell type | Initial movement cost | Behavior |
|---|---:|---|
| Normal floor | 1 | Ordinary movement |
| Grass | 2 | Slightly more expensive |
| Sand | 4 | More expensive |
| Mud | 7 | Very expensive |
| Wall | Impassable | Cannot enter |

Rules:

- Normal floor is the default; it does not need to be stored for every cell.
- A traversable cell has at most one terrain type at a time.
- A cell cannot simultaneously be a wall and weighted terrain.
- The cost is charged when entering a cell. The start cell itself contributes no entry cost; the cost of entering the goal does count.
- Keep terrain costs and colors in one clearly named definition so they are easy to change.
- Dijkstra minimizes the sum of costs, not the number of moves.
- BFS remains useful for equal-cost grids, where it minimizes the number of moves.

### Algorithm responsibilities

- **BFS:** use when every move has equal cost; finds a route with the fewest moves.
- **Dijkstra:** use when traversable cells have different non-negative costs; finds a route with the lowest total cost.
- **A* (later, optional):** use a cost-aware heuristic to guide search toward the goal. It must still account for terrain costs correctly.

Do not make BFS appear to support weighted terrain when it does not.

---

## 6. Implementation roadmap

### Phase 0 — Protect the working foundation

- [x] Keep the grid, start, goal, walls, and BFS in place.
- [x] Animate BFS exploration and final-path reveal.
- [x] Correct the search reset state.
- [x] Manually test the reset fix.
- [ ] Run through the existing controls and note any bugs before adding terrain.
- [ ] Confirm wall, start, goal, and random-maze editing always clear stale search visuals.
- [ ] Confirm an unreachable goal reports no path and does not show an old route.

**Exit condition:** the existing BFS app remains stable enough to serve as a baseline.

### Phase 1 — Design and store terrain data

- [ ] Inspect how `walls`, start, and goal are represented in `main.py`.
- [ ] Choose a simple representation, such as a dictionary mapping cell coordinates to terrain types.
- [ ] Define terrain names, costs, and colors in one location.
- [ ] Treat cells absent from the terrain dictionary as normal floor.
- [ ] Define consistent behavior for painting terrain on a wall or moving the start/goal onto a terrain cell.
- [ ] Ensure maze generation and search reset handle terrain predictably.

**Exit condition:** terrain can be represented correctly without yet changing the pathfinding algorithm.

### Phase 2 — Add terrain editing to the interface

- [ ] Add a terrain mode without removing wall, start, or goal modes.
- [ ] Let the user choose which terrain type to paint.
- [ ] Let the user restore a cell to normal floor.
- [ ] Prevent invalid overlaps between walls and terrain.
- [ ] Show the selected editing mode and terrain type.
- [ ] Add a clear terrain legend.
- [ ] Reset the active search whenever terrain changes.

**Exit condition:** users can paint, replace, and erase terrain, and the drawing always matches the stored grid state.

### Phase 3 — Implement Dijkstra as a separate algorithm

- [ ] Create `algorithms/dijkstra.py`.
- [ ] Learn how a priority queue selects the cell with the lowest known route cost.
- [ ] Track the cheapest known cost to reach each cell.
- [ ] Track predecessors so the route can be reconstructed.
- [ ] Respect walls and grid boundaries.
- [ ] Use terrain cost when entering a neighbor.
- [ ] Return a clear result when the goal is reached or unreachable.
- [ ] Keep the algorithm independent of Pygame drawing.
- [ ] Add small, repeatable tests for the algorithm before connecting it to the interface.

**Exit condition:** Dijkstra returns a minimum-cost route for hand-checked examples, including one where the cheapest route is longer in number of moves.

### Phase 4 — Connect Dijkstra to the visualizer

- [ ] Add a simple way to choose BFS or Dijkstra.
- [ ] Reuse the current animation approach where it makes the code clearer.
- [ ] Animate Dijkstra's explored cells.
- [ ] Reveal the final route without leaving old animation state behind.
- [ ] Make reset, stop, wall editing, terrain editing, start/goal movement, and random-maze generation work consistently.
- [ ] Show the selected algorithm and search status.
- [ ] Handle unreachable goals without a stale route or stale cost.

**Exit condition:** users can switch between BFS and Dijkstra and run each on the same grid reliably.

### Phase 5 — Explain the results

- [ ] Count the cells explored by the search.
- [ ] Display the number of moves in the final route.
- [ ] Display the total movement cost of the final route.
- [ ] Clearly label route length and route cost as different measurements.
- [ ] Ensure the start and goal remain visible over other visualization layers.
- [ ] Use consistent colors for walls, terrain, explored cells, final route, start, and goal.
- [ ] Avoid adding statistics that cannot be explained or verified.

**Exit condition:** a user can tell which route was found, how many moves it takes, and why its total cost matters.

### Phase 6 — Test and stabilize

- [ ] Test an open grid with no walls or weighted terrain.
- [ ] Test a direct route.
- [ ] Test a route that must detour around walls.
- [ ] Test an unreachable goal.
- [ ] Test start next to goal.
- [ ] Test start and goal surrounded by walls where applicable.
- [ ] Test a high-cost terrain strip where going around is cheaper.
- [ ] Test a case where the fewest-move route is not the lowest-cost route.
- [ ] Test a route containing several terrain types.
- [ ] Test painting terrain over a wall and painting a wall over terrain.
- [ ] Test moving start and goal onto terrain.
- [ ] Test reset after both successful and unsuccessful searches.
- [ ] Test editing terrain during a search and during path animation.
- [ ] Test generating a new maze after terrain has been painted.
- [ ] On an all-normal grid, confirm Dijkstra's total route cost equals its move count under the entry-cost rule above.
- [ ] On an all-normal grid, confirm Dijkstra and BFS both find a minimum-move route; their exact routes may differ.
- [ ] Confirm no stale path, cost, or animation remains after reset or editing.

**Exit condition:** the core scenarios behave correctly and repeatably.

### Phase 7 — Polish and present the project

- [ ] Improve spacing, labels, colors, and controls without obscuring the grid.
- [ ] Keep the interface beginner-friendly and offline.
- [ ] Update README controls, terrain costs, algorithm explanations, and screenshots.
- [ ] Explain what BFS optimizes versus what Dijkstra optimizes.
- [ ] Add a short demo showing a weighted route choice.
- [ ] Document known limitations and possible future work.
- [ ] Review the code and remove temporary debug output.

**Exit condition:** RouteLab is understandable to someone seeing it for the first time and is ready to demonstrate.

### Phase 8 — Optional future extension: A*

Only start this after weighted terrain and Dijkstra are reliable.

- [ ] Implement A* in its own module.
- [ ] Use a heuristic compatible with four-directional movement and the minimum terrain cost.
- [ ] Account for terrain costs in the known path cost.
- [ ] Compare A* and Dijkstra on identical weighted mazes.
- [ ] Compare explored-cell counts and total route costs.
- [ ] Verify that both return minimum-cost routes under the chosen rules.
- [ ] Document that A* often explores fewer cells but is not guaranteed to do so on every maze.

**Exit condition:** A* is an understandable, tested comparison—not just another option in a menu.

---

## 7. Suggested work rhythm

For each small task:

1. Read the relevant code before editing.
2. Make one focused change.
3. Run the app or the algorithm test.
4. Check the expected behavior and one likely edge case.
5. Commit the working change with a descriptive message.
6. Update this checklist only when the task is actually complete.

If a phase feels too large, split it into smaller tasks. Do not start a later phase just because the checklist exists.

## 8. Definition of done

RouteLab's weighted-terrain milestone is complete when:

- Users can edit walls and terrain.
- BFS still works on equal-cost grids.
- Dijkstra finds the lowest-cost route across weighted terrain.
- Search and path animations remain reliable after edits and resets.
- The app shows route length and total cost separately.
- Important edge cases pass.
- The README explains the controls, terrain costs, and algorithm differences.
- The creator can explain how the algorithms work and why they may choose different routes.

## 9. Long-term direction

RouteLab can later help explore how real routing systems represent a road network as a graph: intersections become nodes, roads become connections, and road distance or travel cost becomes an edge weight.

That would be a separate project requiring map data and additional systems. It is not needed for RouteLab's current goals.

---

**Guiding principle:** build the smallest complete thing that teaches something real. A reliable, understood project is better than a large unfinished one.
