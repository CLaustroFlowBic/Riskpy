import pygame 
import Model 
from EventManager import *


class Controller(object):

	def __init__(self, evManager, model):
		
		self.evManager = evManager
		evManager.RegisterListener(self)
		self.model = model
			
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
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.evManager.Post(InputEvent("nigger", None))
					
				#if self.model.surface.get_rect().collidepoint(pygame.mouse.get_pos()):
					
				pos = pygame.mouse.get_pos()
				posInMask = pos[0] - self.model.rect.x, pos[1] - self.model.rect.y
				touching = self.model.rect.collidepoint(*pos) and self.model.mask.get_at(posInMask)
				if touching:
					print("Nigger")
		
