import random
response = "y"
def roll_the_dice():

    while(response == "y" or response == "yes"):
        no = random.randint(1,6)   
        if(no == 1):
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            break
        elif(no == 2):
            print("[-----]")
            print("[     ]")
            print("[ 0 0 ]")
            print("[     ]")
            print("[-----]")
            break
        elif(no == 3):
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
            break
        elif(no == 4):
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
            break
        elif(no == 5):
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
            break
        elif(no == 6):
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
            break
    response = input("Press y to roll again n to exit: ")
if(response == "y"):
  roll_the_dice()