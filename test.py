import pygame as PG


class Human(PG.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PG.image.load("assets\\img\\character\\Human.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

PG.init()
clock = PG.time.Clock()
clock.tick(60)
done = False
size = (700, 500)
screen = PG.display.set_mode(size)
my_group = PG.sprite.Group()
my_sprite = Human()
my_group.add(my_sprite)

PG.display.set_caption("1013")

while not done:
    # 处理事件
    for event in PG.event.get():
        if event.type == PG.QUIT:
            done = True

    my_group.draw(screen)
    screen.fill((255, 255, 255))

    PG.display.update()