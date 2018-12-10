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
                
                    
                #if self.model.surface.get_rect().collidepoint(pygame.mouse.get_pos()):
                pos = pygame.mouse.get_pos()
                
                for territory in self.loadData.Territories:
                    posInMask = pos[0] - territory.get_rect().x, pos[1] - territory.get_rect().y
                    touching = territory.get_rect().collidepoint(*pos) and territory.get_mask().get_at(posInMask)
                    if touching and event.type == pygame.MOUSEBUTTONDOWN:
                        print(territory.get_name())
                    
                    
                
                
        
