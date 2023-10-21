from Game_Objects.GameObject import GameObject
import pygame
import random


class Virus(GameObject):
    def __init__(self, velocity, screenWidth, screenHeight):
        super().__init__(velocity)

        visusImages = ["Assets\\Viruses\\1.png",
                       "Assets\\Viruses\\2.png",
                       "Assets\\Viruses\\3.png",
                       "Assets\\Viruses\\4.png",
                       "Assets\\Viruses\\5.png",
                       "Assets\\Viruses\\6.png",]
        
        self.image = pygame.image.load(random.choice(visusImages))
        self.rect = self.image.get_rect()
        self.rect.x = (screenWidth / 2) - (self.rect.width / 2)
        self.rect.y = (screenHeight / 2) - (self.rect.height / 2)

    def update(self, screen):
        super().update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.update(screen)