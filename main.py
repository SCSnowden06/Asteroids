import pygame as pg
from constants import *
from player import *


def main(): 
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill((0,0,0))
        jit = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
        jit.draw(screen)
        dt = clock.tick(60) / 1000  
        pg.display.flip()
        

    



if __name__ == "__main__":
    main()