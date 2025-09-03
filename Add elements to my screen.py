import pygame
import sys
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
rect_width, rect_height = 200, 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
pygame.draw.rect(window, RED, (rect_x, rect_y, rect_width, rect_height))
font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, WHITE)
text_rect = text.get_rect(center=(320, 50))  
window.blit(text, text_rect)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
