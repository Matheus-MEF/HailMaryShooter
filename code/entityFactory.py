#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.enemy import Enemy
from code.player import Player
from code.background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
import random
from code.HealthPill import HealthPill
from code.DoubleShot import DoubleShot



class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:

            case 'Level1Bg':
                return [
                    Background('Level1Bg', (0, 0)),
                    Background('Level1Bg', (0, -WIN_HEIGHT))
                ]

            case 'Level2Bg':
                return [
                    Background('Level2Bg', (0, 0)),
                    Background('Level2Bg', (0, -WIN_HEIGHT))
                ]


            case 'Player1':
                player = Player('Player1', (0, 0))

                x = (WIN_WIDTH - player.rect.width) // 2
                y = WIN_HEIGHT - player.rect.height - 20

                return Player('Player1', (x, y))

            case 'Player2':
                player = Player('Player2', (0, 0))

                x = (WIN_WIDTH - player.rect.width) // 2
                y = WIN_HEIGHT - player.rect.height - 20

                return Player('Player2', (x, y))

            case 'Enemy1':
                temp_enemy = Enemy('Enemy1', (0, 0))
                x = random.randint(0, WIN_WIDTH - temp_enemy.rect.width)
                y = -temp_enemy.rect.height
                return Enemy('Enemy1', (x, y))

            case 'Enemy2':
                temp_enemy = Enemy('Enemy2', (0, 0))
                x = random.randint(0, WIN_WIDTH - temp_enemy.rect.width)
                y = -temp_enemy.rect.height
                return Enemy('Enemy2', (x, y))

            case 'HealthPill':
                return HealthPill('HealthPill', position)

            case 'DoubleShot':
                return DoubleShot('DoubleShot', position)


            case _:
                raise ValueError(f"Entity inválida: {entity_name}")
