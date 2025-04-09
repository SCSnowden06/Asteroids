from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_ROTATE_SPEED, PLAYER_MOVE_SPEED
import pygame
from shot import *

class Player(CircleShape):
    

    def __init__(self, x, y, shots_group):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.shots_group = shots_group
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        return pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += (dt * PLAYER_ROTATE_SPEED)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-0.5*dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        self.shot_timer -= dt
        

    def move(self, dt): 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt    
        self.x = self.position.x
        self.y = self.position.y

    def shoot(self, dt):
        if self.shot_timer <= 0:
            shot = Shot(self.x, self.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED
            self.position += (self.velocity * dt)
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            self.shots_group.add(shot)
        else:
            print(f"Shots on cooldown! Try again in {self.shot_timer} seconds")
        
