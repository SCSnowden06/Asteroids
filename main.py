import pygame 
from constants import *
from player import *


def main(): 
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     # System initializations
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()                                  # Group initializations
    drawable = pygame.sprite.Group()
    Player.containers = (drawable, updateable)

    jit = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))                   # Player initializations

    while True:                                                 
        for event in pygame.event.get():                        #lets the exit button actually work
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))                                    #here and above are initializing game,   

        updateable.update(dt)                                   #game loop starts here
        for sprite in drawable:
            sprite.draw(screen)
         
        dt = clock.tick(60) / 1000 
        pygame.display.flip()                                   # update screen
        

    
if __name__ == "__main__":                                      # Run
    main()