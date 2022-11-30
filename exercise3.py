# number gaming game
winning_number = 20
user_input = input("guess a number b/w 1 and 90 : ")
user_input =int(user_input)
if user_input== winning_number:
    print("you win")
else:
    if user_input < winning_number:
        print("too low")    
    else:
        print("too high")