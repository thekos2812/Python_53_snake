import pygame
import  sys


WIDTH, HEIGHT = 1000, 1000      # размеры окна

pygame.init()

main_screen = pygame.display.set_mode((WIDTH, HEIGHT))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


