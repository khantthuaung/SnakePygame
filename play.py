from variable import screen,cell_number,cell_size,apple,number_font,pause,clock
from snake import SNAKE
from fruit import FRUIT
import pygame as pg
import json

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = 0
        self.pause = pause

    def update(self):
        if self.pause == False:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #reposition the fruit
            self.fruit.randomize()
            #add length to snake
            self.snake.add_block()
            self.snake.play_crunch_sound()
            self.score +=1
            self.save_score()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self):
        #check offscreen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        #check snake hit itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        # screen.fill((255,255,255))
        # pg.display.update()
        # clock.tick(60)
        pass

    def draw_grass(self):
        grass_color=(167,209,61)

        for row in range(cell_number):
            if row %2 ==0:
                for col in range(cell_number):
                    if col%2 == 0:
                        grass_rect = pg.Rect(col * cell_size,row*cell_size,cell_size,cell_size)
                        pg.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        grass_rect = pg.Rect(col * cell_size,row*cell_size,cell_size,cell_size)
                        pg.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = number_font.render(score_text,True,pg.Color("Black"))
        score_x= int(cell_size*cell_number-662)
        score_y= int(cell_size* cell_number - 682)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        
        bg_rect = pg.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width +6,apple_rect.height)
        pg.draw.rect(screen,(167,209,61),bg_rect)

        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pg.draw.rect(screen,pg.Color("Black"),bg_rect,2)

    def save_score(self):
        game_state = {
            "score": self.score,
            "snake_body" : [(block.x, block.y) for block in self.snake.body]
        }
        with open("game_state.json","w") as file:
            json.dump(game_state,file)
    
    def load_score(self):
        try:
            with open("game_state.json", "r") as file:
                game_state = json.load(file)
                self.score = game_state["score"]
                self.body_pos = [pg.Rect(pos[0], pos[1], cell_size, cell_size) for pos in game_state["snake_body"]]
        except FileNotFoundError:
            # If the file is not found, create a new one with default values
            self.save_score()

    def toggle_pause(self):
        self.pause = not self.pause