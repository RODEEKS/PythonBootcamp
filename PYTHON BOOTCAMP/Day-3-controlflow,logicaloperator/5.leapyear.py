year=int(input("enter year \n"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
