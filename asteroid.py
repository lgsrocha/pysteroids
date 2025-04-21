import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.x = x
        # self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)

        positive = self.velocity.rotate(random_angle)
        negative = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        positive_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        positive_asteroid.velocity = positive * 1.2
        negative_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        negative_asteroid.velocity = negative * 1.2