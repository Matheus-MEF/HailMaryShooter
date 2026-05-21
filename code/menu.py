#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        # abaixo iremos (carregar a imagem), (adicionar um retangulo invisel) e (adicionar a imgagem e ele)
        self.surf = pg.image.load("./asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0,
                                       top=0)  # o retangulo já inicia nas coordenadas 0,0, porem especifiquei apenas para entendimento

    def run(self):

        pg.mixer.music.load("./asset/Menu.mp3")
        pg.mixer.music.play(-1)  # o parametro -1 serve para a musica ficar em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # pegando a imagem e jogando no retangulo
            self.menu_text(50, "Moutain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pg.display.flip()  # atualizando a tela

            # check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()  # end pygame
                    return

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
