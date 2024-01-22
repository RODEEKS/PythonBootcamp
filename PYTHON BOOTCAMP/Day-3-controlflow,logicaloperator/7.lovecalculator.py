print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

com=name1+name2
low=com.lower()

t=low.count("t")
r=low.count("r")
u=low.count("u")
e=low.count("e")
first=t+r+u+e

l=low.count("l")
o=low.count("o")
v=low.count("v")
e=low.count("e")
second=l+o+v+e

score=int(str(first)+str(second))

if (score<10) or (score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>=40) and (score<=50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")