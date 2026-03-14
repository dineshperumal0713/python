import pygame
pygame.init()
screen_size = pygame.display.set_mode((900,800))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.flip()
    



