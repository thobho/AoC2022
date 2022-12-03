from utils import read_input, split_by_step

input = read_input(3)

LOWER_CASE_PRIORITY_ASCII_OFFSET = 96
UPPER_CASE_PRIORITY_ASCII_OFFSET = 38

def get_priority_number(char):
    if ord(char) >= 97:
        return ord(char) - LOWER_CASE_PRIORITY_ASCII_OFFSET
    else:
        return ord(char) - UPPER_CASE_PRIORITY_ASCII_OFFSET


def calculate_priority(items):
    item_count = len(items)
    first_half = set(items[:item_count//2])
    second_half = set(items[item_count//2:])
    duplicate = first_half.intersection(second_half)
    return get_priority_number(next(iter(duplicate)))

splitted_input = input.split("\n")

prioriteis = [calculate_priority(item) for item in splitted_input]

print(sum(prioriteis))

# part 2

groups = split_by_step(input.split('\n'), 3)

def find_stickers(group):
    items_sets = [set(items) for items in group]
    return items_sets[0].intersection(items_sets[1]).intersection(items_sets[2])

stickers = [find_stickers(group) for group in groups]
priority_numbers = [get_priority_number(next(iter(sticker))) for sticker in stickers]

print(sum(priority_numbers))