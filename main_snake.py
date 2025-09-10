import pygame
import  sys
import random



def generate_ball():
    global ball_x
    global ball_y
    global ball_radius


    ball_x = random.randint(0, WIDTH)
    ball_y = random.randint(0, HEIGHT)

    red_channel = random.randint(0, 255)
    green_channel = random.randint(0, 255)
    blue_channel = random.randint(0, 255)

    pygame.draw.circle(
        main_screen,
        (red_channel, green_channel, blue_channel),
        (ball_x, ball_y),
        ball_radius
    )
    pygame.display.update()



WIDTH, HEIGHT = 1000, 1000      # размеры окна

pygame.init()

main_screen = pygame.display.set_mode((WIDTH, HEIGHT))


ball_x, ball_y, ball_radius = 0, 0, 20


while True:
    # main_screen.fill((0, 0, 0))
    generate_ball()
    for event in pygame.event.get():
        print(event, event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


