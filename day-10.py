from utils import read_input

input_lines = read_input(10).split("\n")

ADD_X_CYCLES = 2

def parse_command(input_line):
    if input_line == "noop":
        return ("noop", None)
    [command, arg] = input_line.split(" ")
    return (command, int(arg))

def print_pixel(cycle, x):
    break_lines = {40,80,120,160,200}
    pos = cycle - 1

    if abs(pos % 40 - x)<=1:
        print("#", end="")
    else:
        print(".", end="")
    if cycle in break_lines:
        print("\n")


def next_state(machine_state, program):
    check_points = {20,60,100,140,180,220}
    (cycle, x, addx_cointer, program_pointer, chceck_strength) = machine_state
    (command, arg) = program[program_pointer]

    if cycle in check_points:
        chceck_strength.append(cycle * x)
    
    
    print_pixel(cycle,x)

    if command == 'noop':
        return (cycle + 1, x, 1, program_pointer + 1, chceck_strength)

    if command == 'addx':
        if addx_cointer == ADD_X_CYCLES:
            return (cycle + 1, x + arg, 1, program_pointer + 1, chceck_strength)
        else:
            return (cycle + 1, x, addx_cointer + 1, program_pointer, chceck_strength)


def run(input_lines):
    commands = [parse_command(line) for line in input_lines]
    states = []
    state = (1, 1, 1, 0, [])
    while state[3] < len(commands):
        (cycle, x, addx_cointer, program_pointer, chceck_strength) = state
        states.append((cycle, x))
        state = next_state(state, commands)
    return states

signals = run(input_lines)

# for s in signals:
#     (c,x) = s

#     if abs(c-x)<=1:
#         print("#", end="")
#     else:
#         print(".", end="")
    
#     if c % 40 ==0:
#         print("\n")


    

