#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from abc import ABC, abstractmethod

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, ENTITY_SPEED


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pg.image.load(f'./asset/{name}.png').convert_alpha()

        if "Bg" not in name:
            self.surf = pg.transform.scale(
                self.surf,
                (
                    self.surf.get_width() // 2,
                    self.surf.get_height() // 2
                )
            )
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED.get(self.name, 0)
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):

        pass
