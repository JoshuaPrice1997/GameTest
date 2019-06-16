# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720))
    x = y = 100
     
    # define a variable to control the main loop
    running = True
    player = pygame.image.load('idle1.png').convert()
    background = pygame.image.load('adelaide.jpg').convert()
    screen.blit(background,(0,0))
    screen.blit(player,(x,y))
    print(background)
    # main loop
    while running:
        screen.blit(background,(0,0))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:y -= 10
        if key[pygame.K_a]:x -= 10
        if key[pygame.K_d]:x += 10
        if key[pygame.K_s]:y += 10
        screen.blit(player,(x,y))
        pygame.display.update()
        pygame.time.delay(100)

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()