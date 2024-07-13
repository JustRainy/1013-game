import pygame as PG


class Human(PG.sprite.Sprite):
    def __init__(self, frames = 1):
        super().__init__()
        image = PG.image.load("assets\\img\\character\\Human.png").convert()
        self.original_width = image.get_width() // frames  # 整除造型数，平均分图片
        self.original_height = image.get_height()
        self.images = []
        frame_surface = PG.Surface([self.original_width, self.original_height])
        x=0  # 初始坐标设置为0
        for i in range(frames):
            frame_surface = PG.Surface([self.original_width, self.original_height])
            frame_surface.blit(image,[x,0])
            self.images.append(frame_surface.copy())  # 注意这里需要用到Surface的copy方法才可以有效保存精灵矩形
            x -= self.original_width    # 每一次减去一个造型的矩形固定宽度
        self.image = self.images[0]  # 默认显示第一个造型
        self.current_index = 0  # 设置默认造型标志
        self.rect = self.image.get_rect()   # 初始化图片矩形

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

    screen.fill((255, 255, 255))
    my_group.draw(screen)
    PG.display.flip()

    PG.display.update()