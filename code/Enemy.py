import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOOT_DELAY
from code.EnemyShoot import EnemyShoot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            # som do laser
            shoot = pygame.mixer.Sound('./asset/laserEnemy.ogg')
            shoot.play()
            return EnemyShoot(name=f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery))
        else:
            return None