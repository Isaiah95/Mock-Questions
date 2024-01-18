def main():
    convert(input("What time is it? "))
    



def convert(time):
    hours, minutes = time.split(":") # splits apart the hour and minutes from the user entred time based on the ":" "7:30" = 7, 30
    hours = float(hours) # converts str to float type 
    minutes = float(minutes)

    time = (minutes/60) + hours # converts the time (hours, minutes) to an interger 7:30 = 7.5

    if time >= 7 and time <=8: # gives a range of when its breakfest time or not.

        print("Breakfest Time")
    elif time >=12 and time <=13:

        print("Lunch Time")
    elif time >=18 and time <=19:

        print("Dinner Time")
    else: # will not return anything if not in the specified time frames.
        return None             




if __name__ == "__main__": # proper heading for main
    main()