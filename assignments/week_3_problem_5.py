thisdict = { #used a dictnoary to make values and keys for all the furits
  "apple": "130",
  "avacoado": "50",
  "banana": "110",
  "cantaloupe" : "50",
  "grapefruit" : "60",
  "grapes" : "60",
  "honeydew" : "50",
  "kiwifruit" : "50",
  "lemon" : "15",
  "lime" : "20",
  "nectarine" : "60",
  "orange" : "80",
  "peach" : "60",
  "pear" : "100",
  "pineapple" : "50",
  "plums" : "70",
  "strawberries" : "50",
  "sweetcherries" : "100",
  "tangerine" : "50",
  "watermelon" : "80"  
}
item = input("Item: ") # gets the users item as a string
item = item.lower() #converts any string into all lowercase
if item in thisdict: #prints the item Calories if its in the dictonary
    
  print("Calories: ", thisdict[item]) 