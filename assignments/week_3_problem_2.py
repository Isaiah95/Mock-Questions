def main():
    coin(input("Insert Coin: "))

def coin(c):
        c = int(c)
        if c != 50 and c ==5 or c == 10 or c == 25:
              c = 50 - c
              print ("Amount due: ",c)
            
              if c <=0:
                print("change Owed: ", abs(c))
              
if __name__ == "__main__": # proper heading for main
    main()       