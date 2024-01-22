# Enter your height in meters e.g., 1.55
h = float(input())
# Enter your weight in kilograms e.g., 72
w = int(input())

bmi=w/h**2
if bmi>18.5:
  if bmi <25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
  elif bmi>=25 and bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi>=30 and bmi<35:
    print(f"Your BMI is {bmi}, you are obese.")
  elif bmi>=35:
    print("clinically obese")
  else:
    print("not normal")  
else:
  print("u r not")