from Game_Objects.GameObject import GameObject
from Game_Objects.Bullet import Bullet
import pygame

class Player(GameObject):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, velocity, screenWidth, screenHeight):
        super().__init__(velocity)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        
        self.velocity = 5
        
        self.image = pygame.image.load("Assets\\Right\\1.png")
        self.rect = self.image.get_rect()
        self.rect.x = (screenWidth / 2) - (self.rect.width / 2)
        self.rect.y = (screenHeight / 2) - (self.rect.height / 2)

        self.bullets = pygame.sprite.Group()
        self.direction = 'u'
        self.shootKeyPressed = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
            self.direction = 'l'
            self.image = pygame.image.load("Assets\\Left\\1.png")

        if keys[pygame.K_d]:
            self.rect.x += self.velocity
            self.direction = 'r'
            self.image = pygame.image.load("Assets\\Right\\1.png")

        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
            self.direction = 'u'
            self.image = pygame.image.load("Assets\\Up\\1.png")

        if keys[pygame.K_s]:
            self.rect.y += self.velocity
            self.direction = 'd'
            self.image = pygame.image.load("Assets\\Down\\1.png")

    def shoot(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not self.shootKeyPressed:
                self.shootKeyPressed = True

                bulletOffsetY = 0
                bulletOffsetX = 0

                if self.direction == 'l':
                    bulletOffsetX -= 45

                if self.direction == 'r':
                    bulletOffsetX += 25

                if self.direction == 'l' or self.direction == 'r':
                    bulletOffsetY -= 20


                if self.direction == 'u':
                    bulletOffsetY -= 40

                if self.direction == 'u' or self.direction == 'd':
                    bulletOffsetX -= 15
                    
                bulletWidth = 10
                bulletHeight = 10
                bulletVelocity = 20

                self.bullets.add(Bullet(bulletVelocity, 
                                        self.direction, 
                                        self.rect.x + (self.rect.width / 2) - (bulletWidth / 2) + bulletOffsetX, 
                                        self.rect.y + (self.rect.height / 2) - (bulletHeight  /2) + bulletOffsetY))
        else:
            self.shootKeyPressed = False

        self.bullets.draw(screen)

    def filterBullets(self):
        for bullet in self.bullets.sprites():
            if self.screenWidth + bullet.rect.width < bullet.rect.x or bullet.rect.x < 0 - bullet.rect.width:
                print("killing bullet")
                self.bullets.remove(bullet)

            if self.screenHeight + bullet.rect.height < bullet.rect.y or bullet.rect.y < 0 - bullet.rect.height:
                print("killing bullet")
                self.bullets.remove(bullet)

    def update(self, screen):
        super().update()
        self.move()
        self.shoot(screen)
        self.bullets.update()
        self.filterBullets()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.update(screen)
