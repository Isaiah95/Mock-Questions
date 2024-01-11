def main():

    greeting(input ("Greeting: ")) # gets the user input a turns it into the greeting function

def greeting(g):

    g = g.lower()   # forces all statments to be lowercase


    if g[:5] == "hello": # g[:5] checks for 0-4 or first 5 chars in the list. A string is made up of a list of chars.

        print ("$0")
    
    elif g[:1] == ('h'): #g[:1] checks for the first char in the list to be = to h

        print("$20")
    
    else:  # if all greets are not true then you get #100
        
        print("$100")
    
main()    



