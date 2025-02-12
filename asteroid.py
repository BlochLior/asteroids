import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        vector_2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position, new_radius)
        asteroid_2 = Asteroid(self.position, new_radius)
        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2.velocity = vector_2 * 1.2