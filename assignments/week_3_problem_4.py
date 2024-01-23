def main():
    plate = input("Plate: ")  #Gets the string from the user
    if is_valid(plate): #If the Plate is valid it will print valid it will print valid
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): 
    if not s[0].isalpha() or not s[1].isalpha(): #s.isalpha()Checks to see if the first and 2nd number is a letter
        return False #Return False is needed to check if the statment is true or not.
    if not (len(s) >= 2 and len(s) <= 6): #len(s) gets the length of the string and check to see if it has more than  2 charcters and less than 6
        return False
    if not s.isalnum(): #isalnum() Check if all the characters in the text are alphanumeric "abc.." or "123.."
        return False
    for i in range(2,len(s)): #checks to see if starting from the 3 element,s[2], from the end of the string element, i[len(s)] if i is a number 
        if s[i].isdigit():
            if s[i] == "0": #if that number, between s[2] and the end of the string = 0 it will be invalid 
                return False
            else : 
                for j in range(i+1,len(s)): #also while next element above i ,s[i+1], to the end of the string is a letter. it will be invalid
                    if s[j].isalpha(): #We already know the first 2 elements have to be a letter and the next element has to be a number in this for loop...
                                        #so the as long as theres no letters after 3 element it will be valid 
                        return False
    return True                 
    



main()