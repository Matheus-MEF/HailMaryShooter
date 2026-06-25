#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, PLAYER_KEY_SHOOT, WIN_WIDTH, PLAYER_MAX_LIFE
from code.EntityMediator import EntityMediator

from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], sound):
        self.timeout = TIMEOUT_LEVEL  # 20 seconds
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.sound = sound
        player = (EntityFactory.get_entity('Player1'))
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = (EntityFactory.get_entity('Player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, 100)

    def draw_hp_bar(self, x, y, entity, color):
        bar_width = 120
        bar_height = 10

        max_hp = PLAYER_MAX_LIFE[entity.name]
        current_hp = max(0, min(entity.health, max_hp))

        # fundo
        pg.draw.rect(self.window, (60, 60, 60), (x, y, bar_width, bar_height))

        # preenchimento
        fill = int((current_hp / max_hp) * bar_width)

        pg.draw.rect(self.window, color, (x, y, fill, bar_height))

    def run(self, player_score: list[int]):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    ent.draw(self.window)
                else:
                    self.window.blit(ent.surf, ent.rect)
                ent.move()

                if isinstance(ent, Enemy):
                    shot = ent.shoot()
                    if shot is not None:
                        self.entity_list.append(shot)
                        self.sound.enemy_shot.play()

                if isinstance(ent, Player):
                    keys = pg.key.get_pressed()
                    pressed = keys[PLAYER_KEY_SHOOT[ent.name]]
                    shoot = ent.shoot(pressed)
                    if shoot is not None:
                        if ent.double_shot:
                            if ent.name == 'Player1':
                                self.sound.player1_double_shot.play()
                            else:
                                self.sound.player2_double_shot.play()
                        else:
                            if ent.name == 'Player1':
                                self.sound.player1_shot.play()
                            else:
                                self.sound.player2_shot.play()
                        if isinstance(shoot, list):
                            self.entity_list.extend(shoot)
                        else:
                            self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(
                        14,
                        "HP",
                        C_GREEN,
                        (10, WIN_HEIGHT - 65)
                    )
                    self.draw_hp_bar(
                        10,
                        WIN_HEIGHT - 45,
                        ent,
                        C_GREEN
                    )
                if ent.name == 'Player2':
                    self.level_text(
                        14,
                        "HP",
                        C_CYAN,
                        (WIN_WIDTH - 150, WIN_HEIGHT - 65)
                    )

                    self.draw_hp_bar(
                        WIN_WIDTH - 150,
                        WIN_HEIGHT - 45,
                        ent,
                        C_CYAN
                    )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemy = random.choices(['Enemy1', 'Enemy2'], weights=[2, 1])[0]
                    self.entity_list.append(EntityFactory.get_entity(enemy))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # printed text
            self.level_text(
                14,
                f'{self.name} - TIME: {self.timeout / 1000 :.1f}s',
                C_WHITE,
                (WIN_WIDTH // 2 - 120, 5)
            )

            self.level_text(
                14,
                f'FPS: {clock.get_fps() :.0f}',
                C_WHITE,
                (WIN_WIDTH // 2 - 10, 5)
            )
            # self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            # COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list, sound=self.sound)
            EntityMediator.verify_health(entity_list=self.entity_list, sound=self.sound)
            pg.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucia Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
