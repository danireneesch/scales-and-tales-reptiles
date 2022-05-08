'''
RRP - Excel Module
Danielle Schultz
Allows data from Excel file to be read and manipulated
'''

import pandas as pd


# Create data frames for worksheets

file = 'FinalProjectInventory.xlsx'
data = pd.ExcelFile(file)
reptilesDF = data.parse('Reptiles')
inventoryDF = data.parse('Inventory')


# Read and print data from worksheets

def listData(sheet):
    
    if sheet == 'Reptiles':
        return(reptilesDF.to_string())

    if sheet == 'Inventory':
        return(inventoryDF.to_string())


# add new row

def addRow(sheet):
    
    if sheet == 'Reptiles':
        petID = '7341'
        rName = 'Fig Newton'
        rAge = 'Young'
        rSex = 'Female'
        rSpecies = 'Newt'
        rZip = '43621'
        newEntryRep = {'Pet ID':petID, 'Name':rName, 'Age':rAge,
                       'Sex':rSex, 'Species':rSpecies, 'Zip':rZip}
        newRepDF = pd.DataFrame(newEntryRep, index=[1])
        updatedRepDF = pd.concat([reptilesDF, newRepDF], ignore_index=True)
        return(updatedRepDF)

    if sheet == 'Inventory':
        iNumber = '368931'
        iName = 'Basking Platform'
        iCategory = 'Habitat'
        iPrice = 15.99
        iStock = 0
        newEntryInv = {'Item #':iNumber, 'Name':iName, 'Category':iCategory,
                       'Price':iPrice, '# In Stock':iStock}
        newInvDF = pd.DataFrame(newEntryInv, index=[1])
        updatedInvDF = pd.concat([inventoryDF, newInvDF], ignore_index=True)
        return(updatedInvDF)


