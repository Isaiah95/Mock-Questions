def coin():
        d = 50 # The total number of coins need to buy a soda
        s=[5,10,25] # an array of all the possible types of coins you could use
        
        while d > 0:  #a while loop is used to keep asking for coin until the 50 is payed
            
            c=int(input("Insert Coin: " )) # takes the coin from user and stores it as c

            if c in s : # if c is in the array of s it will subtract your coin from 50 then store d as that new value 
                
                d = d - c
                
            if d > 0:
                 print ("Amount due: ",d) # its nesscary to use the order here so that it wouldn't ask for amount due after the change is 0

            elif d <= 0:
                
                print("Change Owed: ", abs(d))

                
           
coin()   