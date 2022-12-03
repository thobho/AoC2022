from utils import read_input

input = read_input(1)
raw_chunks = input.split("\n\n")

chunks = [[int(i) for i in chunk.split("\n")] for chunk in raw_chunks]

calories_sums = [sum(chunk) for chunk in chunks]
calories_sums.sort()

print(sum(calories_sums[-3:]))
