import pygame
import os
from os import *


#Deals with loading images etc into the game
class LoadData(object):

    def __init__(self):

        self.alx = 100
        self.aly = 100
        self.xy = [[self.alx, self.aly], 
                    [self.alx + 58, self.aly - 10],
                    [self.alx + 65, self.aly + 47],
                    [self.alx + 129, self.aly + 47],
                    [self.alx + 73, self.aly + 98],
                    [self.alx + 116, self.aly + 100],
                    [self.alx + 83, self.aly + 158],
                    [self.alx + 176, self.aly + 44],
                    [self.alx + 225, self.aly - 43]]
        self.pngArray = []
        self.Territories = []
        self.getpngFilenames()
        
    def get_Territories(self):
        return Territories
    def getpngFilenames(self):
        
        print(os.listdir("images"))
        temparray = os.listdir("images")


        for i in range(0, len(temparray)-1, 1):
            if temparray[i][-3:] == "png":
                self.pngArray.append(temparray[i])

        for i in range(0, len(self.pngArray), 1):
            self.Territories.append(self.makeSurfaces(self.pngArray[i], self.xy[i][0], self.xy[i][1]))

        print(self.Territories)

    def makeSurfaces(self, name, x, y):
        
        surface = pygame.image.load("images/" + name)
        territory = Territory(surface, surface.get_rect(topleft = (x, y)), pygame.mask.from_surface(surface, 50), name[2:-4], x, y)
        print(name)
        
        return territory



class Territory(object):

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


a = LoadData()

