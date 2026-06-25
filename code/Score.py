from datetime import datetime
import sys
import pygame as pg

from pygame import K_BACKSPACE, K_ESCAPE, K_RETURN
from pygame.font import Font
from pygame import Surface, Rect

from code.DBProxy import DBProxy
from code.Const import C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS


class Score:

    def __init__(self, window: pg.Surface):
        self.window = window
        self.surf = pg.image.load("./asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    # -----------------------------
    # SAVE SCORE SCREEN
    # -----------------------------
    def save(self, game_mode: str, player_score: list[int]):
        pg.mixer.music.load("./asset/Score.mp3")
        pg.mixer.music.play(-1)

        db_proxy = DBProxy('DBScore')
        name = ""

        # -----------------------------
        # DEFINE SCORE + RESULT TEXT
        # -----------------------------
        if game_mode == MENU_OPTION[0]:
            score = player_score[0]
            prompt_text = "Enter Player 1 name (4 characters)"
            result_text = "WIN!"

        elif game_mode == MENU_OPTION[1]:
            score = (player_score[0] + player_score[1]) / 2
            prompt_text = "Enter Team name (4 characters)"
            result_text = "COOP COMPLETE"

        else:  # COMPETITIVE
            if player_score[0] > player_score[1]:
                score = player_score[0]
                result_text = "PLAYER 1 WINS"
            elif player_score[1] > player_score[0]:
                score = player_score[1]
                result_text = "PLAYER 2 WINS"
            else:
                score = player_score[0]
                result_text = "DRAW"

            prompt_text = "Enter Winner name (4 characters)"

        # -----------------------------
        # INPUT LOOP
        # -----------------------------
        while True:
            self.window.blit(self.surf, self.rect)

            self.score_text(48, result_text, C_YELLOW, SCORE_POS['Title'])
            self.score_text(20, prompt_text, C_WHITE, SCORE_POS['EnterName'])
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                elif event.type == pg.KEYDOWN:

                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({
                            'name': name,
                            'score': score,
                            'date': get_formatted_date()
                        })
                        db_proxy.close()
                        self.show()
                        return

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]

                    elif event.unicode.isalnum() and len(name) < 4:
                        name += event.unicode.upper()

            pg.display.flip()

    # -----------------------------
    # SCOREBOARD SCREEN
    # -----------------------------
    def show(self):
        pg.mixer.music.load("./asset/Score.mp3")
        pg.mixer.music.play(-1)

        self.window.blit(self.surf, self.rect)

        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME        SCORE           DATE', C_YELLOW, SCORE_POS['Label'])

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i, player_score in enumerate(list_score):
            _id, name, score, date = player_score

            self.score_text(
                20,
                f'{name}   {score:05d}   {date}',
                C_YELLOW,
                SCORE_POS[i]
            )

        # -----------------------------
        # WAIT INPUT LOOP
        # -----------------------------
        while True:
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pg.display.flip()

    # -----------------------------
    # TEXT RENDER
    # -----------------------------
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


# -----------------------------
# UTIL
# -----------------------------
def get_formatted_date():
    current_datetime = datetime.now()
    return current_datetime.strftime("%H:%M - %d/%m/%y")