import pygame

class Paddle():
    colour = (0,128,255)
    startpos_x = 10
    startpos_y = 275
    width = 100
    height = 20

class Ball():
    colour = (255,0,0)
    startpos_x = 50
    startpos_y = 50
    radius =20
    


screen_height = 400
screen_width = 300

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_height,screen_width))
paddle = Paddle()
ball = Ball()

done = False
x = paddle.startpos_x
y = paddle.startpos_y

ball_x = ball.startpos_x
ball_y = ball.startpos_y

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0,0,0))
    pressed = pygame.key.get_pressed()        
    if pressed[pygame.K_RIGHT] and x <= screen_width: x +=3
    if pressed[pygame.K_LEFT] and x >=0 : x -=3


    pygame.draw.circle(screen,ball.colour,(ball_x,ball_y),ball.radius)
    pygame.draw.rect(screen,paddle.colour,pygame.Rect(x,y,paddle.width,paddle.height))

    pygame.display.flip()
    clock.tick(60)
    

