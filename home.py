import random
from data import Game 


print("---------------------------Welcome to Quiz game---------------------------")

gm = Game()



for i in range(1,8):
    if i == 1:
        print()
        gm.que1()
        print()
        print("_____________________________________________________________")
    elif i == 2:
        print()
        gm.que2()
        print()
        print("_____________________________________________________________")    
    elif i == 3:
        print()
        gm.que3()
        print()
        print("_____________________________________________________________")
    elif i == 4:
        print()
        gm.que4()
        print()
        print("_____________________________________________________________")
    elif i == 5:    
        print()
        gm.que5()
        print()
        print("_____________________________________________________________")
    elif i == 6:
        print()
        gm.que6()
        print()
        print("_____________________________________________________________")
        
    elif i == 7:
        print()
        print()
        print()
        print("game is over :-) ")
        print()
        print()
        print()
