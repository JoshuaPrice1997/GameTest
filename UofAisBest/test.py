import pygame
import numpy as np
import pandas as panda

def main():
     
    # initialize the pygame module
    pygame.init()
    #THE LOGO IS CURRENTLY EXPLICIT
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("")
     
    #Default window size 720p
    screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    #Keeps track of window size
    MAXX = 1280
    MAXY = 720
    #default player position
    x = y = 100
    #keeps track of game state
    state = 0
    running = True
    #importing assets
    tiles = loadTiles()
    text = loadText()
    print(text)
    player = pygame.image.load('idle1.png').convert()
    background = pygame.image.load('adelaide.jpg').convert()
    background = pygame.transform.scale(background,(1280,720))
    mapo = np.loadtxt('map.txt',usecols=range(5))

    graphics = panda.DataFrame(data = {player,background},index=['player','background'])

    while running:
        #loading current key presses
        key = pygame.key.get_pressed()

        #Checking for certain events
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                running = False
            #resize window
            if event.type == pygame.VIDEORESIZE:
                #changing parameters
                surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
                #updating background
                background = pygame.transform.scale(background,(event.w,event.h))
                #Updating parameters
                MAXX = event.w
                MAXY = event.h
        
        if state == 0:
            #---------------------#
            #Menu state
            #---------------------#
            fontSize = int(MAXY/20)
            welcome = pygame.transform.scale(text[0]['welcome'],(int(fontSize*42/8),fontSize))
            enter = pygame.transform.scale(text[0]['enter'],(int(fontSize*42/16),int(fontSize/2)))
            screen.blit(welcome,(MAXX/2-int(fontSize*42/16),MAXY/2-fontSize/2))
            screen.blit(enter,(MAXX/2-int(fontSize*42/32),MAXY/2+fontSize*2-fontSize/2))
            #chane to game state
            if key[pygame.K_RETURN]:state += 1


        if state == 1:
            #---------------------#
            #Game State
            #---------------------#
            screen.blit(background,(0,0))
            screen.blit(player,(x,y))
            #basic movement
            if key[pygame.K_w]:y -= 10
            if key[pygame.K_a]:x -= 10
            if key[pygame.K_d]:x += 10
            if key[pygame.K_s]:y += 10

        #Quit game
        if key[pygame.K_ESCAPE]:sys.exit

        #Input Lag
        pygame.time.delay(10)

        #Animate
        pygame.display.update()

# def loadGraphics():
#     player = pygame.image.load('idle1.png').convert()
#     background = pygame.image.load('adelaide.jpg').convert()
#     background = pygame.transform.scale(background,(1280,720))
#     welcome = pygame.image.load('welcome.png').convert()
#     grass = pygame.transform.scale(pygame.image.load('grass.png').convert(),(128,128))
#     path = pygame.transform.scale(pygame.image.load('path.png').convert,(128,128))
#     enter = pygame.image.load('enter.png').convert()

def loadTiles():
    tiles = panda.DataFrame()
    tileDat = np.genfromtxt('tiles.txt',usecols=range(2),dtype=str)
    for i in range(tileDat.shape[0]):
        temp = panda.DataFrame(data={pygame.transform.scale(pygame.image.load(tileDat[i][1]+'.png').convert(),(128,128))},index=[tileDat[i][1]])
        tiles = tiles.append(temp)
    return tiles

def loadText():
    text = panda.DataFrame()
    textDat = np.genfromtxt('text.txt',usecols=range(2),dtype=str)
    print(textDat.shape)
    for i in range(textDat.shape[0]):
        temp = panda.DataFrame(data={pygame.image.load(textDat[i][1]+'.png').convert()},index=[textDat[i][1]])
        text = text.append(temp)
    return text


     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()