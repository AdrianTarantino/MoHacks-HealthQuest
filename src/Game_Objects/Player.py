import pygame

class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       self.velocity = 5
       self.Left = False
       self.Right = False
       self.Up = False
       self.Down = False 


       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
            self.Left = True
            self.Right = False
        if keys[pygame.K_d]:
            self.rect.x += self.velocity
            self.Right = True
            self.Left = False
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
            self.Up = True
            self.Down = False
        if keys[pygame.K_s]:
            self.rect.y += self.velocity
            self.Up = False
            self.Down = True

    def update(self):
        super().update(self)

        self.movement()

    def draw(self, screen):
        self.update()
        screen.blit(self.image, self.rect)