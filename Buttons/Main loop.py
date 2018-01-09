import pygame
from Mouse_and_Burttons import *

# initialize the game engine
pygame.init()
myfont = pygame.font.SysFont("Bookman Old Style",10)

#create window
screen = pygame.display.set_mode((700,500))
screen.fill((0,200,50))

# set window caption
pygame.display.set_caption("Test window")



MOUSE = Mouse()
# adding the items to the machines outcome invent to take
group = pygame.sprite.Group()
ag = pygame.sprite.Group() # accepters group

fb = Parent_accepter(MOUSE,[0,110])
ag.add(fb)
fb = Parent_accepter(MOUSE,[50,110])
ag.add(fb)



text = myfont.render("Burgers: ",False,(0,0,0))
screen.blit(text,[90,90])
fm = Filtered_mover(MOUSE,ag,[100,100])
group.add(fm)

clock = pygame.time.Clock()


# ------ game loop ------
game = True
while game:

    # checks for keys pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # this code did not have to change. Made sure of it.
            collide = pygame.sprite.spritecollide(MOUSE,group,False)
            for i in collide:
                i.interaction()
                
            


    screen.fill((0, 200, 50))


    #updates
    MOUSE.update()
    ag.draw(screen)
    group.draw(screen)
    screen.blit(text,[90,80])
    
    
    # update the screen with that weve done
    pygame.display.flip()
    # fps cap
    clock.tick(60)


# quits the game closing the window
pygame.quit()

