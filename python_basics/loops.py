def total_value():

    num = int(input("Enter a number: "))
    total = 0
    while num >0:
        total += num
        num = num-1
    print ("the sum is", total)

# print multiplication table for entered number

def num_multiplication():

    num2 = int(input("Enter a number: "))
    table = 1
    while table <=10:
        print(num2, "*", table , "==",num2*table)
        table +=1

def secret_number():
    secret_num = 7
    running = True
    while running:
        guess_num = int(input("enter the guess: "))
        if guess_num == secret_num:
            print("You got it!")
            running = False



def modification_secret():
    secret_num = 7
    while True:
        guess = int(input("Enter a number: "))
        if guess == secret_num:
            print("You got it!")
            break
        elif guess > secret_num:
            print("The guess is greater thn secret number")
        else:
            print("The guess is smaller")



def guess_count():
    secret_num = 7
    counter=0
    while True:
        counter+=1
        guess = int(input("Enter a number: "))
        if guess == secret_num:
            print("You got it!")
            print("You guessed it in",counter,"guesses")
            break
        elif guess > secret_num:
            print("The guess is greater thn secret number")
        else:
            print("The guess is smaller")