import pygame
import os
#from os import *
import json


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
        self.phasePos = [(400, 500), (500, 500), (600, 500)]
        self.loadButtons()
        self.getpngFilenames()
        
        
    def loadButtons(self):
        
        self.phase = [pygame.image.load("buttons/fortify.png"),
        pygame.image.load("buttons/attack.png"),
        pygame.image.load("buttons/placing.png")]
        
        
        
        
    
    def get_Territories(self):
        
        return Territories
        
    def getpngFilenames(self):
        """Gets the image files and loads them into Territories with positions"""
        
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

        # NOTE: image data (.png's and positions) have previously been sorted

    def makeSurfaces(self, name, x, y):
        
        surface = pygame.image.load("images/" + name)
        
        # gets the top left corner of the image starting at the middle
        #also offset so it doesn't look weird
        x = x - surface.get_width()/2 + 50
        y = y - surface.get_height()/2 + 80
        
        #makes a territory
        territory = Territory(surface, surface.get_rect(topleft = (x, y)), pygame.mask.from_surface(surface, 50), name[3:-4], x, y)
        
        return territory



class Territory(object):
    """Territory class contains data: image, position, name , rect, collision/mask"""
    def __init__(self, surface, rect, mask, name, x, y):
        self.x = x
        self.y = y
        self.surface = surface
        self.rect = rect
        self.mask = mask
        self.name = name
        
        
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
        



