import pygame
from random import uniform
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        x, y = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        direction = uniform(20, 50)
        print(direction)
        pos_asteroid = Asteroid(x, y, new_radius)
        neg_asteroid = Asteroid(x, y, new_radius)
        pos_asteroid.velocity = self.velocity.rotate(direction)
        neg_asteroid.velocity = self.velocity.rotate(-direction)
        pos_asteroid.velocity *= 1.2
        neg_asteroid.velocity *= 1.2
