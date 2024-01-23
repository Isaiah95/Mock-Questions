def twtrr():
    t = input("Input: ") # Gets user input
    t = t.lower() # forces everthing to be lower
    s = ['a', 'i','e', 'o','u'] # list of all vowels
    for d in s:  # checks to see if a vowel is used 
        if d in t: #replaces the vowels with an empty char
            t = t.replace(d,'')
    print("Output:", t)











twtrr()
