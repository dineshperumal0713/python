import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my firt pygame window")

center_rect = pygame.Rect(0, 0, 300, 300)
center_rect.center = (250, 250)

font = pygame.font.SysFont("Arial", 25)
text_surface = font.render("my firrst pygame window", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), center_rect)
    screen.blit(text_surface, (130, 235))

    pygame.display.flip()

pygame.quit()
