
def mathint():
    expression = input('enter expression: ')
    x, y, z = expression.split()
    x = int(x)
    z = int(z)
    if y == "+":

        return x + z
    elif y=="/":
            
        return x/z
print(mathint())
