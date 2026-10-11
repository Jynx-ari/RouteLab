# RouteLab

**A beginner-friendly pathfinding visualizer built with Python and Pygame.**

RouteLab lets you create a grid maze and watch Breadth-First Search (BFS) explore it one cell at a time to find a shortest path from a start cell to a goal.

## Features

- **Interactive grid** — add and remove walls with mouse clicks.
- **Choose start and goal** — place the start and goal cells wherever you like.
- **Animated BFS** — watch the algorithm explore the grid.
- **Shortest-path display** — see the route BFS finds when the goal is reachable.
- **Visual legend and controls** — keybinds and cell colors are shown in the window.

## Getting started

### Requirements

- Python 3
- Pygame

### Install Pygame

```bash
python -m pip install pygame
```

If your system uses `python3` instead of `python`, run:

```bash
python3 -m pip install pygame
```

### Run RouteLab

Clone the repository and enter its directory:

```bash
git clone https://github.com/Jynx-ari/RouteLab.git
cd RouteLab
```

Run the program:

```bash
python main.py
```

If needed, use `python3 main.py` instead.

## Controls

| Key / action | What it does |
| --- | --- |
| `W` | Switch to wall mode |
| `S` | Switch to start-placement mode |
| `G` | Switch to goal-placement mode |
| `Enter` | Run animated BFS |
| Left-click (wall mode) | Add a wall or remove an existing wall |
| Left-click (start mode) | Move the start cell |
| Left-click (goal mode) | Move the goal cell |

Clicking the control panel above the grid does not change the grid.

## Cell colors

| Color | Meaning |
| --- | --- |
| Blue | Start |
| Green | Goal |
| Gray | Wall |
| Purple-blue | Explored cell |
| White | Shortest path found |

## How it works

RouteLab uses **Breadth-First Search (BFS)**. BFS explores the grid in layers using a first-in, first-out queue. Because each move between neighboring cells has the same cost, BFS finds a shortest path when one exists.

The grid allows movement in four directions: up, down, left, and right. Walls block movement. If the goal cannot be reached, RouteLab finishes without displaying a path.

## Project status

RouteLab is an in-progress learning project. The current version focuses on making BFS visible and understandable; additional algorithms and features may be added as the project develops.

## Why RouteLab?

The goal is not just to show a path, but to help learners see how a pathfinding algorithm explores a space and how obstacles affect its search.

---

Made as a hands-on project to learn Python, Pygame, and pathfinding algorithms.