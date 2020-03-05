#Luis Machuca
#3/5/2020
#This program will add up the two numbers and it will tell the user if the sum is greater,less, or equal to the sum. 
x= int(input("What number will you like to enter first?"))
y = int(input("What is the second number you will like to add?"))
x+y>10 or x+y<10 or x+y==10
def sum1(x,y):
    z = x+y
    if x+y>10:
        print(z,'is greater than 10')
    if x+y<10:
        print(z,'is less than 10')
    if x+y==10:
        print(z,'is equal to 10')
sum1(x,y)
