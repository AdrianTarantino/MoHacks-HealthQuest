from Game_Objects.GameObject import GameObject
import pygame
import random


class Virus(GameObject):
    def __init__(self, velocity, screenWidth, screenHeight):
        super().__init__(velocity)

        self.visusImages = ["Assets\\Viruses\\1.png",
                            "Assets\\Viruses\\2.png",
                            "Assets\\Viruses\\3.png",
                            "Assets\\Viruses\\4.png",
                            "Assets\\Viruses\\5.png",
                            "Assets\\Viruses\\6.png",]
        
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.image = pygame.image.load(random.choice(self.visusImages))
        self.rect = self.image.get_rect()

        self.xVelocityMultiplier = 1
        self.yVelocityMultiplier = 1

        self.virusState = random.randint(0,3)
        variationMax = 200

        match self.virusState:
            # Leftside
            case 0:
                self.rect.x = 0 - (2 * self.rect.width) - random.randint(0, variationMax)
                self.rect.y = random.randint(0 + self.rect.height, screenHeight - self.rect.height)

                self.xVelocityMultiplier = 1
                self.yVelocityMultiplier = 0

            # Rightside
            case 1:
                self.rect.x = screenWidth + (2 * self.rect.width) + random.randint(0, variationMax)
                self.rect.y = random.randint(0 + self.rect.height, screenHeight - self.rect.height)

                self.xVelocityMultiplier = -1
                self.yVelocityMultiplier = 0

            # Upside
            case 2:
                self.rect.x = random.randint(0 + self.rect.width, screenWidth - self.rect.width)
                self.rect.y = 0 - (2 * self.rect.height) - random.randint(0, variationMax)

                self.xVelocityMultiplier = 0
                self.yVelocityMultiplier = 1

            # Downside
            case 3:
                self.rect.x = random.randint(0 + self.rect.width, screenWidth - self.rect.width)
                self.rect.y = screenHeight + (2 * self.rect.width) + random.randint(0, variationMax)

                self.xVelocityMultiplier = 0
                self.yVelocityMultiplier = -1

    def move(self):
        self.rect.x += self.velocity * self.xVelocityMultiplier
        self.rect.y += self.velocity * self.yVelocityMultiplier
    
    def outOfRange(self):
        if (self.screenWidth > self.rect.x and self.xVelocityMultiplier == 1): return
        if (self.rect.x > 0 and self.xVelocityMultiplier == -1): return
        if (self.screenHeight > self.rect.y and self.yVelocityMultiplier == 1): return
        if (self.rect.y > 0 and self.yVelocityMultiplier == -1): return

        self.reset()

    def reset(self):
        self.image = pygame.image.load(random.choice(self.visusImages))
        self.rect = self.image.get_rect()
        
        self.virusState = random.randint(0,3)
        variationMax = 200

        match self.virusState:
            # Leftside
            case 0:
                self.rect.x = 0 - (2 * self.rect.width) - random.randint(0, variationMax)
                self.rect.y = random.randint(0 + self.rect.height, self.screenHeight - self.rect.height)

                self.xVelocityMultiplier = 1
                self.yVelocityMultiplier = 0

            # Rightside
            case 1:
                self.rect.x = self.screenWidth + (2 * self.rect.width) + random.randint(0, variationMax)
                self.rect.y = random.randint(0 + self.rect.height, self.screenHeight - self.rect.height)

                self.xVelocityMultiplier = -1
                self.yVelocityMultiplier = 0

            # Upside
            case 2:
                self.rect.x = random.randint(0 + self.rect.width, self.screenWidth - self.rect.width)
                self.rect.y = 0 - (2 * self.rect.height) - random.randint(0, variationMax)

                self.xVelocityMultiplier = 0
                self.yVelocityMultiplier = 1

            # Downside
            case 3:
                self.rect.x = random.randint(0 + self.rect.width, self.screenWidth - self.rect.width)
                self.rect.y = self.screenHeight + (2 * self.rect.width) + random.randint(0, variationMax)

                self.xVelocityMultiplier = 0
                self.yVelocityMultiplier = -1

    def update(self, screen):
        print(self.rect.x, ", ", self.rect.y)
        super().update()
        self.move()
        self.outOfRange()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.update(screen)
