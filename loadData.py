import pygame
import os
from os import *


#Deals with loading images etc into the game
class LoadData(object):

    def __init__(self):
		
        self.pngArray = []
        self.surfaceinfoArray = []
        self.getpngFilenames()        
    
		
    def getpngFilenames(self):
                
        print(os.listdir("images"))
        temparray = os.listdir("images")

                
        for i in range(0, len(temparray)-1, 1):
            if temparray[i][-3:] == "png":
                self.pngArray.append(temparray[i])

        for i in self.pngArray:
            self.surfaceinfoArray.append(self.makeSurfaces(i))
       
        print(self.surfaceinfoArray)

    def makeSurfaces(self, name):
        temp = []
        surface = pygame.image.load("images/" + name)

        temp.append(surface)
        temp.append(surface.get_rect(center =(36, 36)))
        temp.append(pygame.mask.from_surface(surface))
        return temp


a = LoadData()

