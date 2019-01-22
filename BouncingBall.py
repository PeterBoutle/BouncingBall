import pygame as pyg
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

BALL_SIZE = 25

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.colour = WHITE

class Paddle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.colour = WHITE

def make_ball():
    ball = Ball()
        # starting pos of ball
    ball.x = random.randrange(BALL_SIZE,SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE,SCREEN_HEIGHT - BALL_SIZE)
    ball.colour = RED
    ball.change_x = random.randrange(-2,3)
    ball.change_y = random.randrange(-2,3)
    return ball

def make_paddle():
    paddle = Paddle()
    paddle.y = SCREEN_HEIGHT - 10
    paddle.x = SCREEN_WIDTH/2
    paddle.width = 50
    paddle.height = 10
    paddle.colour = BLUE
    return paddle

def main():
    pyg.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pyg.display.set_mode(size)

    pyg.display.set_caption("bouncing Balls!")

    done = False

    clock = pyg.time.Clock()
    ball_list =[]
    ball = make_ball()
    ball_list.append(ball)
    paddle = make_paddle()

    while not done:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                done = True

        pressed = pyg.key.get_pressed()        
        if pressed[pyg.K_RIGHT] and paddle.x + paddle.width <= SCREEN_WIDTH: paddle.x +=3
        if pressed[pyg.K_LEFT] and paddle.x >=0 : paddle.x -=3   
        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        screen.fill(BLACK)

        for ball in ball_list:
            pyg.draw.circle(screen,ball.colour,[ball.x,ball.y],BALL_SIZE)
        pyg.draw.rect(screen,paddle.colour,pyg.Rect(paddle.x,paddle.y,paddle.width,paddle.height))


        clock.tick(60)
        pyg.display.flip()


if __name__ =="__main__":
    main()




        