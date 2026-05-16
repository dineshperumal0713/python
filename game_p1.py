import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


WHITE, BLUE, RED = (255, 255, 255), (0, 0, 255), (255, 0, 0)


class Box(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()


player = Box(BLUE, 400, 300)
all_sprites.add(player)


for _ in range(7):
    enemy = Box(RED, random.randint(0, 770), random.randint(0, 570))
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.rect.x -= 5
    if keys[pygame.K_RIGHT]: player.rect.x += 5
    if keys[pygame.K_UP]:    player.rect.y -= 5
    if keys[pygame.K_DOWN]:  player.rect.y += 5

    
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        print(f"Current Score: {score}")

   
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()