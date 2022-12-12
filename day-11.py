import primefac 
import functools

# TODO: Part 2 not correct

class Monkey:
    
    def reduce_worries(x):
        # return x // 3
        return x % 9699690

    def __init__(self, items, operation, test) -> None:
        self.items = items
        self.test = test
        self.operation = operation
        self.bussiness = 0
    
    def inspect_all_items(self):
        result = []
        for item_index in range(0, len(self.items)):
            item_with_next_monkey = self.inspect_next_item(item_index)
            result.append(item_with_next_monkey)
        self.items = []
        return result
    
    def inspect_next_item(self, item_index):
        if not len(self.items):
            return None
        next_item = self.items[item_index]
        after_operation = self.operation(next_item)
        item_reduced_worries = Monkey.reduce_worries(after_operation)
        (predicate, next_monkeys) = self.test
        self.bussiness += 1
        if predicate(item_reduced_worries):
            return (item_reduced_worries, next_monkeys[0])
        else:
            return (item_reduced_worries, next_monkeys[1])
    
    def add_item(self, item):
        self.items.append(item)

    def __str__(self) -> str:
        return str(self.items)

# test data
# m0 = Monkey([79, 98], lambda x: x * 19, (lambda x: x % 23 == 0, [2,3]))
# m1 = Monkey([54, 65, 75, 74], lambda x: x + 6, (lambda x: x % 19 == 0, [2,0]))
# m2 = Monkey([79, 60, 97], lambda x: x * x, (lambda x: x % 13 == 0, [1,3]))
# m3 = Monkey([74], lambda x: x + 3, (lambda x: x % 17 == 0, [0,1]))
# monkeys = [m0,m1,m2,m3]



# data
m0 = Monkey([56, 52, 58, 96, 70, 75, 72], lambda x: x * 17, (lambda x: x % 11 == 0, [2,3]))
m1 = Monkey([75, 58, 86, 80, 55, 81], lambda x: x + 7, (lambda x: x % 3 == 0, [6,5]))
m2 = Monkey([73, 68, 73, 90], lambda x: x * x, (lambda x: x % 5 == 0, [1,7]))
m3 = Monkey([72, 89, 55, 51, 59], lambda x: x + 1, (lambda x: x % 7 == 0, [2,7]))
m4 = Monkey([76, 76, 91], lambda x: x * 3, (lambda x: x % 19 == 0, [0,3]))
m5 = Monkey([88], lambda x: x + 4, (lambda x: x % 2 == 0, [6,4]))
m6 = Monkey([64, 63, 56, 50, 77, 55, 55, 86], lambda x: x + 8, (lambda x: x % 13 == 0, [4,0]))
m7 = Monkey([79, 58], lambda x: x + 6, (lambda x: x % 17 == 0, [1,5]))

monkeys = [m0, m1,m2,m3,m4,m5,m6, m7]

def round(monkeys, current_monkey_index):
    current_monkey = monkeys[current_monkey_index]
    items_with_next_monkeys = current_monkey.inspect_all_items()
    
    for item_with_next_monkey in items_with_next_monkeys:
        (item, next_monkey_index) = item_with_next_monkey
        monkeys[next_monkey_index].add_item(item)

for round_index in range(0,20):
    for monkey_index in range(0, len(monkeys)):
        round(monkeys, monkey_index)
    print(f"\nRound {round_index}", end=":\n")
    for m in monkeys:
        print(m)

bussiness_scores = [m.bussiness for m in monkeys]
sorted_business_scores = sorted(bussiness_scores, reverse=True)
print(bussiness_scores)
print(sorted_business_scores[0] * sorted_business_scores[1])
common_divisor = functools.reduce(lambda x,y: x * y, [2,3,5,7,11,13,17,19])
# common_divisor = functools.reduce(lambda x,y: x * y, [13,17,19,23])
print(common_divisor)