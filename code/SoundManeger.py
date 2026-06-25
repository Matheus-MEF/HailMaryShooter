import pygame as pg

class SoundManager:

    def __init__(self):
        # Combate
        self.player1_shot = pg.mixer.Sound('./asset/Player1Shot.mp3')
        self.player2_shot = pg.mixer.Sound('./asset/Player2Shot.mp3')

        self.player1_double_shot = pg.mixer.Sound('./asset/Player1Double.mp3')
        self.player2_double_shot = pg.mixer.Sound('./asset/Player2Double.mp3')

        self.enemy_shot = pg.mixer.Sound('./asset/EnemyShot.mp3')

        self.explosion = pg.mixer.Sound('./asset/Explosion.mp3')
        self.player_hit = pg.mixer.Sound('./asset/Damage.mp3')

        # Power-ups
        self.health = pg.mixer.Sound('./asset/HealthPill.mp3')
        self.double_shot = pg.mixer.Sound('./asset/DoubleShot.mp3')

        # Volume
        self.player1_shot.set_volume(0.4)
        self.player2_shot.set_volume(0.4)
        self.player1_double_shot.set_volume(0.4)
        self.player2_double_shot.set_volume(0.4)
        self.enemy_shot.set_volume(0.4)

        self.explosion.set_volume(0.9)
        self.double_shot.set_volume(0.5)