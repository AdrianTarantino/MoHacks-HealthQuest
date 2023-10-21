from Game_Objects.GameObject import GameObject


class Bullet(GameObject):
    def __init__(self, color, width, height, velocity, direction, startingXPosition, startingYPosition):
        super().__init__(color, width, height, velocity)
        self.direction = direction
        self.rect.x = startingXPosition
        self.rect.y = startingYPosition

    def move(self):
        match self.direction:
            case 'u':
                self.rect.y -= self.velocity
            case 'd':
                self.rect.y += self.velocity
            case 'l':
                self.rect.x -= self.velocity
            case 'r':
                self.rect.x += self.velocity

    def update(self):
        super().update()
        self.move()

    def draw(self, screen):
        self.update()
        screen.blit(self.image, self.rect)
