from utils import read_input 

input = read_input(4)

def exract_pairs(raw_input):
    print(raw_input)
    [first_section, second_section] = raw_input.split(",")
    (a,b) = first_section.split("-")
    (c,d) = second_section.split("-")
    return ((int(a),int(b)), (int(c),int(d)))

pairs = [exract_pairs(line) for line in input.split("\n")]

# part 1
def is_full_overlap(first, second):
    (first_start,first_end) = first
    (second_start,second_end) = second
    
    is_first_longer_or_equal = first_end - first_start >= second_end - second_start

    if is_first_longer_or_equal:
        return first_start <= second_start and first_end >= second_end
    
    return second_start <= first_start and second_end >= first_end

overlapping = [is_full_overlap(pair[0], pair[1]) for pair in pairs]
print(sum(overlapping))

# part 2

def is_overlap(first, second):
    (first_start,first_end) = first
    (second_start,second_end) = second
    first_range = range(first_start, first_end + 1)
    second_range = range(second_start, second_end + 1)
    first_set = set(first_range)
    second_set = set(second_range)
    overlapping_sectors = first_set & second_set
    return len(overlapping_sectors) != 0

overlapping = [is_overlap(pair[0], pair[1]) for pair in pairs]
print(sum(overlapping))
