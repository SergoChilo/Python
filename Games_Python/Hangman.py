import random

name = input('Enter your name : ')
print(f'Hi {name} !!!!!  Let\'s play Hangman!')
WORDS = ['windows','word', 'apple', 'down', 'hangman']
Max_Errors = 10

#Vibor slova
def return_random_word():
    return random.choice(WORDS)

#Ruchnoy vvod
def handle_user_input():
    user_input = input('Please guess a letter or word: ')
    return user_input

#Otobrajenie bukvi esli est
def get_initial_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses

def is_game_finished(statuses, current_error):
    if current_error >= Max_Errors:
        return True
    for status in statuses:
        if not status:
            return False
    return True

def perform_check_action(word, statuses, letter):
    if letter not in word:
        return False
    for index, l in enumerate(word):
        if letter == l:
            statuses[index] = True
    return True

def print_word(word, statuses):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end='')
        else:
            print('_', end=' ')

def main():
    word = return_random_word()
    statuses = get_initial_statuses(word)
    current_errors = 0
    while not is_game_finished(statuses, current_errors):
        print_word(word, statuses)
        print('Errors left: ', Max_Errors - current_errors)
        letter = handle_user_input()
        result = perform_check_action(word, statuses, letter)
        if not result:
            current_errors += 1
    print('Game is finished!')

main()