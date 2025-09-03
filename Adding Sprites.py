import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites Game")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
fixed_sprite = pygame.Rect(200, 150, 100, 100)   
movable_sprite = pygame.Rect(300, 300, 80, 80)
speed = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        movable_sprite.x -= speed
    if keys[pygame.K_RIGHT]:
        movable_sprite.x += speed
    if keys[pygame.K_UP]:
        movable_sprite.y -= speed
    if keys[pygame.K_DOWN]:
        movable_sprite.y += speed
    window.fill(BLACK)
    pygame.draw.rect(window, RED, fixed_sprite)      
    pygame.draw.rect(window, BLUE, movable_sprite)
    pygame.display.flip()
    clock.tick(60)
