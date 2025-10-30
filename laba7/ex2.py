import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

playlist = ["1.mp3", "2.mp3", "3.mp3"]
index = 0
pygame.mixer.music.load(playlist[index])

font = pygame.font.SysFont(None, 36)
state = "Stopped"

running = True
while running:
    screen.fill((30, 30, 30))
    text1 = font.render(f"Now playing: {playlist[index]}", True, (255, 255, 255))
    text2 = font.render(f"State: {state}", True, (200, 200, 200))
    screen.blit(text1, (20, 70))
    screen.blit(text2, (20, 110))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
                state = "Playing"
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                state = "Stopped"
            elif event.key == pygame.K_n:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                state = "Playing"
            elif event.key == pygame.K_b:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                state = "Playing"

pygame.quit()
