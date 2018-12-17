import pygame 	

from EventManager import *


#should be all the data associated with the current game

#model has the current selection
class GameEngine(object):

    def __init__(self, evManager):

        self.evManager = evManager
        evManager.RegisterListener(self)
        self.running = False
        #make phase and such go here
        
        
    def notify(self, event):

        if isinstance(event, QuitEvent):
            self.running = False

    def run(self):

        self.running = True
        self.evManager.Post(InitializeEvent())
        
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)
       
    #VARIABLE
    # need to have some grid like data structure loaded in so we can check if the player is selecting an adjacent tile

    # Territory CLASS
    # the model here needs to have all of the territories 
    #needs to store information about the territories
    # - what contient, - how many troops, does it need to know which player it is apart of, 
    # how many armies they give

class Territory():
    def __init__(self):
        
        self.id
        self.name
        self.continent
        self.armies
        self.income
        
#player CLASS
# all need to have data associated with them 
# - turn order, - what contients they own, - cards they have
class Player():
    def __init__(self):
        self.id
        self.turnNumber
        self.color
        self.continentsOwned = []
        
        #potentially split this into different arrays for the differnt cards
        self.cards = []

    
#game CLASS
# needs to know what phase the game is in, does it need to know the player
# - menu, options ( should just extend the menu ), player selection
# - put down units phase until last unit
# - turn one player one, im guessing
#       - recieve units, they decied where to put them
#       - preform attacks
#       - fortify, which means moving armies form one and only one position, to another adjacent tile
    
class Game():
    def __init__(self):
       self.phase
        
        
        
        
        
        
        