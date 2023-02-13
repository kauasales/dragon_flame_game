class Dragon(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.size = (16, 16)
        self.pos = (10, 10)
        self.rect = pygame.Rect(self.pos, self.size)

        self.speed = 50
        self.dir = pygame.math.Vector2()

    def update(self, screen, dt):
        self.rect.topleft = self.pos
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        self.move(dt)

    def move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.speed * self.dir * dt








 elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if abs(event.value) > 0.4:
                        p1.dir.x = event.value
                    else:
                        p1.dir.x = 0
                elif event.axis == 1:
                    if abs(event.value) > 0.4:
                        p1.dir.y = event.value
                    else:
                        p1.dir.y = 0