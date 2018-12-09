import pygame 

from EventManager import *


#should be all the data associated with the current game
class GameEngine(object):

	def __init__(self, evManager):
	
		self.evManager = evManager
		evManager.RegisterListener(self)
		self.running = False
		
		self.surface = pygame.image.load("images/1_Alaska.png")  
		self.surface.get_rect(center= (36, 36))
		self.rect = pygame.image.load("images/1_Alaska.png").get_rect(center=(36, 36))
		self.mask = pygame.mask.from_surface(self.surface)
		
	def notify(self, event):
	
		if isinstance(event, QuitEvent):
			self.running = False
	
	def run(self):
	
		self.running = True
		self.evManager.Post(InitializeEvent())
		
		while self.running:
			newTick = TickEvent()
			self.evManager.Post(newTick)