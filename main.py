import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    # print("Starting asteroid!")
    # print(SCREEN_WIDTH)
    # print(SCREEN_HEIGHT)
    delta_time = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        player.draw(screen) # draw here, anywhere else the screen renders the background above the player sprite
        pygame.display.flip()


        delta_time.tick(60)
        dt = delta_time.tick(60) / 1000



if __name__ == "__main__":
    main()
