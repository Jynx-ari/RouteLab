import pygame

pygame.init()

w = 800
h = 600
cell_s = 40

ROWS = h // cell_s
COLS = w // cell_s

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RouteLab: Grid Example")
clock = pygame.time.Clock()
framerate=60
running=True

walls = set()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            cell_x = x // cell_s
            cell_y = y // cell_s
            cell = (cell_y, cell_x)
            if cell in walls:
                walls.remove(cell)
            else:
                walls.add(cell)
            


    screen.fill((25, 28, 36))

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * cell_s,
                row * cell_s,
                cell_s,
                cell_s
                )
            if (row, col) in walls:
                pygame.draw.rect(screen, (80, 85, 100), rect)
            else:
                pygame.draw.rect(screen, (65, 72, 85), rect, 1)
    
    pygame.display.flip()
    
    clock.tick(framerate)

pygame.quit()

    