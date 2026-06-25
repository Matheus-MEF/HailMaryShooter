#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, C_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./asset/Level1Bg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pg.mixer.music.load("./asset/Menu.mp3")
        pg.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # TITLE
            self.menu_text(50, "HailMary", C_GREEN, (WIN_WIDTH / 2, 40))
            self.menu_text(50, "Shooter", C_GREEN, (WIN_WIDTH / 2, 80))

            # CONTROLS TEXT
            self.menu_text(
                14,
                "P1: W A S D move | T shoot",
                C_WHITE,
                (WIN_WIDTH / 2, 120)
            )
            self.menu_text(
                14,
                "P2: ARROWS move | NUMPAD 0 shoot",
                C_WHITE,
                (WIN_WIDTH / 2, 140)
            )
            # MENU OPTIONS
            for i in range(len(MENU_OPTION)):
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(
                    20,
                    MENU_OPTION[i],
                    color,
                    (WIN_WIDTH / 2, 180 + 25 * i)
                )

            pg.display.flip()

            # EVENTS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:

                    if event.key in (pg.K_s, pg.K_DOWN):
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    if event.key in (pg.K_w, pg.K_UP):
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    if event.key == pg.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)