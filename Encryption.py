bruteforce = {}

import string

letters = string.ascii_letters
#string constant containing lowercase and uppercase letters

def encrypt(message,rotation):
    """Encrypts a message by rotation."""
    complement = 26 - rotation
    result = ''
    for i in message:
        #if i is a letter
        if i in letters:
            #if the rotation goes beyond the letter 'Z'
            if ((ord(i) + rotation) > 90):
                #subtracting by (26-rotation) will yield the same result
                newAscii = ord(i) - complement
                #replace the letter with the rotated one
                newLetter = chr(newAscii)
                #add this to our result string
                result += newLetter
            else:
                #shift ascii representation by 'rotation'
                newAscii = ord(i) + rotation
                #replace the letter with the rotated one
                newLetter = chr(newAscii)
                #add this to our result string
                result += newLetter
        else:
            #if part of the string is not a letter leave as is
            result += i
    #return the new string        
    return result

def decrypt(message,method,rotation):
    """Decrypts by rotation whether you know the key or not."""
    #rotation number is known
    if method == 'y':
        complement = 26 - rotation
        #switch the parameters of 'encrypt' and use 'encrypt'
        return encrypt(message,complement)
    #rotation number not known solve by brute force
    #perform 26 rotations
    elif method == 'n':
        for i in range(1,26):
            #put each entry into a dictionary called BruteD
            bruteforce[i] = str(encrypt(message,26-i))
        return

def cont(answer):
    """Run 'Cryptography()' again if desired."""
    #If the user wants to continue
    if answer == "y":
        #restart the main program
        cryptography()
    else: #otherwise
        return #end the program


def cryptography():
    """Rotates letters in a message by some value."""
    #take input from the user, turn it into a lowercase string
    choice = str(input("Want to encrypt or decrypt?\n")).lower()
    #correct input is 'ecnrypt' or the number '1'
    if choice == "encrypt" or choice == "1":
        #Ask for the desired string to rotate
        message = input("Enter a string:\n").upper()
        #Ask for the rotation key, turn it into an integer
        #and take the modulo 26
        rotation = int(input("Enter rotation number:\n")) % 26
        #Return the result of the encryption function
        print('Rot %d = %s' % (rotation,str(encrypt(message,rotation))))
        #Ask the user if they want to continue
        more = input("\nContinue?(y,n)\n").lower()
        #pass the response to the function 'cont(answer)'
        cont(more)
    #if the user chose decryption
    elif choice == "decrypt" or choice == "2":
        #Ask for a string to decrypt
        message = input("Enter a string:\n").upper()
        #Ask if the rotation key is known
        method = input("Do you know the secret rotation number?(y/n)\n").lower()
        #if they know it, perform a single rotation
        if method == "yes" or method == "y":
            #Ask for the rotation number
            rotation = int(input("Enter rotation number:\n")) % 26
            #Print the result and its rotation
            print('Rot %d = %s' % (rotation,str(decrypt(message,'y',rotation))))
            #Ask user if they want to continue
            more = input("\nContinue?(y,n)\n").lower()
            #Pass the result to the function 'cont'
            cont(more)
        #if they don't know the rotation key perform 26 rotations    
        elif method == "no" or method == "n":
            #pass a dummy value for rotation
            rotation = 0
            #tell the user brute force is taking place
            print('\nDecrypting by brute force.\n')
            #decrypt using brute force method
            decrypt(message,'n',rotation)
            #in the range from 1 to 26
            for i in range(1,26):
                #print the entries in the dictionary
                print('Rot %d = %s' % (i, bruteforce[i]))
            #Ask user if they want to continue    
            more = input("\nContinue?(y,n)\n").lower()
            #pass the answer to the function 'cont'
            cont(more)

cryptography()
