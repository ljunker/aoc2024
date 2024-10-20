import os
import pathlib


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split(",")]


def part1(numbers):
    pass


def part2(numbers):
    pass


if __name__ == "__main__":
    paths = sorted([f for f in os.listdir(".") if f.startswith("example.txt")])
    # paths.append("input.txt")
    for path in paths:
        print(path)
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)
        print(part1(numbers))
