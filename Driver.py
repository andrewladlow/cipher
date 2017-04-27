from Encode import Encode
from Decode import Decode

enc = Encode()
dec = Decode()

choice = ""
originalMsg = ""
firstCipher = ""
cipherKey = ""
cipher = ""
finalCipher = ""
decodedMsg = ""

while choice != "4":
    print("\nSelect an option below: ")
    print("1. Enter a message to be encoded")
    print("2. Enter keyword to generate final ciphertext")
    print("3. Enter final ciphertext to decode message")
    print("4. Quit")
    
    choice = input()
    
    if (choice == "1"):
        while not 0 < len(originalMsg) <= 80:
            originalMsg = input("Enter a message between 1 and 80 characters: ")
        firstCipher = enc.genCipher(originalMsg)
        print("\nFirst ciphertext: " + firstCipher)
        
    elif (choice == "2"):
        print("First ciphertext length:", len(enc.getFirstCipher()))
        while len(cipherKey) is 0 or len(enc.getFirstCipher()) % len(cipherKey) is not 0:
            cipherKey = input("Enter keyword (Must divide into first ciphertext): ")

        cipher = enc.genKey(cipherKey)
        print("\nFinal ciphertext: " + cipher)

    elif (choice == "3"):
        while len(finalCipher) is 0 or finalCipher != cipher:
            finalCipher = input("Enter final ciphertext: ")
        decodedMsg = dec.decrypt(enc.getGrid(), enc.getKey(), finalCipher)
        print("\nDecoded message: " + decodedMsg)
            
    elif (choice == "4"):
        quit()
