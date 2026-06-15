from datetime import datetime
import sys

import pygame as pg
from pygame import K_BACKSPACE, K_ESCAPE, K_RETURN, KEYDOWN, Surface, Rect
from code.DBProxy import DBProxy
from code.level import Level
from code.Const import C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS

class Score:

    def __init__(self, window: pg.Surface):
        self.window = window
        self.surf = pg.image.load("./asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0,
                                       top=0)  
                                    


    
    def save(self, game_mode: str, player_score: list[int]):
        pg.mixer.music.load("./asset/Score.mp3")
        pg.mixer.music.play(-1)  # o parametro -1 serve para a musica ficar em loop
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = ' Enter Player 1 name (4 characters):'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1] / 2)
                text = 'Enter Team name (4 characters):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 characters)'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters)'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date() })
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                        
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pg.display.flip()
       

    def show(self):
        pg.mixer.music.load("./asset/Score.mp3")
        pg.mixer.music.play(-1)  # o parametro -1 serve para a musica ficar em 
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME        SCORE           DATE     ', C_YELLOW, SCORE_POS['Label'])
        db_proxy  = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name} {score :05d} {date}', C_YELLOW, SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pg.display.flip()
            

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"  