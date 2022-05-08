'''
Reptile Rescue Program
Danielle Schultz
Allows reptile rescue to upload pets available for adoption and
manage supply inventory.
'''

from breezypythongui import EasyFrame
import openpyxl
import pandas as pd
from fpDataGrab import *

class mainWindow(EasyFrame):
    '''Starting window for application'''

    def __init__(self):
        '''Set up window and widgets'''
        EasyFrame.__init__(self, title = "Home Screen")

        # Button  and field for viewing adoptable reptiles
        self.addButton(text = "View Reptiles", row = 0, column = 0,
                       command = self.showReptiles)
        self.repOut = self.addTextArea("", row = 1, column = 0,
                                           columnspan = 4,
                                           width = 50, height = 5)

        # Button and field for viewing inventory
        self.addButton(text = "View Inventory", row = 2, column = 0,
                       command = self.showInventory)
        self.invOut = self.addTextArea("", row = 3, column = 0,
                                           columnspan = 4,
                                           width = 50, height = 5)

    # Event handler methods for buttons
    def showReptiles(self):
        '''Outputs list of available reptiles'''
        reptileList = listData('Reptiles')
        self.repOut.setText(reptileList)

    def showInventory(self):
        '''Outputs list of available inventory'''
        inventoryList = listData('Inventory')
        self.invOut.setText(inventoryList)

# Instantiate and create window
def main():
    mainWindow().mainloop()

if __name__ == "__main__":
    main()

