import pygame
import random

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
GRASS = (50, 160, 60)
DIRT = (139, 69, 19)
LINK_GREEN = (34, 139, 34)
LINK_SKIN = (255, 220, 180)
SWORD_STEEL = (192, 192, 192)
ENEMY_VIOLET = (120, 0, 150)

# Player & Game States
player = pygame.Rect(400, 300, 40, 40)
player_speed = 5
sword_timer = 0
hit_flash = 0
shake_amount = 0

# Enemy Setup (Multiple Enemies)
enemies = [pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 40, 40) for _ in range(3)]

def draw_player(surface, rect):
    # Body/Tunic
    pygame.draw.rect(surface, LINK_GREEN, rect)
    # Head
    head = pygame.Rect(rect.x + 10, rect.y - 10, 20, 20)
    pygame.draw.rect(surface, LINK_SKIN, head)
    # Hat
    pygame.draw.polygon(surface, LINK_GREEN, [(head.x, head.y), (head.right, head.y), (head.centerx, head.y - 15)])

def draw_enemy(surface, rect):
    pygame.draw.rect(surface, ENEMY_VIOLET, rect, border_radius=10)
    # Eyes
    pygame.draw.circle(surface, (255, 255, 255), (rect.x + 10, rect.y + 15), 4)
    pygame.draw.circle(surface, (255, 255, 255), (rect.right - 10, rect.y + 15), 4)

running = True
while running:
    # Camera Shake logic
    offset_x = random.randint(-shake_amount, shake_amount)
    offset_y = random.randint(-shake_amount, shake_amount)
    if shake_amount > 0: shake_amount -= 1

    # Drawing background
    screen.fill(GRASS)
    for x in range(0, WIDTH, 100): # Simple grid "tiles"
        for y in range(0, HEIGHT, 100):
            pygame.draw.rect(screen, (45, 150, 55), (x + offset_x, y + offset_y, 98, 98), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sword_timer = 15

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player.y -= player_speed
    if keys[pygame.K_s]: player.y += player_speed
    if keys[pygame.K_a]: player.x -= player_speed
    if keys[pygame.K_d]: player.x += player_speed

    # Combat Logic
    if sword_timer > 0:
        sword_rect = pygame.Rect(player.right + offset_x, player.centery - 5 + offset_y, 40, 15)
        pygame.draw.rect(screen, SWORD_STEEL, sword_rect)
        sword_timer -= 1
        for e in enemies[:]:
            if sword_rect.colliderect(e):
                enemies.remove(e)
                shake_amount = 10
                hit_flash = 5

    # Draw Entities
    draw_player(screen, player.move(offset_x, offset_y))
    
    for e in enemies:
        draw_enemy(screen, e.move(offset_x, offset_y))
        # Simple Chase AI
        if e.x < player.x: e.x += 1
        elif e.x > player.x: e.x -= 1
        if e.y < player.y: e.y += 1
        elif e.y > player.y: e.y -= 1

    # Flash effect when hitting
    if hit_flash > 0:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((255, 255, 255))
        overlay.set_alpha(100)
        screen.blit(overlay, (0,0))
        hit_flash -= 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()