from Game_Objects.GameObject import GameObject
from Game_Objects.Bullet import Bullet
import pygame

class Player(GameObject):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, velocity, screenWidth, screenHeight, frameRate, patchNumbers, animationFrameRate):
        super().__init__(velocity)

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.frameRate = frameRate
        self.patchNumbers = patchNumbers
        self.animationFrameRate = animationFrameRate
        
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

        if self.animationFrameRate <= 60:
                self.animationFrameRate += 1
        else:
                self.animationFrameRate = 1

        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
            self.direction = 'l'

            if self.animationFrameRate%3 == 0:
                if self.patchNumbers['l'] <= 4:
                    self.image = pygame.image.load(f"Assets\\Left\\{self.patchNumbers['l']}.png")
                    self.patchNumbers['l'] += 1
                else:
                    self.patchNumbers['l'] = 1
                    self.image = pygame.image.load(f"Assets\\Left\\{self.patchNumbers['l']}.png")
                    self.patchNumbers['l'] += 1

        if keys[pygame.K_d]:
            self.rect.x += self.velocity
            self.direction = 'r'
            if self.animationFrameRate%3 == 0:
                if self.patchNumbers['r'] <= 4:
                    self.image = pygame.image.load(f"Assets\\Right\\{self.patchNumbers['r']}.png")
                    self.patchNumbers['r'] += 1
                else:
                    self.patchNumbers['r'] = 1
                    self.image = pygame.image.load(f"Assets\\Right\\{self.patchNumbers['r']}.png")
                    self.patchNumbers['r'] += 1
            self.Down = True
            self.Up = False

        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
            self.direction = 'u'

            if self.animationFrameRate%3 == 0:
                if self.patchNumbers['u'] <= 4:
                    self.image = pygame.image.load(f"Assets\\Up\\{self.patchNumbers['u']}.png")
                    self.patchNumbers['u'] += 1
                else:
                    self.patchNumbers['u'] = 1
                    self.image = pygame.image.load(f"Assets\\Up\\{self.patchNumbers['u']}.png")
                    self.patchNumbers['u'] += 1
            self.Up = True
            self.Down = False

        if keys[pygame.K_s]:
            self.rect.y += self.velocity
            self.direction = 'd'

            if self.animationFrameRate%3 == 0:
                if self.patchNumbers['d'] <= 4:
                    self.image = pygame.image.load(f"Assets\\Down\\{self.patchNumbers['d']}.png")
                    self.patchNumbers['d'] += 1
                else:
                    self.patchNumbers['d'] = 1
                    self.image = pygame.image.load(f"Assets\\Down\\{self.patchNumbers['d']}.png")
                    self.patchNumbers['d'] += 1
            self.Right = True
            self.Left = False

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

    def bulletCollide(self, viruses):
        for bullet in self.bullets:
            for virus in viruses:
                if pygame.Rect.colliderect(bullet.rect, virus.rect):
                    self.bullets.remove(bullet)
                    virus.reset()

    def isInfected(self, viruses):
        for virus in viruses:
            if pygame.Rect.colliderect(virus.rect, self.rect):
                return True
            
        return False

    def reset(self):
        self.rect.x = (self.screenWidth / 2) - (self.rect.width / 2)
        self.rect.y = (self.screenHeight / 2) - (self.rect.height / 2)

        self.bullets = pygame.sprite.Group()
        self.direction = 'u'
        self.shootKeyPressed = False

    def update(self, screen, viruses):
        super().update()
        self.move()
        self.shoot(screen)
        self.bullets.update()
        self.filterBullets()
        self.bulletCollide(viruses)

    def draw(self, screen, viruses):
        screen.blit(self.image, self.rect)
        self.update(screen, viruses)
    
