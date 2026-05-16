import pygame
import random

# Initialize Pygame, the mixer for audio, and the font module
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Setup Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Box Collector Game")
clock = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- MEDIA & FONTS ---

# 1. Load Background Image
bg_image = pygame.image.load("background.png").convert()

# 2. Load and Play Background Music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)  # Loops continuously
pygame.mixer.music.set_volume(0.3)

# 3. Load Collision Sound Effect
hit_sound = pygame.mixer.Sound("hit.wav")
hit_sound.set_volume(0.5)

# 4. Set Up Font
font = pygame.font.Font(None, 36)

# --- GAME OBJECTS ---

class Box(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create Player
player = Box(BLUE, 400, 300)
all_sprites.add(player)

# Create Enemies
for _ in range(7):
    enemy = Box(RED, random.randint(0, 770), random.randint(0, 570))
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
running = True

# --- GAME LOOP ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.rect.x -= 5
    if keys[pygame.K_RIGHT]: player.rect.x += 5
    if keys[pygame.K_UP]:    player.rect.y -= 5
    if keys[pygame.K_DOWN]:  player.rect.y += 5

    # 2. Screen Boundaries Check (Clamp player within the 800x600 screen)
    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > 800:
        player.rect.right = 800
    if player.rect.top < 0:
        player.rect.top = 0
    if player.rect.bottom > 600:
        player.rect.bottom = 600

    # 3. Collision Logic
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        hit_sound.play()  # Play sound effect

    # 4. Drawing & Rendering
    # Draw background image
    screen.blit(bg_image, (0, 0))
    
    # Draw sprites on top of background
    all_sprites.draw(screen)
    
    # Render and draw score text on top of everything
    score_surface = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (15, 15))
    
    pygame.display.flip()
    clock.tick(60)

# Stop the music and quit
pygame.mixer.music.stop()
pygame.quit()