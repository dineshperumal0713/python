

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("my first pygame window")


text_surface = font.render("my first pygame window", True, (255, 255, 255))
font = pygame.font.SysFont("None", 35)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((58, 58, 58))

    screen.blit(text_surface, (130, 235))

    pygame.display.flip()

pygame.quit()