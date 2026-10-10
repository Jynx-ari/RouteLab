import pygame

pygame.init()

w = 800
h = 600
cell_s = 40

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RouteLab: Grid Example")
clock = pygame.time.Clock()
framerate=60
running=True

while running:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
    
    screen.fill((25, 28, 36))

    for x in range(0, w, cell_s):
        for y in range(0, h, cell_s):
            rect = pygame.Rect(x, y,  cell_s, cell_s)
            pygame.draw.rect(screen, (65, 72, 85), rect, 1)

    pygame.display.flip()
    
    clock.tick(framerate)

pygame.quit()

    