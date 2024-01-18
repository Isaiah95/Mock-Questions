print("Type a sentence emoji :) or ):")

emoji = input()
x=emoji.replace(":)", "🙂").replace(":(", "🙁") # you could replace two chars by using the function replace twice

print(x)
