import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Ball")
x, y = 200, 200     
radius = 25          
speed = 20
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= 400:
        x += speed
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= 400:
        y += speed
    screen.fill((255, 255, 255))                
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius) 
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
