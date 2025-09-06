import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()
player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 40)
player_speed = 5
enemies = []
for _ in range(7):
    rect = pygame.Rect(random.randint(20, WIDTH-40),
            random.randint(20, HEIGHT-40),
            30, 30)
    enemies.append(rect)
score = 0
font = pygame.font.SysFont(None, 36)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(20, WIDTH-40)
            enemy.y = random.randint(20, HEIGHT-40)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

