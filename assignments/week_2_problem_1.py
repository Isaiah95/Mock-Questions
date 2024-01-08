def main():
    d = deep_to_main(input("What is the Answer to the Great Question of Life,"))

def deep_to_main(d): # goes through 3 ways 42 can be a string

    if d == ("42"): 

        return print("Yes")
    elif d == ("forty-two") or ("forty-two".upper()): #the or statment allows for any case type .upper forces the string to be upper case
        
        
        return print("Yes")
    elif d == ("forty two") or ("forty two".upper()): #the or statment allows for any case type .upper forces the string to be upper case

        return print("Yes")
    else: #if any other case is input the function will return 0

        return print("no")  
        

main()
    


