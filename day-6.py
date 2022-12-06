from utils import read_input 

input = read_input(6)
UNIQUE_START_COUNT=14

def find_start(message):
    for i in range(len(message) - UNIQUE_START_COUNT):
        chunk = message[i:i+UNIQUE_START_COUNT]
        if len(set(chunk)) == UNIQUE_START_COUNT:
            return i + UNIQUE_START_COUNT

answer = find_start(input)

print(answer)