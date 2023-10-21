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
gameState = "start"
startButton = [200, 480, 400, 100]
helpButton = [10, 10, 100, 100]
backButton = [10, 515, 200, 75]
reddish = 'red'
orangish = '#ffb300'
arialFont = pygame.font.SysFont("Arial", 90, True, False)
backFont = pygame.font.SysFont("Arial", 60, "white")
fontRenders = {"titleFont1" : arialFont.render("HEALTHCARE", 1, "white"),
               "titleFont2" : arialFont.render("HUSTLE", 1, "white"),
               "startFont" : arialFont.render("START", 1, "white"),
               "helpFont" : arialFont.render("?", 1, "white"),
               "backFont" : backFont.render("BACK", 1, "white")}

Levels = [TestLevel]
player = Player("white", 50, 50, 5, WIDTH, HEIGHT)

CamX = player.rect.x
CamY = player.rect.y

while running:
    ev = pygame.event.poll()
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
        
    mousePos = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePos[0], mousePos[1], 1, 1)

    if gameState == "start":

        if mouseRect.colliderect(startButton):
            # highlights the button as the mouse is hovering it
            reddish = "#bd0000"
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # sends you to the main game after clicking the button
                gameState = "gaming"
        elif mouseRect.colliderect(helpButton):
            # highlights the button as the mouse is hovering it
            orangish = "#d69702"
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # sends you to the help screen
                gameState = "help"
        else:
            reddish = "red"
            orangish = '#ffb300'

        # fill the screenskie
        screen.fill("blue")

        # displaying stuff
        pygame.draw.rect(screen, reddish, startButton)
        pygame.draw.rect(screen, orangish, helpButton)
        screen.blit(fontRenders['helpFont'], (30, 10))
        screen.blit(fontRenders['startFont'], (250, 480))
        screen.blit(fontRenders['titleFont1'], (100, 150))
        screen.blit(fontRenders['titleFont2'], (220, 250))

    elif gameState == "help":
        orangish = '#ffb300'

        if mouseRect.colliderect(backButton):
            # highlights the button as the mouse is hovering it
            orangish = "#d69702"
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # sends you to the main game after clicking the button
                gameState = "start"
        else:
            orangish = '#ffb300'

        screen.fill("green")
        pygame.draw.rect(screen, orangish, backButton)
        screen.blit(fontRenders['backFont'], (25, 520))
        

    elif gameState == "gaming":

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        screen.blit(TestLevel, (1100 -CamX *2,790 -CamY *2))
        player.draw(screen)

    else:
        gameState = "start"

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
