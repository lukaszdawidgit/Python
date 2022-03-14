""" Lotto game"""
from random import sample
ALL_NUMBERS = range(1, 50)
COST_OF_DRAW = 3

def random_numbers():
    """
    Generate 6 numbers out of 49
    @return:
    list[]
    """
    return sample(ALL_NUMBERS, k = 6)

def play_for_5():
    """
    for list[i] add +1 to xyz, when xyz >3, stop
    clear on each loop
    """

def play_until_you_win(my_numbers, fake_random_numbers):
    """
    while loop, check how many attemps require to guess  6 numbers out of 49
    @param: my_numbers (list) user numbers
    @return: game_counter (int) to get amount of attempts
    """
    winning_numbers = []
    game_counter = 0
    while winning_numbers != my_numbers:
        winning_numbers = fake_random_numbers
        winning_numbers.sort()
        game_counter += 1
    print(winning_numbers)
    return game_counter


if __name__ == '__main__':
    MY_NUMBERS = [1, 13, 25, 36, 39, 49]
    COUNTER = play_until_you_win(MY_NUMBERS, random_numbers())
    TOTAL_COST = COUNTER * COST_OF_DRAW
    print(f'It costed: {TOTAL_COST:,} zl')
