import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    # set the window resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    delta_time = pygame.time.Clock()
    dt = 0
    # Sprite groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    # Adds to the containers for the PLayer class to updatable and drawable groups
    Player.containers = (updatable, drawable)

    # draw the player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # print(f"This is drawable { drawable }")
    # print(f"This is updatable: {updatable}")

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    # drawable = pygame.sprite.Group()  # all objects that can be drawn

    while True:
        for event in pygame.event.get():
            # Quit window
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color="black")
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over!")
                return

        pygame.display.flip()

        delta_time.tick(60)
        dt = delta_time.tick(60) / 1000


if __name__ == "__main__":
    main()
