import pygame
from constants import *

def main():
    pygame.init
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, BLACK)
        pygame.display.flip() 


    print("Starting Asteroids!")
    print('Screen width: 1280')
    print('Screen height: 720')

if __name__ == '__main__':
    main()