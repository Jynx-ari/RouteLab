
import pygame
from collections import deque

pygame.init()

w = 800
h = 600
cell_s = 40

ROWS = h // cell_s
COLS = w // cell_s

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RouteLab: Animated BFS")
clock = pygame.time.Clock()

# Grid setup
walls = set()
starthere_ = (1, 1)
goal_ = (ROWS - 2, COLS - 2)

mode = "wall"
path = []
visited = set()

# Animation setup
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

        # Reveal one explored cell
        yield current, visited, []

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = came_from[current]

            path.reverse()

            # Search finished successfully
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

    # No route to the goal
    yield None, visited, []


framerate = 60
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
                    visited = set()
                    path = []

                    search_steps = find_path(
                        starthere_, goal_, walls
                    )
                    search_running = True
                    last_step_time = pygame.time.get_ticks()

        # Mouse controls
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            mouse_x, mouse_y = event.pos

            col = mouse_x // cell_s
            row = mouse_y // cell_s
            cell = (row, col)

            # Ignore clicks outside the grid
            if not (0 <= row < ROWS and 0 <= col < COLS):
                continue

            # Stop the previous search when editing
            path = []
            visited = set()
            search_steps = None
            search_running = False

            if mode == "wall":
                if cell != starthere_ and cell != goal_:
                    if cell in walls:
                        walls.remove(cell)
                    else:
                        walls.add(cell)

            elif mode == "start":
                if cell != goal_ and cell not in walls:
                    starthere_ = cell

            elif mode == "goal":
                if cell != starthere_ and cell not in walls:
                    goal_ = cell

    # Advance BFS gradually
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
                        print("Path found!")
                    else:
                        print("No path found!")

            except StopIteration:
                search_running = False

    # Draw the grid
    screen.fill((25, 28, 36))

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * cell_s,
                row * cell_s,
                cell_s,
                cell_s,
            )

            cell = (row, col)

            if cell in walls:
                pygame.draw.rect(screen, (80, 85, 100), rect)

            if cell in visited:
                pygame.draw.rect(screen, (100, 120, 180), rect)

            if cell in path:
                pygame.draw.rect(screen, (255, 255, 255), rect)

            if cell == starthere_:
                pygame.draw.rect(screen, (60, 140, 255), rect)

            if cell == goal_:
                pygame.draw.rect(screen, (60, 255, 140), rect)

            pygame.draw.rect(screen, (65, 72, 85), rect, 1)

    pygame.display.flip()
    clock.tick(framerate)

pygame.quit()
