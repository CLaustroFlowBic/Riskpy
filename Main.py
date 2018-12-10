import EventManager
import Model 
import View
import Controller
import loadData
from loadData import LoadData

#problem :
# loadData is running twice i dont know why 

def run():
    evManager = EventManager.EventManager()
    load = loadData.LoadData()
    gamemodel = Model.GameEngine(evManager)
    keyboard = Controller.Controller(evManager, gamemodel, load)
    graphics = View.View(evManager, gamemodel, load)



    gamemodel.run()

if __name__ == '__main__':
    run()

