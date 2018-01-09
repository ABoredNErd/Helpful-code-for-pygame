import pygame as pg


# ------ mover classes --------
class Parent_mover(pg.sprite.Sprite):
    def __init__(self,MOUSE,location = [0,0], size = [20,20]):
        super().__init__()

        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()

        # attributes that the classe needs to work.
        self.MOUSE = MOUSE
        self.defualt_location = location

        
        self.update(location)

    def interaction(self):
        if self.MOUSE.moving != None:
            self.MOUSE.moving = None
        else:
            self.MOUSE.moving = self.update
    
    # will change the location to location passed to it
    def update(self,location):
        self.rect.x, self.rect.y = location[0],location[1]

class Filtered_mover(Parent_mover):
    def __init__(self, MOUSE, accepter, location = [0,0], size = [20,20]):
        super().__init__(MOUSE,location = location, size = size)
        self.accepter = accepter

    def interaction(self):
        collide =pg.sprite.spritecollide(self.MOUSE, self.accepter, False)
        if self.MOUSE.moving != None and collide != []:
            self.MOUSE.moving = None
            for s in collide:
                self.defualt_location = [s.rect.x + 10,s.rect.y + 10]
                self.update(self.defualt_location)
            
        elif self.MOUSE.moving == None:
            super().interaction()
        else:
            self.update(self.defualt_location)
            self.MOUSE.moving = None
            


# ------ accepter classes --------
# location to place the parent_mover
class Parent_accepter(pg.sprite.Sprite):
    def __init__(self,MOUSE,location = [0,0], size = [40,40]):
        # Makes the sprite
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill((200,0,0))
        self.rect = self.image.get_rect()
        
        self.MOUSE = MOUSE
        self.location = location


        self.update(location)        

      
    def interaction(self):
        if self.MOUSE.moving != None:
            self.MOUSE.moving([self.rect.x + 5, self.rect.y + 5])
        
    

    # allows the player to change the location or the collour of the accepter.
    def update(self,location = False, colour = False):
        if location != False:
            self.rect.x, self.rect.y = location[0],location[1]
            self.location = location
        if colour != False:
            self.image.fill(colour)




# ------- Mouse class ------ 
class Mouse(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() # runs the builder of the sprite class
        self.image = pg.Surface([1,1])
        self.rect = self.image.get_rect()

        self.moving = None # for when moving a sprite.
        

    def update(self):
        # get location of the mouse
        location = pg.mouse.get_pos()
        # change location of the sprite to the mouse position
        self.rect.x = location[0]
        self.rect.y = location[1]
        if self.moving != None:
             self.moving([self.rect.x-1,self.rect.y-1])



"""
very basic system. No need to change the mouse interaction code in the main loop.
Mouse code however does need to be changed, however only 3 lines are added. 


When it comes to group you have two options. The first is add them to the main buttons group. Or you could create a new group for movers, however I do
not see a need for this. Just have a group for all sprites on the game screen. All groups can use the basic interaction code with the mouse in the main
loop as long as there interaction code DOES NOT require paremeters.

You can fix this issue of paramters by setting the paremters in the builder method and then store them with self.NAMEofVARIABLE to be used later on.

"""
