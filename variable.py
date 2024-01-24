import pygame as pg

pg.font.init()
pg.mixer.init()
pg.mixer.pre_init(44100, -16, 2, 1024)
cell_size = 38
cell_number =20
screen = pg.display.set_mode((cell_number*cell_size,cell_size*cell_number))
clock = pg.time.Clock()
apple = pg.image.load('Graphics/apple.png').convert_alpha()
number_font = pg.font.Font('Font/BigSpace.ttf')
setting_font = pg.font.Font('Font/BigSpace.ttf',25)
button_font = pg.font.Font('Font/MarioRegular.ttf')
title_font = pg.font.Font('Font/PixelPowerline-9xOK.ttf',60)
pause = False
# start_sound = pg.mixer.Sound('Sound/start.mp3')
# menu_sound = pg.mixer.Sound('Sound/mainmenu.wav')

####
element_x =int(cell_number*cell_size/3)
element_y =int(cell_number* cell_size/2)

############
title = pg.Rect(element_x-80,element_y-400,400,200)
options_text = title.copy()
pause_text = title.copy()
########################
button_w = 200
button_h = 40
start_btn = pg.Rect(element_x+20,element_y-90, button_w,button_h)
pause_btn = pg.Rect(int(cell_number*cell_size/2+230) ,int(cell_size*cell_number-700), button_w,button_h)
option_btn = pg.Rect(element_x+20,element_y, button_w,button_h)
quit_btn = pg.Rect(element_x+20,element_y+90, button_w,button_h)
back_btn = quit_btn.copy()
resume_btn = start_btn.copy()
mainmenu_btn = quit_btn.copy()
##############
bar_height = 30
bar_width = 300        
slider_height = bar_height +20
slider_width = 20
volume  = 0.5
bar_x = int(cell_number*cell_size/2 - 150)
bar_y = int(cell_number*cell_size/2)

slider_y = int(bar_y - (slider_height - bar_height) / 2)

SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE,150)
