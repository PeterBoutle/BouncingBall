import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,300))

done = False
x = 10
y = 275
colour = (0,128,255)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0,0,0))
    pressed = pygame.key.get_pressed()        
    if pressed[pygame.K_RIGHT]: x +=3
    if pressed[pygame.K_LEFT]: x -=3

    pygame.draw.rect(screen,colour,pygame.Rect(x,y,100,20))

    pygame.display.flip()
    clock.tick(60)
    
