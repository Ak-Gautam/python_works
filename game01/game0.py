import pygame

pygame.init()
screen = pygame.display.set_mode((600, 480))


done = False

font = pygame.font.SysFont("Times new Roman", 62)

text = font.render("Hello, Pygame", True, (150, 50, 50))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    screen.fill((255, 255, 255))

    screen.blit(text, (300 - text.get_width()//2, 240-text.get_height()//2))

    pygame.display.flip()