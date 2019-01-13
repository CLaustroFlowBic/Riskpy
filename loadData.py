import pygame
import os
#from os import *
import json

PLACING = 0 
SELECTING = 1
#Deals with loading images etc into the game
class LoadData(object):

    def __init__(self):
    
        #note: position data is the middle of the image
        with open('xyData.json', "r") as f:
            data = json.load(f)
            self.x = data["x"]
            self.y = data["y"]
        
        #names of the files
        self.pngArray = []
        
        #Territory image data
        self.Territories = []
        
        self.phase = []
        self.phasePos = [(400, 500), (500, 500), (600, 500), (700, 500)]
        self.phaseIndicator = None
    
        self.nextButton = None
        
        self.playButton = None
        self.title = ""
        self.loadButtons()
        self.getpngFilenames()
        
        self.playerSelectButtons = []
        self.loadPlayerSelect()
        
        
    def loadButtons(self):
        
        self.phase = [pygame.image.load("buttons/fortify.png"),
        pygame.image.load("buttons/attack.png"),
        pygame.image.load("buttons/placing.png")]
        self.phaseIndicator = pygame.image.load("buttons/selected.png")
        
        self.title = pygame.image.load("buttons/Title.png")
        
        self.nextButton = Button(pygame.image.load("buttons/next.png"), 
                                pygame.image.load("buttons/next.png").get_rect(topleft = (700, 500)),
                                (700, 500), "next",
                                pygame.image.load("buttons/nextrollover.png"))
       
        
        
        self.playButton = Button (pygame.image.load("buttons/play.png"),
                                pygame.image.load("buttons/play.png").get_rect(topleft = (270,300)),
                                (270, 300), "play",
                                 pygame.image.load("buttons/playrollover.png"))
        
    def loadPlayerSelect(self):
        self.redPlayerButton = Button(pygame.image.load("buttons/redUnselected.png"), 
                                    pygame.image.load("buttons/redUnselected.png").get_rect(topleft = (100,100)),
                                    (100,100), "red",
                                    pygame.image.load("buttons/redRollover.png"),
                                    pygame.image.load("buttons/redSelected.png"))
                                    
        self.bluePlayerButton = Button(pygame.image.load("buttons/blueUnselected.png"), 
                                    pygame.image.load("buttons/blueUnselected.png").get_rect(topleft = (100,200)),
                                    (100,200), "blue",
                                    pygame.image.load("buttons/blueRollover.png"),
                                    pygame.image.load("buttons/blueSelected.png"))
       
        self.pinkPlayerButton = Button(pygame.image.load("buttons/pinkUnselected.png"), 
                                    pygame.image.load("buttons/pinkUnselected.png").get_rect(topleft = (200,100)),
                                    (200,100), "pink",
                                    pygame.image.load("buttons/pinkRollover.png"),
                                    pygame.image.load("buttons/pinkSelected.png"))
                                        
        self.tealPlayerButton = Button(pygame.image.load("buttons/tealUnselected.png"), 
                                    pygame.image.load("buttons/tealUnselected.png").get_rect(topleft = (200,200)),
                                    (200,200),"teal",
                                    pygame.image.load("buttons/tealRollover.png"),
                                    pygame.image.load("buttons/tealSelected.png"))
                                    
        self.playerSelectButtons = [self.redPlayerButton, self.bluePlayerButton, self.pinkPlayerButton, self.tealPlayerButton]
    def get_Territories(self):
        
        return Territories
        
    def getpngFilenames(self):
        """Gets the image files and loads them into Territories with positions
        NOTE: image data (.png's and positions) have previously been sorted"""
        
        #gets all the files in directory "images"
        temparray = os.listdir("images")

        #goes through "images" directory
        for i in range(0, len(temparray)-1, 1):
            
            #checks if it is of .png type
            if temparray[i][-3:] == "png":
                self.pngArray.append(temparray[i])
        self.pngArray.sort()
        
       
        
        #goes thorugh all .png files and makes them into territories
        for i in range(0, len(self.pngArray), 1):
            self.Territories.append(self.makeSurfaces(self.pngArray[i], (self.x[i] - self.x[0]), (self.y[i] - self.y[0])))

    #!Change name to make more descriptive!
    def makeSurfaces(self, name, x, y):
        """Loads an image from image folder with specified name makes into Territory objects"""
        
        surface = pygame.image.load("images/" + name)
        
        # gets the top left corner of the image starting at the middle
        #also offset so it is on the visible area
        x = x - surface.get_width()/2 + 50
        y = y - surface.get_height()/2 + 80
        
        #makes a territory
        territory = Territory(surface, surface.get_rect(topleft = (x, y)), pygame.mask.from_surface(surface, 50), name[3:-4], x, y)
        
        return territory


class Button():
    def __init__(self, surface, rect, position, name, rolloverImage = None, selectedImage = None):
    
        #make a redirect to image does not exits
        self.images = [surface]
        if rolloverImage != None:
            self.images.append(rolloverImage)
        if selectedImage != None:
            self.images.append(selectedImage)
        self.imageLength = len(self.images)
        self.state = 0
        self.rect = rect
        self.name = name
        self.position = position
        
        
    def get_image(self):
        return self.image
        
    def display(self, screen):
        screen.blit(self.images[self.state], self.position)
        
        
    def collision (self, event, pos, callback, parameter = None):
        """Changes image depending on collision state and returns a callback if selected /n callback is optional"""
        
        #Checks if colliding with mouse
        if (self.get_rect().collidepoint(*pos)):
            
            #checks if a rollover exists
            if(self.imageLength >= 2) and self.state != 2:
                self.state = 1
            
            #checks mousedown Event 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #checks if a selected image exits
                if self.imageLength >= 3:
                    
                    #Checks if already pressed if it is go back to state 0
                    if self.state == 2:
                        #change this to one if unselection looks werid
                        self.state = 1
                    #if not go to state 3 selected
                    else:   
                        self.state = 2
                if parameter == None:
                
                    return callback()
                else:
                    return callback(parameter)
        else:
            if self.state == 2:
                self.state = 2
            else:
                self.state = 0
        
    
    def get_name(self):
        return self.name
    def get_rect(self):
        return self.rect
        
class Territory(Button):
    def __init__(self, surface, rect, mask, name, x, y, rolloverImage = None, selectedImage = None):
        Button.__init__(self, surface, rect, (x, y), name,  rolloverImage, selectedImage)
        self.x = x
        self.y = y
        self.surface = surface
        self.rect = rect
        self.mask = mask
        self.name = name
    
    def state(self, context, callback):
        #placing = 0 
        #selecing = 1
    
        if context == PLACING:
            #depending on how this happens could be a callback or just return the id
            return callback
        if context == SELECTING:
            pass
    
    def collision (self, event, pos, callback, parameter = None):
        """dealing with the collision between the territory and mouse"""
        posInMask = pos[0] - self.get_rect().x, pos[1] - self.get_rect().y
        touching = self.get_rect().collidepoint(*pos) and self.get_mask().get_at(posInMask)
        if (touching and event.type == pygame.MOUSEBUTTONDOWN):
            callback(parameter)
                
    
    
    def get_surface(self):
        return self.surface
        
    def get_rect(self):
        return self.rect
        
    def get_mask(self):
        return self.mask 
        
    def get_name(self):
        return self.name
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y  
    def get_name(self):
        return self.name
    #needs collison context, either saving into memory and using for something
    #or placing which means just one pressing on the territory 
            


