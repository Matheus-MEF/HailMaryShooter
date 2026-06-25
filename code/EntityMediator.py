from code.DoubleShot import DoubleShot
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.enemy import Enemy
from code.entity import Entity
from code.PlayerShot import PlayerShot
from code.EnemyShot import EnemyShot
from code.player import Player
import random
from code.entityFactory import EntityFactory
from code.HealthPill import HealthPill



class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.bottom < 0 :
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2, sound):

        valid_interaction = False

        # -----------------------------
        # DEFINIÇÃO DE INTERAÇÕES VÁLIDAS
        # -----------------------------
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, HealthPill):
            valid_interaction = True
        elif isinstance(ent1, HealthPill) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, DoubleShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, DoubleShot):
            valid_interaction = True
        # -----------------------------
        # SE NÃO HOUVER INTERAÇÃO
        # -----------------------------
        if not valid_interaction:
            return
        # -----------------------------
        # CHECAGEM DE COLISÃO (AABB)
        # -----------------------------
        if not (
                ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom
        ):
            return

        # =====================================================
        # 1. PLAYER vs ENEMY (COLISÃO DE NAVE)
        # =====================================================
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):

            if not ent1.invulnerable:
                ent1.health -= 100
                ent1.invulnerable = True
                ent1.invulnerable_time = 180
                sound.player_hit.play()
                ent2.health = 0

            return

        if isinstance(ent1, Enemy) and isinstance(ent2, Player):

            if not ent2.invulnerable:
                ent2.health -= 100
                ent2.invulnerable = True
                ent2.invulnerable_time = 180
                sound.player_hit.play()

                ent1.health = 0

            return

        # =====================================================
        # 2. HEALTH PILL
        # =====================================================
        if isinstance(ent1, Player) and isinstance(ent2, HealthPill):
            ent1.health = min(ent1.health + 50, 320)
            ent2.health = 0
            sound.health.play()
            return

        if isinstance(ent1, HealthPill) and isinstance(ent2, Player):
            ent2.health = min(ent2.health + 50, 320)
            ent1.health = 0
            sound.health.play()
            return

        # =====================================================
        # 2.1 DOUBLE SHOT
        # =====================================================
        if isinstance(ent1, Player) and isinstance(ent2, DoubleShot):
            if not ent1.double_shot:
                ent1.double_shot = True
                ENTITY_SPEED[ent1.name] += 1
                ENTITY_SPEED[f'{ent1.name}Shot'] += 1
            ent1.power_timer = 600  # ~10 segundos
            ent2.health = 0
            sound.double_shot.play()

        if isinstance(ent1, DoubleShot) and isinstance(ent2, Player):
            if not ent2.double_shot:
                ent2.double_shot = True
                ENTITY_SPEED[ent2.name] += 1
                ENTITY_SPEED[f'{ent2.name}Shot'] += 1
            ent2.power_timer = 600
            ent1.health = 0
            sound.double_shot.play()
            return

        # =====================================================
        # 3. TIROS
        # =====================================================
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            ent1.health -= ent2.damage
            ent1.last_dmg = ent2.name
            ent2.health = 0
            return

        if isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            ent2.health -= ent1.damage
            ent2.last_dmg = ent1.name
            ent1.health = 0
            return

        if isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            if not ent2.invulnerable:
                ent2.health -= ent1.damage
                ent1.health = 0
                sound.player_hit.play()
                return
            else:
                return

        if isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            if not ent1.invulnerable:
                ent1.health -= ent2.damage
                ent2.health = 0
                sound.player_hit.play()
                return
            else:
                return

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score



    @staticmethod
    def verify_collision(entity_list: list[Entity], sound):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2, sound)

    @staticmethod
    def verify_health(entity_list: list[Entity], sound):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                    sound.explosion.play()

                    roll = random.random()
                    if roll < 0.60:
                        return
                    elif roll < 0.80:
                        item = EntityFactory.get_entity('HealthPill', ent.rect.center)
                        entity_list.append(item)
                    else:
                        item = EntityFactory.get_entity('DoubleShot', ent.rect.center)
                        entity_list.append(item)

                entity_list.remove(ent)
