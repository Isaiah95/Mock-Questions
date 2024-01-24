
def findduplicates(string1 = (input("Type in a sentence: ")),string2 = (input("Type in another sentence: "))):

    string1 = string1.split()# makes the string a list
    string2 = string2.split() 
    string2 = string1 + string2 #joins string 1 and 2 together to have on list
    list(dict.fromkeys(string2)) # creaates a dictonary to get the values of string2 then should remove the same values
    print(string2)

findduplicates()      
    