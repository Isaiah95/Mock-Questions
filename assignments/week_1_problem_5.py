def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    d = d.lstrip("$") #lstrip takes away the leading string which in this case is "$"
    d = float(d) #float allows for decimals inputs
    

    return d


def percent_to_float(p):

    p = p.rstrip("%")   #rstrip takes away the trailing charcter which is going to be "%"
    p = float(p) #float allows for decimals inputs

    return p/100 #dividing by 100 returns the percentage instead of the actual number

main()