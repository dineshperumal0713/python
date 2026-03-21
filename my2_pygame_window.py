import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("my first pygame window")

font = pygame.font.SysFont("Arial", 25)
text_surface = font.render("my first pygame window", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((58, 58, 58))

    screen.blit(text_surface, (130, 235))

    pygame.display.flip()

pygame.quit()