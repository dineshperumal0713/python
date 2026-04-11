import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
player_rect = pygame.Rect(100, 100, 50, 50)  
static_rect = pygame.Rect(300, 200, 50, 50)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)    
    screen.fill((255, 255, 255))               
    pygame.draw.rect(screen, (0, 0, 255), player_rect)  
    pygame.draw.rect(screen, (200, 0, 0), static_rect)  
    
  
    pygame.display.flip()
 

pygame.quit()