import pygame
from constants import *


def main():
    pygame.init()
    # print("Starting asteroid!")
    # print(SCREEN_WIDTH)
    # print(SCREEN_HEIGHT)
    delta_time = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.Surface.fill(screen, color="black")
        # pygame.display.flip()

        # delta_time.tick(60)
        # dt = delta_time.tick(60) / 1000

if __name__ == "__main__":
    main()
