import pygame
import os
WITHD , HEIGHT = 900 , 500
WIN = pygame.display.set_mode((WITHD , HEIGHT))
icon=pygame.display.set_caption('First game#')
WHITE = (255 , 255 , 255)
FPS = 60

def draw_color():
     WIN.fill(WHITE)
     pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_color()
        

    pygame.quit()

if __name__ == "__main__":
    main()
