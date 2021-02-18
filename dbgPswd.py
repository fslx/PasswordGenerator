import random
import time
import string
# source-code written by: https://github.com/fsty

"""randChar = ["A", "B", "C", "D",
            "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] - fixed w/ randValues.

randNum = [] 
 
randSymbol = ["@", "$",
                   "!", "+", "§"]"""

randValues = string.ascii_lowercase + string.ascii_uppercase + string.digits + "~@#$%^&*_" 
def generateFile():
            file_object_gen_yn = str(input(r"Do you wish to generate a new password.txt in your current working directory? y/n ")).lower()
            if file_object_gen_yn == "y":
                        print(r"created a new file in C/: ^ /Home/~ ")
                        file_Object = open("passwords.txt", "x")
                        return generatePassword()
            else:
                        print("Assuming file already exists in current working directory, continuing running function genererateUser")
                        print("If the file does not exists, a syntax error is likely to occur.")
                        return generatePassword()  
            
def generatePassword():
    print("The program is starting, it will create circa n passwords where n = range(0,n) in for loop, to stop the program hold ctrl+shift+C \n")
    print("Starting...\n")
    time.sleep(1)

    
    for i in range(0, 30): # set this interval before running to have a set number of accounts created.
        print(random.choice(randValues)) 
        file_Object = open(r"passwords.txt", "a")
        file_Object.write(random.choice(randValues))   
generateFile()


