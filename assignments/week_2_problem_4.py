def mathint(): #used a function so it could be accessiable to call
    expression = input('Enter expression: ')
    x, y, z = expression.split() # split() takes a string and sperates the charcters into diffrent variables
    x = int(x) #int(x) takes the x string and turns it into a int type. this is nesscary to do math equations
    z = int(z)
    if y == "+": #y is left a string because the symbols are always gonna be a string.

        return x + z # this line does math between two intergers x and z
    
    elif y=="/":

        return x/z
    
    elif y =="-":

        return x-z
    
    elif y == "*":

        return x*z
print(mathint()) #prints the function
