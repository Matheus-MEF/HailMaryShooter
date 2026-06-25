#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, \
    PLAYER_KEY_DOWN, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.PlayerShot import PlayerShot
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.invulnerable = False
        self.invulnerable_time = 0
        # POWER-UP
        self.double_shot = False
        self.power_timer = 0

    def move(self):
        pressed_key = pg.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if self.invulnerable:
            self.invulnerable_time -= 1

            if self.invulnerable_time <= 0:
                self.invulnerable = False
        if self.double_shot:
            self.power_timer -= 1
            if self.power_timer <= 0:
                self.double_shot = False
                ENTITY_SPEED[self.name] -= 1
                ENTITY_SPEED[f'{self.name}Shot'] -= 1

    def shoot(self, pressed=False):
        # cooldown sempre roda independente de input
        if self.shot_delay > 0:
            self.shot_delay -= 1
            return None
        # só dispara se houve input real (evento)
        if not pressed:
            return None
        # reseta cooldown
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        # DOUBLE SHOT
        if self.double_shot:
            return [
                PlayerShot(
                    name=f'{self.name}Shot',
                    position=(self.rect.centerx - 12, self.rect.top)
                ),
                PlayerShot(
                    name=f'{self.name}Shot',
                    position=(self.rect.centerx + 12, self.rect.top)
                )
            ]
        # SINGLE SHOT
        return PlayerShot(
            name=f'{self.name}Shot',
            position=(self.rect.centerx, self.rect.top)
        )

    def draw(self, window):
        if self.invulnerable:
            # pisca: desenha só em frames alternados
            if (self.invulnerable_time // 5) % 2 == 0:
                window.blit(self.surf, self.rect)
        else:
            window.blit(self.surf, self.rect)
