import pygame
import random

# 1. Initialize Pygame and set up the window
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites Demo")

# 2. Define the Sprite class
class SquareSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, can_change=False):
        super().__init__()
        # Create a 50x50 surface for the sprite
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.can_change = can_change
        self.timer = 0

    def update(self):
        # Only change color if the flag is set
        if self.can_change:
            self.timer += 1
            if self.timer % 60 == 0:  # Change roughly every second at 60 FPS
                # Generate a random RGB color tuple
                new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.image.fill(new_color)

# 3. Create sprite instances and a group
# Static blue sprite on the left, changing red sprite on the right
static_sprite = SquareSprite((50, 150, 255), 200, 200)
changing_sprite = SquareSprite((255, 50, 50), 400, 200, can_change=True)

all_sprites = pygame.sprite.Group()
all_sprites.add(static_sprite)
all_sprites.add(changing_sprite)

# 4. Main Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic: update all sprites in the group
    all_sprites.update()

    # Drawing: fill background, draw sprites, and flip display
    screen.fill((255, 255, 255)) # White background
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60) # Limit to 60 frames per second

pygame.quit()