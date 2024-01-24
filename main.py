import pygame as pg
import asyncio
import sys
from pygame.math import Vector2
from play import MAIN
from menu import MENU
from setting import OPTIONS
from variable import *

pg.init()

menu = MENU()
main_game = MAIN()
options = OPTIONS()

async def main():
    game_state = "menu"
    volume = 0.5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pg.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pg.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pg.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if pause_btn.collidepoint(event.pos):
                    game_state = "pause"
                    main_game.toggle_pause()
            if game_state =="menu":
                if event.type == pg.MOUSEBUTTONDOWN:
                    if quit_btn.collidepoint(event.pos):
                        pg.quit()
                        sys.exit()
                    if start_btn.collidepoint(event.pos):
                        # start_sound.play()
                        game_state = "game"
                    if option_btn.collidepoint(event.pos):
                        game_state = "options"
            elif game_state == "options":
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back_btn.collidepoint(event.pos):
                        game_state = "menu"
                if event.type == pg.MOUSEMOTION:
                    if pg.mouse.get_pressed()[0]: 
                        mouseX, _ = event.pos
                        volume = max(0, min(1, (mouseX - bar_x) / bar_width))
                        # menu_sound.set_volume(volume)
            elif game_state == "pause":
                if event.type == pg.MOUSEBUTTONDOWN:
                    if resume_btn.collidepoint(event.pos):
                        game_state = "game"
                        main_game.toggle_pause()
                    if option_btn.collidepoint(event.pos):
                        game_state = "options"
                    if mainmenu_btn.collidepoint(event.pos):
                        game_state = "menu"
            
        await asyncio.sleep(0)
        if game_state == "game":
            #menu_sound.stop()
            pg.display.set_caption("Snake Game")
            screen.fill((175,215,70))
            main_game.draw_elements()
            menu.create_button("Graphics/pause2.png",pause_btn)
            pg.display.update()
            clock.tick(60)

        elif game_state == "menu":
            # menu_sound.play()
            pg.display.set_caption("Main Menu")
            screen.fill((236, 227, 36))
            main_game.draw_grass()
            menu.draw_buttons()
            pg.display.update()
            clock.tick(60)
            
        elif game_state == "options":
            pg.display.set_caption("Options")
            screen.fill((183, 231, 37))
            slider_x = int(bar_x + volume * bar_width - slider_width / 2)
            main_game.draw_grass()
            options.create_slider(volume)
            menu.create_title("Options",options_text)
            menu.create_button("Graphics/back.PNG", back_btn)
            pg.display.flip()

        elif game_state == "pause":
            screen.fill((183, 231, 37))
            main_game.draw_grass()
            menu.create_title("Pause",pause_text)
            menu.create_button("Graphics/resume.PNG", resume_btn)
            menu.create_button("Graphics/mainmenu.PNG", mainmenu_btn)
            menu.create_button("Graphics/options1.PNG", option_btn)
            pg.display.update()

        

        

asyncio.run(main())