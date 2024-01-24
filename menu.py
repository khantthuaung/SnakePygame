import pygame as pg
import sys
from variable import *

button_color = pg.Color("white")
class MENU():
    def __init__(self):
       pass

    def create_button(self,image_name,button):
        image_load = pg.image.load(image_name).convert_alpha()
        image_rect = image_load.get_rect(center = button.center)
        screen.blit(image_load,image_rect)

    def create_title(self, text, rect):
        title_text = title_font.render(text, True, (231, 37, 230))
        title_rect = title_text.get_rect(center = rect.center)
        screen.blit(title_text,title_rect)

    def draw_buttons(self):
        self.create_title("Main Menu",title)
        self.create_button("Graphics/play1.PNG",start_btn)
        self.create_button("Graphics/options1.PNG",option_btn)
        self.create_button("Graphics/quit1.PNG",quit_btn)


