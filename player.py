import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

PLAYER_RADIUS = 20

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = ((self.position + forward * self.radius).x, (self.position + forward * self.radius).y)
        b = ((self.position - forward * self.radius - right).x, (self.position - forward * self.radius - right).y)
        c = ((self.position - forward * self.radius + right).x, (self.position - forward * self.radius + right).y)
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move_direction(dt)
        if keys[pygame.K_s]:
            self.move_direction(-dt)

        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def move_direction(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer <= 0:
                
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            return Shot(self.position.copy(), velocity)
        return None
    
