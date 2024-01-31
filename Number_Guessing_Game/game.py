import random

print('WELCOME TO THE NUMBER GUESSING GAME')
name = input('Enter your name champion\n')
print(f'RULE\n{name}, you only have 5 chance. You have to guess the number between 1 to 100')

actual_number = random.randint(1, 100)

chance = 0
gameon = True



def user_input_validation():
    user_data = input(f'Enter your guess\n')

    if user_data.isdigit() == True or user_data.upper() == 'EXIT':
        return user_data
    
    print('INVALID INPUT')
    return user_input_validation()
    


user_input = user_input_validation()

while gameon:
    if type(user_input) == str and user_input.upper() == 'EXIT':
        print('THANK YOU FOR PLAYING')
        gameon = False
        break
    else:
        user_input = int(user_input)


    if user_input == actual_number:
        print(f'YOU GUESSES RIGHT {name}')
        gameon = False
        break
    elif user_input in range(actual_number-10, actual_number+10):
        print('YOU ARE CLOSER')
    else:
        print("DON'T LOOSE HOPE LET TAKE ANOTHER CHANCE")
    
    chance += 1
    if chance == 5:
        print(f'SORRY {name} YOU LOST THE GAME THE ACTUAL NUMBER IS {actual_number}')
        gameon = False
        break
    
    user_input = user_input_validation()

