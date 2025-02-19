import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, position, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_for_collisions(self, object):
        distance = pygame.math.Vector2.distance_to(self.position, object.position)
        r1 = self.radius
        r2 = object.radius
        return distance <= r1 + r2