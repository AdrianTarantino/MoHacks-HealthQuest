from Game_Objects.GameObject import GameObject
import pygame


class Bullet(GameObject):
    def __init__(self, velocity, direction, startingXPosition, startingYPosition):
        super().__init__(velocity)
        self.direction = direction

        match self.direction:
            case 'u':
                self.image = pygame.image.load("Assets\\Syringe\\up.png")

            case 'd':
                self.image = pygame.image.load("Assets\\Syringe\\down.png")
                
            case 'l':
                self.image = pygame.image.load("Assets\\Syringe\\left.png")
                
            case 'r':
                self.image = pygame.image.load("Assets\\Syringe\\right.png")

        self.rect = self.image.get_rect()
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
