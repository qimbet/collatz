#Collatz conjecture solver
#This is code to iterate through the Collatz conjecture until an input value reaches 1. 
#This project does not account for the case in which the Collatz sequence does not lead to 1. 

#Collatz Conjecture: 
#For any positive integer:
#Even numbers: divide by 2
#Odd numbers: Multiply by 3, add 1

import time


def checkEven(x):
    if ((x % 2) == 0):
        return(True)
    else:
        return(False)
    
def collatz():
    while(True):        
        for i in range (1,7):   #input & data validation. Returns positive integer x
            if (i == 6):
                print("stop fooling around please")
                time.sleep(1)
                exit()

            x = input("Enter a positive number: ")
            if (x.isnumeric() != True):
                print("That was not an integer!\n")
                continue
            elif (int(x) <= 0):
                print("That was not a positive number!\n")
                continue
            
            x = int(x)
            break
            
        while(x != 1):
            if (checkEven(x) == True):
                x = x//2
                x = int(x)
            else:
                x = (x*3)+1
            print("The current value is: " + str(x))

        print("The current value is: 1 \n")
        print("\nProgram finished. \nEnter a new number to try again.\n")

collatz()
