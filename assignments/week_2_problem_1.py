def main():
    deep_to_main(input("What is the Answer to the Great Question of Life,"))

def deep_to_main(d): # goes through 3 ways 42 can be a string

    d = d.lower() # forces the string to be lower

    if d == ("42"):

         print("Yes")
    elif d == ("forty-two"): #the or statment allows for any case type .upper forces the string to be upper case
        
        
        print("Yes")
    elif d == ("forty two"): #the or statment allows for any case type .upper forces the string to be upper case

        print("Yes")
    else: #if any other case is input the function will return 0

         print("no")  
        

main()
    


