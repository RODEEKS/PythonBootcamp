a=8/3
print(a) #2.6666666666666665
print(int(a)) #2
print(round(a)) #3
print(round(a,2)) #2.67
print(8/3) #2.6666666666666665
print(8//3) #2
print(type(8//3)) #<class 'int'>
print(type(8/3)) #<class 'float'>

a=3
# print("value is " + a) #error 
print("value is " , a) #value is 3

#f-string

a=3
b=3.4
c=True
print(f"a is {a},b is {b}, c is {c}")
