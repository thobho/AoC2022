from utils import read_input 

input = read_input(9)

class Pos:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"[{self.x},{self.y}]"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Rope:
    def __init__(self, len, start_x=0, start_y=0) -> None:
        self.head = Pos(start_x,start_y)
        self.tail = [Pos(start_x,start_y) for i in range(len - 1)]
        self.tail_visited = {Pos(start_x,start_y)}
    
    def __str__(self) -> str:
        tail_str = "".join([str(pos) for pos in self.tail])
        return f"{self.head}{tail_str}"

    def move_head(self, instruction):
        [direction, distance] = instruction.split(" ")
        for _ in range(int(distance)):
            self._move_head_once(direction)
            for i in range(len(self.tail)):
                current = self.tail[i]
                if i == 0:
                    previous = self.head
                else:
                    previous = self.tail[i-1]
                current_afeter_move = self._move_tail(current, previous)
                self.tail[i] = current_afeter_move
                self.tail_visited.add(Pos(self.tail[-1].x, self.tail[-1].y))
        self.print(10,10)

    def _move_head_once(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == 'U':
            self.head = Pos(x, y + 1)
        if direction == 'D':
            self.head = Pos(x, y - 1)
        if direction == 'R':
            self.head = Pos(x + 1, y)
        if direction == 'L':
            self.head = Pos(x - 1, y)
    
    def _move_tail(self, current, prev):
        c = current
        p = prev

        if abs(p.x - c.x) <= 1 and abs(p.y - c.y) <= 1:
            return current
        if c.y - p.y == 2: # tail to up
            if c.x - p.x == 2:
                return Pos(p.x + 1, p.y + 1)
            if c.x - p.x == -2:
                return Pos(p.x - 1, p.y + 1)
            return Pos(p.x, p.y + 1)
        if c.y - p.y == -2: # tail to down
            if c.x - p.x == 2:
                return Pos(p.x + 1, p.y - 1)
            if c.x - p.x == -2:
                return Pos(p.x - 1, p.y - 1) 
            return Pos(p.x, p.y - 1)
        if c.x - p.x == 2: # tail to right
            return Pos(p.x + 1,p.y)
        if c.x - p.x == -2: # tail to left
            return Pos(p.x - 1,p.y)

    
    def _get_print_sign(self, x, y):
        if x == self.head.x and y == self.head.y:
            return 'H '
        for i in range(len(self.tail)):
            node = self.tail[i]
            if x == node.x and y == node.y:
                return f"{str(i + 1)} "
        return '. '
    
    def print(self, width, height):
        for w in range(width):
            print("\n")
            for h in range(height):
                print(self._get_print_sign(h, w), end="")
        print("\n= = = = = = = = = =")


rope = Rope(10,0,0)

for line in input.split("\n"):
    rope.move_head(line)

for p in rope.tail_visited:
    print(p)

print(len(rope.tail_visited))