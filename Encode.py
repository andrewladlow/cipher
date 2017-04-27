import re
from random import shuffle
from string import digits, ascii_uppercase


class Encode :

    def __init__(self):
        pass
    
    # randomly fills a 6x6 grid with letters A-Z and digits 0-9
    def genGrid(self):
        chars = list(digits + ascii_uppercase)
        shuffle(chars)
        # creates 6 sublists, forming the grid rows
        global grid
        grid = [chars[0:6], chars[6:12], chars[12:18], chars[18:24], chars[24:30], chars[30:36]]
        print("    ", end = "")
        for char in ascii_uppercase[0:6]:
            print(char, end = "    ")
        print()
        for char, row in zip(ascii_uppercase[0:6], grid):
            print(char, row)  
            
    # searches for a given value within a grid, returning its co-ords if found
    def findVal(self, grid, value):
        for rowNum, row in enumerate(grid):
            for colNum, element in enumerate(row):
                if element == value:
                    return (rowNum, colNum)
                
    # converts a given number (co-ord) into its letter equivalent
    def numToChar(self, number):
        if 0 <= number <= 5:
            return ascii_uppercase[number]
        else:
            raise ValueError('Number out of bounds')            
    
    # creates first cipher text from grid co-ords
    def genCipher(self, msg):
        self.genGrid()
        global firstCipher
        firstCipher = ""
        global originalMsg
        originalMsg = msg
        # remove all non-alphanumeric chars and convert to upper case
        originalMsg = re.sub(r"[^a-zA-Z0-9]","", originalMsg).upper()
        originalMsg = originalMsg.upper()
        
        for char in originalMsg:
            # scans through grid, taking each message char and converting to letter co-ords
            row, col = map(self.numToChar, self.findVal(grid, char))
            firstCipher = firstCipher + row + col
            
        return firstCipher 
    
    def genKey(self, inputKey):
        global firstCipher
        firstCipher = list(firstCipher)
        
        global cipherKey
        cipherKey = inputKey.upper()
        
        # creates the sublists (rows) for the keyword grid
        print("ORIGINAL KEYWORD GRID")
        keyWordGrid = [firstCipher[i:i+len(cipherKey)] for i in range(0,len(firstCipher),len(cipherKey))]
        print("  ", end = "")
        for char in cipherKey:
            print(char, end = "    ")
        print()
        for row in keyWordGrid:
            print(row)
        print()
        
        # creates a list (0,1,2,3) linked to key word
        # e.g. for key word MARK: M=0, A=1, R=2, K=3
        # key word then sorted from 0-9 -> A-Z and linked number values are displayed in place e.g. AKMR = [1,3,0,2]
        indices = sorted(range(len(cipherKey)), key=lambda i: cipherKey[i])
        cipherKeySorted = ([cipherKey[i] for i in indices])
        
        # sorts grid according to its new column arrangement
        # takes nth element of each old row and copies each to new rows, repeats for all indices
        print("SORTED KEYWORD GRID")
        keyWordGridSorted = ([[row[i] for i in indices] for row in keyWordGrid])
        print("  ", end = "")
        for char in cipherKeySorted:
            print(char, end = "    ")
        print()
        for row in keyWordGridSorted:
            print(row)
        
        # reads down each column and retrieves letters
        # takes first element of each old row and copies to single new row, repeat for second element etc
        finalCipherTemp = [[row[col] for row in keyWordGridSorted] for col in range(len(row))]
        
        # flattens nested lists then joins to single string
        # for sublist in grid -> for item in sublist -> return item
        finalCipher = [item for sublist in finalCipherTemp for item in sublist]
        finalCipher = "".join(finalCipher)
        
        return finalCipher
    
    def getGrid(self):
        return grid
    
    def getKey(self):
        return cipherKey
    
    def getFirstCipher(self):
        return firstCipher