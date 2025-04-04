import pygame 
from constants import *
from player import *


def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    jit = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    while True:                                                 
        for event in pygame.event.get():                        #lets the exit button actually work
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))                                    #here and above are initializing game,   

        jit.update(dt)                                          #game loop starts here
        jit.draw(screen)
        dt = clock.tick(60) / 1000  

        pygame.display.flip()                                   #update screen
        

    



if __name__ == "__main__":
    main()