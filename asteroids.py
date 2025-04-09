from circleshape import CircleShape
from constants import *
import pygame
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self. x = x
        self.y = y
        self.radius = radius
        
    def draw(self, screen):
        return pygame.draw.circle(screen , (122,128, 144) , self.position, self.radius,  2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.x = self.position.x
        self.y = self.position.y
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid = Asteroid(self.x, self.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid.velocity.rotate(random.uniform(20,50)) 


        