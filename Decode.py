class Decode:
    
    def __init__(self):
        pass
        
    def decrypt(self, gridCopy, wordCopy, finalCipherCopy):
        grid = gridCopy
        cipherKey = wordCopy
        finalCipher = finalCipherCopy
        
        # creates a number list (0,1,2,3) linked to key word
        # e.g. for key word MARK: 0 : cipherKey[0] : M, 1:1:A, 2:2:R, 3:3:K
        # key word then sorted from 0-9 -> A-Z and linked number values are displayed e.g. AKMR = [1,3,0,2]
        indices = sorted(range(len(cipherKey)), key=lambda i: cipherKey[i])
        
        gridColumnLen= len(finalCipher) // len(cipherKey)
        
        # creates list, each element is the list of letters in each key word grid column
        gridColumns = [finalCipher[i:i+gridColumnLen] for i in range(0,len(finalCipher),gridColumnLen)]
        
        global keyWordGridSorted
        # swaps rows <-> cols
        keyWordGridSorted = list(zip(*gridColumns))
    
        # prints the sorted keyword grid that was used to create final cipher text
        print("SORTED KEYWORD GRID")
        global cipherKeySorted
        cipherKeySorted = ([cipherKey[i] for i in indices])
        print("  ", end = "")
        for char in cipherKeySorted:
            print(char, end = "    ")
        print()
        
        for row in keyWordGridSorted:
            print(row)
        print()
        
        # inverts the previously generated indices to reverse the grid column sorting
        # e.g. for key word MARK (AKMR): A(0) : indices[0] = 1, K(1):1:3, M(2):2:0, R(3):3:2
        # list is sorted from lowest to highest in terms of linked values e.g. [2,0,3,1]
        global indicesDecoded
        indicesDecoded = sorted(range(len(cipherKeySorted)), key=lambda i: indices[i])
        
        # prints the key word grid prior to its column sort
        print("ORIGINAL KEYWORD GRID")
        global keyWordGrid
        # takes nth element of each old row and copies it to a new row, repeats for all indices
        keyWordGrid = ([[row[i] for i in indicesDecoded] for row in keyWordGridSorted])
        print("  ", end = "")
        for char in cipherKey:
            print(char, end = "    ")
        print()
        for row in keyWordGrid:
            print(row)
        
        # prints the first cipher that was generated prior to use of key word
        global firstCipher
        # returns all individual elements from nested list
        firstCipher = [item for sublist in keyWordGrid for item in sublist]
        firstCipher = "".join(firstCipher)
        print("\nFirst ciphertext: ",firstCipher)
        
        # creates list of pairs of first cipher elements, representing co-ords of chars in letter format
        firstCipherList = [firstCipher[i:i+2] for i in range(0, len(firstCipher), 2)]
                
        # turns char pairs from letters into numbers representing position in alphanumeric grid in row, col format
        # e.g. A,A = 0,0... A,B = 0,1 etc
        firstCipherListInt = [[ord((char.lower())) - 97 for char in element] for element in firstCipherList]
        
        global originalMsg
        originalMsg = ""

        # searches each row, col pair in alphanumeric grid and returns its element
        # e.g. grid[2][3] = element at 2nd row, 3rd col
        for y, x in firstCipherListInt:
            originalMsg = originalMsg + grid[y][x]
        
        return originalMsg

        