
import pygame
from collections import deque

pygame.init()

# settings and stuffs iduno
w = 800
h = 680
cell_s = 40
grid_top = 80

ROWS = (h - grid_top) // cell_s
COLS = w // cell_s

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RouteLab - Pathfinding Visualizer")
clock = pygame.time.Clock()

# fonts
title_font = pygame.font.SysFont(None, 32)
font = pygame.font.SysFont(None, 24)

# grid state
walls = set()
starthere_ = (1, 1)
goal_ = (ROWS - 2, COLS - 2)

mode = "wall"
path = []
visited = set()

# BFS animation thingy
search_steps = None
search_running = False
step_delay_ms = 30
last_step_time = 0


def find_path(start, goal, walls):
    queue = deque([start])
    came_from = {start: None}
    visited = set()

    while queue:
        current = queue.popleft()
        visited.add(current)

        # Reveal the next explored cell >:3
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
            (row, col + 1),
        ]

        for neighbor in neighbors:
            r, c = neighbor

            if not (0 <= r < ROWS):
                continue
            if not (0 <= c < COLS):
                continue
            if neighbor in walls or neighbor in came_from:
                continue

            came_from[neighbor] = current
            queue.append(neighbor)

    # No path found >:C
    yield None, visited, []


def reset_search():
    global path, visited, search_steps, search_running

    path = []
    visited = set()
    search_steps = None
    search_running = False


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mode = "wall"

            elif event.key == pygame.K_s:
                mode = "start"

            elif event.key == pygame.K_g:
                mode = "goal"

            elif event.key == pygame.K_RETURN:
                if not search_running:
                    reset_search()
                    search_steps = find_path(
                        starthere_, goal_, walls
                    )
                    search_running = True
                    last_step_time = pygame.time.get_ticks()

        # mouse controls
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            mouse_x, mouse_y = event.pos

            # ignore clicks in the control panel
            if mouse_y < grid_top:
                continue

            col = mouse_x // cell_s
            row = (mouse_y - grid_top) // cell_s
            cell = (row, col)

            # ignore clicks outside the grid
            if not (0 <= row < ROWS and 0 <= col < COLS):
                continue

            if mode == "wall":
                if cell != starthere_ and cell != goal_:
                    reset_search()

                    if cell in walls:
                        walls.remove(cell)
                    else:
                        walls.add(cell)

            elif mode == "start":
                if cell != goal_ and cell not in walls:
                    reset_search()
                    starthere_ = cell

            elif mode == "goal":
                if cell != starthere_ and cell not in walls:
                    reset_search()
                    goal_ = cell

    # move BFS one step at a time
    if search_running:
        now = pygame.time.get_ticks()

        if now - last_step_time >= step_delay_ms:
            last_step_time = now

            try:
                current, visited, new_path = next(search_steps)

                if current is None:
                    path = new_path
                    search_running = False

                    print("Path length:", len(path))
                    print("Cells explored:", len(visited))

                    if path:
                        print("Path found! YIPEEE")
                    else:
                        print("Uh oh.. No path found!")

            except StopIteration:
                search_running = False

    # renderrr background
    screen.fill((25, 28, 36))

    # render title
    title = title_font.render(
        "RouteLab - Pathfinding Visualizer!",
        True,
        (255, 255, 255),
    )
    screen.blit(title, (10, 8))

    # render keyboard controls
    controls = [
        "W: Wall mode!",
        "S: Move start blokc",
        "G: Move goal blok",
        "ENTER: Run the path finder",
    ]

    for i, control in enumerate(controls):
        text = font.render(
            control,
            True,
            (200, 205, 220),
        )

        x = 10 + (i % 2) * 200
        y = 42 + (i // 2) * 22

        screen.blit(text, (x, y))

    # all the modes
    mode_names = {
        "wall": "WALL",
        "start": "START",
        "goal": "GOAL",
    }

    mode_text = font.render(
        f"Current mode: {mode_names[mode]}",
        True,
        (255, 220, 120),
    )
    screen.blit(mode_text, (420, 42))

    # render grid cells
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * cell_s,
                grid_top + row * cell_s,
                cell_s,
                cell_s,
            )

            cell = (row, col)

            if cell in walls:
                pygame.draw.rect(
                    screen, (80, 85, 100), rect
                )

            if cell in visited:
                pygame.draw.rect(
                    screen, (100, 120, 180), rect
                )

            if cell in path:
                pygame.draw.rect(
                    screen, (255, 255, 255), rect
                )

            if cell == starthere_:
                pygame.draw.rect(
                    screen, (60, 140, 255), rect
                )

            if cell == goal_:
                pygame.draw.rect(
                    screen, (60, 255, 140), rect
                )

            pygame.draw.rect(
                screen, (65, 72, 85), rect, 1
            )

    # render legend below the grid
    legend_y = grid_top + ROWS * cell_s + 4

    legend = [
        ("Start", (60, 140, 255)),
        ("Goal", (60, 255, 140)),
        ("Explored", (100, 120, 180)),
        ("Path", (255, 255, 255)),
        ("Wall", (80, 85, 100)),
    ]

    for i, (label, color) in enumerate(legend):
        x = 10 + i * 145

        pygame.draw.rect(
            screen, color,
            pygame.Rect(x, legend_y, 14, 14),
        )

        label_text = font.render(
            label, True, (220, 225, 235)
        )
        screen.blit(label_text, (x + 20, legend_y - 3))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
