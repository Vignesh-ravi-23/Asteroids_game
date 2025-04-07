import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius, velocity):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self)

        self.velocity = velocity
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (150, 150, 150), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

        for group in getattr(self.__class__, 'containers', []):
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_position()
        self.rect.center = self.position

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # small asteroid, just disappear

        # calculate new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # generate random angle to spread
        random_angle = random.uniform(20, 50)

        # two new velocity directions
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        # create two smaller asteroids
        Asteroid(self.position.x, self.position.y, new_radius, vel1)
        Asteroid(self.position.x, self.position.y, new_radius, vel2)
