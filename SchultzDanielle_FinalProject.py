'''
Reptile Rescue Program
Danielle Schultz
Allows reptile rescue to upload pets available for adoption and
manage supply inventory.
'''

from breezypythongui import EasyFrame
import openpyxl
# import os
import pandas as pd

class mainWindow(EasyFrame):
    '''Starting window for application'''

    def __init__(self):
        '''Set up window and widgets'''
        EasyFrame.__init__(self, title = "Home Screen")

        # Button for adding adoptable reptiles
        self.addButton(text = "Adoptable Reptiles", row = 0, column = 0)

        # Button for viewing inventory
        self.addButton(text = "View Inventory", row = 1, column = 0)

    # Event handler methods for buttons
    def showReptiles(self):
        '''Outputs list of available reptiles'''
        reptileList = ""
        self.messageBox(title = "Reptiles", message = reptileList
        

# Instantiate and create window
def main():
    mainWindow().mainloop()

if __name__ == "__main__":
    main()

'''
https://medium.com/analytics-vidhya/how-to-extract-information-from-your-excel-sheet-using-python-5f4f518aec49
'''
