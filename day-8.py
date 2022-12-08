from utils import read_input 

input = read_input(8)

# [row][col]
trees = [[int(tree) for tree in line] for line in input.split("\n")]

# part 1
def safe_max(numbers):
    if len(numbers) == 0:
        return -1
    return max(numbers)

def get_highest_horizontal(trees, row, col):
    tree_row = trees[row]
    left = tree_row[0:col]
    right = tree_row[col+1:len(tree_row)]
    return (safe_max(left), safe_max(right))

def get_vertical(trees, row, col):
    tree_col = [row[col] for row in trees]
    upper = tree_col[0:row]
    lower = tree_col[row+1:len(tree_col)]
    return (safe_max(upper), safe_max(lower))

def is_visible(trees, row, col):
    tree_height = trees[row][col]
    (left, right) = get_highest_horizontal(trees, row, col)
    (upper, lower) = get_vertical(trees, row, col)
    return tree_height > left or tree_height > right or tree_height > upper or tree_height > lower

def count_visibles(trees):
    counter = 0
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            if is_visible(trees, i, j):
                counter = counter + 1
    return counter

print(count_visibles(trees))

# part 2
def get_horizontal(trees, row, col):
    tree_row = trees[row]
    left = tree_row[0:col]
    right = tree_row[col+1:len(tree_row)]
    return (list(reversed(left)), right)

def get_vertical(trees, row, col):
    tree_col = [row[col] for row in trees]
    upper = tree_col[0:row]
    lower = tree_col[row+1:len(tree_col)]
    return (list(reversed(upper)), lower)

def get_visible_trees(tree_height, tree_list):
    result = 0
    for tree in tree_list:
        if tree >= tree_height:
            return result + 1
        result = result + 1
    return result


def calculate_scenic_score(trees, row, col):
    (left, right) = get_horizontal(trees, row, col)
    (up, down) = get_vertical(trees, row, col)
    l = get_visible_trees(trees[row][col], left)
    r = get_visible_trees(trees[row][col], right)
    u = get_visible_trees(trees[row][col], up)
    d = get_visible_trees(trees[row][col], down)
    return l * r* u *d

def get_highest_scenic_score(trees):
    highest = 0
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            score = calculate_scenic_score(trees, i, j)
            if score > highest:
                highest = score
    return highest

print(get_highest_scenic_score(trees))