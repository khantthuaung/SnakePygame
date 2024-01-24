import random,pygame
from pygame import Vector2
from variable import cell_size,screen,apple,cell_number
class FRUIT:
    def __init__(self):
        #create x and y position
        self.randomize()
        
    def draw_fruit(self):
        #draw rect
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        #pg.draw.rect(screen,pg.Color("red"),fruit_rect)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)