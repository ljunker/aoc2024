from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=2)

print(puzzle.input_data[:20])

for n, example in enumerate(puzzle.examples):
    f = open("example.txt" + str(n) + ".txt", "w")
    f.write(example.input_data)
    f.close()

f = open("input.txt", "w")
f.write(puzzle.input_data)
f.close()
