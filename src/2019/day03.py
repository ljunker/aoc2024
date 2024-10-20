import os
import pathlib


def parse(puzzle_input):
    return [line for line in puzzle_input.split()]


directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def part1(wires):
    intersections = calc_intersections(wires)
    closest = 1000000000
    for inter in intersections:
        dist = abs(inter[0]) + abs(inter[1])
        if dist < closest:
            closest = dist
    return closest


def calc_intersections(wires):
    all_coords = []
    for wire in wires:
        coords = set()
        current = (0, 0)
        directives = [directive for directive in wire.split(",")]
        for directive in directives:
            direction, amount = directive[0], int(directive[1:])
            for i in range(amount):
                current = (current[0] + directions[direction][0], current[1] + directions[direction][1])
                coords.add(current)
        all_coords.append(coords)
    intersections = all_coords[0].intersection(all_coords[1])
    return intersections


def calc_length_to_intersection(inter, wire):
    length = 0
    current = (0, 0)
    directives = [directive for directive in wire.split(",")]
    for directive in directives:
        direction, amount = directive[0], int(directive[1:])
        for i in range(amount):
            current = (current[0] + directions[direction][0], current[1] + directions[direction][1])
            length += 1
            if inter == current:
                return length
    return length


def part2(wires):
    intersections = calc_intersections(wires)
    lengths = []
    for inter in intersections:
        length0 = calc_length_to_intersection(inter, wires[0])
        length1 = calc_length_to_intersection(inter, wires[1])
        lengths.append(length0 + length1)
    return sorted(lengths)[0]


if __name__ == "__main__":
    paths = sorted([f for f in os.listdir(".") if f.startswith("example0")])
    paths.append("input.txt")
    for path in paths:
        print(path)
        puzzle_input = pathlib.Path(path).read_text().strip()

        lines = parse(puzzle_input)
        print(part2(lines))
