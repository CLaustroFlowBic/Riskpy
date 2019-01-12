import pygame 	
import loadData
from EventManager import *


#should be all the data associated with the current game

#model has the current selection
class GameEngine(object):

    def __init__(self, evManager, loadData):

        self.evManager = evManager
        evManager.RegisterListener(self)
        self.running = False
        self.loadData = loadData
        #make phase and such go here
        self.phase = 'mainmenu'
        self.gamePhase = 0 
        self.players = []
        self.turn = 0
        
    def notify(self, event):

        if isinstance(event, QuitEvent):
            self.running = False

    def run(self):

        self.running = True
        self.evManager.Post(InitializeEvent())
        
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)
            
    def nextButtonCollide(self, colliding):
        
        self.loadData.nextButton.rollover = colliding
    def nextPhase(self):
        print("next Phase")
    
    def getPlayers(self, array):
    
        for i in range(len(array)):
            self.players.append (Player(i+ 1, array[i]))
            
        self.updateTurn()
        
    def updateTurn(self):
    
        if self.turn == len(self.players):
            self.turn =1
        else:
            self.turn += 1
        for i in self.players:
            i.updateSelection(self.turn)
       
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
    def __init__(self, id, color):
        self.id = id
        self.surface = pygame.Surface((50,50))
        self.dest = (id * 50, 500)
        self.color = self.checkColor(color)
        self.surface.fill(self.color)

        self.continentsOwned = []
        
        #potentially split this into different arrays for the differnt cards
        self.cards = []
        
    def updateSelection(self, turn):
        print(turn, self.id)
        if self.id == turn:
            
            self.surface.fill((255,255,255), self.surface.get_rect().inflate(-10,-10))
        else:
            self.surface.fill(self.color)
    def checkColor(self, color):
        if color == "red":
            return((255, 0 , 0))
        elif color == "blue":
            return((0, 0, 255))
        elif color == "pink":
            return((200, 100, 0))
        elif color == "teal":
            return ((0, 200, 100))
    
#game CLASS
# needs to know what phase the game is in, does it need to know the player
# - menu, options ( should just extend the menu ), player selection
# - put down units phase until last unit
# - turn one player one, im guessing
#       - recieve units, they decied where to put them
#       - preform attacks
#       - fortify, which means moving armies form one and only one position, to another adjacent tile

#lass Phase():


#class Fortify(Phase):
   # def __init__(self):
   #    self.phase
#class Attack(Phase):

#class Placing(Phase):

        
        
        
        
        
        
        