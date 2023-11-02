import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Programming fundamentals")

x_coordinate = 500
y_coordinate = 300

running = True
while running:
    pygame.time.Clock().tick(60)
    print(x_coordinate, y_coordinate)
    for event in pygame.event.get():
        pass
    if event.type == pygame.QUIT:
        break

    pygame.draw.rect(
        screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        (x_coordinate, y_coordinate, 50, 50)
    )

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_coordinate -= 50
    if button[pygame.K_RIGHT]:
        x_coordinate += 50
    if button[pygame.K_UP]:
        y_coordinate -= 50
    if button[pygame.K_DOWN]:
        y_coordinate += 50

    if x_coordinate <= 0:
        x_coordinate = 0
    elif x_coordinate >= 750:
        x_coordinate = 750
    if y_coordinate <= 0:
        y_coordinate = 0
    elif y_coordinate >= 550:
        y_coordinate = 550


    pygame.display.flip()