import pygame
pygame.init()
window = pygame.display.set_mode((800,600))
r1,r2=pygame.Rect(100,250,50,50),pygame.Rect(650,250,50,50)
c1,c2=(255,0,0),(0,0,255)
run=1
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT: run=0
        if i.type==pygame.KEYDOWN and i.key==pygame.K_SPACE:
            c1,c2=(0,255,0),(255,255,0)  
    window.fill((255,255,255))
    pygame.draw.rect(window,c1,r1);pygame.draw.rect(window,c2,r2)
    pygame.display.flip()
pygame.quit()