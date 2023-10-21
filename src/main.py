# Example file showing a basic pygame "game loop"
import pygame
from Game_Objects.Player import Player
from Game_Objects.Level import Level
from Game_Objects.Virus import Virus

WIDTH = 800
HEIGHT = 600

# pygame setup
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Assets\\music\\backgroundSong (fast).mp3") 
pygame.mixer.music.play(-1,0.0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
pauseState = ''
BossAlive = True
gameState = "start"
score = 0
startButton = [WIDTH * 290/1000, HEIGHT * 7/10, WIDTH * 420/1000, HEIGHT * 140/1000]
helpButton = [10, 10, 70, 70]
backButton = [10, 540, 180, 50]
reddish = 'red'
orangish = '#ffb300'
arialFont = pygame.font.SysFont("Arial", int (WIDTH * 120/1000), True, False)
backFont = pygame.font.SysFont("Arial", int (WIDTH * 60/1000), True, False)
helpFont = pygame.font.SysFont("Arial", 70, True, False)
fontRenders = {"titleFont1" : arialFont.render("HEALTHCARE", 1, "white"),
               "titleFont2" : arialFont.render("HUSTLE", 1, "white"),
               "pauseFont1" : arialFont.render("PAUSE", 1, "white"),
               "pauseFont2" : arialFont.render("SCREEN", 1, "white"),
               "startFont" : arialFont.render("START", 1, "white"),
               "helpFont" : helpFont.render("?", 1, "white"),
               "backFont" : backFont.render("BACK", 1, "white"),
               "youDied" : arialFont.render("YOU DIED", 1, "red")}

player = Player(7, WIDTH, HEIGHT, 1, {'d' : 1, 'u' : 1, 'r' : 1, 'l' : 1}, 1)
viruses = pygame.sprite.Group()
viruses.add(Virus(8, WIDTH, HEIGHT),
            Virus(8, WIDTH, HEIGHT),
            Virus(8, WIDTH, HEIGHT),
            Virus(8, WIDTH, HEIGHT))

scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
highscoreFont = backFont.render(f"HIGHSCORE: {player.highscore[0]}", 1, "red")

CamX = player.rect.x
CamY = player.rect.y

testLevelImage = "MapMaterials\Spawn.png"
testLevel = pygame.image.load(testLevelImage)
hallwaySplit = pygame.image.load("MapMaterials\VerticleSplitPath.png")
Cluster = pygame.image.load("MapMaterials\Exam Room Cluster.png")
PathWBranch = pygame.image.load("MapMaterials\PathWithBranch.png")
triage = pygame.image.load("MapMaterials\Triage Area.png")
BossRoom = pygame.image.load("MapMaterials\BossRoom.png")

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

    if player.rect.x > WIDTH - 40:
        player.rect.x -= player.velocity
    elif player.rect.x < -10:
        player.rect.x += player.velocity
    elif player.rect.y > HEIGHT - 40:
        player.rect.y -= player.velocity
    elif player.rect.y < 0:
        player.rect.y += player.velocity

    if gameState == "start":
        highscoreFont = backFont.render(f"HIGHSCORE: {player.highscore[0]}", 1, "red")
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
        screen.blit(fontRenders['helpFont'], (24, 5))
        screen.blit(fontRenders['startFont'], (startButton[0] + WIDTH * 1/100, startButton[1] - 10))
        screen.blit(fontRenders['titleFont1'], (WIDTH * 1/10, HEIGHT * 150/1000))
        screen.blit(fontRenders['titleFont2'], (WIDTH * 2/10 + WIDTH * 45/800, HEIGHT * 300/1000))
        screen.blit(highscoreFont, (startButton[0] + WIDTH/100, startButton[1] + 100))

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

        screen.blit(fontRenders['backFont'], (backButton[0] + 10, backButton[1]))

    elif gameState == "gaming":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                gameState = 'pause'
                pauseState = "gaming"

        if player.rect.x > 350 and player.rect.x < 522:
            if player.rect.y > 0 and player.rect.y < 46:
                gameState = 'Hallway'
                print("joke that went too far")
                player.rect.x, player.rect.y = (330, 450)

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("purple")
        # testLevel.draw(screen)
        screen.blit(testLevel, ((WIDTH / 2) - (testLevel.get_width() / 2), (HEIGHT / 2) - (testLevel.get_height() / 2)))

        # RENDER YOUR GAME HERE
        player.draw(screen, viruses)
        if player.isInfected(viruses):
            print("dead")
            screen.blit(fontRenders['youDied'], (WIDTH/5, WIDTH/2))
            gameState = "end"

        viruses.draw(screen)
        viruses.update(screen)
        scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
        screen.blit(scoreFont, (5, 5))

    elif gameState == "Hallway":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                    gameState = 'pause'
                    pauseState = "Hallway"
        
        if player.rect.y <= 0 and gameState == "Hallway":
            gameState = 'ExamRoomcluster'
            player.rect.x, player.rect.y = (400, 500)
        
        if player.rect.x >= 600 and gameState == "Hallway":
            gameState = 'Path'
            player.rect.x, player.rect.y = (100, 200)
        
        if player.rect.y >= HEIGHT - 100 and gameState == "Hallway":
            gameState = "gaming"
            player.rect.x, player.rect.y = (350, 45)

        if player.rect.colliderect(0, 0, 245, 600):
            player.rect.x += player.velocity
        elif player.rect.colliderect(510, 405, 320, 10):
            player.rect.y -= player.velocity
        elif player.rect.colliderect(500, 405, 10, 395):
            player.rect.x -= player.velocity
        elif player.rect.colliderect(530, 190, 330, 10):
            player.rect.y += player.velocity
        elif player.rect.colliderect(500, 0, 10, 200):
            player.rect.x -= player.velocity

        screen.fill("black")        
        screen.blit(hallwaySplit, ((WIDTH/2 + 100) - (testLevel.get_width() / 2), (HEIGHT/2 -100) - (testLevel.get_height() / 2)))
        player.draw(screen, viruses)
        scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
        screen.blit(scoreFont, (5, 5))
    
    elif gameState == "ExamRoomcluster":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                    gameState = 'pause'
                    pauseState = "ExamRoomcluster"

        if player.rect.y >= HEIGHT - 100:
            gameState = "Hallway"
            player.rect.x, player.rect.y = (400, 100)

        screen.blit(Cluster, (0,0))
        player.draw(screen, viruses)
        scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
        screen.blit(scoreFont, (5, 5))
    
    elif gameState == "Path":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                    gameState = 'pause'
                    pauseState = "Path"

        if player.rect.x <= 0:
            gameState = "Hallway"
            player.rect.x, player.rect.y = (500, 200)

        if player.rect.y >= 550 and gameState == "Path":
            gameState = "Triage"
            player.rect.x, player.rect.y = (400,50)
        
        if player.rect.x >= 750:
            gameState = "Boss"
            player.rect.x, player.rect.y = (50,300)

        if player.rect.colliderect(0, 0, 800, 150):
            player.rect.y += player.velocity
        elif player.rect.colliderect(0, 380, 250, 10):
            player.rect.y -= player.velocity
        elif player.rect.colliderect(250, 380, 10, 420):
            player.rect.x += player.velocity
        elif player.rect.colliderect(540, 400, 10, 420):
            player.rect.x -= player.velocity
        elif player.rect.colliderect(540, 380, 230, 10):
            player.rect.y -= player.velocity

        screen.blit(PathWBranch, (0,0))
        player.draw(screen, viruses)
        scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
        screen.blit(scoreFont, (5, 5))

    elif gameState == "Triage":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                    gameState = 'pause'
                    pauseState = "Triage"

        if player.rect.x > 260 and player.rect.x < 462 and player.rect.y < 30 and player.rect.y > -10:
            gameState = "Path"
            player.rect.x, player.rect.y = (400,500)

        screen.blit(triage, (0,0))
        player.draw(screen, viruses)
        scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
        screen.blit(scoreFont, (5, 5))

    elif gameState == "Boss":
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                    gameState = 'pause'
                    pauseState = "Boss"

        if BossAlive == False and player.rect.x <= 0:
            gameState = "Path"
            player.rect.x, player.rect.y = (400,500)

        screen.blit(BossRoom, (0,0))
        player.draw(screen, viruses)
        scoreFont = backFont.render(f"SCORE: {player.score}", 1, "#ffc800")
        screen.blit(scoreFont, (5, 5))
    
    elif gameState == "pause":
        screen.fill("red")

        screen.blit(fontRenders['pauseFont1'], (300, 50))
        screen.blit(fontRenders['pauseFont2'], (245, 170))

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
               gameState = pauseState

    else:
        print('brooo')
        pygame.time.wait(1000)
        gameState = "start"

        player.reset()
        for virus in viruses:
            virus.reset()

    # flip() the display to put your work on screen

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()