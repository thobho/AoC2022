from utils import read_input 
import re

input = read_input(5)

[stacks_input,instructinos_input] = input.split("\n\n")

def extract_stack_at_index(stack_input_lines, index):
    result = []
    for line in stack_input_lines:
        crate_label = line[index * 4 : index * 4 + 4][1]
        if crate_label.strip():
            result.append(crate_label)
    return result

def extract_stacks(stack_input):
    stack_input_lines = stack_input.split("\n")
    stack_lines = stack_input_lines[0 : len(stack_input_lines)-1]
    stack_lines.reverse()
    stack_indices = stack_input_lines[-1]
    last_index = int(stack_indices[-2])
    return [extract_stack_at_index(stack_lines, column_index) for column_index in range(0, last_index)]
    
def extract_moves(instructions_input):
    return [[int(char) for char in re.findall(r'\d+',line)] for line in instructions_input.split("\n")]


stacks = extract_stacks(stacks_input)
moves = extract_moves(instructinos_input)

# part 1
# def perform_move(stacks, move):
#     [crates_count_to_move, start, end] = move
#     for _ in range(0, crates_count_to_move):
#         element = stacks[start - 1].pop()
#         stacks[end - 1].append(element)
#     return stacks

# part 2
def pop_n(list, n):
    split = len(list) - n
    rest = list[split:len(list)]
    del list[len(list) - n:]
    return rest

def perform_move(stacks, move):
    [crates_count_to_move, start, end] = move
    elements = pop_n(stacks[start - 1], crates_count_to_move)
    stacks[end - 1].extend(elements)
    return stacks
# end of part 2

def move(stacks, moves):
    for move in moves:
        stacks = perform_move(stacks, move)
    return stacks

def extract_tops(stacks):
    tops = [stack[-1] for stack in stacks]
    return ''.join(tops)

move_result = move(stacks, moves)
tops = extract_tops(move_result)

print(tops)

