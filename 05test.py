#project to create snake water and gun
import random


def snake_game():
    text=int(input("""
1=snake
2=water
3=gun"""))
    computer =random.randint(1,3)
    
    if computer == text:
        print("draw")
    elif computer ==1 and text==2:
        print("computer won")
    elif computer==2 and text==3:
        print("computer won")
    elif computer==3 and text==1:
        print("computer won")
    elif computer==1 and text==3:
        print("you won")
    elif computer ==2 and text==1:
        print("you won")
    elif computer==3 and text==2:
        print("you won")
    elif computer==1 and text==3:
        print("you won")
    elif computer==2 and text==1:
        print("you won")
    elif computer==3 and text==2:
        print("you won")
    else:
        print("some thing wrong error")
    print(computer,"you",text)
    
        
while True:
    snake_game()
