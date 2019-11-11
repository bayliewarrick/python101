from random import randint

choices = ['rock','paper','scissors']

def cpu_choice():
    choice1 = choices[randint(0,2)]
    return choice1

def player_choice():
    choice2 = input('Enter Rock, Paper, or Scissors:')
    if choice2 not in choices:
        print('Choose a valid selection!')

def compare_choices():
    if (choice1 == 'rock' and choice2 == 'scissors'):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you lose!")
    elif (choice1 == 'paper' and choice2 == 'rock'):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you lose!")
    elif (choice1 == 'scissors' and choice2 == 'paper'):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you lose!")
    elif (choice1 == 'rock' and choice2 == 'paper'):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you win!")
    elif (choice1 == 'scissors' and choice2 == 'rock'):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you win!")                
    elif (choice1 == 'paper' and choice2 == 'scissors'):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you win!")    
    elif (choice1 == choice2):
        print (f"Computer chose: {choice1} and you chose: {choice2}! you tie!")

def start_game():
    cpu_choice()
    print(choice1)
    player_choice()
    compare_choices()

start_game()
