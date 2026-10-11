# RouteLab: Weighted Terrain Implementation Plan

> Goal: extend RouteLab from a wall-only maze into a small pathfinding laboratory where different terrain types have different movement costs.
>
> Keep the project understandable and build this in small, testable steps. Do not start every phase at once.

## Current baseline

- [x] Editable grid with start and goal cells
- [x] Draw and erase walls
- [x] Animate Breadth-First Search (BFS) exploration
- [x] Animate the final path
- [x] Reset search state when the maze changes
- [ ] Add weighted terrain

## What weighted terrain means

A traversable cell can have a movement cost. The pathfinder should minimize the **total cost** of a route, not simply the number of cells in it.

Initial terrain rules:

| Cell type | Suggested cost | Meaning |
|---|---:|---|
| Normal floor | 1 | Ordinary movement |
| Grass | 2 | Slightly harder to cross |
| Sand | 4 | More expensive movement |
| Mud | 7 | Very expensive movement |
| Wall | Impassable | Cannot enter |

These values are initial design choices, not fixed requirements. Keep them in one clearly named place in the code so they can be changed easily.

**Important:** the cost is paid when entering a terrain cell. The start cell does not add a cost to the route. The goal cell's terrain cost does count if the route enters it.

## Decisions and boundaries

- Keep the existing grid and mouse interaction model.
- Preserve BFS for ordinary equal-cost mazes.
- Add **Dijkstra's algorithm** as the first weighted pathfinding algorithm. It can find a minimum-cost route when movement costs are non-negative.
- Do not change the existing BFS to pretend it supports weighted costs; BFS minimizes the number of moves when every move has the same cost.
- Show the total cost of the final route, separately from its number of moves.
- Keep this version offline and single-user. No map downloads, GPS, networking, or complex simulation.
- Consider A* with terrain costs only after weighted terrain and Dijkstra are working reliably.
- Do not prioritize a full interface redesign yet. Make only the small controls and legend needed to use the feature.

## Phase 1 — Define terrain data

- [ ] Decide how terrain is represented in memory (for example, a dictionary mapping grid cells to terrain types).
- [ ] Make normal floor the default, so existing mazes continue to work without storing every ordinary cell.
- [ ] Define the terrain types, movement costs, and display colors in one clear location.
- [ ] Ensure a cell cannot be both a wall and weighted terrain.
- [ ] Ensure start and goal placement removes or overrides conflicting wall/terrain state in a consistent way.
- [ ] Keep terrain data separate from the algorithm and drawing code where practical.

**Done when:** terrain types and costs can be represented correctly without breaking the current maze.

## Phase 2 — Add terrain editing

- [ ] Add a simple terrain-selection mode alongside the existing wall, start, and goal modes.
- [ ] Let the user select a terrain type and paint it onto traversable cells.
- [ ] Provide a way to return a cell to normal floor.
- [ ] Prevent terrain from being painted onto walls, or define one consistent conversion behavior.
- [ ] Reset the current search whenever the maze or terrain changes.
- [ ] Update the legend and on-screen controls so the user can tell which mode and terrain are selected.

**Done when:** users can paint, change, and erase terrain, and the visual state matches the stored data.

## Phase 3 — Implement Dijkstra separately

- [ ] Create a separate algorithm module, such as `algorithms/dijkstra.py`.
- [ ] Learn and use a priority queue to process the currently cheapest known cell first.
- [ ] Track the cheapest known cost to reach each cell.
- [ ] Track predecessors so the final route can be reconstructed.
- [ ] Ignore walls and reject out-of-bounds neighbors.
- [ ] Animate explored cells using the same general interface pattern as BFS where practical.
- [ ] Return a clear result for both a found route and an unreachable goal.
- [ ] Keep the algorithm independent of Pygame drawing.

**Done when:** Dijkstra finds a minimum-cost route on hand-made examples, including cases where the cheapest route has more steps than the shortest route.

## Phase 4 — Connect the algorithm to the app

- [ ] Add a simple algorithm choice: BFS or Dijkstra.
- [ ] Keep BFS available for equal-cost comparisons and existing behavior.
- [ ] Pass walls and terrain costs into Dijkstra.
- [ ] Ensure reset, pause/stop, maze editing, and path animation work with both algorithms.
- [ ] Show the selected algorithm and current search status.
- [ ] Handle an unreachable goal without showing a stale path or cost.

**Done when:** both algorithms can run on the same maze without corrupting each other's state.

## Phase 5 — Show meaningful results

- [ ] Display the number of explored cells.
- [ ] Display the number of moves in the final route.
- [ ] Display the total terrain cost of the final route.
- [ ] Make the difference between route length and route cost clear.
- [ ] Use consistent colors for terrain, walls, explored cells, the final path, start, and goal.
- [ ] Make sure start and goal remain visible even when a search or path passes through them.

**Done when:** a user can see not only which route was found, but why its total cost matters.

## Phase 6 — Test before adding more features

- [ ] A clear straight route through normal floor.
- [ ] A high-cost terrain strip where a longer route around it is cheaper.
- [ ] A case where the direct route is also the cheapest route.
- [ ] A case where the cheapest route has more moves than the shortest route.
- [ ] A route containing several different terrain types.
- [ ] An unreachable goal.
- [ ] Start next to goal.
- [ ] Start and goal cannot be overwritten by terrain painting in an inconsistent way.
- [ ] Editing terrain after a successful search clears the previous result.
- [ ] Generating a new maze clears or handles old terrain consistently.
- [ ] Reset and stop behavior work while Dijkstra is exploring and while the path is animating.
- [ ] On an all-normal grid, Dijkstra's route cost equals its number of moves (with the start excluded and each entered cell costing 1).
- [ ] On an all-normal grid, Dijkstra finds the same minimum route length as BFS, although the exact route may differ.

**Done when:** all cases behave correctly and no old path, cost, or animation leaks into a new search.

## Later ideas — not part of the first weighted-terrain milestone

- [ ] Add A* that accounts for terrain costs.
- [ ] Compare BFS and Dijkstra on equal-cost grids.
- [ ] Compare Dijkstra and A* on weighted grids.
- [ ] Add a few maze/terrain presets for repeatable demonstrations.
- [ ] Improve the visual design after the feature is stable.

## Completion checklist

Weighted terrain is complete when:

- [ ] Users can paint and erase different terrain types.
- [ ] Terrain costs are visible and documented.
- [ ] Dijkstra finds a minimum-total-cost route.
- [ ] The app animates the search and final route reliably.
- [ ] Route length and total cost are reported separately.
- [ ] The tests above pass.
- [ ] The README explains how to use weighted terrain and what Dijkstra optimizes.

**Guiding rule:** finish one phase, run the app, test it, and commit the working change before moving on. A reliable small step is better than a large rewrite.
