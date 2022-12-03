def read_input(day):
    filename = "day-%s.txt" % day
    with open(filename) as f:
        lines = f.read()
    return lines


def split_by_step(input, step):
    result = []
    for i in range(0, len(input), step):
        result.append(input[i:i+step])
    return result