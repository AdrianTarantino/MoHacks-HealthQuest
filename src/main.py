# Example file showing a basic pygame "game loop"
import pygame
from Game_Objects.Player import Player


WIDTH = 1000
HEIGHT = 800
TestLevel = pygame.image.load("MapMaterials\Spawn.png")


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
Levels = [TestLevel]

player = Player("white", 50, 50, 5, WIDTH, HEIGHT)

CamX = player.rect.x
CamY = player.rect.y

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()


    if player.rect.x >  WIDTH/10 *6:
        player.velocity = 5
        if(player.Right == True):
            CamX += 5
            player.velocity = 0
        if(keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s]):
            player.velocity = 5
            CamX -= 0
    elif player.rect.x <  HEIGHT/10 *4:
        player.velocity = 5
        if(player.Left == True):
            CamX -= 5
            player.velocity = 0
        if(keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
            player.velocity = 5
            CamX += 0
    elif player.rect.y > WIDTH/10 * 6:
        player.velocity = 5
        if(player.Down == True):
            CamY += 5
            player.velocity = 0
        if(keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_d]):
            player.velocity = 5
            CamY -= 0
        if(keys[pygame.K_a] and keys[pygame.K_d] and keys[pygame.K_w]):
            player.velocity = 5
            CamY = 0
    elif player.rect.y <  HEIGHT/10 *4:
        player.velocity = 5
        if(player.Up == True):
            CamY -= 5
            player.velocity = 0
        if(keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s]):
            player.velocity = 5
            CamY += 0
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(TestLevel, (1100 -CamX *2,790 -CamY *2))
    #screen.blit(TestLevel, (player.rect.x -CamX, player.rect.y -CamY)) COME BACK TO THE MOVEMENT THINGY


    # RENDER YOUR GAME HERE
    player.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
