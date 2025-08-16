import pygame
pygame.init()
Window = pygame.display.set_mode((00,400))
Window.fill((255,255,255))
GREEN = (0,255,0)
pygame.draw.circle(Window,GREEN,(300,300),50)
pygame.draw.circle(Window,GREEN,(100,100),50,3)
pygame.display.update()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()