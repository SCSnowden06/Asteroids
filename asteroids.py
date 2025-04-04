from circleshape import CircleShape
from constants import *
import pygame



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self. x = x
        self.y = y
        self. radius = radius
    
    def draw(self, screen):
        return pygame.draw.circle(screen , (122,128, 144) , self.position, self.radius,  2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)


        