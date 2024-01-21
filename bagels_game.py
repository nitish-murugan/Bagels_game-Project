import random
random_number = str(random.randint(100,999))
tries = 0
loop = True
def checking1(number):
    global loop
    if(random_number == number):
        print("\n------------------------------------")
        print("You got it in ",tries," tries")
        print("------------------------------------\n\n")
        loop = False
def checking2(number):
    global tries
    crt_digit = 0
    incrt_digit = 0
    random_number_lst = list(random_number)
    for i in number:
        if(i in random_number_lst):
            crt_digit+=1
        else:
            incrt_digit+=1
    print("Correct digits => ",crt_digit,"   | ","Incorrect digits => ",incrt_digit)

    number_lst = list(number)
    crt_position = 0
    incrt_position = 0
    index = 0
    for i in range(3):
        if(random_number_lst[index] == number_lst[index]):
            crt_position+=1
        else:
            incrt_position+=1
        index+=1

    
    print("Correct position => ",crt_position," | ","Incorrect position => ",incrt_position,"\n")
    tries+=1
print("You have only ten chances\n")
for i in range(10):
    print("Trial NO. ",i+1)
    number_input = input("Enter any 3-digit number => ")
    checking2(number_input)
    if(loop):
        checking1(number_input) 
    if(loop):
        pass
    else:
        break
