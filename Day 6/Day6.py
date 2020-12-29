import collections

with open("input6.txt") as f:
    input = f.readlines()

input = [x.strip() for x in input]
input.append("")

answers = ""
part1answers = 0
counter = 0
part2answers = 0

for line in input:
    if line != "":
        counter += 1
        answers = answers + line
    else:
        frequencies = collections.Counter(answers)
        repeated = {}

        for key, value in frequencies.items():
            if value == counter:
                repeated[key] = value

        part2answers = part2answers + len(repeated)
        part1answers = part1answers + len(set(answers))
        answers = ""
        counter = 0

print(part1answers)
print(part2answers)

