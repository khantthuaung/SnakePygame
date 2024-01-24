import pygame as pg
import sys
from variable import *

class OPTIONS:
    def __init__(self):
        pass
    def create_slider(self,volume):
        slider_x = int(bar_x + volume * bar_width - slider_width / 2)
        pg.draw.rect(screen, pg.Color("black"),(bar_x,bar_y,bar_width,bar_height))
        pg.draw.rect(screen,(59, 241, 19),(bar_x,bar_y,int(volume* bar_width),bar_height))

        pg.draw.rect(screen, pg.Color("black"),(slider_x,slider_y,slider_width,slider_height))

        music_text = setting_font.render(f"Music:", True, (87, 94, 248))
        volume_text = setting_font.render(f"{volume*100:.0f}", True, (87, 94, 248))
        screen.blit(music_text, (bar_x -80, bar_y))
        screen.blit(volume_text, (slider_x, bar_y - slider_height))