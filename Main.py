import EventManager
import Model 
import View
import Controller

def run():
	evManager = EventManager.EventManager()
	
	gamemodel = Model.GameEngine(evManager)
	keyboard = Controller.Controller(evManager, gamemodel)
	graphics = View.View(evManager, gamemodel)
	
	gamemodel.run()
	
if __name__ == '__main__':
	run()

