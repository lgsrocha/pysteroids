from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # self.radius = PLAYER_RADIUS
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color = "white"
        pygame.draw.polygon(screen, color, self.triangle(), 2)

    def rotate(self, dt):
        print(f"Player Rotation before: {self.rotation}")
        self.rotation += (PLAYER_TURN_SPEED * dt)
        print(f"Player Rotation after: {self.rotation}")


    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            negative_dt = dt * -1
            self.rotate(negative_dt)
                
        if keys[pygame.K_d]:
            positive_dt = dt * 1
            self.rotate(positive_dt)
                