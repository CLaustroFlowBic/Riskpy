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
    
    def territoryCollisons(self, event, pos):
        
        #this block is only called when the game is running and is in on of four states
        for territory in self.loadData.Territories:
            posInMask = pos[0] - territory.get_rect().x, pos[1] - territory.get_rect().y
            touching = territory.get_rect().collidepoint(*pos) and territory.get_mask().get_at(posInMask)
            if (touching and event.type == pygame.MOUSEBUTTONDOWN):
                print(territory.get_name())
                
  #  def nextPhaseButton(self, event, pos):
        if (self.loadData.nextButton.get_rect().collidepoint(*pos)):
            
            self.model.nextButtonCollide(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.model.nextPhase()
        else:
            self.model.nextButtonCollide(False)
    
    
   # def playButton(self, event, pos):
        """Collisions for the Play Button In the Main menu"""
        #make these part of the button class use a callback function
        
        if (self.loadData.playButton.get_rect().collidepoint(*pos)):
            self.loadData.playButton.rollover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.model.phase = "playerselect"
        else:
            self.loadData.playButton.rollover = False
            
    def nextPhase(self):
        pass
    def playButton(self):
        
        self.model.phase = "gamescreen"
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
                
                    self.territoryCollisons(event, pos)
                    #self.nextPhaseButton(event, pos)
                    self.loadData.nextButton.collision(event, pos, self.nextPhase)
                
                elif self.model.phase == 'playerselect':
                    pass
                #Main Menu Collisions
                elif self.model.phase == 'mainmenu':
                    
                    #self.playButton(event, pos)
                    self.loadData.playButton.collision(event, pos, self.playButton)
                    #do the button shit collisons for the main menus
                


    
                
                
                    
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
                        
                    
                    
                
    #def selection
    #def placing
    #   - this is going to call the model with a selected territory
        
