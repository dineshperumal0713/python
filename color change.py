import pygame
import random


pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites Demo")


class SquareSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, can_change=False):
        super().__init__()
        
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.can_change = can_change
        self.timer = 0

    def update(self):
     
        if self.can_change:
            self.timer += 1
            if self.timer % 60 == 0:  
                new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.image.fill(new_color)


static_sprite = SquareSprite((50, 150, 255), 200, 200)
changing_sprite = SquareSprite((255, 50, 50), 400, 200, can_change=True)

all_sprites = pygame.sprite.Group()
all_sprites.add(static_sprite)
all_sprites.add(changing_sprite)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    all_sprites.update()

    
    screen.fill((255, 255, 255)) 
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60) 

pygame.quit()