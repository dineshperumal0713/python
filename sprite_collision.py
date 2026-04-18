import pygame
import random

screen_width , screen_hieght = 640, 480
movement_speed = 5
font_size = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load("background_image.jpg"), (screen_width, screen_hieght))
font = pygame.font.SysFont("Times New Roman", font_size)
class sprite(pygame.sprite.Sprite):
     def __init__(self, color, hieght, width):
            super().__init__()
            self.image = pygame.Surface([width,hieght])
            self.image.fill(pygame.Color("blue"))
            pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,hieght),0)
            self.rect = self.image.get_rect()
     def move(self, x_change, y_change):
             self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width),0)
             self.rect.y = max(min(self.rect.y + y_change, screen_hieght - self.rect.hieght),0)
screen = pygame.display.set_mode((screen_width, screen_hieght))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()
sprite1 = sprite(pygame.Color("yellow"),20,30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, screen_width - sprite1.rect.width), random.randint(0, screen_hieght - sprite1.rect.hieght)
all_sprites.add(sprite1)
sprite2 = sprite(pygame.Color("red"),20,30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, screen_width - sprite2.rect.width),random.randint(0, screen_hieght - sprite2.rect.hieght)
all_sprites.add(sprite2)
running,won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):

          running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)

    if won:
       win_text = font.render("You win!", True, pygame.Color("yellow"))
       screen.blit(win_text,((screen_width - win_text.get_width())//2, (screen_hieght - win_text.get_height())// 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
