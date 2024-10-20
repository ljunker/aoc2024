import os
import pathlib


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split(",")]


def number_to_pairs(number):
    digits = [int(d) for d in str(number)]
    return [(digits[i], digits[i + 1]) for i in range(len(digits) - 1)]


def only_increasing_digits(digit_pairs):
    return all([i[0] <= i[1] for i in digit_pairs])


def six_digit_number(number):
    return len(str(number)) == 6


def exactly_two_adjacent_are_same(digit_pairs):
    count = 0
    for pair in digit_pairs:
        if pair[0] == pair[1]:
            count += 1
    return count >= 1


def part1():
    count = 0
    for i in range(240298, 785956):
        digit_pairs = number_to_pairs(i)
        if only_increasing_digits(digit_pairs) and six_digit_number(i) and exactly_two_adjacent_are_same(digit_pairs):
            count += 1
    return count


def digits_only_two_groups(digits):
    last = "blub"
    length = 0
    for d in digits:
        if d != last:
            if length == 1:
                return True
            length = 0
            last = d
        else:
            length += 1
    if length == 1:
        return True
    return False


def part2():
    count = 0
    for i in range(240298, 785956):
        digit_pairs = number_to_pairs(i)
        if only_increasing_digits(digit_pairs) and six_digit_number(i) and digits_only_two_groups(str(i)):
            count += 1
    return count


if __name__ == "__main__":
    print(part2())
