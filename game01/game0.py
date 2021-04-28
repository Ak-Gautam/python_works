import pygame
import sys
from random import randint

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 40, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    bg = [0, 0, 0]
    size = [400, 400]
    screen = pygame.display.set_mode(size)
    player = Sprite([40, 50])
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5

    wall = Sprite([randint(0, 400), randint(1, 390)])

    wall_group = pygame.sprite.Group()
    wall_group.add(wall)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()
        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx*[-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy*[-1, 1][i]

        screen.fill(bg)

        hit = pygame.sprite.spritecollide(player, wall_group, True)

        if hit:
            player.image.fill((255, 255, 255))

        player_group.draw(screen)
        wall_group.draw(screen)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    sys.exit

if __name__ == '__main__':
    main()