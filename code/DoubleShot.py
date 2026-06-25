from code.entity import Entity


class DoubleShot(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += self.speed