# importing the tools needed
import pygame
import sys
import random

# this creates the display window
screenwidth = 600
screenheight = 400
gridsize = 20
gridwidth = screenwidth / gridsize
gridheight = screenheight / gridsize

# variables for how each control moves the snake
w    = (0, -1)
s  = (0, 1)
a  = (-1, 0)
d = (1, 0)

# the main function that has most needed variables
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenwidth, screenheight), 0, 32)
    surface = pygame.Surface(screen.get_size())
    snake = Snake()
    food = Food()
    myfont = pygame.font.SysFont("comic sans", 24)
    score = 0

# a loop of all processes that should be running while the game going on
    while True:
        clock.tick(15)
        snake.handler()
        grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score = snake.length - 1
            food.randomposit()
        snake.draw(surface)
        food.draw(surface) 
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (0,0,0))
        screen.blit(text, (500, 5))
        pygame.display.update() 

# the class for the snake 
class Snake(object):
    def __init__(self):
        self.length = 1
        self.posit = [((screenwidth / 2), (screenheight / 2))]
        self.direction = random.choice([w, s, a, d])
        self.color = (55, 255, 0)

# gives the position of the snakes head
    def get_head_position(self):
        return self.posit[0]

# how the snake turns
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

# what happens when the player dies
    def reset(self):
        self.length = 1
        self.posit =  [((screenwidth / 2), (screenheight / 2))]
        self.direction = random.choice([w, s, a, d])

# how the game is able to tell if the snakes body overlaps with itself
    def move(self):
        headpos = self.get_head_position()
        x, y = self.direction
        gridize = (((headpos[0] + (x*gridsize)) % screenwidth), (headpos[1] + (y*gridsize)) % screenheight)
        if len(self.posit) > 2 and gridize in self.posit[2:]:
            self.reset()
        else:
            self.posit.insert(0, gridize)
            if len(self.posit) > self.length:
                self.posit.pop()                    

# function that draws the snake
    def draw(self, surface):
        for p in self.posit:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)

# this handles all of the player inputs
    def handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.turn(w)
                elif event.key == pygame.K_s:
                    self.turn(s)
                elif event.key == pygame.K_a:
                    self.turn(a)
                elif event.key == pygame.K_d:
                    self.turn(d)

# class for the food object
class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 34, 0)
        self.randomposit()

# function for how the food is randomly spawned in after it is eaten
    def randomposit(self):
        self.position = (random.randint(0, gridwidth-1) * gridsize, random.randint(0, gridheight-1) * gridsize)

# function that draws the food
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)

# function that draws the background squares
def grid(surface):
    for y in range(0, int(gridheight)):
        for x in range(0, int(gridwidth)):
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (176, 35, 160), rr)

# what needs to run when the program is opened
main()
import pygame
import sys
import random

class Snake():
    def __init__(self):
        self.length = 1
        self.posit = [((screenwidth/2), (screenheight/2))]
        self.direction = random.choice([w, s, a, d])
        self.score = 0

    def get_head_position(self):
        return self.posit[0]