#Luis Machuca
#3/5/2020
#In this program it will generate a different list and it will print the list and say if there
#is a value of 5 or not 
import random
radom1=[random.randrange(1,15,1) for i in range(7)]
print("This is a random number:"+str(radom1))
#This checks if the list has a value of 5
if 5 in res:
    print("Number 5 does exist in this list")
else:
    print("There is no number 5 in this list") 
    
