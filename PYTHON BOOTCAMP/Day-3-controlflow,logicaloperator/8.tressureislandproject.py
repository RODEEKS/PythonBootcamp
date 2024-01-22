print("Welcome to RODEEKS island")
print("You have to find the tressure")
ch1=input('You\'re at crossroad. where you want to go type "left" or "right" ?\n').lower()

if ch1=="left":
    ch2=input('You\'ve came to lake. now type "wait" for boat or "swim" fo  crossing ?\n').lower()
    if ch2=="wait":
        ch3=input('You\'re infront of door. choose either "red" and "blue" for game over or "yellow" door to win the tressure !!!\n').lower()
        if ch3=="yellow":
            print("YOU WIN")
        else:
            print("YOU LOOSE")
    else:
        print("game over")
else:
    print("game over")
    