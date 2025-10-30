import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

bg = pygame.image.load(r"C:\Users\Dias\Downloads\mickey.png")
bg = pygame.transform.scale(bg, (400, 400))
center = (200, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute

    second_angle = 6 * sec
    minute_angle = 6 * minute

    screen.blit(bg, (0, 0))

    sec_x = center[0] + 100 * math.sin(math.radians(second_angle))
    sec_y = center[1] - 100 * math.cos(math.radians(second_angle))
    pygame.draw.line(screen, (255, 0, 0), center, (sec_x, sec_y), 2)

    min_x = center[0] + 80 * math.sin(math.radians(minute_angle))
    min_y = center[1] - 80 * math.cos(math.radians(minute_angle))
    pygame.draw.line(screen, (0, 0, 0), center, (min_x, min_y), 4)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
