import pygame as pg

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Score import Score
from code.SoundManeger import SoundManager
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.sound = SoundManager()
        self.window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def set_resolution(self, size):
        self.window = pg.display.set_mode(size)

    def run(self):

        while True:
            score = Score(self.window)

            # MENU
            self.set_resolution((547, 324))

            menu = Menu(self.window)
            menu_return = menu.run()

            # START GAME
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:

                menu_image = menu.surf


                # TRANSIÇÃO
                self.resize_transition(
                    start_size=(547, 324),
                    end_size=(WIN_WIDTH, WIN_HEIGHT),
                    image=menu_image
                )

                player_score = [0, 0]

                # LEVEL 1
                level = Level(self.window, 'Level1', menu_return, player_score, self.sound)
                level_return = level.run(player_score)

                # LIMPEZA FORÇADA
                self.window.fill((0, 0, 0))
                pg.display.flip()
                pg.event.pump()

                # LEVEL 2
                if level_return:

                    level = Level(self.window, 'Level2', menu_return, player_score, self.sound)
                    level_return = level.run(player_score)

                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pg.quit()
                quit()

    def resize_transition(self, start_size, end_size, steps=30, image=None):

        sw, sh = start_size
        ew, eh = end_size

        clock = pg.time.Clock()

        if image is None:
            image = pg.Surface(start_size)
            image.fill((0, 0, 0))

        for i in range(1, steps + 1):

            self.window.fill((0, 0, 0))

            t = i / steps

            new_w = int(sw + (ew - sw) * t)
            new_h = int(sh + (eh - sh) * t)

            self.set_resolution((new_w, new_h))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            scaled = pg.transform.smoothscale(image, (new_w, new_h))

            self.window.blit(scaled, (0, 0))
            pg.display.flip()

            clock.tick(60)
