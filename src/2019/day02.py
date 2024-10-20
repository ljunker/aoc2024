import os
import pathlib
from IntComp import IntComp


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split(",")]


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
