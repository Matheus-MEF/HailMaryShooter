#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]
        if self.rect.bottom <= 0:
            self.rect.top = WIN_HEIGHT
        pass
