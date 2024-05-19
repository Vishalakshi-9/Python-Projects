# Snake Water and Gun Game

import random

computer = random.randint(0,2)
user = int(input("Choose any one:\n 0 for Snake\n 1 for water\n 2 for Gun\n"))

print("You: ", user)
print("Computer:", computer)

def check(computer,user):
        if(computer==user):
             print("Oops!! No win No loss.")
    
        if(computer==0 and user==1):
            print("You lost. Snake drank the water.")
    
        if(computer==0 and user==2):
             print("You Win. Gun killed the snake.")

        if(computer==1 and user==0):
             print("You Win. Snake drank the water.")    

        if(computer==1 and user==2):
             print("You lost. Water diffused the gun.")

        if(computer==2 and user==0):
             print("You lost. Gun killed the Snake.")

        if(computer==2 and user==1):
             print("You Win. Water diffused the gun.")
             
check(computer,user)
             
             
  
