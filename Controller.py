import pygame 
import Model 
import loadData
from loadData import LoadData
from EventManager import *


class Controller(object):

    def __init__(self, evManager, model, loadData):
        
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model
        self.loadData = loadData
        self.players = []
     
    def nextPhase(self):
        """callback for the nextphase button"""
        self.model.updateGamePhase()
    def gameStart(self):
        if len(self.players) < 2:
            print("not today g")
        else:
            self.model.getPlayers(self.players)
            
            self.model.phase = "gamescreen"
    def playButton(self):
        """callback for the play butotn on the main screen"""
        self.model.phase = "playerselect"
    def playerSelect(self, color):
        if color in self.players:
            self.players.remove(color)
        else:
            self.players.append(color)
    def territoryCollision(self, name):
        
        print(name)
    
        
    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                # handle window manager closing our window
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # handle key down events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    else:
                        # post any other keys to the message queue for everyone else to see
                        self.evManager.Post(InputEvent(event.unicode, None))
                
                pos = pygame.mouse.get_pos()
                
                #Game Screen Collisions
                if self.model.phase == 'gamescreen':
                    
                    if self.model.gamePhase == 0 :
                        if self.model.initalPlacement:
                            
                            #collisions for all territories
                            for i in self.loadData.Territories:
                                i.collision(event,pos, self.model.initalFortify, i.name)
                    
                    #collision for next Phase button
                    self.loadData.nextButton.collision(event, pos, self.nextPhase)
                
                elif self.model.phase == 'playerselect':
                    for i in self.loadData.playerSelectButtons:
                        i.collision(event, pos, self.playerSelect, i.get_name())
                    
                    self.loadData.nextButton.collision(event, pos, self.gameStart)
                    
                #Main Menu Collisions
                elif self.model.phase == 'mainmenu':

                    self.loadData.playButton.collision(event, pos, self.playButton)
                    
                


    
                
                
                    
                        #AESTHETIC
                        #when hovered
                        #glow or outlined when selected 
                        
                        
                        #maybe replace this with a evmanger post event
                        #this is also dependant on context 
                        # needs to also check for state
                        
                        # at the inital army placing phase
                        # if a territory is clicked this means add 1 army here
                        
                        # Attacking phase
                        # when initially clicked this means this territory must be part of the players
                        # and this territory must have more than one unit
                        # and clicking on this means that the player wants to attack with this territories armies
                        # after this the player can click on any adjacent tiles
                        
                    
                    
            
