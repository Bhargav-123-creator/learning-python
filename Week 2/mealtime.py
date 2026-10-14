def main():
    x = input("What time is it:")
    hour , minute = x.split(":")
    hour = int(hour)
    minute = float(minute)
    y = input("AM or PM:")
    y = y.lower()
    if y == "am":
        if hour == 12:
            hour = 0
        time = hour + (minute/60)
    elif y == "pm":
        if hour != 12:
            hour += 12
        time = hour + (minute/60) + 12
    else:
        print("nothing")
    mealtime(time)



def mealtime(n):
    if   8 >=  n >= 7:
        print("Breakfast time")
    elif 13 >= n >= 12:
        print("Lunch time")
    elif 19 >= n >= 18:
        print("Dinner")
    else:
        print("nothing")

main()


