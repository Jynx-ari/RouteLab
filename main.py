import pygame
from collections import deque

pygame.init()

w = 800
h = 600
cell_s = 40

ROWS = h // cell_s
COLS = w // cell_s

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("RouteLab: Grid Example")
clock = pygame.time.Clock()


walls = set()
starthere_ = (1,1)
goal_ = (ROWS-2, COLS-2)

mode = "wall"
path = []
def find_path(start, goal, walls):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        #found destination? maybe idk
        if current == goal:
            path = []


            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        row, col = current
        neighbors = [
        (row-1, col), 
        (row+1, col), 
        (row, col-1), 
        (row, col+1)
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
    return [] #brahh no found?

framerate=60
running=True




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mode = "wall"
            elif event.key == pygame.K_s:
                mode = "start" #start!
            elif event.key == pygame.K_g:
                mode = "goal" #goal!
            elif event.key == pygame.K_RETURN:
                path = find_path(starthere_, goal_, walls)
                print(path)


        #Mouse clicks goes here!
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):

            mouse_x, mouse_y = event.pos

            col = mouse_x // cell_s
            row = mouse_y // cell_s

            cell = (row, col)
            path = []
            if mode == "wall":
                if cell != starthere_ and cell != goal_:
                    if cell in walls:
                        walls.remove(cell)
                    else:
                        walls.add(cell)
            elif mode =="start":
                if cell != goal_ and cell not in walls:
                    starthere_ = cell
            elif mode == "goal":
                if cell not in walls and cell != starthere_:
                    goal_ = cell


    screen.fill((25, 28, 36))

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * cell_s,
                row * cell_s,
                cell_s,
                cell_s
                )
            
            cell = (row, col)
            
            if cell in walls:
                pygame.draw.rect(screen, (80, 85, 100), rect)
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

    