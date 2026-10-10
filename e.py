
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40

ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RouteLab")

clock = pygame.time.Clock()

# The maze
walls = set()

# Start and destination positions: (row, column)
start = (1, 1)
goal = (ROWS - 2, COLS - 2)

# What should a mouse click do?
mode = "wall"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change the mouse-click mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mode = "wall"
            elif event.key == pygame.K_s:
                mode = "start"
            elif event.key == pygame.K_g:
                mode = "goal"

        # Handle left mouse clicks
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            mouse_x, mouse_y = event.pos

            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE

            cell = (row, col)

            if mode == "wall":
                if cell != start and cell != goal:
                    if cell in walls:
                        walls.remove(cell)
                    else:
                        walls.add(cell)

            elif mode == "start":
                if cell not in walls and cell != goal:
                    start = cell

            elif mode == "goal":
                if cell not in walls and cell != start:
                    goal = cell

    # Draw the background
    screen.fill((25, 28, 36))

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )

            cell = (row, col)

            if cell in walls:
                pygame.draw.rect(screen, (80, 85, 100), rect)

            if cell == start:
                pygame.draw.rect(screen, (60, 140, 255), rect)

            if cell == goal:
                pygame.draw.rect(screen, (60, 200, 120), rect)

            pygame.draw.rect(screen, (65, 72, 85), rect, 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
