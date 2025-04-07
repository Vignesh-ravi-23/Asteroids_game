import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
        
        # Ensure subclass implements triangle() before calling
        if hasattr(self, "triangle"):
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_position()
 
    def collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)

    def wrap_position(self):
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

