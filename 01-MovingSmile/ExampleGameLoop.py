import pygame
import sys

pygame.init()

pygame.display.set_caption("Dave Fisher")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(pygame.Color("Gray"))

    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Cyan"), (50, 150), 25)
    pygame.draw.circle(screen, (128, 0, 0), (screen.get_width() / 2, screen.get_height() / 2), 100)
    pygame.draw.circle(screen, (255, 255, 0), (0, screen.get_height()), 10)

    pygame.display.update()
