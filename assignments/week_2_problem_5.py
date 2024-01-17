def main():
    convert(input("What time is it? "))
    



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if hours >= 7 and hours <=8:

        print("Breakfest Time")
    elif hours >=12 and hours <=13:

        print("Lunch Time")
    elif hours >=18 and hours <=19:

        print("Dinner Time")
    else:
        return None             




if __name__ == "__main__":
    main()