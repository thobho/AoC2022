from utils import read_input 

input = read_input(7)

class Node:
    def __init__(self, name, size, isFile, childs, parent):
        self.name = name
        self.size = size
        self.isFile = isFile
        self.childs = childs
        self.parent = parent
    
    def __str__(self) -> str:
        return f"{self.name} | {self.size}"

    def add_child(self, child):
        self.childs.append(child)
    
    def go_to_child(self, dir_name):
        result = list(filter(lambda x: x.name == dir_name, self.childs))
        if len(result) == 0:
            raise Exception
        return result[0]
    
    def go_to_parent(self):
        return self.parent

input_lines = input.split("\n")
root_input_line = input_lines[0]
rest_input_lines = input_lines[1:]

root_file = Node(root_input_line[4:], 0, False, [], None)

def process_input(current_node):
    for command in rest_input_lines[1:]:
        if command.startswith("dir"):
            new_dir = Node(command[4:], 0, False, [], current_node)
            current_node.add_child(new_dir)
        elif command == "$ ls":
            continue
        elif command == "$ cd ..":
            current_node = current_node.go_to_parent()
        elif command.startswith("$ cd") and command != "$ cd ..":
            current_node = current_node.go_to_child(command[5:])
        else:
            [size, name] = command.split(" ")
            new_file = Node(name, int(size), True, None, current_node)
            current_node.add_child(new_file)

def calculate_sizes(current_node):
    if current_node.isFile:
        return current_node.size
    else:
        nodes_sizes_elems = [calculate_sizes(child) for child in current_node.childs]
        nodes_sizes = sum(nodes_sizes_elems)
        current_node.size = nodes_sizes
        return nodes_sizes

def all_dir_nodes(current_node, accu):
    for child in current_node.childs:
        if not child.isFile:
            accu.append(child)
            all_dir_nodes(child, accu)
    return accu

def find_small(current_node, threshold, accu):
    for child in current_node.childs:
        if child.size < threshold and not child.isFile:
            accu.append(child)
        if not child.isFile:    
            find_small(child, threshold, accu)
    return accu

process_input(root_file)
calculate_sizes(root_file)
small_nodes = find_small(root_file, 100000, [])
small_sizes = [node.size for node in small_nodes]
#print(sum(small_sizes))

#part 2

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
current_size = calculate_sizes(root_file)
free_size = TOTAL_SPACE - current_size
space_to_be_cleaned = REQUIRED_SPACE - free_size
all_nodes = all_dir_nodes(root_file, [])
all_sizes = [node.size for node in all_nodes]
potentially_to_delete = list(filter(lambda x: x>=space_to_be_cleaned, all_sizes))
to_delete_size = min(potentially_to_delete)
print(to_delete_size)