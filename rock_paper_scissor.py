import random as r
def choiceDetermine():
    rockPaper = ['rock','paper','scissor']
    choice = r.choice(rockPaper)
    userOption = input("\nEnter your choice (rock/paper/scissor) => ")
    result(choice,userOption)
    


def result(a,b):
    print("Computer choice = ",a," User choice = ",b)
    if(a == 'rock'):
        if(b == 'rock'):
            print("--------------------------------")
            print(a," & ",b," are same")
            print("--------------------------------")
            choiceDetermine()
        elif(b == 'paper'):
            print("--------------------------------")
            print("Paper wins !! \nUser wins")
            print("--------------------------------")
        else:
            print("--------------------------------")
            print("Rock wins !! \nComputer wins")
            print("--------------------------------")
    elif(a == 'paper'):
        if(b == 'paper'):
            print("--------------------------------")
            print(a," & ",b," are same")
            print("--------------------------------")
            choiceDetermine()
        elif(b == 'rock'):
            print("--------------------------------")
            print("Paper wins !! \nComputer wins")
            print("--------------------------------")
        else:
            print("--------------------------------")
            print("Scissor wins !! \nUser wins")
            print("--------------------------------")
    else:
        if(b == 'scissor'):
            print("--------------------------------")
            print(a," & ",b," are same")
            print("--------------------------------")
            choiceDetermine()
        elif(b == 'rock'):
            print("--------------------------------")
            print("Rock wins !! \nUser wins")
            print("--------------------------------")
        else:
            print("--------------------------------")
            print("Scissor wins !! \nUser wins")
            print("--------------------------------")
loop = 'y'            
while(loop == 'y'):
    choiceDetermine()
    loop = input("Do you want to continue(y/n) => ")
