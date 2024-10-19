import os
import pathlib
import sys
import math

def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split()]


def part1(numbers):
    sum = 0
    for num1 in numbers:
        num1 /= 3
        num1 = math.floor(num1)
        num1 -= 2
        sum += num1
    return sum

def calc_fuel_for_one_number(number):
    fuelSum = 0
    needsFuel = part1([number])
    fuelSum += needsFuel
    while needsFuel > 0:
        needsFuel = part1([needsFuel])
        if needsFuel > 0:
            fuelSum += needsFuel
    return fuelSum

def part2(numbers):
    fuel_sum = 0
    for num in numbers:
        fuel_sum += calc_fuel_for_one_number(num)
    return fuel_sum



if __name__ == "__main__":
    paths = sorted([f for f in os.listdir(".") if f.startswith("example.txt")])
    paths.append("input.txt")
    for path in paths:
        print(path)
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)
        print(part2(numbers))
