import pygame
import Model

from EventManager import *


class View(object):

	def __init__(self, evManager, model):

		self.evManager = evManager
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
			
	def renderall(self):
	
		if not self.isinitialized:
			return
		# clear display
		self.screen.fill((255,255,255))
		# draw some words on the screen
		
		self.screen.blit(self.model.surface.convert_alpha(), (0,0))
		# flip the display to show whatever we drew
		pygame.display.flip()
			
	def initialize(self):
            """
            Set up the pygame graphical display and loads graphical resources.
            """

            result = pygame.init()
            pygame.font.init()
            pygame.display.set_caption('demo game')
            self.screen = pygame.display.set_mode((800, 600))
            self.clock = pygame.time.Clock()
            self.smallfont = pygame.font.Font(None, 40)
            self.isinitialized = True

	
	
			

