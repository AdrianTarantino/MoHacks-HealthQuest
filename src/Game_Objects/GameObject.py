import pygame

class GameObject(pygame.sprite.Sprite):
    
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, velocity):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.velocity = velocity

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([50, 50])
        self.image.fill("white")

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        super().update(self)

        