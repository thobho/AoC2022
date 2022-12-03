from utils import read_input

input = read_input(2)

extra_points = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3  # scissors
}

### part 1
game_rules = {
    'A': { # rock
        'X': 3, # rock
        'Y': 6, # paper
        'Z': 0, # scisors
    },
    'B': { # paper
        'X': 0, # rock
        'Y': 3, # paper
        'Z': 6, # scisors
    },
    'C': { # scissors
        'X': 6, # rock
        'Y': 0, # paper
        'Z': 3, # scisors
    },
}

def play_game(game):
    [his_input, my_input] = game.split(" ") 
    game_point = game_rules[his_input][my_input]
    extra_point = extra_points[my_input]
    return game_point + extra_point

partial_results = [play_game(game) for game in input.split("\n")] 
print(sum(partial_results))

### part 2
game_rules = {
    'A': { # rock
        'X': ('C', 0), # lose
        'Y': ('A', 3), # draw
        'Z': ('B', 6), # win
    },
    'B': { # paper
        'X': ('A', 0), # lose
        'Y': ('B', 3), # draw
        'Z': ('C', 6), # win
    },
    'C': { # scissors
        'X': ('B', 0), # lose
        'Y': ('C', 3), # draw
        'Z': ('A' , 6), # win
    },
}

def play_game_2(game):
    [his_input, expected_result] = game.split(" ")
    (my_input, my_points) = game_rules[his_input][expected_result]
    extra_point = extra_points[my_input]
    return my_points + extra_point

partial_results = [play_game_2(game) for game in input.split("\n")] 
print(sum(partial_results))