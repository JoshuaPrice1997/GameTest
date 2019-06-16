# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    MAXX = 1280
    MAXY = 720
    x = y = 100
    state = 0
    # define a variable to control the main loop
    running = True
    player = pygame.image.load('idle1.png').convert()
    background = pygame.image.load('adelaide.jpg').convert()
    background = pygame.transform.scale(background,(1280,720))
    welcome = pygame.image.load('welcome.png').convert()
    enter = pygame.image.load('enter.png').convert()
    #screen.blit(background,(0,0))
    #screen.blit(player,(x,y))
    # main loop
    while running:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
                background = pygame.transform.scale(background,(event.w,event.h))
                MAXX = event.w
                MAXY = event.h
        
        if state == 0:
            fontSize = int(MAXY/20)
            welcome = pygame.transform.scale(welcome,(int(fontSize*42/8),fontSize))
            enter = pygame.transform.scale(enter,(int(fontSize*42/16),int(fontSize/2)))
            screen.blit(welcome,(MAXX/2-int(fontSize*42/16),MAXY/2-fontSize/2))
            screen.blit(enter,(MAXX/2-int(fontSize*42/32),MAXY/2+fontSize*2-fontSize/2))
            if key[pygame.K_RETURN]:state += 1
        if state == 1:
            screen.blit(background,(0,0))
            screen.blit(player,(x,y))
        
        if key[pygame.K_w]:y -= 10
        if key[pygame.K_a]:x -= 10
        if key[pygame.K_d]:x += 10
        if key[pygame.K_s]:y += 10
        
        pygame.time.delay(100)
        pygame.display.update()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()