import pygame 
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *


def main(): 
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     # System initializations
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()                                  # Group initializations
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawable, updateable)
    Asteroid.containers = (drawable, updateable, asteroids)
    AsteroidField.containers = (updateable)

    jit = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))                   # Player initializations
    asteroid_field = AsteroidField()

    while True:                                                 
        for event in pygame.event.get():                        #lets the exit button actually work
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))                                    #here and above are initializing game,   


        updateable.update(dt)                                   #game loop starts here
        asteroids.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if(CircleShape.is_colliding(asteroid, jit)):
                print("GAME OVER")
                sys.exit(0)

         
        dt = clock.tick(60) / 1000 
        pygame.display.flip()                                   # update screen
        

    
if __name__ == "__main__":                                      # Run
    main()