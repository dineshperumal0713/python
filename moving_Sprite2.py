import pygame

 
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Sprite Demo")

class BouncingSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed_x, speed_y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

      
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        
        # Reverse speed if hitting vertical walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1


static_sprite = pygame.sprite.Sprite()
static_sprite.image = pygame.Surface((50, 50))
static_sprite.image.fill((50, 150, 255))
static_sprite.rect = static_sprite.image.get_rect(center=(300, 200))

bouncing_sprite = BouncingSprite((255, 100, 100), 100, 100, 5, 4)


all_sprites = pygame.sprite.Group(static_sprite, bouncing_sprite)

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