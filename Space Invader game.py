import math
import random
import pygame
screen_width = 1000
screen_height = 1000
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 5
enemy_speed_y = 30
bullet_speed_y = 40
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('logo.png')
pygame.display.set_caption("Space Invader Game")
icon = pygame.image.load('UFO.jpg')
pygame.display.set_icon(icon)
playerimg = pygame.image.load('Player.jpg')
playerx = player_start_x
playery = player_start_y
playerx_change = 0
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('Enemy.jpg'))
    enemyx.append(random.randint(0,screen_width-64))
    enemyy.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)
bulletimg = pygame.image.load('Bullet.jpg')
bulletx = 0
bullety = player_start_y
bulletx_change = 0
bullety_change = bullet_speed_y
bullet_state = "Ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render("score"+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))
def game_over_text():
    over_text = over_font.render("gameover",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < collision_distance
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                bullety = playery 
fire_bullet(bulletx, bullety)
if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
    playerx_change = 0
    playerx += playerx_change
    playerX = max(0, min(playerx, screen_width - 64)) 
for i in range(num_of_enemies):
    if enemyy[i] > 340: 
        for j in range(num_of_enemies):
            enemyy[j] = 2000
            game_over_text()
            break
    enemyx[i] += enemyx_change[i]
    if enemyx[i] <= 0 or enemyx[i] >= screen_width - 64:
        enemyx_change[i] *= -1
        enemyy[i] += enemyy_change[i]
    if isCollision(enemyx[i], enemyy[i], bulletx, bullety):
        bullety = player_start_y
        bullet_state = "ready"
        score_value += 1
        enemyx[i] = random.randint(0, screen_width - 64)
        enemyy[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
    enemy(enemyx[i], enemyy[i], i)
if bullety <= 0:
    bullety = player_start_y
    bullet_state = "ready"
elif bullet_state == "fire":
    fire_bullet(bulletx, bullety)
    bullety -= bullety_change
player(playerX, playery)
show_score(textx, texty)
pygame.display.update()