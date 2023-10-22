from Game_Objects.GameObject import GameObject
import pygame

class BossVirus(GameObject):
    def __init__(self, velocity, health, screenWidth, screenHeight):
        super().__init__(velocity)

        self.health = health

        self.image = pygame.image.load("Assets\\Viruses\\monster_tentackle.png")
        self.rect = self.image.get_rect()
        self.rect.x = (screenWidth / 2) - (self.rect.width / 2)
        self.rect.y = (screenHeight / 2) - (self.rect.height / 2)

    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False
    
    def move(self, playerX, playerY):
        if self.health <= 250: 
            self.velocity += 0.01
        if playerX > self.rect.x:
            self.rect.x += self.velocity
        if playerX < self.rect.x:
            self.rect.x -= self.velocity
        if playerY > self.rect.y:
            self.rect.y += self.velocity
        if playerY < self.rect.y:
            self.rect.y -= self.velocity

    def checkCollision(self, player):
        for bullet in player.bullets.sprites():
            if pygame.Rect.colliderect(bullet.rect, self.rect):
                player.bullets.remove(bullet)
                self.health -= 25

    def update(self, player):
        super().update()
        self.move(player.rect.x, player.rect.y)
        self.checkCollision(player)

    def draw(self, screen, player):
        self.update(player)
        screen.blit(self.image, self.rect)
