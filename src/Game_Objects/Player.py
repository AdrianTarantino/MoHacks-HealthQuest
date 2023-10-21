from Game_Objects.GameObject import GameObject
from Game_Objects.Bullet import Bullet
import pygame

class Player(GameObject):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height, velocity, screenWidth, screenHeight):
        super().__init__(color, width, height, velocity)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.velocity = 5
        self.Left = False
        self.Right = False
        self.Up = False
        self.Down = False 

        self.rect.x = (screenWidth / 2) - (width / 2)
        self.rect.y = (screenHeight / 2) - (height / 2)

        self.bullets = pygame.sprite.Group()
        self.direction = 'u'
        self.shootKeyPressed = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
            self.Left = True
            self.Right = False
            self.direction = 'l'
        if keys[pygame.K_d]:
            self.rect.x += self.velocity
            self.direction = 'r'
            self.Right = True
            self.Left = False
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
            self.direction = 'u'
            self.Up = True
            self.Down = False
        if keys[pygame.K_s]:
            self.rect.y += self.velocity
            self.direction = 'd'
            self.Up = False
            self.Down = True

    def shoot(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not self.shootKeyPressed:
                self.shootKeyPressed = True
                bulletWidth = 10
                bulletHeight = 10
                bulletVelocity = 20

                self.bullets.add(Bullet("grey", 
                                        bulletWidth, 
                                        bulletHeight, 
                                        bulletVelocity, 
                                        self.direction, 
                                        self.rect.x + (self.rect.width / 2) - (bulletWidth / 2), 
                                        self.rect.y + (self.rect.height / 2) - (bulletHeight  /2)))
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
        self.update(screen)
        screen.blit(self.image, self.rect)
