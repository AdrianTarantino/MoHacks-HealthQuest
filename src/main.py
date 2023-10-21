# Example file showing a basic pygame "game loop"
import pygame
from Game_Objects.Player import Player
from Game_Objects.Level import Level
from Game_Objects.Virus import Virus

WIDTH = 1280
HEIGHT = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
gameState = "start"
startButton = [290, 510, 420, 120]
helpButton = [10, 10, 120, 120]
backButton = [10, 700, 200, 75]
reddish = 'red'
orangish = '#ffb300'
arialFont = pygame.font.SysFont("Arial", 120, True, False)
backFont = pygame.font.SysFont("Arial", 60, "white")
fontRenders = {"titleFont1" : arialFont.render("HEALTHCARE", 1, "white"),
               "titleFont2" : arialFont.render("HUSTLE", 1, "white"),
               "pauseFont1" : arialFont.render("PAUSE", 1, "white"),
               "pauseFont2" : arialFont.render("SCREEN", 1, "white"),
               "startFont" : arialFont.render("START", 1, "white"),
               "helpFont" : arialFont.render("?", 1, "white"),
               "backFont" : backFont.render("BACK", 1, "white")}

player = Player(5, WIDTH, HEIGHT)
testVirus = Virus(13, WIDTH, HEIGHT)

CamX = player.rect.x
CamY = player.rect.y

testLevelImage = "MapMaterials\Spawn.png"
testLevel = pygame.image.load(testLevelImage)

while running:
    ev = pygame.event.poll()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
        
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
        screen.blit(fontRenders['helpFont'], (30, 5))
        screen.blit(fontRenders['startFont'], (305, 505))
        screen.blit(fontRenders['titleFont1'], (100, 150))
        screen.blit(fontRenders['titleFont2'], (255, 270))

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

        screen.blit(fontRenders['backFont'], (25, 705))

    elif gameState == "gaming":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                gameState = 'pause'

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("purple")
        # testLevel.draw(screen)
        screen.blit(testLevel, ((WIDTH / 2) - (testLevel.get_width() / 2), (HEIGHT / 2) - (testLevel.get_height() / 2)))

        # RENDER YOUR GAME HERE
        player.draw(screen)
        testVirus.draw(screen)

    elif gameState == "pause":
        screen.fill("red")

        screen.blit(fontRenders['pauseFont1'], (300, 50))
        screen.blit(fontRenders['pauseFont2'], (245, 170))

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
               gameState = 'gaming'

    else:
        print('brooo')
        pygame.time.wait(1000)
        gameState = "start"

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
