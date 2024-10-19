import os
import pathlib
import sys
import math

def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split(",")]

class IntComp:
    def __init__(self, numbers):
        self.program = numbers
        self.cursor = 0

    def read_pos(self):
        return self.program[self.cursor]

    def read_at(self, pos):
        return self.program[pos]

    def read_params(self):
        self.cursor += 1
        op1 = self.read_at(self.read_pos())
        self.cursor += 1
        op2 = self.read_at(self.read_pos())
        self.cursor += 1
        dest = self.read_pos()
        return op1, op2, dest

    def do_add(self):
        op1, op2, dest = self.read_params()
        self.program[dest] = op1 + op2

    def do_mult(self):
        op1, op2, dest = self.read_params()
        self.program[dest] = op1 * op2

    def run(self):
        op_code = self.read_pos()
        while op_code != 99:
            if op_code == 1:
                try:
                    self.do_add()
                except IndexError:
                    break
            if op_code == 2:
                try:
                    self.do_mult()
                except IndexError:
                    break
            self.cursor += 1
            op_code = self.read_pos()

        self.cursor = 0
        return self.read_pos()

    def set_state(self, noun, verb):
        self.program[1] = noun
        self.program[2] = verb



def part1(numbers):
    comp = IntComp(numbers)
    comp.set_state(12, 2)
    return comp.run()


def part2(numbers):
    for i in range(99):
        for j in range(99):
            comp = IntComp(numbers.copy())
            comp.set_state(i, j)
            result = comp.run()
            if result == 19690720:
                return 100 * i + j



if __name__ == "__main__":
    paths = sorted([f for f in os.listdir(".") if f.startswith("example.txt")])
    paths.append("input.txt")
    for path in paths:
        print(path)
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)
        print(part2(numbers))
