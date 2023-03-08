import random


a = input('Enter your name : ')
print(f'::: Hi {a}, lets start game :::')
Empty_mark = 'x'
Moves = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
    }

# 16 cifr, posledni - Empty_mark -> x
def shuffle_field():
    field = list(range(1, 17))
    field[-1] = Empty_mark
    possible_moves = list(Moves.keys())
    applied_moves = 0
    while applied_moves < 100:
        random_move = random.choice(possible_moves) # Randome xod is xodov(4)
        try:
            field = perform_move(field, random_move) # primenit k polyu sluchayni shag
            applied_moves += 1
        except IndexError:
            continue
    return field

def print_field(field):
    for i in range(0, 16, 4):
        print(field[i:i+4])
    print('\n')

#Meshat cifri
def is_game_finished(field):
    ideal = list(range(1, 16))
    ideal.append(Empty_mark)
    return ideal == field     # True or False

# Shagovoe ogranichenie
def perform_move(field, key):
    currnt_position = field.index(Empty_mark)

    if key == 's' and currnt_position >= 12:
        raise IndexError('Can\'t move down')
    if key == 'd' and currnt_position % 4 == 3:
        raise IndexError('Can\'t move right')
    if key == 'w' and currnt_position < 4:
        raise IndexError('Can\'t move up')
    if key == 'a' and currnt_position % 4 == 0:
        raise IndexError('Can\'t move left')
    delta = Moves[key]
    field[currnt_position], field[currnt_position + delta] = field[
        currnt_position + delta], field[currnt_position]
    return field


# Vvod polzovatelya , esli ne pravilno, vazvrashat vopros
def handle_user_input():
    while True:
        user_move = input('Please, select your move: w ⇧  a ⇦  s ⇩  d ⇨  ')
        if user_move in Moves.keys():
            return user_move

def main():
    field = shuffle_field()
    #field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x'] ##TEST
    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)
    print(f'You Win {a}! CONGRATS !!!!!!!!')



if __name__ == '__main__':

    main()