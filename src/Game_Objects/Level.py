import pygame


class Level(pygame.sprite.Sprite):
    def __init__(self, imagePath, screenWidth, screenHeight):
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()
        
        self.rect.x = (screenWidth / 2) - (self.rect.width / 2)
        self.rect.y = (screenHeight / 2) - (self.rect.height / 2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
