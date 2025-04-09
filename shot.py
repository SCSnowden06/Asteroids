from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self. x = x
        self.y = y
        self. radius = SHOT_RADIUS

    def draw(self, screen):
        return pygame.draw.circle(screen , (255 , 0 , 0) , self.position, self.radius,  2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)