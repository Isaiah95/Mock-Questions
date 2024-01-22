def main():
    names(input("camelCase: ")) # gets the user input for the string

def names(n):
    s= "" #strings are immutable, so you would need a new empty string to replace the uppercase letters with "_"


    for i in n:

        if(i.isupper()): #checks to see if anything in the string is uppercase
            s+="_" # if so then it will replace them "_"
            s += i.lower() # Also the lower case letter instead of the upper one
        else:    
            s+= i.lower() # when nothing is uppercase, it will finish going through the rest of the string
            
             
    print("snake_case:",s)

if __name__ == "__main__": # proper heading for main
    main()       
    