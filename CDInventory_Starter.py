#---------------------------------------------------#
# Title: CDInventory.py
# Desc: Script for Assignment 05
# Change Log: 
# Jason Johanneck, 2021-Nov-14, Initial Creation.
#---------------------------------------------------#

# Declare variabls
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
dicRow = {}
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print()
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
#--- Quit
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
#--- Load CD Inventory from File    
    if strChoice == 'l':
        # no elif necessary, as this code is only reached if strChoice is not 'exit'
        lstRow = []
        objFile = open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id':lstRow[0],'title':lstRow[1],'artist':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('This data was loaded:')
        print()
        for row in lstTbl:
            print(row.values())
#--- Add CD Inventory   
    elif strChoice == 'a':  
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = str(strID)
        dicRow = {'id':intID,'title':strTitle,'Artist':strArtist}
        lstTbl.append(dicRow)
        print()
        print('You added: ',dicRow)
        print(lstTbl)
#--- Display CD Inventory
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row.values())
#--- Delete a CD from Inventory
    elif strChoice == 'd':
        lstNew = []
        Found = 'n'
        strID = input('Enter an ID to Delete: ')
        intID = str(strID)
        for row in lstTbl:
            dicRow = row
            for i in row.values():
                if i == intID:
                    Found = 'y'
                    # print(dicRow)
            if Found == 'n':
                lstNew.append(row)
            else:
                Found = 'n'
        lstTbl = lstNew
        print()
        print('Now your list is: ')
        print(lstTbl)
#--- Save Inventory to a File                      
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        ObjFile = open(strFileName,'a')
        for row in lstTbl:
            strOut = ''
            for item in row.values():
                strOut += str(item) + ','
            strOut = strOut[:-1] + '\n'
            print()
            print('writing this: ' + strOut)
            ObjFile.write(strOut)
        ObjFile.close()
        lstTbl = []
    else:
        print('Please choose either l, a, i, d, s or x!')

