import pygame as pg
import math 
from code.Const import ENTITY_SPEED
from code.entity import Entity


class HealthPill(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        # aumenta tamanho (só dela)
        self.surf = pg.transform.scale(
            self.surf,
            (
                int(self.surf.get_width() * 1),
                int(self.surf.get_height() * 1)
            )
        )

        # guarda imagem base para rotação
        self.base_image = self.surf.copy()
        self.angle = 0

    def move(self):
        # movimento padrão
        self.rect.centery += ENTITY_SPEED[self.name]
        self.rect.centerx += math.sin(pg.time.get_ticks() * 0.005) * 0.5

        # rotação (efeito visual)
        self.angle = (self.angle + 5) % 360

        center = self.rect.center
        self.surf = pg.transform.rotate(self.base_image, self.angle)
        self.rect = self.surf.get_rect(center=center)