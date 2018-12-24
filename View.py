import pygame
import Model
import loadData
from EventManager import *


class View(object):

    def __init__(self, evManager, model, loadData):

        self.evManager = evManager
        
        self.loadData = loadData
        evManager.RegisterListener(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.smallfont = None
    
       
        
    

    def notify(self, event):
        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, QuitEvent):
            self.isinitialized = False
            pygame.quit()
            
        elif isinstance(event, TickEvent):
            self.renderall()
            self.clock.tick(30)
            
        
        #elif isinstance(event, MenuEvent):
            #self.menuRender
        
        
            
    
    def gameScreen(self):
        self.screen.fill((255, 255, 255))
        for i in self.loadData.Territories:
            self.screen.blit(i.get_surface(), (i.get_x(), i.get_y()))
            
        for i in range(0, len(self.loadData.phase), 1):
            self.screen.blit(self.loadData.phase[i], self.loadData.phasePos[i])
    
       # self.screen.blit(self.loadData.nextButton.get_image()[self.loadData.nextButton.rollover], self.loadData.phasePos[3])
        self.loadData.nextButton.display(self.screen)
        

    def mainMenuScreen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.loadData.title, (100, 100))
        #self.screen.blit(self.loadData.playButton.get_image()[self.loadData.playButton.rollover], (270,300))
        self.loadData.playButton.display(self.screen)

    def playerSelectScreen(self):
        self.screen.fill((0, 0, 0))
    
    def renderall(self):
        alx = 100
        aly = 100
        if not self.isinitialized:
            return
        # clear display
        
        
        
        if self.model.phase == 'gamescreen':
            self.gameScreen()
            
        elif self.model.phase == 'playerselect':
            self.playerSelectScreen()
            
        elif self.model.phase == 'mainmenu':
            self.mainMenuScreen()
        
        pygame.display.flip()
            
    def initialize(self):
            """
            Set up the pygame graphical display and loads graphical resources.
            """

            result = pygame.init()
            pygame.font.init()
            pygame.display.set_caption('Riskypy')
            self.screen = pygame.display.set_mode((800, 600))
            self.clock = pygame.time.Clock()
            self.smallfont = pygame.font.Font(None, 40)
            self.isinitialized = True


