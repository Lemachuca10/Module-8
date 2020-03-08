#Luis Machuca
#3/5/2020
def parameter12():
    year21 = int(input("Enter the year to check if it is a leap year:"))
    if ((year21%400 == 0) or ((year21%4 == 0) and (year21%100 != 0))):
        print("%d is a leap year" %year21)
    else:
        print("%d is Not a Leap year"%year21)
parameter12()
              
