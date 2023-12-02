# Roman Ramirez
# ADVENT OF CODE 2023
# DAY 02

import numpy as np

def get_input(filename):
    my_input = []
    with open(filename,'r') as f:
        for line in f:
            my_input.append(line.strip())
    return my_input

def part1():
    text = get_input('input.txt')
    
    game_list = list()
    for game in text:
        _,items = game.split(": ")
        set_list = list()
        for set in items.split('; '):
            set_nums = [0, 0, 0]
            for cubes in set.split(", "):
                if 'red' in cubes:
                    set_nums[0] += int(cubes.replace(" red",""))
                elif 'green' in cubes:
                    set_nums[1] += int(cubes.replace(" green",""))
                elif 'blue' in cubes:
                    set_nums[2] += int(cubes.replace(" blue",""))
            set_list.append(set_nums)
        game_list.append(set_list)

    checker = np.array([12, 13, 14])
    
    total = 0
    for (i, game) in enumerate(game_list):
        game_number = i + 1
        valid_game = True
        for set in game:
            if not all([c <= 0 for c in np.array(set) - checker]):
                valid_game = False
        if valid_game: total += game_number
    print(total)
        
def part2():
    text = get_input('input.txt')
    
    game_list = list()
    for game in text:
        _,items = game.split(": ")
        set_list = list()
        for set in items.split('; '):
            set_nums = [0, 0, 0]
            for cubes in set.split(", "):
                if 'red' in cubes:
                    set_nums[0] += int(cubes.replace(" red",""))
                elif 'green' in cubes:
                    set_nums[1] += int(cubes.replace(" green",""))
                elif 'blue' in cubes:
                    set_nums[2] += int(cubes.replace(" blue",""))
            set_list.append(set_nums)
        game_list.append(set_list)
    
    total = 0
    for (i, game) in enumerate(game_list):
        power = 1
        for elem in np.array(game).max(axis=0):
            power *= elem
        total += power
    print(total)
                


if __name__ == '__main__':
    part2()